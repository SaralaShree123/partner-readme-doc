#!/usr/bin/env python3
"""Apply 360dialog-style redesign to partner-docs (guides + API hubs)."""
from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "PAGE-MIGRATION-MAP.csv"


def slug_from_path(path: str) -> str:
    return Path(path).stem


def write_order_yaml(folder: Path, slugs: list[str]) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    content = "\n".join(f"- {s}" for s in slugs) + "\n"
    (folder / "_order.yaml").write_text(content, encoding="utf-8")


def move_guide(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    shutil.move(str(src), str(dst))


def apply_guide_moves() -> dict[str, list[str]]:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    moves = [r for r in rows if r["action"] == "MOVE" and r["content_type"] == "Guide"]
    moves.sort(key=lambda r: r["current_path"].count("/"), reverse=True)

    section_pages: dict[str, list[str]] = {}

    for row in moves:
        src = ROOT / row["current_path"]
        dst = ROOT / row["proposed_new_path"]
        if not src.exists():
            print(f"SKIP missing: {src}")
            continue
        move_guide(src, dst)
        section = row["target_section"]
        slug = slug_from_path(row["proposed_new_path"])
        section_pages.setdefault(section, []).append(slug)
        print(f"MOVED: {row['current_path']} -> {row['proposed_new_path']}")

    return section_pages


def create_get_started_pages() -> None:
    gs = ROOT / "docs" / "Get Started"
    qs = gs / "quickstarts"

    overview = gs / "overview.md"
    if not overview.exists():
        overview.write_text(
            """---
title: Overview
excerpt: Welcome to Gupshup Partner Documentation
deprecated: false
hidden: false
metadata:
  title: Gupshup Partner Documentation
  description: Get started with Gupshup Partner APIs, Partner Portal, and WhatsApp integrations.
  robots: index
next:
  description: Start the 5-step quickstart path
  pages:
    - docs/Get Started/quickstarts/get-started-as-partner
---

# Welcome to Gupshup Partner Documentation

Build WhatsApp-powered solutions on Gupshup's Partner platform — whether you are an **ISV**, **Tech Provider**, **Agency**, or **Enterprise** integrator.

## Quick links

| Resource | Description |
|----------|-------------|
| [Quickstarts](quickstarts/) | 5-step path from signup to first message |
| [Partner API](/reference/partner-apis) | API reference grouped by category |
| [Partner Hub](../Partner%20Hub/support) | Wallet, billing, and support |
| [Onboarding](../Onboarding/inbound-events-v2) | Webhooks, events, and onboarding |

## Who this is for

- **SaaS platforms** embedding WhatsApp for customers
- **ISVs** building branded customer experiences
- **Tech Providers** registered with Meta
- **Agencies & enterprises** managing WABA at scale

## Partner journey

1. **Sign up** — [Get Started as a Partner](quickstarts/get-started-as-partner)
2. **Register** — [Solution Partners & Tech Providers](what-is-sp-tp)
3. **Create an app** — [Create your first App](quickstarts/create-your-first-app)
4. **Authenticate** — [Generate Secret and Token](quickstarts/generate-secret-and-token)
5. **Send messages** — [Send your first message](quickstarts/send-your-first-message)

## Explore

- [Pricing](pricing)
- [Gupshup Partner Eco-System](gupshup-partner-eco-system)
- [Gupshup Partner Offering](gupshup-partner-offering)
""",
            encoding="utf-8",
        )

    qs_index = qs / "index.md"
    if not qs_index.exists():
        qs_index.write_text(
            """---
title: Quickstarts
excerpt: Five steps from partner signup to your first WhatsApp message
deprecated: false
hidden: false
metadata:
  title: Partner Quickstarts
  description: Step-by-step guide for Gupshup Partner onboarding
  robots: index
---

# Quickstarts

Follow these five steps to integrate with Gupshup Partner APIs — modeled after the standard partner onboarding path.

| Step | Guide | What you'll do |
|------|-------|----------------|
| 1 | [Get Started as a Partner](get-started-as-partner) | Understand the partner ecosystem and sign up |
| 2 | [Register as Tech Provider](register-as-tech-provider) | Learn about Solution Partners & Tech Providers |
| 3 | [Create your first App](create-your-first-app) | Create a WABA application in Partner Portal |
| 4 | [Generate Secret and Token](generate-secret-and-token) | Set up API authentication |
| 5 | [Send your first message](send-your-first-message) | Send a WhatsApp message via Partner API |

> **Next:** Explore [Onboarding](../Onboarding/) for webhooks, events, and advanced setup.
""",
            encoding="utf-8",
        )

    # Quickstart step pages (create from existing or alias)
    quickstart_map = {
        "get-started-as-partner.md": ("introduction.md", "Get Started as a Partner"),
        "register-as-tech-provider.md": ("what-is-sp-tp.md", "Register as Tech Provider"),
        "send-your-first-message.md": ("../Messaging/whatsapp-messages.md", "Send your first message"),
    }
    for filename, (source, title) in quickstart_map.items():
        target = qs / filename
        if target.exists():
            continue
        if source.startswith("../"):
            src_path = (qs / source).resolve()
        else:
            src_path = gs / source
        if src_path.exists():
            content = src_path.read_text(encoding="utf-8")
            content = re.sub(r"^title:.*$", f"title: {title}", content, count=1, flags=re.M)
            target.write_text(content, encoding="utf-8")
        else:
            target.write_text(
                f"""---
title: {title}
excerpt: ''
deprecated: false
hidden: false
metadata:
  robots: index
---

See the linked guide in this section for full details.
""",
                encoding="utf-8",
            )


def build_section_orders(section_pages: dict[str, list[str]]) -> None:
    orders = {
        "Get Started": [
            "overview",
            "quickstarts",
            "introduction",
            "gupshup-partner-eco-system",
            "what-is-sp-tp",
            "pricing",
            "tier-based-pricing",
            "gupshup-partner-offering",
            "amplead",
            "get-started-with-meta-partner-eco-system",
            "get-solution-id-from-meta",
        ],
        "Onboarding": [
            "inbound-events-v2",
            "account-events",
            "billing-events",
            "message-events",
            "system-events",
            "user-events",
            "pmp-events-1",
            "understanding-webhooks-and-callback",
            "partner-hosted-embedded-sign-up-flow",
            "co-existence-closed-beta-phase",
            "coexistence-events",
            "coexistence-webhooks",
            "get-started-guide-with-gupshup-flow-management-apis",
        ],
        "Partner Hub": [
            "get-started-with-partner-portal",
            "partner-portal-walkthrough",
            "wallet-1",
            "commissions",
            "overdraft-limit",
            "partner-wallet-balance-transfer",
            "recharge-via-stipe-or-ebanx",
            "wire-transfer-automation",
            "support",
            "partner-customer-portal",
            "partner-customer-migration-to-partner-customer-portal-pcp",
            "unused-commission-policy",
            "meta-whatsapp-features",
        ],
        "Messaging": [
            "whatsapp-messages",
            "welcome-messages",
            "outbound-messages",
            "inbound-messages",
            "types-of-inbound-messages",
            "text",
            "media",
            "interactive",
            "media-management",
            "marketing-messages-lite-mm-lite-api",
            "mark-message-as-readtyping-indicator",
            "partner-whatsapp-groups-api-beta",
            "guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup",
            "obtain-user-call-permissions",
            "permanent-call-permissions-for-whatsapp-voice",
        ],
        "Commerce & Payments": [
            "whatsapp-brazil-payments",
            "wallet-creation-kyc-flow-guide",
            "partner-usd-wire-transfers",
        ],
    }

    for section, preferred in orders.items():
        folder = ROOT / "docs" / section
        if not folder.exists():
            continue
        existing = {p.stem for p in folder.glob("*.md")}
        slugs = [s for s in preferred if s in existing]
        slugs += sorted(existing - set(slugs))
        write_order_yaml(folder, slugs)

    # Quickstarts sub-order
    qs = ROOT / "docs" / "Get Started" / "quickstarts"
    if qs.exists():
        qs_order = [
            "index",
            "get-started-as-partner",
            "register-as-tech-provider",
            "create-your-first-app",
            "generate-secret-and-token",
            "send-your-first-message",
            "partner-rate-limits",
        ]
        existing = {p.stem for p in qs.glob("*.md")}
        slugs = [s for s in qs_order if s in existing]
        slugs += sorted(existing - set(slugs))
        write_order_yaml(qs, slugs)


def update_docs_root_order() -> None:
    order = [
        "Get Started",
        "Onboarding",
        "Partner Hub",
        "Messaging",
        "Commerce & Payments",
        "Security",
        "Meta WhatsApp Features",
        "Amplead",
        "Partner Onboarding Guidance",
        "Partner Security",
        "Partner customer portal",
        "tpp-partner-hosted-onboarding",
        "Partner Portal (hidden)",
        "testing",
        "abc",
    ]
    existing = {p.name for p in (ROOT / "docs").iterdir() if p.is_dir()}
    final = [s for s in order if s in existing]
    final += sorted(existing - set(final) - {"Partner Portal", "Voice", "WhatsApp Payments", "INR Wallet", "Wire Transfer", "Type Indicator", "WhatsApp Groups"})
    write_order_yaml(ROOT / "docs", final)


def create_api_hubs() -> None:
    api_root = ROOT / "reference" / "Partner APIs"
    categories = {
        "partner-management": {
            "title": "Partner Management",
            "desc": "Partner authentication, app listing, and linking applications.",
            "links": [
                ("partner-app-management/app", "Link App with Partner"),
                ("partner-app-management/partners-linked-application", "Partner Linked Application"),
            ],
        },
        "channel-management": {
            "title": "Channel Management",
            "desc": "Create, update, and manage WABA channel applications.",
            "links": [
                ("app-onboarding-apis", "App Onboarding APIs"),
                ("partner-app-management/app", "Create & Update App"),
                ("partner-app-management/deleteapp", "Delete App"),
                ("partner-app-management/obo-to-embed-flow", "Embed Link Flow"),
            ],
        },
        "waba-account-management": {
            "title": "WABA Account Management",
            "desc": "WABA health, phone numbers, quality ratings, and account settings.",
            "links": [
                ("partner-app-management/phone-for-an-app", "Phone for an App"),
                ("partner-app-management/analytics", "Analytics"),
            ],
        },
        "webhook-management": {
            "title": "Webhook Management",
            "desc": "Set up and manage webhook subscriptions and callback URLs.",
            "links": [
                ("partner-app-management/subscription-management", "Subscription Management"),
                ("partner-app-management/set-callback-url", "Set Callback URL"),
            ],
        },
        "balance-and-usage": {
            "title": "Balance & Usage",
            "desc": "Wallet balance, commissions, usage, and billing APIs.",
            "links": [
                ("partner-app-management/commission", "Commission & Capping"),
            ],
        },
        "templates-management": {
            "title": "Templates Management",
            "desc": "Create, apply, manage, and send WhatsApp message templates.",
            "links": [
                ("template-apis", "Template APIs"),
                ("auth-template-v2", "Auth Template V2"),
            ],
        },
        "messaging-v3": {
            "title": "Messaging (V3)",
            "desc": "Send session messages — text, media, interactive, reactions, and more.",
            "links": [
                ("partner-meta-and-whatsapp-apis/passthrough-apis", "Passthrough APIs (V3)"),
            ],
        },
        "media-management": {
            "title": "Media Management",
            "desc": "Upload, download, and delete media for WhatsApp messages.",
            "links": [
                ("partner-app-management/generate-media-id", "Generate Media ID"),
            ],
        },
        "whatsapp-flows": {
            "title": "WhatsApp Flows",
            "desc": "Create, publish, and manage WhatsApp Flow experiences.",
            "links": [
                ("partner-meta-and-whatsapp-apis/flow-management", "Flow Management"),
            ],
        },
        "business-profile": {
            "title": "Business Profile",
            "desc": "Manage business profile, photo, and display name.",
            "links": [
                ("partner-app-management/business-profile", "Business Profile APIs"),
            ],
        },
        "user-management": {
            "title": "User Management",
            "desc": "Block, unblock, and list blocked WhatsApp users.",
            "links": [
                ("partner-app-management/block-user", "Block User APIs"),
            ],
        },
        "marketing-messages-lite": {
            "title": "Marketing Messages Lite",
            "desc": "MM Lite enablement, sending, and insights.",
            "links": [
                ("mmliteapi", "MM Lite APIs"),
            ],
        },
    }

    overview = api_root / "overview.md"
    if not overview.exists():
        overview.write_text(
            """---
title: Partner API Overview
excerpt: Gupshup Partner API reference organized by category
deprecated: false
hidden: false
metadata:
  title: Partner API
  description: Gupshup Partner API reference
  robots: index
---

# Partner API

Gupshup Partner APIs let you build branded WhatsApp experiences for your customers. Endpoints are grouped by business category below.

## API Categories

| Category | Description |
|----------|-------------|
| [Partner Management](partner-management/) | Authentication, apps, linking |
| [Channel Management](channel-management/) | Create and manage WABA apps |
| [WABA Account Management](waba-account-management/) | Health, phone, quality |
| [Webhook Management](webhook-management/) | Subscriptions and callbacks |
| [Balance & Usage](balance-and-usage/) | Wallet and billing |
| [Templates Management](templates-management/) | Message templates |
| [Messaging (V3)](messaging-v3/) | Session messages |
| [Media Management](media-management/) | Media upload/download |
| [WhatsApp Flows](whatsapp-flows/) | Flow lifecycle |
| [Business Profile](business-profile/) | Profile and display name |
| [User Management](user-management/) | Block/unblock users |
| [Marketing Messages Lite](marketing-messages-lite/) | MM Lite |

## Authentication

All Partner API requests require a partner token. See [Generate Secret and Token](/docs/get-started/quickstarts/generate-secret-and-token) in the guides.
""",
            encoding="utf-8",
        )

    for slug, info in categories.items():
        cat_dir = api_root / slug
        cat_dir.mkdir(parents=True, exist_ok=True)
        index = cat_dir / "index.md"
        lines = [
            "---",
            f"title: {info['title']}",
            f"excerpt: {info['desc']}",
            "deprecated: false",
            "hidden: false",
            "metadata:",
            "  robots: index",
            "---",
            "",
            f"# {info['title']}",
            "",
            info["desc"],
            "",
            "## Endpoints",
            "",
        ]
        for link_path, label in info["links"]:
            lines.append(f"- [{label}](../{link_path}/)")
        lines.append("")
        index.write_text("\n".join(lines), encoding="utf-8")

    # Update Partner APIs _order.yaml
    cat_slugs = list(categories.keys())
    legacy = [
        "partner-app-management",
        "template-apis",
        "app-onboarding-apis",
        "partner-meta-and-whatsapp-apis",
        "mmliteapi",
        "auth-template-v2",
        "message-searcher-apis",
        "apikey-regeneration-apis",
        "solution-migrate-intent-api",
        "type-indicator",
        "default-1",
    ]
    order = ["overview"] + cat_slugs + [s for s in legacy if (api_root / s).exists()]
    write_order_yaml(api_root, order)

    # Update reference root order - Partner APIs first
    ref_order = ["Partner APIs"]
    for item in (ROOT / "reference" / "_order.yaml").read_text().splitlines():
        name = item.lstrip("- ").strip()
        if name and name != "Partner APIs":
            ref_order.append(name)
    write_order_yaml(ROOT / "reference", ref_order)


def cleanup_empty_dirs(path: Path) -> None:
    if not path.is_dir():
        return
    for child in sorted(path.iterdir()):
        if child.is_dir():
            cleanup_empty_dirs(child)
    if path.name == "docs" or path.name == "reference":
        return
    try:
        if not any(path.iterdir()):
            path.rmdir()
            print(f"REMOVED empty: {path.relative_to(ROOT)}")
    except OSError:
        pass


def main() -> None:
    print("=== Phase 1-2: Guide moves ===")
    section_pages = apply_guide_moves()
    print("\n=== Creating Get Started pages ===")
    create_get_started_pages()
    print("\n=== Building section _order.yaml ===")
    build_section_orders(section_pages)
    print("\n=== Updating docs root order ===")
    update_docs_root_order()
    print("\n=== Phase 3: API category hubs ===")
    create_api_hubs()
    print("\n=== Cleanup empty directories ===")
    cleanup_empty_dirs(ROOT / "docs")
    print("\nDone.")


if __name__ == "__main__":
    main()
