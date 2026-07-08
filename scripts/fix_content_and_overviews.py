#!/usr/bin/env python3
"""Fix overview pages, quickstarts, and API reference content for 360dialog-style redesign."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def page(title: str, summary: str, body: str, slug: str | None = None, hidden: bool = False) -> str:
    lines = [
        "---",
        f"title: {title}",
        f"summary: {summary}",
        f"excerpt: {summary}",
        "deprecated: false",
        f"hidden: {'true' if hidden else 'false'}",
        "metadata:",
        "  robots: index",
    ]
    if slug:
        lines.append(f"slug: {slug}")
    lines.extend(["---", "", body.strip(), ""])
    return "\n".join(lines)


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE: {rel}")


def fix_main_overview() -> None:
    write(
        "docs/get-started/overview.md",
        page(
            "Overview",
            "Welcome to the Gupshup Partner Documentation Hub.",
            """# Gupshup Partner Documentation

This documentation is a central resource for current and prospective **Gupshup integration partners**. It provides the technical and operational guidance needed to build, launch, and scale WhatsApp Business API solutions on the Gupshup platform.

> **For Gupshup Partners**
>
> This documentation focuses on partner-specific concepts, workflows, and integration requirements for ISVs, Tech Providers, agencies, and enterprises.

---

## Get started

Kick off your partner journey with quick access to the most essential guides and tools.

