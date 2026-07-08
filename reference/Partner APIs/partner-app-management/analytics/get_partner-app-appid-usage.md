---
title: Get App's Daily Usage
excerpt: >-
  This API endpoint retrieves detailed usage statistics and billing information
  for a specific partner application within a specified date range. It provides
  comprehensive metrics including message counts by category (authentication,
  marketing, utility, service), fees breakdown (WhatsApp fees, Gupshup fees),
  billing information (cumulative bill, discount, cap), and conversation counts.
  This is essential for tracking application usage, billing analysis, and cost
  management.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-usage
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

| Parameters    | Value                 | Description                       |
| :------------ | :-------------------- | :-------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application  |
| appId         | `{{APP_ID}}`            | Unique Identifier for Gupshup App |
| from          | `{{FROM_DATE}}`         | date in YYYY-MM-DD format.        |
| to            | `{{TO_DATE}}`           | date in YYYY-MM-DD format.        |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io
/partner/app/{{APP_ID}}/usage?from={{FROM_DATE}}&to={{TO_DATE}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
 {
    "status": "success",
    "partnerAppUsageList": [
        {
            "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
            "appName": "Jan10pass",
            "authentication": 0,
            "cumulativeBill": 0.007,
            "currency": "USD",
            "date": "2024-01-10",
            "discount": 0.0,
            "fep": 0,
            "ftc": 1,
            "gsCap": 75.0,
            "gsFees": 0.007,
            "incomingMsg": 2,
            "outgoingMsg": 4,
            "outgoingMediaMsg": 0,
            "marketing": 0,
            "service": 0,
            "templateMsg": 0,
            "templateMediaMsg": 1,
            "totalFees": 0.007,
            "totalMsg": 7,
            "utility": 0,
            "waFees": 0.0,
            "internationalAuthentication": 1
        },
        {
            "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
            "appName": "Jan10pass",
            "authentication": 0,
            "cumulativeBill": 0.234,
            "currency": "USD",
            "date": "2024-01-18",
            "discount": 0.0,
            "fep": 0,
            "ftc": 1,
            "gsCap": 75.0,
            "gsFees": 0.091,
            "incomingMsg": 9,
            "outgoingMsg": 82,
            "outgoingMediaMsg": 0,
            "marketing": 1,
            "service": 0,
            "templateMsg": 0,
            "templateMediaMsg": 0,
            "totalFees": 0.101,
            "totalMsg": 91,
            "utility": 0,
            "waFees": 0.01,
            "internationalAuthentication": 1
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Comments               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                        |
| 200         | `{       "status": "success",       "partnerAppUsageList": [           {               "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",               "appName": "Jan10pass",               "authentication": 0,               "cumulativeBill": 0.007,               "currency": "USD",               "date": "2024-01-10",               "discount": 0.0,               "fep": 0,               "ftc": 1,               "gsCap": 75.0,               "gsFees": 0.007,               "incomingMsg": 2,               "outgoingMsg": 4,               "outgoingMediaMsg": 0,               "marketing": 0,               "service": 0,               "templateMsg": 0,               "templateMediaMsg": 1,               "totalFees": 0.007,               "totalMsg": 7,               "utility": 0,               "waFees": 0.0,               "internationalAuthentication": 1           },           {               "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",               "appName": "Jan10pass",               "authentication": 0,               "cumulativeBill": 0.234,               "currency": "USD",               "date": "2024-01-18",               "discount": 0.0,               "fep": 0,               "ftc": 1,               "gsCap": 75.0,               "gsFees": 0.091,               "incomingMsg": 9,               "outgoingMsg": 82,               "outgoingMediaMsg": 0,               "marketing": 1,               "service": 0,               "templateMsg": 0,               "templateMediaMsg": 0,               "totalFees": 0.101,               "totalMsg": 91,               "utility": 0,               "waFees": 0.01,               "internationalAuthentication": 1           }       ]   }` |                        |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | For any Internal Error |