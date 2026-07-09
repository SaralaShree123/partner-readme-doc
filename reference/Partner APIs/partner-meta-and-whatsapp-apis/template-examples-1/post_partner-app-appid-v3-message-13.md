---
api:
  file: partner-portal-api-45.json
  operationId: post_partner-app-appid-v3-message
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note:
>
> 1. Sending Marketing Templates through MM Lite for enhanced delivery optimization. For more details, refer to [_MM Lite_](/docs/marketing-messages-lite-mm-lite-api) document.
> 2. Use the `recipient` parameter only when BSUID is enabled for the app.
> 3. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Data type</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid<br>Partner App Access<br>Token.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App ID to fetch the<br>access token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The ID should be a valid app Id of Gupshup.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>messaging_product</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>whatsapp</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Messaging product</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>individual</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Recipient type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>to</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>91785876xxxx</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Destination phone number where the message needs to be sent</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>IN.461449821882xxxx</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Destination BSUID where the message needs to be sent</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be a valid BSUID</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Messaging type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type should be <code>template</code> to send a template message.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{&lt;BODY&gt;}</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Template message inside body</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Object</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
	"messaging_product": "whatsapp",
	"recipient_type": "individual",
  "to": "16505551234",
	"recipient": "IN.4614498218826880",
	"type": "template",
	"template": {
		"name": "abandoned_cart",
		"language": {
			"code": "en_US"
		},
		"components": [
			{
				"type": "header",
				"parameters": [
					{
						"type": "text",
						"text": "Pablo"
					}
				]
			},
			{
				"type": "body",
				"parameters": [
					{
						"type": "text",
						"text": "10OFF"
					}
				]
			},
			{
				"type": "button",
				"sub_type": "mpm",
				"index": 0,
				"parameters": [
					{
						"type": "action",
						"action": {
							"thumbnail_product_retailer_id": "2lc20305pt",
							"sections": [
								{
									"title": "Popular Bundles",
									"product_items": [
										{
											"product_retailer_id": "2lc20305pt"
										},
										{
											"product_retailer_id": "nseiw1x3ch"
										}
									]
								},
								{
									"title": "Premium Packages",
									"product_items": [
										{
											"product_retailer_id": "n6k6x0y7oe"
										}
									]
								}
							]
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

| Status Code | Response                                                                                                                                                                                                                    | Comments                                       |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
| **Success** |                                                                                                                                                                                                                             |                                                |
| 200         | `{   	"messages": [   		{   			"id": "GUPSHUP_MESSAGE_ID"   		}   	],   	"messaging_product": "whatsapp",   	"contacts": [   		{   			"input": "DESTINATION_PHONE_NO",   			"wa_id": "DESTINATION_PHONE_NO"   		}   	]   }` |                                                |
| **Error**   |                                                                                                                                                                                                                             |                                                |
| 400         | `{   	"message": "Callback Billing must be enabled for this API",   	"status": "error"   }`                                                                                                                                 | if Callback billing is not enabled for the app |
| 400         | `{   	"message": "Invalid App Details",   	"status": "error"   }`                                                                                                                                                           | if app details are not found                   |
| 401         | `{   	"status": "error",   	"message": "Authentication Failed"   }`                                                                                                                                                         | When API key authentication fails              |
