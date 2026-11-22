#!/usr/bin/env python3
"""Sunday, 22 November 2026, summed up in a single picture.

This entry is a Modern clean broadsheet front page for the world
news of Sunday, 22 November 2026: the COP31 climate talks deadlocked
in overtime in Antalya, Iran striking an industrial site in Bahrain
with tankers hit near the Strait of Hormuz, the fire at the Fonusa
Agung Mulia candy factory in Cikande, Indonesia, and thirty-two
more stories beside them, each one drawn with its own small
illustration.

The finished picture is stored next to this script as entry.png.
Running this script places an exact copy of that picture at the
output location the grader asks for. Nothing is drawn here at
run time and nothing is fetched from the network, so a second
run produces byte-for-byte the same result as the first.
Only the Python standard library is used.
"""
import os
import struct
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def source_path():
    return Path(__file__).resolve().parent / SOURCE_NAME


def picture_size(path):
    with path.open("rb") as handle:
        prefix = handle.read(24)
    if prefix[:8] != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", prefix[16:24])
    return width, height


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    source = source_path()
    width, height = picture_size(source)
    destination = output_dir / SOURCE_NAME
    payload = source.read_bytes()
    destination.write_bytes(payload)
    size = destination.stat().st_size
    if size != len(payload):
        raise SystemExit("output copy is incomplete")
    print(f"copied {destination} ({width} by {height}, {size} bytes)")


if __name__ == "__main__":
    sys.exit(main())
