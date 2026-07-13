---
title: Link App with Partner
excerpt: >-
  This API endpoint lets authenticated partners link a Gupshup application to
  their account using an API key and app name. 
api:
  file: partner-portal-public-apis.json
  operationId: post_partner-account-api-applink
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---

Link an existing Gupshup application to your partner account with an API key and app name. After linking, you can manage the app through Partner APIs.

<Callout icon="📘" theme="info">
  Additional Check: Partner must have MFA (Multi-Factor Authentication) enabled
</Callout>

### Parameters

| Parameters    | Value               | Description                         |
| :------------ | :------------------ | :---------------------------------- |
| Authorization | \{\{PARTNER_TOKEN}} | JWT Token issued post Partner login |
| apiKey        | \{\{API_KEY}}       | API key for the app                 |
| appName       | \{\{APP_NAME}}      | Unique Identifier for Gupshup App   |

### Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/account/api/appLink' \
--header 'Authorization: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'apiKey={{API_KEY}}' \
--data-urlencode 'appName={{APP_NAME}}'
```

### Sample Response

```json
{
        "partnerApps": {
            "createdOn": 1609829592910,
            "healthy": false,
            "id": "fa*b***e-d2**-****-be38-0****d*9a**b",
            "live": false,
            "modifiedOn": 1614162854108,
            "name": "assistant0092",
            "partnerId": 1,
            "phone": "91**********",
            "stopped": false,
            "walletId": "1**"
        }
    }
```

<br />
