---
title: Block/ Unblock User
excerpt: Use this API to enable/disable block user at partner level.
api:
  file: partner-portal-api-11.json
  operationId: updateBlockUserPartnerConfig
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Value               | Description                          | Data Types | Require/Optional | Constraints                                  |
| :------------ | :------------------ | :----------------------------------- | :--------- | :--------------- | :------------------------------------------- |
| Authorization | `{PARTNER_TOKEN}`   | Access Token for the application     | String     | Required         | Should be a valid Partner Access Token       |
| blockEnabled  | `{BLOCKED_ENABLED}` | To enable pass true else pass false. | Boolean    | Required         | blockEnabled is true/false. Mandatory fields |

## Sample Request

```curl
curl --location --request PUT '<PARNTER_BASE_URL>/partner/account/config/block/user' \
--header 'Authorization: {PARTNER_TOKEN}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'blockEnabled={BLOCKED_ENABLED}'
```

## Sample Response

```json
{
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                           | Comments                          |
| :---------- | :------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Success** |                                                                                                    |                                   |
| 200         | `{       "status": "success"   }`                                                                  |                                   |
| **Error**   |                                                                                                    |                                   |
| 400         | `{       "status": "error",       "message": "Please review the request parameters and retry"   }` | incorrect params                  |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                  | When API key authentication fails |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                  | 10 Requests per Minute            |