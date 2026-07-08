---
title: Send Order Status Session Message
excerpt: Use this API to send order status session message.
api:
  file: partner-whatsapp-pay-apis-1.json
  operationId: post_partner-app-appid-v3-message
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

| Key           | Value                   | Description                                                                         | Data Types | Require/Optional | Constraints                                                                        |
| :------------ | :---------------------- | :---------------------------------------------------------------------------------- | :--------- | :--------------- | :--------------------------------------------------------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application                                                    | String     | Required         | - Should be a valid Partner App Access Token                                       |
| appId         | `{{APP_ID}}`            | Id of the app                                                                       | String     | Required         | The Id should be a valid app Id of gupshup                                         |
| to            | `{{DESTINATION}}`       | Destination phone no. where the message needs to be sent                            | String     | Required         |                                                                                    |
| type          | `{{TYPE}}`              | type of message                                                                     | String     | Required         | Must be template for order status template message                                 |
| footer        | `{{FOOTER}}`            | message footer                                                                      | String     | Optional         | Footer is optional                                                                 |
| reference_id  | `{{REFERENCE_ID}}`      | Id to update a particular transaction                                               | String     | Required         | An order details must be sent earlier having the same reference id                 |
| status        | `{{STATUS}}`            | Used to update the status of the order details message having the same reference id | String     | Required         | Must be one of processing \| partially_shipped \| shipped \| completed \| canceled |

## Sample Request

```curl
curl --location -g --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "messaging_product": "whatsapp",
    "to": "{{DESTINATION}}",
    "type": "interactive",
    "recipient_type": "individual",
    "interactive": {
        "type": "order_status",
        "body": {
            "text": "your-text-body-content"
        },
        "footer": {
            "text": "your-text-footer-content"
        },
        "action": {
            "name": "review_order",
            "parameters": {
                "reference_id": "{{REFERENCE_ID}}",
                "order": {
                    "status": "{{STATUS}}", 
                    "description": "optional-text"
                }
            }
        }
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

| Status Code | Response                                                                                                                                                                                                                                                                                      | Comments                                       |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                               |                                                |
| 200         | `{ "messages": [ { "id": "GUPSHUP_MESSAGE_ID" } ], "messaging_product": "whatsapp", "contacts": [ { "input": "DESTINATION_PHONE_NO", "wa_id": "DESTINATION_PHONE_NO" } ] }` |                                                |
| **Error**   |                                                                                                                                                                                                                                                                                               |                                                |
| 400         | `{ "message": "Callback Billing must be enabled for this API", "status": "error" }`                                                                                                                                                                                             | if Callback billing is not enabled for the app |
| 400         | `{ "message": "The provided app is not of the expected type for this API. Please ensure that the app is on cloud.", "status": "error" }`                                                                                                                                        | if the app is onPrem app instead of cloud      |
| 400         | `{ "message": "Invalid App Details", "status": "error" }`                                                                                                                                                                                                                       | if app details are not found                   |