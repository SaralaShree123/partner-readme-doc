---
title: Billing events
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘
>
> There is no Meta fees charged for service conversations 1st Nov onwards, hence the billable parameter will be false for service conversations

The billing-event informs you if a conversation is billable or not. Learn more about [Conversation based pricing](https://support.gupshup.io/hc/es-co/articles/4414423534617-Gu%C3%ADa-r%C3%A1pida-sobre-la-implementaci%C3%B3n-de-Precios-Basados-en-Conversaciones-PBC-en-el-Autoservicio-de-Gupshup).

```json billing-event
{
    "app": "DemoAPI",
    "timestamp":1580546677791,
    "version":2,
    "type": "billing-event",
    "payload":
  	{
      "deductions":
      {
            "type": "marketing/authentication/utility/service/FEP/FTC",
            "conversationType": "service",
            "model": "NBP/CBP",
            "source": "whatsapp",
            "billable":"true/false",
        		"category": "marketing lite",
       },
       "references":
      {
        "id":"59f8db90c37e-4408-90ab-cc54ef8246ad",
        "gsId":"ee4a68a0-1203-4c85-8dc3-49d0b3226a35",
        "conversationId":"532b57b5f6e63595ccd74c6010e5c5c7",
        "destination":"91XX985XX10X"
      }
    }
}
```

#### Deductions - Object Description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        type
      </td>

      <td>
        The type of conversation. Possible values:

        * FEP (Free entry point)
        * Marketing
        * Authentication
        * Utility -Service
        * FTC (Free Tier conversation)
      </td>

      <td>
        Marketing
      </td>
    </tr>

    <tr>
      <td>
        conversationType
      </td>

      <td>
        The type of FTC (Free Tier Conversation). This parameter is only received for `type` FTC.\
        If type='FTC' then conversationType is "service"
      </td>

      <td>
        Service
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        * marketing
        * marketing\_lite
        * utility
        * authentication
        * authentication\_international
        * service
        * referral\_conversion
      </td>

      <td>
        marketing\_lite
      </td>
    </tr>

    <tr>
      <td>
        model
      </td>

      <td>
        The pricing policy model applied for this message. Possible values:

        * CBP (Conversation based pricing)
        * NBP (Notification based pricing)
      </td>

      <td>
        CBP
      </td>
    </tr>

    <tr>
      <td>
        source
      </td>

      <td>
        Origin source of the conversation
      </td>

      <td>
        whatsapp
      </td>
    </tr>

    <tr>
      <td>
        billable
      </td>

      <td>
        The value is either `true` or `false` depending on whether a conversation is billable or not.
      </td>

      <td>
        false
      </td>
    </tr>
  </tbody>
</Table>

#### References - Object Description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        Unique WhatsApp identifier for a message
      </td>

      <td>
        59f8db90c37e-4408-90ab-cc54ef8246ad
      </td>
    </tr>

    <tr>
      <td>
        `gsId`
      </td>

      <td>
        Unique Gupshup identifier for a message
      </td>

      <td>
        ee4a68a0-1203-4c85-8dc3-49d0b3226a35
      </td>
    </tr>

    <tr>
      <td>
        `conversationId`
      </td>

      <td>
        Unique identifier for a conversation
      </td>

      <td>
        532b57b5f6e63595ccd74c6010e5c5c7
      </td>
    </tr>

    <tr>
      <td>
        `destination`
      </td>

      <td>
        Phone number of the user engaged in the conversation.
        Phone Number will be in E.164 format.
      </td>

      <td>
        91XX985XX10X
      </td>
    </tr>
  </tbody>
</Table>

# Call Interactions

This document outlines the structure and fields of billing events related to call interactions.

## Sample Payload

```Text Billing
{
	"entry":
  [
		{
			"changes":
      [
				{
					"field": "billing-event",
					"value":
          {
						"billing":
            {
							"deductions":
              {
								"billable": "true/false",
								"conversation_type": "call",
								"source": "whatsapp"
                "category": "marketing lite",
							},
							"references":
              {
								"conversation_type": "MESSAGE/CALL",
								"destination": "9191638XXXXX",
								"source": "9112fXXXXXX",
								"direction": "[USER_INITIATED|BUSINESS_INITIATED]",
								"id": "WHATSAPP_CALL_ID",
								"duration": "12321",
								"start_time": "",
								"end_time": ""
							}
						}
					}
				}
			]
		}
	],
	"gs_app_id": "GUPSHUP_APP_ID",
	"object": "whatsapp_business_account"
}
```

### Root-Level Field Descriptions

| Key                | Description                                                                                     |
| :----------------- | :---------------------------------------------------------------------------------------------- |
| entry              | An array containing event entries. Each entry represents a change related to a billing event.   |
| changes            | An array detailing the specific changes in the billing event.                                   |
| field              | Specifies the type of event. For billing events, this is set to "billing-event".                |
| value              | Contains the billing information.                                                               |
| billing            | Holds the deductions and references related to the billing event.                               |
| deductions         | Details about the billing deductions.                                                           |
| billable           | Indicates whether the wallet is deducted for this event. Possible values are "true" or "false". |
| conversation\_type | Specifies the type of conversation. In this context, it is "call".                              |
| source             | Denotes the source of billing, e.g., "whatsapp".                                                |
| references         | Provides additional information related to the billing event.                                   |
| conversation\_type | Refers to the type of conversation, either "MESSAGE" or "CALL".                                 |
| destination        | The recipient's phone number.                                                                   |
| source             | The sender's phone number.                                                                      |
| direction          | Indicates the direction of the call, either "USER\_INITIATED" or "BUSINESS\_INITIATED".         |
| id                 | The unique identifier for the WhatsApp call.                                                    |
| duration           | The duration of the call in seconds.                                                            |
| start\_time        | The start time of the call.                                                                     |
| end\_time          | The end time of the call.                                                                       |
| gs\_app\_id        | The unique identifier for the Gupshup application.                                              |
| object             | Specifies the object type, in this case, "whatsapp\_business\_account".                         |

## Sample Meta Billing Event

```Text Sample Meta Billing
{
	"entry": [
		{
			"changes": [
				{
					"field": "billing-event",
					"value": {
						"billing": {
							"deductions": {
								"billable": "true",
								"conversation_type": "call",
								"source": "whatsapp"
							},
							"references": {
								"conversation_type": "CALL",
								"destination": "919355015912",
								"direction": "USER_INITIATED",
								"duration": 18,
								"end_time": 1743598139,
								"id":"wacid.HBgMOTE5NjQzNTk1NDUyFQIAEhggMTczN0EzM0E4Q0MyRjk5RUQwQzQwRTZBQjk5NkRDODQcGAw5MTkzNTUwMTU5MTIVAgAA",
								"source": "919643595452",
								"start_time": 1743598121
							}
						}
					}
				}
			],
			"time": 1743598141518
		}
	],
	"gs_app_id": "b6016edd-12fb-4da1-8e96-e5bb634e271f",
	"object": "whatsapp_business_account"
}
```

## Sample GS Billing Event

```Text Sample GS Billing
{
	"entry": [
		{
			"changes": [
				{
					"field": "billing-event",
					"value": {
						"billing": {
							"deductions": {
								"billable": "false",
								"conversation_type": "call",
								"source": "gupshup"
							},
							"references": {
								"conversation_type": "CALL",
								"destination": "919355015912",
								"direction": "USER_INITIATED",
								"duration": 18,
								"end_time": 1743598139,
								"id":"wacid.HBgMOTE5NjQzNTk1NDUyFQIAEhggMTczN0EzM0E4Q0MyRjk5RUQwQzQwRTZBQjk5NkRDODQcGAw5MTkzNTUwMTU5MTIVAgAA",
								"source": "919643595452",
								"start_time": 1743598121
							}
						}
					}
				}
			],
			"time": 1743598141518
		}
	],
	"gs_app_id": "b6016edd-12fb-4da1-8e96-e5bb634e271f",
	"object": "whatsapp_business_account"
}
```