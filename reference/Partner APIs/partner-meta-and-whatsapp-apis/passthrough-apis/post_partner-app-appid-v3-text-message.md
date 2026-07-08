---
api:
  file: text.json
  operationId: post_partner-app-appid-v3-message
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Text messages are messages containing only a text body and an optional link preview.

#### [Meta Text Message Doc Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/text-messages)

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

| Key               | Description                                                 | Values                               | Data Types | Required/Optional                                                                                  | Constraints                                                         |
| :---------------- | :---------------------------------------------------------- | :----------------------------------- | :--------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Authorization     | Access Token for the application                            | \{\{PARTNER_APP_TOKEN}}              | String     | Required                                                                                           | Should be a valid Partner App Access Token.                         |
| appId             | App ID to fetch the access token                            | \{\{APP_ID}}                         | String     | Required                                                                                           | The Id should be a valid app Id of Gupshup                          |
| messaging_product | Messaging product                                           | whatsapp                             | String     | Required                                                                                           |                                                                     |
| recipient_type    | Recipient type                                              | individual                           | String     | Required                                                                                           |                                                                     |
| to                | Destination phone number where the message needs to be sent | 91785876xxxx                         | String     | Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead) | Must be a valid phone number                                        |
| recipient         | Destination BSUID where the message needs to be sent        | IN.461449821882xxxx                  | String     | Optional                                                                                           | Must be a valid BSUID                                               |
| type              | Messaging type                                              | text                                 | String     | Required                                                                                           | Type should be `text` to send text message.                         |
| text              | Text message inside body                                    | `"text": \{"body": "Hii meta test"}` | Object     | Required                                                                                           | Key should be `text` to send text message. Maximum 4096 characters. |

## Sample Request

Without Context

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "{{WHATSAPP_USER_PHONE_NUMBER}}",
	"recipient": "{{BSUID}}",
  "type": "text",
  "text": {
    "body": "{{TEXT_BODY}}"
  }
}'
```

With Context

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "{{WHATSAPP_USER_PHONE_NUMBER}}",
  "type": "text",
  "context": {
    "message_id": "{{PREVIOUS_MESSAGE_ID}}"
  },
  "text": {
    "body": "{{TEXT_BODY}}",
    "preview_url": true
  }
}'
```

## Sample Response

```json
{
    "messages": [
        {
            "id": "GUPSHUP_MESSAGE_ID"
        }
    ],
    "messaging_product": "whatsapp",
    "contacts": [
        {
            "input": "DESTINATION_PHONE_NO",
            "wa_id": "DESTINATION_PHONE_NO"
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                        | Comments                                       |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                 |                                                |
| 200         | \{       "messages": [           \{               "id": "GUPSHUP_MESSAGE_ID"           }       ],       "messaging_product": "whatsapp",       "contacts": [           \{               "input": "DESTINATION_PHONE_NO",               "wa_id": "DESTINATION_PHONE_NO"           }       ]   }` |                                                |
| **Error**   |                                                                                                                                                                                                                                                                                                 |                                                |
| 401         | \{           "status": "error",           "message": "Authentication Failed"   }`                                                                                                                                                                                                               | When API key authentication fails              |
| 400         | \{       "message": "Callback Billing must be enabled for this API",       "status": "error"   }`                                                                                                                                                                                               | If Callback billing is not enabled for the app |
| 400         | \{       "message": "Invalid App Details",       "status": "error"   }`                                                                                                                                                                                                                         | If app details are not found.                  |

<br />
