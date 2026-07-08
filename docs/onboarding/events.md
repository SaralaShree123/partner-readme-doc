---
summary: Events
title: Events
deprecated: false
hidden: false
metadata:
  title: Events-V3
  robots: index
---
# Enqueued - V3 Event

```Text JSON
Type of object that sent the event	{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "statuses": [
              {
                "gs_id": "2baff204-c39a-4121-90b5-f53f26d522b3",
                "id": "wamid.HBgMOTE5MTYzODA1ODczFQIAERgSNkZCMThGMEEwQzJDOUFGQjFBAA==",
                "recipient_id": "9191****873",
                "status": "enqueued",
                "timestamp": 1710941393420
              }Type of object that sent the event	
            ]
          }
        }
      ]
    }
  ],
  "gs_app_id": "82ed52f4-30c0-4f12-81b4-e7ad07bd41de",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                     | Description                            | Example                              |
| :---------------------- | :------------------------------------- | :----------------------------------- |
| object                  | Type of object that sent the event     | whatsapp_business_account            |
| gs_app_id               | Gupshup application ID                 | 82ed52f4-30c0-4f12-81b4-e7ad07bd41de |
| messaging_product       | Messaging product                      | whatsapp                             |
| statuses[].id           | WhatsApp message ID (wamid)            | wamid.HBgMOTE5...                    |
| statuses[].recipient_id | Destination phone number               | 9191****873                          |
| statuses[].status       | Message status                         | enqueued                             |
| statuses[].timestamp    | Time when status was updated (s or ms) | 1710941393420                        |

# Sent - V3 Event

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "9****8",
              "phone_number_id": "158072934066266"
            },
            "statuses": [
              {
                "conversation": {
                  "expiration_timestamp": "1710936120",
                  "id": "3dabdf65abaf1cbbf85217d232cce91f"
                },
                "gs_id": "7daeb742-f2dc-4c09-90e0-d879d20f7b98",
                "id": "wamid.HBgMOTE5MTYzODA1ODczFQIAERgSMDQ4Rj...",
                "recipient_id": "91****73",
                "status": "sent",
                "timestamp": "1710930461"
              }
            ]
          }
        }
      ],
      "id": "112535025189792"
    }
  ],
  "gs_app_id": "82ed52f4-30c0-4f12-81b4-e7ad07bd41de",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                        | Example                              |
| :---------------------------- | :--------------------------------- | :----------------------------------- |
| object                        | Type of object that sent the event | whatsapp_business_account            |
| gs_app_id                     | Gupshup application ID             | 82ed52f4-30c0-4f12-81b4-e7ad07bd41de |
| metadata.display_phone_number | Display phone number               | 9******8                             |
| metadata.phone_number_id      | Phone number ID                    | 158072934066266                      |
| statuses[].conversation.id    | Conversation ID                    | 3dabdf65abaf1cbbf85217d232cce91f     |
| statuses[].id                 | WhatsApp message ID (wamid)        | wamid.HBgMOTE5...                    |
| statuses[].recipient_id       | Destination phone number           | 91*****3                             |
| statuses[].status             | Message status                     | sent                                 |
| statuses[].timestamp          | Timestamp (in seconds)             | 1710930461                           |

# Delivered - V3 Event

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "9*****58",
              "phone_number_id": "158072934066266"
            },
            "statuses": [
              {
                "conversation": {
                  "id": "3dabdf65abaf1cbbf85217d232cce91f"
                },
                "gs_id": "7daeb742-f2dc-4c09-90e0-d879d20f7b98",
                "id": "wamid.HBgMOTE5MTYzODA1ODczFQIAERgSMDQ4Rj...",
                "recipient_id": "91****873",
                "status": "delivered",
                "timestamp": "1710930462"
              }
            ]
          }
        }
      ],
      "id": "112535025189792"
    }
  ],
  "gs_app_id": "82ed52f4-30c0-4f12-81b4-e7ad07bd41de",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                         | Example                          |
| :---------------------------- | :---------------------------------- | :------------------------------- |
| object                        | Type of object that sent the event  | whatsapp_business_account        |
| gs_app_id                     | Gupshup application ID              | 82ed52f4-30c0-4f12-81b4-e7ad...  |
| metadata.display_phone_number | Display phone number                | 91****58                         |
| metadata.phone_number_id      | Phone number ID                     | 158072934066266                  |
| statuses[].conversation.id    | Unique conversation ID              | 3dabdf65abaf1cbbf85217d232cce91f |
| statuses[].id                 | WhatsApp message ID (wamid)         | wamid.HBgMOTE5MTYz...            |
| statuses[].recipient_id       | Destination phone number            | 91*****3                         |
| statuses[].status             | Message status                      | delivered                        |
| statuses[].timestamp          | Timestamp (in seconds) for delivery | 1710930462                       |

# Read-V3 Event

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "9*******8",
              "phone_number_id": "158072934066266"
            },
            "statuses": [
              {
                "gs_id": "7b8f0910-db98-4cce-be5f-e6e1e847b4bd",
                "id": "wamid.HBgMOTE5MTYzODA1ODczFQIAERgSMUUzNz...",
                "recipient_id": "91*******73",
                "status": "read",
                "timestamp": "1720779817"
              }
            ]
          }
        }
      ],
      "id": "112535025189792"
    }
  ],
  "gs_app_id": "82ed52f4-30c0-4f12-81b4-e7ad07bd41de",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                        | Example                         |
| :---------------------------- | :--------------------------------- | :------------------------------ |
| object                        | Type of object that sent the event | whatsapp_business_account       |
| gs_app_id                     | Gupshup application ID             | 82ed52f4-30c0-4f12-81b4-e7ad... |
| metadata.display_phone_number | Display phone number               | 91*****8                        |
| metadata.phone_number_id      | Phone number ID                    | 158072934066266                 |
| statuses[].id                 | WhatsApp message ID (wamid)        | wamid.HBgMOTE5MTYz...           |
| statuses[].recipient_id       | Destination phone number           | 91****73                        |
| statuses[].status             | Message status                     | read                            |
| statuses[].timestamp          | Timestamp for the "read" status    | 1720779817                      |

# Failed-V3 Event

```Text JSON
{
  "entry": [
    {
      "changes": [
        {
          "field": "messages",
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "91*******8",
              "phone_number_id": "158072934066266"
            },
            "statuses": [
              {
                "errors": [
                  {
                    "code": 131047,
                    "href": "https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/",
                    "title": "Message failed to send..."
                  }
                ],
                "gs_id": "91f58e90-f5ba-4cfc-9ca7-e4ab965b9449",
                "id": "wamid.HBgMOTE3OTgwODkwOTc4FQIAERgSNERF...",
                "recipient_id": "91*******78",
                "status": "failed",
                "timestamp": "1710941507"
              }
            ]
          }
        }
      ],
      "id": "112535025189792"
    }
  ],
  "gs_app_id": "82ed52f4-30c0-4f12-81b4-e7ad07bd41de",
  "object": "whatsapp_business_account"
}	
```

## Payload Description

| Key                           | Description                        | Example                                   |
| :---------------------------- | :--------------------------------- | :---------------------------------------- |
| object                        | Type of object that sent the event | whatsapp_business_account                 |
| gs_app_id                     | Gupshup application ID             | 82ed52f4-30c0-4f12-81b4-e7ad...           |
| metadata.display_phone_number | Display phone number               | 91*******8                                |
| metadata.phone_number_id      | Phone number ID                    | 158072934066266                           |
| statuses[].errors[].code      | Error code                         | 131047                                    |
| statuses[].errors[].title     | Error title                        | "Message failed to send..."               |
| statuses[].id                 | WhatsApp message ID (wamid)        | wamid.HBgMOTE3OTgwODkwOTc4FQIAERgSNERF... |
| statuses[].recipient_id       | Destination phone number           | 91*******8                                |
| statuses[].status             | Message status                     | failed                                    |
| statuses[].timestamp          | Timestamp of message failure       | 1710941507                                |

<br />

# V3 Incoming Media Messages Event

## Video

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
                  "name": "Avadhoot Yadav"
                },
                "user_id": "IN.35081637581480220",
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "from": "917506080480",
                "from_user_id": "IN.35081637581480220",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E0MkM5RjE2RkRBRjQzRDRGMDEA",
                "timestamp": "1782372987",
                "type": "video",
                "video": {
                  "id": "1791860341777005",
                  "mime_type": "video/mp4",
                  "sha256": "zCYvqunwILzc9sXt3/2HyNYWv0L0V7WfXe5a0gqn8t0=",
                  "url": "https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1791860341777005?download=false"
                }
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "917835039205",
              "phone_number_id": "105523045970845"
            }
          }
        }
      ],
      "id": "116676371511027"
    }
  ],
  "gs_app_id": "07c7c72d-20e3-4ff9-a5a1-14d1186eeec8",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                          | Example                                                                                                                                                                                                                            |
| ----------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                          | Type of object that sent the event   | video                                                                                                                                                                                                                              |
| gs_app_id                     | Gupshup application ID               | 07c7c72d-20e3-4ff9-a5a1-14d1186eeec8                                                                                                                                                                                               |
| messaging_product             | Messaging product                    | whatsapp                                                                                                                                                                                                                           |
| contacts[].profile.name       | Name of the contact                  | Avadhoot Yadav                                                                                                                                                                                                                     |
| contacts[].user_id            | User ID of the contact               | IN.35081637581480220                                                                                                                                                                                                               |
| contacts[].wa_id              | WhatsApp ID of the contact           | 917506080480                                                                                                                                                                                                                       |
| messages[].from               | Sender's phone number                | 917506080480                                                                                                                                                                                                                       |
| messages[].from_user_id       | Sender's user ID                     | IN.35081637581480220                                                                                                                                                                                                               |
| messages[].id                 | Message ID (wamid)                   | wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E0MkM5RjE2RkRBRjQzRDRGMDEA                                                                                                                                                                     |
| messages[].timestamp          | Time when message was sent (seconds) | 1782372987                                                                                                                                                                                                                         |
| messages[].type               | Type of message content              | video                                                                                                                                                                                                                              |
| messages[].video.id           | Video ID                             | 1791860341777005                                                                                                                                                                                                                   |
| messages[].video.mime_type    | Video MIME type                      | video/mp4                                                                                                                                                                                                                          |
| messages[].video.sha256       | Video SHA256 hash                    | zCYvqunwILzc9sXt3/2HyNYWv0L0V7WfXe5a0gqn8t0=                                                                                                                                                                                       |
| messages[].video.url          | Video URL                            | [https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1791860341777005?download=false](https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1791860341777005?download=false) |
| metadata.display_phone_number | Display phone number                 | 917835039205                                                                                                                                                                                                                       |
| metadata.phone_number_id      | Phone number ID                      | 105523045970845                                                                                                                                                                                                                    |
| entry[].changes[].field       | Field that changed                   | messages                                                                                                                                                                                                                           |
| entry[].id                    | Account ID                           | 116676371511027                                                                                                                                                                                                                    |
| object                        | Object type                          | whatsapp_business_account                                                                                                                                                                                                          |

<br />

## Audio

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
                  "name": "Avadhoot Yadav"
                },
                "user_id": "IN.35081637581480220",
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "audio": {
                  "id": "3609461882553011",
                  "mime_type": "audio/ogg; codecs=opus",
                  "sha256": "wua6L0gsWIGhTqM0SxPYpfcT2rkJrvRB0lpqI+cpISo=",
                  "url": "https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/3609461882553011?download=false",
                  "voice": true
                },
                "from": "917506080480",
                "from_user_id": "IN.35081637581480220",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E2QjQ5NUUyMUZDQzg2MDJEMjEA",
                "timestamp": "1782372953",
                "type": "audio"
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "917835039205",
              "phone_number_id": "105523045970845"
            }
          }
        }
      ],
      "id": "116676371511027"
    }
  ],
  "gs_app_id": "07c7c72d-20e3-4ff9-a5a1-14d1186eeec8",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                          | Example                                                                                                                                                                                                                            |
| ----------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                          | Type of object that sent the event   | audio                                                                                                                                                                                                                              |
| gs_app_id                     | Gupshup application ID               | 07c7c72d-20e3-4ff9-a5a1-14d1186eeec8                                                                                                                                                                                               |
| messaging_product             | Messaging product                    | whatsapp                                                                                                                                                                                                                           |
| contacts[].profile.name       | Name of the contact                  | Avadhoot Yadav                                                                                                                                                                                                                     |
| contacts[].user_id            | User ID of the contact               | IN.35081637581480220                                                                                                                                                                                                               |
| contacts[].wa_id              | WhatsApp ID of the contact           | 917506080480                                                                                                                                                                                                                       |
| messages[].from               | Sender's phone number                | 917506080480                                                                                                                                                                                                                       |
| messages[].from_user_id       | Sender's user ID                     | IN.35081637581480220                                                                                                                                                                                                               |
| messages[].id                 | Message ID (wamid)                   | wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E2QjQ5NUUyMUZDQzg2MDJEMjEA                                                                                                                                                                     |
| messages[].timestamp          | Time when message was sent (seconds) | 1782372953                                                                                                                                                                                                                         |
| messages[].type               | Type of message content              | audio                                                                                                                                                                                                                              |
| messages[].audio.id           | Audio ID                             | 3609461882553011                                                                                                                                                                                                                   |
| messages[].audio.mime_type    | Audio MIME type                      | audio/ogg; codecs=opus                                                                                                                                                                                                             |
| messages[].audio.sha256       | Audio SHA256 hash                    | wua6L0gsWIGhTqM0SxPYpfcT2rkJrvRB0lpqI+cpISo=                                                                                                                                                                                       |
| messages[].audio.url          | Audio URL                            | [https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/3609461882553011?download=false](https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/3609461882553011?download=false) |
| messages[].audio.voice        | Whether this is a voice message      | true                                                                                                                                                                                                                               |
| metadata.display_phone_number | Display phone number                 | 917835039205                                                                                                                                                                                                                       |
| metadata.phone_number_id      | Phone number ID                      | 105523045970845                                                                                                                                                                                                                    |
| entry[].changes[].field       | Field that changed                   | messages                                                                                                                                                                                                                           |
| entry[].id                    | Account ID                           | 116676371511027                                                                                                                                                                                                                    |
| object                        | Object type                          | whatsapp_business_account                                                                                                                                                                                                          |

<br />

## Image

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
                  "name": "Avadhoot Yadav"
                },
                "user_id": "IN.35081637581480220",
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "from": "917506080480",
                "from_user_id": "IN.35081637581480220",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FGQkI0QTUyM0NCNjlCMkNBNkMA",
                "image": {
                  "id": "1751740922668458",
                  "mime_type": "image/jpeg",
                  "sha256": "nH77thkhdX34LtswPHcKJJIViehvFyEQkfM2kaDO/oI=",
                  "url": "https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1751740922668458?download=false"
                },
                "timestamp": "1782372910",
                "type": "image"
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "917835039205",
              "phone_number_id": "105523045970845"
            }
          }
        }
      ],
      "id": "116676371511027"
    }
  ],
  "gs_app_id": "07c7c72d-20e3-4ff9-a5a1-14d1186eeec8",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                          | Example                                                                                                                                                                                                                            |
| ----------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                          | Type of object that sent the event   | image                                                                                                                                                                                                                              |
| gs_app_id                     | Gupshup application ID               | 07c7c72d-20e3-4ff9-a5a1-14d1186eeec8                                                                                                                                                                                               |
| messaging_product             | Messaging product                    | whatsapp                                                                                                                                                                                                                           |
| contacts[].profile.name       | Name of the contact                  | Avadhoot Yadav                                                                                                                                                                                                                     |
| contacts[].user_id            | User ID of the contact               | IN.35081637581480220                                                                                                                                                                                                               |
| contacts[].wa_id              | WhatsApp ID of the contact           | 917506080480                                                                                                                                                                                                                       |
| messages[].from               | Sender's phone number                | 917506080480                                                                                                                                                                                                                       |
| messages[].from_user_id       | Sender's user ID                     | IN.35081637581480220                                                                                                                                                                                                               |
| messages[].id                 | Message ID (wamid)                   | wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FGQkI0QTUyM0NCNjlCMkNBNkMA                                                                                                                                                                     |
| messages[].timestamp          | Time when message was sent (seconds) | 1782372910                                                                                                                                                                                                                         |
| messages[].type               | Type of message content              | image                                                                                                                                                                                                                              |
| messages[].image.id           | Image ID                             | 1751740922668458                                                                                                                                                                                                                   |
| messages[].image.mime_type    | Image MIME type                      | image/jpeg                                                                                                                                                                                                                         |
| messages[].image.sha256       | Image SHA256 hash                    | nH77thkhdX34LtswPHcKJJIViehvFyEQkfM2kaDO/oI=                                                                                                                                                                                       |
| messages[].image.url          | Image URL                            | [https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1751740922668458?download=false](https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1751740922668458?download=false) |
| metadata.display_phone_number | Display phone number                 | 917835039205                                                                                                                                                                                                                       |
| metadata.phone_number_id      | Phone number ID                      | 105523045970845                                                                                                                                                                                                                    |
| entry[].changes[].field       | Field that changed                   | messages                                                                                                                                                                                                                           |
| entry[].id                    | Account ID                           | 116676371511027                                                                                                                                                                                                                    |
| object                        | Object type                          | whatsapp_business_account                                                                                                                                                                                                          |

<br />

## Document

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
                  "name": "Avadhoot Yadav"
                },
                "user_id": "IN.35081637581480220",
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "document": {
                  "filename": "demo.docx",
                  "id": "1046654134600113",
                  "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                  "sha256": "JpMp/HrlSz8omzrFLv3jh+3C5WbvmkjWN+hBAix+Dqs=",
                  "url": "https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1046654134600113?download=false&fileName=demo.docx"
                },
                "from": "917506080480",
                "from_user_id": "IN.35081637581480220",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0EwMjA2OUQzMzlDMUM3MTNFMjIA",
                "timestamp": "1782372793",
                "type": "document"
              }
            ],
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "917835039205",
              "phone_number_id": "105523045970845"
            }
          }
        }
      ],
      "id": "116676371511027"
    }
  ],
  "gs_app_id": "07c7c72d-20e3-4ff9-a5a1-14d1186eeec8",
  "object": "whatsapp_business_account"
}
```

