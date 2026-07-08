---
title: Verify and attach the Credit Line
excerpt: >-
  API to verify and attach the credit line to a whitelisted WhatsApp Business
  Account (WABA). This endpoint completes the embedded onboarding process by
  verifying the WABA and attaching the necessary credit line for WhatsApp
  Business messaging. This is a critical step that must be performed after
  whitelisting the WABA.
api:
  file: obo-to-embed-flow-1.json
  operationId: get_partner-app-appid-obotoembed-verify
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

| Key           | Value                 | Description                                | Data Types | Require/Optional | Constraints                                                                                           |
| :------------ | :-------------------- | :----------------------------------------- | :--------- | :--------------- | :---------------------------------------------------------------------------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application           | String     | Required         | - Should be a valid Partner App Access Token                                                          |
| appId         | `{{APP_ID}}`            | Id of the app for which callback to be set | String     | Required         | - The ID should be a valid app Id of Gupshup.  - It should belong to the same account as the `apikey` |

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/obotoembed/verify' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
    "message": "Credit line added successfully for WABA id {waba_id}",
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                              | Comments               |
| :---------- | :-------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                       |                        |
| 200         | `{       "message": "Credit line added successfully for WABA id {waba_id}",       "status": "success"   }`            |                        |
| **Error**   |                                                                                                                       |                        |
| 400         | `{       "message": "WABA is not migrated to embed yet , ownership type : ON_BEHALF_OF",       "status": "error"   }` |                        |
| 400         | `{       "status": "error",       "message": "Unable to add credit line for WABA id 349130351627715"   }`             |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                     | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal Server Error"   }`                                                 | For any Internal Error |