---
title: Get Pre-filled Data
excerpt: >-
  Use this API to get pre-filled data for an app, which will be shown to the
  user during the ES flow.
api:
  file: partner-prefillied-data.json
  operationId: get_partner-app-appid-onboarding-embed-prefilled
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Values                | Description                      | Data types | Required/Optional | Constraints                                |
| :------------ | :-------------------- | :------------------------------- | :--------- | :---------------- | :----------------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application | String     | Required          | Should be a valid Partner App Access Token |
| appId         | `{{APP_ID}}`            | App ID to fetch the access token | String     | Required          | The Id should be a valid app Id of Gupshup |

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/onboarding/embed/prefilled' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
    "appId": "<app_id>",
    "businessName": "<business_name>",
    "businessPhoneCode": "<business_phone_code>",
    "businessPhoneNumber": "<business_phone_number>",
    "city": "<city>",
    "country": "<contry>",
    "email": "<business_email>",
    "phoneCategory": "<phone_category>",
    "phoneDescription": "<phone_description>",
    "phoneDisplayName": "<phone_displayname>",
    "state": "<state>",
    "status": "<status>",
    "streetAddress1": "<streetAddress1>",
    "streetAddress2": "<streetAddress2>",
    "timezone": "<timezone>",
    "website": "<business_website>",
    "zipPostal": "<business_postal_code>"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Comments |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |          |
| 200         | `{       "appId": "\<app_id>",       "businessName": "\<business_name>",       "businessPhoneCode": "\<business_phone_code>",       "businessPhoneNumber": "\<business_phone_number>",       "city": "<city>",       "country": "<contry>",       "email": "\<business_email>",       "phoneCategory": "\<phone_category>",       "phoneDescription": "\<phone_description>",       "phoneDisplayName": "\<phone_displayname>",       "state": "<state>",       "status": "<status>",       "streetAddress1": "<streetAddress1>",       "streetAddress2": "<streetAddress2>",       "timezone": "<timezone>",       "website": "\<business_website>",       "zipPostal": "\<business_postal_code>"   }` |          |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |          |
| 401         | `{       "message": "Authentication Failed",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |          |