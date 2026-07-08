---
summary: Bot Testing
title: Bot Testing
deprecated: false
hidden: true
metadata:
  robots: index
---
this is a testing page for automation agent

<br />

## Carousel Message Examples

Carousel messages allow you to send a horizontally scrollable set of cards, each containing rich media, text, and interactive buttons. This format is ideal for showcasing multiple products, services, or options in a single message.

> 1. Messages must include between 2 and 10 cards.
> 2. Main message body text is required.
> 3. Main message headers, footers, and interactive components are not supported.
> 4. Cards must include either an image or video header. Other header types are not supported.
> 5. Card body text is optional.
> 6. Cards must include either one URL button, or one or more quick-reply buttons. Button types and numbers must match across all cards (for example, if you define a card with 2 quick-reply buttons, all cards must define exactly 2 quick-reply buttons).

## Request Parameters

| Key | Description | Values | Data Type | Required/Optional | Constraints |
|-----|-------------|--------|-----------|-------------------|-------------|
| **Headers** | | | | | |
| Authorisation | Access Token for the application | sk_8eb35b1f81c24af2xxxxxx | String | Required | Should be a valid Partner App Access Token. |
| **Path Params** | | | | | |
| App Id | App ID to fetch the access token | bf9ee64c-3d4d-4ac4-xxxx-732e577007c4 | String | Required | The Id should be a valid app Id of Gupshup |
| **Body JSON** | | | | | |
| messaging_product | Messaging product | whatsapp | String | Required | |
| recipient_type | Recipient type | individual | String | Required | |
| to | Destination phone no where the message need to be send | 91785876xxxx | String | Required | Must be a valid phone number. |
| type | Messaging type | interactive | String | Required | Type should be interactive to send interactive message. |
| interactive | interactive message inside body | See example below | Object | Required | Must contain carousel configuration with cards array |

### Interactive Object Example

```json
"interactive": {
    "type": "carousel",
    "body": {
      "text": "Check out our latest offers!"
    },
    "action": {
      "cards": [
        {
          "card_index": 0,
          "type": "cta_url",
          "header": {
            "type": "image",
            "image": {
              "link": "https://gs-upload.gupshup.io/whatsapp/sample-media/png/sample01.png"
            }
          },
          "body": {
            "text": "Product 1"
          },
          "buttons": [
            {
              "type": "url",
              "title": "View Details",
              "url": "https://example.com/product1"
            }
          ]
        }
      ]
    }
  }
```