---
title: Set Conversational Component
excerpt: >-
  API to configure conversational components for WhatsApp Business API.
  Conversational components are pre-built interactive elements that enable rich,
  interactive customer experiences with features like quick replies, buttons,
  lists, and more structured message formats. This endpoint allows you to create
  and update component configurations for your application.
api:
  file: conversational-component-apis.json
  operationId: post_partner-app-appid-conversational-component
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

| Key                    | Description                                   | Value                                  | Data Type | Required/Optional | Constraints                                                                                                                                             |
| :--------------------- | :-------------------------------------------- | :------------------------------------- | :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Authorization          | Access Token for the application              | `{PARTNER_APP_TOKEN}`                  | String    | Required          | Should be a valid Partner App Access Token                                                                                                              |
| APP ID                 | appId of the account                          | `bf9ee64c-3d4d-4ac4-xxxx-732e577007c4` | String    | Required          | Should be a valid appId                                                                                                                                 |
| enable_welcome_message | set to true to receive request_welcome events | True/False                             | Boolean   | Required          | Should be true/false                                                                                                                                    |
| commands               | configure the various commands for your apps  | List of Objects                        | List      | Required          | You can define up to 30 commands. Each command has a maximum of 32 characters, and each hint has a maximum of 256 characters. Emojis are not supported. |
| prompts                | configure the ice breakers for your apps      | List of String                         | List      | Required          | You can set up 4 ice breakers, each with a maximum of 80 characters. Emojis are not supported.                                                          |

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{APP_ID}/conversational/component' \
--header 'Authorization: {PARTNER_APP_TOKEN}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "enable_welcome_message": true,
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
    "prompts": [
        "Book a flight",
        "plan a vacation"
    ]
}'
```

## Sample Response

```json
{
    "status": "success",
    "success": true
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                    | Comments                                |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                             |                                         |
| 200         | `{       "status": "success",       "success": true   }`                                                                                                                                                                                                                    |                                         |
| **Error**   |                                                                                                                                                                                                                                                                             |                                         |
| 401         | `{       "message": "Authentication Failed",       "status": "error"   }`                                                                                                                                                                                                   | When API authentication fails           |
| 400         | `{       "error": {           "code": 105,           "fbtrace_id": "AuzfcgaHAKSQQv2yL1T_Tyf",           "message": "(#105) The parameter prompts must have at most 4 elements, 5 found.",           "type": "OAuthException"       },       "status": "error"   }`          | more than 4 ice-breakers added          |
| 400         | `{       "error": {           "code": 100,           "fbtrace_id": "AP4UAoO-eaN9WVCOlGjuaM7",           "message": "(#100) Param commands[8]['command_name'] must be at most 32 characters long.",           "type": "OAuthException"       },       "status": "error"   }` | command name is more than 32 characters |