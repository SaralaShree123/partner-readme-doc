---
title: General Purpose AI Provider V2
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

V2 Webhook event:

`{"app":"TestingEndtoEnd","timestamp":1770372417279,"version":2,"type":"billing-event","payload":{"deductions":{"type":"regular","model":"PMP","source":"whatsapp","billable":true,"category":"general_purpose_ai"},"references":{"id":"wamid.HBgMOTE4ODcxNjAxMjk3FQIAERgSMTdCRE111UyRkNDNDc0RUU4MjA4AA==","destination":"398871601297"}}}`