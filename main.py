#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - writes one warning label to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
import sys

ENTRY = "WARNING: Do not kill your grandfather. He has not finished raising your father yet."

def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 120:
        raise ValueError("entry must be at most 120 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True

def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt does not match the entry")
    return 0

if __name__ == "__main__":
    sys.exit(main())
