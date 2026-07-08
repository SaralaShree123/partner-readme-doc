#!/usr/bin/env python3
"""
Fix ReadMe overview collisions + API reference structure to match 360dialog.

Root cause: ReadMe Git sync maps file STEMS to URL slugs. Multiple
docs/**/overview.md files all become /docs/overview — so Onboarding/Messaging
"Overview" opens the same page (often looking like Pricing/landing mix).

Fix: keep ONE overview.md (Get Started landing). Rename every other overview
to a unique filename that matches its intended slug.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REF = ROOT / "reference"


def page(title: str, summary: str, body: str, slug: str, hidden: bool = False) -> str:
    return f"""---
title: {title}
summary: {summary}
excerpt: {summary}
deprecated: false
hidden: {'true' if hidden else 'false'}
metadata:
  robots: index
slug: {slug}
---

{body.strip()}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT)}")


def rewrite_order(folder: Path, renames: dict[str, str]) -> None:
    order = folder / "_order.yaml"
    if not order.exists():
        return
    lines = []
    for line in order.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\s*-\s*)(.+)$", line)
        if m:
            prefix, name = m.group(1), m.group(2).strip()
            name = renames.get(name, name)
            lines.append(f"{prefix}{name}")
        else:
            lines.append(line)
    order.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"ORDER {order.relative_to(ROOT)}")


def rename_overview_files() -> None:
    """Keep only get-started/overview.md as filename overview.md."""
    renames = {
        DOCS / "onboarding" / "overview.md": ("onboarding-overview.md", "onboarding-overview"),
        DOCS / "partner-hub" / "overview.md": ("partner-hub-overview.md", "partner-hub-overview"),
        DOCS / "messaging" / "overview.md": ("messaging-overview.md", "messaging-overview"),
        DOCS / "commerce-and-payments" / "overview.md": ("commerce-overview.md", "commerce-overview"),
        DOCS / "security" / "overview.md": ("security-overview.md", "security-overview"),
        DOCS / "meta-whatsapp-features" / "overview.md": (
            "meta-whatsapp-features-overview.md",
            "meta-whatsapp-features-overview",
        ),
        DOCS / "partner-api" / "overview.md": ("partner-api-overview.md", "partner-api-overview"),
        DOCS / "partner-api" / "api-reference" / "overview.md": (
            "api-reference-overview.md",
            "api-reference-overview",
        ),
    }

    for src, (new_name, slug) in renames.items():
        if not src.exists():
            print(f"SKIP missing {src}")
            continue
        dst = src.with_name(new_name)
        text = src.read_text(encoding="utf-8")
        # ensure slug matches filename
        if re.search(r"^slug:\s*.+$", text, re.M):
            text = re.sub(r"^slug:\s*.+$", f"slug: {slug}", text, count=1, flags=re.M)
        else:
            text = text.replace("---\n", f"---\nslug: {slug}\n", 1)
        if dst.exists() and dst != src:
            dst.unlink()
        src.write_text(text, encoding="utf-8")
        src.rename(dst)
        print(f"RENAME {src.relative_to(ROOT)} → {dst.relative_to(ROOT)}")
        rewrite_order(src.parent, {"overview": slug})

    # Also update partner-api/_order.yaml: overview → partner-api-overview
    rewrite_order(DOCS / "partner-api", {"overview": "partner-api-overview"})
    rewrite_order(DOCS / "partner-api" / "api-reference", {"overview": "api-reference-overview"})


