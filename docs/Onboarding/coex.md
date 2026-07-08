---
title: Coex
deprecated: false
hidden: true
metadata:
  robots: index
---
# Edit Webhook Event upon Editing Media Message with Caption

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
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "edit": {
                  "message": {
                    "image": {
                      "caption": "Heylooo givig",
                      "id": "903470842067649",
                      "mime_type": "image/jpeg",
                      "sha256": "8V/pEU8aOxbDSZpEYkIE6s7Pr7yJvlZ6tz4PW39Zccs=",
                      "url": "https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=903470842067649&source=webhook&ext=1769753821&hash=ARlbBG8TjKXO8ZCHMiykC6rKJ0f1LoKP2g6ul7_6uabn3A"
                    },
                    "type": "image"
                  },
                  "original_message_id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E0ODM3QUM2Nzc0ODI5ODBDMjkA"
                },
                "from": "917506080480",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FCMTZCNkE5RUUxN0MwQTg3MEUA",
                "timestamp": "1769753520",
                "type": "edit"
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
  "gs_app_id": "20e0cd5c-0476-4947-9003-532553be24c8",
  "object": "whatsapp_business_account"
}
```

<br />

# Edit Webhook Even upon Editing Text Message

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
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "edit": {
                  "message": {
                    "text": {
                      "body": "Hey WA user"
                    },
                    "type": "text"
                  },
                  "original_message_id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E5M0EzMEYwNzc1Qzg0MjU1MTEA"
                },
                "from": "917506080480",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0EzQzM1RTA2QkU1QTQxODA4NjkA",
                "timestamp": "1769753418",
                "type": "edit"
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
  "gs_app_id": "20e0cd5c-0476-4947-9003-532553be24c8",
  "object": "whatsapp_business_account"
}

```

<br />

# Revoke Webhook Event upon Deleting a Message

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
                "wa_id": "917506080480"
              }
            ],
            "messages": [
              {
                "from": "917506080480",
                "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E4MTkzMDBBQTVEMjJENzkyRUIA",
                "revoke": {
                  "original_message_id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FGMTg2MENGRDI1RDQzRTdEODcA"
                },
                "timestamp": "1769753870",
                "type": "revoke"
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
  "gs_app_id": "20e0cd5c-0476-4947-9003-532553be24c8",
  "object": "whatsapp_business_account"
}
```

<br />

# Account Update - PARTNER_APP_UNINSTALLED Webhook Event

Your business customers can use the WhatsApp Business app to disconnect from Cloud API by navigating to Settings > Account > Business Platform and clicking the Disconnect Account button. When a business customer disconnects from Cloud API, an account_update webhook with a PARTNER_APP_UNINSTALLED event is triggered.

```json
{
  "entry": [
    {
      "changes": [
        {
          "field": "account_update",
          "value": {
            "event": "PARTNER_APP_UNINSTALLED",
            "waba_info": {
              "owner_business_id": "1903704936437045",
              "partner_app_id": "978415460924688",
              "waba_id": "1197332449152321"
            }
          }
        }
      ],
      "id": "1148530713280127",
      "time": 1769764486
    }
  ],
  "gs_app_id": "20e0cd5c-0476-4947-9003-532553be24c8",
  "object": "whatsapp_business_account"
}
```

<br />

Contacts synchronization when syncType set to smb_app_state_sync

```json
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

Send message with field smb_message_echoes for contacts syncronization

```json
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

Edit message with field smb_message_echoes for contacts syncronization

```json
{
    "entry": [
        {
            "changes": [
                {
                    "field": "smb_message_echoes",
                    "value": {
                        "message_echoes": [
                            {
                                "edit": {
                                    "message": {
                                        "text": {
                                            "body": "Hey akshay"
                                        },
                                        "type": "text"
                                    },
                                    "original_message_id": "wamid.HBgMOTE4NDQ2MDAwOTA5FQIAERgUMkFERTUzRkEzRkI0REE0RkEyNkQA"
                                },
                                "from": "918750963486",
                                "id": "wamid.HBgMOTE4NDQ2MDAwOTA5FQIAERgUMkEwQzhBMEM3OTRCRDVBQUY2RjgA",
                                "timestamp": "1773387747",
                                "to": "918446000909",
                                "type": "edit"
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

Revoke message with field smb_message_echoes for contacts syncronization

```json
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
                                "id": "wamid.HBgMOTE4NDQ2MDAwOTA5FQIAERgUMkFBODVDMDk3MjExNEMwM0Q4RUIA",
                                "revoke": {
                                    "original_message_id": "wamid.HBgMOTE4NDQ2MDAwOTA5FQIAERgUMkFERTUzRkEzRkI0REE0RkEyNkQA"
                                },
                                "timestamp": "1773387781",
                                "to": "918446000909",
                                "type": "revoke"
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
