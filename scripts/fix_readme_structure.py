#!/usr/bin/env python3
"""Fix ReadMe git-sync structure to match 360dialog redesign plan."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Folder renames: current → kebab-case (ReadMe-friendly)
FOLDER_RENAMES = {
    "Get Started": "get-started",
    "Onboarding": "onboarding",
    "Partner Hub": "partner-hub",
    "Messaging": "messaging",
    "Commerce & Payments": "commerce-and-payments",
    "Meta WhatsApp Features": "meta-whatsapp-features",
    "Security": "security",
    "Partner Portal (hidden)": "partner-portal-hidden",
}

DOCS_ORDER = [
    "get-started",
    "onboarding",
    "partner-api",
    "partner-hub",
    "messaging",
    "commerce-and-payments",
    "security",
    "meta-whatsapp-features",
    "amplead",
    "partner-portal-hidden",
]

GET_STARTED_ORDER = [
    "overview",
    "quickstarts",
    "introduction",
    "gupshup-partner-eco-system",
    "what-is-sp-tp",
    "pricing",
    "tier-based-pricing",
    "gupshup-partner-offering",
    "get-started-with-meta-partner-eco-system",
    "get-solution-id-from-meta",
]

QUICKSTARTS_ORDER = [
    "index",
    "get-started-as-partner",
    "register-as-tech-provider",
    "create-your-first-app",
    "generate-secret-and-token",
    "send-your-first-message",
    "partner-rate-limits",
]

ONBOARDING_ORDER = [
    "overview",
    "onboarding-apis",
    "understanding-webhooks-and-callback",
    "inbound-events-v2",
    "account-events",
    "billing-events",
    "message-events",
    "system-events",
    "user-events",
    "partner-hosted-embedded-sign-up-flow",
    "co-existence-closed-beta-phase",
    "coexistence-events",
    "coexistence-webhooks",
    "gupshup-ip-allowlisting",
    "tpp-partner-hosted-onboarding",
]

PARTNER_HUB_ORDER = [
    "overview",
    "get-started-with-partner-portal",
    "partner-portal-walkthrough",
    "wallet-1",
    "commissions",
    "support",
    "partner-customer-portal",
    "partner-wallet-balance-transfer",
    "wire-transfer-automation",
    "unused-commission-policy",
]

MESSAGING_ORDER = [
    "overview",
    "whatsapp-messages",
    "welcome-messages",
    "outbound-messages",
    "inbound-messages",
    "media-management",
    "marketing-messages-lite-mm-lite-api",
    "guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup",
    "obtain-user-call-permissions",
]

COMMERCE_ORDER = [
    "overview",
    "whatsapp-brazil-payments",
    "wallet-creation-kyc-flow-guide",
    "partner-usd-wire-transfers",
]

API_CATEGORIES = {
    "partner-management": {
        "title": "Partner Management",
        "summary": "Partner authentication, app listing, and linking applications.",
        "endpoints": [
            ("Get Partner Token", "post_partner-account-login"),
            ("Get Partner Apps", "get_partner-account-api-partnerapps"),
            ("Link App with Partner", "post_partner-account-api-applink"),
        ],
    },
    "channel-management": {
        "title": "Channel Management",
        "summary": "Create, update, and manage WABA channel applications.",
        "endpoints": [
            ("Create App", "post_partner-app"),
            ("Update application", "put_partner-app-appid"),
            ("Generate Embed Signed Link", "get_partner-app-appid-onboarding-embed-link"),
            ("Filter app list", "get_partner-app-list"),
        ],
    },
    "waba-account-management": {
        "title": "WABA Account Management",
        "summary": "WABA health, phone numbers, quality ratings, and account settings.",
        "endpoints": [
            ("Get Waba Info", "getwabahealth"),
            ("Check Health", "get_partner-app-appid-health"),
            ("Register phone", "registerphoneapp"),
        ],
    },
    "webhook-management": {
        "title": "Webhook Management",
        "summary": "Set up and manage webhook subscriptions and callback URLs.",
        "endpoints": [
            ("Set subscription", "setsubscription-api-v3"),
            ("Get All Subscriptions", "get_partner-app-appid-subscription"),
            ("Update App Subscription", "put_partner-app-appid-subscription-subscriptionid"),
        ],
    },
    "balance-and-usage": {
        "title": "Balance & Usage",
        "summary": "Wallet balance, commissions, usage, and billing APIs.",
        "endpoints": [
            ("Get Wallet Balance", "get_partner-app-appid-wallet-balance"),
            ("Get App's Daily Usage", "get_partner-app-appid-usage"),
            ("Get App's Daily Discount", "get_partner-app-appid-discount"),
        ],
    },
    "templates-management": {
        "title": "Templates Management",
        "summary": "Create, apply, manage, and send WhatsApp message templates.",
        "endpoints": [
            ("Get Templates", "get_partner-app-appid-templates"),
            ("Apply For Templates", "post_partner-app-appid-templates-6"),
            ("Delete Template", "delete_partner-app-appid-template-elementname"),
            ("Send msg With Template ID", "post_partner-app-appid-template-msg"),
        ],
    },
    "messaging-v3": {
        "title": "Messaging (V3)",
        "summary": "Send session messages — text, media, interactive, reactions, and more.",
        "endpoints": [
            ("Text Message", "post_partner-app-appid-v3-text-message"),
            ("Image Message", "post_partner-app-appid-v3-image-message"),
            ("Interactive Message", "post_partner-app-appid-v3-interactive-message"),
            ("Passthrough APIs overview", "passthrough-apis"),
        ],
    },
    "media-management": {
        "title": "Media Management",
        "summary": "Upload, download, and delete media for WhatsApp messages.",
        "endpoints": [
            ("Generate Media ID (file upload)", "post_partner-app-appid-media"),
            ("Download Media", "downloadmedia"),
            ("Delete media by ID", "delete_partner-app-appid-media-mediaid"),
        ],
    },
    "whatsapp-flows": {
        "title": "WhatsApp Flows",
        "summary": "Create, publish, and manage WhatsApp Flow experiences.",
        "endpoints": [
            ("Create Flow", "createflow"),
            ("Get All Flows", "getallflow"),
            ("Publish flow", "publishflow"),
        ],
    },
    "business-profile": {
        "title": "Business Profile",
        "summary": "Manage business profile, photo, and display name.",
        "endpoints": [
            ("Get Profile Details", "get_partner-app-appid-business-profile"),
            ("Update Profile Details", "put_partner-app-appid-business-profile"),
            ("Get Profile Picture", "get_partner-app-appid-business-profile-photo"),
        ],
    },
    "user-management": {
        "title": "User Management",
        "summary": "Block, unblock, and list blocked WhatsApp users.",
        "endpoints": [
            ("Get Blocked Users list", "get_partner-app-appid-user-blocklist"),
            ("Block Users", "post_partner-app-appid-user-block"),
            ("Unblock Users", "post_partner-app-appid-user-unblock"),
        ],
    },
    "marketing-messages-lite": {
        "title": "Marketing Messages Lite",
        "summary": "MM Lite enablement, sending, and insights.",
        "endpoints": [
            ("Enable MM Lite messages", "post_app-appid-mmlite-msg-enable"),
            ("MM Lite Send Message", "mmlitesendmessage"),
        ],
    },
}


def write_order(folder: Path, slugs: list[str]) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    existing = {p.stem for p in folder.glob("*.md")}
    ordered = [s for s in slugs if s in existing]
    ordered += sorted(existing - set(ordered))
    (folder / "_order.yaml").write_text(
        "\n".join(f"- {s}" for s in ordered) + "\n", encoding="utf-8"
    )


def rename_folders() -> None:
    for old, new in FOLDER_RENAMES.items():
        src = DOCS / old
        dst = DOCS / new
        if src.exists() and not dst.exists():
            shutil.move(str(src), str(dst))
            print(f"RENAMED: {old} → {new}")
        elif src.exists() and dst.exists():
            for item in src.iterdir():
                target = dst / item.name
                if not target.exists():
                    shutil.move(str(item), str(target))
            shutil.rmtree(src)
            print(f"MERGED: {old} → {new}")


def remove_stale_folders() -> None:
    stale = [
        "Partner Onboarding Guidance",
        "Partner Security",
        "Partner customer portal",
        "abc",
        "testing",
    ]
    for name in stale:
        path = DOCS / name
        if path.exists():
            # move any md files to partner-portal-hidden
            hidden = DOCS / "partner-portal-hidden"
            hidden.mkdir(exist_ok=True)
            for md in path.rglob("*.md"):
                dest = hidden / md.name
                if not dest.exists():
                    shutil.copy2(md, dest)
            shutil.rmtree(path)
            print(f"REMOVED stale: {name}")


def page(title: str, summary: str, body: str, hidden: bool = False) -> str:
    h = "true" if hidden else "false"
    return f"""---
