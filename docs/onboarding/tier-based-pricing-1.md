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

Sample V3 Webhook Payload

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "account_update",
          "value": {
            "event": "VOLUME_BASED_PRICING_TIER_UPDATE",
            "volume_tier_info": {
              "effective_month": "2025-11",
              "pricing_category": "UTILITY",
              "region": "INDIA",
              "tier": "25000001:50000000",
              "tier_update_time": 1743451903
            }
          }
        }
      ],
      "id": "216141188246170",
      "time": 1743451903
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

<br />

| **Field**                                                   | **Type** | **Description**                                                       |
| ----------------------------------------------------------- | -------- | --------------------------------------------------------------------- |
| `object`                                                    | string   | Type of object — `whatsapp_business_account`                          |
| `gs_app_id`                                                 | string   | Unique Gupshup App ID associated with the event                       |
| `entry[].id`                                                | string   | WhatsApp Business Account (WABA) ID                                   |
| `entry[].time`                                              | number   | Unix timestamp when the event was generated                           |
| `entry[].changes[].field`                                   | string   | Event field name — `account_update`                                   |
| `entry[].changes[].value.event`                             | string   | Type of event triggered — `VOLUME_BASED_PRICING_TIER_UPDATE`          |
| `entry[].changes[].value.volume_tier_info.effective_month`  | string   | Month (YYYY-MM) when the new pricing tier becomes effective           |
| `entry[].changes[].value.volume_tier_info.pricing_category` | string   | Template category affected (e.g., UTILITY, MARKETING, AUTHENTICATION) |
| `entry[].changes[].value.volume_tier_info.region`           | string   | Region or country where the tier applies                              |
| `entry[].changes[].value.volume_tier_info.tier`             | string   | New volume tier range (e.g., `25000001:50000000`)                     |
| `entry[].changes[].value.volume_tier_info.tier_update_time` | number   | Unix timestamp indicating when the WABA reached the new tier          |

<br />