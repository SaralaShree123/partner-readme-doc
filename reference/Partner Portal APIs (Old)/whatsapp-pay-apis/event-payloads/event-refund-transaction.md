---
title: Event - Refund Transaction
excerpt: The partners will receive this event on successful payment transactions.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
```
{
    "entry": [
        {
            "changes": [
                {
                    "field": "messages",
                    "value": {
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "{{sourceNo}}",
                            "phone_number_id": "174027659133661"
                        },
                        "statuses": [
                            {
                                "id": "wamid.HBgMOTE4OTEwODY0MzcxFQIAEhgKMTY5MTI4Nzc2NwA=",
                                "payment": {
                                    "amount": {
                                        "offset": 100,
                                        "value": 100
                                    },
                                    "currency": "INR",
                                    "reference_id": "BM345A-16",
                                    "transaction": {
                                        "amount": {
                                            "offset": 1000,
                                            "value": 1000
                                        },
                                        "created_timestamp": 1707287109,
                                        "currency": "INR",
                                        "id": "order_NXtDlCJBziFTnj",
                                        "refunds": [
                                            {
                                                "amount": {
                                                    "offset": 100,
                                                    "value": 100
                                                },
                                                "created_timestamp": 1707287160,
                                                "id": "rfnd_NXtF8rj6lP7Ag7",
                                                "speed_processed": "normal",
                                                "status": "completed",
                                                "updated_timestamp": 1707287228
                                            }
                                        ],
                                        "status": "captured",
                                        "type": "razorpay",
                                        "updated_timestamp": 1707287109
                                    }
                                },
                                "recipient_id": "{{destinationNo}}",
                                "status": "captured",
                                "timestamp": "1707287230",
                                "type": "payment"
                            }
                        ]
                    }
                }
            ],
            "id": "174161222453488"
        }
    ],
    "gs_app_id": "GUPSHUP_APP_ID",
    "object": "whatsapp_business_account"
}
```
