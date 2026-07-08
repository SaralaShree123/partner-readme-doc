---
summary: WhatsApp Groups Sample Events
title: WhatsApp Groups Sample Events
deprecated: false
hidden: true
metadata:
  robots: index
---
# Group Account level Events

## Create Event 

```
{
    "entry": [
        {
            "changes": [
                {
                    "field": "group_lifecycle_update",
                    "value": {
                        "groups": [
                            {
                                "description": "This is Group for gupshup",
                                "group_id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYzNDIzMTQ4MDxxxxx",
                                "invite_link": "https://chat.whatsapp.com/BwEEU01Yuod1zPiapnbXqO ",
                                "join_approval_mode": "auto_approve",
                                "request_id": "6E485DA48931CFDD9CCDF97DE6FFF1B4",
                                "subject": "Test PP Grp",
                                "timestamp": 1761886979,
                                "type": "group_create"
                            }
                        ],
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "918929874278",
                            "phone_number_id": "101372823049689"
                        }
                    }
                }
            ],
            "id": "104505526065633"
        }
    ],
    "gs_app_id": "a41b30f4-d202-xxxx-911e-3a8fbfbfb797",
    "object": "whatsapp_business_account"
}
```

## Group Participant Add Using Invite Link

```
{
    "entry": [
        {
            "changes": [
                {
                    "field": "group_participants_update",
                    "value": {
                        "groups": [
                            {
                                "added_participants": [
                                    {
                                        "wa_id": "917385180297"
                                    }
                                ],
                                "group_id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYzNDIzMTQ4MDkxxxxx",
                                "reason": "invite_link",
                                "timestamp": 1761888373,
                                "type": "group_participants_add"
                            }
                        ],
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "918929874278",
                            "phone_number_id": "101372823049689"
                        }
                    }
                }
            ],
            "id": "104505526065633"
        }
    ],
    "gs_app_id": "a41b30f4-d202-xxxx-911e-3a8fbfbfb797",
    "object": "whatsapp_business_account"
}
```

<br />

# Message Type Events

## Incomming Event

```
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
                                    "name": "Rahul"
                                },
                                "wa_id": "917385180297"
                            }
                        ],
                        "messages": [
                            {
                                "from": "917385180297",
                                "group_id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYzNDIzMTQ4MDkxxxxxx",
                                "id": "wamid.HBgSMTIwMzYzNDIzMTQ4MDkxNzE2FQgAEhgWM0VCMDNGOEE5MzZBNDcyQkZCN0I5QxwYDDkxxxxNzM4NTE4MDI5NxUCAAA=",
                                "text": {
                                    "body": "hii"
                                },
                                "timestamp": "1761899474",
                                "type": "text"
                            }
                        ],
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "918929874278",
                            "phone_number_id": "101372823049689"
                        }
                    }
                }
            ],
            "id": "104505526065633"
        }
    ],
    "gs_app_id": "a41b30f4-d202-xxxx-911e-3a8fbfbfb797",
    "object": "whatsapp_business_account"
}
```

<br />

<br />
