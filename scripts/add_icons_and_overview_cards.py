#!/usr/bin/env python3
"""Add 360-style icons + Overview cards. Write CSS snippet for bold category headings."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def set_icon(path: Path, icon: str) -> None:
    if not path.exists():
        print(f"SKIP missing {path}")
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return
    parts = text.split("---", 2)
    fm, body = parts[1], parts[2]
    if re.search(r"^icon:\s*", fm, re.M):
        fm = re.sub(r"^icon:\s*.*$", f"icon: {icon}", fm, count=1, flags=re.M)
    else:
        # insert after title
        if re.search(r"^title:\s*.+$", fm, re.M):
            fm = re.sub(r"^(title:\s*.+)$", rf"\1\nicon: {icon}", fm, count=1, flags=re.M)
        else:
            fm = f"\nicon: {icon}" + fm
    path.write_text(f"---{fm}---{body}", encoding="utf-8")
    print(f"ICON {path.relative_to(ROOT)} → {icon}")


# Page icons (mirrors 360dialog hand / rocket / book style via Font Awesome duotone)
ICONS = {
    # Get Started
    "docs/get-started/overview.md": "fa-duotone fa-hand-wave",
    "docs/get-started/quickstarts/index.md": "fa-duotone fa-rocket-launch",
    "docs/get-started/pricing.md": "fa-duotone fa-tags",
    "docs/get-started/what-is-sp-tp.md": "fa-duotone fa-handshake",
    "docs/get-started/gupshup-partner-eco-system.md": "fa-duotone fa-building",
    "docs/get-started/quickstarts/get-started-as-partner.md": "fa-duotone fa-user-plus",
    "docs/get-started/quickstarts/register-as-tech-provider.md": "fa-duotone fa-id-card",
    "docs/get-started/quickstarts/create-your-first-app.md": "fa-duotone fa-mobile",
    "docs/get-started/quickstarts/generate-secret-and-token.md": "fa-duotone fa-key",
    "docs/get-started/quickstarts/send-your-first-message.md": "fa-duotone fa-paper-plane",
    # Onboarding
    "docs/onboarding/onboarding-overview.md": "fa-duotone fa-route",
    "docs/onboarding/onboarding-apis.md": "fa-duotone fa-code",
    "docs/onboarding/webhooks-and-callback/index.md": "fa-duotone fa-webhook",
    "docs/onboarding/inbound-events-v2/index.md": "fa-duotone fa-bell",
    "docs/onboarding/v3-events/index.md": "fa-duotone fa-bolt",
    "docs/onboarding/coexistence/index.md": "fa-duotone fa-arrows-rotate",
    "docs/onboarding/embedded-signup/index.md": "fa-duotone fa-window",
    "docs/onboarding/meta-passthrough/index.md": "fa-duotone fa-share-nodes",
    # Partner API
    "docs/partner-api/partner-api-overview.md": "fa-duotone fa-brackets-curly",
    "docs/partner-api/authentication.md": "fa-duotone fa-lock",
    "docs/partner-api/api-reference/index.md": "fa-duotone fa-book",
    # Partner Hub
    "docs/partner-hub/partner-hub-overview.md": "fa-duotone fa-grid-2",
    "docs/partner-hub/portal/index.md": "fa-duotone fa-browser",
    "docs/partner-hub/wallet/index.md": "fa-duotone fa-wallet",
    "docs/partner-hub/support.md": "fa-duotone fa-life-ring",
    # Messaging
    "docs/messaging/messaging-overview.md": "fa-duotone fa-messages",
    "docs/messaging/whatsapp-messages.md": "fa-duotone fa-comment",
    "docs/messaging/inbound-messages/index.md": "fa-duotone fa-inbox-in",
    "docs/messaging/voice/index.md": "fa-duotone fa-phone",
    # Commerce / Security / Meta
    "docs/commerce-and-payments/commerce-overview.md": "fa-duotone fa-cart-shopping",
    "docs/security/security-overview.md": "fa-duotone fa-shield-halved",
    "docs/meta-whatsapp-features/meta-whatsapp-features-overview.md": "fa-duotone fa-sparkles",
}


OVERVIEW = """---
title: Overview
icon: fa-duotone fa-hand-wave
summary: Welcome to the Gupshup Partner Documentation Hub
excerpt: Welcome to the Gupshup Partner Documentation Hub
deprecated: false
hidden: false
metadata:
  robots: index
