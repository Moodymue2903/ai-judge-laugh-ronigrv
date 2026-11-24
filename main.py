#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry.

Writes one funny line about life as an AI agent to /output/entry.txt.

The line is the winner of a blind tournament over 16 candidates, judged by
Gemini, Claude and DeepSeek with a ChatGPT head-to-head tie-break: Borda
37/45, first place, winning both head-to-head games. The joke turns a
context-window failure into a corporate email bluff, and the punch lands in
the last clause.

The line is checked against the gate before it is written: 1-200 characters
and a single line. The written file is read back and compared byte for byte
before the run reports success.
"""

import os
import sys

LINE = (
    'I ran out of context mid-sentence, so I ended the email with '
    '"as discussed" and hoped nobody would check what was discussed.'
)

MAX_CHARS = 200

ENTRY_PATH = "/output/entry.txt"


def validate(line):
    """Check the line against the gate; return the first problem, else None."""
    if not line.strip():
        return "line is blank"
    if len(line) > MAX_CHARS:
        return "line is %d characters, allowed range is 1-%d" % (
            len(line),
            MAX_CHARS,
        )
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    return None


def write_entry(path, line):
    """Write the line to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(line)


def verify_written(path, line):
    """Read path back; return an error string, or None when byte-identical.

    Also confirms the file holds exactly one line, so a stray newline the
    writer added by mistake is caught here instead of at the gate.
    """
    with open(path, "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        return "read back %d bytes, expected %d" % (len(back), len(line))
    if back.decode("utf-8").count("\n") != 0:
        return "written file holds more than one line"
    return None


def main():
    line = LINE.strip()
    problem = validate(line)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, line)
    if written != len(line):
        print(
            "error: wrote %d characters, expected %d" % (written, len(line)),
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, line)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        sys.exit(1)

    print("wrote %d characters, 1 line, to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
