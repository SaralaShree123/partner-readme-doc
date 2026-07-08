#!/usr/bin/env python3
"""
Restructure Guides + API Reference into nested ReadMe folders (360-style expanders).

ReadMe rule (docs.readme.com/main/docs/documentation-structure):
- A folder with index.md + _order.yaml becomes an expandable sidebar page
- _order.yaml must NEVER list "index" (index.md is implied)
- Leaf pages are flat .md files; pages with children are folders
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REF = ROOT / "reference" / "Partner APIs"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT)}")


def write_order(folder: Path, slugs: list[str]) -> None:
    # Never include "index"
    slugs = [s for s in slugs if s != "index"]
    write(folder / "_order.yaml", "\n".join(f"- {s}" for s in slugs) + "\n")


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


def move_to_folder(src: Path, dest_dir: Path, new_name: str | None = None) -> Path | None:
    if not src.exists():
        return None
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (new_name or src.name)
    if dest.exists() and dest.resolve() != src.resolve():
        dest.unlink()
    shutil.move(str(src), str(dest))
    print(f"MOVE {src.relative_to(ROOT)} → {dest.relative_to(ROOT)}")
    return dest


def make_section(folder: Path, title: str, summary: str, body: str, children: list[str], slug: str | None = None) -> None:
    """Create/ensure folder with index.md + _order.yaml for expandable sidebar."""
    folder.mkdir(parents=True, exist_ok=True)
    write(
        folder / "index.md",
        page(title, summary, body, slug=slug or folder.name),
    )
    # Only list children that exist
    existing = {p.stem for p in folder.glob("*.md") if p.name != "index.md"}
    existing |= {p.name for p in folder.iterdir() if p.is_dir() and p.name != "__pycache__"}
    ordered = [c for c in children if c in existing]
    ordered += sorted(existing - set(ordered))
    write_order(folder, ordered)


# ---------------------------------------------------------------------------
# GET STARTED — fix quickstarts order (remove index)
# ---------------------------------------------------------------------------
def fix_get_started() -> None:
    qs = DOCS / "get-started" / "quickstarts"
    write_order(
        qs,
        [
            "get-started-as-partner",
            "register-as-tech-provider",
            "create-your-first-app",
            "generate-secret-and-token",
            "send-your-first-message",
            "partner-rate-limits",
        ],
    )
    # Ensure index.md has Quickstarts title
    write(
        qs / "index.md",
        page(
            "Quickstarts",
            "Five steps from partner signup to your first WhatsApp message.",
            """# Quickstarts

Follow these steps in order to go from partner signup to sending your first WhatsApp message.

| Step | Guide | Outcome |
|------|-------|---------|
| 1 | [Get Started as a Partner](/docs/get-started-as-partner) | Partner account and portal access |
| 2 | [Register as Tech Provider](/docs/register-as-tech-provider) | Meta Tech Provider setup |
| 3 | [Create your first App](/docs/create-your-first-app) | WABA onboarded via Partner Portal |
| 4 | [Generate Secret and Token](/docs/generate-secret-and-token) | API credentials |
| 5 | [Send your first message](/docs/send-your-first-message) | First WhatsApp message |

Use the sidebar chevron to open each step.
""",
            slug="quickstarts",
        ),
    )
    write_order(
        DOCS / "get-started",
        [
            "overview",
            "quickstarts",
            "gupshup-partner-eco-system",
            "what-is-sp-tp",
            "pricing",
            "tier-based-pricing",
            "get-solution-id-from-meta",
            "get-started-with-meta-partner-eco-system",
            "gupshup-partner-offering",
            "amplead",
        ],
    )


# ---------------------------------------------------------------------------
# ONBOARDING — nested sections
# ---------------------------------------------------------------------------
def nest_onboarding() -> None:
    base = DOCS / "onboarding"

    # --- webhooks-and-callback ---
    webhooks = base / "webhooks-and-callback"
    for name in [
        "webhook-key-points.md",
        "set-callback-url-1.md",
        "inbound-events.md",
    ]:
        move_to_folder(base / name, webhooks)
    # Convert understanding-webhooks hub into index
    src = base / "understanding-webhooks-and-callback.md"
    if src.exists():
        text = src.read_text(encoding="utf-8")
        # rewrite as index content
        write(
            webhooks / "index.md",
            page(
                "Webhooks & Callback",
                "How webhooks and callback URLs work for Partner apps.",
                """# Webhooks & Callback

