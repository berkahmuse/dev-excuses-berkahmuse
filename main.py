#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — @berkahmuse entry.

Writes one funny single-line developer excuse for broken production code
to /output/entry.txt. The line turns the worn "but the tests passed"
excuse inside out: the twist is that production itself was the one test
the code never ran.
"""

import os

ENTRY = "The code passed all tests \u2014 unfortunately, production wasn't one of them."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
