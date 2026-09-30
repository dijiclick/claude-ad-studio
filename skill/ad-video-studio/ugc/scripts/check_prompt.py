#!/usr/bin/env python3
"""Lint an AI UGC video prompt against the course's realism layers and ad-safety rules.

Usage: check_prompt.py PROMPT_FILE [--seconds 8] [--lang tr|en] [--presenter]
  --seconds    clip length the dialogue must fit (default 8)
  --lang       dialogue language: pace differs (tr ≈ 2.4 words/s, en ≈ 3 words/s)
  --presenter  AI person must not testify (no first-person "I used / I bought")
Exit 0 = no FAIL (WARNs are advice). Prints one line per check.
"""
import argparse, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("file"); ap.add_argument("--seconds", type=float, default=8)
ap.add_argument("--lang", default="en"); ap.add_argument("--presenter", action="store_true")
a = ap.parse_args()
p = open(a.file).read()
low = p.lower()
res = []  # (level, msg)

def need(level, label, *patterns):
    ok = any(re.search(x, low) for x in patterns)
    res.append(("PASS" if ok else level, label))

# Core layers (FAIL if missing — each one removes an AI tell)
need("FAIL", "camera = phone (iPhone / smartphone / UGC phone footage)", r"iphone", r"smartphone", r"phone (front )?camera")
need("FAIL", "camera motion stated (handheld / static / propped / mounted)", r"handheld", r"static", r"locked-off", r"propped", r"mounted", r"tripod")
need("FAIL", "a named light source", r"(window|vanity|overhead|lamp|daylight|sunlight|ring light|golden hour|tungsten|fluorescent)[^.]{0,40}light|light (from|through|coming)", r"\d{4}\s?k\b")
need("FAIL", "skin realism (pores / natural texture)", r"pores", r"skin texture", r"natural texture")
need("FAIL", "diegetic audio (mic / room sound)", r"\bmic\b", r"microphone", r"ambien", r"room (tone|echo|acoustic)", r"earphone")
need("FAIL", "no on-screen text in the generation", r"no (text|subtitles|captions)", r"subtitles", r"captions")
need("WARN", "performance beats tied to words (on the word / on \"…\")", r"on the word", r"on [\"“'][^\"”']+[\"”']", r"\bbeat\b", r"\d(\.\d)?\s?s(ec)?\b.*(tilts|leans|points|raises|smiles|nods)")
need("WARN", "one lived-in background detail", r"background", r"behind (her|him)")
need("WARN", "vertical 9:16 / 720x1280", r"9:16", r"720x1280", r"vertical")
need("WARN", "'no music' / one-take", r"no music", r"one[- ]take", r"no cuts")
need("WARN", "beauty-filter negatives", r"beauty filter", r"skin smoothing", r"airbrush", r"waxy")
need("WARN", "phone-file realism (IMG_####.MOV)", r"img_\d+\.mov")

# Contradictions
selfie = re.search(r"selfie|arm'?s length", low)
static = re.search(r"static locked-off|locked-off shot", low)
propped = re.search(r"propped|mounted|tripod|on (the|a) (table|counter|dashboard)", low)
if selfie and static and not propped:
    res.append(("WARN", "selfie at arm's length + 'static locked-off' → an unmoving selfie looks AI; use handheld micro-jitter or say the phone is propped"))
if re.search(r"handheld", low) and re.search(r"negative[^\n]*camera shake|camera shake[^\n]*negative", low):
    res.append(("WARN", "handheld prompt lists 'camera shake' as a negative — drop it"))
if re.search(r"\b(label|pouch|jar|bottle|bag|box|package|packaging)\b", low) and not re.search(r"mirror", low):
    res.append(("WARN", "product/label present: add 'label text reads correctly left to right (not mirrored)'"))

# Length
if len(p) > 5000:
    res.append(("FAIL", f"prompt is {len(p)} chars (> 5,000 — keep video prompts compact; the course capped at 5,000)"))
else:
    res.append(("PASS", f"prompt length {len(p)} chars"))

# Dialogue vs duration
m = re.search(r"(dialogue[^\n]*|exact script[^\n]*|\bshe says|\bhe says|\bsays)\s*:?", p, re.I)
seg = p[m.end():] if m else p
end = re.search(r"\n\s*(audio|ugc authenticity|pace:|negatives|quality control|cinematography)", seg, re.I)
seg = seg[:end.start()] if end else seg
full = re.findall(r'^\s*"(.+)"\s*$', seg, re.M)  # a whole line in straight quotes = the spoken line (may contain “nested” quotes)
quotes = full or re.findall(r"[\"“]([^\"”\n]{3,})[\"”]", seg)
dialogue = " ".join(quotes) if m else (max(quotes, key=len) if quotes else "")
if dialogue:
    words = len(re.findall(r"\w+", dialogue))
    rate = 2.4 if a.lang == "tr" else 3.0
    lo, hi = rate * a.seconds * 0.7, rate * a.seconds * 1.1
    lvl = "PASS" if lo <= words <= hi else "WARN"
    tip = " — short: fine for a hook you cut after the line; else pad with throwaway words and cut them in the edit" if words < lo else (" — too long: split into another clip" if words > hi else "")
    res.append((lvl, f"dialogue {words} words for {a.seconds:g}s (fits ~{lo:.0f}–{hi:.0f}){tip} — \"{dialogue[:50]}…\""))
else:
    res.append(("WARN", "no quoted dialogue found (exact script in quotes?)"))

# Claims & policy
risky = [r"\binstant(ly)?\b", r"anında", r"saniyesinde", r"\bguarantee", r"garanti", r"\bcures?\b", r"tedavi eder",
         r"lose \d+", r"\d+\s?(kg|lbs?) (lose|ver)", r"\bdr\.\s", r"\bdoctor\b", r"\bdoktor\b", r"watermark remov", r"remove (the )?watermark"]
for r_ in risky:
    m = re.search(r_, low)
    if m:
        res.append(("WARN", f"risky claim/term '{m.group(0)}' — ad platforms & consumer law (no speed/medical/credential claims)"))
if a.presenter:
    for r_ in [r"\bi (used|bought|tried|ordered)\b", r"\bkulland[ıi]m\b", r"\bald[ıi]m\b", r"\bdenedim\b", r"\bsipariş ettim\b"]:
        m = re.search(r_, low)
        if m:
            res.append(("FAIL", f"presenter mode: first-person testimony '{m.group(0)}' — AI person must present, not testify"))

order = {"FAIL": 0, "WARN": 1, "PASS": 2}
for lvl, msg in sorted(res, key=lambda x: order[x[0]]):
    print(f"{lvl:4}  {msg}")
fails = sum(1 for l, _ in res if l == "FAIL")
print(f"\n{fails} FAIL, {sum(1 for l,_ in res if l=='WARN')} WARN")
sys.exit(1 if fails else 0)
