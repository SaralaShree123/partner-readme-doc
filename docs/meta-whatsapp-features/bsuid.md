---
summary: >-
title: BSUID
excerpt: >-
  A BSUID is a unique user identifier that can be used to message a WhatsApp
  user when you don’t know their phone number. BSUID will be assigned to the
  userid parameter and appear in following messages webhooks
deprecated: false
hidden: false
metadata:
  robots: index
---
# API Reference to enable BSUID

[https://partner-docs.gupshup.io/update/docs/api-to-enable-bsuid-flag-for-an-app](https://partner-docs.gupshup.io/update/docs/api-to-enable-bsuid-flag-for-an-app)

<br />

# V2 Subscription Events with BSUID Attributes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type
      </th>

      <th>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Outgoing Message
      </td>

      <td>
        ```json
        {
          "app": "Highbreed",
          "timestamp": 1776944128172,
          "version": 2,
          "type": "message-event",
          "payload": {
            "id": "cc3651a4-493b-4a38-b867-c547af202259",
            "gsId": "793df8da-2283-4774-a861-c2ffbae83823",
            "type": "sent",
            "destination": "917506080480",
            "payload": {
              "ts": 1776944126
            },
            "conversation": {
              "id": "05c0fb064921e533f66798cc17f8e5ff",
              "expiresAt": 1776944126,
              "type": "authentication"
            },
            "pricing": {
              "policy": "PMP",
              "category": "authentication",
              "type": "regular"
            },
            "userId": "IN.1648738043044942"
          }
        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        Incoming Message
      </td>

      <td>
        ```json
        {
          "app": "Highbreed",
          "timestamp": 1776944344359,
          "version": 2,
          "type": "message",
          "payload": {
            "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FFNTVCQzgxQzNBQUExQzUwMEMA",
            "source": "917506080480",
            "type": "text",
            "payload": {
              "text": "Hello partner portal"
            },
            "sender": {
              "phone": "917506080480",
              "name": "Avadhoot Yadav",
              "country_code": "91",
              "dial_code": "7506080480",
              "userId": "IN.1648738043044942"
            }
          }
        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        Coex Outgoing Message
      </td>

      <td>
        ```json
        {
          "app": "pirate",
          "timestamp": 1778217168716,
          "version": 2,
          "type": "message-event",
          "payload": {
            "id": "8d0e9a05-e049-4930-9d21-557f047d0921",
            "gsId": "0614a4df-13f1-4948-87f0-06c980ac5796",
            "type": "read",
            "destination": "917506080480",
            "payload": {
              "ts": 1778217167
            },
            "userId": "IN.3724117084395812"
          }
        }

        ```
      </td>
    </tr>

    <tr>
      <td>
        Coex Incoming Message
      </td>

      <td>
        ```json
        {
          "app": "pirate",
          "timestamp": 1778217320707,
          "version": 2,
          "type": "message",
          "payload": {
            "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FDM0NBQUQ2RUY0REMzQzk1NzIA",
            "source": "917506080480",
            "type": "text",
            "payload": {
              "text": "Ki haal chaal"
            },
            "sender": {
              "phone": "917506080480",
              "name": "Avadhoot Yadav",
              "country_code": "91",
              "dial_code": "7506080480",
              "userId": "IN.3724117084395812"
            }
          }
        }

        ```
      </td>
    </tr>

    <tr>
      <td>
        Voice Template Message
      </td>

      <td>
        ```json
        {
           "app":"Raigad",
           "timestamp":1778240807924,
           "version":2,
           "type":"message-event",
           "payload":{
              "id":"aeaa3485-321c-4e50-9d4d-506cc8d1daaa",
              "gsId":"58af2766-ddf5-4f78-9aa4-3cb075db5038",
              "type":"delivered",
              "destination":"918888998545",
              "payload":{
                 "ts":1778240806
              },
              "userId":"IN.3757610504379803"
           }
        }

        ```
      </td>
    </tr>
  </tbody>
</Table>

<br />

<br />

<br />

# V3 Subscription Events with BSUID Attributes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type
      </th>

      <th>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Outgoing Message
      </td>

      <td>
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
                        "user_id": "IN.1648738043044942",
                        "wa_id": "917506080480"
                      }
                    ],
                    "messaging_product": "whatsapp",
                    "metadata": {
                      "display_phone_number": "919355040978",
                      "phone_number_id": "269033402967482"
                    },
                    "statuses": [
                      {
                        "conversation": {
                          "expiration_timestamp": "1776944126",
                          "id": "05c0fb064921e533f66798cc17f8e5ff",
                          "origin": {
                            "type": "authentication"
                          }
                        },
                        "gs_id": "793df8da-2283-4774-a861-c2ffbae83823",
                        "id": "cc3651a4-493b-4a38-b867-c547af202259",
                        "meta_msg_id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAERgSRUJFMTZDNjI5NjEyNUFBMDM0AA==",
                        "pricing": {
                          "billable": true,
                          "category": "authentication",
                          "pricing_model": "PMP",
                          "type": "regular"
                        },
                        "recipient_id": "917506080480",
                        "recipient_user_id": "IN.1648738043044942",
                        "status": "sent",
                        "timestamp": "1776944126"
                      }
                    ]
                  }
                }
              ],
              "id": "293928007134319"
            }
          ],
          "gs_app_id": "4005ef9e-581e-41f4-9b04-e0797e0463d2",
          "object": "whatsapp_business_account"
        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        Incoming Message
      </td>

      <td>
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
                        "user_id": "IN.1648738043044942",
                        "wa_id": "917506080480"
                      }
                    ],
                    "messages": [
                      {
                        "from": "917506080480",
                        "from_user_id": "IN.1648738043044942",
                        "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0FFNTVCQzgxQzNBQUExQzUwMEMA",
                        "text": {
                          "body": "Hello partner portal"
                        },
                        "timestamp": "1776944342",
                        "type": "text"
                      }
                    ],
                    "messaging_product": "whatsapp",
                    "metadata": {
                      "display_phone_number": "919355040978",
                      "phone_number_id": "269033402967482"
                    }
                  }
                }
              ],
              "id": "293928007134319"
            }
          ],
          "gs_app_id": "4005ef9e-581e-41f4-9b04-e0797e0463d2",
          "object": "whatsapp_business_account"
        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        Coex Outgoing Message from WhatsApp Business App
      </td>

      <td>
        ```json
        {
          "entry": [
            {
              "changes": [
                {
                  "field": "smb_message_echoes",
                  "value": {
                    "contacts": [
                      {
                        "user_id": "IN.3724117084395812",
                        "wa_id": "917506080480"
                      }
                    ],
                    "message_echoes": [
                      {
                        "from": "918588096070",
                        "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAERgUMkE4NDk2OTk2MzEwQkJENDZFNEQA",
                        "text": {
                          "body": "Heyy avi, sorry active was false"
                        },
                        "timestamp": "1778216475",
                        "to": "917506080480",
                        "to_user_id": "IN.3724117084395812",
                        "type": "text"
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
      </td>
    </tr>

    <tr>
      <td>
        Coex Outgoing Message from Gupshup API
      </td>

      <td>
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
                        "user_id": "IN.3724117084395812",
                        "wa_id": "917506080480"
                      }
                    ],
                    "messaging_product": "whatsapp",
                    "metadata": {
                      "display_phone_number": "918588096070",
                      "phone_number_id": "1005385572668707"
                    },
                    "statuses": [
                      {
                        "conversation": {
                          "id": "01ca6fe72b4ad6fc445b1b61b46164e3",
                          "origin": {
                            "type": "service"
                          }
                        },
                        "gs_id": "50a770da-760c-40d8-a37a-63674281a369",
                        "id": "202fe5b0-ce23-4d6f-8b98-140231823104",
                        "meta_msg_id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAERgSMEY0QjBGRUNEODY1NTNEN0E2AA==",
                        "pricing": {
                          "billable": false,
                          "category": "service",
                          "pricing_model": "PMP",
                          "type": "free_customer_service"
                        },
                        "recipient_id": "917506080480",
                        "recipient_user_id": "IN.3724117084395812",
                        "status": "delivered",
                        "timestamp": "1778216901"
                      }
                    ]
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
      </td>
    </tr>

    <tr>
      <td>
        Coex Incoming Message
      </td>

      <td>
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
                        "user_id": "IN.3724117084395812",
                        "wa_id": "917506080480"
                      }
                    ],
                    "messages": [
                      {
                        "from": "917506080480",
                        "from_user_id": "IN.3724117084395812",
                        "id": "wamid.HBgMOTE3NTA2MDgwNDgwFQIAEhgUM0E0NzA1QjBERjczQ0RGRDZENTMA",
                        "text": {
                          "body": "Heyy no problem"
                        },
                        "timestamp": "1778216789",
                        "type": "text"
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
      </td>
    </tr>

    <tr>
      <td>
        Voice Template Message
      </td>

      <td>
        ```json
        {
           "entry":[
              {
                 "changes":[
                    {
                       "field":"messages",
                       "value":{
                          "contacts":[
                             {
                                "user_id":"IN.3757610504379803",
                                "wa_id":"918888998545"
                             }
                          ],
                          "messaging_product":"whatsapp",
                          "metadata":{
                             "display_phone_number":"918588096355",
                             "phone_number_id":"1127818030413076"
                          },
                          "statuses":[
                             {
                                "conversation":{
                                   "id":"1434dcb5b4535510030c9db8047ddfcf",
                                   "origin":{
                                      "type":"marketing_lite"
                                   }
                                },
                                "gs_id":"58af2766-ddf5-4f78-9aa4-3cb075db5038",
                                "id":"aeaa3485-321c-4e50-9d4d-506cc8d1daaa",
                                "meta_msg_id":"wamid.HBgMOTE4ODg4OTk4NTQ1FQIAERgSRTdGRjc1Q0E3RDYyNUVDNTBBAA==",
                                "pricing":{
                                   "billable":true,
                                   "category":"marketing_lite",
                                   "pricing_model":"PMP",
                                   "type":"regular"
                                },
                                "recipient_id":"918888998545",
                                "recipient_user_id":"IN.3757610504379803",
                                "status":"delivered",
                                "timestamp":"1778240806"
                             }
                          ]
                       }
                    }
                 ],
                 "id":"731055923430007"
              }
           ],
           "gs_app_id":"c9e6265c-7809-464a-9e4d-5c8311be6f2c",
           "object":"whatsapp_business_account"
        }

        ```
      </td>
    </tr>
  </tbody>
</Table>

<br />

<br />

<br />

## Other impacted webhooks :

## user_preferences (Both v2 and v3 events are supported)

If enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , username in the v3 webhook

If enableBSUID is is true then the v2 payload will also contain userid , parent_user_id along with existing payload in v2 webhook

### Example of v2 payload when enableBSUID is true :

```
{
  "app": "<appName>",
  "appId": "<appId>",
  "timestamp": <timestamp>,
  "version": 2,
  "type": "preference-event",
  "payload": {
    "type": "user_preferences",
    "payload": {
      "user_preferences": [
        {
          "wa_id": "919297545638",
          "userid": "user_id",//added
          "parent_user_id" : "parent_user_id"
          "detail": "User requested to stop marketing messages",
          "category": "marketing_messages",
          "value": "stop",
          "timestamp": <timestamp>
        }
      ]
    }
  }
}
```

<br />

<br />

<br />

## VOICE webhooks (Only v3 webhook supported) :

### Call Permission Request v3 webhook

if enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , username , from_user_id , from_parent_user_id in the Call Permission Request v3 webhook

### Business-initiated connected calls webhooks :

if enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , profile , to_user_id , to_parent_user_id in the v3 webhook

### User-initiated connected calls webhooks :

if enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , username , from_user_id , from_parent_user_id in the v3 webhook

### Business-initiated terminated calls webhooks :

if enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , profile , to_user_id , to_parent_user_id in the v3 webhook

### User-initiated terminated calls webhooks :

if enableBSUIDV3 is not enabled then it will not contain : userid , parent_user_id , profile , to_user_id , to_parent_user_id in the v3 webhook

### Business-initiated calls status webhooks :

If enableBSUIDV3 is not enabled then it will not contain : recipient_user_id , recipient_parent_user_id , contacts in the v3 webhook

<br />

## Coexistence ( Only v3 webhook supported ):

### For smb_message_echoes webhook :

if enableBSUIDV3 is not enabled then it will not contain : contacts , to_user_id , to_parent_user_id in the v3 webhook

<br />

<br />

<br />

<br />
