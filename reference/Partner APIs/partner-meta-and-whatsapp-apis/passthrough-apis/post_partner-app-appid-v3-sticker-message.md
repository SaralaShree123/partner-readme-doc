---
api:
  file: sticker.json
  operationId: post_partner-app-appid-v3-message
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Sticker messages display animated or static sticker images in a WhatsApp message.

#### [Meta Sticker Message Dock Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/sticker-messages)

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

| Key               | Description                                                 | Values                                   | Data Types | Required/Optional                                                                                  | Constraints                                     |
| :---------------- | :---------------------------------------------------------- | :--------------------------------------- | :--------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| Authorization     | Access Token for the application                            | \{\{PARTNER_APP_TOKEN}}                  | String     | Required                                                                                           | Should be a valid Partner App Access Token.     |
| appId             | App ID to fetch the access token                            | \{\{APP_ID}}                             | String     | Required                                                                                           | The Id should be a valid app Id of Gupshup      |
| messaging_product | Messaging product                                           | whatsapp                                 | String     | Required                                                                                           |                                                 |
| recipient_type    | Recipient type                                              | individual                               | String     | Required                                                                                           |                                                 |
| to                | Destination phone number where the message needs to be sent | 91785876xxxx                             | String     | Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead) | Must be a valid phone number                    |
| recipient         | Destination BSUID where the message needs to be sent        | IN.461449821882xxxx                      | String     | Optional                                                                                           | Must be a valid BSUID                           |
| type              | Messaging type                                              | sticker                                  | String     | Required                                                                                           | Type should be sticker to send sticker message. |
| sticker           | Add sticker body                                            | `"sticker": \{"id" : "798882015472548"}` | Object     | Required                                                                                           | Key should be sticker to send sticker message.  |

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/`{{APP_ID}}`/v3/message' \
--header 'Authorization: `{{PARTNER_APP_TOKEN}}`' \
--header 'Content-Type: application/json' \
--data-raw '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "`{{WHATSAPP_USER_PHONE_NUMBER}}`",
	"recipient": "{{BSUID}}",
  "type": "sticker",
  "sticker": {
    "id" : "`{{MEDIA_ID}}`"
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
| 400         | \{       "message": "Invalid App Details",       "status": "error"   }`                                                                                                                                                                                                                         | If app details are not found                   |
