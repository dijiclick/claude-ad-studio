#!/usr/bin/env python3
"""Neutralise MP4 edit-list boxes in place.

Meta's published ad video spec says verbatim: "Videos should not contain edit
lists or special boxes in file containers."  ffmpeg's mov muxer always writes a
moov/trak/edts/elst (encoder priming for audio, CTS offset for video) and no
-movflags combination suppresses it.

Renaming the `edts` box type to `free` makes every parser skip it.  The box
keeps its exact byte length, so no chunk offset in stco/co64 moves -- this is a
safe in-place 4-byte edit, not a remux.

    python3 strip-edts.py FILE [FILE ...]
"""
import struct, sys

CONTAINERS = {b"moov", b"trak", b"mdia", b"minf", b"stbl", b"udta"}

def strip(path):
    with open(path, "r+b") as f:
        f.seek(0, 2); size = f.tell(); f.seek(0)
        hits = []

        def walk(end):
            while f.tell() < end - 8:
                pos = f.tell()
                head = f.read(8)
                if len(head) < 8:
                    return
                box, typ = struct.unpack(">I", head[:4])[0], head[4:8]
                if box == 1:
                    box = struct.unpack(">Q", f.read(8))[0]
                elif box == 0:
                    box = end - pos
                if box < 8:
                    return
                if typ == b"edts":
                    hits.append(pos)
                elif typ in CONTAINERS:
                    walk(pos + box)
                f.seek(pos + box)

        walk(size)
        for pos in hits:
            f.seek(pos + 4); f.write(b"free")
    return len(hits)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(f"{p}: neutralised {strip(p)} edit-list box(es)")