def rewrite_landing_overview() -> None:
    """360dialog-style landing — unique filename stays overview.md under get-started only."""
    write(
        DOCS / "get-started" / "overview.md",
        page(
            "Overview",
            "Welcome to the Gupshup Partner Documentation Hub",
            """# Overview

This documentation is a central resource for current and prospective **Gupshup integration partners**. It provides the technical and operational guidance needed to build, launch, and scale WhatsApp Business API solutions using the Gupshup platform.

> 📘 **For Gupshup Partners**
>
> This documentation is intended for Gupshup Partners and focuses on partner-specific concepts, workflows, and integration requirements.
>
> Sign up at [partner.gupshup.io](https://partner.gupshup.io/).

---

## Get started

Kick off your Partner journey with quick access to the most essential guides and tools.

| Resource | Description |
|----------|-------------|
| [Quickstarts](/docs/quickstarts) | Five steps from signup to your first WhatsApp message |
| [Partner API Reference](/docs/api-reference-overview) | Explore APIs grouped by business capability |
| [Partner Portal](https://partner.gupshup.io/) | Manage apps, customers, and integrations |
| [Support](/docs/support) | Help and escalation paths |

---

## Who is Gupshup for?

| Partner Type | How They Benefit from Gupshup |
|--------------|-------------------------------|
| SaaS Platforms | Add WhatsApp messaging into your product and automate client workflows |
| Enterprises | Deploy large-scale messaging for sales, marketing, and support use cases |
| Agencies & Developers | Build WhatsApp-powered solutions and tools |
| ISVs | Become a Meta Tech Provider with Gupshup’s partner platform |

---

## How it works

Gupshup provides a developer-first, API-driven approach to WhatsApp Business messaging. Integrate, onboard clients, and manage messaging workflows in a scalable partner ecosystem.

### Partner journey

1. **Set up your Partner account** — Create a partner account and start testing → [Get Started as a Partner](/docs/get-started-as-partner)
2. **Integrate Partner APIs** — Generate credentials and authenticate → [Generate Secret and Token](/docs/generate-secret-and-token)
3. **Onboard clients & manage WABAs** — Create apps and connect numbers → [Create your first App](/docs/create-your-first-app)
4. **Scale & optimise messaging** — Send messages and grow → [Send your first message](/docs/send-your-first-message)

---

## Documentation sections

| Section | What it covers |
|---------|----------------|
| [Get Started](/docs/overview) | Landing, quickstarts, pricing, Tech Provider program |
| [Onboarding](/docs/onboarding-overview) | Webhooks, events, coexistence, onboarding APIs |
| [Partner API](/docs/partner-api-overview) | REST APIs by category |
| [Partner Hub](/docs/partner-hub-overview) | Portal UI, wallet, support |
| [Messaging](/docs/messaging-overview) | Templates, session messages, media, voice |
| [Commerce & Payments](/docs/commerce-overview) | Brazil payments, INR wallet, wire transfers |

---

## Next steps

| | |
|---|---|
| [Explore Quickstarts](/docs/quickstarts) | Five steps to your first message |
| [See Pricing](/docs/pricing) | Costs associated with becoming a Gupshup Partner |
| [Learn About Tech Providers](/docs/what-is-sp-tp) | Solution Partners & Tech Providers |
""",
            slug="overview",
        ),
    )


