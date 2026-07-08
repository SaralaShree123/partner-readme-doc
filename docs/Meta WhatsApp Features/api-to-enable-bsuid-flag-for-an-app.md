---
title: API to enable BSUID flag for an app
excerpt: >-
  This document describes the Partner Portal API that updates Business Scoped
  User ID (BSUID) flags on a WhatsApp app’s configuration on v2 or/and v3
  subscriptions. You can enable eithter 1 or both subscriptions thorugh this
  API.
deprecated: false
hidden: false
metadata:
  robots: index
---
If you want to enable BSUID for v2 incoming messages and webhooks, pass enableBSUID": true

If you want to enable BSUID for v3 incoming messages and webhooks, pass enableBSUIDV3": true

You can even pass both for setting both to true.

Once enabled, all incoming DLR and message webhooks will be passed to your respective subscription including the BSUID of the user along with phone number, wherever it is received from Meta. This is applicable only for events coming post the flag is enabled.

You can also disable the flag by passing enableBSUID or enableBSUIDV3 : false

<Callout icon="📘" theme="info">
  ###

  BSUID flag can only be enabled for live apps
</Callout>

<br />

### Rate limit: 10 requests per 60 seconds per route

## Request example

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/[APP_ID]/config/bsuid'  \
--header 'Authorization: Bearer [PARTNER_APP_TOKEN]'  \
--header 'Content-Type: application/json'  \
--data '{ "enableBSUID": true, "enableBSUIDV3": true }'
```

## &#x20;Set only one flag if needed:

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/[APP_ID]/config/bsuid'  \
--header 'Authorization: Bearer [PARTNER_APP_TOKEN]'  \
--header 'Content-Type: application/json'  \
--data '{ "enableBSUIDV3": true }'
```

## Response example

### Response

```json
{ "status": "success" }
```

### Example – missing both flags (400):

```json
{ 
  "status": "error",
	"message": "At least one of enableBSUID or enableBSUIDV3 must be provided" 
}
```

<br />

[Read more about the BSUID webhooks ](https://support.gupshup.io/hc/en-us/articles/55873677826713)
