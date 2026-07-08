---
api:
  file: product-card-session.json
  operationId: post_partner-app-appid-v3-message
hidden: false
---
<Callout icon="📘" theme="info">
  1. The product carousel message contains a card object. You must add 2 card objects to your message, and can add a maximum of 10. Each card exists in a cards[] array and must be given a "card_index" value of 0 through 9.
  2. The type of each card must be set to "product", and each card must reference the same "catalog_id".
  3. You must add a message body to the message, and no header, footer, or buttons are allowed.
  4. Lastly, each card must specify the product and catalog identifiers "product_retailer_id" and "catalog_id".
  5. Use the `recipient` parameter only when BSUID is enabled for the app.
  6. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.
</Callout>

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
        Values
      </th>

      <th style={{ textAlign: "left" }}>
        Data Type
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
        Headers
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Authorisation
      </td>

      <td style={{ textAlign: "left" }}>
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        sk_8eb35b1f81c24af2xxxxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Path Params
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        App Id
      </td>

      <td style={{ textAlign: "left" }}>
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        bf9ee64c-3d4d-4ac4-xxxx-732e577007c4
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        The Id should be a valid app Id of Gupshup
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Body JSON
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

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
        interactive
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Type should be interactive to send interactive message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        interactive
      </td>

      <td style={{ textAlign: "left" }}>
        interactive message inside body
      </td>

      <td style={{ textAlign: "left" }}>
        ```json

          "interactive": {
              "type": "carousel", // must be carousel
              "body": {
                "text": "<MESSAGE_BODY_TEXT>"
              },
              "action": {
                "cards": [
                  {
                    "card_index": 0,
                    "type": "product",
                    "action": {
                      "product_retailer_id": "abc123xyz",
                      "catalog_id": "123456789"
                    }
                  }
                  // additional product cards
                ]
              }
            
        ```
      </td>

      <td style={{ textAlign: "left" }}>
        Object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Key should be interactive to send text message.
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{app_id}}/v3/message' \
--header 'Authorization: sk_f39ed14bd5exxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "918888xxx",
	"recipient": "IN.4614498218826880",
  "type": "interactive",
  "interactive": {
    "type": "carousel",
    "body": {
      "text": "Check out our latest Adidas products!"
    },
    "action": {
      "cards": [
        {
          "card_index": 0,
          "type": "product",
          "action": {
            "product_retailer_id": "xyli96fcbn",
            "catalog_id": "834584418374992"
          }
        },
        {
          "card_index": 1,
          "type": "product",
          "action": {
            "product_retailer_id": "zqc2qfz5fm",
            "catalog_id": "834584418374992"
          }
        }
      ]
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
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Success
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
        `{ "messages": [ { "id": "GUPSHUP_MESSAGE_ID" } ], "messaging_product": "whatsapp", "contacts": [ { "input": "DESTINATION_PHONE_NO", "wa_id": "DESTINATION_PHONE_NO" } ] }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Error
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `{
                                                                                                        "status": "error",
                                                                                                        "message": "Authentication Failed"
                                                                                                }`
      </td>

      <td>
        When Partner Token authentication fails
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
                                                                                                    "message": "Callback Billing must be enabled for this API",
                                                                                                    "status": "error"
                                                                                                }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
