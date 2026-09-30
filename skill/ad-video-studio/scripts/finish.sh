#!/usr/bin/env bash
# Mix a music bed under the rendered voiceover (looped, ducked by the voice, faded out),
# normalise to -14 LUFS, and neutralise MP4 edit lists (Meta rejects them).
# usage: finish.sh RAW.mp4 MUSIC.(mp3|m4a) OUT.mp4 DURATION_SECONDS [MUSIC_GAIN=0.55]
set -euo pipefail
raw="$1"; music="$2"; out="$3"; dur="$4"; gain="${5:-0.55}"
fade=$(python3 -c "print(max(0, $dur - 1.0))")
ffmpeg -loglevel error -y -i "$raw" -stream_loop 2 -i "$music" -filter_complex \
  "[1:a]atrim=0:$dur,asetpts=PTS-STARTPTS,volume=$gain,afade=t=in:d=0.15,afade=t=out:st=$fade:d=1.0[m];\
   [0:a]asplit=2[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=250[md];\
   [v][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$out"
python3 "$(dirname "$0")/strip-edts.py" "$out"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$out"
