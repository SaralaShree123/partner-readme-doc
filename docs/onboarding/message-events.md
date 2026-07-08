---
summary: Message events
title: Message events
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
These events state the status of the message sent using the send message API to the WhatsApp API client (which essentially sends out a message to the customer). The WhatsApp Business API client will send notifications to inform you of the status of the messages between you and users. When you send a message successfully, you will receive a notification on your callback URL stating when the message was sent, delivered, and read. The order of these notifications in your app may not reflect the actual timing of the message status. View the timestamp to determine the timing, if necessary. The notifications you may receive are:

```json message-event
{
   "app":"DemoAPI",
   "timestamp":1580546677791,
   "version":2,
   "type":"message-event",
   "payload":{
      "id":"59f8db90-c37e-4408-90ab-cc54ef8246ad"(Gupshup Message ID)|"gBEGkYaYVSEEAgnZxQ3JmKK6Wvg" (WhatsApp Message ID)
      "gsId": "ee4a68a0-1203-4c85-8dc3-49d0b3226a35" (Gupshup Message ID - This property is only applicable for DLR events)
      "type":"enqueued"|"failed"|"sent"|"delivered"|"read|"deleted"",
      "destination":"91XX985XX10X",
      "payload": ## This varies according to 'type' property value
   }
}
```

> 📘
>
> Events received after a week of sending the message will not have the GSID available in the notification payload.

