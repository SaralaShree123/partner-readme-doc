---
title: Update Partner Capping
excerpt: Use this API to update the Gupshup fee cap for a Gupshup app.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-capping
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

| Parameters    | Value                     | Description                                        |
| :------------ | :------------------------ | :------------------------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application                   |
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App                  |
| cap           | \{\{CAPPING\_VALUE}}      | Capping value. Values supported between: 50 to 750 |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/capping' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'cap={{CAPPING_VALUE}}'
```

### Sample Response

```json
 {
            "status": "success"
        }
        
```
