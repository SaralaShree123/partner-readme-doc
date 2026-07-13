---
title: Coexistence
icon: fa-duotone fa-mobile
summary: Use the WhatsApp Business app and Cloud API on the same number.
excerpt: Use the WhatsApp Business app and Cloud API on the same number.
deprecated: false
hidden: false
metadata:
  robots: index
slug: what-is-coexistence
---

# Coexistence

**Coexistence** (also called **Coex**) lets a business use the same phone number on both the **WhatsApp Business app** and the **WhatsApp Business Platform (Cloud API)** through Gupshup.

That means the business can message at scale via API while still handling one-to-one chats in the WhatsApp Business app — without giving up the existing number, history, or audience.

## Why use coexistence?

- Keep the WhatsApp Business app for day-to-day chatting
- Add API messaging, insights, and Click-to-WhatsApp style growth
- Helpful for SMBs already active on the Business app who want to scale

Meta generally recommends coexistence for businesses **already using** the WhatsApp Business app consistently — not for brand-new Business app accounts that are not yet active.

## How communication works

Coexistence relies on **message echoes**:

- Messages sent via the API appear in the WhatsApp Business app automatically
- Messages sent from the WhatsApp Business app are delivered to your webhook (for example via `smb_message_echoes`) so your platform stays in sync

## Pricing (high level)

- Messages sent from the WhatsApp Business app remain free on WhatsApp’s app side
- Messages sent through the Cloud API follow WhatsApp Business Platform pricing
- Template messages are still required to start many business-initiated API conversations
- Service/session replies follow the usual customer service window rules

## Important constraints

- Do **not** uninstall the WhatsApp Business app after onboarding — that can disconnect the account
- Open the WhatsApp Business app at least once every **13 days** to keep the account active
- Chat history sync from the app to the platform is supported with the correct setup
- Some platform features may be limited on coexistence numbers (for example Official Business Account / blue badge behavior, some migrations, calling API, and profile picture updates after onboarding — confirm current Meta feature comparison for your use case)
- Companion/linked devices may be unlinked at onboarding; only supported devices can be re-linked

## Related guides

- [Coexistence](/docs/coexistence)
- [Coexistence guide](/docs/co-existence-closed-beta-phase)
- [Phone numbers](/docs/phone-numbers)
- [What is Embedded Signup?](/docs/what-is-embedded-signup)
- [Onboarding](/docs/onboarding-overview)
