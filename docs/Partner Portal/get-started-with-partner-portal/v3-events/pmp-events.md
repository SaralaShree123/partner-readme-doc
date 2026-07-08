---
title: PMP Events
excerpt: Inbound v3 events post the per message based pricing roll out on 1st July 2025
deprecated: false
hidden: false
metadata:
  title: PMP
  robots: index
---
# Sent

<Accordion title="Key Changes in Sent event V3" icon="fa-info-circle">
  * Addition of new key type inside pricing object
  * Value of pricing\_model key to change from CBP to PMP
</Accordion>

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "{{APP_PHONE}}",
              "phone_number_id": "{{PHONE_ID}}"
            },
            "statuses": [
              {
                "conversation": {
                  "expiration_timestamp": "1710936120",
                  "id": "{{CONVERSATION_ID}}",
                  "origin": {
                    "type": "service"
                  }
                },
                "gs_id": "{{GS_MESSAGE_ID}}",
                "id": "{{WA_MESSAGE_ID}}",
                "pricing": {
                  "billable": true,
                  "category": "marketing",
                  "pricing_model": "PMP",
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

## Payload Description

| Key                             | Description                        | Example                            |
| :------------------------------ | :--------------------------------- | :--------------------------------- |
| object                          | Type of object that sent the event | whatsapp\_business\_account        |
| gs\_app\_id                     | Gupshup application ID             | 7bf06899-5f0f-4cca-be3b-xxxxxxxxxx |
| metadata.display\_phone\_number | Display phone number               | 9\*\*\*\*\*\*8                     |
| metadata.phone\_number\_id      | Phone number ID                    | 158072934066266                    |
| statuses\[].conversation.id     | Conversation ID                    | 0f957b88cfb1558f6199exxxxxxxx      |
| statuses\[].id                  | WhatsApp message ID (wamid)        | d04cc3a7-18f0-4571-831e-xxxxxxxx   |
| statuses\[].recipient\_id       | Destination phone number           | 79507xxxxx                         |
| statuses\[].status              | Message status                     | sent                               |
| statuses\[].timestamp           | Timestamp (in seconds)             | 1739354482                         |

# Delivered

<br />

<Accordion title="Key Changes in Delivered event V3" icon="fa-info-circle">
  * Addition of new key type inside pricing object
  * Value of pricing\_model key to change from CBP to PMP
</Accordion>

<br />

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "{{APP_PHONE}}",
              "phone_number_id": "{{PHONE_ID}}"
            },
            "statuses": [
              {
                "conversation": {
                  "expiration_timestamp": "1710936120",
                  "id": "{{CONVERSATION_ID}}",
                  "origin": {
                    "type": "service"
                  }
                },
                "gs_id": "{{GS_MESSAGE_ID}}",
                "id": "{{WA_MESSAGE_ID}}",
                "pricing": {
                  "billable": true,
                  "category": "marketing",
                  "pricing_model": "PMP",
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

## Payload Description

| Key                             | Description                        | Example                            |
| :------------------------------ | :--------------------------------- | :--------------------------------- |
| object                          | Type of object that sent the event | whatsapp\_business\_account        |
| gs\_app\_id                     | Gupshup application ID             | 7bf06899-5f0f-4cca-be3b-xxxxxxxxxx |
| metadata.display\_phone\_number | Display phone number               | 9\*\*\*\*\*\*8                     |
| metadata.phone\_number\_id      | Phone number ID                    | 158072934066266                    |
| statuses\[].conversation.id     | Conversation ID                    | 0f957b88cfb1558f6199exxxxxxxx      |
| statuses\[].id                  | WhatsApp message ID (wamid)        | d04cc3a7-18f0-4571-831e-xxxxxxxx   |
| statuses\[].recipient\_id       | Destination phone number           | 79507xxxxx                         |
| statuses\[].status              | Message status                     | delivered                          |
| statuses\[].timestamp           | Timestamp (in seconds)             | 1739354482                         |

# Billing

<Accordion title="Key Changes for Billing Event V3" icon="fa-info-circle">
  * Removal of conversation\_id and conversation\_type key
  * Addition of new key category
  * Value of model key to change from CBP to PMP
  * typekey inside deductions object to take up new values (refer table below for supported values)
</Accordion>

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "billing-event",
          "value": {
            "billing": {
              "deductions": {
                "billable": true,
                "model": "PMP",
                "source": "whatsapp",
                "type": "regular",
                "category": "marketing"
              },
              "references": {
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

## Payload Description

| Key                             | Description                        | Example                           |
| :------------------------------ | :--------------------------------- | :-------------------------------- |
| object                          | Type of object that sent the event | whatsapp\_business\_account       |
| gs\_app\_id                     | Gupshup application ID             | xxxxxxx23d31f949e98869bc9a1xxxxxx |
| metadata.display\_phone\_number | Display phone number               | 79507xxxxxxxx                     |
| metadata.phone\_number\_id      | Phone number ID                    | 158072934066266                   |
| statuses\[].conversation.id     | Conversation ID                    | 3dabdf65abaf1cbbf85217d232cce91f  |
| statuses\[].id                  | WhatsApp message ID (wamid)        | d04cc3a7-18f0-4571-831e-xxxxxxxx  |
| statuses\[].recipient\_id       | Destination phone number           | 79507xxxxxxxx                     |