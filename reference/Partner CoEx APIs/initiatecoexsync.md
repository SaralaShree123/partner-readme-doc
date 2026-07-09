---
api:
  file: coex_new_contact_sync_api.json
  operationId: initiateCoexSync
hidden: false
---
# CoEx Event Guide

[/update/docs/coexistence-events](/update/docs/coexistence-events)

<br />

# Description

1. **Method/path**: POST /app/:appId/coex/sync (optional trailing slash supported).
2. **Full URL segment**: BASE_URL/partner/app/:appId/coex/sync (context path /partner, controller prefix /app).
3. **Auth**: Role PARTNER_APP (see Authentication above).
4. **Content-Type**: application/x-www-form-urlencoded.
5. **Rate limit**: 10 requests per 60 seconds

<br />

# Note:

Both smb_app_state_sync and history synchronization can be triggered only once, and must be initiated within 24 hours of onboarding.

<br />

# Request example

## Contacts sync (smb_app_state_sync):

```curl
curl --location --request POST '{{BASE_URL}}/partner/app/{{APP_ID}}/coex/sync' \
  --header 'Authorization: Bearer {{PARTNER_APP_TOKEN}}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'syncType=smb_app_state_sync'
```

<br />

## Message history sync (history):

```curl
curl --location --request POST '{{BASE_URL}}/partner/app/{{APP_ID}}/coex/sync' \
  --header 'Authorization: Bearer {{PARTNER_APP_TOKEN}}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'syncType=history'
```

<br />

# Steps to use this API

1. Make the API call with the desired syncType
2. Then you will receive an event from Meta on the webhook as mentioned in the document <Anchor label="here" target="_blank" href="https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users#synchronizing-whatsapp-business-app-data">here</Anchor>

# Purpose of Request ID

The request ID is from meta. If you don't receive the respective event after the API call from meta, then this ID can be used to raise the missing event issue with meta.

<br />

# Response example

## Success

```curl
{
  "data": {
    "messaging_product": "whatsapp",
    "request_id": "<REQUEST_ID>"
  },
  "status": "success"
}
```

<br />

## Sync modes (syncType):

| Value              | Purpose                                                                                                                                                                       |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| smb_app_state_sync | Initiates contacts synchronization. On success, smb_app_state_sync webhooks describe current WhatsApp Business App contacts; future contact changes trigger further webhooks. |
| history            | Initiates message history synchronization. If the business opts to share history, history webhooks describe messages in the agreed time range.                                |

<br />

## Request parameters

| Key             | Description                       | Values                                                                                   | Data type | Required / optional | Constraints                                                                                             |
| :-------------- | :-------------------------------- | :--------------------------------------------------------------------------------------- | :-------- | :------------------ | :------------------------------------------------------------------------------------------------------ |
| **Path**        |                                   |                                                                                          |           |                     |                                                                                                         |
| appId           | WhatsApp / Partner app identifier | UUID or app id string                                                                    | String    | Required            | Must be an app linked to the authenticated partner; portal checks access before proxying.               |
| **Headers**     |                                   |                                                                                          |           |                     |                                                                                                         |
| Authorization   | Partner App token                 | Bearer \{\{Partner App JWT}} or allowed alternatives per route (sk_, hardened JWT, etc.) | String    | Required            | Must satisfy @Authenticated + PARTNER_APP.                                                              |
| Content-Type    | Media type                        | application/x-www-form-urlencoded                                                        | String    | Required            | Form body carries syncType.                                                                             |
| **Body (form)** |                                   |                                                                                          |           |                     |                                                                                                         |
| syncType        | Sync mode                         | smb_app_state_sync \ history                                                             | String    | Required            | Case-insensitive match; other values → 400 with message syncType must be smb_app_state_sync or history. |
|                 |                                   |                                                                                          |           |                     |                                                                                                         |

<br />

## Status codes

| Status code | Meaning                  | Comments                                                                                                                        |
| :---------- | :----------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| 200         | Success                  | Body and semantics mirror the upstream WASS response when the proxy call succeeds (e.g. shape above).                           |
| 400         | Bad Request              | Missing/invalid syncType; app not linked to partner; missing API key for app; invalid parameter from portal validation.         |
| 401         | Unauthorized             | Missing or invalid authentication for Partner App route.                                                                        |
| 403         | Forbidden                | Caller lacks PARTNER_APP or relevant permissions.                                                                               |
| 429         | Too many requests        | Rate limit exceeded (10 / 60s for this route).                                                                                  |
| 4xx/5xx     | Upstream or client error | When WASS returns a non-success, the portal passes through status and body via the same helper used for other WhatsApp proxies. |
| 500         | Internal server error    | Unexpected failure in portal after proxy or unhandled exception.                                                                |

<br />