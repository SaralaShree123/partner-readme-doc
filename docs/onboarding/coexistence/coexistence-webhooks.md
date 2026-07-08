---
summary: Coexistence Webhooks
title: Coexistence Webhooks
deprecated: false
hidden: true
metadata:
  robots: index
---
<Callout icon="❗️">
  **Please Note: This page has been deprecated.** 

  Please navigate to this <Anchor label="page " target="_blank" href="https://partner-docs.gupshup.io/update/docs/coexistence-events">page </Anchor> for the latest details on Coexistence Events and Webhooks.
</Callout>

# Coex Feature Events

Please look at the meta documentation for more information [here](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users#history)

## history

Describes the WhatsApp Business app chat history of a business that has chosen to share their chat history with a solution provider, or the business’s decision to decline chat history sharing.

**Payload syntax — chat history sharing approved**

```Text payload syntax
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "<WABA_ID>",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "<BUSINESS_PHONE_NUMBER>",
              "phone_number_id": "<BUSINESS_PHONE_NUMBER_ID>"
            },
            "history": [
              {
                "metadata": {
                  "phase": <PHASE>,
                  "chunk_order": <CHUNK_ORDER>,
                  "progress": <PROGRESS>
                },
                "threads": [
                  /* First chat history thread object */
                  {
                    "id": "<WHATSAPP_USER_PHONE_NUMBER>",
                    "messages": [
                      /* First message object in thread */
                      {
                        "from": "<BUSINESS_OR_WHATSAPP_USER_PHONE_NUMBER>",
                        "to": "<WHATSAPP_USER_PHONE_NUMBER>", // only included if SMB message echo
                        "id": "<WHATSAPP_MESSAGE_ID>",
                        "timestamp": "<DEVICE_TIMESTAMP>,
                        "type": "<MESSAGE_TYPE>",
                        "<MESSAGE_TYPE>": {
                          <MESSAGE_CONTENTS>
                        },
                        "history_context": {
                          "status": "<MESSAGE_STATUS>"
                        }
                      },
                      /* Additional message objects in thread would follow, if any */
                    ]
                  },
                  /* Additional chat history thread objects would follow, if any */
                ]
              }
            ]
          },
          "field": "history"
        }
      ]
    }
  ]
}


```

## smb_app_state_sync

Describes one or more WhatsApp contacts in a business customer’s WhatsApp Business app.
 Trigger events:

* a solution provider synchronizes the WhatsApp contacts of a business customer who they have onboarded with a WhatsApp Business app phone number
* a business customer, onboarded by a solution provider, with a WhatsApp Business app phone number adds, edits, or removes a WhatsApp contacts

```json Payload syntax
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "<WABA_ID>",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "<BUSINESS_PHONE_NUMBER>",
              "phone_number_id": "<BUSINESS_PHONE_NUMBER_ID>"
            },
            "state_sync": [
              {
                "type": "contact",
                "contact": {
                  "full_name": "<CONTACT_FULL_NAME>",
                  "first_name": "<CONTACT_FIRST_NAME>",
                  "phone_number": "<CONTACT_PHONE_NUMBER>"
                },
                "action": "<ACTION>",
                "metadata": {
                  "timestamp": "<WEBHOOK_TIMESTAMP>"
                }
              },
              * Additional contacts would follow, if any */
            ]
          },
          "field": "smb_app_state_sync"
        }
      ]
    }
  ]
}


```

## smb_message_echoes

Trigger events

A business customer uses the WhatsApp Business app or supported companion device to message a WhatsApp user.

```Text Payload syntax
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "<WABA_ID>",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "<BUSINESS_PHONE_NUMBER>",
              "phone_number_id": "<BUSINESS_PHONE_NUMBER_ID>"
            },
            "message_echoes": [
              {
                "from": "<BUSINESS_PHONE_NUMBER>",
                "to": "<WHATSAPP_USER_PHONE_NUMBER>",
                "id": "<WHATSAPP_MESSAGE_ID>",
                "timestamp": "<WEBHOOK_TIMESTAMP>",
                "type": "<MESSAGE_TYPE>",
                "<MESSAGE_TYPE>": {
                  <MESSAGE_CONTENTS>
                }
              }
            ]
          },
          "field": "smb_message_echoes"
        }
      ]
    }
  ]
}


```

Example Payload

This example payload describes a text message (type is text) sent to a WhatsApp user by a business customer with the WhatsApp Business app.

```json Example
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "102290129340398",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550783881",
              "phone_number_id": "106540352242922"
            },
            "message_echoes": [
              {
                "from": "15550783881",
                "to": "16505551234",
                "id": "wamid.HBgLMTY0NjcwNDM1OTUVAgARGBIyNDlBOEI5QUQ4NDc0N0FCNjMA",
                "timestamp": "1700255121",
                "type": "text"
                "text": {
                  "body": "Here's the info you requested! https://www.meta.com/quest/quest-3/"
                }
              }
            ]
          },
          "field": "smb_message_echoes"
        }
      ]
    }
  ]
}


```

<br />

# Account Level Events

For more Coex WhatsApp account level events please check out meta documentation <Anchor label="here" target="_blank" href="https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users#webhooks">here</Anchor>.

<br />