def rebuild_section_hubs() -> None:
    """Ensure renamed hub pages have correct body + unique content (not pricing)."""
    write(
        DOCS / "onboarding" / "onboarding-overview.md",
        page(
            "Onboarding Overview",
            "Integrate with Gupshup: apps, webhooks, events, and coexistence.",
            """# Onboarding

Guides for integrating with the Gupshup Partner Platform — credentials, webhooks, events, and advanced onboarding.

## Core topics

| Topic | Guide |
|-------|-------|
| Onboarding APIs | [Onboarding APIs](/docs/onboarding-apis) |
| Webhooks & callbacks | [Understanding Webhooks](/docs/understanding-webhooks-and-callback) |
| Inbound events (V2) | [Inbound events (V2)](/docs/inbound-events-v2) |
| Incoming events (V3) | [Incoming Events (V3)](/docs/v3-events) |
| Coexistence | [Coexistence](/docs/co-existence-closed-beta-phase) |
| Embedded signup | [Partner Hosted Embedded Sign Up](/docs/partner-hosted-embedded-sign-up-flow) |
| IP allowlisting | [Gupshup IP Allowlisting](/docs/gupshup-ip-allowlisting) |

## Event guides

| Event type | Guide |
|------------|-------|
| Account events | [Account events](/docs/account-events) |
| Billing events | [Billing events](/docs/billing-events) |
| Message events | [Message events](/docs/message-events) |
| System events | [System events](/docs/system-events) |
| User events | [User events](/docs/user-events) |
""",
            slug="onboarding-overview",
        ),
    )

    write(
        DOCS / "partner-hub" / "partner-hub-overview.md",
        page(
            "Partner Hub Overview",
            "Partner Portal UI for managing apps, customers, and billing.",
            """# Partner Hub

The Gupshup Partner Portal is your control center for WhatsApp partner operations.

## Portal guides

| Topic | Guide |
|-------|-------|
| Get started | [Get started with Partner Portal](/docs/get-started-with-partner-portal) |
| Walkthrough | [Partner Portal Walkthrough](/docs/partner-portal-walkthrough) |
| Wallet | [Wallet](/docs/wallet-1) |
| Commissions | [Commissions / Wallet Overview](/docs/commissions) |
| Support | [Support](/docs/support) |
| Customer portal | [Partner Customer Portal](/docs/partner-customer-portal) |
""",
            slug="partner-hub-overview",
        ),
    )

    write(
        DOCS / "messaging" / "messaging-overview.md",
        page(
            "Messaging Overview",
            "Send and receive WhatsApp messages, templates, media, and voice.",
            """# Messaging

Guides for sending and receiving WhatsApp messages on the Gupshup Partner Platform.

| Topic | Guide |
|-------|-------|
| WhatsApp Messages | [WhatsApp Messages](/docs/whatsapp-messages) |
| Outbound messages | [Outbound messages](/docs/outbound-messages) |
| Inbound messages | [Inbound Messages](/docs/inbound-messages) |
| Media | [Media Management](/docs/media-management) |
| Marketing Messages Lite | [MM Lite](/docs/marketing-messages-lite-mm-lite-api) |
| Voice (Outbound) | [Voice Outbound & SIP](/docs/guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup) |

## Related API categories

- [Templates Management](/docs/templates-management)
- [Messaging (V3)](/docs/messaging-v3)
- [Media Management](/docs/media-management)
""",
            slug="messaging-overview",
        ),
    )

    write(
        DOCS / "commerce-and-payments" / "commerce-overview.md",
        page(
            "Commerce & Payments Overview",
            "Payments, wallet, and billing for partner commerce.",
            """# Commerce & Payments

| Topic | Guide |
|-------|-------|
| Brazil Payments | [WhatsApp Brazil Payments](/docs/whatsapp-brazil-payments) |
| INR Wallet & KYC | [INR Wallet Creation & KYC Flow](/docs/wallet-creation-kyc-flow-guide) |
| USD Wire Transfers | [Partner USD Wire Transfers](/docs/partner-usd-wire-transfers) |
""",
            slug="commerce-overview",
        ),
    )

    write(
        DOCS / "security" / "security-overview.md",
        page(
            "Security Overview",
            "Partner Portal security, authentication, and best practices.",
            """# Security

| Topic | Guide |
|-------|-------|
| Portal security | [Security in Partner Portal](/docs/security-in-partner-portal) |
| Google Authenticator | [Google Authenticator](/docs/google-authenticator-for-partner-portal) |
| Authy | [Authy Authenticator](/docs/authy-authenticator-app-for-partner-portal) |
| Security wizard | [Security Wizard](/docs/comprehensive-step-by-step-guide-for-the-partner-portal-security-wizard) |
| JWT | [Signing the JWT Token](/docs/signing-the-jwt-token-test-jwt-step) |
| API key rotation | [Account API Key Rotation](/docs/account-api-key-rotation-security-wizard) |
""",
            slug="security-overview",
        ),
    )

    write(
        DOCS / "meta-whatsapp-features" / "meta-whatsapp-features-overview.md",
        page(
            "Meta WhatsApp Features Overview",
            "Meta WhatsApp platform features for partners.",
            """# Meta WhatsApp Features

| Topic | Guide |
|-------|-------|
| BSUID | [BSUID](/docs/bsuid) |
| Enable BSUID flag | [API to enable BSUID flag](/docs/api-to-enable-bsuid-flag-for-an-app) |
""",
            slug="meta-whatsapp-features-overview",
        ),
    )


