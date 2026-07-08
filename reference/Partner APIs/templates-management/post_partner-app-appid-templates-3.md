---
title: Zero-tap authentication templates with message validity
excerpt: >-
  Use this API to create a zero-tap authentication template with message
  validity.
api:
  file: message-validity-period-for-authentication-templates.json
  operationId: post_partner-app-appid-templates
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note:
> 
> - Zero-tap is only supported on Android.
> - If you send a zero-tap authentication template to a WhatsApp user who is using a non-Android device, the WhatsApp client will display a copy code button instead.
> - Message Validity is valid only for authentication and utility templates.
> - Message Validity for authentication templates ranges from 1 to 10 minutes and for utility templates it ranges from 1 to 60 minutes.

## Request Parameters

| Key             | Description                                          | Constraints                                                                                                                                                                                        |
| :-------------- | :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apikey          | Apikey of the account where the app is to be created | Should be a valid `gupshup.io` apikey                                                                                                                                                              |
| languageCode    | Valid Language code for the template                 |                                                                                                                                                                                                    |
| content         | Template body                                        |                                                                                                                                                                                                    |
| footer          | Template Footer                                      | Optional                                                                                                                                                                                           |
| category        | Template Category                                    | Must always be `AUTHENTICATION` for zero-tap templates                                                                                                                                             |
| templateType    | Template Type                                        | Must be text                                                                                                                                                                                       |
| example         | Template Body example                                |                                                                                                                                                                                                    |
| vertical        | Template Vertical                                    |                                                                                                                                                                                                    |
| elementName     | Template Name                                        |                                                                                                                                                                                                    |
| buttons         | Zero Tap Auth template buttons                       |                                                                                                                                                                                                    |
| messageValidity | validity of the template during messaging            | - value will be in seconds - supported only for utility and authentication templates - for utility templates, it can be between 60 - 3600 - for authentication templates value is between 60 - 600 |

## Sample Request

```curl
curl --location '{{apifront_base_url}}/wa/app/:appId/template' \
--header 'apikey: {{api_key}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'languageCode={{language_code}}' \
--data-urlencode 'content={{template body}}' \
--data-urlencode 'footer={{template footer}}' \
--data-urlencode 'category=AUTHENTICATION' \
--data-urlencode 'example={{template body example}}' \
--data-urlencode 'vertical={{template vertical}}' \
--data-urlencode 'templateType=TEXT' \
--data-urlencode 'elementName={{template name}}' \
--data-urlencode 'buttons=[{"type":"OTP","otp_type":"ZERO_TAP","text":"zero_tap_test","zero_tap_terms_accepted":true,"supported_apps":[{"package_name":"com.whatsapp.otp.sample","signature_hash":"K8a/AINcGX7"}]}]' \
--data-urlencode 'footer={{footer}}' \
--data-urlencode 'addSecurityRecommendation=true' \
--data-urlencode 'codeExpirationMinutes=12' \
--data-urlencode 'messageValidity={{message_validity}}'
```

## Meta Payload Example

```
{
  "name": "<TEMPLATE_NAME>",
  "language": "<TEMPLATE_LANGUAGE>",
  "category": "authentication",
  "message_send_ttl_seconds": <TIME_TO_LIVE>, // Optional
  "components": [
    {
      "type": "body",
      "add_security_recommendation": <SECURITY_RECOMMENDATION> // Optional
    },
    {
      "type": "footer",
      "code_expiration_minutes": <CODE_EXPIRATION> // Optional
    },
    {
      "type": "buttons",
      "buttons": [
        {
          "type": "otp",
          "otp_type": "zero_tap",
          "text": "<CODY_CODE_BUTTON_TEXT>", // Optional
          "autofill_text": "<AUTOFILL_BUTTON_TEXT>", // Optional
          "zero_tap_terms_accepted": <TERMS_ACCEPTED>,
          "supported_apps": [
            { 
              "package_name": "<PACKAGE_NAME>",
              "signature_hash": "<SIGNATURE_HASH>"
            }
          ]
        }
      ]
    }
  ]
}
```

