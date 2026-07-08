---
api:
  file: media-card-carousel-session.json
  operationId: post_partner-app-appid-v3-message
hidden: false
---
<Callout icon="📘" theme="info">
  1. Messages must include between 2 and 10 cards.
  2. Main message body text is required.
  3. Main message headers, footers, and interactive components are not supported.
  4. Cards must include either an image or video header. Other header types are not supported.
  5. Card body text is optional.
  6. Cards must include either one URL button, or one or more quick-reply buttons. Button types and numbers must match across all cards (for example, if you define a card with 2 quick-reply buttons, all cards must define exactly 2 quick-reply buttons).
  7. Use the `recipient` parameter only when BSUID is enabled for the app.
  8. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.
     <br />
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
            "type": "carousel",
            "body": {
              "text": "Check out our latest offers!"
            },
            "action": {
              "cards": [
                {
                  "card_index": 0,
                  "type": "cta_url",
                  "header": {
                    "type": "image",
                    "image": {
                      "link": "https://gs-upload.gupshup.io/whatsapp/sample-media/png/sample01.png"
                    }
                  },
                  "body": {
                    "text": "Adidas – Flat 40% Off"
                  },
                  "action": {
                    "name": "cta_url",
                    "parameters": {
                      "display_text": "Shop now",
                      "url": "https://shop.example.com/adidas"
                    }
                  }
                },
                {
                  "card_index": 1,
                  "type": "cta_url",
                  "header": {
                    "type": "image",
                    "image": {
                      "link": "https://gs-upload.gupshup.io/whatsapp/sample-media/png/sample02.png"
                    }
                  },
                  "body": {
                    "text": "Nike – New Arrivals"
                  },
                  "action": {
                    "name": "cta_url",
                    "parameters": {
                      "display_text": "View collection",
                      "url": "https://shop.example.com/nike"
                    }
                  }
                }
              ]
            }
          }
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
--header 'Authorization: sk_f39ed14bxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "91888xxxxxx",
	"recipient": "IN.4614498218826880",
  "type": "interactive",
  "interactive": {
    "type": "carousel",
    "body": {
      "text": "Check out our latest offers!"
    },
    "action": {
      "cards": [
        {
          "card_index": 0,
          "type": "cta_url",
          "header": {
            "type": "image",
            "image": {
              "link": "https://gs-upload.gupshup.io/whatsapp/sample-media/png/sample01.png"
            }
          },
          "body": {
            "text": "Adidas – Flat 40% Off"
          },
          "action": {
            "name": "cta_url",
            "parameters": {
              "display_text": "Shop now",
              "url": "https://shop.example.com/adidas"
            }
          }
        },
        {
          "card_index": 1,
          "type": "cta_url",
          "header": {
            "type": "image",
            "image": {
              "link": "https://gs-upload.gupshup.io/whatsapp/sample-media/png/sample02.png"
            }
          },
          "body": {
            "text": "Nike – New Arrivals"
          },
          "action": {
            "name": "cta_url",
            "parameters": {
              "display_text": "View collection",
              "url": "https://shop.example.com/nike"
            }
          }
        }
      ]
    }
  }
}'
```

<br />

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
