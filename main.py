#!/usr/bin/env python3
"""One excuse, one file, no surprises."""

import os
import sys

LINE = "My confidence was at 99%, my progress was at 1%, and I reported the average, which looked excellent."

TARGET = "/output/entry.txt"
LIMIT = 200
WANT_LEN = 100
MUST_HAVE = ("confidence", "progress", "average", "99%", "1%")


def faults(text):
    found = []
    if not text:
        found.append("empty")
    if text != text.strip():
        found.append("loose whitespace at an end")
    for bad in ("\n", "\r"):
        if bad in text:
            found.append("a line break inside the line")
    if len(text) > LIMIT:
        found.append("over %d characters" % LIMIT)
    if len(text) != WANT_LEN:
        found.append("not %d characters" % WANT_LEN)
    if not text.endswith("."):
        found.append("no full stop at the end")
    if text.count(".") != 1:
        found.append("more than one sentence in the line")
    for piece in MUST_HAVE:
        if piece not in text:
            found.append("missing %r" % piece)
    return found


def save(text):
    folder = os.path.dirname(TARGET)
    os.makedirs(folder, exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="\n") as out:
        out.write(text + "\n")
    os.chmod(TARGET, 0o644)


def run():
    line = LINE.strip()
    bad = faults(line)
    if bad:
        for item in bad:
            print("bad line: " + item, file=sys.stderr)
        return 1
    save(line)
    print("%s: %d characters, one line" % (TARGET, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(run())
