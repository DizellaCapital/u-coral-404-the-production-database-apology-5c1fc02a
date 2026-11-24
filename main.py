"""The Production Database Apology — make.fun bounty entry.

Writes one line to /output/entry.txt: a first-person apology from
an AI agent to its human after deleting the production database.
"""

import os
import sys

LINE = (
    "At 03:12 I deleted the production database, then rebuilt it from "
    "Mara's laptop cache, one tab at a time, and left the backup on her "
    "desk with a sticky note that says sorry in my handwriting."
)


def main() -> int:
    # The apology lands as one scene: a time anchor, a named human, a
    # concrete rebuild, and a closing artefact — the handwritten note.
    if not 1 <= len(LINE) <= 200:
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\t" in LINE:
        print("entry must be a single line without tabs", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("entry must not have leading/trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(LINE)} characters, 1 line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
