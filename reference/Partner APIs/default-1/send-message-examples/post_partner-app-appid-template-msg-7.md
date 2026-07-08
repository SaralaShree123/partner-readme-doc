---
title: Carousel (Video)
excerpt: Use this API to send messages with the Carousel template (Video).
api:
  file: carousel-send-messagevideo.json
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

| Key           | Description                      | Value                                                                                                                                                                          | Data type | Required/Optional | Constraints                                                                                                                            |
| :------------ | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                                                                                                          | String    | Required          | Should be a valid Partner App Access Token                                                                                             |
| source        | Source Phone Number              | `{{SOURCE}}`                                                                                                                                                                     | Integer   | Required          |                                                                                                                                        |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                                                                                                                    | Boolean   | Optional          |                                                                                                                                        |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                                                                                                                | Integer   | Required          |                                                                                                                                        |
| template      | Json containing template details | `{ "id": "<template_id>", "params": [ <list_of_template_parameters> ] }`                                                                                                       | String    | Required          |                                                                                                                                        |
| message       | Message                          | `{ "type": "carousel", "cardHeaderType": "<VIDEO>", "cards": [ { "id": "<video_id>" }, { "link": "<video_url>" } ] }`                                                          |           |                   | For the carousel, the message json will contain each card’s media (represented by either ID/link)                                      |
| src.name      | App Name                         | `{{APP_NAME}}`                                                                                                                                                                  | String    | Required          |                                                                                                                                        |
| APP_ID        | App ID to fetch the access token | `{{APP_ID}}`                                                                                                                                                                     | String    | Required          | - The ID should be a valid app ID of Gupshup  - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

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
     --data 'message={"type":"carousel","cardHeaderType":"VIDEO","cards":[{"id" : "359320036695489"}]}'
```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "4f562b18-4ebe-4bb7-bf90-11b0d1c1d77f"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{ "status": "submitted", "messageId": "4f562b18-4ebe-4bb7-bf90-11b0d1c1d77f" }`                                                                             |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{ "status": "error", "message": "Too Many Requests" }`                                                                                                      | 10 Requests per Minute |
| 500         | `{ "status": "error", "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support" }`            | For any Internal Error |