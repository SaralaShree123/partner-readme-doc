---
title: Get User Status
excerpt: Use this API to retrieve the user status.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-userstatus
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Parameters    | Value                 | Description                        |
| :------------ | :-------------------- | :--------------------------------- |
| Authorization | `{PARTNER_APP_TOKEN}` | Access Token for the application   |
| appId         | `{APP_ID}`            | Unique Identifier for Gupshup App  |
| phone         | 91xxxxxxxxxx          | Phone number to check optin status |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{APP_ID}/userStatus?phone={PHONE_NUMBER}' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

### Sample Response

```json
  {
        "userStatus": {
            "active": false,
            "appId": "9e****0d-ad**-4***-**35-4cd*****fa**",
            "blocked": true,
            "countryCode": "91",
            "dialCode": "**********",
            "phone": "************",
            "status": "OPT_IN"
        }
    }
```

### Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                   | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                                                                                                                                                            |                        |
| 200         | `{       "userStatus": {           "active": false,           "appId": "b8d8565a-b320-4492-bfb1-2264bee17e04",           "blocked": false,           "countryCode": "91",           "dialCode": "9422032010",           "phone": "919422032010",           "status": "OPT_IN"       }   }` |                        |
| 200         | `{     "message": "Check User optin & User Preference. Please contact Gupshup team." }`                                                                                                                                                                                                    | When user is not opted |
| **Error**   |                                                                                                                                                                                                                                                                                            |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                          | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`                                                                                                                                  | For any Internal Error |