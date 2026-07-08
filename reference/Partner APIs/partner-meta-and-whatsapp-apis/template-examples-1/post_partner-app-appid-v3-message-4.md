---
api:
  file: partner-portal-api-17.json
  operationId: post_partner-app-appid-v3-message
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Product card carousel templates allow you to send a single text message accompanied by a set of up to 10 product cards in a horizontally scrollable view

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Values</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Data Types</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner App Access Token.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>APP ID</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App ID to fetch the access token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>bf9ee64c-3d4d-4ac4-xxxx-732e577007c4</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The Id should be a valid app Id of Gupshup</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>messaging_product</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Messaging product</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>whatsapp</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>recipient_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Recipient type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>individual</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>to</p></td>
 <td style="border: 1px solid #ddd; padding: 8px;"><p>Destination phone number where the message needs to be sent</p>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>91785876xxxx</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead)</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be a valid phone number</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>recipient</p>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Destination BSUID where the message needs to be sent</p>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>IN.461449821882xxxx</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be a valid BSUID</p>
</td>
</tr>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Messaging type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>video</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Type should be <code>video</code> to<br>send video message.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Template message inside body</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;template&quot;: {<br>    &quot;name&quot;: &quot;Template&quot;<br>    ......<br>  }</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Object</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Key should be template to send template message.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/<APP_ID>/v3/message' \
--header 'Authorization: <PARTNER_APP_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "<WHATSAPP_USER_PHONE_NUMBER>",
	"recipient": "<BSUID>",
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

| Status Code | Response                                                                                                                                                                                                                                                                              | Comments                                       |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                       |                                                |
| 200         | `{     "messages": [           {               "id": "GUPSHUP_MESSAGE_ID"           }       ],     "messaging_product": "whatsapp",     "contacts": [           {               "input": "DESTINATION_PHONE_NO",               "wa_id": "DESTINATION_PHONE_NO"           }       ] }` |                                                |
| **Error**   |                                                                                                                                                                                                                                                                                       |                                                |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                                                                                                                                                                                                     | When API key authentication fails              |
| 400         | `{       "message": "Callback Billing must be enabled for this API",       "status": "error"   }`                                                                                                                                                                                     | If Callback billing is not enabled for the app |
| 400         | `{       "message": "Invalid App Details",       "status": "error"   }`                                                                                                                                                                                                               | If app details are not found                   |
