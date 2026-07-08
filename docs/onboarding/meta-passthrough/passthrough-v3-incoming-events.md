---
summary: Event payloads for passthrough APIs.
title: Passthrough (V3) Incoming events
excerpt: Event payloads for passthrough APIs.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Message Events

```Text Message Sent
{
  "gs_app_id" : "GUPSHUP_APP_ID",
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "BUSINESS_DISPLAY_PHONE_NUMBER",
              "phone_number_id": "BUSINESS_PHONE_NUMBER_ID"
            },
            "statuses": [
              {
                "id": "WHATSAPP_MESSAGE_ID",
                "gs_id": "GUPSHUP_MESSAGE_ID",
                "status": "sent",
                "timestamp": "TIMESTAMP",
                "recipient_id": "CUSTOMER_PHONE_NUMBER",
                "conversation": {
                  "id": "CONVERSATION_ID",
                  "expiration_timestamp": "CONVERSATION_EXPIRATION_TIMESTAMP",
                  "origin": {
                    "type": "user_initiated"
                  }
                },
                "pricing": {
                  "billable": true,
                  "pricing_model": "CBP",
                  "category": "service"
                }
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}
```
```Text callback start
{
    "object": "whatsapp_business_account",
    "gs_app_id": "GUPSHUP_APP_ID",
    "entry": [
        {
            "changes": [
                {
                    "field": "messages",
                    "value": {
                        "messaging_product": "whatsapp",
                        "statuses": [
                            {
                                "type": "set-callback"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
```
```Text Enqueued
{
  "gs_app_id" : "GUPSHUP_APP_ID",
  "object": "whatsapp_business_account",
  "entry": [
    {
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "statuses": [
              {
                "id": "WHATSAPP_MESSAGE_ID",
                "gs_id": "GUPSHUP_MESSAGE_ID",
                "status": "enqueued",
                "timestamp": "TIMESTAMP",
                "recipient_id": "CUSTOMER_PHONE_NUMBER"
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}


```
```Text Failed
{
  "gs_app_id": "GUPSHUP_APP_ID",
  "object": "whatsapp_business_account",
  "entry": [
    {
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "statuses": [
              {
                "id": "WHATSAPP_MESSAGE_ID",
                "gs_id": "GUPSHUP_MESSAGE_ID",
                "status": "failed",
                "timestamp": "TIMESTAMP",
                "recipient_id": "CUSTOMER_PHONE_NUMBER",
                "code": "",
                "reason": ""
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}

```