A webhook is an HTTP/HTTPS callback triggered by events on the platform. Partners use webhooks to receive inbound WhatsApp messages and status notifications.

## In this section

| Topic | Guide |
|-------|-------|
| Key requirements | [Webhook Key Points](/docs/webhook-key-points) |
| Set callback URL | [Set Callback URL](/docs/set-callback-url-1) |
| Inbound events overview | [Inbound Events](/docs/inbound-events) |

## Related sections

- [Inbound events (V2)](/docs/inbound-events-v2)
- [Incoming Events (V3)](/docs/v3-events)
- [Webhook Management APIs](/docs/webhook-management)
""",
                slug="webhooks-and-callback",
            ),
        )
        src.unlink()
        print("REMOVED understanding-webhooks-and-callback.md (became webhooks-and-callback/index.md)")
    write_order(webhooks, ["webhook-key-points", "set-callback-url-1", "inbound-events"])

    # --- inbound-events-v2 ---
    v2 = base / "inbound-events-v2"
    v2_children = [
        "account-events.md",
        "billing-events.md",
        "message-events.md",
        "system-events.md",
        "user-events.md",
        "pmp-events-1.md",
    ]
    for name in v2_children:
        move_to_folder(base / name, v2)
    src = base / "inbound-events-v2.md"
    if src.exists():
        write(
            v2 / "index.md",
            page(
                "Inbound events (V2)",
                "V2 inbound webhook event reference for Partner apps.",
                """# Inbound events (V2)

Reference for V2 inbound webhook events sent to your callback URL.

## Event types

| Event type | Guide |
|------------|-------|
| Account events | [Account events](/docs/account-events) |
| Billing events | [Billing events](/docs/billing-events) |
| Message events | [Message events](/docs/message-events) |
| System events | [System events](/docs/system-events) |
| User events | [User events](/docs/user-events) |
| PMP events | [PMP Events](/docs/pmp-events-1) |

Start with [Webhooks & Callback](/docs/webhooks-and-callback) if you have not set up a callback URL yet.
""",
                slug="inbound-events-v2",
            ),
        )
        src.unlink()
    write_order(
        v2,
        ["account-events", "billing-events", "message-events", "system-events", "user-events", "pmp-events-1"],
    )

    # --- v3-events ---
    v3 = base / "v3-events"
    v3_children = [
        "events.md",
        "template-events.md",
        "mm-lite-click-events-for-v3.md",
        "coex.md",
        "partner-pmp.md",
        "wallet-pmp.md",
        "pmp-events.md",
        "tier-based-pricing-1.md",
        "inbound-message-events.md",
    ]
    for name in v3_children:
        move_to_folder(base / name, v3)
    src = base / "v3-events.md"
    if src.exists():
        write(
            v3 / "index.md",
            page(
                "Incoming Events (V3)",
                "V3 incoming webhook events for Partner apps.",
                """# Incoming Events (V3)

Reference for V3 incoming events.

## In this section

