#!/usr/bin/env bash
# Rank voiceover takes by the energy of their opening (the hook must sound excited).
# usage: pick-take.sh SECONDS take1.mp3 take2.mp3 ...   -> loudest RMS first
secs="$1"; shift
for f in "$@"; do
  rms=$(ffmpeg -t "$secs" -i "$f" -af astats -f null - 2>&1 | grep "RMS level dB" | tail -1 | awk '{print $NF}')
  echo "$rms $f"
done | sort -rn
