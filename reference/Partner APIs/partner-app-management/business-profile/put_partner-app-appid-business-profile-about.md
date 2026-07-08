---
title: Update Profile About
excerpt: >-
  Updates the 'About' text (business description) in the WhatsApp Business
  profile. The about text provides a brief introduction to your business (max
  512 characters). This is a simplified endpoint that updates only the
  description text, completely replacing the existing text.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-business-profile-about
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
| about         | \{\{ABOUT}}               | Business profile about            |
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/about' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'about={{ABOUT}}'
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