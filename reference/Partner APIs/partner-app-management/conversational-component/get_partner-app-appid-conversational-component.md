---
title: Get Conversational Component
excerpt: >-
  API to retrieve configured conversational components for WhatsApp Business
  API. Conversational components are in-chat features that you can enable on
  business phone numbers. They make it easier for WhatsApp users to interact
  with your business. You can configure easy-to-use commands, provide
  pre-written ice breakers that users can tap, and greet first time users with a
  welcome message.
api:
  file: conversational-component-apis.json
  operationId: get_partner-app-appid-conversational-component
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Description                      | Value                                  | Data Type | Required/Optional | Constraints                                |
| :------------ | :------------------------------- | :------------------------------------- | :-------- | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application | `{PARTNER_APP_TOKEN}`                  | String    | Required          | Should be a valid Partner App Access Token |
| APP ID        | appId of the account             | `bf9ee64c-3d4d-4ac4-xxxx-732e577007c4` | String    | Required          | The Id should be a valid app Id of Gupshup |

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{APP_ID}/conversational/component' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

## Sample Response

```json
{
    "conversational_automation": {
        "prompts": [
            "Book a flight",
            "plan a vacation"
        ],
        "commands": [
            {
                "command_name": "tickets",
                "command_description": "Book flight tickets"
            },
            {
                "command_name": "hotel",
                "command_description": "Book hotel"
            }
        ],
        "enable_welcome_message": false,
        "id": "{id}"
    },
    "id": "{phone_id}"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Comments                       |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                |
| 200         | `{       "conversational_automation": {           "prompts": [               "Book a flight",               "plan a vacation"           ],           "commands": [               {                   "command_name": "tickets",                   "command_description": "Book flight tickets"               },               {                   "command_name": "hotel",                   "command_description": "Book hotel"               }           ],           "enable_welcome_message": false,           "id": "{id}"       },       "id": "{phone_id}"   }` |                                |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                |
| 401         | `{       "message": "Authentication Failed",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | When API authentication fails  |