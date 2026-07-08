---
api:
  file: gupshup_v3_document_message_api.yaml
  operationId: sendDocumentMessage
hidden: true
---
<br />

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

# Sample Request

```
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "{{PHONE_NUMBER}}",
		"recipient": "{{BSUID}}"
    "type": "document",
    "document": {
        "id": "{{MEDIA_ID}}", 
        "link": "{{MEDIA_LINK}}", 
        "caption": "{{MEDIA_CAPTION}}",
        "filename": "{{MEDIA_FILENAME}}"
    }
}'
```

<br />

# Sample Response

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

<br />

# Request Parameters

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
        Data Types
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
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Should be a valid Partner App Access Token.
      </td>
    </tr>

    <tr>
      <td>
        APP ID
      </td>

      <td>
        App ID to fetch the access token
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
        The Id should be a valid app Id of Gupshup
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
        document
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Type should be document to send document message.
      </td>
    </tr>

    <tr>
      <td>
        document
      </td>

      <td>
        Add document media ID or link inside body
      </td>

      <td>
        ```
        {
                "id": "{{MEDIA_ID}}", 
                "link": "{{MEDIA_LINK}}", 
                "caption": "{{MEDIA_CAPTION}}",
                "filename": "{{MEDIA_FILENAME}}"
            }
        ```
      </td>

      <td>
        Object
      </td>

      <td>
        Required
      </td>

      <td>
        Key should be document to send document message.
      </td>
    </tr>

    <tr>
      <td>
        caption
      </td>

      <td>
        Media asset caption text
      </td>

      <td>
        e.g - Please find the document attached
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        Maximum 1024 characters.
      </td>
    </tr>

    <tr>
      <td>
        filename
      </td>

      <td>
        Document filename, with extension
      </td>

      <td>
        e.g - demo.txt
      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        The WhatsApp client will use an appropriate file type icon based on the extension.
      </td>
    </tr>

    <tr>
      <td>
        id
      </td>

      <td>
        ID of the uploaded media asset.
      </td>

      <td>
        e.g - 1013859600285441
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Required if using uploaded media, otherwise omit.
      </td>
    </tr>

    <tr>
      <td>
        link
      </td>

      <td>
        URL of the media asset hosted on your public server.
      </td>

      <td>
        e.g - [https://www.luckyshrub.com/invoices/FmOzfD9cKf/lucky-shrub-invoice.pdf](https://www.luckyshrub.com/invoices/FmOzfD9cKf/lucky-shrub-invoice.pdf)
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Required if using hosted media, otherwise omit. For better performance, we recommend using id and an uploaded media asset ID instead.
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Status Codes

| Status Code | Response                                                                                                                                                          | Comments                                                                        |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| **Success** |                                                                                                                                                                   |                                                                                 |
| 200         | `{"messages": [{"id": "GUPSHUP_MESSAGE_ID"}], "messaging_product": "whatsapp", "contacts": [{"input": "DESTINATION_PHONE_NO", "wa_id": "DESTINATION_PHONE_NO"}]}` |                                                                                 |
| **Error**   |                                                                                                                                                                   |                                                                                 |
| 401         | `{"status": "error", "message": "Authentication Failed"}`                                                                                                         | When API key authentication failsIf Callback billing is not enabled for the app |
| 400         | `{"message": "Callback Billing must be enabled for this API", "status": "error"}`                                                                                 | If Callback billing is not enabled for the app                                  |
| 400         | `{"message": "Invalid App Details", "status": "error"}`                                                                                                           | If app details are not found                                                    |
