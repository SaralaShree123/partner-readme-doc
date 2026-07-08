---
title: Whitelist the WABA ID
excerpt: >-
  API to whitelist WhatsApp Business Account (WABA) ID for embedded onboarding
  flow. This endpoint enables partners to whitelist their WABA for the embedded
  onboarding solution, which is required before attaching credit lines and
  completing the WhatsApp onboarding process.
api:
  file: obo-to-embed-flow-1.json
  operationId: post_partner-app-appid-obotoembed-whitelist
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

| Key           | Value                 | Description                                | Data Types | Require/Optional | Constraints                                                                                        |
| :------------ | :-------------------- | :----------------------------------------- | :--------- | :--------------- | :------------------------------------------------------------------------------------------------- |
| Authorization | `{PARTNER_APP_TOKEN}` | Access Token for the application           | String     | Required         | - Should be a valid Partner App Access Token                                                       |
| appId         | `{APP_ID}`            | Id of the app for which callback to be set | String     | Required         | - The ID should be a valid appId of Gupshup.  - It should belong to the same account as the apikey |

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{APP_ID}/obotoembed/whitelist' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

## Sample Response

```json
{
    "embedSignupUrl": "https://gs.tc.im/kZviNa8Zlx9",
    "id": "1016427996774921",
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                    | Comments               |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                             |                        |
| 200         | `{ "embedSignupUrl": "https://gs.tc.im/kZviNa8Zlx9", "id": "1016427996774921", "status": "success" }`                       |                        |
| **Error**   |                                                                                                                             |                        |
| 400         | `{ "message": "Error while whitelisting WABA.", "status": "error" }`                                                        |                        |
| 429         | `{ "status": "error", "message": "Too Many Requests" }`                                                                     | 10 Requests per Minute |
| 500         | `{ "status": "error", "message": "Internal Server Error" }`                                                                 | For any Internal Error |