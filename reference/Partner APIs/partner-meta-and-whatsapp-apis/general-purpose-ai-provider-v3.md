---
title: General Purpose AI Provider V3
excerpt: 'Billing event should be pushed to end partners for AI provider deductions '
deprecated: false
hidden: true
metadata:
  robots: index
---
```curl
curl --location --request POST 'https://qa-internal-wds.smsgupshup.dev/publisher/api/wa/events/cloud/918929190367' \
--header 'content-type: application/json' \
--data-raw '{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "758747873957634",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918929190367",
              "phone_number_id": "1005972845928404"
            },
            "statuses": [
              {
                "id": "wamid.HBgMOTE4ODcxNjAxMjk3FQIAERgSMTdCRE111UyRkNDNDc0RUU4MjA4AA==",
                "status": "delivered",
                "timestamp": "1770366909",
                "recipient_id": "398871601297",
                "conversation": {
                  "id": "c0ab246839b33ca5014b41fd2ede5b862e2",
                  "expiration_timestamp": "1770366909",
                  "origin": {
                    "type": "general_purpose_ai"
                  }
                },
                "pricing": {
                  "billable": true,
                  "pricing_model": "PMP",
                  "category": "general_purpose_ai",
                  "type": "regular"
                }
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}'
```

V3 webhook event:

`{"entry":[{"changes":[{"field":"billing-event","value":{"billing":{"deductions":{"billable":true,"category":"general_purpose_ai","model":"PMP","source":"whatsapp","type":"regular"},"references":{"destination":"398871601297","id":"wamid.HBgMOTE4ODcxNjAxMjk3FQIAERgSMTdCRE111UyRkNDNDc0RUU4MjA4AA=="}}}}]}],"gs_app_id":"4a1322a2-9f29-4faa-8961-8e58784c5e95","object":"whatsapp_business_account"}`