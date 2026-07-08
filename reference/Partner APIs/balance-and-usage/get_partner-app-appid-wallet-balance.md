---
title: Get Wallet Balance
excerpt: >-
  Use this API to retrieve the wallet balance details for your partner
  application. This endpoint provides current balance, currency, and overdraft
  limit information for billing and financial monitoring.
api:
  file: partner-portal-public-apis-1.json
  operationId: get_partner-app-appid-wallet-balance
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  1. App must belong to authenticated user
  2. Rate limit: **10 requests per second**
</Callout>

### Parameters

| Parameters    | Value                   | Description                       |    |    |
| :------------ | :---------------------- | :-------------------------------- | :- | :- |
| Authorization | \{\{PARTNER_APP_TOKEN}} | Access Token for the application  |    |    |
| appId         | \{\{APP_ID}}            | Unique Identifier for Gupshup App |    |    |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/wallet/balance' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
  "status": "success",
  "walletResponse": {
    "currency": "USD",
    "currentBalance": ***.**,
    "overDraftLimit": 0
  }
}
```
