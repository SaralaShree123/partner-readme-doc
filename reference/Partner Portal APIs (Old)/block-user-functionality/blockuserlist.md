---
title: Get Block User List
excerpt: Use this API to get user block status list.
api:
  file: partner-portal-api-12.json
  operationId: blockUserList
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

| Key           | Value                 | Description                      | Data Types | Require/Optional | Constraints                                |
| :------------ | :-------------------- | :------------------------------- | :--------- | :--------------- | :----------------------------------------- |
| Authorization | `<PARTNER_APP_TOKEN>` | Access Token for the application | String     | Required         | Should be a valid Partner App Access Token |
| Page          | `<PAGE_NO>`           | Page                             | Integer    | Required         |                                            |
| Page Size     | `<PAGE_SIZE>`         | Page Size                        | Integer    | Required         |                                            |

## Sample Request

```curl
curl --location '<PARNTER_BASE_URL>/partner/app/<APP_ID>/user/list?pageNo=<PAGE_NO>&pageSize=<PAGE_SIZE>' \
--header 'Authorization: <PARNTER_APP_TOKEN>'
```

## Sample Response

```json
{
    "status": "success",
    "users": [
        {
            "phone": "918787656783",
            "blocked": true
        },
        {
            "phone": "918787656786",
            "blocked": true
        },
        {
            "phone": "918787656787",
            "blocked": true
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                             | Comments                          |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                      |                                   |
| 200         | `{       "status": "success",       "users": [           {               "phone": "918787656783",               "blocked": true           },           {               "phone": "918787656786",               "blocked": true           },           {               "phone": "918787656787",               "blocked": true           }       ]   }` |                                   |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                      |                                   |
| 400         | `{       "status": "error",       "message": "Please review the request parameters and retry"   }`                                                                                                                                                                                                                                                   | incorrect params                  |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                                                                                                                                                                                                                                                                    | When API key authentication fails |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                    | 10 Requests per Minute            |