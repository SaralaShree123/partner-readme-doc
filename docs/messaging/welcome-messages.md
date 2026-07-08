---
summary: Welcome Messages
title: Welcome Messages
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
The Welcome Message feature is an integral part of the Conversational Components developed by Meta. It serves the purpose of greeting first-time users with a welcoming message. These Conversational Components are in-chat features designed to enhance user interaction with your business.

<Image align="center" width="500px" src="https://files.readme.io/336fd8b-welome_message.png" />

## Activation Process

### Obtain WABA ID

1. Log in to your Gupshup account and select your App name.
2. Within the **Settings** tab, locate your WABA ID.

   <Image alt="Collecting WABA ID" align="center" border={true} src="https://files.readme.io/164314e-Screenshot_2024-05-16_at_11.26.46_AM.png">
     Collecting WABA ID
   </Image>

### Enabling the Welcome Message Feature

1. Log in to your **Facebook Business Manager** account.

2. Navigate to **Accounts > WhatsApp accounts** and search for your WABA ID.

3. Select the **WhatsApp Manager**.

   <Image alt="Click on the WhatsApp Manager" align="center" border={true} src="https://files.readme.io/b1fe5cf-Screenshot_2024-05-16_at_11.30.51_AM.png">
     Selecting WhatsApp Manager
   </Image>

4. Within the **WhatsApp Manager**, go to **Account tools > Phone numbers** and locate the desired phone number.

5. Click on the **Settings** icon adjacent to your phone number.

6. Proceed to **Automations** and locate **Welcome messages** on the right-hand side panel.

7. By default, the feature is disabled. Toggle the switch to enable it.

   <Image alt="Turn ON Welcome messages" align="center" border={true} src="https://files.readme.io/29942a9-Screenshot_2024-05-16_at_11.33.12_AM.png">
     Turn ON welcome messages
   </Image>

> 📘
>
> Enabling this feature initiates a process where Meta checks for any prior message threads between the user and your business phone number. If no such thread exists, it activates a `messages` webhook with `type` set to `request_welcome`. This webhook can be utilized to craft and send your personalized welcome message to the user.

## Webhook Payload

```json v2 Payload
{
    "app": "<APP_NAME>",
    "phone": "<APP_PHONE_NUMBER>",
    "timestamp": 1712046854895,
    "version": 2,
    "type": "message",
    "payload": {
        "id": "<MESSAGE_ID>",
        "source": "<PHONE_NUMBER>",
        "type": "request_welcome",
        "sender": {
            "phone": "<SENDER_PHONE_NUMBER>",
            "name": "<SENDER_NAME>",
            "country_code": "<SENDER_COUNTRY_CODE>",
            "dial_code": "<SENDER_DIAL_CODE>"
        }
    }
}
```

## Testing

To test out the configured conversational feature, launch the WhatsApp app and initiate a chat with your designated business phone number.

Before proceeding with welcome messages, ensure there's no existing chat thread with the business number by following these steps:

1. Open the existing chat thread in your WhatsApp client.
2. Tap on the profile of the business phone number.
3. Select Clear **Chat followed** by **Clear All Messages**.
4. Return to the now empty chat thread.

Once the chat thread is cleared, you can proceed to send a message to the business phone number. This action should trigger the `request_welcome` webhook, allowing you to evaluate the functionality seamlessly.