| Topic | Guide |
|-------|-------|
| Events overview | [Events](/docs/events) |
| Template events | [Template events](/docs/template-events) |
| Message events | [Inbound message events](/docs/inbound-message-events) |
| MM Lite click events | [MM Lite click events](/docs/mm-lite-click-events-for-v3) |
| Coex | [Coex](/docs/coex) |
| Partner PMP | [Partner PMP](/docs/partner-pmp) |
| Wallet PMP | [Wallet PMP](/docs/wallet-pmp) |
| PMP events | [PMP events](/docs/pmp-events) |
""",
                slug="v3-events",
            ),
        )
        src.unlink()
    write_order(
        v3,
        [
            "events",
            "template-events",
            "inbound-message-events",
            "mm-lite-click-events-for-v3",
            "coex",
            "partner-pmp",
            "wallet-pmp",
            "pmp-events",
            "tier-based-pricing-1",
        ],
    )

    # --- coexistence ---
    coex = base / "coexistence"
    for name in [
        "co-existence-closed-beta-phase.md",
        "coexistence-events.md",
        "coexistence-webhooks.md",
        "copy-of-co-existence-closed-beta-phase.md",
    ]:
        move_to_folder(base / name, coex)
    # Use co-existence page as index body (move rename)
    src = coex / "co-existence-closed-beta-phase.md"
    if src.exists() and not (coex / "index.md").exists():
        # Keep full content as child "overview" and create hub index
        write(
            coex / "index.md",
            page(
                "Coexistence",
                "WhatsApp Coexistence: Business App + Cloud API together.",
                """# Coexistence

Clients can onboard a number to WhatsApp Cloud API even if it is already connected to the WhatsApp Business App.

## In this section

| Topic | Guide |
|-------|-------|
| Coexistence guide | [Coexistence (Closed Beta)](/docs/co-existence-closed-beta-phase) |
| Coexistence events | [Coexistence Events](/docs/coexistence-events) |
| Coexistence webhooks | [Coexistence Webhooks](/docs/coexistence-webhooks) |
""",
                slug="coexistence",
            ),
        )
    write_order(
        coex,
        [
            "co-existence-closed-beta-phase",
            "coexistence-events",
            "coexistence-webhooks",
            "copy-of-co-existence-closed-beta-phase",
        ],
    )

    # --- embedded-signup ---
    emb = base / "embedded-signup"
    for name in [
        "partner-hosted-embedded-sign-up-flow.md",
        "tech-partner-hosted-embed-sign-up-flow.md",
        "error-codes.md",
        "tpp-partner-hosted-onboarding.md",
    ]:
        move_to_folder(base / name, emb)
    src = emb / "partner-hosted-embedded-sign-up-flow.md"
    if src.exists():
        write(
            emb / "index.md",
            page(
                "Embedded Signup",
                "Host Meta Embedded Signup in your own UI.",
                """# Embedded Signup

Host the Meta Embedded Signup experience in your product so customers can onboard WhatsApp numbers without leaving your UI.

## In this section

| Topic | Guide |
|-------|-------|
| Partner hosted flow | [Partner Hosted Embedded Sign Up](/docs/partner-hosted-embedded-sign-up-flow) |
| Tech Partner hosted flow | [Tech Partner Hosted Embed Sign Up](/docs/tech-partner-hosted-embed-sign-up-flow) |
| Error codes | [Error codes](/docs/error-codes) |
| TPP onboarding | [TPP Partner Hosted Onboarding](/docs/tpp-partner-hosted-onboarding) |
""",
                slug="embedded-signup",
            ),
        )
    write_order(
        emb,
        [
            "partner-hosted-embedded-sign-up-flow",
            "tech-partner-hosted-embed-sign-up-flow",
            "error-codes",
            "tpp-partner-hosted-onboarding",
        ],
    )

    # --- passthrough / meta ---
    pt = base / "meta-passthrough"
    for name in [
        "meta-passthrough-apis.md",
        "passthrough_apis_flow_management.md",
        "passthrough-v3-incoming-events.md",
        "whatsapp-dynamic-flows.md",
        "whatsapp-pay-events.md",
        "whatsapp-passthrough-apis-for-partners.md",
        "for-partners.md",
        "get-started-guide-with-gupshup-flow-management-apis.md",
    ]:
        move_to_folder(base / name, pt)
    write(
        pt / "index.md",
        page(
            "Meta Passthrough & Flows",
            "Passthrough messaging and Flow management for Partners.",
            """# Meta Passthrough & Flows

