---
title: Embedded Signup
icon: fa-duotone fa-window
summary: Embedded Signup lets customers connect WhatsApp without leaving your product.
excerpt: Embedded Signup lets customers connect WhatsApp without leaving your product.
deprecated: false
hidden: false
metadata:
  robots: index
slug: what-is-embedded-signup
---

# Embedded Signup

**Embedded Signup** is Meta’s onboarding flow that partners host inside their own product (or launch from Partner Portal). Customers create or connect a WhatsApp Business Account and phone number in one secure flow, instead of jumping across multiple portals.

## What it is used for

- Creating WhatsApp Business Accounts (WABAs)
- Registering business phone numbers on the WhatsApp Business Platform
- Sharing the required business assets with Gupshup so messaging can start

## Why partners use it

- Keeps onboarding inside your branded experience
- Reduces manual Partner Portal steps for each customer
- Works with Tech Provider and Solution Partner setups

## Choose the right path for the number

Before starting Embedded Signup, check how the phone number is already used:

| WhatsApp API | Personal WhatsApp | WhatsApp Business app | Typical path |
|--------------|-------------------|------------------------|--------------|
| Yes | No | No | Migration to Gupshup |
| Yes | No | Yes | Coexistence / COEX migration path |
| No | No | No | Standard Embedded Signup |
| No | No | Yes | [Coexistence](/docs/what-is-coexistence) onboarding |
| No | Yes | No | Embedded Signup (after Messenger account is cleared if required) |

## Typical prerequisites

- Partner account on Gupshup
- A valid business phone number that can receive SMS or voice OTP
- Meta Business portfolio admin access (where required)
- Complete business info (legal name, address, website, business phone) to reduce WABA restrictions
- A live HTTPS website that clearly describes the business (Meta integrity review)

Only an owner/admin of the Meta Business portfolio should complete the Facebook Login steps. Third parties should not navigate Embedded Signup on behalf of the business.

## Related guides

- [Embedded Signup](/docs/embedded-signup)
- [Partner-hosted Embedded Sign Up](/docs/tech-partner-hosted-embed-sign-up-flow)
- [Phone numbers](/docs/phone-numbers)
- [Channel Management APIs](/docs/channel-management)
