---
title: Delete Pre-filled Data
excerpt: Use this API to Delete pre-filled data for an app.
api:
  file: partner-prefillied-data.json
  operationId: delete_partner-app-appid-onboarding-embed-prefilled
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

| Key           | Values                | Description                      | Data types | Required/Optional | Constraints                                |
| :------------ | :-------------------- | :------------------------------- | :--------- | :---------------- | :----------------------------------------- |
| Authorization | `{PARTNER_APP_TOKEN}` | Access Token for the application | String     | Required          | Should be a valid Partner App Access Token |
| appId         | `{APP_ID}`            | App ID to fetch the access token | String     | Required          | The Id should be a valid app Id of Gupshup |

## Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{APP_ID}/onboarding/embed/prefilled' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

## Sample Response

```json

```

## Status Codes

| Status Code | Response                                                                  | Comments |
| :---------- | :------------------------------------------------------------------------ | :------- |
| **Success** |                                                                           |          |
| 202         | 1                                                                         |          |
| **Error**   |                                                                           |          |
| 401         | `{ "message": "Authentication Failed", "status": "error" }`               |          |