| Topic | Guide |
|-------|-------|
| Meta passthrough APIs | [Meta passthrough APIs](/docs/meta-passthrough-apis) |
| Flow management | [Passthrough — Flow Management](/docs/passthrough_apis_flow_management) |
| V3 incoming events | [Passthrough V3 Incoming Events](/docs/passthrough-v3-incoming-events) |
| Dynamic flows | [WhatsApp Dynamic Flows](/docs/whatsapp-dynamic-flows) |
| WhatsApp Pay events | [WhatsApp Pay Events](/docs/whatsapp-pay-events) |
""",
            slug="meta-passthrough",
        ),
    )
    write_order(
        pt,
        [
            "meta-passthrough-apis",
            "passthrough_apis_flow_management",
            "passthrough-v3-incoming-events",
            "whatsapp-dynamic-flows",
            "whatsapp-pay-events",
            "whatsapp-passthrough-apis-for-partners",
            "for-partners",
            "get-started-guide-with-gupshup-flow-management-apis",
        ],
    )

    # Parent onboarding order — expandable folders + top-level pages
    write_order(
        base,
        [
            "onboarding-overview",
            "onboarding-apis",
            "webhooks-and-callback",
            "inbound-events-v2",
            "v3-events",
            "coexistence",
            "embedded-signup",
            "meta-passthrough",
            "gupshup-ip-allowlisting",
            "whatsapp-groups-sample-events",
        ],
    )


# ---------------------------------------------------------------------------
# MESSAGING — nested
# ---------------------------------------------------------------------------
def nest_messaging() -> None:
    base = DOCS / "messaging"

    inbound = base / "inbound-messages"
    for name in [
        "inbound-messages.md",
        "types-of-inbound-messages.md",
        "text.md",
        "media.md",
        "interactive.md",
        "singlemulti-product-message.md",
        "request-welcome.md",
        "other.md",
    ]:
        move_to_folder(base / name, inbound)
    # rename inbound-messages.md → keep as child? Use as index instead
    src = inbound / "inbound-messages.md"
    if src.exists():
        write(
            inbound / "index.md",
            page(
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
""",
                slug="inbound-messages",
            ),
        )
        src.unlink()
    write_order(
        inbound,
        [
            "types-of-inbound-messages",
            "text",
            "media",
            "interactive",
            "singlemulti-product-message",
            "request-welcome",
            "other",
        ],
    )

    voice = base / "voice"
    for name in [
        "guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup.md",
        "copy-of-guide-to-whatsapp-voice-inbound-sip-integration-via-gupshup.md",
        "obtain-user-call-permissions.md",
        "permanent-call-permissions-for-whatsapp-voice.md",
    ]:
        move_to_folder(base / name, voice)
    write(
        voice / "index.md",
        page(
            "Voice",
            "WhatsApp Voice (inbound/outbound) and SIP integration for partners.",
            """# Voice

| Topic | Guide |
|-------|-------|
| Voice Outbound & SIP | [Voice Outbound](/docs/guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup) |
| Voice Inbound | [Voice Inbound](/docs/copy-of-guide-to-whatsapp-voice-inbound-sip-integration-via-gupshup) |
| Call permissions | [Obtain User Call Permissions](/docs/obtain-user-call-permissions) |
| Permanent permissions | [Permanent Call Permissions](/docs/permanent-call-permissions-for-whatsapp-voice) |
""",
            slug="voice",
        ),
    )
    write_order(
        voice,
        [
            "guide-to-voice-outbound-business-initiated-calls-sip-integration-via-gupshup",
            "copy-of-guide-to-whatsapp-voice-inbound-sip-integration-via-gupshup",
            "obtain-user-call-permissions",
            "permanent-call-permissions-for-whatsapp-voice",
        ],
    )

    write_order(
        base,
        [
            "messaging-overview",
            "whatsapp-messages",
            "welcome-messages",
            "outbound-messages",
            "inbound-messages",
            "media-management",
            "marketing-messages-lite-mm-lite-api",
            "voice",
            "mark-message-as-readtyping-indicator",
            "partner-whatsapp-groups-api-beta",
        ],
    )


