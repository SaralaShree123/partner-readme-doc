---
title: Authentication-based Message Templates
api:
  file: authentication_based_template_msg.json
  operationId: post_partner-app-appid-v3-message
hidden: true
---
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
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
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
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        `{{APP_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        \- The Id should be a valid app Id of Gupshup.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        messaging\_product
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
        recipient\_type
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
        Destination phone no

        where the
        message
        need to be
        send
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
        Must be a valid phone number
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
        template
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
        \{          
           \<BODY>
        }
      </td>

      <td style={{ textAlign: "left" }}>
        Object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
	"messaging_product": "whatsapp",
	"recipient_type": "individual",
	"to": "<CUSTOMER_PHONE_NUMBER>",
	"type": "template",
	"template": 
	{
		"name": "<TEMPLATE_NAME>",
		"language": {
		"code": "<TEMPLATE_LANGUAGE_CODE>"
	},
	"components": 
	[
	{
		"type": "body",
		"parameters": 
		[
		{
			"type": "text",
			"text": "<ONE-TIME PASSWORD>"
		}
		]
	},
	{
		"type": "button",
		"sub_type": "url",
		"index": "0",
		"parameters": 
		[
		{
			"type": "text",
			"text": "<ONE-TIME PASSWORD>"
		}
		]
	}
	]
	}
}'
```

## Sample Response

```
{
	"messages": 
	[
	{
		"id": "GUPSHUP_MESSAGE_ID"
	}
	],
	"messaging_product": "whatsapp",
	"contacts": 
		[
		{
			"input": "DESTINATION_PHONE_NO",
			"wa_id": "DESTINATION_PHONE_NO"
		}
		]
}
```

<br />

## Status Codes

<Table align={["left","left","left","left"]}>
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

      <th>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{
        "messages":
        \[
        \{
        "id": "GUPSHUP\_MESSAGE\_ID"
        }
        ],
        "messaging\_product": "whatsapp",
        "contacts":
        \[
        \{
        "input": "DESTINATION\_PHONE\_NO",
        "wa\_id": "DESTINATION\_PHONE\_NO"
        }
        ]
        }
      </td>

      <td>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "message": "Callback Billing must be enabled for this API",
        "status": "error"
        }
      </td>

      <td>
        if Callback billing is not enabled for the app
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
        "message": "Invalid App Details",
        "status": "error"
        }
      </td>

      <td>
        if app details are not found
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
        "status": "error",
        "message": "Authentication failed"
        }
      </td>

      <td>
        When API key authentication fails
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>