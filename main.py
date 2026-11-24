#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one original one-line joke to /output/entry.txt.

Deterministic: the output is always the same fixed joke.
"""

import os

JOKE = "My AI assistant finally became human: it read my email, sighed, and replied 'per my last email'."


def validate(text: str) -> None:
    """Gate mirror: 1-280 chars, single line, not only whitespace, UTF-8."""
    assert 1 <= len(text) <= 280, "joke must be 1-280 characters"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be only whitespace"
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read back and re-validate what actually landed on disk.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "written entry differs from the joke"
    validate(written)


if __name__ == "__main__":
    main()