## Sample Response

```json
{
    "status": "success",
    "template": {
            "appId": "ceb2b861-24f6-406c-901f-3f788e02f5ea",
            "buttonSupported": "URL",
            "category": "AUTHENTICATION",
            "containerMeta": "{\"appId\":\"ceb2b861-24f6-406c-901f-3f788e02f5ea\",\"data\":\"*{{1}}* is your verification code. For your security, do not share this code.\",\"buttons\":[{\"type\":\"URL\",\"text\":\"sample copy code\",\"url\":\"https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp{{1}}\",\"example\":[\"https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp123456\"]}],\"footer\":\"This code expires in 10 minutes.\",\"sampleText\":\"*123456* is your verification code. For your security, do not share this code.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":true,\"codeExpirationMinutes\":10,\"messageSendTTLSeconds\":65}",
            "createdOn": 1720611283112,
            "data": "*{{1}}* is your verification code. For your security, do not share this code.\nThis code expires in 10 minutes. | [sample copy code,https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp{{1}}]",
            "elementName": "zero_tap_auth_123",
            "externalId": "863682358935224",
            "id": "a7b69e78-9e0c-494e-86f8-d91bffe173bd",
            "internalCategory": 0,
            "internalType": 0,
            "languageCode": "en",
            "languagePolicy": "deterministic",
            "meta": "{\"example\":\"[123456] is your verification code. For your security, do not share this code.\",\"newAuthTemplate\":true}",
            "modifiedOn": 1720614670877,
            "namespace": "6a54628a_7f29_45a7_80b1_46549f39062d",
            "priority": 3,
            "quality": "UNKNOWN",
            "retry": 0,
            "stage": "NONE",
            "status": "APPROVED",
            "templateType": "TEXT",
            "vertical": "zero_tap_auth_152",
            "wabaId": "103775135696983"
        }
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Comments                      |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |
| 200         | `{       "status": "success",       "template": {               "appId": "ceb2b861-24f6-406c-901f-3f788e02f5ea",               "buttonSupported": "URL",               "category": "AUTHENTICATION",               "containerMeta": "{\"appId\":\"ceb2b861-24f6-406c-901f-3f788e02f5ea\",\"data\":\"_{{1}}_ is your verification code. For your security, do not share this code.\",\"buttons\":\[{\"type\":\"URL\",\"text\":\"sample copy code\",\"url\":\"<https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp{{1}}\",\"example\":[\"https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp123456\"]}],\"footer\":\"This> code expires in 10 minutes.\",\"sampleText\":\"_123456_ is your verification code. For your security, do not share this code.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":true,\"codeExpirationMinutes\":10,\"messageSendTTLSeconds\":65}",               "createdOn": 1720611283112,               "data": "_{{1}}_ is your verification code. For your security, do not share this code.\\nThis code expires in 10 minutes. \| [sample copy code,https://www.whatsapp.com/otp/code/?otp_type=ZERO_TAP&cta_display_name=Autofill&package_name=com.whatsapp.otp.sample&signature_hash=K8a%2FAINcGX7&code_expiration_minutes=10&code=otp{{1}}]",               "elementName": "zero_tap_auth_123",               "externalId": "863682358935224",               "id": "a7b69e78-9e0c-494e-86f8-d91bffe173bd",               "internalCategory": 0,               "internalType": 0,               "languageCode": "en",               "languagePolicy": "deterministic",               "meta": "{\"example\":\"[123456] is your verification code. For your security, do not share this code.\",\"newAuthTemplate\":true}",               "modifiedOn": 1720614670877,               "namespace": "6a54628a_7f29_45a7_80b1_46549f39062d",               "priority": 3,               "quality": "UNKNOWN",               "retry": 0,               "stage": "NONE",               "status": "APPROVED",               "templateType": "TEXT",               "vertical": "zero_tap_auth_152",               "wabaId": "103775135696983"           }   }` |                               |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |
| 401         | `{       "message": "Authentication Failed",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | When API authentication fails |