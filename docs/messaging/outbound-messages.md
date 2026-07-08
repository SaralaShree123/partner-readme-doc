---
summary: Outbound messages
title: Outbound messages
deprecated: false
hidden: true
metadata:
  robots: index
---
Outbound messages are messages you send to your users. Outbound messages are classified into two types:**Template messages** and **Session messages**.  Here we will look at the different types of outbound messages you can send using Gupshup's API

## Session messaging

You can send Session messages to Active users only. When a user sends a message to your WhatsApp Business API, they become an active user. A session starts from the latest user message. Sessions remain Active for 24 hours.

You can use our [send message API](https://docs.gupshup.io/reference/msg) for sending session messages

## Template messaging

Template messages are Highly Structured(HSM)/ Notification messages. Once your WhatsApp Business API is Live, you can create template messages and submit them to WhatsApp for approval. You can send Template messages to users that you have opted-in. To know how you can opt-in users, read [frequently asked questions](https://support.gupshup.io/hc/en-us/articles/360012075919-How-do-I-opt-in-users).