# ---------------------------------------------------------------------------
# PARTNER HUB — nested
# ---------------------------------------------------------------------------
def nest_partner_hub() -> None:
    base = DOCS / "partner-hub"

    portal = base / "portal"
    for name in [
        "get-started-with-partner-portal.md",
        "partner-portal-walkthrough.md",
        "partner-customer-portal.md",
        "partner-customer-migration-to-partner-customer-portal-pcp.md",
    ]:
        move_to_folder(base / name, portal)
    write(
        portal / "index.md",
        page(
            "Partner Portal",
            "Partner Portal UI guides for managing customers and WABAs.",
            """# Partner Portal

| Topic | Guide |
|-------|-------|
| Get started | [Get started with Partner Portal](/docs/get-started-with-partner-portal) |
| Walkthrough | [Partner Portal Walkthrough](/docs/partner-portal-walkthrough) |
| Customer portal | [Partner Customer Portal](/docs/partner-customer-portal) |
| PCP migration | [Customer Migration to PCP](/docs/partner-customer-migration-to-partner-customer-portal-pcp) |
""",
            slug="portal",
        ),
    )
    write_order(
        portal,
        [
            "get-started-with-partner-portal",
            "partner-portal-walkthrough",
            "partner-customer-portal",
            "partner-customer-migration-to-partner-customer-portal-pcp",
        ],
    )

    wallet = base / "wallet"
    for name in [
        "wallet-1.md",
        "commissions.md",
        "overdraft-limit.md",
        "partner-wallet-balance-transfer.md",
        "partner-wallet-balance-transfer-copy.md",
        "recharge-via-stipe-or-ebanx.md",
        "wire-transfer-automation.md",
        "unused-commission-policy.md",
    ]:
        move_to_folder(base / name, wallet)
    write(
        wallet / "index.md",
        page(
            "Wallet & Billing",
            "Prepaid wallet, commissions, and billing for partners.",
            """# Wallet & Billing

| Topic | Guide |
|-------|-------|
| Wallet | [Wallet](/docs/wallet-1) |
| Wallet overview / commissions | [Commissions](/docs/commissions) |
| Overdraft | [Overdraft Limit](/docs/overdraft-limit) |
| Balance transfer | [Wallet Balance Transfer](/docs/partner-wallet-balance-transfer) |
| Recharge | [Recharge via Stripe or Ebanx](/docs/recharge-via-stipe-or-ebanx) |
| Wire transfers | [Wire Transfers](/docs/wire-transfer-automation) |
| Unused commissions | [Unused Commission Policy](/docs/unused-commission-policy) |
""",
            slug="wallet",
        ),
    )
    write_order(
        wallet,
        [
            "wallet-1",
            "commissions",
            "overdraft-limit",
            "partner-wallet-balance-transfer",
            "recharge-via-stipe-or-ebanx",
            "wire-transfer-automation",
            "unused-commission-policy",
            "partner-wallet-balance-transfer-copy",
        ],
    )

    write_order(
        base,
        [
            "partner-hub-overview",
            "portal",
            "wallet",
            "support",
            "meta-whatsapp-features",
        ],
    )


