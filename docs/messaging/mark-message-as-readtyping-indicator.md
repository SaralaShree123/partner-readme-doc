---
summary: >-
title: Mark message as Read/Typing indicator
excerpt: >-
  Typing indicators enhance the messaging experience by signaling to the
  WhatsApp user that a response is being prepared. This feature builds user
  trust and improves perceived responsiveness . 
deprecated: false
hidden: false
metadata:
  robots: index
---
### This guide explains how and when to use typing indicators effectively using the WhatsApp Business API.

![](https://files.readme.io/2dc21af46982370c4edf4ef9346574af6c35d7d2a44eb1c9f4098d7422fe1960-image.png)

***

## How Typing Indicators Work

### When your system receives an incoming message via the messages webhook, the payload will contain a unique message.id. You can use this ID to:

* **Mark the message as read**, and
* **Send a typing indicator**, showing that you’re preparing a response.

> 📘 You can use this partner <Anchor label="API" target="_blank" href="/reference/voicecallaction-1#/">API</Anchor> to mark the message as read and send typing indicators for a message ID.

***

## Duration of Typing Indicator

* The typing indicator is automatically dismissed in either of the following cases:
  * When the response message is sent
  * Or after 25 seconds, whichever is earlier

***

## Things to Avoid

* Don’t spam the user with typing indicators.
* Don’t trigger typing if the delay is negligible (\<1s).

***

## Summary

Typing indicators are a subtle but powerful UX tool. Use them wisely to keep users engaged and informed, especially when your system needs a moment before replying.

***