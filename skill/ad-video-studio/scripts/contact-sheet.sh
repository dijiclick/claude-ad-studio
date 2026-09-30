#!/usr/bin/env bash
# One image with a frame from each given time, side by side — read it to review a render.
# usage: contact-sheet.sh VIDEO OUT.png T1 T2 T3 ...
v="$1"; out="$2"; shift 2
tmp=$(mktemp -d); args=(); n=0
for t in "$@"; do
  ffmpeg -loglevel error -y -ss "$t" -i "$v" -frames:v 1 -vf scale=300:-1 "$tmp/$n.png"
  args+=(-i "$tmp/$n.png"); n=$((n+1))
done
ffmpeg -loglevel error -y "${args[@]}" -filter_complex "hstack=$n" "$out"
rm -rf "$tmp"; echo "$out"
