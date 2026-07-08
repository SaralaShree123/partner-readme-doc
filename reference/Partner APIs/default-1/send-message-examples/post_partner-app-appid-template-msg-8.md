---
title: Carousel (Image)
excerpt: Use this API to send messages with the Carousel template (Image).
api:
  file: carousel-send-message.json
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

| Key           | Description                      | Value                                                                                                                                                                           | Data type | Required/Optional | Constraints                                                                                                                           |
| :------------ | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                                                                                                           | String    | Required          | Should be a valid Partner App Access Token                                                                                            |
| source        | Source Phone Number              | `{{SOURCE}}`                                                                                                                                                                      | Integer   | Required          |                                                                                                                                       |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                                                                                                                     | Boolean   | Optional          |                                                                                                                                       |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                                                                                                                 | Integer   | Required          |                                                                                                                                       |
| template      | Json containing template details | `{     "id": "\<template_id>",     "params": [      \<list_of_template_parameters>     ]}`                                                                                      | String    | Required          |                                                                                                                                       |
| message       | Message Json                     | `{     "type": "carousel",     "cardHeaderType": "<IMAGE>",     "cards": [       {         "id": "<image_id>"       },       {         "link": "<image_url>"       }     ]   }` | String    | Required          | For the carousel, the message json will contain each card’s media (represented by either ID/link)                                     |
| src.name      | App Name                         | `{{APP_NAME}}`                                                                                                                                                                    | String    | Required          |                                                                                                                                       |
| APP_ID        | App ID to fetch the access token |                                                                                                                                                                                 | String    | Required          | - The Id should be a valid app Id of Gupshup - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

## Sample Request

```curl
curl --request POST \
     --url https://partner.gupshup.io/partner/app/947d28b8-459b-4dfe-9d4c-0ac8c6c245c9/template/msg \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'token: sk_711916ad1d5d4f21a9520fdef20516a1' \
     --data source=919643874844 \
     --data sandbox=true \
     --data destination=918886912227 \
     --data 'template={"id":"5d856a59-2990-4197-a502-8af90bfac11a","params":["user"]}' \
     --data src.name=ProdMonitoringCloud \
     --data 'message={"type":"carousel","cardHeaderType":"IMAGE","cards":[{"link":"https://fastly.picsum.photos/id/13/2500/1667.jpg?hmac=SoX9UoHhN8HyklRA4A3vcCWJMVtiBXUg0W4ljWTor7s"},{"link":"https://fastly.picsum.photos/id/25/5000/3333.jpg?hmac=yCz9LeSs-i72Ru0YvvpsoECnCTxZjzGde805gWrAHkM"},{"link":"https://fastly.picsum.photos/id/28/4928/3264.jpg?hmac=GnYF-RnBUg44PFfU5pcw_Qs0ReOyStdnZ8MtQWJqTfA"},{"link":"https://fastly.picsum.photos/id/27/3264/1836.jpg?hmac=p3BVIgKKQpHhfGRRCbsi2MCAzw8mWBCayBsKxxtWO8g"}]}'
```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "76581256-df63-4823-b03d-e7c5d169f934"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{     "status": "submitted",     "messageId": "76581256-df63-4823-b03d-e7c5d169f934"   }`                                                                   |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                            | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support"   }` | For any Internal Error |