---
title: Delete Non-Admin Partner User
excerpt: Use this API to delete the partner user.
api:
  file: user-managemnet-apis.json
  operationId: delete_partner-users-userid
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

| Key           | Description                         | Value             | Data Type | Required/Optional | Constraints                             |
| :------------ | :---------------------------------- | :---------------- | :-------- | :---------------- | :-------------------------------------- |
| Authorization | JWT Token issues post Partner login | `{PARTNER_TOKEN}` | String    | Required          | It should be a valid Partner JWT Token. |
| userId        | User ID of the user                 | `{USER_ID}`       | Integer   | Required          |                                         |

## Sample Request

```curl
curl --location --request DELETE 'http://{BASE_URL}/partner/users/{USERID}' \
--header 'Authorization: {PARTNER_TOKEN}'
```

## Sample Response

```json
{
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                  | Comments                           |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------- |
| **Success** |                                                                                                                                                           |                                    |
| 200         | `{       "status": "success"   }`                                                                                                                         | When the user deleted successfully |
| **Error**   |                                                                                                                                                           |                                    |
| 400         | `{       "status": "error",       "message": "Cannot delete an admin user"   }`                                                                           |                                    |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                         | 10 Requests per Minute             |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"   }` | For any Internal Error             |