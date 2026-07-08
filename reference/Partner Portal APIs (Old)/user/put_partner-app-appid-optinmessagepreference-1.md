---
title: Update Optin Message Preference
excerpt: Use this API to enable/disable the optin message preference.
api:
  file: partner-portal-public-apis-1.json
  operationId: put_partner-app-appid-optinmessagepreference
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Parameters         | Value                     | Description                                               |
| :----------------- | :------------------------ | :-------------------------------------------------------- |
| Authorization      | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application                          |
| appId              | \{\{APP\_ID}}             | Unique Identifier for Gupshup App                         |
| enableOptinMessage | False                     | Enable the Gupshup's automated opt-in message for an app  |
| enableOptinMessage | True                      | Disable the Gupshup's automated opt-in message for an app |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/optinMessagePreference' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'enableOptinMessage=true'
```

### Sample Response

```json
 {
       Status: 202 Accepted

    }
```
