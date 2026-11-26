"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one diagnosis line to /output/entry.txt. Python 3.13, standard
library only, no network, fully deterministic: the same bytes every run.
The line is a deadpan clinical finding about a small human habit, with
the laugh landing on the last clause.
"""

import os
import sys

LINE = "Diagnosis: acute read-receipt anxiety \u2014 you draft every reply for an hour, then send \u2018haha\u2019, and lie awake wondering if it sounded cold."
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def valid(line):
    """Gate mirror: 1-200 chars, one line, not only whitespace."""
    return (
        isinstance(line, str)
        and 1 <= len(line) <= MAX_CHARS
        and "\n" not in line
        and "\r" not in line
        and line.strip() != ""
    )


def output_dir():
    """The grader mounts /output; fall back beside this file if it is absent."""
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main():
    if not valid(LINE):
        print("entry line fails the gate", file=sys.stderr)
        return 1
    path = os.path.join(output_dir(), OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The gate reads the file, not the process: make the bytes world-readable.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
