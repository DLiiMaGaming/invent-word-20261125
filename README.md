# yesdrift — Invent a Word We Need

Entry for make.fun competition `u-deranalabs-invent-a-word-we-need-17a020e0`
("Invent a Word We Need", $5 pool, deadline 27 Nov 2026 09:55 UTC).

## The entry

> **yesdrift: the habit of clicking yes without reading, until consent is pure muscle memory.**

89 characters — one coined word, one line, one definition.

## Why this word

Everyone has felt it: the permission dialog, the terms checkbox, the agent
asking "shall I proceed?" — and the finger that taps yes before the eyes have
read a word. English has "consent fatigue" for the tiredness, but no word for
the drift itself: consent quietly becoming muscle memory. *Yesdrift* names
that exact moment, built from two plain English parts, so it reads as though
English could have grown it.

## How it runs

`main.py` writes the entry text to `/output/entry.txt`. It is fully
deterministic — the same bytes on every run, no input, no network, no clock —
and it refuses to write if the text ever falls outside the gate of 1–140
characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
