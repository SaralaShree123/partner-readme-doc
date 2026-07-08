---
title: Payment Status Check API
excerpt: Use this API to check payment status of WhatsApp Pay Transactions.
api:
  file: partner-release-85-apis.json
  operationId: get_partner-app-appid-payments-payment-configuration-reference-id
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameter

| Key                   | Description                                                      | Constraints                                                                              |
| :-------------------- | :--------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| PARTNER_TOKEN         | JWT Token issues post Partner login                              | It should be a valid Partner JWT Token.                                                  |
| appId                 | AppId of the app for which the embed link needs to be generated. | It should be a valid appId associated with the account.                                  |
| payment_configuration | Payment config is used for WhatsApp pay transaction              | Valid payment configuration must be configured in the meta.                              |
| reference_id          | Unique ID to identify each transaction                           | It should be a valid ID used for a WhatsApp pay transaction using order details message. |

## Sample Request

```curl
curl --location --request GET '{{partner_portal_base_url}}/partner/app/:appId/payments/{{payment_configuration}}/{{reference_id}}' \
--header 'token: {{PARTNER_TOKEN}}'
```

## Sample Response

```
{
    "payments": [
        {
            "reference_id": "BM345A-16",
            "status": "CAPTURED",
            "amount": {
                "offset": 100,
                "value": 100
            },
            "currency": "INR",
            "transactions": [
                {
                    "id": "order_NXtDlCJBziFTnj",
                    "type": "razorpay",
                    "status": "success",
                    "created_timestamp": 1707287109,
                    "updated_timestamp": 1707287109,
                    "refunds": [
                        {
                            "id": "rfnd_NXtF8rj6lP7Ag7",
                            "amount": {
                                "offset": 100,
                                "value": 100
                            },
                            "speed_processed": "normal",
                            "status": "completed",
                            "created_timestamp": 1707287160,
                            "updated_timestamp": 1707287228
                        }
                    ],
                    "amount": {
                        "offset": 100,
                        "value": 100
                    },
                    "currency": "INR"
                }
            ]
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Comment                                                  |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                          |
| 200         | `{ "payments": [ { "reference_id": "BM345A-16", "status": "CAPTURED", "amount": { "offset": 100, "value": 100 }, "currency": "INR", "transactions": [ { "id": "order_NXtDlCJBziFTnj", "type": "razorpay", "status": "success", "created_timestamp": 1707287109, "updated_timestamp": 1707287109, "refunds": [ { "id": "rfnd_NXtF8rj6lP7Ag7", "amount": { "offset": 100, "value": 100 }, "speed_processed": "normal", "status": "completed", "created_timestamp": 1707287160, "updated_timestamp": 1707287228 } ], "amount": { "offset": 100, "value": 100 }, "currency": "INR" } ] } ] }` | Successfully.                                            |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                          |
| 400         | `{ "status": "error", "message": "Authentication Failed" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Either the user or lang in the query parameter is empty. |
| 400         | `{ "status": "error", "message": "(#134006) Reference id is invalid" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | For invalid or wrong reference id.                       |
| 400         | `{ "status": "error", "message": "(#134009) Payment configuration id is invalid" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | For invalid or wrong payment configuration.              |
| 401         | `{ "status": "error", "message": "Authentication Failed" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | When API key authentication fails.                       |
| 429         | `{ "status": "error", "message": "Too Many Requests" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | When the request rate limit exceeds.                     |