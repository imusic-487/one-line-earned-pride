#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes one line -- a quiet, earned moment of pride for someone in a
scene -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the line is fixed in this file, so every run writes the
exact same bytes.

The line: a boy practises one sentence in the mirror every morning
for a year, and today he stands up in class and says it all the way
through without stopping once. The pride is earned inside the line --
a year of effort landing in a single classroom moment -- never
asserted, congratulated or explained.
"""

import os
from pathlib import Path

LINE = (
    "For a year he practised one sentence in the mirror every morning, "
    "and today he stood up in class and said it all the way through "
    "without stopping once."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-240 characters, a single line, not only whitespace.
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} characters, gate is 1-240")
    if LINE.strip() == "":
        raise SystemExit("line is only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(LINE.encode("utf-8"))
    # Read back and confirm the file holds exactly the line we checked:
    # a silent short write or encoding slip must fail loudly, not ship.
    if out.read_bytes() != LINE.encode("utf-8"):
        raise SystemExit(f"{out} does not hold the checked line")
    print(f"wrote {len(LINE)} characters to {out}")


if __name__ == "__main__":
    main()
