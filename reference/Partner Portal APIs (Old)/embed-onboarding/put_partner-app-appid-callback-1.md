---
title: Set callback for an appID
excerpt: Use this endpoint to configure a customer callback URL for the application.
api:
  file: onboarding-api.json
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
## Parameters

| Key              | Description                                                                                                         | Constraints                                                                   |
| :--------------- | :------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------- |
| PARTNER_TOKEN    | JWT Token issues post Partner login                                                                                 | Should be a valid Partner JWT Token.                                          |
| url              | url to set for custom callback                                                                                      | Should be a valid URL                                                         |
| modes            | modes for which callback should be used. Taken as comma separated values                                            | Should be any of `[NONE,READ,DELIVERED,SENT,DELETED,OTHERS,TEMPLATE,ACCOUNT]` |
| directForwarding | The boolean value is true if the events are sent directly and false if the events need to be sent via the platform. | Should only contain true or false value.                                      |
| notifyWithPhone  | The boolean value which is true if the events should contain the source phone number. false otherwise.              | Should only contain true or false value.                                      |

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
        "url" : "<callback_url>",
        "custom" : <true/false>,
        "modes" : [
            "<callback_modes_list>"
        ]
    }
}
```

## Status Codes

| Status Code   | Response                                                                                                                                                                                                        | Comment                                                             |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| _**Success**_ |                                                                                                                                                                                                                 |                                                                     |
| 200           | `{       "status": "success",       "callback": {           "url" : "<callback_url>",           "custom" : <true/false>,           "modes" : [               "<callback_modes_list>"           ]       }   }` | Custom URL set successfully.                                        |
| _**Error**_   |                                                                                                                                                                                                                 |                                                                     |
| 400           | `{       "status": "error",       "message": "Invalid App Details Passed"   }`                                                                                                                                  | Incorrect App Id Provided.                                          |
| 429           | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                               | When the request rate limit exceeds.                                |
| 500           | `{       "status": "error",       "message": "Unable to Set Callback URL"   }`                                                                                                                                  | Error occurred while setting the callback URL, try after some time. |