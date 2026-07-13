---
title: Send your first message
icon: fa-duotone fa-paper-plane
summary: Send your first WhatsApp message using the Partner API.
excerpt: Send your first WhatsApp message using the Partner API.
deprecated: false
hidden: false
metadata:
  robots: index
slug: send-your-first-message
---

# Send your first message

## Prerequisites

- Partner token from [Generate Secret and Token](/docs/generate-secret-and-token)
- Live app with approved template (for business-initiated messages outside 24-hour window)

## Steps

### 1. Choose message type

| Type | When to use | Guide |
|------|-------------|-------|
| Template message | Outside 24-hour window | [Templates Management](/reference/templates-management) |
| Session message | Within 24-hour window | [Messaging (V3)](/reference/messaging-v3) |

### 2. Send a template message

Use [Send msg With Template ID](/reference/post_partner-app-appid-template-msg) or see [Send Template Message Examples](/reference/send-message-examples).

### 3. Send a session message

Use [Text Message (V3)](/reference/post_partner-app-appid-v3-text-message).

### 4. Verify delivery

Configure [webhooks](/docs/webhooks-and-callback) to receive message and delivery status notifications.

## Learn more

- [WhatsApp Messages](/docs/whatsapp-messages) — Full messaging concepts and message types
- [Message events](/docs/message-events) — Delivery status webhook events

## You are integrated!

Continue with [Onboarding](/docs/onboarding-overview) and the full [API Reference](/reference/partner-api-overview).
