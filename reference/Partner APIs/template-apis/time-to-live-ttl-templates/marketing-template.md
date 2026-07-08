---
title: Marketing template
excerpt: Use this API to create a template for a particular app.
deprecated: false
hidden: true
metadata:
  robots: index
---
Here you can create a template for a particular app. you will need below details to start using this api.

1. app Id
2. app token

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'vertical=TEXT' \
--data-urlencode 'content=your ticket has been confirmed for {{1}} persons on date {{2}}.' \
--data-urlencode 'header=This is the header' \
--data-urlencode 'exampleHeader=This is the header' \
--data-urlencode 'footer=This is the footer' \
--data-urlencode 'buttons=[{"type":"PHONE_NUMBER","text":"Call Us","phone_number":"+919872329959"},{"type":"URL","text":"Book A Demo","url":"https://bookins.gupshup.io/{{1}}","example":["https://bookins.gupshup.io/abc"]}] or for “Authentication” category: [{"type":"OTP","otp_type":"COPY_CODE","text":"Copy OTP"},{"type":"OTP", “otp-type”: “ONE_TAP”, "text":"Book A Demo", "autofill_text": "Autofill", #One-tap buttons only "package_name": "com.example.myapplication" #One-tap buttons only , "signature_hash": "K8a%2FAINcGX7", #One-tap buttons only }]' \
--data-urlencode 'example=your ticket has been confirmed for 4 persons on date 2020-05-04.' \
--data-urlencode 'enableSample=true' \
--data-urlencode 'message_send_ttl_seconds=43200' \
--data-urlencode 'allowTemplateCategoryChange=false' \'
```

## Sample Response

```
{
    "status": "success",
    "template": {
        "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"bf9ee64c-3d4d-4ac4-8668-732e577007c4\",\"data\":\"This is category for copy code button template.\",\"footer\":\"This is footer\",\"sampleText\":\"This is category for copy code button template.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
        "createdOn": 1708205191624,
        "data": "This is category for copy code button template.\nThis is footer",
        "elementName": "automation_template_2956534",
        "id": "e8e837c2-a3a8-4845-958f-ec7febb54aec",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"This is category for copy code button template.\"}",
        "modifiedOn": 1708205191624,
        "namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "TEXT",
        "vertical": "Internal_vertical",
        "wabaId": "216141188246170"
    }
}
```