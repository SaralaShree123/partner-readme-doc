---
title: Payment Refund API
excerpt: Use this API to refund a payment of a particular reference ID.
api:
  file: partner-release-85-apis.json
  operationId: post_partner-app-appid-payments-refund
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

| Key                   | Description                                                       | Constraints                                                                          |
| :-------------------- | :---------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| PARTNER_TOKEN         | JWT Token issues post Partner login                               | Should be a valid Partner JWT Token.                                                 |
| appId                 | App ID of the app for which the embed link needs to be generated. | Should be a valid appId associated with the account.                                 |
| payment_configuration | Payment config to be used in for WhatsApp pay transaction         | Valid payment configuration must be configured in the meta                           |
| reference_id          | Unique ID to identify each transaction                            | Should be a valid id used for a whatsapp pay transaction using order details message |
| speed                 | Speed at which a refund should be processed                       | Must be instant or normal                                                            |

## Sample Request

```curl
curl --location '{{partner_portal_base_url}}/partner/app/:appId/payments/refund' \
--header 'token: {{PARTNER_TOKEN}}' \
--data '{
    "reference_id": "{{reference_id}}",
    "speed": "instant",
    "payment_config_id": "payment_config_id",
    "amount": {
        "currency": "INR",
        "value": "{{amount}}",
        "offset": "100"
    }
}'
```

## Sample Response

```
{
  "id": "refund-id",
  "status": "pending",
  "speed_processed": "normal"
}
```

## Status Codes

| Status Code | Response                                                                                           | Comment                                                                                         |
| :---------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                    |                                                                                                 |
| 200         | `{     "id": "refund-id",     "status": "pending",     "speed_processed": "normal"   }`            | The speed_processed may not be same as the one send in request as it depends on payment gateway |
| **Error**   |                                                                                                    |                                                                                                 |
| 400         | `{           "status": "error",           "message": "Authentication Failed"   }`                  | Either user or lang in query parameter is empty.                                                |
| 400         | `{       "status": "error",       "message": "(#100) The parameter reference_id is required."   }` | Incorrect or empty payment configuration                                                        |
| 400         | `{       "status": "error",       "message": "(#100) The parameter reference_id is required."   }` | Incorrect or empty reference id                                                                 |
| 401         | `{           "status": "error",           "message": "Authentication Failed"   }`                  | When API key authentication fails                                                               |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                  | When request rate limit exceeds.                                                                |