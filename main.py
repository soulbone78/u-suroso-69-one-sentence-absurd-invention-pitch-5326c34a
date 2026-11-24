#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

import os

SENTENCE = (
    "A washing machine that holds one sock hostage per load "
    "until you confess where all the others went."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 220, "sentence must be 1-220 characters"
    assert SENTENCE.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
