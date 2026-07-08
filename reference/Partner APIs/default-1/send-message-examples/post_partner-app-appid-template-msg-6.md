---
title: Limited Time Offer (LTO)
excerpt: Use this API to send messages with the LTO  template.
api:
  file: lto-send-message.json
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

| Key           | Description                      | Value                                                                                                                                                     | Data type | Required/Optional | Constraints                                                                                                                            |
| :------------ | :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                                                                                   | String    | Required          | Should be a valid Partner App Access Token                                                                                             |
| source        | Source Phone Number              | `{{SOURCE}}`                                                                                                                                              | Integer   | Required          |                                                                                                                                        |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                                                                                               | Boolean   | Optional          |                                                                                                                                        |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                                                                                         | Integer   | Required          |                                                                                                                                        |
| template      | Json containing template details | `{     "id":"{{templateId}}",     "params":[ <list_of_template_parameters>],     "expiration":{{expiration_time_in_UNIX_timestamp_in_milliseconds.}}   }` | String    | Required          | - Must include valid template id - Expiration must be provided for LTO templates created where has_expiration is true                  |
| src.name      | App Name                         | `{{APP_NAME}}`                                                                                                                                            | String    | Required          |                                                                                                                                        |
| APP_ID        | App ID to fetch the access token | `{{APP_ID}}`                                                                                                                                              | String    | Required          | - The ID should be a valid app Id of Gupshup  - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

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
     --data 'template={"id":"5fcb3ffb-3dae-4d46-9836-55b0cc509dd1","params":["250FF"],"expiration":1714694865000}' \
     --data src.name=ProdMonitoringCloud
```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "3a4c8b42-d0ce-4607-836a-eb18a2838a88"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{     "status": "submitted",     "messageId": "3a4c8b42-d0ce-4607-836a-eb18a2838a88"   }`                                                                   |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                            | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support"   }` | For any Internal Error |