## Common payload object description

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
        This is Gupshup Message Id for message-event types: `enqueued` and `failed`
        In case of `failed` please check the below [Sync](https://partner-docs.gupshup.io/docs/message-events#/sync-failed) and [Async](https://partner-docs.gupshup.io/docs/message-events#/async-failed) section.
        For the DLR events `sent`, `delivered`, `read` it is always WhatsApp Message ID.
      </td>

      <td>
        `59f8db90-c37e-4408-90ab-cc54ef8246ad`
        OR
        `gBEGkYaYVSEEAgnZxQ3JmKK6Wvg`
      </td>
    </tr>

    <tr>
      <td>
        `gsId`
      </td>

      <td>
        This is Gupshup Message Id and only present for message-event types: DLR events: `sent`, `delivered`, `read`.
      </td>

      <td>
        `59f8db90-c37e-4408-90ab-cc54ef8246ad`
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        The type of message-event received on your webhook
        Must be one of these: `enqueued`, `failed`, `sent`, `delivered`, `read`.
      </td>

      <td>
        Refer to the description given below.
      </td>
    </tr>

    <tr>
      <td>
        `destination`
      </td>

      <td>
        User's phone number
      </td>

      <td>
        918x98xx21x4
      </td>
    </tr>

    <tr>
      <td>
        `ts`
      </td>

      <td>
        Timestamp sent by Meta. This property is received for events `sent`, `delivered`, and `read`.
      </td>

      <td>
        1585344475
      </td>
    </tr>

    <tr>
      <td>
        `timestamp`
      </td>

      <td>
        The time when Gupshup generated the event.
      </td>

      <td>
        1580546677791
      </td>
    </tr>
  </tbody>
</Table>

## Types of message events

```json enqueued
{
  "app": "DemoAPI",
  "timestamp": 1580546677791,
  "version": 2,
  "type": "message-event",
  "payload": {
    "id": "59f8db90-c37e-4408-90ab-cc54ef8246ad",
    "type": "enqueued",
    "destination": "91XX985XX10X",
    "payload": {
      "whatsappMessageId": "gBEGkYaYVSEEAgkD7bRi9syGnBk",
      "type": "session"
    }
  }
}
```
```json sync- failed
{
    "app": "DemoAPI",
    "timestamp": 1580311136040,
    "version": 2,
    "type": "message-event",
    "payload": {
        "id": "ee4a68a0-1203-4c85-8dc3-49d0b3226a35",
        "type": "failed",
        "destination": "918x98xx21x4",
        "payload": {
            "code": 1008,
            "reason": "User is not Opted in and Inactive"
        }
    }
}
```
```json async- failed
{
    "app": "DemoAPI",
    "timestamp": 1663138637856,
    "version": 2,
    "type": "message-event",
    "payload": {
        "id": "9163a016-710e-41ee-978b-79a1adbd734e",
        "gsId": "72f61f22-5aa4-4615-a970-943edf6da01c",
        "type": "failed",
        "destination": "918x98xx21x4",
        "payload": {
            "code": 470,
            "reason": "Message failed to send because more than 24 hours have passed since the customer last replied to this number"
        }
    }
}
```
```Text sent
{
	"app": "{{APP_NAME}}",
	"phone": "{{APP_PHONE}}",
	"timestamp": {{TIMESTAMP}},
	"version": 2,
	"type": "message-event",
	"payload": 
	{
		"id": "{{WA_MESSAGE_ID}}",
		"gsId": "{{GS_MESSAGE_ID}}",
		"type": "sent",
		"destination": "{{DESTINATION}}",
		"payload": 
    {
			"ts": {{META_TS}}
		},
	"conversation": 
  	{
			"id": "{{CONVERSATION_ID}}",
			"expiresAt": {{CONVERSATION_EXPIRY}},
			"type": "service"
		},
		"pricing": 
  	{
			"policy": "CBP",
			"category": "service"
		}
	}
}
```
```json delivered
{
	"app": "2GvVby7hAeoXOig4Zt24htQn",
	"phone": "917065917373",
	"timestamp": 1747136693404,
	"version": 2,
	"type": "message-event",
	"payload": 
  {
		"id": "326822fd-55e9-4112-b810-e86909cd71f6",
		"gsId": "1a6207e5-af37-4fc8-948a-25867d3ab077",
		"type": "delivered",
		"destination": "917980890978",
		"payload": 
		{
			"ts": 1747136691
		}
	}
}
```
```json read
{
  "app": "DemoAPI",
  "timestamp": 1585344602933,
  "version": 2,
  "type": "message-event",
  "payload": {
    "id": "gBEGkYaYVSEEAgnZxQ3JmKK6Wvg",
    "gsId": "ee4a68a0-1203-4c85-8dc3-49d0b3226a35",
    "type": "read",
    "destination": "918x98xx21x4",
    "payload": {
      "ts": 1585344602
    }
  }
}
```
```json deleted
{
  "app": "demoapp",
  "timestamp": 1654703394680,
  "version": 2,
  "type": "message-event",
  "payload": {
    "id": "ABEGkZhngpgo-sJRwQ6dszYhU",
    "type": "deleted",
    "destination": "919867XX9135",
    "payload": {
      "ts": 1654703389
    }
  }
}
```
```json Referral(CTX)
{
  "messages": [
    {
      "referral": {
        "source_url": "https://fb.me/3tkSI06bP",
        "source_id": "6570618339781",
        "source_type": "ad",
        "body": "WhatsApp Messenger: More than 2 billion people in over 180 countries use WhatsApp to stay in touch with friends and family, anytime and anywhere. WhatsApp is free and offers simple, secure, reliable messaging and calling, available on phones all over the world.",
        "headline": "Chat with us",
        "media_type": "image",
        "image_url": "https://scontent.xx.fbcdn.net/v/t45.1600-4/355945306_6362276590981_9061280892424810783_n.jpg?stp=c3.122.300.300a_dst-jpg_p306x306&_nc_cat=103&ccb=1-7&_nc_sid=567a6d&_nc_ohc=pYcuA_DcMeUAb4eCSRW&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=00_AfAqx_EFyDb1elHBHbjofACWwoxSytEJt2Aeu5vEyWOdQA&oe=66147417",
        "ctwa_clid": "ARAHuTtGzmFlOO_WcXezfYBRzrxoH2Emo4kj-mXVvHoMQVU748gp6Sp-IKS2_scLmfnBJSWvvsZpVqjJfMQPM6TJy1_dNFC1ZUztlDk4i1RijetS"
      },
      "from": "918871601297",
      "id": "wamid.HBgMOTE4ODcxNjAxMjk3FQIAEhgUM0FEOUJDNjc1NDJGMUNEMUNFMDEA",
      "timestamp": "1712229906",
      "text": {
        "body": "Hello! Can I get more info on this?"
      },
      "type": "text"
    }
  ],
  "contacts": [
    {
      "profile": {
        "name": "Niiiishh"
      },
      "wa_id": "918871601297"
    }
  ]
}
```

### Enqueued

This event is received when a message is successfully sent to the WhatsApp Business API client(docker).

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
        `whatsappMessageId`
      </td>

      <td>
        The WhatsApp message id generated while sending a message to an end-user on WhatsApp
      </td>

      <td>
        gBEGkYaYVSEEA
        gkD7bRi9syGnBk
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        Indicates the type of message

        See [different types of messages you can send to users](https://docs.gupshup.io/docs/outbound-messages).
      </td>

      <td>
        session
      </td>
    </tr>
  </tbody>
</Table>

### Sync Failed

This event is received when the message sending has failed. You will receive the reason for failure on your callback URL

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
        `code`
      </td>

      <td>
        The failure/exception code
      </td>

      <td>
        1002
      </td>
    </tr>

    <tr>
      <td>
        `reason`
      </td>

      <td>
        Message failure reason with respect to the error code.

        See [error and status messages](https://partner-docs.gupshup.io/docs/error-codes#/).
      </td>

      <td>
        Number Does Not Exist On WhatsApp
      </td>
    </tr>

    <tr>
      <td>
        `id`
      </td>

      <td>
        id is Gupshup Message ID
      </td>

      <td>
        ee4a68a0-1203-4c85-8dc3-49d0b3226a35
      </td>
    </tr>
  </tbody>
</Table>

### Async Failed

This event is received when messages have been failed by Whatsapp docker.

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
        `code`
      </td>

      <td>
        The failure/exception code
      </td>

      <td>
        1002
      </td>
    </tr>

    <tr>
      <td>
        `reason`
      </td>

      <td>
        Message failure reason with respect to the error code.

        See [error and status messages](https://partner-docs.gupshup.io/docs/error-codes#/).
      </td>

      <td>
        Number Does Not Exists On WhatsApp
      </td>
    </tr>

    <tr>
      <td>
        `gsId`
      </td>

      <td>
        gsId is Gupshup Message ID
      </td>

      <td>
        72f61f22-5aa4-4615-a970-943edf6da01c
      </td>
    </tr>
  </tbody>
</Table>

### Sent

The `sent` event is received when the message is sent to the end-user.

`conversation` object description

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
        Unique ID for a conversation.
      </td>

      <td>
        532b57b5f6e63595ccd74c6010e5c5c7
      </td>
    </tr>

    <tr>
      <td>
        `expiresAt`
      </td>

      <td>
        Conversation expiration timestamp in seconds
      </td>

      <td>
        1518780636
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        The type of conversation. Possible values:

        * FEP (Free entry point)
        * Marketing
        * Marketing Lite
        * Authentication
        * Utility Service
      </td>

      <td>
        Marketing
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
  </tbody>
</Table>

`pricing` object description

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
        `policy`
      </td>

      <td>
        The pricing policy applied for this message. Possible values:

        * CBP (Conversation based pricing)
        * NBP (Notification based pricing)
      </td>

      <td>
        CBP
      </td>
    </tr>

    <tr>
      <td>
        `category`
      </td>

      <td>
        The pricing category. Possible values:

        * FEP
        * Marketing
        * Utility
        * Authentication
        * Service
      </td>

      <td>
        Marketing
      </td>
    </tr>
  </tbody>
</Table>

### Delivered

This event is received when the message sent by your business was delivered to the user's device.

### Read

The `read` event is received when the message sent by your business is read by the user. Read notifications will only be available for users who have read receipts enabled. For users that do not have it enabled, you will only receive the delivered notification.

For status to be read, it must have been delivered. In some scenarios, such as when a user is on the chat screen and a message arrives, the message is delivered and read almost simultaneously. In this or other similar scenarios, the given notification will not be sent back, as it is implied that a message has been delivered if it has been read.

### Delete

\[No longer supported by Meta] The `delete` event is received when a user deletes a message for everyone (not 'delete for me') which they have sent to your WhatsApp Business API.

### Others

`Other` events are miscellaneous events received asynchronously on your callback. These are ad hoc events received from your WABAs docker.

### Mismatch

This event is only triggered when the destination number provided in the API request does not match the WhatsApp ID. The mismatch event does not require a subscription and will help you manage user conversations more effectively. Learn more about the [mismatch event](https://support.gupshup.io/hc/es-co/articles/4413210201625).

| Key     | Description                              | Example       |
| :------ | :--------------------------------------- | :------------ |
| `wa_id` | WhatsApp ID of the destination number    | 5593587654321 |
| `phone` | Dialable number/given destination number | 553587654321  |

### Referral (CTX)

| Key                | Description                                                                                                                   | Example                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **source\_url**    | The Meta URL that leads to the ad or post clicked by the customer. Accessing this URL displays the ad viewed by the customer. | `"https://www.meta.com/ad/12345"`               |
| **source\_type**   | Specifies the type of source for the ad; it can either be an `ad` or a `post`.                                                | `"ad"`                                          |
| **source\_id**     | The Meta ID for the ad or post.                                                                                               | `"1234567890"`                                  |
| **headline**       | The headline used in the ad or post.                                                                                          | `"Get 20% off on your first order!"`            |
| **body**           | The body text for the ad or post.                                                                                             | `"Shop now and save on your favorite items."`   |
| **media\_type**    | Specifies the type of media present in the ad or post. Possible values are `image` or `video`.                                | `"image"`                                       |
| **image\_url**     | The URL of the image used in the ad, applicable when `media_type` is `image`.                                                 | `"https://www.meta.com/ad/12345/image.jpg"`     |
| **video\_url**     | The URL of the video used in the ad, applicable when `media_type` is `video`.                                                 | `"https://www.meta.com/ad/12345/video.mp4"`     |
| **thumbnail\_url** | The URL of the thumbnail for the video, applicable when `media_type` is `video`.                                              | `"https://www.meta.com/ad/12345/thumbnail.jpg"` |
| **ctwa\_clid**     | The Click ID generated by Meta for ads that redirect to WhatsApp.                                                             | `"abc123xyz456"`                                |

#### Supported Message Types

The `referral` object can be included in the following types of messages:

* `text`, `location`, `contact`, `image`, `video`, `document`, `voice`, and `sticker`.