| Resource | Description |
|----------|-------------|
| [Quickstarts](/docs/quickstarts) | 5-step path from signup to your first message |
| [Partner API](/reference/partner-api-overview) | Complete API reference grouped by business capability |
| [Partner Portal](https://partner.gupshup.io) | Manage apps, billing, and customers |
| [Support](/docs/support) | Contact and help resources |

---

## Who is Gupshup for?

| Partner Type | How They Benefit |
|--------------|------------------|
| **SaaS Platforms** | Add WhatsApp messaging into your product and automate client workflows |
| **Enterprises** | Deploy large-scale messaging for sales, marketing, and support |
| **Agencies & Developers** | Build WhatsApp-powered solutions and tools for clients |
| **ISVs & Tech Providers** | Become a Meta Tech Provider with Gupshup's partner APIs and portal |

---

## Partner journey

### 1. Set up your partner account

Create a partner account at [partner.gupshup.io](https://partner.gupshup.io), get approved, and access the Partner Portal.

→ [Get Started as a Partner](/docs/get-started-as-partner)

### 2. Integrate with Partner APIs

Generate API credentials and understand authentication.

→ [Generate Secret and Token](/docs/generate-secret-and-token) · [Authentication](/docs/authentication)

### 3. Onboard clients and manage WABAs

Create apps, configure webhooks, and onboard WhatsApp Business numbers.

→ [Create your first App](/docs/create-your-first-app) · [Onboarding](/docs/onboarding-overview)

### 4. Send messages and scale

Send template and session messages, then optimize with analytics and billing tools.

→ [Send your first message](/docs/send-your-first-message) · [Messaging](/docs/messaging-overview)

---

## Documentation sections

| Section | What it covers |
|---------|----------------|
| [Get Started](/docs/overview) | Overview, pricing, quickstarts, Tech Provider program |
| [Onboarding](/docs/onboarding-overview) | Webhooks, events, coexistence, onboarding APIs |
| [Partner API](/docs/partner-api-overview) | REST APIs by category |
| [Partner Hub](/docs/partner-hub-overview) | Portal UI, wallet, billing, support |
| [Messaging](/docs/messaging-overview) | Templates, session messages, media, voice |
| [Commerce & Payments](/docs/commerce-overview) | Brazil payments, INR wallet, wire transfers |

---

## Next steps

| | |
|---|---|
| [Explore Quickstarts](/docs/quickstarts) | Five steps to your first message |
| [See Pricing](/docs/pricing) | Billing models, wallet, and commissions |
| [Learn About Tech Providers](/docs/what-is-sp-tp) | Solution Partners & Tech Providers |
""",
            slug="overview",
        ),
    )


def fix_section_overviews() -> None:
    write(
        "docs/onboarding/overview.md",
        page(
            "Onboarding Overview",
            "Integrate with Gupshup: apps, webhooks, events, and coexistence.",
            """# Onboarding

Guides for integrating with the Gupshup Partner Platform — app creation, webhooks, events, and advanced setup.

## Core topics

| Topic | Guide |
|-------|-------|
| Onboarding APIs | [Onboarding APIs](/docs/onboarding-apis) |
| Webhooks & callbacks | [Understanding Webhooks](/docs/understanding-webhooks-and-callback) |
| Inbound events (V2) | [Inbound Events V2](/docs/inbound-events-v2) |
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
        "docs/partner-hub/overview.md",
        page(
            "Partner Hub Overview",
            "Partner Portal UI for managing apps, customers, and billing.",
            """# Partner Hub

The Gupshup Partner Portal is your control center for WhatsApp partner operations.

## Portal guides

| Topic | Guide |
|-------|-------|
| Getting started | [Get started with Partner Portal](/docs/get-started-with-partner-portal) |
| Walkthrough | [Partner Portal Walkthrough](/docs/partner-portal-walkthrough) |
| Wallet & billing | [Wallet](/docs/wallet-1) · [Commissions](/docs/commissions) |
| Support | [Support](/docs/support) |
| Customer portal | [Partner Customer Portal](/docs/partner-customer-portal) |
| Wire transfers | [Partner Wire Transfers](/docs/wire-transfer-automation) |
""",
            slug="partner-hub-overview",
        ),
    )

    write(
        "docs/messaging/overview.md",
        page(
            "Messaging Overview",
            "Send and receive WhatsApp messages, templates, media, and voice.",
            """# Messaging

Guides for sending and receiving WhatsApp messages on the Gupshup Partner Platform.

## Message guides

| Topic | Guide |
|-------|-------|
| Core concepts | [WhatsApp Messages](/docs/whatsapp-messages) |
| Outbound messages | [Outbound messages](/docs/outbound-messages) |
| Inbound messages | [Inbound Messages](/docs/inbound-messages) |
| Media | [Media Management](/docs/media-management) |
| MM Lite | [Marketing Messages Lite](/docs/marketing-messages-lite-mm-lite-api) |
| Voice (Outbound) | [Voice Outbound & SIP](/docs/guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup) |
| Voice permissions | [Obtain User Call Permissions](/docs/obtain-user-call-permissions) |

## Related API categories

- [Templates Management](/reference/templates-management)
- [Messaging (V3)](/reference/messaging-v3)
- [Media Management](/reference/media-management)
- [WhatsApp Flows](/reference/whatsapp-flows)
""",
            slug="messaging-overview",
        ),
    )

    write(
        "docs/commerce-and-payments/overview.md",
        page(
            "Commerce & Payments Overview",
            "Payments, wallet, and billing for partner commerce.",
            """# Commerce & Payments

Guides for payments, wallet setup, and billing on the Gupshup Partner Platform.

| Topic | Guide |
|-------|-------|
| Brazil Payments | [WhatsApp Brazil Payments](/docs/whatsapp-brazil-payments) |
| INR Wallet & KYC | [INR Wallet Creation & KYC Flow](/docs/wallet-creation-kyc-flow-guide) |
| USD Wire Transfers | [Partner USD Wire Transfers](/docs/partner-usd-wire-transfers) |

## Related Partner Hub guides

- [Wallet](/docs/wallet-1)
- [Recharge via Stripe or Ebanx](/docs/recharge-via-stipe-or-ebanx)
""",
            slug="commerce-overview",
        ),
    )

    write(
        "docs/security/overview.md",
        page(
            "Security Overview",
            "Partner Portal security, authentication, and best practices.",
            """# Security

Security guides for the Gupshup Partner Platform.

| Topic | Guide |
|-------|-------|
| Portal security | [Security in Partner Portal](/docs/security-in-partner-portal) |
| Google Authenticator | [Google Authenticator for Partner Portal](/docs/google-authenticator-for-partner-portal) |
| Authy | [Authy Authenticator for Partner Portal](/docs/authy-authenticator-app-for-partner-portal) |
| Security wizard | [Partner Portal Security Wizard](/docs/comprehensive-step-by-step-guide-for-the-partner-portal-security-wizard) |
| JWT tokens | [Signing the JWT Token](/docs/signing-the-jwt-token-test-jwt-step) |
| API key rotation | [Account API Key Rotation](/docs/account-api-key-rotation-security-wizard) |
""",
            slug="security-overview",
        ),
    )

    write(
        "docs/meta-whatsapp-features/overview.md",
        page(
            "Meta WhatsApp Features Overview",
            "Meta WhatsApp platform features for partners.",
            """# Meta WhatsApp Features

Guides for Meta WhatsApp platform features available to Gupshup partners.

| Topic | Guide |
|-------|-------|
| BSUID | [BSUID](/docs/bsuid) |
| Enable BSUID flag | [API to enable BSUID flag](/docs/api-to-enable-bsuid-flag-for-an-app) |
""",
            slug="meta-whatsapp-features-overview",
        ),
    )


def fix_quickstarts() -> None:
    write(
        "docs/get-started/quickstarts/index.md",
        page(
            "Quickstarts",
            "Five steps from partner signup to your first WhatsApp message.",
            """# Quickstarts

Follow these steps in order to go from partner signup to sending your first WhatsApp message.

| Step | Guide | Outcome |
|------|-------|---------|
| 1 | [Get Started as a Partner](/docs/get-started-as-partner) | Partner account and portal access |
| 2 | [Register as Tech Provider](/docs/register-as-tech-provider) | Meta Tech Provider / Solution ID (if applicable) |
| 3 | [Create your first App](/docs/create-your-first-app) | WABA onboarded via Partner Portal |
| 4 | [Generate Secret and Token](/docs/generate-secret-and-token) | API credentials |
| 5 | [Send your first message](/docs/send-your-first-message) | First WhatsApp message sent |

Each page includes prerequisites, numbered steps, and a link to the next step.
""",
            slug="quickstarts",
        ),
    )

    write(
        "docs/get-started/quickstarts/get-started-as-partner.md",
        page(
            "Get Started as a Partner",
            "Sign up for the Gupshup Partner program and access the Partner Portal.",
            """# Get Started as a Partner

## Prerequisites

- A registered business eligible for WhatsApp Business API partnership
- Business contact details for partner review

## Steps

### 1. Sign up as a Partner

Sign up at the [Gupshup Partner Portal](https://partner.gupshup.io) by providing basic business information. The Gupshup team reviews each request and activates approved partners.

### 2. Understand partner types

Partners are **Independent Service Providers (ISVs)** or **Tech Providers (TPs)**. Both use Partner APIs and the Partner Portal to serve customers.

> Tech Providers are a Meta construct (introduced Jan 2024). See [Solution Partners & Tech Providers](/docs/what-is-sp-tp).

### 3. Explore the Partner Portal

Once activated, you can:

- Manage WABA applications for your customers
- View message delivery analytics
- Access wallet, billing, and commission details

## What you get

- **Partner APIs** — Build branded UIs for your customers
- **Partner Portal** — Self-serve WABA management
- **Partner Customer Portal** — Optional white-labeled UI for end customers
- **Analytics** — Usage and conversation data across onboarded customers

## Next step

→ [Register as a Tech Provider](/docs/register-as-tech-provider) (if building a Meta app solution) or skip to [Create your first App](/docs/create-your-first-app)
""",
            slug="get-started-as-partner",
        ),
    )

    write(
        "docs/get-started/quickstarts/register-as-tech-provider.md",
        page(
            "Register as Tech Provider",
            "Get your Meta Solution ID and register as a Tech Provider.",
            """# Register as Tech Provider

## Prerequisites

- Approved Gupshup Partner account
- Meta Developer account and WhatsApp Business app

## Steps

### 1. Read the Tech Provider program

Review [Solution Partners & Tech Providers](/docs/what-is-sp-tp) for ISV vs TP roles and Meta requirements.

### 2. Get your Solution ID from Meta

Follow [Get Solution ID from Meta](/docs/get-solution-id-from-meta) to obtain the Solution ID required for embedded onboarding flows.

### 3. Configure your Meta app

Link your Meta app to Gupshup using the Solution ID when creating apps via API or embedded signup.

## Related APIs

- [Generate Embed Signed Link](/reference/get_partner-app-appid-onboarding-embed-link)
- [Create App](/reference/post_partner-app)

## Next step

→ [Create your first App](/docs/create-your-first-app)
""",
            slug="register-as-tech-provider",
        ),
    )

    write(
        "docs/get-started/quickstarts/send-your-first-message.md",
        page(
            "Send your first message",
            "Send your first WhatsApp message using the Partner API.",
            """# Send your first message

## Prerequisites

- Partner token from [Generate Secret and Token](/docs/generate-secret-and-token)
- Live app with approved template (for business-initiated messages outside 24-hour window)

## Steps

### 1. Choose message type

| Type | When to use | Guide |
|------|-------------|-------|
| Template message | Outside 24-hour window | [Templates Management](/reference/templates-management) |
| Session message | Within 24-hour window | [Messaging (V3)](/reference/messaging-v3) |

### 2. Send a template message

Use [Send msg With Template ID](/reference/post_partner-app-appid-template-msg) or see [Send Template Message Examples](/reference/send-message-examples).

### 3. Send a session message

Use [Text Message (V3)](/reference/post_partner-app-appid-v3-text-message).

### 4. Verify delivery

Configure [webhooks](/docs/understanding-webhooks-and-callback) to receive message and delivery status notifications.

## Learn more

- [WhatsApp Messages](/docs/whatsapp-messages) — Full messaging concepts and message types
- [Message events](/docs/message-events) — Delivery status webhook events

## You are integrated!

Continue with [Onboarding](/docs/onboarding-overview) and the full [API Reference](/reference/partner-api-overview).
""",
            slug="send-your-first-message",
        ),
    )

    # Add next-step footer to create-your-first-app and generate-secret-and-token if missing
    for fname, next_link, next_label in [
        ("create-your-first-app.md", "/docs/generate-secret-and-token", "Generate Secret and Token"),
        ("generate-secret-and-token.md", "/docs/send-your-first-message", "Send your first message"),
    ]:
        path = DOCS / "get-started" / "quickstarts" / fname
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if "Next step" not in text:
                text = text.rstrip() + f"\n\n## Next step\n\n→ [{next_label}]({next_link})\n"
                path.write_text(text, encoding="utf-8")
            if "slug:" not in text.split("---", 2)[1]:
                slug = fname.replace(".md", "")
                text = path.read_text(encoding="utf-8")
                text = re.sub(r"^(title: .+)$", rf"\1\nslug: {slug}", text, count=1, flags=re.M)
                path.write_text(text, encoding="utf-8")


def fix_pricing_page() -> None:
    write(
        "docs/get-started/pricing.md",
        page(
            "Pricing",
            "Partner billing models, wallet, and commissions.",
            """# Pricing

Gupshup partners primarily use **prepaid wallet billing**. Partners recharge their wallet; customer usage is deducted from the wallet. Commissions apply for prepaid partners.

For detailed rate information, see the [Gupshup WhatsApp pricing page](https://www.gupshup.io/channels/self-serve/whatsapp/pricing).

## Related guides

| Topic | Guide |
|-------|-------|
| Wallet | [Wallet](/docs/wallet-1) |
| Commissions | [Commissions](/docs/commissions) |
| Overdraft | [Overdraft Limit](/docs/overdraft-limit) |
| Commission policy | [Unused Commission Policy](/docs/unused-commission-policy) |
| Rate limits | [Partner Rate Limits](/docs/partner-rate-limits) |
| Tier pricing | [Tier Based Pricing](/docs/tier-based-pricing) |

## Billing events

Webhook reference: [Billing events](/docs/billing-events)
""",
            slug="pricing",
        ),
    )


def fix_partner_api_docs() -> None:
    write(
        "docs/partner-api/overview.md",
        page(
            "Partner API Overview",
            "REST APIs for partner integrations with Gupshup.",
            """# Partner API

Gupshup exposes Partner APIs for building branded customer experiences on WhatsApp. Endpoints are organized by **business capability** — the same model used by leading partner documentation platforms.

## API Reference by category

→ [Browse all API categories](api-reference/overview)

| Category | Description |
|----------|-------------|
| [Partner Management](api-reference/partner-management) | Login, apps, linking |
| [Channel Management](api-reference/channel-management) | Create and manage WABA apps |
| [WABA Account Management](api-reference/waba-account-management) | Health, phone, quality |
| [Webhook Management](api-reference/webhook-management) | Subscriptions and callbacks |
| [Balance & Usage](api-reference/balance-and-usage) | Wallet and billing |
| [Templates Management](api-reference/templates-management) | Message templates |
| [Messaging (V3)](api-reference/messaging-v3) | Session messages |
| [Media Management](api-reference/media-management) | Media upload/download |
| [WhatsApp Flows](api-reference/whatsapp-flows) | Flow lifecycle |
| [Business Profile](api-reference/business-profile) | Profile and display name |
| [User Management](api-reference/user-management) | Block/unblock users |
| [Marketing Messages Lite](api-reference/marketing-messages-lite) | MM Lite |

## Authentication

→ [Authentication](/docs/authentication)

All requests require a partner token. See [Generate Secret and Token](/docs/generate-secret-and-token).

## Interactive API reference

For full request/response schemas and Try It, see the [Reference section](/reference/partner-api-overview).
""",
            slug="partner-api-overview",
        ),
    )

    write(
        "docs/partner-api/authentication.md",
        page(
            "Authentication",
            "How to authenticate Partner API requests.",
            """# Authentication

## Partner token

1. Generate a client secret in Partner Portal → **Settings** → **API client details**
2. Call [Get Partner Token](/reference/post_partner-account-login) with the secret in the `password` parameter
3. Use the returned token in subsequent API requests

See [Generate Secret and Token](/docs/generate-secret-and-token) for step-by-step instructions.

## App access token

For app-level APIs, use [Get Access Token for an App](/reference/get_partner-app-appid-token).

## Security best practices

- Rotate client secrets regularly (recommended: max 3 months)
- See [Security](/docs/security-overview) for MFA and IP allowlisting guides
""",
            slug="authentication",
        ),
    )


def fix_reference_overview() -> None:
    write(
        "reference/Partner APIs/partner-api-overview.md",
        page(
            "Partner API Overview",
            "Gupshup Partner API reference organized by business category.",
            """# Partner API

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

All Partner API requests require a partner token.

1. [Generate Secret and Token](/docs/generate-secret-and-token) in the guides
2. [Get Partner Token](/reference/post_partner-account-login) API endpoint

## Guides

- [Partner API overview (guides)](/docs/partner-api-overview)
- [Onboarding APIs](/docs/onboarding-apis)
""",
            slug="partner-api-overview",
        ),
    )


def fix_api_category_hubs() -> None:
    """Rebuild reference category hubs and docs/partner-api/api-reference with real endpoint links."""
    ref_slugs = {p.stem for p in (ROOT / "reference").rglob("*.md")}

    categories = {
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
                ("Reaction Message", "post_partner-app-appid-v3-reaction-message"),
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

    for slug, meta in categories.items():
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
                lines.append(f"| {name} | *endpoint available in Partner APIs* |")
        lines.append("")

        hub_body = "\n".join(lines)

        # docs/partner-api/api-reference/{slug}.md
        write(
            f"docs/partner-api/api-reference/{slug}.md",
            page(meta["title"], meta["summary"], hub_body, slug=slug),
        )

        # reference/Partner APIs/{slug}/index.md
        ref_dir = ROOT / "reference" / "Partner APIs" / slug
        ref_dir.mkdir(parents=True, exist_ok=True)
        write(
            f"reference/Partner APIs/{slug}/index.md",
            page(meta["title"], meta["summary"], hub_body, slug=slug),
        )

    write(
        "docs/partner-api/api-reference/overview.md",
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

For interactive Try It and full OpenAPI schemas, see [/reference/partner-api-overview](/reference/partner-api-overview).
""",
            slug="api-reference-overview",
        ),
    )


def update_orders() -> None:
    orders = {
        "docs/security/_order.yaml": [
            "overview", "security-in-partner-portal",
            "google-authenticator-for-partner-portal",
            "authy-authenticator-app-for-partner-portal",
            "user-experience-after-auth0-mfa",
            "comprehensive-step-by-step-guide-for-the-partner-portal-security-wizard",
            "partner-authentication-guide-universal-tokens-ut-overview",
            "signing-the-jwt-token-test-jwt-step",
            "account-api-key-rotation-security-wizard",
        ],
        "docs/meta-whatsapp-features/_order.yaml": [
            "overview", "bsuid", "api-to-enable-bsuid-flag-for-an-app",
        ],
    }
    for rel, slugs in orders.items():
        path = ROOT / rel
        if path.parent.exists():
            existing = {p.stem for p in path.parent.glob("*.md")}
            ordered = [s for s in slugs if s in existing]
            ordered += sorted(existing - set(ordered))
            path.write_text("\n".join(f"- {s}" for s in ordered) + "\n", encoding="utf-8")


def main() -> None:
    print("=== Fix main overview (360 style) ===")
    fix_main_overview()
    print("\n=== Fix section overviews (unique slugs) ===")
    fix_section_overviews()
    print("\n=== Fix quickstarts ===")
    fix_quickstarts()
    print("\n=== Fix pricing page ===")
    fix_pricing_page()
    print("\n=== Fix partner-api docs ===")
    fix_partner_api_docs()
    print("\n=== Fix reference overview ===")
    fix_reference_overview()
    print("\n=== Fix API category hubs ===")
    fix_api_category_hubs()
    print("\n=== Update orders ===")
    update_orders()
    print("\nDone.")


if __name__ == "__main__":
    main()
