---
title: Get communication types
excerpt: ''
api:
  file: get-communication-types.json
  operationId: get_partner-users-communications
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

| Key           | Value             | Description                         | Data Types | Require/Optional | Constraints |
| :------------ | :---------------- | :---------------------------------- | :--------- | :--------------- | :---------- |
| Authorization | `{PARTNER_TOKEN}` | JWT Token issued post-partner login | String     | Required         |             |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/users/communications' \
--header 'Authorization:{PARTNER_TOKEN}'
```

## Sample Response

```json
{
    "status": "success",
    "Communication Types": "Marketing & Newsletter, Product & Technical, Financial"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                 | Comments               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                          |                        |
| 200         | `{       "status": "success",       "Communication Types": "Marketing & Newsletter, Product & Technical, Financial"   }`                                 |                        |
| **Error**   |                                                                                                                                                          |                        |
| 401         | `{       "message": "Authentication Failed",       "status": "error"   }`                                                                                |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                        | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error.Please try again later and If Issue still persist then contact Gupshup Dev Support"   }` | For any Internal Error |