def rebuild_partner_api_guides() -> None:
    """Match 360 Partner API: Overview → Authentication → API Reference categories."""
    write(
        DOCS / "partner-api" / "partner-api-overview.md",
        page(
            "Partner API Overview",
            "REST APIs for partner integrations with Gupshup.",
            """# Partner API

Gupshup Partner APIs let you build branded WhatsApp experiences for your customers. Endpoints are organized by **business capability**, similar to [360dialog Partner API](https://docs.360dialog.com/partner/partner-api).

## Start here

| | |
|---|---|
| [Authentication](/docs/authentication) | Partner token and app access token |
| [API Reference](/docs/api-reference-overview) | All categories and endpoints |

## API categories

| Category | Description |
|----------|-------------|
| [Partner Management](/docs/partner-management) | Login, apps, linking |
| [Channel Management](/docs/channel-management) | Create and manage WABA apps |
| [WABA Account Management](/docs/waba-account-management) | Health, phone, quality |
| [Webhook Management](/docs/webhook-management) | Subscriptions and callbacks |
| [Balance & Usage](/docs/balance-and-usage) | Wallet and billing APIs |
| [Templates Management](/docs/templates-management) | Create and send templates |
| [Messaging (V3)](/docs/messaging-v3) | Session / passthrough messages |
| [Media Management](/docs/media-management) | Upload / download media |
| [WhatsApp Flows](/docs/whatsapp-flows) | Flow lifecycle |
| [Business Profile](/docs/business-profile) | Profile and display name |
| [User Management](/docs/user-management) | Block / unblock users |
| [Marketing Messages Lite](/docs/marketing-messages-lite) | MM Lite |

## Interactive Try It

Full request/response schemas live under **API Reference** in the top nav → [Partner API Overview](/reference/partner-api-overview).
""",
            slug="partner-api-overview",
        ),
    )

    write(
        DOCS / "partner-api" / "authentication.md",
        page(
            "Authentication",
            "How to authenticate Partner API requests.",
            """# Authentication

## Partner token

1. In Partner Portal go to **Settings → API client details**
2. Generate a **client secret**
3. Call [Get Partner Token](/reference/post_partner-account-login) with the secret in the `password` parameter
4. Use the returned token on subsequent Partner API calls

Step-by-step UI guide: [Generate Secret and Token](/docs/generate-secret-and-token)

## App access token

For app-level APIs, use [Get Access Token for an App](/reference/get_partner-app-appid-token).

## Related

- [Partner Management](/docs/partner-management)
- [Security Overview](/docs/security-overview)
""",
            slug="authentication",
        ),
    )

    write(
        DOCS / "partner-api" / "api-reference" / "api-reference-overview.md",
        page(
            "API Reference",
            "Partner API endpoints grouped by business category.",
            """# API Reference

Available endpoints, authentication, and category groups for the Gupshup Partner API.

| Category | Description |
|----------|-------------|
| [Partner Management](/docs/partner-management) | Login, apps, linking |
| [Channel Management](/docs/channel-management) | Create and manage WABA apps |
| [WABA Account Management](/docs/waba-account-management) | Health, phone, quality |
| [Webhook Management](/docs/webhook-management) | Subscriptions and callbacks |
| [Balance & Usage](/docs/balance-and-usage) | Wallet and billing |
| [Templates Management](/docs/templates-management) | Message templates |
| [Messaging (V3)](/docs/messaging-v3) | Session messages |
| [Media Management](/docs/media-management) | Media upload/download |
| [WhatsApp Flows](/docs/whatsapp-flows) | Flow lifecycle |
| [Business Profile](/docs/business-profile) | Profile and display name |
| [User Management](/docs/user-management) | Block/unblock users |
| [Marketing Messages Lite](/docs/marketing-messages-lite) | MM Lite |

For interactive Try It and OpenAPI schemas, open the **API Reference** tab → [Partner API Overview](/reference/partner-api-overview).
""",
            slug="api-reference-overview",
        ),
    )

    # Category hubs — 360 style: description + endpoint list with reference links
    categories = {
        "partner-management": (
            "Partner Management",
            "Endpoints for managing partner accounts, authentication, and app linking.",
            [
                ("Get Partner Token", "post_partner-account-login", "Authenticate and obtain a partner token."),
                ("Get Partner Apps", "get_partner-account-api-partnerapps", "List apps linked to the partner."),
                ("Link App with Partner", "post_partner-account-api-applink", "Link an application to the partner."),
            ],
        ),
        "channel-management": (
            "Channel Management",
            "Endpoints for creating and managing WABA channel applications.",
            [
                ("Create App", "post_partner-app", "Create a new partner application."),
                ("Update application", "put_partner-app-appid", "Update an existing application."),
                ("Generate Embed Signed Link", "get_partner-app-appid-onboarding-embed-link", "Create an embed onboarding link."),
                ("Filter app list", "get_partner-app-list", "Filter and list partner apps."),
            ],
        ),
        "waba-account-management": (
            "WABA Account Management",
            "Endpoints for WABA health, phone registration, and account quality.",
            [
                ("Get Waba Info", "getwabahealth", "Retrieve WABA health information."),
                ("Check Health", "get_partner-app-appid-health", "Check app/channel health."),
                ("Register phone", "registerphoneapp", "Register a phone number for an app."),
            ],
        ),
        "webhook-management": (
            "Webhook Management",
            "Endpoints for webhook subscriptions and callbacks.",
            [
                ("Set subscription", "setsubscription-api-v3", "Create a webhook subscription."),
                ("Get All Subscriptions", "get_partner-app-appid-subscription", "List subscriptions for an app."),
                ("Update App Subscription", "put_partner-app-appid-subscription-subscriptionid", "Update a subscription."),
            ],
        ),
        "balance-and-usage": (
            "Balance & Usage",
            "Endpoints for wallet balance, usage, and discounts.",
            [
                ("Get Wallet Balance", "get_partner-app-appid-wallet-balance", "Get wallet balance for an app."),
                ("Get App's Daily Usage", "get_partner-app-appid-usage", "Get daily usage."),
                ("Get App's Daily Discount", "get_partner-app-appid-discount", "Get daily discount."),
            ],
        ),
        "templates-management": (
            "Templates Management",
            "Endpoints for creating, managing, and sending WhatsApp message templates.",
            [
                ("Get Templates", "get_partner-app-appid-templates", "List templates for an app."),
                ("Apply For Templates", "post_partner-app-appid-templates-6", "Submit a template for approval."),
                ("Delete Template", "delete_partner-app-appid-template-elementname", "Delete a template."),
                ("Send msg With Template ID", "post_partner-app-appid-template-msg", "Send a template message."),
            ],
        ),
        "messaging-v3": (
            "Messaging (V3)",
            "Endpoints for sending session (passthrough) messages.",
            [
                ("Text Message", "post_partner-app-appid-v3-text-message", "Send a text session message."),
                ("Image Message", "post_partner-app-appid-v3-image-message", "Send an image session message."),
                ("Interactive Message", "post_partner-app-appid-v3-interactive-message", "Send an interactive message."),
                ("Reaction Message", "post_partner-app-appid-v3-reaction-message", "Send a reaction."),
            ],
        ),
        "media-management": (
            "Media Management",
            "Endpoints for uploading, downloading, and deleting media.",
            [
                ("Generate Media ID (file upload)", "post_partner-app-appid-media", "Upload media and get a media ID."),
                ("Download Media", "downloadmedia", "Download media by ID."),
                ("Delete media by ID", "delete_partner-app-appid-media-mediaid", "Delete media."),
            ],
        ),
        "whatsapp-flows": (
            "WhatsApp Flows",
            "Endpoints for creating, publishing, and managing WhatsApp Flows.",
            [
                ("Create Flow", "createflow", "Create a flow."),
                ("Get All Flows", "getallflow", "List flows."),
                ("Publish flow", "publishflow", "Publish a flow."),
            ],
        ),
        "business-profile": (
            "Business Profile",
            "Endpoints for business profile and display name.",
            [
                ("Get Profile Details", "get_partner-app-appid-business-profile", "Get business profile."),
                ("Update Profile Details", "put_partner-app-appid-business-profile", "Update business profile."),
                ("Get Profile Picture", "get_partner-app-appid-business-profile-photo", "Get profile photo."),
            ],
        ),
        "user-management": (
            "User Management",
            "Endpoints for blocking and unblocking WhatsApp users.",
            [
                ("Get Blocked Users list", "get_partner-app-appid-user-blocklist", "List blocked users."),
                ("Block Users", "post_partner-app-appid-user-block", "Block users."),
                ("Unblock Users", "post_partner-app-appid-user-unblock", "Unblock users."),
            ],
        ),
        "marketing-messages-lite": (
            "Marketing Messages Lite",
            "Endpoints for MM Lite enablement and sending.",
            [
                ("Enable MM Lite messages", "post_app-appid-mmlite-msg-enable", "Enable MM Lite for an app."),
                ("MM Lite Send Message", "mmlitesendmessage", "Send an MM Lite message."),
            ],
        ),
    }

    ref_slugs = {p.stem for p in REF.rglob("*.md")}
    order_slugs = ["api-reference-overview"]

    for slug, (title, summary, endpoints) in categories.items():
        order_slugs.append(slug)
        parts = [f"# {title}", "", summary, ""]
        for name, ref_slug, desc in endpoints:
            parts += [f"## {name}", "", f"> {desc}", ""]
            if ref_slug in ref_slugs:
                parts.append(f"→ Full endpoint & Try It: [/reference/{ref_slug}](/reference/{ref_slug})")
            else:
                parts.append(f"→ See API Reference for `{ref_slug}`")
            parts.append("")
        body = "\n".join(parts)

        write(DOCS / "partner-api" / "api-reference" / f"{slug}.md", page(title, summary, body, slug=slug))

        # Mirror under Reference tab category hub
        write(REF / "Partner APIs" / slug / "index.md", page(title, summary, body, slug=slug))

    (DOCS / "partner-api" / "api-reference" / "_order.yaml").write_text(
        "\n".join(f"- {s}" for s in order_slugs) + "\n", encoding="utf-8"
    )
    (DOCS / "partner-api" / "_order.yaml").write_text(
        "- partner-api-overview\n- authentication\n- api-reference\n", encoding="utf-8"
    )

    # Reference Partner APIs order: categories first, legacy last
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
    ref_order = ["partner-api-overview"] + list(categories.keys()) + [
        x for x in legacy if (REF / "Partner APIs" / x).exists()
    ]
    (REF / "Partner APIs" / "_order.yaml").write_text(
        "\n".join(f"- {s}" for s in ref_order) + "\n", encoding="utf-8"
    )

    write(
        REF / "Partner APIs" / "partner-api-overview.md",
        page(
            "Partner API Overview",
            "Gupshup Partner API reference organized by business category.",
            """# Partner API

Gupshup Partner APIs are grouped by business category (same model as 360dialog Partner API Reference).

| Category | Description |
|----------|-------------|
| [Partner Management](partner-management/) | Login, apps, linking |
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

1. [Generate Secret and Token](/docs/generate-secret-and-token)
2. [Get Partner Token](/reference/post_partner-account-login)

## Guides

- [Partner API Overview (Guides)](/docs/partner-api-overview)
- [API Reference (Guides)](/docs/api-reference-overview)
""",
            slug="partner-api-overview",
        ),
    )


