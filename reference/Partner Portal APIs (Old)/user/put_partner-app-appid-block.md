---
title: Block User
excerpt: |-
  Use this API to block the user. 
  "Works for On-Prem Only"
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-block
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

| Parameters    | Value                     | Description                       |
| :------------ | :------------------------ | :-------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application  |
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |
| phone         | 91xxxxxxx                 | Phone number                      |
| isBlocked     | true/false                | Block app user                    |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/block' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'phone={{PHONE_NUMBER}}' \
--data-urlencode 'isBlocked=false'
```

### Sample Response

```json
 {
        "status": "success"
    }
```
