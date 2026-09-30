#!/usr/bin/env python3
"""Break a reference ad video into what Claude needs to deconstruct it (replaces the course's Gemini Gem step).

Usage: deconstruct_video.py VIDEO [OUT_DIR] [--every 1.0] [--engine whisper|parakeet]

Writes to OUT_DIR (default: <video>_deconstruct/):
  frames/t0000.0.jpg ...  one frame every N seconds (default 1s), 540px tall
  contact_sheet.jpg       up to 36 frames in one grid (read this first)
  transcript.srt          timestamped speech (whisper by default; --engine parakeet = faster, English/EU only)
  info.txt                duration, resolution, fps, audio present
Then read info.txt, transcript.srt and the frames, and fill the deconstruction template in SKILL.md.
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("out", nargs="?")
ap.add_argument("--every", type=float, default=1.0)
ap.add_argument("--engine", choices=["parakeet", "whisper"], default="whisper",
                help="whisper (default) = 99 languages incl. Turkish/Persian/Arabic; parakeet = ~2x faster but English + 24 European languages only (NOT Turkish)")
a = ap.parse_args()

v = Path(a.video).expanduser().resolve()
if not v.exists():
    sys.exit(f"not found: {v}")
out = Path(a.out).expanduser() if a.out else v.with_name(v.stem + "_deconstruct")
(out / "frames").mkdir(parents=True, exist_ok=True)

probe = json.loads(subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(v)],
                                  capture_output=True, text=True).stdout)
dur = float(probe["format"]["duration"])
vs = next(s for s in probe["streams"] if s["codec_type"] == "video")
has_audio = any(s["codec_type"] == "audio" for s in probe["streams"])
num, den = (vs.get("r_frame_rate", "30/1").split("/") + ["1"])[:2]
(out / "info.txt").write_text(f"file: {v.name}\nduration_s: {dur:.1f}\nresolution: {vs['width']}x{vs['height']}\n"
                              f"fps: {float(num)/float(den):.1f}\naudio: {has_audio}\n")

t = 0.0
while t < dur - 0.1:  # a seek at the very end yields no frame
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", str(v), "-frames:v", "1",
                    "-vf", "scale=-2:540", "-q:v", "4", str(out / "frames" / f"t{t:06.1f}.jpg")],
                   stderr=subprocess.DEVNULL)  # a missing frame is skipped, not fatal
    t += a.every

if has_audio:
    wav = out / "audio.wav"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(v), "-ar", "16000", "-ac", "1", str(wav)], check=True)
    if a.engine == "parakeet":
        cmd = ["uvx", "--python", "3.12", "--from", "parakeet-mlx", "parakeet-mlx", str(wav), "--output-format", "srt", "--output-dir", str(out)]
    else:
        cmd = ["uvx", "--python", "3.12", "--from", "mlx-whisper", "mlx_whisper", str(wav), "--model",
               "mlx-community/whisper-large-v3-turbo", "--output-format", "srt", "--output-dir", str(out)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.move(str(out / "audio.srt"), out / "transcript.srt")
    wav.unlink()

frames = sorted((out / "frames").glob("*.jpg"))
n = len(frames)
cols = 6 if n > 24 else 4
sheet = [f for f in frames][::max(1, n // 36)][:36]  # max 36 tiles
lst = out / "frames.txt"
lst.write_text("".join(f"file '{f}'\n" for f in sheet))
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                "-vf", f"scale=-2:320,tile={cols}x{-(-len(sheet)//cols)}",
                "-frames:v", "1", str(out / "contact_sheet.jpg")], check=False)
lst.unlink()
step = a.every * max(1, n // 36)
with open(out / "info.txt", "a") as f:
    f.write(f"contact_sheet: {len(sheet)} frames, left-to-right then top-to-bottom, one every {step:g}s starting at 0s\n")
print(f"OK {out}\n  {dur:.1f}s, {n} frames, transcript: {'transcript.srt' if has_audio else 'none (no audio)'}")
