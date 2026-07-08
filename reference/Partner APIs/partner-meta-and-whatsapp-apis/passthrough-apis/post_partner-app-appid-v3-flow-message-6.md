---
api:
  file: Passthrough_flow (2).json
  operationId: post_partner-app-appid-v3-message
hidden: true
---
<Callout icon="📘" theme="info">
  **Note: **

  1. Eligibility depends not only on business verification, but also on WABA quality and messaging limits. To determine if a client is eligible to use Flows, you should attempt to send a Flow. If the account is not yet eligible, Meta recommends focusing on improving the quality of the current WABA (WhatsApp Business Account).
  2. Once the quality checks are successfully completed, your account will receive higher messaging limits and access to Flows.
  3. Use the `recipient` parameter only when BSUID is enabled for the app.
  4. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.
</Callout>

After you create a WhatsApp Flow, you can send it. To send a message with a flow, we have introduced a new type of the Interactive Object called flow.

#### [Meta Flow Message Doc Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-flow-messages)

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
        Data Types
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
        APP ID
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
        The Id should be a valid app Id of Gupshup
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
        Type should be interactive to send address message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        interactive
      </td>

      <td style={{ textAlign: "left" }}>
        Add sticker   body
      </td>

      <td style={{ textAlign: "left" }}>
        "interactive": \{

        "\{\{Flow_BODY}}"

        }
      </td>

      <td style={{ textAlign: "left" }}>
        Object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Key should be interactive to send flow message.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "recipient_type": "individual",
    "messaging_product": "whatsapp",
    "to": "{{WHATSAPP_USER_PHONE_NUMBER}}",
		"recipient": "{{BSUID}}",
    "type": "interactive",
    "interactive": {
        "type": "flow",
        "header": {
            "type": "{{TYPE}}",
            "text": "{{FLOW_MSG_HEADER}}"
        },
        "body": {
            "text": "{{FLOW_MSG_BODY}}}"
        },
        "footer": {
            "text": "{{FLOW_MSG_FOOTER}}"
        },
        "action": {
            "name": "flow",
            "parameters": {
                "flow_message_version": "{{FLOW_MSG_VERSION}}",
                "flow_token": "{{FLOW_TOKEN}}",
                "flow_id": "{{FLOW_ID}}",
                "flow_cta": "{{FLOW_CTA}}",
                "flow_action": "{{FLOW_ACTION}}",
                "flow_action_payload": {
                    "screen": "{{SCREEN_NAME}}",
                    "data": {
                        "product_name": "{{PRODUCT_NAME}}",
                        "product_description": "{{DESCRIPTION}}",
                        "product_price": {{PRODUCT_PRICE}}
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

        "messages": [\{"id": "GUPSHUP_MESSAGE_ID"
        }
        ],
        "messaging_product": "whatsapp",
        "contacts": [
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
        401
      </td>

      <td>
        \{

        "status": "error","message": "Authentication Failed"}
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
        \{

        "message": "Callback Billing must be enabled for this API","status": "error"}
      </td>

      <td>
        If Callback billing is not enabled for the app
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
        If app details are not found
      </td>
    </tr>
  </tbody>
</Table>
