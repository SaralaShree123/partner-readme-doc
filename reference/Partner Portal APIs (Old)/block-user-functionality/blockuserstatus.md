---
title: Get User Status
excerpt: Use this API to get user block status.
api:
  file: partner-portal-api-13.json
  operationId: blockUserStatus
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

| Key           | Value             | Description                      | Data Types | Require/Optional | Constraints                              |
| :------------ | :---------------- | :------------------------------- | :--------- | :--------------- | :--------------------------------------- |
| Authorization | `{{PARTNER_TOKEN}}` | Access Token for the application | String     | Required         | - Should be a valid Partner Access Token |
| appId         | `{{App_ID}}`        | App ID to fetch the access token | String     | Required         |                                          |
| PHONE         | Phone number      | `<PHONE>`                          | String     | Required         |                                          |

## Sample Request

```curl
curl --location '<PARNTER_BASE_URL>/partner/app/<APP_ID>/user/<PHONE>' \
--header 'Authorization: <PARNTER_APP_TOKEN>'
```

## Sample Response

```json
{
    "status": "success",
    "user": {
        "phone": "918787656784",
        "blocked": false
    }
}
```

## Status Codes

| Status Code | Response                                                                                                                 | Comments                          |
| :---------- | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Success** |                                                                                                                          |                                   |
| 200         | `{       "status": "success",       "user": {           "phone": "918787656784",           "blocked": false       }   }` |                                   |
| **Error**   |                                                                                                                          |                                   |
| 400         | `{       "status": "error",       "message": "Please review the request parameters and retry"   }`                       | incorrect params                  |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                                        | When API key authentication fails |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                        | 10 Requests per Minute            |