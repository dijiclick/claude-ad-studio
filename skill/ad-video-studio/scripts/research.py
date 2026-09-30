#!/usr/bin/env python3
"""Find what already WORKS in a market before making an ad.

    research.py OUT_DIR --country TR --query "indirim" [--query "..."] [--page "Brand"] [-n 40]

Pulls live ads from the public Meta Ad Library with `meta-ads-collector` (no API key),
downloads their videos/images, and ranks them by the two signals the Ad Library does
expose: how long an ad has been running (advertisers keep paying for what converts)
and how many copies of it run at once. Writes OUT_DIR/winners.md (ranked table) and a
6-frame contact sheet per top video so the ads can be read as images.
"""
import argparse, json, os, subprocess, sys
from datetime import datetime, timezone

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--country", default="TR")
ap.add_argument("--query", action="append", default=[])
ap.add_argument("--page", action="append", default=[], help="advertiser page name")
ap.add_argument("-n", type=int, default=40, help="ads per query/page")
ap.add_argument("--top", type=int, default=12)
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
media = os.path.join(a.out, "media")

runs = [("q", q) for q in a.query] + [("p", p) for p in a.page]
if not runs:
    sys.exit("give at least one --query or --page")
ads = {}
for kind, val in runs:
    out = os.path.join(a.out, f"raw-{kind}-{abs(hash(val)) % 10**8}.json")
    cmd = ["meta-ads-collector", "-c", a.country, "-n", str(a.n), "--download-media", "--media-dir", media,
           "-o", out, "--no-proxy", "--deduplicate"]
    cmd += ["-q", val] if kind == "q" else ["--page-name", val]
    print("collect:", val, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode or not os.path.exists(out):
        print("  failed:", (r.stderr or r.stdout)[-300:]); continue
    for ad in json.load(open(out)).get("ads", []):
        ads[ad["id"]] = ad

now = datetime.now(timezone.utc)
def days(ad):
    s = ad.get("delivery_start_time")
    if not s: return 0
    try: d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError: return 0
    if d.tzinfo is None: d = d.replace(tzinfo=timezone.utc)
    return max(0, (now - d).days)

rows = []
for ad in ads.values():
    c = (ad.get("creatives") or [{}])[0]
    vid = next((os.path.join(media, f) for f in sorted(os.listdir(media)) if f.startswith(ad["id"]) and f.endswith("_video_hd.mp4")), None) if os.path.isdir(media) else None
    copies = ad.get("collation_count") or 1
    rows.append({"id": ad["id"], "page": (ad.get("page") or {}).get("name", ""), "days": days(ad), "copies": copies,
                 "active": ad.get("is_active"), "text": (c.get("body") or c.get("title") or "").replace("\n", " ")[:140],
                 "video": vid, "image_url": c.get("image_url"), "url": ad.get("ad_snapshot_url") or ad.get("snapshot_url") or ""})
# longevity first, then how many variants the advertiser keeps alive
rows.sort(key=lambda r: (r["days"] * (1 + 0.25 * (r["copies"] - 1))), reverse=True)

sheets = os.path.join(a.out, "sheets"); os.makedirs(sheets, exist_ok=True)
lines = [f"# Winners — {', '.join(v for _, v in runs)} ({a.country}), {now:%Y-%m-%d}", "",
         "| # | advertiser | days running | copies | video | opening copy |", "|---|---|---|---|---|---|"]
for i, r in enumerate(rows[: a.top], 1):
    sheet = ""
    if r["video"]:
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", r["video"]],
                             capture_output=True, text=True).stdout.strip() or "10"
        sheet = os.path.join(sheets, f"{i:02d}-{r['id']}.png")
        step = max(float(dur) / 6, 0.5)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", r["video"], "-vf",
                        f"fps=1/{step:.2f},scale=240:-1,tile=6x1", "-frames:v", "1", sheet])
    if not sheet and r.get("image_url"):
        # catalog / static ads: the collector saves no media for them, but the creative has an image URL
        sheet = os.path.join(sheets, f"{i:02d}-{r['id']}.jpg")
        try:
            import urllib.request
            urllib.request.urlretrieve(r["image_url"], sheet)
        except Exception:
            sheet = ""
    lines.append(f"| {i} | {r['page']} | {r['days']} | {r['copies']} | {os.path.basename(sheet) if sheet else '—'} | {r['text']} |")
open(os.path.join(a.out, "winners.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
