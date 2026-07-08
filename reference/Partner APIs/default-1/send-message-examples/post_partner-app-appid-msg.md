---
title: Location
excerpt: Use this API to send messages with the Location template.
api:
  file: send-message-with-location-template.json
  operationId: post_partner-app-appid-msg
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

| Key           | Description                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Data type | Required/Optional | Constraints                                                                                                                             |
| :------------ | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                                                                                                                                                                                                                                                                                                                                                                                | String    | Required          | Should be a valid Partner App Access Token                                                                                              |
| src           | Source Phone Number              | `{{SOURCE}}`                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer   | Required          |                                                                                                                                         |
| sandbox       | Boolean value                    | `{SANDBOX}`                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean   | Optional          |                                                                                                                                         |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer   | Required          |                                                                                                                                         |
| message       | Message Json                     | `{           "recipient_type": "individual",           "preview_url": false,           "to": "919970754444",           "type": "location",           "location":{                 "name":"R. 7 de Abril - República",                 "address":"São Paulo - SP, Brazil",              "longitude":-46.6444751,"latitude":-23.5463588           },   "caption":"The location for the event is Hadapsar,Pune",           "channel": "whatsapp"       }` | String    | Required          |                                                                                                                                         |
| APP_ID        | App ID to fetch the access token | `{{APP_ID}}`                                                                                                                                                                                                                                                                                                                                                                                                                                           | String    | Required          | - The Id should be a valid app Id of Gupshup. - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used. |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/template/msg' \
--header 'Connection: keep-alive' \
--header 'Authorization: sk_8eb35b1f81c24af293a405164a392f30' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'source=917835039205' \
--data-urlencode 'sandbox=false' \
--data-urlencode 'destination=919970754444' \
--data-urlencode 'template={"id": "f7163aa4-b0fa-4a4e-8478-13d75e08ed4a","params": []}' \
--data-urlencode 'src.name=PartnerPortal' \
--data-urlencode 'message={"type":"LOCATION","LOCATION":{\"example\":\"The place for the event is kothrud,Pune\"}}'	
```

## Sample Response

```json
{
    "status": "submitted",
    "messageId": "d255d161-2d9e-455a-8776-9f64d0291e36"
}	
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{       "status": "submitted",       "messageId": "d255d161-2d9e-455a-8776-9f64d0291e36"   }`                                                               |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                            | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support"   }` | For any Internal Error |