---
api:
  file: Address_Message(1).json
  operationId: post_partnerapp{appId}v3message
hidden: false
link:
  new_tab: false
metadata:
  robots: noindex
---
Address messages give your users a simpler way to share the shipping address with the business on Whats App.

Address messages are interactive messages that contain the 4 main parts: header, body, footer, and action. Inside the action component business specifies the name “address_message” and relevant parameters.

#### [Meta Address Message Doc Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/address-messages)

<br />

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

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
        Value
      </th>

      <th>
        Data type
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
        Authorization
      </td>

      <td>
        Access Token for the application
      </td>

      <td>
        \{\{PARTNER_APP_TOKEN}}
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td>
        appId
      </td>

      <td>
        App ID to fetch the access token
      </td>

      <td>
        \{\{APP_ID}}
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        The Id should be a valid app Id of Gupshup.
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

      </td>
    </tr>

    <tr>
      <td>
        to
      </td>

      <td>
        Destination phone number where the message needs to be sent
      </td>

      <td>
        91785876xxxx
      </td>

      <td>
        String
      </td>

      <td>
        Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead)
      </td>

      <td>
        Must be a valid phone number
      </td>
    </tr>

    <tr>
      <td>
        recipient
      </td>

      <td>
        Destination BSUID where the message needs to be sent
      </td>

      <td>
        IN.461449821882xxxx
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        Must be a valid BSUID
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        Messaging type
      </td>

      <td>
        interactive
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Type should be interactive to send address message.
      </td>
    </tr>

    <tr>
      <td>
        interactive
      </td>

      <td>
        Add address body
      </td>

      <td>
        "interactive":

        \{"type": "address_message","body":\{"text": "Thanks for your order! Tell us what address you’d like this order delivered to."},        "action":        \{        "name": "address_message",        "parameters":        \{        "country": "IN",        "values":        \{        "name": "CUSTOMER_NAME",        "phone_number": "+91xxxxxxxxxx"        }        } }}
      </td>

      <td>
        Object
      </td>

      <td>
        Required
      </td>

      <td>
        •	Key should be interactive to send address message.

        • Currently address messages are supported in the following two countries: India and Singapore.  
        • For more information please refer provide meta document
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
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "{{WHATSAPP_USER_PHONE_NUMBER}}",
		"recipient": "{{BSUID}}",
    "type": "interactive",
    "interactive": {
        "type": "address_message",
        "body": {
            "text": "{{TEXT_MSG}}"
        },
        "action": {
            "name": "address_message",
            "parameters": {
                "country": "{{COUNTRY_ISO_COD}}"
            }
        }
    }
}'
```

## Sample Response

```
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

        "messages": [\{"id": "GUPSHUP_MESSAGE_ID"}],"messaging_product": "whatsapp","contacts": [\{"input": "DESTINATION_PHONE_NO",        "wa_id": "DESTINATION_PHONE_NO"        }        ]        }
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

        "status": "error","message": "Authentication Failed"}
      </td>

      <td>
        When API key authentication fails
      </td>
    </tr>
  </tbody>
</Table>
