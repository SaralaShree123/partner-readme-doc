---
title: Product card carousel templates
deprecated: false
hidden: true
metadata:
  robots: index
---
Product Card Carousel templates allow sending a text message with up to 10 product cards in a horizontally scrollable carousel. When users tap View, they can see product details, add items to the cart, and place orders directly within WhatsApp.

Request Parameters

<br />

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
        APP ID
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
        Body Json
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
        Destination phone no where the message need to be send
      </td>

      <td style={{ textAlign: "left" }}>
        91785876xxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Must be a valid phone number.
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
        Type should be template to
        send template message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        template
      </td>

      <td style={{ textAlign: "left" }}>
        Template message inside body
      </td>

      <td style={{ textAlign: "left" }}>
        ```text
        "template": {
            "name": "Template"
            ......
          }
        ```
      </td>

      <td style={{ textAlign: "left" }}>
        object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Key should be template to send template message.
      </td>
    </tr>
  </tbody>
</Table>

```curl
curl --location 'https://partner.gupshup.io/partner/app/<APP_ID>/v3/message' \
--header 'Authorization: <PARTNER_APP_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "<WHATSAPP_USER_PHONE_NUMBER>",
  "type": "template",
  "template": {
    "name": "<TEMPLATE_NAME>",
    "language": {
      "code": "<TEMPLATE_LANGUAGE>"
    },
    "components": [
      {
        "type": "body",
        "parameters": [
          <MESSAGE_BODY_TEXT_VARIABLE>,
          <MESSAGE_BODY_TEXT_VARIABLE>
        ]
      },
      {
        "type": "carousel",
        "cards": [
          {
            "card_index": <CARD_INDEX>,
            "components": [
              {
                "type": "header",
                "parameters": [
                  {
                    "type": "product",
                    "product": {
                      "product_retailer_id": "<PRODUCT_ID>",
                      "catalog_id": "<CATALOG_ID>"
                    }
                  }
                ]
              }
            ]
          }

          /* Addt'l cards would follow. */

        ]
      }
    ]
  }
}'
```

<br />

Status codes

<br />

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
        ```text
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
        401
      </td>

      <td>
        `{
                                                                                "status": "error",
                                                                                "message": "Authentication Failed"
                                                                        }`
      </td>

      <td>
        When API key authentication fails
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
        if Callback billing is not enabled for the app
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
                                                                            "message": "Invalid App Details",
                                                                            "status": "error"
                                                                        }`
      </td>

      <td>
        if app details are not found
      </td>
    </tr>
  </tbody>
</Table>