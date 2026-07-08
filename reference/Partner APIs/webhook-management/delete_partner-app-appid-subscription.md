---
title: Delete all subscriptions for an app
excerpt: >-
  This API endpoint removes all webhook subscriptions for a partner application.
  This is a bulk operation that deletes every configured webhook at once. Use
  this with extreme caution as it's irreversible and will immediately stop all
  event deliveries to all webhooks. For removing individual subscriptions, use
  the delete specific subscription endpoint instead.
api:
  file: delete-all-subscriptions.json
  operationId: delete_partner-app-appid-subscription
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Value                 | Description                                        | Data Types | Require/Optional | Constraints                                                              |
| :------------ | :-------------------- | :------------------------------------------------- | :--------- | :--------------- | :----------------------------------------------------------------------- |
| Authorization | `{PARTNER_APP_TOKEN}` | Partner app access token issued post partner login | String     | Required         | Should be a valid Partner app access token belonging to the passed appId |
| appId         | `{App_ID}`            | App ID for the app to be deleted                   | String     | Required         | Valid app ID                                                             |

## Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/:appId/subscription' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

## Sample Response

```json

```

## Status Codes

| Status Code | Response                                                              | Comments                                                |
| :---------- | :-------------------------------------------------------------------- | :------------------------------------------------------ |
| **Success** |                                                                       |                                                         |
| 204         |                                                                       | Success when all subscriptions are deleted. No content. |
| **Error**   |                                                                       |                                                         |
| 400         | `{     "status":"error",     "message/data":"&lt;Specific to API&gt;"   }`  | Error with respect to API                               |
| 401         | `{     "status":"error",     "message":"Unauthorized Access"   }`     | When authentication fails                               |
| 403         | `{     "status":"error",     "message":"Unauthorized Access"   }`     | Access is not allowed                                   |
| 429         | `{       "status": "error",       "message": "Too Many Requests"   }` | 5 calls per minute                                      |
| 500         | `{     "status": "error",     "message": "Internal Server Error"   }` | For any Internal Error                                  |