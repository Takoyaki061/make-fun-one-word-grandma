#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word: Chattycathy. Grandma misremembers ChatGPT as a talkative
church lady named Chatty Cathy, and texts her by name.
"""
import os

WORD = "Chattycathy"


def main() -> None:
    # Enforce the gate ourselves: 1-30 chars, not only whitespace.
    word = WORD.strip()
    if not 1 <= len(word) <= 30 or not word.strip():
        raise ValueError("entry word fails the gate: %r" % WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
