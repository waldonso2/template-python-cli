"""Command line: reads the input, calls ``core``, prints the result."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from . import core


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="tool", description="PLACEHOLDER")
    parser.add_argument("file", nargs="?", type=argparse.FileType("r", encoding="utf-8"), default=sys.stdin)
    parser.add_argument("--top", type=int, default=10, help="how many words to show")
    args = parser.parse_args(argv)
    for word, n in core.word_counts(args.file.read())[: args.top]:
        print(f"{n}\t{word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