# ---------------------------------------------------------------------------
# PARTNER API (Guides) — api-reference needs index.md
# ---------------------------------------------------------------------------
def nest_partner_api_guides() -> None:
    api = DOCS / "partner-api"
    ref = api / "api-reference"

    # Convert api-reference-overview.md → index.md
    overview = ref / "api-reference-overview.md"
    if overview.exists():
        write(
            ref / "index.md",
            page(
                "API Reference",
                "Partner API endpoints grouped by business category.",
                """# API Reference

Browse Partner API endpoints by business capability (same structure as 360dialog).

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

Open the chevron on **API Reference** in the sidebar to browse each category. For interactive Try It, use the top **API Reference** tab.
""",
                slug="api-reference",
            ),
        )
        overview.unlink()
        print("REMOVED api-reference-overview.md → api-reference/index.md")

    # Convert each category .md into a folder with index.md so they can later hold children
    # For Guides, leaf categories as folders-with-only-index still show as pages.
    # Keep them as .md leaf pages under api-reference (expandable parent is enough).
    write_order(
        ref,
        [
            "partner-management",
            "channel-management",
            "waba-account-management",
            "webhook-management",
            "balance-and-usage",
            "templates-management",
            "messaging-v3",
            "media-management",
            "whatsapp-flows",
            "business-profile",
            "user-management",
            "marketing-messages-lite",
        ],
    )
    write_order(api, ["partner-api-overview", "authentication", "api-reference"])


