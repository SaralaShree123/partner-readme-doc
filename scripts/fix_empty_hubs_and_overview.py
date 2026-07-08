#!/usr/bin/env python3
"""
Careful content fix:
1. Rewrite Overview to match 360dialog master (no Billing/Prepaid body)
2. Hide introduction (contains billing that was colliding with landing UX)
3. Fill all empty hub pages with real hub content + links
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


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


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {rel}")


def fix_overview() -> None:
    # Match https://docs.360dialog.com/partner/get-started/master.md structure
    # NO Prepaid / Billing sections — pricing is a next-step link only
    write(
        "docs/get-started/overview.md",
        page(
            "Overview",
            "Welcome to the Gupshup Partner Documentation Hub",
            """# Overview

This documentation is a central resource for current and prospective **Gupshup integration partners**. It provides the technical and operational guidance needed to build, launch, and scale WhatsApp Business API solutions using the Gupshup platform.

> 📘 **For Gupshup Partners**
>
> This documentation is intended for Gupshup Partners and focuses on partner-specific concepts, workflows, and integration requirements.
>
> Sign up at [partner.gupshup.io](https://partner.gupshup.io).

---

## Get started

Kick off your Partner journey with quick access to the most essential guides and tools.

| | |
|---|---|
| **[Quickstarts](/docs/quickstarts)** | Five steps from signup to your first WhatsApp message |
| **[Partner API Reference](/reference/partner-api-overview)** | Explore the complete API reference for building and managing integrations |
| **[Partner Portal](https://partner.gupshup.io)** | Manage apps, customers, and integrations |
| **[Support](/docs/support)** | Expert support with escalation paths |

---

## Who is Gupshup for?

From SaaS platforms to software vendors, Gupshup serves a diverse range of Partner use cases.

| Partner Type | How They Benefit from Gupshup |
|--------------|-------------------------------|
| SaaS Platforms | Add WhatsApp messaging into your product and automate client workflows |
| Enterprises | Deploy large-scale messaging for sales, marketing, and support use cases |
| Agencies & Developers | Build WhatsApp-powered solutions and tools |
| ISVs | Become a Meta Tech Provider with Gupshup’s expert guidance |

---

## How it works

Gupshup provides a developer-first, API-driven approach to WhatsApp Business messaging.
Easily integrate, onboard clients, and manage messaging workflows within a scalable, partner-friendly ecosystem.

### Partner journey

1. **Set up your Partner account** — Create a partner account, set API credentials, and start testing. → [Get Started as a Partner](/docs/get-started-as-partner)
2. **Integrate WhatsApp API** — Connect Partner APIs and integrate them into your solution. → [Generate Secret and Token](/docs/generate-secret-and-token)
3. **Onboard clients & manage WABAs** — Add numbers, onboard clients, and start messaging. → [Create your first App](/docs/create-your-first-app)
4. **Scale & optimise messaging** — Optimise performance and grow. → [Send your first message](/docs/send-your-first-message)

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


def hide_billing_intro() -> None:
    """Introduction has Billing/Prepaid — hide so it cannot collide with landing UX."""
    path = DOCS / "get-started" / "introduction.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("hidden: false", "hidden: true", 1)
    if "slug:" not in text.split("---", 2)[1]:
        text = text.replace("title: Introduction\n", "title: Introduction\nslug: introduction\n", 1)
    path.write_text(text, encoding="utf-8")
    print("HIDDEN docs/get-started/introduction.md")


def fill_empty_hubs() -> None:
    hubs = {
        "docs/partner-hub/get-started-with-partner-portal.md": page(
            "Get started with Partner Portal",
            "Introduction to the Gupshup Partner Portal for managing customers and WABAs.",
            """# Get started with Partner Portal

Partner Portal enables you to apply for partnership with Gupshup and manage WhatsApp for your customers. Once you become an authorized partner, you can monitor messages sent, delivered, read, and failed for customer apps within a time period.

Partners are either **Independent Service Providers (ISVs)** or **Tech Providers (TPs)**. Gupshup provides Partner APIs and the Partner Portal UI so you can manage customer WABAs and build value on top of the platform.

> 📘 Tech Providers are a Meta construct (introduced 31 Jan 2024). Learn more about [Tech Providers](https://support.gupshup.io/hc/en-us/articles/35249666388889).

> 📘 Partner Portal currently supports WhatsApp as a channel.

## What you can do

| Topic | Guide |
|-------|-------|
| Portal walkthrough | [Partner Portal Walkthrough](/docs/partner-portal-walkthrough) |
| Create your first app | [Create your first App](/docs/create-your-first-app) |
| Generate API credentials | [Generate Secret and Token](/docs/generate-secret-and-token) |
| Wallet & commissions | [Wallet](/docs/wallet-1) · [Commissions](/docs/commissions) |
| Support | [Support](/docs/support) |
| Customer portal | [Partner Customer Portal](/docs/partner-customer-portal) |

## Sign up

Sign up at [partner.gupshup.io](https://partner.gupshup.io). Gupshup reviews each partner request. Once approved, Partner Portal is activated for your account.

## Next step

→ [Partner Portal Walkthrough](/docs/partner-portal-walkthrough)
""",
            slug="get-started-with-partner-portal",
        ),
        "docs/partner-hub/partner-portal-walkthrough.md": page(
            "Partner Portal Walkthrough",
            "Step-by-step walkthrough of core Partner Portal tasks.",
            """# Partner Portal Walkthrough

Use these guided steps to complete core Partner Portal setup.

## Walkthrough steps

| Step | Guide | What you’ll do |
|------|-------|----------------|
| 1 | [Create your first App](/docs/create-your-first-app) | Create a WABA application and go live |
| 2 | [Generate Secret and Token](/docs/generate-secret-and-token) | Create an API client secret and partner token |
| 3 | [Partner Rate Limits](/docs/partner-rate-limits) | Understand rate limits for Partner APIs |

## Related hub topics

| Topic | Guide |
|-------|-------|
| Wallet | [Wallet](/docs/wallet-1) |
| Security | [Security in Partner Portal](/docs/security-in-partner-portal) |
| Support | [Support](/docs/support) |

## Next step

→ [Create your first App](/docs/create-your-first-app)
""",
            slug="partner-portal-walkthrough",
        ),
        "docs/partner-hub/wallet-1.md": page(
            "Wallet",
            "Prepaid wallet billing for Gupshup partners.",
            """# Wallet

The prepaid method of billing is called **Wallet** in Gupshup. You recharge your Gupshup wallet; usage for your apps is deducted from the wallet. The wallet works in **USD**.

## Guides in this section

| Topic | Guide |
|-------|-------|
| Wallet overview & how to recharge | [Wallet Overview](/docs/commissions) |
| Overdraft | [Overdraft Limit](/docs/overdraft-limit) |
| Balance transfer | [Partner Wallet Balance Transfer](/docs/partner-wallet-balance-transfer) |
| Wire transfers | [Partner Wire Transfers](/docs/wire-transfer-automation) |
| Unused commissions | [Unused Commission Policy](/docs/unused-commission-policy) |

## How to use a wallet (summary)

1. Log in to Partner Portal and open **Wallet**
2. Add credits (funds) — 1 credit = 1 USD
3. Save billing details for invoices
4. Pay via **Stripe** or **Ebanx**
5. Monitor balance — you are notified when balance reaches $5

For full steps, see [Wallet Overview](/docs/commissions).
""",
            slug="wallet-1",
        ),
        "docs/partner-hub/recharge-via-stipe-or-ebanx.md": page(
            "Recharge via Stripe or Ebanx",
            "How partners recharge the Gupshup wallet.",
            """# Recharge via Stripe or Ebanx

Partners recharge the prepaid wallet from Partner Portal using supported payment providers.

| Provider | Notes |
|----------|-------|
| **Stripe** | Card payments for eligible regions |
| **Ebanx** | Supported for applicable markets |

## Steps

1. Open Partner Portal → **Wallet**
2. Click **Recharge** / **Add credits**
3. Enter amount (minimum $10, maximum $10,000 per transaction)
4. Confirm billing details
5. Choose **Stripe** or **Ebanx** and complete payment

Related: [Wallet](/docs/wallet-1) · [Wallet Overview](/docs/commissions)
""",
            slug="recharge-via-stipe-or-ebanx",
            hidden=False,
        ),
        "docs/partner-hub/meta-whatsapp-features.md": page(
            "Meta WhatsApp Features",
            "Meta WhatsApp features available to Gupshup partners.",
            """# Meta WhatsApp Features

Feature guides for Meta WhatsApp capabilities available on the Gupshup Partner Platform.

| Topic | Guide |
|-------|-------|
| BSUID | [BSUID](/docs/bsuid) |
| Enable BSUID for an app | [API to enable BSUID flag](/docs/api-to-enable-bsuid-flag-for-an-app) |
| Coexistence | [Coexistence](/docs/co-existence-closed-beta-phase) |

See also: [Meta WhatsApp Features section](/docs/meta-whatsapp-features-overview)
""",
            slug="meta-whatsapp-features",
        ),
        "docs/onboarding/understanding-webhooks-and-callback.md": page(
            "Understanding Webhooks and Callback",
            "How webhooks and callback URLs work for Partner apps.",
            """# Understanding Webhooks and Callback

A webhook is an HTTP/HTTPS callback triggered by events on the platform. Partners use webhooks to receive inbound WhatsApp messages and status notifications.

## Guides in this section

| Topic | Guide |
|-------|-------|
| Key requirements | [Webhook Key Points](/docs/webhook-key-points) |
| Set callback URL | [Set Callback URL](/docs/set-callback-url-1) |
| Inbound events overview | [Inbound Events](/docs/inbound-events) |
| Events (V2) | [Inbound events (V2)](/docs/inbound-events-v2) |
| Events (V3) | [Incoming Events (V3)](/docs/v3-events) |

## Related APIs

- [Webhook Management](/reference/webhook-management)
""",
            slug="understanding-webhooks-and-callback",
        ),
        "docs/onboarding/inbound-events-v2.md": page(
            "Inbound events (V2)",
            "V2 inbound webhook event reference for Partner apps.",
            """# Inbound events (V2)

Reference for V2 inbound webhook events sent to your callback URL.

## Event guides

| Event type | Guide |
|------------|-------|
| Account events | [Account events](/docs/account-events) |
| Billing events | [Billing events](/docs/billing-events) |
| Message events | [Message events](/docs/message-events) |
| System events | [System events](/docs/system-events) |
| User events | [User events](/docs/user-events) |
| PMP events | [PMP Events](/docs/pmp-events-1) |

## Setup

Start with [Understanding Webhooks and Callback](/docs/understanding-webhooks-and-callback) and [Webhook Key Points](/docs/webhook-key-points).
""",
            slug="inbound-events-v2",
        ),
        "docs/onboarding/v3-events.md": page(
            "Incoming Events (V3)",
            "V3 incoming webhook events for Partner apps.",
            """# Incoming Events (V3)

Reference for V3 incoming events.

## Event guides

| Topic | Guide |
|-------|-------|
| Events overview | [Events](/docs/events) |
| Template events | [Template events](/docs/template-events) |
| MM Lite click events | [MM Lite click events for V3](/docs/mm-lite-click-events-for-v3) |
| Coex events | [Coex](/docs/coex) |
| Partner PMP | [Partner PMP](/docs/partner-pmp) |
| Wallet PMP | [Wallet PMP](/docs/wallet-pmp) |
| Tier based pricing | [Tier based pricing](/docs/tier-based-pricing-1) |

## Related

- [Inbound events (V2)](/docs/inbound-events-v2)
- [Understanding Webhooks](/docs/understanding-webhooks-and-callback)
""",
            slug="v3-events",
        ),
        "docs/onboarding/partner-hosted-embedded-sign-up-flow.md": page(
            "Partner hosted embedded sign up flow",
            "Host Meta Embedded Signup in your own UI.",
            """# Partner hosted embedded sign up flow

Host the Meta Embedded Signup experience in your own product so customers can onboard WhatsApp numbers without leaving your UI.

## Guides

| Topic | Guide |
|-------|-------|
| Tech Partner hosted flow | [Tech Partner Hosted Embed Sign Up](/docs/tech-partner-hosted-embed-sign-up-flow) |
| Error codes | [Error codes](/docs/error-codes) |
| TPP onboarding | [TPP Partner Hosted Onboarding](/docs/tpp-partner-hosted-onboarding) |

## Related APIs

- [Channel Management](/reference/channel-management)
- [Generate Embed Signed Link](/reference/get_partner-app-appid-onboarding-embed-link)
""",
            slug="partner-hosted-embedded-sign-up-flow",
        ),
        "docs/onboarding/meta-passthrough-apis.md": page(
            "Meta passthrough APIs",
            "Passthrough and Flow management APIs for Partners.",
            """# Meta passthrough APIs

Guides for Meta passthrough messaging and related Partner capabilities.

## Guides

| Topic | Guide |
|-------|-------|
| Flow management | [Passthrough APIs — Flow Management](/docs/passthrough_apis_flow_management) |
| V3 incoming events | [Passthrough V3 Incoming Events](/docs/passthrough-v3-incoming-events) |
| Dynamic flows | [WhatsApp Dynamic Flows](/docs/whatsapp-dynamic-flows) |
| WhatsApp Pay events | [WhatsApp Pay Events](/docs/whatsapp-pay-events) |
| For partners | [For Partners](/docs/for-partners) |

## API Reference

- [Messaging (V3)](/reference/messaging-v3)
- [WhatsApp Flows](/reference/whatsapp-flows)
""",
            slug="meta-passthrough-apis",
        ),
        "docs/messaging/inbound-messages.md": page(
            "Inbound Messages",
            "Types of inbound WhatsApp messages partners can receive.",
            """# Inbound Messages

Overview of inbound message types delivered to your webhook.

## Message types

| Type | Guide |
|------|-------|
| All types | [Types Of Inbound Messages](/docs/types-of-inbound-messages) |
| Text | [Text](/docs/text) |
| Media | [Media](/docs/media) |
| Interactive | [Interactive](/docs/interactive) |
| Product messages | [Single/Multi Product Messages](/docs/singlemulti-product-message) |
| Request welcome | [Request Welcome](/docs/request-welcome) |
| Other | [Other](/docs/other) |

## Related

- [Understanding Webhooks](/docs/understanding-webhooks-and-callback)
- [Message events](/docs/message-events)
""",
            slug="inbound-messages",
        ),
        "docs/messaging/types-of-inbound-messages.md": page(
            "Types Of Inbound Messages",
            "Catalog of inbound WhatsApp message types.",
            """# Types Of Inbound Messages

| Type | Guide |
|------|-------|
| Text | [Text](/docs/text) |
| Media | [Media](/docs/media) |
| Interactive | [Interactive](/docs/interactive) |
| Single / Multi Product | [Single/Multi Product Messages](/docs/singlemulti-product-message) |
| Request Welcome | [Request Welcome](/docs/request-welcome) |
| Other | [Other](/docs/other) |
""",
            slug="types-of-inbound-messages",
        ),
        "docs/get-started/get-started-with-meta-partner-eco-system.md": page(
            "Meta Partner Eco-System",
            "Overview of Meta partner programs relevant to Gupshup partners.",
            """# Meta Partner Eco-System

Guides related to Meta’s partner programs for Gupshup partners.

| Topic | Guide |
|-------|-------|
| Solution Partners & Tech Providers | [What is SP / TP](/docs/what-is-sp-tp) |
| Get Solution ID from Meta | [Get Solution ID from Meta](/docs/get-solution-id-from-meta) |
| Pricing | [Pricing](/docs/pricing) |
""",
            slug="get-started-with-meta-partner-eco-system",
        ),
        "docs/get-started/gupshup-partner-offering.md": page(
            "Gupshup Partner Offering",
            "Products and offerings available to Gupshup partners.",
            """# Gupshup Partner Offering

| Offering | Guide |
|----------|-------|
| Amplead (C2WA) | [Partner C2WA offering — Amplead](/docs/amplead) |
| Amplead docs | [Amplead Get Started](/docs/amplead-get-started-guide) |
""",
            slug="gupshup-partner-offering",
        ),
    }

    for rel, content in hubs.items():
        write(rel, content)


def fix_orders() -> None:
    # Drop hidden introduction from preferred get-started order visibility
    gs = DOCS / "get-started" / "_order.yaml"
    gs.write_text(
        """- overview
- quickstarts
- gupshup-partner-eco-system
- what-is-sp-tp
- pricing
- tier-based-pricing
- gupshup-partner-offering
- get-started-with-meta-partner-eco-system
- get-solution-id-from-meta
- amplead
""",
        encoding="utf-8",
    )
    print("UPDATED docs/get-started/_order.yaml")


def improve_api_category_like_360() -> None:
    """Rewrite Partner Management hub like 360 — endpoints as sections with links to full Try-It pages."""
    api_pages = {
        "partner-management": (
            "Partner Management",
            "Endpoints for managing partner accounts, authentication, and app linking.",
            [
                ("Get Partner Token", "post_partner-account-login", "Authenticate and obtain a partner token using your client secret."),
                ("Get Partner Apps", "get_partner-account-api-partnerapps", "Retrieve the list of apps linked to the partner account."),
                ("Link App with Partner", "post_partner-account-api-applink", "Link an application with the partner account."),
            ],
        ),
        "channel-management": (
            "Channel Management",
            "Endpoints for creating and managing WABA channel applications.",
            [
                ("Create App", "post_partner-app", "Create a new partner application."),
                ("Update application", "put_partner-app-appid", "Update an existing application."),
                ("Generate Embed Signed Link", "get_partner-app-appid-onboarding-embed-link", "Generate an embed signed link for onboarding."),
                ("Filter app list", "get_partner-app-list", "Filter and list partner apps."),
            ],
        ),
        "templates-management": (
            "Templates Management",
            "Endpoints for creating, managing, and sending WhatsApp message templates.",
            [
                ("Get Templates", "get_partner-app-appid-templates", "List templates for an app."),
                ("Apply For Templates", "post_partner-app-appid-templates-6", "Submit a template for approval."),
                ("Delete Template", "delete_partner-app-appid-template-elementname", "Delete a template by element name."),
                ("Send msg With Template ID", "post_partner-app-appid-template-msg", "Send a template message."),
            ],
        ),
        "messaging-v3": (
            "Messaging (V3)",
            "Endpoints for sending session (passthrough) messages.",
            [
                ("Text Message", "post_partner-app-appid-v3-text-message", "Send a text session message."),
                ("Image Message", "post_partner-app-appid-v3-image-message", "Send an image session message."),
                ("Interactive Message", "post_partner-app-appid-v3-interactive-message", "Send an interactive session message."),
                ("Reaction Message", "post_partner-app-appid-v3-reaction-message", "Send a reaction message."),
            ],
        ),
        "webhook-management": (
            "Webhook Management",
            "Endpoints for webhook subscriptions and callbacks.",
            [
                ("Set subscription", "setsubscription-api-v3", "Create a webhook subscription."),
                ("Get All Subscriptions", "get_partner-app-appid-subscription", "List all subscriptions for an app."),
                ("Update App Subscription", "put_partner-app-appid-subscription-subscriptionid", "Update a subscription."),
            ],
        ),
    }

    ref_slugs = {p.stem for p in (ROOT / "reference").rglob("*.md")}

    for slug, (title, summary, endpoints) in api_pages.items():
        parts = [f"# {title}", "", summary, ""]
        for name, ref_slug, desc in endpoints:
            parts.append(f"## {name}")
            parts.append("")
            parts.append(f"> {desc}")
            parts.append("")
            if ref_slug in ref_slugs:
                parts.append(f"→ Full endpoint docs & Try It: [/reference/{ref_slug}](/reference/{ref_slug})")
            else:
                parts.append(f"→ See Partner APIs for `{ref_slug}`")
            parts.append("")

        body = "\n".join(parts)

        write(
            f"docs/partner-api/api-reference/{slug}.md",
            page(title, summary, body, slug=slug),
        )
        write(
            f"reference/Partner APIs/{slug}/index.md",
            page(title, summary, body, slug=slug),
        )


def main() -> None:
    fix_overview()
    hide_billing_intro()
    fill_empty_hubs()
    fix_orders()
    improve_api_category_like_360()
    print("\nDone. Please commit and push, then set ReadMe landing page to slug: overview")


if __name__ == "__main__":
    main()
