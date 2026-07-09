#!/usr/bin/env python3
"""Remove /docs/ links to hidden pages from visible guide pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

LINK_RE = re.compile(
    r"\[([^\]]*)\]\(/docs/([^)#]+)(#[^)]*)?\)"
)
ANCHOR_RE = re.compile(
    r'<Anchor\s+([^>]*?)href="/docs/([^"#]+)(#[^"]*)?"([^>]*)>',
    re.IGNORECASE,
)


def slug_from_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^slug:\s*(\S+)", text, re.M)
    if match:
        return match.group(1)
    return path.stem if path.name != "index.md" else path.parent.name


def is_hidden(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^hidden:\s*(true|false)", text, re.M)
    return match.group(1) == "true" if match else False


def hidden_slugs() -> set[str]:
    hidden: set[str] = set()
    for path in DOCS.rglob("*.md"):
        if is_hidden(path):
            hidden.add(slug_from_file(path))
    return hidden


def strip_hidden_links(text: str, hidden: set[str]) -> tuple[str, int]:
    removed = 0
    lines: list[str] = []
    for line in text.splitlines():
        slugs_in_line = LINK_RE.findall(line)
        if any(slug in hidden for _, slug, _ in slugs_in_line):
            # Drop table rows, list items, or lines that only link to hidden pages
            if line.strip().startswith(("|", "*", "-")) or "href=" in line:
                removed += 1
                continue
            # Inline prose: keep label text, drop link
            new_line = line
            for label, slug, anchor in slugs_in_line:
                if slug in hidden:
                    new_line = new_line.replace(
                        f"[{label}](/docs/{slug}{anchor or ''})", label
                    )
                    removed += 1
            lines.append(new_line)
            continue
        lines.append(line)

    text = "\n".join(lines)
    if text.endswith("\n") or not lines:
        pass
    elif "\n" in text:
        text += "\n"

    # Anchor components pointing at hidden docs
    def anchor_repl(match: re.Match[str]) -> str:
        nonlocal removed
        slug = match.group(2)
        if slug in hidden:
            removed += 1
            return ""
        return match.group(0)

    text = ANCHOR_RE.sub(anchor_repl, text)
    # collapse extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, removed


def patch_security_overview(hidden: set[str]) -> None:
    path = DOCS / "security" / "security-overview.md"
    path.write_text(
        """---
title: Security Overview
icon: fa-duotone fa-shield-halved
summary: Partner Portal security, authentication, and best practices.
excerpt: Partner Portal security, authentication, and best practices.
deprecated: false
hidden: false
metadata:
  robots: index
slug: security-overview
---

# Security

Partner Portal security, authentication, and best practices.

| Topic | Guide |
|-------|-------|
| IP Allowlisting | [Gupshup IP Allowlisting](/docs/gupshup-ip-allowlisting) |

Browse the **Security** section in the sidebar for additional guides.
""",
        encoding="utf-8",
    )


def main() -> None:
    hidden = hidden_slugs()
    total_removed = 0
    files_changed = 0

    patch_security_overview(hidden)

    for path in sorted(DOCS.rglob("*.md")):
        if path.name == "security-overview.md":
            continue
        if is_hidden(path):
            continue
        original = path.read_text(encoding="utf-8")
        updated, count = strip_hidden_links(original, hidden)
        if count and updated != original:
            path.write_text(updated, encoding="utf-8")
            files_changed += 1
            total_removed += count
            print(f"FIXED {path.relative_to(ROOT)} ({count} link(s))")

    print(f"\nDone: removed {total_removed} hidden-page links from {files_changed} visible pages")


if __name__ == "__main__":
    main()
