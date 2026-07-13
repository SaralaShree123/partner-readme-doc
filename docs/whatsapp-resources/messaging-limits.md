---
title: Messaging limits
icon: fa-duotone fa-gauge-high
summary: How WhatsApp messaging limits affect how many users you can message.
excerpt: How WhatsApp messaging limits affect how many users you can message.
deprecated: false
hidden: false
metadata:
  robots: index
slug: messaging-limits
---

# Messaging limits

**Messaging limits** define how many unique WhatsApp users a business can message with **business-initiated** messages in a moving 24-hour period, outside an open customer service window.

Limits protect user experience and scale up when quality and responsible sending are demonstrated.

## How they work

- Limits are applied at the **Meta business portfolio** level and shared across phone numbers in that portfolio.
- One number can consume the portfolio’s available capacity.
- Only conversations started **outside** the customer service window count toward the limit.
- Replies inside an open customer care window are not counted the same way as business-initiated template outreach.

## Default tiers

New businesses often start at a lower tier (commonly **250** unique users per 24 hours). Limits can scale through tiers such as:

- 2,000
- 10,000
- 100,000
- Unlimited

Increases are controlled by Meta and generally cannot be requested manually through a BSP.

## How limits increase

To reach higher tiers, businesses typically need to:

1. Complete a scaling path (for example business verification, and/or delivering enough high-quality template messages to unique users over a period), then
2. Qualify for **automatic scaling** based on message quality and using a meaningful share of the current limit

When scaling is approved or denied, Meta may notify via email/developer alerts and `business_capability_update` webhooks.

## Quality matters

Poor quality (blocks, reports, low-quality templates) can slow or reverse scaling. Maintaining template quality and expected messaging is essential.

## Checking limits

In Meta: **Business Suite → WhatsApp Manager → Account tools → Messaging limits**.

## Related guides

- [Partner Rate Limits](/docs/partner-rate-limits) (Gupshup API request rate limits — different from Meta messaging limits)
- [What is a WABA?](/docs/what-is-a-waba)
- [Send your first message](/docs/send-your-first-message)
- [Messaging](/docs/messaging-overview)
