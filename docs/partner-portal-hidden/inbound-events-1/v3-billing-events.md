---
summary: v3 Billing events
title: v3 Billing events
deprecated: false
hidden: true
metadata:
  robots: index
---
<Callout icon="📘" theme="info">
  There is no Meta fees charged for service conversations 1st Nov onwards, hence the billable parameter will be false for service conversations.
</Callout>

The billing-event informs you if a conversation is billable or not. Learn more about [Conversation based pricing](https://support.gupshup.io/hc/es-co/articles/4414423534617-Gu%C3%ADa-r%C3%A1pida-sobre-la-implementaci%C3%B3n-de-Precios-Basados-en-Conversaciones-PBC-en-el-Autoservicio-de-Gupshup).

<Callout icon="📘" theme="info">
  Note : There may be a delay of up to 60 minutes in receiving the billing events on V2 and V3 subscriptions in peak times.
</Callout>

```json billing-event
{
    "app": "DemoAPI",
    "timestamp":1580546677791,
    "version":2,
    "type": "billing-event",
    "payload":{
        "deductions":{
            "type": "marketing/authentication/utility/service/FEP/FTC",
            "conversationType": "service",
            "model": "NBP/CBP",
            "source": "whatsapp",
            "billable":"true/false"
       },
        "references":{
            "id":"59f8db90c37e-4408-90ab-cc54ef8246ad",
            "gsId":"ee4a68a0-1203-4c85-8dc3-49d0b3226a35",
            "conversationId":"532b57b5f6e63595ccd74c6010e5c5c7",
            "destination":"91XX985XX10X"
        }
    }
}
```
```Text billing-event-MM Lite
{
  "app": "ODTestXXXXX",
  "timestamp": 1743831556261,
  "version": 2,
  "type": "billing-event",
  "payload": {
    "deductions": {
      "type": "marketing_lite",
      "model": "CBP",
      "source": "whatsapp",
      "billable": true
    },
    "references": {
      "id": "ee1fdcfa-5a71-409f-8e5e-8b43c552a71a",
      "gsId": "ab4085f3-7d1b-4331-95d3-da301ad25baa",
      "conversationId": "ce17b8adb8ddfe3700a7f86c3f952e78",
      "destination": "919108568600"
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
        `type`
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
        `conversationType`
      </td>

      <td>
        The type of FTC (Free Tier Conversation). This parameter is only received for `type` FTC.  
        If type='FTC' then conversationType is "service"
      </td>

      <td>
        Service
      </td>
    </tr>

    <tr>
      <td>
        `model`
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
        `source`
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
        `billable`
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

| Key              | Description                                                                                 | Example                              |
| :--------------- | :------------------------------------------------------------------------------------------ | :----------------------------------- |
| `id`             | Unique WhatsApp identifier for a message                                                    | 59f8db90c37e-4408-90ab-cc54ef8246ad  |
| `gsId`           | Unique Gupshup identifier for a message                                                     | ee4a68a0-1203-4c85-8dc3-49d0b3226a35 |
| `conversationId` | Unique identifier for a conversation                                                        | 532b57b5f6e63595ccd74c6010e5c5c7     |
| `destination`    | Phone number of the user engaged in the conversation. Phone Number will be in E.164 format. | 91XX985XX10X                         |

# Call Interactions

This document outlines the structure and fields of billing events related to call interactions.

## Sample Payload

```Text billing-event
{
	"entry": [
		{
			"changes": [
				{
					"field": "billing-event",
					"value": {
						"billing": {
							"deductions": {
								"billable": "true/false",
								"conversation_type": "call",
								"source": "whatsapp"
							},
							"references": {
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
```Text billing-event-CBP
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
								"billable": true,
								"model": "CBP",
								"source": "whatsapp",
								"type": "marketing",
								"conversation_type": "service"
							},
						"references": 
              {
								"conversation_id": "4fbe96296619fdcf34910786bdd96079",
								"destination": "919163805873",
								"gs_id": "01e8e5c8-a171-457f-af7a-9723c60a95b5",
								"id": "0f19ef62-80ef-48c2-a493-9ac112478d20"
							}
						}
					}
				}
			]
		}
	],
		"gs_app_id": "13ecfc3d-499c-42f4-ba59-1604f8654389",
		"object": "whatsapp_business_account"
}
```
```Text billing-event-PMP
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
								"billable": true,
								"model": "PMP",
								"source": "whatsapp",
								"type": "regular",
								"category": "marketing"
							},
							"references": 
              {
								"destination": "919163805873",
								"gs_id": "01e8e5c8-a171-457f-af7a-9723c60a95b5",
								"id": "0f19ef62-80ef-48c2-a493-9ac112478d20"
							}
						}
					}
				}
			]
		}
	],
		"gs_app_id": "13ecfc3d-499c-42f4-ba59-1604f8654389",
		"object": "whatsapp_business_account"
}
```
```Text billing-event-CBP-sent/delivered
{
	"entry": 
  [
		{
			"changes": 
      [
				{
					"field": "messages",
					"value": 
          {
						"messaging_product": "whatsapp",
						"metadata": 
            {
							"display_phone_number": "{{APP_PHONE}}",
							"phone_number_id": "{{PHONE_ID}}"
						},
						"statuses": 
            [
							{
								"conversation": 
                {
									"expiration_timestamp": "1710936120",
									"id": "{{CONVERSATION_ID}}",
									"origin": 
                  {
										"type": "service"
									}
								},
									"gs_id": "{{GS_MESSAGE_ID}}",
									"id": "{{WA_MESSAGE_ID}}",
									"pricing": 
                {
									"billable": true,
									"category": "service",
									"pricing_model": "CBP"
								},
									"recipient_id": "{{END_USER_PHONE_NUMBER}}",
									"status": "sent",
									"timestamp": "1710930461"
							}
						]
					}
				}
			],
				"id": "112535025189792"
		}
	],
	"gs_app_id": "{{APP_NAME}}",
	"object": "whatsapp_business_account"
}
```
```Text billing-event-PMP-sent/delivered
{
	"entry": 
  [
		{
			"changes": 
      [
				{
					"field": "messages",
					"value": 
          {
						"messaging_product": "whatsapp",
						"metadata": 
            {
							"display_phone_number": "{{APP_PHONE}}",
							"phone_number_id": "{{PHONE_ID}}"
						},
						"statuses": 
            [
							{
								"conversation": 
                {
									"expiration_timestamp": "1710936120",
									"id": "{{CONVERSATION_ID}}",
									"origin": 
                  {
										"type": "service"
									}
								},
								"gs_id": "{{GS_MESSAGE_ID}}",
								"id": "{{WA_MESSAGE_ID}}",
								"pricing": 
                {
									"billable": true,
									"category": "marketing",
									"pricing_model": "PMP"
									"type": "regular"
								},
								"recipient_id": "{{END_USER_PHONE_NUMBER}}",
								"status": "sent",
								"timestamp": "1710930461"
							}
						]
					}
				}
			],
			"id": "112535025189792"
		}
	],
	"gs_app_id": "{{APP_NAME}}",
	"object": "whatsapp_business_account"
}
```

### Root-Level Field Descriptions

| Key               | Description                                                                                     |
| :---------------- | :---------------------------------------------------------------------------------------------- |
| entry             | An array containing event entries. Each entry represents a change related to a billing event.   |
| changes           | An array detailing the specific changes in the billing event.                                   |
| field             | Specifies the type of event. For billing events, this is set to "billing-event".                |
| value             | Contains the billing information.                                                               |
| billing           | Holds the deductions and references related to the billing event.                               |
| deductions        | Details about the billing deductions.                                                           |
| billable          | Indicates whether the wallet is deducted for this event. Possible values are "true" or "false". |
| conversation_type | Specifies the type of conversation. In this context, it is "call".                              |
| source            | Denotes the source of billing, e.g., "whatsapp".                                                |
| references        | Provides additional information related to the billing event.                                   |
| conversation_type | Refers to the type of conversation, either "MESSAGE" or "CALL".                                 |
| destination       | The recipient's phone number.                                                                   |
| source            | The sender's phone number.                                                                      |
| direction         | Indicates the direction of the call, either "USER_INITIATED" or "BUSINESS_INITIATED".           |
| id                | The unique identifier for the WhatsApp call.                                                    |
| duration          | The duration of the call in seconds.                                                            |
| start_time        | The start time of the call.                                                                     |
| end_time          | The end time of the call.                                                                       |
| gs_app_id         | The unique identifier for the Gupshup application.                                              |
| object            | Specifies the object type, in this case, "whatsapp_business_account".                           |

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
