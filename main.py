"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

Python standard library only.
"""

import os
import sys

HAIKU = (
    "The try block swallows\n"
    "the error whole, then nothing\n"
    "the crash was mercy"
)

# Syllable count, line by line (5-7-5), 72 characters total:
#   "The(1) try(1) block(1) swallows(2)" = 5
#   "the(1) error(2) whole(1) then(1) nothing(2)" = 7
#   "the(1) crash(1) was(1) mercy(2)" = 5
# No trailing newline: the file holds exactly the haiku.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)
    return 0


if __name__ == "__main__":
    sys.exit(main())
