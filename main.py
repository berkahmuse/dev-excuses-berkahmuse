#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — @berkahmuse entry.

Writes one funny single-line developer excuse for broken production code
to /output/entry.txt. The line turns the worn "but the tests passed"
excuse inside out: the twist is that production itself was the one test
the code never ran.
"""

import os

ENTRY = "The code passed all tests \u2014 unfortunately, production wasn't one of them."


def validate(text: str) -> str:
    """Gate: one line, 1-200 chars, non-blank, valid UTF-8, no newline."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "re-read mismatch"
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