# ---------------------------------------------------------------------------
# REFERENCE TAB — make categories expandable with endpoint children
# ---------------------------------------------------------------------------
def nest_reference_api() -> None:
    """
    Move key endpoint pages under the 12 category folders so Reference sidebar
    expands Category → endpoints (360 style). Hide bulk legacy dump folders.
    """
    # Map: category folder → list of endpoint .md paths (relative to Partner APIs)
    mapping: dict[str, list[str]] = {
        "partner-management": [
            "partner-app-management/token/post_partner-account-login.md",
            "partner-app-management/app/get_partner-account-api-partnerapps.md",
            "partner-app-management/app/post_partner-account-api-applink.md",
        ],
        "channel-management": [
            "app-onboarding-apis/post_partner-app.md",
            "app-onboarding-apis/put_partner-app-appid.md",
            "app-onboarding-apis/get_partner-app-list.md",
        ],
        "waba-account-management": [],
        "webhook-management": [],
        "balance-and-usage": [],
        "templates-management": [],
        "messaging-v3": [],
        "media-management": [],
        "whatsapp-flows": [],
        "business-profile": [
            "partner-app-management/business-profile/get_partner-app-appid-business-profile.md",
            "partner-app-management/business-profile/put_partner-app-appid-business-profile.md",
            "partner-app-management/business-profile/get_partner-app-appid-business-profile-photo.md",
        ],
        "user-management": [
            "partner-app-management/block-user/get_partner-app-appid-user-blocklist.md",
            "partner-app-management/block-user/post_partner-app-appid-user-block.md",
            "partner-app-management/block-user/post_partner-app-appid-user-unblock.md",
        ],
        "marketing-messages-lite": [],
    }

    # Auto-discover more endpoints by filename patterns into categories
    auto_rules = [
        ("templates-management", "template-apis", None),
        ("messaging-v3", "partner-meta-and-whatsapp-apis/passthrough-apis", None),
        ("whatsapp-flows", "partner-meta-and-whatsapp-apis/flow-management", None),
        ("media-management", "partner-app-management/generate-media-id", None),
        ("webhook-management", "partner-app-management/subscription-management", None),
        ("webhook-management", "partner-app-management/set-callback-url", None),
        ("balance-and-usage", "partner-app-management/commission", None),
        ("channel-management", "app-onboarding-apis", None),
        ("waba-account-management", "partner-app-management/phone-for-an-app", None),
        ("waba-account-management", "partner-app-management/analytics", None),
        ("marketing-messages-lite", "mmliteapi", None),
        ("partner-management", "partner-app-management/token", None),
        ("partner-management", "partner-app-management/partners-linked-application", None),
    ]

    for cat, rel, _ in auto_rules:
        src_dir = REF / rel
        if not src_dir.exists():
            continue
        for md in src_dir.rglob("*.md"):
            if md.name in ("index.md",):
                continue
            mapping.setdefault(cat, [])
            rel_path = str(md.relative_to(REF))
            if rel_path not in mapping[cat]:
                mapping[cat].append(rel_path)

    for cat, files in mapping.items():
        dest = REF / cat
        dest.mkdir(parents=True, exist_ok=True)
        child_slugs = []
        for rel in files:
            src = REF / rel
            if not src.exists():
                continue
            # Avoid name collisions
            dest_file = dest / src.name
            if dest_file.exists() and dest_file.resolve() != src.resolve():
                # already there
                child_slugs.append(src.stem)
                continue
            if src.parent.resolve() == dest.resolve():
                child_slugs.append(src.stem)
                continue
            shutil.copy2(src, dest_file)  # copy to avoid breaking old paths during transition
            # Soft-hide original by setting hidden? Keep originals but mark hidden
            try:
                text = src.read_text(encoding="utf-8")
                if "hidden: true" not in text.split("---", 2)[1]:
                    text = text.replace("hidden: false", "hidden: true", 1)
                    if "hidden:" not in text.split("---", 2)[1]:
                        text = text.replace("---\n", "---\nhidden: true\n", 1)
                    src.write_text(text, encoding="utf-8")
            except Exception:
                pass
            child_slugs.append(src.stem)
            print(f"COPY {rel} → {cat}/{src.name}")

        # Ensure index.md exists
        if not (dest / "index.md").exists():
            write(
                dest / "index.md",
                page(
                    cat.replace("-", " ").title(),
                    f"{cat} APIs",
                    f"# {cat.replace('-', ' ').title()}\n\nBrowse endpoints in the sidebar.",
                    slug=cat,
                ),
            )

        # Dedupe preserve order
        seen = set()
        ordered = []
        for s in child_slugs:
            if s not in seen and s != "index":
                seen.add(s)
                ordered.append(s)
        # Also include any other md already in folder
        for p in dest.glob("*.md"):
            if p.name != "index.md" and p.stem not in seen:
                ordered.append(p.stem)
        write_order(dest, ordered)

    # Hide bulky legacy folders at Partner APIs root by marking their index hidden
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
    for name in legacy:
        idx = REF / name / "index.md"
        if idx.exists():
            text = idx.read_text(encoding="utf-8")
            text = text.replace("hidden: false", "hidden: true", 1)
            if "hidden:" not in text.split("---", 2)[1]:
                text = text.replace("---\n", "---\nhidden: true\n", 1)
            idx.write_text(text, encoding="utf-8")
            print(f"HIDDEN legacy folder index: {name}")

    # Clean Reference order: overview + 12 categories only (legacy hidden still listed last optional)
    categories = [
        "partner-management",
        "channel-management",
        "waba-account-management",
        "webhook-management",
        "balance-and-usage",
        "templates-management",
        "messaging-v3",
        "media-management",
        "whatsapp-flows",
        "business-profile",
        "user-management",
        "marketing-messages-lite",
    ]
    write_order(REF, ["partner-api-overview"] + categories)

    # Rewrite partner-api-overview for Reference
    write(
        REF / "partner-api-overview.md",
        page(
            "Partner API Overview",
            "Gupshup Partner API reference organized by business category.",
            """# Partner API

Browse the sidebar by category. Expand a category to see its endpoints (Try It available on each endpoint page).

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
""",
            slug="partner-api-overview",
        ),
    )


def main() -> None:
    print("=== Get Started / Quickstarts ===")
    fix_get_started()
    print("\n=== Onboarding nesting ===")
    nest_onboarding()
    print("\n=== Messaging nesting ===")
    nest_messaging()
    print("\n=== Partner Hub nesting ===")
    nest_partner_hub()
    print("\n=== Partner API Guides nesting ===")
    nest_partner_api_guides()
    print("\n=== Reference API nesting ===")
    nest_reference_api()
    print("\nDone.")


if __name__ == "__main__":
    main()
