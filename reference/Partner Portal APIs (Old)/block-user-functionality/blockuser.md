---
title: Block User
excerpt: Use this API to block/unblock user.
api:
  file: partner-portal-api-14.json
  operationId: blockUser
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

| Key           | Description                         | Value               | Data Types | Require/Optional | Constraints                                  |
| :------------ | :---------------------------------- | :------------------ | :--------- | :--------------- | :------------------------------------------- |
| Authorization | Access Token for the application    | `{PARTNER_TOKEN}`   | String     | Required         | - Should be a valid Partner Access Token     |
| blockEnabled  | To enable pass true else pass false | `{BLOCKED_ENABLED}` | Boolean    | Required         | blockEnabled is true/false. Mandatory fields |

## Sample Request

```curl
curl --location '<PARNTER_BASE_URL>/partner/app/{APP_ID}/user/block' \
--header 'Authorization: {PARTNER_APP_TOKEN}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'phone={PHONE}' \
--data-urlencode 'isBlocked=true/false'
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