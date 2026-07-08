---
title: Inbound Message
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## What Is an Inbound Message?

An inbound message is a mobile message triggered from our WhatsApp Self-Serve platform and routed to your callback URL.

For example, an inbound event is triggered when:

* You set a callback URL for your app or used the proxy command to invoke your app on the Gupshup Proxy bot phone number (+917834811114) to test the app in sandbox mode.
* An end-user consents (opt-in) to receive notifications from your WhatsApp Business API number.

> 📘
>
> You will receive inbound asynchronous message events on your callback URL with a 5-second delay to ensure that users have enough time to persist the original message-id received for an outbound message.

## Common Payload For All Inbound Events Of Type `Message`

This section explains the inbound event type `message` you receive on your callback URL. It states that a customer has sent a message to your WhatsApp Business API phone number. Here, we will understand the different types of payloads for inbound messages.

```json
{   
  "app": "DemoApp", 
  "timestamp": 1580227766370,   
  "version": 2, 
  "type": "message",    
  "payload": {  
    "id": "ABEGkYaYVSEEAhAL3SLAWwHKeKrt6s3FKB0c",   
    "source": "918x98xx21x4",   
    "type": "text"|"image"|"file"|"audio"|"video"|"contact"|"location"|"button_reply"|"list_reply", 
    "payload": {    
      // Varies according to the type of payload.    
    },  
    "sender": { 
      "phone": "918x98xx21x4",  
      "name": "Drew",   
      "country_code": "91", 
      "dial_code": "8x98xx21x4" 
    },  
    "context": {    
      "id": "gBEGkYaYVSEEAgnPFrOLcjkFjL8",  
      "gsId": "9b71295f-f7af-4c1f-b2b4-31b4a4867bad"    
    }   
  } 
}
```

### Common Payload Object Description

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
        Sample
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `app`
      </td>

      <td>
        The name of the Gupshup app to which the customer has sent a message on WhatsApp
      </td>

      <td>
        DemoAPI
      </td>
    </tr>

    <tr>
      <td>
        `timestamp`
      </td>

      <td>
        The time in UNIX timestamp when Gupshup received the message sent by the customer
      </td>

      <td>
        1584898839530
      </td>
    </tr>

    <tr>
      <td>
        `version`
      </td>

      <td>
        Callback payload version
      </td>

      <td>
        2
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        The type of inbound event
      </td>

      <td>
        `message`
      </td>
    </tr>

    <tr>
      <td>
        `payload`
      </td>

      <td>
        The payload object represents the following:

        * WhatsApp message ID
        * Sender's phone number along with their country code
        * The type of message
        * Content of the message
      </td>

      <td>
        See [the payload object description](https://partner-docs.gupshup.io/update/docs/inbound-message-events#/) for more information.
      </td>
    </tr>

    <tr>
      <td>
        `sender`
      </td>

      <td>
        The sender object represents the following:\
        Name of the sender
        Phone number of the sender
      </td>

      <td>
        See [the sender object description](https://partner-docs.gupshup.io/docs/inbound-message-events#/sender-object-description) for more information.
      </td>
    </tr>

    <tr>
      <td>
        `context`
      </td>

      <td>
        The context object is **optional**, it will only be included when someone replies to one of your messages. It contains information about the content of the original message, such as the Gupshup ID and WhatsApp ID of the message.
      </td>

      <td>
        See [the context object description](https://partner-docs.gupshup.io/docs/inbound-message-events#/context-object-description) for more information.
      </td>
    </tr>
  </tbody>
</Table>

#### Payload Object Description

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
        Sample
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        The unique WhatsApp message identifier for the inbound message
      </td>

      <td>
        ABEGkYaYVSEEAhAt2MgAKjL1qGe88OKyMQfM
      </td>
    </tr>

    <tr>
      <td>
        `source`
      </td>

      <td>
        The phone number of the customer who has sent the message on WhatsApp, number is in E.164 format
      </td>

      <td>
        918x98xx21x4
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        The type of message received from the end user. Depending on 'type', the relevant message object will be received as part of the payload.

        Must be one of these: `text`, `image`, `file`, `audio`, `video`, `contact`, and `location`.
      </td>

      <td>
        `text`
      </td>
    </tr>

    <tr>
      <td>
        `payload`
      </td>

      <td>
        The payload object contains the inbound message content sent by the customer
      </td>

      <td>
        See the types of incoming message received documentation below
      </td>
    </tr>
  </tbody>
</Table>

#### Sender Object Description

| Key            | Description                                                                                      | Sample       |
| :------------- | :----------------------------------------------------------------------------------------------- | :----------- |
| `phone`        | The phone number of the end user who has sent the message on WhatsApp, number is in E.164 format | 918x98xx21x4 |
| `name`         | Name of the end user who has sent the message on WhatsApp                                        | Daniel       |
| `country_code` | The sender's country code                                                                        | 91           |
| `dial_code`    | The sender's dial code                                                                           | 8x98xx21x4   |

#### Context Object Description

| Key    | Description                                                    | Sample                               |
| :----- | :------------------------------------------------------------- | :----------------------------------- |
| `id`   | The unique WhatsApp message identifier for the inbound message | gBEGkYaYVSEEAgnPFrOLcjkFjL8          |
| `gsId` | The unique Gupshup message identifier for the inbound message  | 9b71295f-f7af-4c1f-b2b4-31b4a4867bad |