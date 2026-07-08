---
title: Send order details session message
excerpt: Use this API to send order details session message
api:
  file: partner-whatsapp-pay-apis.json
  operationId: post_partner-app-appid-v3-message
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Data Types</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Require/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Should be a valid Partner App Access Token</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Id of the app</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>The ID should be a valid app Id of Gupshup.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>to</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{DESTINATION}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Destination phone no. where the message needs to be sent</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type of message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be interactive for order details message</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>header</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{HEADER}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message header</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Header is optional in case of order details session message.</li>
<li>If the header is present can be either text or image</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>footer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{FOOTER}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message footer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>reference_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{REFERENCE_ID_VALUE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>unique value for each transaction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be unique for each transaction and maintained properly will be required to retrieve transaction status</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{CURRENCY}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency involved in the transaction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be INR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offset and value</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{OFFSET}}<br>{{VALUE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>use to represent the amount involved</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>offset Must be 100 for INR.</li>
<li>value Positive integer representing the amount value multiplied by offset. For example, ₹12.34 has a value of 1234</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>subtotal</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{SUBTOTAL}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>total amount excluding discount shipping and tax</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The value must be equal to the sum of the amount.value * amount.quantity</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>total_amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{TOTAL_AMOUNT}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>total amount to be paid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>total_amount.value must be equal to subtotal.value + tax.value + shipping.value - discount.value.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payment_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PAYMENT-GATEWAY-TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payment gateway in use</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be razorpay or payu</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>configuration_name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PAYMENT_CONFIG_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name of of the payment config to be used</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be configure in meta in order to complete the transaction</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location -g --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-urlencode '{
    "messaging_product": "whatsapp",
    "to": {{DESTINATION}},
    "type": "{{TYPE}}",
    "recipient_type": "individual",
    "interactive": {
        "type": "order_details",
        "header": {
            "type": "image",
            "image": {
                "link": "{{media link}}"
            }
        },
        "body": {
            "text": "your-text-body-content"
        },
        "footer": {
            "text": "your-text-footer-content"
        },
        "action": {
            "name": "review_and_pay",
            "parameters": {
                "reference_id": "{{reference-id-value}}",
                "type": "digital-goods",
                "payment_settings": [
                    {
                        "type": "payment_gateway",
                        "payment_gateway": {
                            "type": "{{payment-gateway-type}}",
                            "configuration_name": "{{payment-config-id}}"
                        }
                    }
                ],
                "currency": "INR",
                "total_amount": {
                    "offset": 100,
                    "value": 100
                },
                "order": {
                    "status": "pending",
                    "catalog_id": "the-catalog_id",
                     "discount": {
                        "offset": 100,
                        "value": 800
                    },
                    "items": [
                        {
                            "retailer_id": "1234567",
                            "name": "Product name, for example bread",
                            "amount": {
                                "value": 400,
                                "offset": 100
                            },
                            "quantity": 1
                        }
                    ],
                    "shipping": {
                        "offset": 100,
                        "value": 0
                    },
                    "subtotal": {
                        "offset": 100,
                        "value": 400
                    },
                    "tax": {
                        "offset": 100,
                        "value": 500
                    }
                }
            }
        }
    }='
```

## Sample Response

```json
{
    "messages": [
        {
            "id": "GUPSHUP_MESSAGE_ID"
        }
    ],
    "messaging_product": "whatsapp",
    "contacts": [
        {
            "input": "DESTINATION_PHONE_NO",
            "wa_id": "DESTINATION_PHONE_NO"
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                      | Comments                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                               |                                                 |
| 200         | `{       "messages": [           {               "id": "GUPSHUP_MESSAGE_ID"           }       ],       "messaging_product": "whatsapp",       "contacts": [           {               "input": "DESTINATION_PHONE_NO",               "wa_id": "DESTINATION_PHONE_NO"           }       ]   }` |                                                 |
| **Error**   |                                                                                                                                                                                                                                                                                               |                                                 |
| 400         | `{       "message": "Callback Billing must be enabled for this API",       "status": "error"   }`                                                                                                                                                                                             | if Callback billing is not enabled for the app  |
| 400         | `{       "message": "The provided app is not of the expected type for this API. Please ensure that the app is on the cloud.",       "status": "error"   }`                                                                                                                                    | if the app is an on-prem app instead of a cloud |
| 400         | `{       "message": "Invalid App Details",       "status": "error"   }`                                                                                                                                                                                                                       | if app details are not found                    |