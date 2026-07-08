---
title: Get MM Lite link on-boarding for live app
excerpt: Use this API to Get MM Lite Onboarding link.
api:
  file: mm-lite-send-message-and-get-link-for-onboarding-live-app-7.json
  operationId: getMmliteLink_1
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

| Key           | Description                      | Value                 | Data Types | Require/Optional | Constraints                                                                                                                            |
| :------------ | :------------------------------- | :-------------------- | :--------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String     | Required         | Should be a valid Partner App Access Token                                                                                             |
| appId         | App ID to fetch the access token | `{{App_ID}}`            | String     | Required         | - The Id should be a valid app Id of Gupshup  - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |
| lang          | language value                   |                       | String     | Optional         | lang=en                                                                                                                                |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/mmlite/link?lang=en' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
    "link": "https://gs.tc.im/mvf6",
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                                     | Comments        |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
| **Success** |                                                                                                                                              |                 |
| 200         | `{       "link": "https://gs.tc.im/mvf6",       "status": "success"   }`                                                                   |                 |
| **Error**   |                                                                                                                                              |                 |
| 400         | `{       "message": "MM lite onboarding is only allowed for live cloud apps",       "status": "error"   }`                                   | App is not live |
| 400         | `{      "status":"error",       "message":"Unauthorised access to the resource. Please review request parameters and headers and retry"   }` |                 |