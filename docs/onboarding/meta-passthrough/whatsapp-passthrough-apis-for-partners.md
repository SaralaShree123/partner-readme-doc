---
summary: Whatsapp Passthrough APIs for Partners
title: Whatsapp Passthrough APIs for Partners
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
> 📘 The feature is currently in beta mode and is only available to select partners.

# Introduction

Today, all the partners of Gupshup use the Gupshup-specific format APIs to send outgoing messages on WhatsApp to their end clients. We currently support two different versions (v1 and v2) of these APIs which are commonly used by the partners.

These APIs need regular maintenance and changes whenever Meta launches a new feature. This impacts sending a message such as a new template type or a new field in the existing payload. Also, many of our partners come from different BSPs who might already be on Meta-specific format for sending a message and hence it becomes difficult for partners to migrate from a different BSP to Gupshup without too many changes on their side.

Hence, Gupshup has now invested in building raw passthrough APIs which will imitate Meta’s format to ensure new features are rolled out faster and facilitate seamless migration of our partners from other BSPs.

# Objective

1. To allow our existing and new partners to send business messages via a new API which imitates the Meta send message format for various types of templates or session messages.
2. To allow our existing and new partners to set new callback subscriptions for supporting raw incoming messages and other events

# Scope

1. Sending a template message in Meta format.
2. Sending a non-template message in Meta format.
3. Receiving incoming messages and events on a new subscription webhook.
4. Support both prepaid and postpaid billing.
5. Support for media messages.

**Note**: Creation or Management of templates in Meta format is out of scope in the current release.

# Pre-requisites

1. Apps should be on Meta Cloud.
2. A new v3 callback subscription is mandatory to receive incoming events in Meta format.

# Impact on existing partners

Existing partners who are using our existing v1 or v2 APIs can also migrate to the new passthrough APIs or can choose to work with both the existing and new APIs in parallel.

All the existing APIs will work with the existing subscriptions and newer APIs will require new v3 subscriptions.

# Limitations

1. Template matching or Optin checks are not performed.
2. Creation of templates in Meta format not supported through these APIs.
3. Not available on the UI.
4. If a customer has subscribed to both v2 and v3 (passthrough) callback subscriptions for incoming messages and events, they will get such events on both callbacks. Customers have to handle the deduplication logic at their end.

# Implementation

To consume the passthrough send message APIs, the following steps should have been completed:-

