---
title: Text
excerpt: Use this API to send messages using the Text template.
api:
  file: send-message-with-text-template.json
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

| Key           | Description                      | Value                                                                       | Data type | Required/Optional | Constraints                                                                                                                           |
| :------------ | :------------------------------- | :-------------------------------------------------------------------------- | :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Authorization | Access Token for the application | `{PARTNER_APP_TOKEN}`                                                       | String    | Required          | Should be a valid Partner App Access Token                                                                                            |
| source        | Source Phone Number              | `{SOURCE}`                                                                  | Integer   | Required          |                                                                                                                                       |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                  | Boolean   | Optional          |                                                                                                                                       |
| destination   | Destination Phone Number         | `{DESTINATION}`                                                             | Integer   | Required          |                                                                                                                                       |
| template      | Json containing template details | `{     "id":"{{TEMPLAYE_ID}}",     "params":[{{TEMPLATE_PARAMS_LIST}}]   }` | String    | Required          | Must include valid template id                                                                                                        |
| message       | Message Format                   | `{MESSAGE}`                                                                 | String    | Required          | `{     "type": "text",     "text": "\<text_message>"   }`                                                                             |
| src.name      | App Name                         | `{APP_NAME}`                                                                | String    | Required          |                                                                                                                                       |
| appId         | App ID to fetch the access token | `{APP_ID}`                                                                  | String    | Required          | - The ID should be a valid app ID of Gupshup - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

## Sample Request

```curl
curl --request POST \
     --url https://partner.gupshup.io/partner/app/947d28b8-459b-4dfe-9d4c-0ac8c6c245c9/template/msg \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'token: sk_711916ad1d5d4f21a9520fdef20516a1' \
     --data destination=918886912227 \
     --data src.name=august18 \
     --data 'template={"id": "9ff51097-48c9-47c7-a4e4-a9bb5801d8ea", "params": []}' \
     --data 'message={
  "type": "text",
  "text": "<text_message>"
}' \
     --data source=919643874844

```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "ac08ea83-99fa-4d43-a03c-317e4011503c"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{     "status": "submitted",     "messageId": "ac08ea83-99fa-4d43-a03c-317e4011503c"   }`                                                                   |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                            | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support"   }` | For any Internal Error |