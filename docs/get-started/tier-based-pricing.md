---
summary: Tier Update Webhook (VOLUME_BASED_PRICING_TIER_UPDATE)
title: Tier Based Pricing
excerpt: Tier Update Webhook (VOLUME_BASED_PRICING_TIER_UPDATE)
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

Starting October 1, 2025, Meta will trigger a new account_update webhook event — VOLUME_BASED_PRICING_TIER_UPDATE — whenever a WhatsApp Business Account (WABA) moves to a new volume-based pricing tier within any market during a given month.

This webhook provides transparency into pricing tier changes and helps partners update their billing or usage systems accordingly.

Sample V2 Webhook Payload

```json
{
    "app": "Jan10pass",
    "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
    "timestamp": 1762331373939,
    "version": 2,
    "type": "account-event",
    "payload": {
        "type": "pricing-tier-update",
        "payload": {
            "effectiveMonth": "2025-11",
            "pricingCategory": "UTILITY",
            "region": "INDIA",
            "tier": "25000001:50000000",
            "tierUpdateTime": 1743451903
        }
    }
}
```

<br />

### Field Descriptions

| Field                             | Type   | Description                                                           |
| --------------------------------- | ------ | --------------------------------------------------------------------- |
| `app`                             | string | Partner App name                                                      |
| `appId`                           | string | Unique App ID                                                         |
| `timestamp`                       | number | Time (in Unix milliseconds) when the event was generated              |
| `version`                         | number | API subscription version (2 or 3)                                     |
| `type`                            | string | Type of webhook event — `account-event`                               |
| `payload.type`                    | string | Event subtype — `pricing-tier-update`                                 |
| `payload.payload.effectiveMonth`  | string | Month (YYYY-MM) when the new pricing tier becomes effective           |
| `payload.payload.pricingCategory` | string | Template category affected (e.g., UTILITY, MARKETING, AUTHENTICATION) |
| `payload.payload.region`          | string | Region/country where the tier applies                                 |
| `payload.payload.tier`            | string | New volume tier range (e.g., `25000001:50000000`)                     |
| `payload.payload.tierUpdateTime`  | number | Unix timestamp indicating when the WABA reached the new tier          |

<br />