---
summary: Subscription Management
title: Subscription Management
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To manage the subscription effectively, use [subscription](/reference/setsubscription-api-v3) API.

# Incoming Message

## Event - V3 - Status

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918375031069",
              "phone_number_id": "207437372456043"
            },
            "statuses": [
              {
                "gs_id": "3de985af-d06e-41e1-acaf-c379b429668a",
                "id": "fc46fadf-5075-4bb6-9cff-f3ff8c6f6478",
                "recipient_id": "919970754444",
                "status": "read",
                "timestamp": "1705574869"
              }
            ]
          }
        }
      ],
      "id": "216141188246170"
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

## Event - V3 - Message

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "contacts": [
              {
                "profile": {
                  "name": "Sneha"
                },
                "wa_id": "91997075****"
              }
            ],
            "messages": [
              {
                "from": "91997075***",
                "id": "wamid.HBgMOTE5OTcwNzU0NDQ0FQIAEhgUM0E1NjIzMTY1N0VGNUE5NjY1M0EA",
                "text": {
                  "body": "Hi"
                },
                "timestamp": "1705574871",
                "type": "text"
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918375031069",
              "phone_number_id": "207437372456043"
            }
          }
        }
      ],
      "id": "216141188246170"
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```