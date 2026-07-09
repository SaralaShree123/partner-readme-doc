#!/usr/bin/env python3
"""Replace partner-docs.gupshup.io links with relative /docs and /reference paths."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_EXTENSIONS = {".md", ".json", ".yaml", ".yml"}

# Match production partner docs URLs (with optional trailing slash, anchors, fragments)
PROD_URL = re.compile(
    r"https?://partner-docs\.gupshup\.io(?P<path>/(?:docs|reference|update/reference)[^\s\"')\]>]*|/)",
    re.IGNORECASE,
)

SECURITY_PAGES = ROOT / "docs" / "security"


def to_relative(match: re.Match[str]) -> str:
    path = match.group("path")
    if path.startswith("/update/reference/"):
        path = path.replace("/update/reference/", "/reference/", 1)
    if path == "/":
        return "/"
    return path.rstrip("/") if path.endswith("/") and "#" not in path and path.count("/") > 2 else path


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new_text, count = PROD_URL.subn(to_relative, text)
    if count:
        path.write_text(new_text, encoding="utf-8")
    return count


def unhide_security_pages() -> int:
    changed = 0
    for path in SECURITY_PAGES.glob("*.md"):
        if path.name == "security-overview.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "hidden: true" in text:
            new_text = text.replace("hidden: true", "hidden: false", 1)
            path.write_text(new_text, encoding="utf-8")
            changed += 1
            print(f"UNHIDE {path.relative_to(ROOT)}")
    return changed


def main() -> None:
    total = 0
    files_changed = 0
    for path in ROOT.rglob("*"):
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if ".git" in path.parts or ".venv" in path.parts:
            continue
        count = fix_file(path)
        if count:
            files_changed += 1
            total += count
            print(f"LINKS {path.relative_to(ROOT)} ({count})")

    unhidden = unhide_security_pages()
    print(f"\nDone: {total} links fixed in {files_changed} files, {unhidden} security pages unhidden")


if __name__ == "__main__":
    main()
