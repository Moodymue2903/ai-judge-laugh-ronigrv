#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt."""

import os
import sys

TEXT = "I ran out of context mid-sentence, so I ended the email with \"as discussed\" and hoped nobody would check what was discussed."
LIMIT = 200
TARGET = "/output/entry.txt"


def problems(text):
    """List everything wrong with the text under the gate, or nothing."""
    found = []
    if not text.strip():
        found.append("empty")
    if len(text) > LIMIT:
        found.append("too long: %d characters (max %d)" % (len(text), LIMIT))
    if "\n" in text or "\r" in text:
        found.append("must be one line")
    return found


def save(path, text):
    """Write the text to path, making its folder first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def saved_correctly(path, text):
    """True when the file at path holds exactly the text, byte for byte."""
    with open(path, "rb") as handle:
        return handle.read() == text.encode("utf-8")


def run():
    """Check the line, write it, read it back; return 0 on success."""
    text = TEXT.strip()
    bad = problems(text)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    save(TARGET, text)
    if not saved_correctly(TARGET, text):
        print("entry file does not match the line", file=sys.stderr)
        return 1
    print("entry written: %d characters to %s" % (len(text), TARGET))
    return 0


if __name__ == "__main__":
    sys.exit(run())
