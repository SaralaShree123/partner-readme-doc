#!/usr/bin/env python3
"""Restore hidden: true on pages that were hidden in the production ReadMe export."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
# Original production Git export (update path if needed)
EXPORT = Path.home() / "Downloads/partners-docs-v1.0-2026-07-07T06-24-19_b49dd82/docs"


def slug_from_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^slug:\s*(\S+)", text, re.M)
    if match:
        return match.group(1)
    return path.stem if path.name != "index.md" else path.parent.name


def hidden_from_file(path: Path) -> bool | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^hidden:\s*(true|false)", text, re.M)
    if not match:
        return None
    return match.group(1) == "true"


def build_export_hidden_map() -> dict[str, bool]:
    hidden: dict[str, bool] = {}
    if not EXPORT.exists():
        raise SystemExit(f"Export not found: {EXPORT}")
    for path in EXPORT.rglob("*.md"):
        flag = hidden_from_file(path)
        if flag is not None:
            hidden[slug_from_file(path)] = flag
    return hidden


def main() -> None:
    export_hidden = build_export_hidden_map()
    changed = 0
    for path in DOCS.rglob("*.md"):
        slug = slug_from_file(path)
        if slug not in export_hidden or not export_hidden[slug]:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"^hidden:\s*false", text, re.M):
            path.write_text(
                re.sub(r"^hidden:\s*false", "hidden: true", text, count=1, flags=re.M),
                encoding="utf-8",
            )
            changed += 1
            print(f"RE-HIDE {path.relative_to(ROOT)} ({slug})")
    print(f"\nRe-hidden {changed} pages to match production export")


if __name__ == "__main__":
    main()
