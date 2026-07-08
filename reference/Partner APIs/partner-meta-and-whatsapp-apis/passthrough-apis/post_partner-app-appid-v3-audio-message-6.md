---
api:
  file: Passthrough_audio (1).json
  operationId: post_partner-app-appid-v3-message
hidden: true
---
Audio messages display an audio icon and a link to an audio file. When the WhatsApp user taps the icon, the WhatsApp client loads and plays the audio file.

Here you can send audio messages using this API.

#### [Meta Audio Message Doc Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/audio-messages)

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
        The ID should be a valid Gupshup app ID.
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
        audio
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Type should be audio to send audio message.
      </td>
    </tr>

    <tr>
      <td>
        audio
      </td>

      <td>
        Add sticker body
      </td>

      <td>
        "audio": `{  
                                "id" : "798882015472548"  
                                }`
      </td>

      <td>
        Object
      </td>

      <td>
        Required
      </td>

      <td>
        Key should be audio to send audio message.
      </td>
    </tr>

    <tr>
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

      <td>

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
    "type": "audio",
    "audio": {
        "id": "{{MEDIA_ID}}"
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

        "messages": [\{"id": "GUPSHUP_MESSAGE_ID"}],
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
