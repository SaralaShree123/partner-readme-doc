---
summary: Coexistence Events
title: Coexistence Events
deprecated: false
hidden: true
metadata:
  robots: index
---
Embedded Signup lets businesses onboard using their existing WhatsApp Business account and phone number, enabling them to send messages at scale via your app while still maintaining one-to-one messaging and synced chat history in the WhatsApp Business app.

# Synchronizing WhatsApp Business App Data

Use this <Anchor label="Sync API" target="_blank" href="https://partner-docs.gupshup.io/update/reference/initiatecoexsync">Sync API</Anchor> to trigger the `history` and `smb_app_state_sync`

## Webhook event for `history`

Use the [Sync API](https://partner-docs.gupshup.io/update/reference/initiatecoexsync) with syncType=history to start message history sync. If the business opts in, history webhooks will be triggered for messages within the selected time range.

```
{
  "entry": [
    {
      "changes": [
        {
          "field": "history",
          "value": {
            "history": [
              {
                "metadata": {
                  "chunk_order": 1,
                  "phase": 0,
                  "progress": 100
                },
                "threads": [
                  {
                    "id": "917506080480",
                    "messages": [
                      {
                        "from": "918588096070",
                        "history_context": {
                          "from_me": true,
                          "status": "read"
                        },
                        "id": "wamid.HBgMOTE4NTg4MDk2MDcwFQIAERgSQ0FFNjA5RjM4MDdCRDRGMjdFAA==",
                        "text": {
                          "body": "Hi man"
                        },
                        "timestamp": "1775627842",
                        "type": "text"
                      },
                      {
                        "from": "917506080480",
                        "history_context": {
                          "status": "pending"
                        },
                        "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0ExNDdBQ0ZEODQ3NTQ4MENDMzkA",
                        "text": {
                          "body": "Hi dude"
                        },
                        "timestamp": "1775627825",
                        "type": "text"
                      },
                      {
                        "from": "918588096070",
                        "history_context": {
                          "from_me": true,
                          "status": "read"
                        },
                        "id": "wamid.HBgMOTE4NTg4MDk2MDcwFQIAERgSQThFQzU5NDNFODlFM0IxMjFDAA==",
                        "text": {
                          "body": "Hi Avadoot"
                        },
                        "timestamp": "1775627478",
                        "type": "text"
                      },
                      {
                        "from": "917506080480",
                        "history_context": {
                          "status": "pending"
                        },
                        "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0EwODFGMjZCNTA2N0VBQTI3OEYA",
                        "text": {
                          "body": "Heyoo"
                        },
                        "timestamp": "1775627414",
                        "type": "text"
                      },
                      {
                        "from": "918588096070",
                        "history_context": {
                          "from_me": true,
                          "status": "delivered"
                        },
                        "id": "wamid.HBgMOTE4NTg4MDk2MDcwFQIAERgUMkFEQkFCMEFCNEVGMDUyMjk0OUYA",
                        "text": {
                          "body": "Hello"
                        },
                        "timestamp": "1775627221",
                        "type": "text"
                      },
                      {
                        "from": "918588096070",
                        "history_context": {
                          "from_me": true,
                          "status": "delivered"
                        },
                        "id": "wamid.HBgMOTE4NTg4MDk2MDcwFQIAERgUMkFFN0RGRTY0RUNCNEVCNTIxNEIA",
                        "text": {
                          "body": "Hey"
                        },
                        "timestamp": "1775626356",
                        "type": "text"
                      }
                    ]
                  },
                  {
                    "id": "447710173736",
                    "messages": [
                      {
                        "errors": [
                          {
                            "code": 131051,
                            "error_data": {
                              "details": "Unsupported message received"
                            },
                            "message": "Message type unknown",
                            "title": "Message type unknown"
                          }
                        ],
                        "from": "447710173736",
                        "history_context": {
                          "status": "pending"
                        },
                        "id": "wamid.HBgMNDQ3NzEwMTczNzM2FQIAEhgSMDkxQTIyRjhFMDFFOTFCOTdEAA==",
                        "timestamp": "1775628342",
                        "type": "errors"
                      },
                      {
                        "errors": [
                          {
                            "code": 131051,
                            "error_data": {
                              "details": "Unsupported message received"
                            },
                            "message": "Message type unknown",
                            "title": "Message type unknown"
                          }
                        ],
                        "from": "447710173736",
                        "history_context": {
                          "status": "pending"
                        },
                        "id": "wamid.HBgMNDQ3NzEwMTczNzM2FQIAEhgSQUE3RTJFNEFEOEJBNDQ2NUQzAA==",
                        "timestamp": "1775625835",
                        "type": "errors"
                      }
                    ]
                  }
                ]
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "918588096070",
              "phone_number_id": "1005385572668707"
            }
          }
        }
      ],
      "id": "1619622649281109"
    }
  ],
  "gs_app_id": "5d873e48-0b81-4e23-801a-13c6db86cf17",
  "object": "whatsapp_business_account"
}
```

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Placeholder
      </th>

      <th>
        Description
      </th>

      <th>
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        WABA_ID  
        String
      </td>

      <td>
        The business customer’s WhatsApp Business Account ID.
      </td>

      <td>
        102290129340398
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER  
        String
      </td>

      <td>
        The business customer’s business phone number.
      </td>

      <td>
        15550783881
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER_ID  
        String
      </td>

      <td>
        The business customer’s business phone number ID.
      </td>

      <td>
        106540352242922
      </td>
    </tr>

    <tr>
      <td>
        PHASE  
        Integer
      </td>

      <td>
        Indicates history phase. Values can be: 0 — indicates messages are from day 0 (business onboarding time) through day 1 1 — indicates messages are from day 1 through day 90 2 — indicates messages are from day 90 through day 180
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        CHUNK_ORDER  
        Integer
      </td>

      <td>
        Integer Indicates chunk number, which you can use to order sets of webhooks sequentially.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        PROGRESS  
        Integer
      </td>

      <td>
        Indicates percentage total of synchronization progress. Minimum 0, maximum 100.
      </td>

      <td>
        55
      </td>
    </tr>

    <tr>
      <td>
        WHATSAPP_USER_PHONE_NUMBER  
        String
      </td>

      <td>
        The WhatsApp user’s phone number.
      </td>

      <td>
        16505551234
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_OR_WHATSAPP_USER_PHONE_NUMBER  
        String
      </td>

      <td>
        The business customer’s phone number, or the WhatsApp user’s phone number. If the value is the business’s phone number, the message object describes a message sent by the business to a WhatsApp user. If the value is the WhatsApp user’s phone number, the message object describes a message sent by the WhatsApp user to the business.
      </td>

      <td>
        15550783881
      </td>
    </tr>

    <tr>
      <td>
        WHATSAPP_USER_PHONE_NUMBER  
        String
      </td>

      <td>
        The WhatsApp user’s phone number. The to property is only included if the message object represents an SMB message echo.
      </td>

      <td>
        16505551234
      </td>
    </tr>

    <tr>
      <td>
        WHATSAPP_MESSAGE_ID  
        String
      </td>

      <td>
        WhatsApp message ID.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DEVICE_TIMESTAMP  
        String
      </td>

      <td>
        Unix timestamp indicating when the message was received by the recipient’s device.
      </td>

      <td>
        1738796547
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_TYPE  
        String
      </td>

      <td>
        Message type. Note that this placeholder appears twice in the syntax above, as it serves as a placeholder for the type property’s value and its matching property name. See the example payload below for a thread with various message types. If this value is set to media_placeholder, the message object describes a message that contained a media asset. In this case, the message contents will be omitted. Instead, a separate history webhook will follow, describing the content of the message and the media asset ID, but only if the message was sent within the last two weeks of your query. See the example payload below describing a media message’s contents.
      </td>

      <td>
        text
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_CONTENTS  
        Object
      </td>

      <td>
        An object describing the message’s contents. This value will vary based on the message type, as well as the contents message. For example, if a business sends an image message without a caption, the object would not include the caption property. See Sending messages for examples of payloads for each message type.
      </td>

      <td>
        ```text
        {"body":"Here's the info you requested! https://www.meta.com/quest/quest-3/"}
        ```
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_STATUS  
        String
      </td>

      <td>
        Indicates the message’s most recent delivery stats. Values can be: DELIVERED ERROR PENDING PLAYED READ SENT
      </td>

      <td>
        READ
      </td>
    </tr>
  </tbody>
</Table>

## Webhook event for `smb_app_state_sync`

Describes WhatsApp contacts in a business account. Triggered when contacts are synced or when a customer adds, edits, or removes contacts.

Use the [Sync API](https://partner-docs.gupshup.io/update/reference/initiatecoexsync) with `syncType`=`smb_app_state_sync `to start contact sync. Successful requests trigger webhooks for existing and future contact changes. This can be done only once unless the customer offboards and re-onboards.

```
{
    "entry": [
        {
            "changes": [
                {
                    "field": "smb_app_state_sync",
                    "value": {
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "918750963486",
                            "phone_number_id": "950443251490365"
                        },
                        "state_sync": [
                            {
                                "action": "remove",
                                "contact": {
                                    "phone_number": "917715078842"
                                },
                                "metadata": {
                                    "timestamp": "0"
                                },
                                "type": "contact"
                            }
                        ]
                    }
                }
            ],
            "id": "1197332449152321"
        }
    ],
    "gs_app_id": "6d300e4b-426e-4212-8e02-5df480593a5f",
    "object": "whatsapp_business_account"
}
```

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Placeholder
      </th>

      <th>
        Description
      </th>

      <th>
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        WABA_ID  
        String
      </td>

      <td>
        The business customer’s WhatsApp Business Account ID.
      </td>

      <td>
        102290129340398
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER  
        String
      </td>

      <td>
        The business customer’s business phone number.
      </td>

      <td>
        15550783881
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER_ID  
        String
      </td>

      <td>
        The business customer’s business phone number ID.
      </td>

      <td>
        106540352242922
      </td>
    </tr>

    <tr>
      <td>
        CONTACT_FULL_NAME  
        Integer
      </td>

      <td>
        The contact’s full name, as it appears in the business customer’s WhatsApp Business app phone address book. Not included when the business customer removes a contact from their WhatsApp Business app phone address book.
      </td>

      <td>
        Pablo Morales
      </td>
    </tr>

    <tr>
      <td>
        CONTACT_FIRST_NAME  
        String
      </td>

      <td>
        The contact’s first name, as it appears in the business customer’s WhatsApp Business app phone address book. Not included when the business customer removes a contact from their WhatsApp Business app phone address book.
      </td>

      <td>
        Pablo
      </td>
    </tr>

    <tr>
      <td>
        CONTACT_PHONE_NUMBER  
        String
      </td>

      <td>
        The contact’s WhatsApp phone number.
      </td>

      <td>
        16505551234
      </td>
    </tr>

    <tr>
      <td>
        ACTION  
        String
      </td>

      <td>
        Indicates if the business customer added, edited, or deleted a contact from their WhatsApp Business app phone address book. Values can be: add — the business added or edited a contact remove — the business removed a contact
      </td>

      <td>
        add
      </td>
    </tr>

    <tr>
      <td>
        CONTACT_CHANGE_TIMESTAMP  
        String
      </td>

      <td>
        Unix timestamp indicated when the contact was added, edited, or removed.
      </td>

      <td>
        1738346006
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Webhook event for `smb_message_echoes`

Describes a message sent by a business customer to a WhatsApp user with the WhatsApp Business app or supported companion device.

```
{
    "entry": [
        {
            "changes": [
                {
                    "field": "smb_message_echoes",
                    "value": {
                        "message_echoes": [
                            {
                                "from": "918750963486",
                                "id": "wamid.HBgMOTE4NDQ2MDAwOTA5FQIAERgUMkFERTUzRkEzRkI0REE0RkEyNkQA",
                                "text": {
                                    "body": "Hey"
                                },
                                "timestamp": "1773387740",
                                "to": "918446000909",
                                "type": "text"
                            }
                        ],
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "918750963486",
                            "phone_number_id": "950443251490365"
                        }
                    }
                }
            ],
            "id": "1197332449152321"
        }
    ],
    "gs_app_id": "6d300e4b-426e-4212-8e02-5df480593a5f",
    "object": "whatsapp_business_account"
}
```

<br />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Placeholder
      </th>

      <th>
        Description
      </th>

      <th>
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        WABA_ID  
        String
      </td>

      <td>
        The business customer’s WhatsApp Business Account ID.
      </td>

      <td>
        102290129340398
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER  
        String
      </td>

      <td>
        The business customer’s business phone number.
      </td>

      <td>
        15550783881
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS_PHONE_NUMBER_ID  
        String
      </td>

      <td>
        The business customer’s business phone number ID.
      </td>

      <td>
        106540352242922
      </td>
    </tr>

    <tr>
      <td>
        WHATSAPP_USER_PHONE_NUMBER String
      </td>

      <td>
        The WhatsApp user’s phone number.
      </td>

      <td>
        16505551234
      </td>
    </tr>

    <tr>
      <td>
        WHATSAPP_MESSAGE_ID  
        String
      </td>

      <td>
        WhatsApp message ID.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        WEBHOOK_TIMESTAMP  
        String
      </td>

      <td>
        Unix timestamp indicated when the webhook was triggered.
      </td>

      <td>
        1738796547
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_TYPE  
        String
      </td>

      <td>
        Message type. Note that this placeholder appears twice in the syntax above, as it serves as a placeholder for the type property’s value and its matching property name.
      </td>

      <td>
        text
      </td>
    </tr>

    <tr>
      <td>
        MESSAGE_CONTENTS  
        Object
      </td>

      <td>
        An object describing the message’s contents. This value will vary based on the message type, as well as the contents of the message. For example, if a business sends an image message without a caption, the object would not include the caption property. See Sending messages for examples of payloads for each message type.
      </td>

      <td>
        ```text
        {"body":"Here's the info you requested! https://www.meta.com/quest/quest-3/"}
        ```
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Account Level Events

For more Coex WhatsApp account level events please check out meta documentation <Anchor label="here" target="_blank" href="https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users#webhooks">here</Anchor>.