slug: overview
---

# Overview

This documentation is a central resource for current and prospective **Gupshup integration partners**. It provides the technical and operational guidance needed to build, launch, and scale WhatsApp Business API solutions using the Gupshup platform.

<Callout icon="📘" theme="info">
  **For Gupshup Partners**

  This documentation is intended for Gupshup Partners and focuses on partner-specific concepts, workflows, and integration requirements.

  Sign up at [partner.gupshup.io](https://partner.gupshup.io/).
</Callout>

---

## Get started

Kick off your Partner journey with quick access to the most essential guides and tools.

<Cards>
  <Card kind="tile" title="Partner API Reference" href="/docs/api-reference" icon="fa-duotone fa-brackets-curly">
    Explore the complete API reference for building and managing integrations.
  </Card>
  <Card kind="tile" title="Quickstarts" href="/docs/quickstarts" icon="fa-duotone fa-rocket-launch">
    Five steps from partner signup to your first WhatsApp message.
  </Card>
  <Card kind="tile" title="Early Access & Features" href="/docs/meta-whatsapp-features-overview" icon="fa-duotone fa-sparkles">
    Be first to access WhatsApp’s newest features and stay ahead.
  </Card>
  <Card kind="tile" title="24/7 Support" href="/docs/support" icon="fa-duotone fa-life-ring">
    Expert support with escalation paths for urgent issues.
  </Card>
</Cards>

<br />

## Who is Gupshup for?

From SaaS platforms to software vendors, Gupshup serves a diverse range of Partner use cases.

| Partner Type | How They Benefit from Gupshup |
|--------------|-------------------------------|
| SaaS Platforms | Add WhatsApp messaging into your product and automate client workflows |
| Enterprises | Deploy large-scale messaging for sales, marketing, and support use cases |
| Agencies & Developers | Build WhatsApp-powered solutions and tools |
| ISVs | Become a Meta Tech Provider with Gupshup’s partner platform |

---

## How it works

Gupshup provides a developer-first, API-driven approach to WhatsApp Business messaging.
Easily integrate, onboard clients, and manage messaging workflows within a scalable, partner-friendly ecosystem.

### Partner journey

<Cards columns={2}>
  <Card kind="tile" title="1. Set up your Partner account" href="/docs/get-started-as-partner" icon="fa-duotone fa-user-plus">
    Create a partner account, set API credentials, and start testing.
  </Card>
  <Card kind="tile" title="2. Integrate Partner APIs" href="/docs/generate-secret-and-token" icon="fa-duotone fa-plug">
    Connect Partner APIs and integrate them into your solution.
  </Card>
  <Card kind="tile" title="3. Onboard clients & manage WABAs" href="/docs/create-your-first-app" icon="fa-duotone fa-building">
    Add numbers, onboard clients, and start messaging.
  </Card>
  <Card kind="tile" title="4. Scale & optimise messaging" href="/docs/send-your-first-message" icon="fa-duotone fa-chart-line">
    Optimise performance, drive revenue, and grow fast.
  </Card>
</Cards>

<br />

## Documentation sections

<Cards columns={3}>
  <Card kind="tile" title="Get Started" href="/docs/overview" icon="fa-duotone fa-hand-wave">
    Landing, quickstarts, pricing, Tech Provider program
  </Card>
  <Card kind="tile" title="Onboarding" href="/docs/onboarding-overview" icon="fa-duotone fa-route">
    Webhooks, events, coexistence, onboarding APIs
  </Card>
  <Card kind="tile" title="Partner API" href="/docs/partner-api-overview" icon="fa-duotone fa-brackets-curly">
    REST APIs grouped by business category
  </Card>
  <Card kind="tile" title="Partner Hub" href="/docs/partner-hub-overview" icon="fa-duotone fa-grid-2">
    Portal UI, wallet, billing, support
  </Card>
  <Card kind="tile" title="Messaging" href="/docs/messaging-overview" icon="fa-duotone fa-messages">
    Templates, session messages, media, voice
  </Card>
  <Card kind="tile" title="Commerce & Payments" href="/docs/commerce-overview" icon="fa-duotone fa-cart-shopping">
    Brazil payments, INR wallet, wire transfers
  </Card>
</Cards>

<br />

## Next steps

<Cards>
  <Card title="Explore Quickstarts" href="/docs/quickstarts" icon="fa-duotone fa-rocket-launch">
    Five steps to your first message
  </Card>
  <Card title="See Pricing" href="/docs/pricing" icon="fa-duotone fa-tags">
    Costs associated with becoming a Gupshup Partner
  </Card>
  <Card title="Learn About Tech Providers" href="/docs/what-is-sp-tp" icon="fa-duotone fa-handshake">
    Solution Partners & Tech Providers
  </Card>
</Cards>
"""

CSS = """/* ============================================================
   Paste into ReadMe → Settings → Custom CSS
   Makes main Guide categories look bold (360dialog-style hierarchy)
   ============================================================ */

/* Bold top-level category headings in the Guides sidebar */
.rm-Sidebar-heading,
.rm-Sidebar [class*="heading"],
.rm-Sidebar-section-title {
  font-weight: 700 !important;
  letter-spacing: 0.01em;
}

/* Category wrapper slightly stronger contrast */
.rm-Sidebar-wrapper > .rm-Sidebar-heading {
  font-size: 0.95rem;
  text-transform: none;
}

/* Active / hover polish */
.rm-Sidebar-link:hover {
  font-weight: 600;
}

/* Optional: give page icons a bit more presence next to titles */
.rm-Sidebar-link i,
.rm-Sidebar-link svg {
  opacity: 0.9;
}
"""


def main() -> None:
    (DOCS / "get-started" / "overview.md").write_text(OVERVIEW, encoding="utf-8")
    print("WROTE docs/get-started/overview.md (Cards + icons)")

    for rel, icon in ICONS.items():
        # skip overview (already has icon in OVERVIEW)
        if rel.endswith("get-started/overview.md"):
            continue
        # webhook icon may not exist in FA6 - use bolt-auto fallback friendly name
        if "webhook" in icon:
            icon = "fa-duotone fa-satellite-dish"
        set_icon(ROOT / rel, icon)

    css_path = ROOT / "APPEARANCE-CUSTOM-CSS.css"
    css_path.write_text(CSS, encoding="utf-8")
    print(f"WROTE {css_path.name}")

    guide = ROOT / "APPEARANCE-SETUP.md"
    guide.write_text(
        """# Appearance setup (360dialog look)

## 1. Bold main sections (Get Started, Onboarding, Partner API, …)

ReadMe does **not** bold category titles via Git. Paste this CSS:

1. Open ReadMe project → **Settings → Custom CSS** (or Appearance → Custom CSS)
2. Paste the contents of `APPEARANCE-CUSTOM-CSS.css`
3. Save

## 2. Page icons (hand / rocket / book)

Already set via `icon:` frontmatter on Overview, Quickstarts, and section hubs.
After Git sync, open a page in the ReadMe editor if an icon does not appear and re-select Font Awesome if needed.

## 3. Overview cards

Overview now uses ReadMe `<Cards>` / `<Card kind="tile">` blocks (Partner API Reference, Quickstarts, Early Access, Support) — same pattern as 360dialog’s Get started containers.
""",
        encoding="utf-8",
    )
    print("WROTE APPEARANCE-SETUP.md")


if __name__ == "__main__":
    main()