## Payload Description

| Key                           | Description                          | Example                                                                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                          | Type of object that sent the event   | document                                                                                                                                                                                                                                                                  |
| gs_app_id                     | Gupshup application ID               | 07c7c72d-20e3-4ff9-a5a1-14d1186eeec8                                                                                                                                                                                                                                      |
| messaging_product             | Messaging product                    | whatsapp                                                                                                                                                                                                                                                                  |
| contacts[].profile.name       | Name of the contact                  | Avadhoot Yadav                                                                                                                                                                                                                                                            |
| contacts[].user_id            | User ID of the contact               | IN.35081637581480220                                                                                                                                                                                                                                                      |
| contacts[].wa_id              | WhatsApp ID of the contact           | 917506080480                                                                                                                                                                                                                                                              |
| messages[].from               | Sender's phone number                | 917506080480                                                                                                                                                                                                                                                              |
| messages[].from_user_id       | Sender's user ID                     | IN.35081637581480220                                                                                                                                                                                                                                                      |
| messages[].id                 | Message ID (wamid)                   | wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0EwMjA2OUQzMzlDMUM3MTNFMjIA                                                                                                                                                                                                            |
| messages[].timestamp          | Time when message was sent (seconds) | 1782372793                                                                                                                                                                                                                                                                |
| messages[].type               | Type of message content              | document                                                                                                                                                                                                                                                                  |
| messages[].document.filename  | Document filename                    | demo.docx                                                                                                                                                                                                                                                                 |
| messages[].document.id        | Document ID                          | 1046654134600113                                                                                                                                                                                                                                                          |
| messages[].document.mime_type | Document MIME type                   | application/vnd.openxmlformats-officedocument.wordprocessingml.document                                                                                                                                                                                                   |
| messages[].document.sha256    | Document SHA256 hash                 | JpMp/HrlSz8omzrFLv3jh+3C5WbvmkjWN+hBAix+Dqs=                                                                                                                                                                                                                              |
| messages[].document.url       | Document URL                         | [https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1046654134600113?download=false&fileName=demo.docx](https://filemanager.gupshup.io/wa/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/wa/media/1046654134600113?download=false\&fileName=demo.docx) |
| metadata.display_phone_number | Display phone number                 | 917835039205                                                                                                                                                                                                                                                              |
| metadata.phone_number_id      | Phone number ID                      | 105523045970845                                                                                                                                                                                                                                                           |
| entry[].changes[].field       | Field that changed                   | messages                                                                                                                                                                                                                                                                  |
| entry[].id                    | Account ID                           | 116676371511027                                                                                                                                                                                                                                                           |
| object                        | Object type                          | whatsapp_business_account                                                                                                                                                                                                                                                 |