1. Onboarding on the partner portal to get a [partner token](/reference/post_partner-account-login#/)
2. Create an account on gupshup.io to get an API key and a wallet
3. If the partner is on the prepaid model, contact support to convert the wallet to a postpaid
4. If the WABA onboarding is through gupshup.io UI
   1. Use the below APIs to start sending messages after WABA is live.

# Outgoing Session Message

1. **Address**: Address messages give your users a simpler way to share the shipping address with the business on WhatsApp. Read how to send [address](/reference/post_partner-app-appid-v3-address-message-2#/) as a session message.
2. **Audio**: Displays an audio icon, and when the WhatsApp user taps it, the audio file plays. Read how to send [audio](/reference/post_partner-app-appid-v3-audio-message-6#/) as a session message.
3. **Contact**: The user can now send rich contact information directly to WhatsApp users, such as names, phone numbers, physical addresses, and email addresses. Read how to send [contact](/reference/post_partner-app-appid-v3-contact-message-6#/) as a session message.
4. **Flow**: The user can send a flow message after creating a WhatsApp flow.  Read how to send a  [flow](/reference/post_partner-app-appid-v3-flow-message-6#/) as a session message.
5. **Image**: Displays a single image with a caption (optional).  Read how to send  [image](/reference/post_partner-app-appid-v3-image-message#/) as a session message.
6. **Interactive**: To communicate with WhatsApp users and send messages.  Read how to send [interactive](/reference/post_partner-app-appid-v3-interactive-message#/) as a session message.
7. **Reaction**: This feature allows WhatsApp users to respond quickly and visually to messages with emoji reactions.  Read how to send [reaction](/reference/post_partner-app-appid-v3-reaction-message#/) as a session message.
8. **Sticker**: Sticker messages, which display animated or static sticker images, add a fun and expressive element to WhatsApp messages.  Read how to send [sticker](/reference/post_partner-app-appid-v3-sticker-message#/) as a message.
9. **Text**: The text messages contain only a text body and an optional link preview. These messages are widely used for personal and business communication for quick delivery.  Read how to send [text](/reference/post_partner-app-appid-v3-text-message#/) as a session message.
10. **Video**: Display a thumbnail preview of a video message with a caption (optional) on WhatsApp.  When the user taps on the preview, the video loads and plays, providing an immediate viewing experience.  Read how to send [video](/reference/post_partner-app-appid-v3-video-message#/) as a session message.
11. **Document**: Document messages display a document icon that links to a document, allowing a WhatsApp user to tap and download it.

```curl
--data-urlencode 'type=document' \
--data-urlencode 'document= { "link": "https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf"}'

OR

--data-urlencode 'type=document' \
--data-urlencode 'document={"id":"1116325689362602" }'

```

## Flow Management

1. **Create Flow**: This API allows the user to create a flow in a Gupshup application by specifying the flow's name and categories.  Read how to use the [Create Flow API](/reference/createflow#/).
2. **Get Flow**: To retrieve detailed information about a specific flow, the **Get Flow** API is used.  Read how to use the [Get Flow API](/reference/getflowbyid#/).
3. **Get All Flow API**: To retrieve a list of all flows associated with a specific appID,  the **Get All Flow** API is used.  Read how to use the [Get All Flow API](/reference/getallflow#/).
4. **Update Flow**: Used to modify an existing flow within an application by providing the app ID and flow ID.  Read how to use the [Update Flow API](/reference/updateflow#/).
5. **Get Flow Json**: This endpoint is used to retrieve the *Json* assets of specific app flows. Read how to use the [Get Flow Json API](/reference/getflowjson#/).
6. **Get Preview URL**: This endpoint is used to retrieve the preview URL for a specific flow in an application. Read how to use the [Get Preview URL API](/reference/getpreviewurl#/).
7. **Delete Flow**: Used to delete a specific flow in an application by providing the app ID and flow ID. Successful deletion returns a status of "success" with a true value.  Read how to use the [Delete Flow API](/reference/deleteflow#/).
8. **Deprecate Flow**: Used to deprecate the flow.  Read how to use the [Deprecate Flow API](/reference/deprecateflow#/).
9. **Publish Flow**: Used to publish a flow message.  Read how to use the [Publish Flow API](/reference/publishflow#/).
10. **Update Flow Json**: Used for updating the JSON structure of an existing flow.  Read how to use the [Update Flow Json API](/reference/updateflowjson#/).

# Outgoing Template Message

## Request

```curl
curl --location --globoff '{{PARTNER}}/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'messaging_product=whatsapp' \
--data-urlencode 'recipient_type=individual' \
--data-urlencode 'to=919970******' \
--data-urlencode 'type=template' \
--data-urlencode 'template={"language":{"policy":"deterministic","code":"en"},"namespace":"a0ff8e69_71a0_45bf_b6fe_92be4a3c58cd","name":"temp_lto_copyoffercode","components":[{"type":"body","parameters":[{"type":"text","text":"User"}]},{"type":"limited_time_offer","parameters":[{"type":"limited_time_offer","limited_time_offer":{"expiration_time_ms":1704881963523}}]},{"type":"button","sub_type":"copy_code","index":"0","parameters":[{"type":"coupon_code","coupon_code":"1234"}]}]}'
```

## Response

```json
{
   "messages": [
       {
           "id": "8b149927-8f3c-40da-b62c-58eeff60903e"
       }
   ],
   "messaging_product": "whatsapp",
   "contacts": [
       {
           "input": "919970****44",
           "wa_id": "919970******"
       }
   ]
}
```

# Subscription API - V3

To manage the subscription effectively, use [subscription](/reference/setsubscription-api-v3#/) API.

# Incoming Message

## Event - V3 - Status

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918375031069",
              "phone_number_id": "207437372456043"
            },
            "statuses": [
              {
                "gs_id": "3de985af-d06e-41e1-acaf-c379b429668a",
                "id": "fc46fadf-5075-4bb6-9cff-f3ff8c6f6478",
                "recipient_id": "919970754444",
                "status": "read",
                "timestamp": "1705574869"
              }
            ]
          }
        }
      ],
      "id": "216141188246170"
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

## Event - V3 - Message

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "contacts": [
              {
                "profile": {
                  "name": "Sneha"
                },
                "wa_id": "91997075****"
              }
            ],
            "messages": [
              {
                "from": "91997075***",
                "id": "wamid.HBgMOTE5OTcwNzU0NDQ0FQIAEhgUM0E1NjIzMTY1N0VGNUE5NjY1M0EA",
                "text": {
                  "body": "Hi"
                },
                "timestamp": "1705574871",
                "type": "text"
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918375031069",
              "phone_number_id": "207437372456043"
            }
          }
        }
      ],
      "id": "216141188246170"
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```