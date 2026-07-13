---
title: Phone numbers
icon: fa-duotone fa-phone
summary: WhatsApp business phone number requirements and basics for partners.
excerpt: WhatsApp business phone number requirements and basics for partners.
deprecated: false
hidden: false
metadata:
  robots: index
slug: phone-numbers
---

# Phone numbers

A valid **business phone number** must be registered before it can send and receive messages on the WhatsApp Business Platform. Registered numbers can still be used for ordinary calling and SMS, but they cannot be used with the personal WhatsApp (“WhatsApp Messenger”) app at the same time (unless you are using [coexistence](/docs/what-is-coexistence) with the WhatsApp Business app).

## Eligibility requirements

To register a number for WhatsApp Business Platform use, it typically must:

- Be owned by the business (unless using a Meta-provided special number where allowed)
- Include a valid country code and area code (short codes are not supported)
- Be able to receive voice calls or SMS for verification

Use an existing business-owned number when possible. Gupshup does not provide phone numbers as part of the partner service.

## Numbers already on WhatsApp

| Current use | What usually applies |
|-------------|----------------------|
| Personal WhatsApp Messenger | Cannot register for Business Platform until the Messenger account is deleted (or unbanned via Meta’s process if banned) |
| WhatsApp Business app | May be eligible for [coexistence](/docs/what-is-coexistence) instead of a fresh Cloud API-only registration |
| Already on Cloud API with another BSP | Usually requires a migration flow, not a fresh Embedded Signup |

Choosing the correct option during Embedded Signup depends on whether the number is already connected to WhatsApp API, Business app, or personal WhatsApp.

## Phone number limits

New Meta business portfolios are often capped at a small number of registered business phone numbers at first (for example starting at 2, with room to grow). Limits can increase based on verification and messaging activity. When a limit increases, Meta may send a `business_capability_update` webhook and a Business Suite notification.

## Where to view numbers

Business phone numbers and status appear in **Meta Business Manager → WhatsApp Accounts → WhatsApp Manager → Phone numbers**.

## Downgrade / delete a number

Deleting (downgrading) a number from the WhatsApp Business Platform can free it for use on personal WhatsApp or the WhatsApp Business app, or for re-registration later. This is done in Meta’s WhatsApp Manager (not via a Partner API). Numbers that sent paid messages recently may be blocked from deletion for a period (commonly 30 days).

## Related guides

- [What is a WABA?](/docs/what-is-a-waba)
- [What is Embedded Signup?](/docs/what-is-embedded-signup)
- [What is coexistence?](/docs/what-is-coexistence)
- [Embedded Signup](/docs/embedded-signup)
