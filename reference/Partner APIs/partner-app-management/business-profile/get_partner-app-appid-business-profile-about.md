---
title: Get Profile About
excerpt: >-
  This API endpoint retrieves the 'About' text from the WhatsApp Business
  profile for a specific partner application. The about text is the business
  description that appears on your WhatsApp Business profile and provides a
  brief introduction to your business, services, or mission. This is a
  simplified endpoint that returns only the description text, unlike the full
  profile endpoint which returns all profile fields.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-business-profile-about
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
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/about' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
            "about": {
                "message": "<about>"
            },
            "status": "success"
        }
```