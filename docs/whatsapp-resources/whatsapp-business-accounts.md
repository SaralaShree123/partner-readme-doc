---
title: WhatsApp Business Accounts
icon: fa-duotone fa-building
summary: WhatsApp Business Account (WABA) basics for partners.
excerpt: WhatsApp Business Account (WABA) basics for partners.
deprecated: false
hidden: false
metadata:
  robots: index
slug: what-is-a-waba
---

# WhatsApp Business Accounts

A **WhatsApp Business Account (WABA)** stores the phone numbers registered on the WhatsApp Business Platform. Partners create and manage WABAs for their customers through Gupshup.

## WABA types

There are two common WABA types:

| Type | What it is |
|------|------------|
| **WhatsApp Business app account** | Created in Meta Business Suite. Can connect one phone number to both the WhatsApp Business app and the WhatsApp Business Platform using [coexistence](/docs/what-is-coexistence). Typically limited to one number and cannot be migrated to another Meta business portfolio. |
| **WhatsApp Business Platform account** | Created through a BSP such as Gupshup (usually via Embedded Signup). Used for Cloud API messaging. Can hold multiple phone numbers and supports portfolio migration in supported cases. |

## Why it matters for partners

- Every WhatsApp number you onboard sits under a WABA.
- Templates, quality rating, and messaging limits relate to the WABA and its phone numbers / business portfolio.
- Partner APIs for channels, templates, and account health operate on WABA-linked apps.

## Common limitations

- A WABA can have a maximum of **250** message templates.
- Meta Business portfolios are initially limited in how many phone numbers and WABAs they can hold (limits can increase over time).
- A WABA belongs to only one Meta Business portfolio.
- Time zone and currency rules may be locked once billing/credit line settings are attached.

## WABA ID

Each WABA has a unique **WABA ID**, shown in Meta Business Manager under WhatsApp Accounts. You will use this ID in Partner Portal and API workflows.

## Creating a WABA with Gupshup

Partners typically create WABAs by onboarding customers through **Embedded Signup** (or related Partner Portal / API flows), not by manual Meta-only setup alone.

## Related guides

- [Phone numbers](/docs/phone-numbers)
- [What is Embedded Signup?](/docs/what-is-embedded-signup)
- [Create your first App](/docs/create-your-first-app)
- [WABA Account Management APIs](/docs/waba-account-management)
