---
title: Delete Profile Picture
excerpt: Use this API to remove the profile picture set for a business profile.
api:
  file: partner-portal-public-apis.json
  operationId: delete_partner-app-appid-business-profile-photo
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ This  endpoint isn't supported for CAPI PNs.

### Parameters

| Parameters    | Value                     | Description                       |
| :------------ | :------------------------ | :-------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application  |
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/photo' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
            "message": "profile photo deleted successfully",
            "status": "success"
        }
```
