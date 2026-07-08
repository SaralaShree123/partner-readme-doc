---
title: Optin App User
excerpt: Use this API to set Optin for the app user.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-optin
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

| Parameters    | Value                     | Description                             |
| :------------ | :------------------------ | :-------------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application        |
| APP ID        | \{\{APP\_ID}}             | Unique Identifier for Gupshup App       |
| phone         | 91xxxxxxxxxx              | Phone number of user to get status for. |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/optin' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'phone={{PHONE_NUMBER}}'
```

### Sample Response

```json
  Status code will be - 202  (Accepted)
    Response will be empty as it is async process
```
