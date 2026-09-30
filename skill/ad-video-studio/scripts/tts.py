#!/usr/bin/env python3
"""ElevenLabs v3 voiceover with word timings.

    TTS_TEXT="[excited] ..." python3 tts.py OUT_PREFIX [--voice VOICE_ID] [--lang tr]

Writes OUT_PREFIX.mp3 + OUT_PREFIX.json and prints every word with its start-end time,
which is what the composition's scene/caption timings are built from. Audio tags like
[excited] are allowed in the text; they are not spoken.
Key: $ELEVENLABS_API_KEY, else ELEVENLABS_API_KEY= in the skill's .env, else ~/Tools/OpenMontage/.env.
"""
import argparse, base64, json, os, sys, urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--voice", default="cbqdgvVi3C6sgxIWpqIh")  # Füsun Tuncer (TR female, Istanbul)
ap.add_argument("--lang", default="tr")
ap.add_argument("--stability", type=float, default=0.5)
a = ap.parse_args()

key = os.environ.get("ELEVENLABS_API_KEY")
for env in (os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"), os.path.expanduser("~/Tools/OpenMontage/.env")):
    if not key and os.path.exists(env):
        key = next((l.split("=", 1)[1].strip().strip('"') for l in open(env) if l.startswith("ELEVENLABS_API_KEY=")), None)
if not key:
    sys.exit("no ELEVENLABS_API_KEY")
text = os.environ.get("TTS_TEXT") or sys.exit("set TTS_TEXT")

body = {"text": text, "model_id": "eleven_v3", "language_code": a.lang,
        "voice_settings": {"stability": a.stability, "similarity_boost": 0.8}}
req = urllib.request.Request(
    f"https://api.elevenlabs.io/v1/text-to-speech/{a.voice}/with-timestamps?output_format=mp3_44100_192",
    data=json.dumps(body).encode(), headers={"xi-api-key": key, "Content-Type": "application/json"})
try:
    res = json.load(urllib.request.urlopen(req, timeout=180))
except urllib.error.HTTPError as e:
    sys.exit(e.read().decode()[:500])

open(a.out + ".mp3", "wb").write(base64.b64decode(res["audio_base64"]))
al = res["alignment"]
json.dump({"text": text, "alignment": al}, open(a.out + ".json", "w"), ensure_ascii=False)

words, cur, st, prev = [], "", None, 0.0
for ch, s, e in zip(al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]):
    if ch == " ":
        if cur:
            words.append((cur, st, prev)); cur = ""
        continue
    if not cur:
        st = s
    cur += ch; prev = e
if cur:
    words.append((cur, st, prev))
print(f"{a.out}: {al['character_end_times_seconds'][-1]:.2f}s")
print(" ".join(f"{w}[{s:.2f}-{e:.2f}]" for w, s, e in words if not w.startswith("[")))
