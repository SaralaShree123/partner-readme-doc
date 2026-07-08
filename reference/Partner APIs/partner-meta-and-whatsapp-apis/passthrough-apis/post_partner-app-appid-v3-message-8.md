---
api:
  file: Pix_send_session_msg.json
  operationId: post_partner-app-appid-v3-message
hidden: true
---
<br />

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER_APP_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{APP_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        The Id should be a valid app Id of Gupshup.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        messaging_product
      </td>

      <td style={{ textAlign: "left" }}>
        Messaging product
      </td>

      <td style={{ textAlign: "left" }}>
        whatsapp
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        recipient_type
      </td>

      <td style={{ textAlign: "left" }}>
        Recipient type
      </td>

      <td style={{ textAlign: "left" }}>
        individual
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        to
      </td>

      <td style={{ textAlign: "left" }}>
        Destination phone number where the message needs to be sent
      </td>

      <td style={{ textAlign: "left" }}>
        91785876xxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead)
      </td>

      <td style={{ textAlign: "left" }}>
        Must be a valid phone number
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        recipient
      </td>

      <td style={{ textAlign: "left" }}>
        Destination BSUID where the message needs to be sent
      </td>

      <td style={{ textAlign: "left" }}>
        IN.461449821882xxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Must be a valid BSUID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        type
      </td>

      <td style={{ textAlign: "left" }}>
        Messaging type
      </td>

      <td style={{ textAlign: "left" }}>
        text
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Type should be interactive to send

        interactive message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        interactive
      </td>

      <td style={{ textAlign: "left" }}>
        Add interactive

        body
      </td>

      <td style={{ textAlign: "left" }}>
        "interactive": \{\<Interactive body>}
      </td>

      <td style={{ textAlign: "left" }}>
        object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Key should be a interactive to send interactive message.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
 "messaging_product": "whatsapp",
 "recipient_type": "individual",
 "to": {{destinationNumber}},
"recipient": "{{BSUID}}",
 "type": "interactive",
 "interactive": {
   "type": "order_details",
   "body": {
     "text": "Your message content"
   },
   "action": {
     "name": "review_and_pay",
     "parameters": {
       "reference_id": "987654333",
       "type": "digital-goods",
       "payment_type": "br",
       "payment_settings": [
         {
           "type": "pix_dynamic_code",
           "pix_dynamic_code": {
             "code": "00020101021226.gov.bcb.pix.example.com...",
             "merchant_name": "Account holder name",
             "key": "39580525000189",
             "key_type": "CNPJ"
           }
         }
       ],
       "currency": "BRL",
       "total_amount": {
         "value": 50000,
         "offset": 100
       },
       "order": {
         "status": "pending",
         "tax": {
           "value": 0,
           "offset": 100,
           "description": "optional text"
           },
         "items": [
           {
             "retailer_id": "1234567",
             "name": "Cake",
             "amount": {
               "value": 50000,
               "offset": 100
             },
             "quantity": 1
           }
         ],
         "subtotal": {
           "value": 50000,
           "offset": 100
         }
       }
     }
   }
 }
}'
```

## Sample Response

```json
{
	"messages": 
	[
		{
			"id": "GUPSHUP_MESSAGE_ID"
		}
	],
	"messaging_product": "whatsapp",
	"contacts": 
	[
		{
			"input": "DESTINATION_PHONE_NO",
			"wa_id": "DESTINATION_PHONE_NO"
		}
	]
}
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
      </th>

      <th>
        Response
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{

        "messages":[\{"id": "GUPSHUP_MESSAGE_ID"
        }
        ],
        "messaging_product": "whatsapp",
        "contacts":
        [
        \{
        "input": "DESTINATION_PHONE_NO",
        "wa_id": "DESTINATION_PHONE_NO"
        }
        ]
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "message": "Callback Billing must be enabled for this API",\  
        "status": "error"}
      </td>

      <td>
        if Callback billing is not enabled for the app
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{  
        "message": "Invalid App Details", "status": "error"}
      </td>

      <td>
        if app details are not found
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{

        "status": "error",  
        "message": "Authentication Failed"}
      </td>

      <td>
        When API key authentication fails
      </td>
    </tr>
  </tbody>
</Table>
