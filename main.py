#!/usr/bin/env python3
"""Museum of the Year 3000 — print the exhibit label exactly as written."""

from pathlib import Path

def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    print(text, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
