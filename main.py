#!/usr/bin/env python3
"""Invent a Word We Need (make.fun) — entry program.

Writes one coined word and its one-line definition to /output/entry.txt.
Deterministic: the same bytes on every run. No input, no network, no clock.
"""

import os

ENTRY = (
    "yesdrift: the habit of clicking yes without reading, "
    "until consent is pure muscle memory."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
    # Fail loudly here rather than shipping an entry the gate would refuse.
    chars = len(ENTRY)
    if not 1 <= chars <= 140:
        raise SystemExit(f"entry is {chars} characters, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
