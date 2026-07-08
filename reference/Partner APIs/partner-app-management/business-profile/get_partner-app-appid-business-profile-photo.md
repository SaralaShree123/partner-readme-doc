---
title: Get Profile Picture
excerpt: >-
  This API endpoint retrieves the URL of the business profile photo for a
  specific partner application's WhatsApp Business profile. The profile photo is
  the visual representation of your business that appears to users when they
  view your WhatsApp Business profile. This endpoint returns the photo URL which
  can be used to display or download the current profile photo.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-business-profile-photo
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
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/photo' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
            "message": "<link>",
            "status": "success"
        }
```