---
title: Update Profile Picture
excerpt: >-
  This API endpoint uploads or updates the business profile photo for a specific
  partner application's WhatsApp Business profile. The profile photo is the
  visual representation of your business that appears to users when they view
  your WhatsApp Business profile. This endpoint accepts an image file and sets
  it as the new profile photo, replacing any existing photo.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-business-profile-photo
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
| appID         | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |
| image         | \{\{FILE\_PATH}}          | Profile photo image file          |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile/photo' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'image=@"/path/to/file"'
```

### Sample Response

```json
{
            "message": "profile picture updated successfully",
            "status": "success"
        }
```