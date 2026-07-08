---
title: Catalog
excerpt: Use this API to send messages with a Catalog template.
api:
  file: send-message-with-catalog-template.json
  operationId: post_partner-app-appid-template-msg
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

| Key           | Description                      | Value                                                                                     | Data type | Required/Optional | Constraints                                                                                                                             |
| :------------ | :------------------------------- | :---------------------------------------------------------------------------------------- | :-------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                     | String    | Required          | Should be a valid Partner App Access Token                                                                                              |
| source        | Source Phone Number              | `{{SOURCE}}`                                                                                | Integer   | Required          |                                                                                                                                         |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                               | Boolean   | Optional          |                                                                                                                                         |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                           | Integer   | Required          |                                                                                                                                         |
| template      | Json containing template details | `{ "id": "\<template_id>", "params": [ <list_of_template_parameters> ] }`                  | String    | Required          |                                                                                                                                         |
| src.name      | App Name                         | `{{APP_NAME}}`                                                                              | String    | Required          |                                                                                                                                         |
| channel       | Channel name                     | `{{CHANNEL_NAME}}`                                                                          | String    | Required          | Must be `whatsapp`                                                                                                                      |
| APP_ID        | App ID to fetch the access token |                                                                                           | String    | Required          | - The ID should be a valid app ID of Gupshup. - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used. |

## Sample Request

```curl
curl --request POST \
     --url https://partner.gupshup.io/partner/app/947d28b8-459b-4dfe-9d4c-0ac8c6c245c9/template/msg \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'token: sk_711916ad1d5d4f21a9520fdef20516a1' \
     --data source=919643874844 \
     --data destination=918886912227 \
     --data sandbox=true \
     --data src.name=ProdMonitoringCloud \
     --data 'template={
	"id": "8985923d-682d-4bb7-b037-66b61c8c7877",
	"params": ["a2py9opgpp"]
}' \
     --data channel=whatsapp
```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "ab1e8d9f-4ebf-4f9a-a32f-78396d44e7c4"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{ "status": "submitted", "messageId": "ab1e8d9f-4ebf-4f9a-a32f-78396d44e7c4" }`                                                                             |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{ "status": "error", "message": "Too Many Requests" }`                                                                                                      | 10 Requests per Minute |
| 500         | `{ "status": "error", "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support" }`           | For any Internal Error |