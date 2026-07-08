---
api:
  file: token-apis.json
  operationId: post_partner-account-login
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  ###

  Note:

  The partner token will be used as authorization in other Partner APIs. Currently, the expiry for the token is **24 hours**.

  Rate limit is 10 requests per 60 seconds
</Callout>

<br />

### Request Parameters

| Key      | Value              | Description                                                   |
| :------- | :----------------- | :------------------------------------------------------------ |
| Email    | {{EMAIL}}          | Email address through partner has signed up on partner portal |
| Password | {{CLIENT\_SECRET}} | Client Secret set by the partner on the partner portal        |

### Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/account/login' \
--header 'Accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'email={{EMAIL}}' \
--data-urlencode 'password={{CLIENT_SECRET}}'
```

### Sample Response

```json
{
  "token": "{{PARTNER_TOKEN}}",
  "id": 1**3,
  "name": "gupshup",
  "terms_read": true,
  "admin": true,
  "email": "peter.parker@zylker.com",
  "activationRead": false,
  "billingType": "PREPAID",
  "contactName": "peter",
  "phoneNumber": "898",
  "enableCustomer": false,
  "enableWallet": true,
  "enableInrWallet": false,
  "enableLoaderWallet": false,
  "enableAppOnboarding": true,
  "isTpp": false,
  "onboardEnabled": false
}
```

<br />
