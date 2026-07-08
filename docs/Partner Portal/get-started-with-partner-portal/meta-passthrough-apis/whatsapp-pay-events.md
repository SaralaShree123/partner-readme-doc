---
title: WhatsApp Pay Events
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Partners must subscribe to the events using the [Set Subscription](https://partner-docs.gupshup.io/reference/setsubscription-api-v3) APIs from Gupshup.

## The types of WhatsApp Pay Events

* Payment Transaction
* Refund Transaction

### Payment Transaction

Upon successful payment transactions, the partners receive notification of this event.

```json Event-Transaction
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
                                "id": "wamid.HBgMOTE4OTEwODY0MzcxFQIAEhgKMTczMDIzOTczMQA=",
                                "payment": {
                                    "amount": {
                                        "offset": 100,
                                        "value": 100
                                    },
                                    "currency": "INR",
                                    "reference_id": "BM345A-15",
                                    "transaction": {
                                        "amount": {
                                            "offset": 1000,
                                            "value": 1000
                                        },
                                        "created_timestamp": 1706940110,
                                        "currency": "INR",
                                        "id": "order_NWIfb9Ph4cq3k7",
                                        "status": "captured",
                                        "type": "razorpay",
                                        "updated_timestamp": 1706940110
                                    }
                                },
                                "recipient_id": "{{destinationNo}}",
                                "status": "captured",
                                "timestamp": "1706940112",
                                "type": "payment"
                            }
                        ]
                    }
                }
            ],
            "id": "174161222453488"
        }
    ],
    "gs_app_id": "{{GUPSHUP_APP_ID}}",
    "object": "whatsapp_business_account"
}
```

### Refund Transaction

Upon successful refund transactions, the partners receive webhook event.

```json Event-Refund
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

## Common payload object description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        This is Gupshup Message Id for message-event types: `enqueued` and `failed`
        In case of `failed` please check the below [Sync](https://partner-docs.gupshup.io/docs/message-events#/sync-failed) and [Async](https://partner-docs.gupshup.io/docs/message-events#/async-failed) section.
        For the DLR events `sent`, `delivered`, `read` it is always WhatsApp Message ID.
      </td>

      <td>
        `59f8db90-c37e-4408-90ab-cc54ef8246ad`
        OR
        `gBEGkYaYVSEEAgnZxQ3JmKK6Wvg`
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        The updated status of a template. Possible values are:  `captured`, `completed`
      </td>

      <td>
        captured/completed
      </td>
    </tr>

    <tr>
      <td>
        `gsId`
      </td>

      <td>
        This is Gupshup Message Id and only present for message-event types: DLR events: `sent`, `delivered`, `read`.
      </td>

      <td>
        `59f8db90-c37e-4408-90ab-cc54ef8246ad`
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        The type of message-event received on your webhook
        Must be one of these: `razorpay`
      </td>

      <td>
        Refer to the description given below.
      </td>
    </tr>

    <tr>
      <td>
        `destination`
      </td>

      <td>
        User's phone number
      </td>

      <td>
        918x98xx21x4
      </td>
    </tr>

    <tr>
      <td>
        `ts`
      </td>

      <td>
        The timestamp of the event in seconds. This property is received for events `sent`, `delivered`, and `read`.
      </td>

      <td>
        1585344475
      </td>
    </tr>
  </tbody>
</Table>