---
title: Set callback for an appID
excerpt: Use this endpoint to configure a customer callback URL for the application.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-callback
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 🚧 We are going to be deprecating this API soon, we request you that you start using the [subscription API](https://partner-docs.gupshup.io/reference/setsubscription-api-v3#/), as it provides you with a granular control for event management on your callback URL

## Parameters

| Key              | Description                                                                                                             | Constraints                                                                   |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| PARTNER\_TOKEN   | JWT Token issues post Partner login                                                                                     | Should be a valid Partner JWT Token.                                          |
| url              | url to set for custom callback                                                                                          | Should be a valid URL                                                         |
| modes            | modes for which callback should be used. Taken as comma separated values                                                | Should be any of `[NONE,READ,DELIVERED,SENT,DELETED,OTHERS,TEMPLATE,ACCOUNT]` |
| directForwarding | boolean value which is true if the events to be sent directly and false if the events need to be sent via the platform. | Should only contain true or false value.                                      |
| notifyWithPhone  | The boolean value is true if the events contain the source phone number. false otherwise.                               | Should only contain true or false value.                                      |

## Sample Request

```curl
curl --location --request PUT '{{partner_portal_base_url}}/partner/app/:appId/callback' \
--header 'token: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'url={{callback_url}}' \
--data-urlencode 'directForwarding={{directForwarding}}' \
--data-urlencode 'notifyWithPhone={{notifyWithPhone}}' \
--data-urlencode 'modes={{modes}}'
```

## Sample Response

```
{
    "status": "success",
    "callback": {
        "url" : "&lt;callback_url&gt;",
        "custom" : &lt;true/false&gt;,
        "modes" : [
            "&lt;callback_modes_list&gt;"
        ]
    }
}
```

## Status Codes

| Status Code   | Response                                                                                                                                                                                                      | Comment                                                             |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------ |
| ***Success*** |                                                                                                                                                                                                               |                                                                     |
| 200           | `{       "status": "success",       "callback": {           "url" : "<callback_url>",           "custom" : <true/false>,           "modes" : [               "<callback_modes_list>"           ]       }   }` | Custom URL set successfully.                                        |
| ***Error***   |                                                                                                                                                                                                               |                                                                     |
| 400           | `{       "status": "error",       "message": "Invalid App Details Passed"   }`                                                                                                                                | Incorrect App Id Provided.                                          |
| 429           | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                             | When the request rate limit exceeds.                                |
| 500           | `{       "status": "error",       "message": "Unable to Set Callback URL"   }`                                                                                                                                | Error occurred while setting the callback URL, try after some time. |