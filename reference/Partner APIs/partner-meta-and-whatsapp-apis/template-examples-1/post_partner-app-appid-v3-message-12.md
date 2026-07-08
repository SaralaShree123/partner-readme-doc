---
api:
  file: partner-portal-api-44.json
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
> 1. Sending Marketing Templates through MM Lite for enhanced delivery optimization. For more details, refer to [_MM Lite_](https://partner-docs.gupshup.io/docs/marketing-messages-lite-mm-lite-api) document.
> 2. Use the `recipient` parameter only when BSUID is enabled for the app.
> 3. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

| Key               | Value                   | Description                                                 | Data type | Required/Optional                                                                                  | Constraints                                               |
| :---------------- | :---------------------- | :---------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Authorization     | \{\{PARTNER_APP_TOKEN}} | Access Token for the application                            | String    | Required                                                                                           | Should be a valid Partner App Access Token.               |
| appId             | \{\{APP_ID}}            | App ID to fetch the access token                            | String    | Required                                                                                           | The ID should be a valid app Id of Gupshup.               |
| messaging_product | whatsapp                | Messaging product                                           | String    | Required                                                                                           |                                                           |
| recipient_type    | individual              | Recipient type                                              | String    | Required                                                                                           |                                                           |
| to                | 91785876xxxx            | Destination phone number where the message needs to be sent | String    | Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead) | Must be a valid phone number                              |
| recipient         | IN.461449821882xxxx     | Destination BSUID where the message needs to be sent        | String    | Optional                                                                                           | Must be a valid BSUID                                     |
| type              | template                | Messaging type                                              | String    | Required                                                                                           | The type should be `template` to send a template message. |
| template          | `{<BODY>}`              | Template message inside body                                | Object    | Required                                                                                           |                                                           |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
	"messaging_product": "whatsapp",
	"recipient_type": "individual",
  "to": "PHONE_NUMBER",
	"recipient": "BSUID",
	"type": "template",
	"template": {
		"name": "TEMPLATE_NAME",
		"language": {
			"code": "LANGUAGE_AND_LOCALE_CODE"
		},
		"components": [
			{
				"type": "header",
				"parameters": [
				{
					"type": "image",
					"image": {
						"link": "https://URL"
					}
				}
			]
		},
		{
			"type": "body",
			"parameters": [
				{
					"type": "text",
					"text": "TEXT-STRING"
				},
				{
					"type": "currency",
					"currency": {
					"fallback_value": "VALUE",
					"code": "USD",
					"amount_1000": "NUMBER"
					}
				},
				{
					"type": "date_time",
					"date_time": {
					"fallback_value": "MONTH DAY, YEAR"
					}
				}
			]
		}
	]
}
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
        ```
        {  
        	"message": "Callback Billing must be enabled for this API",  
        	"status": "error"  
        }
        ```
      </td>

      <td>
        if Callback billing is not  
        enabled for the app
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
        if app details are not found
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        ```
        {  
        	"status": "error",  
        	"message": "Authentication Failed"  
        }
        ```
      </td>

      <td>
        When API key authentication fails
      </td>
    </tr>
  </tbody>
</Table>
