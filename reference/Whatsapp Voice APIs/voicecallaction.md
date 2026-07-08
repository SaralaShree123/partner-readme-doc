---
title: Accept/Reject/Terminate Call
excerpt: Use this API to accept/reject/terminate voice calls based on voice events.
api:
  file: partner-portal-api-19.json
  operationId: voiceCallAction
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

| Key           | Description                            | Value                 | Data type | Required/Optional | Constraints                                         |
| :------------ | :------------------------------------- | :-------------------- | :-------- | :---------------- | :-------------------------------------------------- |
| Authorization | Access Token for the application       | `{PARTNER_APP_TOKEN}` | String    | Required          | Should be a valid Partner App Access Token          |
| action        | Action to be taken on an incoming call | `{ACTION}`            | String    | Required          | action is accept/reject/terminate. Mandatory fields |
| call_id       | Call ID in webhook                     | `{CALL_ID}`           | String    | Required          |                                                     |
| sdp           | Session Description Protocol           | `{SDP}`               | String    |                   |                                                     |
| session       | Session Details                        |                       | String    |                   | Mandatory for accept action only                    |

## Sample Request

```curl
curl --location https://partner.gupshup.io/partner/app/&lt;APP_ID&gt;/v1/event' \
--header 'token: &lt;PARTNER_APP_TOKEN&gt;' \
--header 'Content-Type: application/json' \
--data '{
    "type":"voice-event",
    "voice":{
        "messaging_product": "whatsapp",
        "action":"{ACTION}",
        "call_id":"{CALL_ID}",
        "session":{
          "sdp_type":"answer",
          "sdp":"{SDP}"
        }
    }
}'
```

## Sample Response

```json
{
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                           | Comments                          |
| :---------- | :------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Success** |                                                                                                    |                                   |
| 200         | `{       "status": "success"   }`                                                                  |                                   |
| **Error**   |                                                                                                    |                                   |
| 400         | `{       "status": "error",       "message": "Please review the request parameters and retry"   }` | incorrect params                  |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                  | When API key authentication fails |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                  | 10 Requests per Minute            |