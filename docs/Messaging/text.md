---
title: Text
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
## User Sends You A Message

```json User Sends You A Message
{
  "app": "docdeck",
  "timestamp": 1718007189549,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD",
    "source": "91XXXXX4",
    "type": "text",
    "payload": {
      "text": "Hi"
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    }
  }
}
```

#### Common Payload Object Description

| Key         | Description                                                                       | Sample        |
| :---------- | :-------------------------------------------------------------------------------- | :------------ |
| `app`       | The name of the Gupshup app to which the customer has sent a message on WhatsApp  | docdeck       |
| `timestamp` | The time in UNIX timestamp when Gupshup received the message sent by the customer | 1718007189549 |
| `version`   | Callback payload version                                                          | 2             |
| `type`      | The type of inbound event                                                         | message       |

#### Message Payload Object Description

| Key       | Description                                                                                      | Sample                       |
| :-------- | :----------------------------------------------------------------------------------------------- | :--------------------------- |
| `id`      | The unique WhatsApp message identifier for the inbound message                                   | ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD |
| `source`  | The phone number of the customer who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4                     |
| `type`    | The type of message received from the end user.                                                  | text                         |
| `payload` | The payload object contains the inbound message content sent by the customer                     | Hi                           |

#### Sender Object Description

| Key            | Description                                                                                      | Sample   |
| :------------- | :----------------------------------------------------------------------------------------------- | :------- |
| `phone`        | The phone number of the end user who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4 |
| `name`         | Name of the end user who has sent the message on WhatsApp                                        | SJ       |
| `country_code` | The sender's country code                                                                        | 91       |
| `dial_code`    | The sender's dial code                                                                           | 9XXXXX4  |

## User Replies To Your Message

Users can respond to a specific message on WhatsApp. To understand the context of a message reply, we include the context object. The context object provides the Gupshup message-id(property: `gsId`) of the message the user has replied to and the WhatsApp message-id(property: `id`) of the original message.

```json Customer Replies To A Business Message
{
  "app": "docdeck",
  "timestamp": 1718007189549,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD",
    "source": "91XXXXX4",
    "type": "text",
    "payload": {
      "text": "Hi"
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    },
    "context": {
      "id": "gBEGkYaYVSEEAgnPFrOLcjkFjL8",
      "gsId": "9b71295f-f7af-4c1f-b2b4-31b4a4867bad"
    }
  }
}
```

#### Common Payload Object Description

| Key         | Description                                                                       | Sample        |
| :---------- | :-------------------------------------------------------------------------------- | :------------ |
| `app`       | The name of the Gupshup app to which the customer has sent a message on WhatsApp  | docdeck       |
| `timestamp` | The time in UNIX timestamp when Gupshup received the message sent by the customer | 1718007189549 |
| `version`   | Callback payload version                                                          | 2             |
| `type`      | The type of inbound event                                                         | message       |

#### Message Payload Object Description

| Key       | Description                                                                                      | Sample                       |
| :-------- | :----------------------------------------------------------------------------------------------- | :--------------------------- |
| `id`      | The unique WhatsApp message identifier for the inbound message                                   | ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD |
| `source`  | The phone number of the customer who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4                     |
| `type`    | The type of message received from the end user.                                                  | text                         |
| `payload` | The payload object contains the inbound message content sent by the customer                     | Hi                           |

#### Sender Object Description

| Key            | Description                                                                                      | Sample   |
| :------------- | :----------------------------------------------------------------------------------------------- | :------- |
| `phone`        | The phone number of the end user who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4 |
| `name`         | Name of the end user who has sent the message on WhatsApp                                        | SJ       |
| `country_code` | The sender's country code                                                                        | 91       |
| `dial_code`    | The sender's dial code                                                                           | 9XXXXX4  |

#### Context Object Description

| Key    | Description                                                    | Sample                               |
| :----- | :------------------------------------------------------------- | :----------------------------------- |
| `id`   | The unique WhatsApp message identifier for the inbound message | gBEGkYaYVSEEAgnPFrOLcjkFjL8          |
| `gsId` | The unique Gupshup message identifier for the inbound message  | 9b71295f-f7af-4c1f-b2b4-31b4a4867bad |

## User Clicks The Button On A Quick Reply Template Message

When your customer clicks on a quick reply button, a response goes to your Webhook URL.

To understand the context of a message reply, we include the context object. The context object provides the Gupshup message-id(property: `gsId`) of the message the user has replied to and the WhatsApp message-id(property: `id`) of the original message. In addition to this payload, the object provides the button text that the user clicked.

```json Customer Clicked On A Quick Reply Template Message Button
{
   "app": "docdeck",
  "timestamp": 1718007189549,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD",
    "source": "91XXXXX4",
    "type": "text",
    "payload": {
      "text": "View Account Balance", 
      "type": "button"
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    },
    "context": {
      "id": "gBEGkYaYVSEEAgnPFrOLcjkFjL8",
      "gsId": "9b71295f-f7af-4c1f-b2b4-31b4a4867bad"
    }
  }
}
```

#### Common Payload Object Description

| Key         | Description                                                                       | Sample        |
| :---------- | :-------------------------------------------------------------------------------- | :------------ |
| `app`       | The name of the Gupshup app to which the customer has sent a message on WhatsApp  | docdeck       |
| `timestamp` | The time in UNIX timestamp when Gupshup received the message sent by the customer | 1718007189549 |
| `version`   | Callback payload version                                                          | 2             |
| `type`      | The type of inbound event                                                         | message       |

#### Message Payload Object Description

| Key       | Description                                                                                      | Sample                       |
| :-------- | :----------------------------------------------------------------------------------------------- | :--------------------------- |
| `id`      | The unique WhatsApp message identifier for the inbound message                                   | ABEGkZUTIXZ0Ago6jWqOZm-Sz0WD |
| `source`  | The phone number of the customer who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4                     |
| `type`    | The type of message received from the end user.                                                  | text                         |
| `payload` | The payload object contains the inbound message content sent by the customer                     | View Account Balance         |
| `type`    | Button                                                                                           | button                       |

#### Sender Object Description

| Key            | Description                                                                                      | Sample   |
| :------------- | :----------------------------------------------------------------------------------------------- | :------- |
| `phone`        | The phone number of the end user who has sent the message on WhatsApp, number is in E.164 format | 91XXXXX4 |
| `name`         | Name of the end user who has sent the message on WhatsApp                                        | SJ       |
| `country_code` | The sender's country code                                                                        | 91       |
| `dial_code`    | The sender's dial code                                                                           | 9XXXXX4  |

#### Context Object Description

| Key    | Description                                                    | Sample                               |
| :----- | :------------------------------------------------------------- | :----------------------------------- |
| `id`   | The unique WhatsApp message identifier for the inbound message | gBEGkYaYVSEEAgnPFrOLcjkFjL8          |
| `gsId` | The unique Gupshup message identifier for the inbound message  | 9b71295f-f7af-4c1f-b2b4-31b4a4867bad |