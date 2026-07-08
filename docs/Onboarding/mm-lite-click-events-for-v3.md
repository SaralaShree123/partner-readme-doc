---
title: MM LITE click events for v3
deprecated: false
hidden: true
metadata:
  robots: index
---
We deliver a webhook payload when users click on the body or call-to-action of your marketing message. You can subscribe to this webhook to capture this data and use it to inform your campaign decisions.

# Webhook Event

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
                            "display_phone_number": "919355040978",
                            "phone_number_id": "269033402967482"
                        },
                        "user_actions": [
                            {
                                "action_type": "marketing_messages_link_click",
                                "marketing_messages_link_click_data": {
                                    "click_component": "CTA",
                                    "click_id": "IwAR7aCUKUapCC35tsF7QFRxKy9QDMU0TeBDg7Y3FoU0x2ct_M3X_Gtka8QxLEWA_wapm_ZGRhNzM4ZDYtNTlhNy00OGE5LThhZWEtZmY5MDgzMjA1ZGQ4",
                                    "tracking_token": "AI@AQJDlawEsjXDxNNHvxMB9McpYs2wTRTsrWKQC28lFj5vu78y5WMT-J1DW9QWT8kytfhTi5hasXSA1jv9zN_D1h91"
                                },
                                "timestamp": "1755665204"
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
```

<br />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Field Type
      </th>

      <th>
        Field Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        action_type
      </td>

      <td>
        Required (String)
      </td>

      <td>
        Name of the action
      </td>
    </tr>

    <tr>
      <td>
        timestamp
      </td>

      <td>
        Required (Unix timestamp)
      </td>

      <td>
        Timestamp of when the event happened
      </td>
    </tr>

    <tr>
      <td>
        click_component
      </td>

      <td>
        Optional (Enum)
      </td>

      <td>
        The click action

        Can either be cta or body
      </td>
    </tr>

    <tr>
      <td>
        click_id
      </td>

      <td>
        Optional (String)
      </td>

      <td>
        The unique identifier for the click. Is also appended to the original url when the user visits the url.
      </td>
    </tr>

    <tr>
      <td>
        tracking_token
      </td>

      <td>
        Optional (String)
      </td>

      <td>
        Internal Meta token for processing and tracking
      </td>
    </tr>

    <tr>
      <td>
        product_id
      </td>

      <td>
        Optional (String)
      </td>

      <td>
        ID of the product, if it was assigned in Ads Manager or Marketing API.
      </td>
    </tr>
  </tbody>
</Table>
