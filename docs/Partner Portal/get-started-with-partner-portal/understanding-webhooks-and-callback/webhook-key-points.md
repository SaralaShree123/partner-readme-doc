---
title: Webhook Key Points
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
A webhook is an HTTP/HTTPS callback triggered by a user-defined event at the originating site. In its simplest form, a webhook is a web service that receives HTTPS POST requests from a source.

Webhooks manage incoming messages from WhatsApp users, including text, location, and media such as photos and documents, as well as the status of messages you've sent. Webhooks provide both timely notifications and out-of-band issues, thus establishing one in the application settings is strongly recommended.

Customers' messages sent to your WhatsApp Business Phone Number are routed to your Webhook. When a client sends a text message or a media attachment to your WhatsApp Business, the platform logs the message and sends a notice (HTTPS POST request) to the Webhook defined in your app's settings.

## Webhook Key Points

Before configuring your first webhook/ callback URL, you must know its key points.

* The webhook should return **HTTP\_SUCCESS** (code: 2xx) with an empty response.

> 📘
>
> Failing to do so within 10 seconds, our platform will consider that the notification has failed and attempt again after a brief interval.

* Your webhook should process inbound messages & events asynchronously but acknowledge its reception synchronously & instantly.

> 📘
>
> The optimal acknowledgment time is less than 100 milliseconds; nevertheless, we recognize that network delays might occur, hence 500-1000 milliseconds is the recommended acknowledgment time. The longer your response time, the more inbound messages and events will be delayed each time.

* The webhook should accept the HTTP header: **User-Agent**.
* The webhook should accept user events: **sandbox-start**.
* The webhook should have public access.

> 🚧
>
> You can whitelist Gupshup's inbound request IPs as a security measure. Not only it will keep it private but also eradicate security vulnerabilities.
>
> Drop an email to: [devsupport@gupshup.io](mailto:devsupport@gupshup.io) to connect with our support team to get these IPs.