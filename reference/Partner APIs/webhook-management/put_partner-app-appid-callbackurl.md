---
title: Set Callback Url
excerpt: Use this API to set callback URL for your Gupshup App
api:
  file: set-callback-url.json
  operationId: put_partner-app-appid-callbackurl
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 🚧 ⚠We are going to be deprecating this API soon, we request you that you start using the [subscription API](/reference/setsubscription-api-v3#/), as it provides you with a granular control for event management on your callback URL

Once set you will get DLR events on that callback URL.

### Parameters

| Parameters    | Value                   | Description                                                                                                           |
| :------------ | :---------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application                                                                                      |
| appId         | `{{APP_ID}}`            | Unique Identifier for Gupshup App                                                                                     |
| callbackUrl   | `{{Callback_URL}}`      | [Learn how you can successfully set a callback URL for an app.](https://docs.gupshup.io/docs/set-webhookcallback-url) |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/callbackUrl' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'callbackUrl={{CALLBACK_URL}}'
```

### Sample Response

```json
{
  "status": "success"
}   
```

### Status Codes

| Status Code | Response                                                            | Comments               |
| :---------- | :------------------------------------------------------------------ | :--------------------- |
| **Success** |                                                                     |                        |
| 200         | `{       "status": "success"   }`                                   |                        |
| **Error**   |                                                                     |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`   | 10 Requests per Minute |
| 500         | `{  "status": "error",  "message": "Error updating callback URL" }` | For any Internal Error |