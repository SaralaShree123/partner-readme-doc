---
title: PMP Events
excerpt: Inbound v2 events post the per message based pricing roll out on 1st July 2025
deprecated: false
hidden: false
metadata:
  title: PMP
  robots: index
---
## Billing Event

<Accordion title="Key changes for billing event" icon="fa-info-circle">
  1. Removal of conversation\_id and conversation\_type key
  2. Addition of new key category
  3. Value of model key to change from CBP to PMP
  4. type key inside deductions object to take up new values (refer table below for supported values)
</Accordion>

```json billing-event
{
	"app": "xxxxxxx23d31f949e98869bc9a1xxxxxx",
	"timestamp": 1739354482884,
	"version": 2,
	"type": "billing-event",
	"payload": 
  {
		"deductions": 
    {
			"type": "regular",
			"model": "PMP",
			"source": "whatsapp",
			"billable": true,
			"category": "marketing"
		},
			"references": 
    {
			"id": "d04cc3a7-18f0-4571-831e-xxxxxxxx",
			"gsId": "7bf06899-5f0f-4cca-be3b-xxxxxxxxxx",
			"destination": "79507xxxxxxxx"
		}
	}
}
```

<br />

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
        billing-event
      </td>

      <td>
        billing-event
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
        marketing
      </td>
    </tr>

    <tr>
      <td>
        model
      </td>

      <td>
        PMP
      </td>

      <td>
        PMP
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
        gupshup/whatsapp
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

    <tr>
      <td>
        gsId
      </td>

      <td>
        Unique Gupshup identifier for a message
      </td>

      <td>
        7bf06899-5f0f-4cca-be3b-xxxxxxxxxx
      </td>
    </tr>

    <tr>
      <td>
        destination
      </td>

      <td>
        Phone number of the user engaged in the conversation.
      </td>

      <td>
        79507xxxxxxxx
      </td>
    </tr>
  </tbody>
</Table>

#### References - Object Description

| Key         | Description                                           | Example                            |
| :---------- | :---------------------------------------------------- | :--------------------------------- |
| id          | Unique WhatsApp identifier for a message              | d04cc3a7-18f0-4571-831e-xxxxxxxx   |
| gsId        | Unique Gupshup identifier for a message               | 7bf06899-5f0f-4cca-be3b-xxxxxxxxxx |
| destination | Phone number of the user engaged in the conversation. | 79507xxxxxxxx                      |

## Sent

<Accordion title="Key changes for sent event " icon="fa-info-circle">
  * conversation object may not be available depedning on webhook version
  * Addition of new key type inside pricing object
  * Value of policy key to change from CBP to PMP
  * type key inside conversation object to take up new values (refer table below for supported values)
  * category key inside pricing object to take up new values (refer table below for supported values)
</Accordion>

```json sent
{
  "app": "{{xxxxxxx23d31f949e98869bc9a1xxxxxx}}",
  "phone": "{{APP_PHONE}}",
  "timestamp": {{1739354482884}},
  "version": 2,
  "type": "message-event",
  "payload": 
	{
    "id": "{{d04cc3a7-18f0-4571-831e-xxxxxxxx}}",
    "gsId": "{{7bf06899-5f0f-4cca-be3b-xxxxxxxxxx}}",
    "type": "sent",
    "destination": "{{79507xxxxxxxx}}",
    "payload": 
    {
      "ts": {{1739354482}}
    },
    "conversation": 
		{
      "id": "0f957b88cfb1558f6199exxxxxxxx",
      "expiresAt": 1747048500,
      "type": "marketing"
    },
    "pricing": 
		{
      "policy": "PMP",
      "category": "service",
      "type": "regular"
    }
  }
}
```

<br />

The **sent** event is received when the message is sent to the end-user.

**conversation** object description. Please note the conversation object is **optional**, and will be forwarded based on if Meta sends it to us.

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
        id
      </td>

      <td>
        Unique ID for a conversation.
      </td>

      <td>
        d04cc3a7-18f0-4571-831e-xxxxxxxx
      </td>
    </tr>

    <tr>
      <td>
        gsId
      </td>

      <td>
        Unique Gupshup identifier for a message
      </td>

      <td>
        7bf06899-5f0f-4cca-be3b-xxxxxxxxxx
      </td>
    </tr>

    <tr>
      <td>
        destination
      </td>

      <td>
        Phone number of the user engaged in the conversation.
      </td>

      <td>
        79507xxxxxxxx
      </td>
    </tr>

    <tr>
      <td>
        conversation\_id
      </td>

      <td>
        conversation id
      </td>

      <td>
        0f957b88cfb1558f6199exxxxxxxx
      </td>
    </tr>

    <tr>
      <td>
        expiresAt
      </td>

      <td>
        Conversation expiration timestamp in seconds
      </td>

      <td>
        1747048500
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        The type of conversation. Possible values:

        * marketing
        * marketing\_lite
        * utility
        * authentication
        * authentication\_international
        * service
        * referral\_conversion
      </td>

      <td>
        Marketing
      </td>
    </tr>
  </tbody>
</Table>

**pricing** object description

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
        policy
      </td>

      <td>
        The pricing policy applied for this message. Possible values of policy:

        * CBP
        * PMP
      </td>

      <td>
        PMP
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        The pricing category. Possible values:

        * marketing

        - marketing\_lite

        * utility
        * authentication
        * authentication\_international
        * service
        * referral\_conversion
      </td>

      <td>
        service
      </td>
    </tr>
  </tbody>
</Table>

## Delivered

> 📘 No change in delivered event payload