def update_section_orders() -> None:
    orders = {
        "onboarding": [
            "onboarding-overview",
            "onboarding-apis",
            "understanding-webhooks-and-callback",
            "inbound-events-v2",
            "v3-events",
            "partner-hosted-embedded-sign-up-flow",
            "co-existence-closed-beta-phase",
            "gupshup-ip-allowlisting",
        ],
        "partner-hub": [
            "partner-hub-overview",
            "get-started-with-partner-portal",
            "partner-portal-walkthrough",
            "wallet-1",
            "commissions",
            "support",
            "partner-customer-portal",
        ],
        "messaging": [
            "messaging-overview",
            "whatsapp-messages",
            "outbound-messages",
            "inbound-messages",
            "media-management",
            "marketing-messages-lite-mm-lite-api",
        ],
        "commerce-and-payments": [
            "commerce-overview",
            "whatsapp-brazil-payments",
            "wallet-creation-kyc-flow-guide",
            "partner-usd-wire-transfers",
        ],
        "security": [
            "security-overview",
            "security-in-partner-portal",
            "google-authenticator-for-partner-portal",
            "authy-authenticator-app-for-partner-portal",
            "comprehensive-step-by-step-guide-for-the-partner-portal-security-wizard",
        ],
        "meta-whatsapp-features": [
            "meta-whatsapp-features-overview",
            "bsuid",
            "api-to-enable-bsuid-flag-for-an-app",
        ],
        "get-started": [
            "overview",
            "quickstarts",
            "gupshup-partner-eco-system",
            "what-is-sp-tp",
            "pricing",
            "get-solution-id-from-meta",
        ],
    }
    for folder, preferred in orders.items():
        path = DOCS / folder
        if not path.exists():
            continue
        existing = {p.stem for p in path.glob("*.md")}
        ordered = [s for s in preferred if s in existing]
        ordered += sorted(existing - set(ordered))
        (path / "_order.yaml").write_text("\n".join(f"- {s}" for s in ordered) + "\n", encoding="utf-8")
        print(f"ORDER docs/{folder}/_order.yaml")


def assert_unique_overview_filename() -> None:
    overs = list(DOCS.rglob("overview.md"))
    print("Remaining overview.md files:")
    for p in overs:
        print(f"  {p.relative_to(ROOT)}")
    assert len(overs) == 1, f"Expected exactly 1 overview.md, found {len(overs)}: {overs}"
    assert overs[0] == DOCS / "get-started" / "overview.md"


def main() -> None:
    rename_overview_files()
    rewrite_landing_overview()
    rebuild_section_hubs()
    rebuild_partner_api_guides()
    update_section_orders()
    assert_unique_overview_filename()
    print("\nOK: only get-started/overview.md remains as overview.md")


if __name__ == "__main__":
    main()
