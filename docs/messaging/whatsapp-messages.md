---
summary: WhatsApp Messages
title: WhatsApp Messages
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
This guide provides an overview of how messages work on the WhatsApp Business Platform.

You can send the following message types using the platform:

* Text messages
* Media messages: image, video, audio, document, and sticker messages.
* Contact messages
* Location messages
* Interactive messages: List messages, Reply button messages, and Single and Multi Product Messages.
* Template messages

## Conversations

Conversations are 24-hour message threads between you and your customers and are the basis for pricing. Conversations can be opened by sending either free-form messages or template messages. See Pricing to see how conversations are opened and closed, and how they factor into our pricing model.

## Scaling Conversations

To learn how to increase the number of conversations you can open in a 24-hour window, see [Messaging Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits).

## Message Status

For each message you send, a notification about the status of the message will be sent to your webhook callback. In the table below, click the arrow in the left column for the WhatsApp app equivalent to each status, if available.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Name
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        deleted
      </td>

      <td style={{ textAlign: "left" }}>
        A message sent by the customer was deleted by the customer. Upon receiving this notification, you should ensure that the message is deleted from your system if it was downloaded from the server.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        delivered
      </td>

      <td style={{ textAlign: "left" }}>
        A message sent by you was delivered to the customer's device.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        failed
      </td>

      <td style={{ textAlign: "left" }}>
        A message sent by you failed to send. A reason for the failure will be included in the callback.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        read
      </td>

      <td style={{ textAlign: "left" }}>
        A message sent by you was read by the customer. read notifications are only available for customers that have read receipts enabled. For customers that do not have it enabled, you only receive the delivered notification.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        sent
      </td>

      <td style={{ textAlign: "left" }}>
        A message you sent is in transit within our systems.  

        For On-Premises API users: To receive notifications for sent messages, set the sent\_status setting to true in the application settings. The sent status notification is disabled by default.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        warning
      </td>

      <td style={{ textAlign: "left" }}>
        A message you sent contains an item in a catalog that is not available or does not exist.
      </td>
    </tr>
  </tbody>
</Table>

The order of these notifications in your app may not reflect the actual timing of the message status. View the timestamp to determine the timing, if necessary.
