---
title: Get Profile Details
excerpt: >-
  Retrieves the WhatsApp Business profile information for a specific partner
  application. The business profile contains public-facing information about
  your business including address, description, email, website, and industry
  vertical.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-business-profile
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Parameters    | Value                     | Description                       |
| :------------ | :------------------------ | :-------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application  |
| appId         | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
            "profile": {
                "address": "<address>",
                "profileEmail": "<emailId>",
                "desc": "<description>",
                "vertical": "<vertical>",
                "website1": "<website1>",
                "website2": "<website2>"
            },
            "status": "success"
        }
```