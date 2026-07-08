---
api:
  file: Direct send message.json
  operationId: passthroughSendMessage
hidden: true
---
# Overview

This document describes the Partner Portal API for sending direct (session) WhatsApp messages to a user. The endpoint is a passthrough to WhatsApp Cloud API v3 messaging.

Supported direct message types in this doc include text and interactive (reply buttons). The same endpoint also accepts other WhatsApp message types supported by upstream (e.g. image) when included in the JSON body.

<br />

# Send Direct Message — Text

## Request example

```
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "<RECIPIENT_PHONE_NUMBER>",
  "type": "text",
  "text": {
    "body": "<BODY_TEXT>"
  },
  "category": "utility"
}'
```

<br />

## Description

This API sends a text direct (session) message to a WhatsApp user. Use "type": "text" with a text.body field. Include "category": "utility" (or another valid category) as required by your messaging use case.

<br />

# Send Direct Message — Interactive (Reply Buttons)

## Request example

```
curl --request POST \
  --url 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
  --header 'Authorization: {{PARTNER_APP_TOKEN}}' \
  --header 'Content-Type: application/json' \
  --data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "<RECIPIENT_PHONE_NUMBER>",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "header": {
      "type": "image",
      "image": {
        "link": "https://picsum.photos/id/237/200/300"
      }
    },
    "body": {
      "text": "Your refund of 5USD for order 94661 has been processed.\nAmount will reflect in your account within 5 weeks."
    },
    "footer": {
      "text": "Thank you"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "1",
            "title": "Click Me!"
          }
        }
      ]
    }
  },
  "category": "utility"
}'
```

<br />

## Description

This API sends an interactive direct message with reply buttons. Set "type": "interactive" and provide the interactive object (header, body, footer, and action.buttons as per WhatsApp Cloud API).

<br />

# Send Direct Message — With TTL

Direct Send supports an optional TTL parameter for utility-category messages.

## Request example

```
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "<RECIPIENT_PHONE_NUMBER>",
  "type": "text",
  "text": {
    "body": "<BODY_TEXT>"
  },
  "category": "utility",
  "ttl_seconds": 600
}'
```

<br />

## TTL constraints

| Constraint        | Value                                                     |
| :---------------- | :-------------------------------------------------------- |
| Minimum           | 30 seconds                                                |
| Maximum           | 43,200 seconds (12 hours)                                 |
| Category required | "category": "utility" must be present for TTL to apply    |
| Without category  | Using ttl_seconds without category returns error code 100 |

<br />

# Response

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
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        200
      </td>

      <td>
        ````
        ```
        {
          "messages": [
            {
              "id": "{{GUPSHUP_MESSAGE_ID}}"
            }
          ],
          "messaging_product": "whatsapp",
          "contacts": [
            {
              "input": "{{DESTINATION_PHONE_NO}}",
              "wa_id": "{{DESTINATION_PHONE_NO}}"
            }
          ]
        }
        ````
      </td>

      <td>
        Success response (shape as returned by WhatsApp upstream)
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        ```
        ``
        {
          "status": "error",
          "message": "Authentication Failed"
        }

        ```
      </td>

      <td>
        When API key / Partner App token authentication fails
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        ```
        {
          "message": "Invalid App Details",
          "status": "error"
        }
        ```
      </td>

      <td>
        If app details are not found or app is not associated with the partner
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        Upstream validation error (e.g. error code 100)
      </td>

      <td>
        e.g. ttl_seconds used without "category": "utility"
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        ```

        {
          "status": "error",
          "message": "Internal server error..."
        }
        ```
      </td>

      <td>
        Unexpected portal or upstream failure
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Request parameters

<br />

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Values
      </th>

      <th>
        Data Type
      </th>

      <th>
        Required/Optional
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Headers**
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Authorization
      </td>

      <td>
        Access token for the application
      </td>

      <td>
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Valid Partner App access token (PARTNER_APP role). Obtain via partner login and GET /partner/app/appId/token.
      </td>
    </tr>

    <tr>
      <td>
        Content-Type
      </td>

      <td>
        Request media type
      </td>

      <td>
        application/json
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Must be application/json.
      </td>
    </tr>

    <tr>
      <td>
        **Path params**
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        APP ID
      </td>

      <td>
        App ID for the WhatsApp application
      </td>

      <td>
        `{{APP_ID}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Valid Gupshup app ID linked to the partner account.
      </td>
    </tr>

    <tr>
      <td>
        **Body JSON**
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        messaging_product
      </td>

      <td>
        Messaging product
      </td>

      <td>
        whatsapp
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Fixed value whatsapp.
      </td>
    </tr>

    <tr>
      <td>
        recipient_type
      </td>

      <td>
        Recipient type
      </td>

      <td>
        individual
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Typically individual for one-to-one messages.
      </td>
    </tr>

    <tr>
      <td>
        to
      </td>

      <td>
        Destination phone number (E.164 without +)
      </td>

      <td>
        e.g. 919428952010
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Valid WhatsApp-enabled phone number.
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        Message type
      </td>

      <td>
        text, interactive, etc.
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        text for plain text; interactive for button/list messages.
      </td>
    </tr>

    <tr>
      <td>
        text
      </td>

      <td>
        Text message payload
      </td>

      <td>
        `{ "body": "<BODY_TEXT>" } `
      </td>

      <td>
        Object
      </td>

      <td>
        Required when type is textRequired
      </td>

      <td>
        body is the message text.
      </td>
    </tr>

    <tr>
      <td>
        interactive
      </td>

      <td>
        Interactive message payload
      </td>

      <td>
        See interactive example above
      </td>

      <td>
        Object
      </td>

      <td>
        Required when type is interactive
      </td>

      <td>
        Structure per WhatsApp Cloud API (header, body, footer, action).
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        Message category
      </td>

      <td>
        utility
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        <br />
      </td>
    </tr>

    <tr>
      <td>
        ttl_seconds
      </td>

      <td>
        Time-to-live for the message (seconds)
      </td>

      <td>
        e.g. 600
      </td>

      <td>
        Integer
      </td>

      <td>
        Optional
      </td>

      <td>
        Min 30, max 43200. Only effective with "category": "utility".
      </td>
    </tr>
  </tbody>
</Table>
