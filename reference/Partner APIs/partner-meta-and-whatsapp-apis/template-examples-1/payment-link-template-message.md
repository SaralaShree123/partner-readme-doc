---
title: Payment Link Template Message
excerpt: Use this API to send a payment link template message to a WhatsApp user.
deprecated: false
hidden: false
metadata:
  robots: index
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
        Destination phone no where the message need to be send
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
        template
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
        template
      </td>

      <td style={{ textAlign: "left" }}>
        Add template body
      </td>

      <td style={{ textAlign: "left" }}>
        template: \{\<body>}
      </td>

      <td style={{ textAlign: "left" }}>
        object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Key should be a template to send interactive message.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/dbb0afed-9377-4f82-bd28-77e419c818c9/v3/message' \
--header 'Authorization: sk_c33e12d15ab84e16baab042d8ffd468a' \
--header 'Content-Type: application/json' \
--data '{
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "5511972932562",
		"recipient": "IN.4614498218826880",
    "type": "template",
    "template": {
        "name": "boleto_and_payment_link_order_detail_template_aug_6_2025_test",
        "language": {
            "policy": "deterministic",
            "code": "en"
        },
        "components": [
            {
                "type": "body",
                "parameters": []
            },
            {
                "type": "button",
                "sub_type": "order_details",
                "index": 0,
                "parameters": [
                    {
                        "type": "action",
                        "action": {
                            "order_details": {
                                "currency": "BRL",
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
                                                "value": 100,
                                                "offset": 100
                                            },
                                            "quantity": 1
                                        }
                                    ],
                                    "subtotal": {
                                        "value": 100,
                                        "offset": 100
                                    }
                                },
                                "total_amount": {
                                    "value": 100,
                                    "offset": 100
                                },
                                "reference_id": "reference-id-76126787",
                                "type": "digital-goods",
                                "payment_type": "br",
                                "payment_settings": [
                                    {
                                        "type": "payment_link",
                                        "payment_link": {
                                            "uri": "https://my-payment-link-url"
                                        }
                                    }
                                ]
                            }
                        }
                    }
                ]
            }
        ]
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

        "messages":[\{"id": "GUPSHUP_MESSAGE_ID"}],"messaging_product": "whatsapp",        "contacts":        [        \{        "input": "DESTINATION_PHONE_NO",        "wa_id": "DESTINATION_PHONE_NO"        }        ]        }
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

        "message": "Callback Billing must be enabled for this API","status": "error"}
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

        "message": "Invalid App Details","status": "error"}
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
