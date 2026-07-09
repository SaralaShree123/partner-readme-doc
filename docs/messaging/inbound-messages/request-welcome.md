---
summary: Request Welcome
title: Request Welcome
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
Businesses can be notified by a webhook whenever a WhatsApp user opens a chat with you for the first time. This can be useful if you want to reply to these users with a special welcome message of your design.

Welcome Messages are great for service interactions, such as customer support or account servicing. For example, you can embed a WhatsApp button on your app or website. When users tap the button, they will be redirected to WhatsApp where they will receive a welcome message that provides context on how they can interact with you.

<Image align="center" alt="Preview of a Welcome Message" border={true} caption="Preview of a Welcome Message" src="https://files.readme.io/d107677-Screenshot_2024-05-14_at_5.20.48_PM.png" width="60% " />

## User receives your welcome message

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

### Other Reference

Welcome Messages is a subset of the Conversational Components. Dive into the specifics by visiting Conversational Components: Welcome Messages for a comprehensive overview.