title: {title}
summary: {summary}
excerpt: {summary}
deprecated: false
hidden: {h}
metadata:
  robots: index
---

{body.strip()}
"""


def create_section_overviews() -> None:
    write_order(DOCS / "get-started", GET_STARTED_ORDER)
    write_order(DOCS / "get-started" / "quickstarts", QUICKSTARTS_ORDER)
    write_order(DOCS / "onboarding", ONBOARDING_ORDER)
    write_order(DOCS / "partner-hub", PARTNER_HUB_ORDER)
    write_order(DOCS / "messaging", MESSAGING_ORDER)
    write_order(DOCS / "commerce-and-payments", COMMERCE_ORDER)

    (DOCS / "get-started" / "overview.md").write_text(
        page(
            "Overview",
            "Welcome to the Gupshup Partner Documentation Hub.",
            """# Gupshup Partner Developer Hub

Welcome to the Gupshup Partner Documentation — structured like [360dialog Partner Docs](https://docs.360dialog.com/partner), with all Gupshup content preserved.

## Start here

| Path | Description |
|------|-------------|
| [Quickstarts](quickstarts/) | 5 steps: signup → first message |
| [Partner API](/reference/partner-api-overview) | APIs grouped by business capability |
| [Partner Hub](../partner-hub/support) | Wallet, billing, and support |
| [Onboarding](../onboarding/) | Webhooks, events, and onboarding |

## Partner journey

1. [Get Started as a Partner](/docs/get-started-as-partner)
2. [Register as Tech Provider](/docs/register-as-tech-provider)
3. [Create your first App](/docs/create-your-first-app)
4. [Generate Secret and Token](/docs/generate-secret-and-token)
5. [Send your first message](/docs/send-your-first-message)

## Documentation sections

| Section | What it covers |
|---------|----------------|
| **Get Started** | Overview, pricing, quickstarts, Tech Provider program |
| **Onboarding** | Webhooks, events, coexistence, onboarding APIs |
| **Partner API** | REST APIs by category |
| **Partner Hub** | Portal UI, wallet, billing, support |
| **Messaging** | Templates, session messages, media, voice |
| **Commerce & Payments** | Brazil payments, INR wallet, wire transfers |
""",
        ),
        encoding="utf-8",
    )

    qs_index = DOCS / "get-started" / "quickstarts" / "index.md"
    qs_index.write_text(
        page(
            "Quickstarts",
            "Five steps from partner signup to your first WhatsApp message.",
            """# Quickstarts

| Step | Guide | Outcome |
|------|-------|---------|
| 1 | [Get Started as a Partner](/docs/get-started-as-partner) | Partner account and portal access |
| 2 | [Register as Tech Provider](/docs/register-as-tech-provider) | Meta Tech Provider setup |
| 3 | [Create your first App](/docs/create-your-first-app) | WABA onboarded via Partner Portal |
| 4 | [Generate Secret and Token](/docs/generate-secret-and-token) | API credentials |
| 5 | [Send your first message](/docs/send-your-first-message) | First WhatsApp message |
""",
        ),
        encoding="utf-8",
    )

    (DOCS / "onboarding" / "overview.md").write_text(
        page(
            "Onboarding Overview",
            "Integrate with Gupshup: apps, webhooks, events, and coexistence.",
            """# Onboarding

| Topic | Guide |
|-------|-------|
| Onboarding APIs | [Onboarding APIs](/docs/onboarding-apis) |
| Webhooks | [Understanding Webhooks](/docs/understanding-webhooks-and-callback) |
| Events (V2) | [Inbound Events V2](/docs/inbound-events-v2) |
| Coexistence | [Coexistence](/docs/co-existence-closed-beta-phase) |
| Embedded Signup | [Partner Hosted Embedded Sign Up](/docs/partner-hosted-embedded-sign-up-flow) |
""",
        ),
        encoding="utf-8",
    )

    (DOCS / "partner-hub" / "overview.md").write_text(
        page(
            "Partner Hub Overview",
            "Partner Portal UI for managing apps, customers, and billing.",
            """# Partner Hub

| Topic | Guide |
|-------|-------|
| Portal walkthrough | [Partner Portal Walkthrough](/docs/partner-portal-walkthrough) |
| Wallet & billing | [Wallet](/docs/wallet-1) |
| Support | [Support](/docs/support) |
| Customer portal | [Partner Customer Portal](/docs/partner-customer-portal) |
""",
        ),
        encoding="utf-8",
    )

    (DOCS / "messaging" / "overview.md").write_text(
        page(
            "Messaging Overview",
            "Send and receive WhatsApp messages, templates, media, and voice.",
            """# Messaging

| Topic | Guide |
|-------|-------|
| WhatsApp Messages | [WhatsApp Messages](/docs/whatsapp-messages) |
| Media | [Media Management](/docs/media-management) |
| MM Lite | [Marketing Messages Lite](/docs/marketing-messages-lite-mm-lite-api) |
| Voice (Outbound) | [Voice Outbound](/docs/guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup) |

## Related API categories

- [Templates Management](/reference/templates-management)
- [Messaging (V3)](/reference/messaging-v3)
- [Media Management](/reference/media-management)
""",
        ),
        encoding="utf-8",
    )

    (DOCS / "commerce-and-payments" / "overview.md").write_text(
        page(
            "Commerce & Payments Overview",
            "Payments, wallet, and billing for partner commerce.",
            """# Commerce & Payments

| Topic | Guide |
|-------|-------|
| Brazil Payments | [WhatsApp Brazil Payments](/docs/whatsapp-brazil-payments) |
| INR Wallet | [INR Wallet KYC Flow](/docs/wallet-creation-kyc-flow-guide) |
| Wire Transfers | [USD Wire Transfers](/docs/partner-usd-wire-transfers) |
""",
        ),
        encoding="utf-8",
    )


def create_partner_api_docs_section() -> None:
    """docs/partner-api/ — 360-style API intro + category hubs (links to reference/)."""
    api_docs = DOCS / "partner-api"
    api_ref = api_docs / "api-reference"
    api_ref.mkdir(parents=True, exist_ok=True)

    (api_docs / "overview.md").write_text(
        page(
            "Partner API Overview",
            "REST APIs for partner integrations with Gupshup.",
            """# Partner API

Gupshup exposes Partner APIs for building branded customer experiences on WhatsApp.

## API Reference

Endpoints are grouped by **business capability** (like 360dialog):

→ [API Reference](api-reference/overview)

## Authentication

All requests require a partner token. See [Generate Secret and Token](/docs/generate-secret-and-token).

## Base URL

Use the base URL shown in your Partner Portal API settings.
""",
        ),
        encoding="utf-8",
    )

    (api_docs / "authentication.md").write_text(
        page(
            "Authentication",
            "Partner API authentication with secret and token.",
            """# Authentication

Partner APIs use a **partner token** obtained via your client secret.

1. Generate a secret in Partner Portal → [Generate Secret and Token](/docs/generate-secret-and-token)
2. Exchange secret for token via [Get Partner Token](/reference/post_partner-account-login)
3. Pass token in API requests as documented per endpoint
""",
        ),
        encoding="utf-8",
    )

    write_order(api_docs, ["overview", "authentication", "api-reference"])

    # Category hub pages
    ref_slugs = {p.stem for p in (ROOT / "reference").rglob("*.md")}
    cat_order = ["overview"]
    for slug, meta in API_CATEGORIES.items():
        cat_order.append(slug)
        lines = [
            f"# {meta['title']}",
            "",
            meta["summary"],
            "",
            "| API | Reference |",
            "|-----|-----------|",
        ]
        for name, ref_slug in meta["endpoints"]:
            if ref_slug in ref_slugs:
                lines.append(f"| {name} | [/reference/{ref_slug}](/reference/{ref_slug}) |")
            else:
                lines.append(f"| {name} | *(see Partner APIs folder)* |")
        lines.append("")
        (api_ref / f"{slug}.md").write_text(
            page(meta["title"], meta["summary"], "\n".join(lines)),
            encoding="utf-8",
        )

    (api_ref / "overview.md").write_text(
        page(
            "API Reference",
            "Partner API endpoints grouped by business category.",
            """# API Reference

| Category | Description |
|----------|-------------|
| [Partner Management](partner-management) | Login, apps, linking |
| [Channel Management](channel-management) | Create and manage WABA apps |
| [WABA Account Management](waba-account-management) | Health, phone, quality |
| [Webhook Management](webhook-management) | Subscriptions and callbacks |
| [Balance & Usage](balance-and-usage) | Wallet and billing |
| [Templates Management](templates-management) | Message templates |
| [Messaging (V3)](messaging-v3) | Session messages |
| [Media Management](media-management) | Media upload/download |
| [WhatsApp Flows](whatsapp-flows) | Flow lifecycle |
| [Business Profile](business-profile) | Profile and display name |
| [User Management](user-management) | Block/unblock users |
| [Marketing Messages Lite](marketing-messages-lite) | MM Lite |
""",
        ),
        encoding="utf-8",
    )
    write_order(api_ref, cat_order)


def fix_reference_section() -> None:
    api_root = ROOT / "reference" / "Partner APIs"

    # Rename overview to unique slug to avoid 404 conflicts
    overview = api_root / "overview.md"
    new_overview = api_root / "partner-api-overview.md"
    if overview.exists() and not new_overview.exists():
        shutil.move(str(overview), str(new_overview))

    body = """# Partner API

Gupshup Partner APIs let you build branded WhatsApp experiences. Endpoints are grouped by business category.

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

See [Generate Secret and Token](/docs/generate-secret-and-token) and [Get Partner Token](/reference/post_partner-account-login).
"""
    new_overview.write_text(
        page("Partner API Overview", "Gupshup Partner API reference organized by category.", body),
        encoding="utf-8",
    )

    # Fix category hub index pages with /reference/ links
    ref_slugs = {p.stem for p in (ROOT / "reference").rglob("*.md")}
    for slug, meta in API_CATEGORIES.items():
        cat_dir = api_root / slug
        cat_dir.mkdir(exist_ok=True)
        lines = [f"# {meta['title']}", "", meta["summary"], "", "## Endpoints", ""]
        for name, ref_slug in meta["endpoints"]:
            if ref_slug in ref_slugs:
                lines.append(f"- [{name}](/reference/{ref_slug})")
        lines.append("")
        (cat_dir / "index.md").write_text(
            page(meta["title"], meta["summary"], "\n".join(lines)),
            encoding="utf-8",
        )

    # Update Partner APIs order — categories first, then legacy folders
    cat_slugs = ["partner-api-overview"] + list(API_CATEGORIES.keys())
    legacy = [
        "partner-app-management", "template-apis", "app-onboarding-apis",
        "partner-meta-and-whatsapp-apis", "mmliteapi", "auth-template-v2",
        "message-searcher-apis", "apikey-regeneration-apis",
        "solution-migrate-intent-api", "type-indicator", "default-1",
    ]
    order = cat_slugs + [s for s in legacy if (api_root / s).exists()]
    write_order(api_root, order)

    # Reference root — Partner APIs first
    ref_order_path = ROOT / "reference" / "_order.yaml"
    ref_order_path.write_text(
        "- Partner APIs\n"
        + "\n".join(
            f"- {line.lstrip('- ')}"
            for line in ref_order_path.read_text().splitlines()
            if line.strip() and "Partner APIs" not in line
        )
        + "\n",
        encoding="utf-8",
    )


def update_docs_root_order() -> None:
    existing = {p.name for p in DOCS.iterdir() if p.is_dir()}
    order = [s for s in DOCS_ORDER if s in existing]
    (DOCS / "_order.yaml").write_text(
        "\n".join(f"- {s}" for s in order) + "\n", encoding="utf-8"
    )


def add_summary_to_pages() -> None:
    """Ensure pages have summary field for ReadMe git sync."""
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        if "summary:" in text.split("---", 2)[1]:
            continue
        m = re.search(r"^title:\s*(.+)$", text, re.M)
        title = m.group(1).strip() if m else md.stem.replace("-", " ").title()
        em = re.search(r"^excerpt:\s*['\"]?(.*?)['\"]?\s*$", text, re.M)
        summary = em.group(1).strip() if em and em.group(1).strip() else title
        text = text.replace("---\n", f"---\nsummary: {summary}\n", 1)
        md.write_text(text, encoding="utf-8")


def main() -> None:
    print("=== Rename folders to kebab-case ===")
    rename_folders()
    print("\n=== Remove stale categories ===")
    remove_stale_folders()
    print("\n=== Create section overviews ===")
    create_section_overviews()
    print("\n=== Create partner-api docs section ===")
    create_partner_api_docs_section()
    print("\n=== Fix reference section ===")
    fix_reference_section()
    print("\n=== Update root order ===")
    update_docs_root_order()
    print("\n=== Add summary frontmatter ===")
    add_summary_to_pages()
    print("\nDone. Push to GitHub to sync ReadMe.")


if __name__ == "__main__":
    main()
