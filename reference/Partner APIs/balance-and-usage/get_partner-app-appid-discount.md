---
title: Get App's Daily Discount
excerpt: >-
  This API endpoint retrieves daily discount and billing details for a specific
  partner application for a given month. It provides comprehensive financial
  information including Gupshup fees, caps, daily bills, cumulative bills, and
  discounts applied. This is essential for prepaid account billing analysis,
  financial tracking, discount verification, and cost management on a day-by-day
  basis within a specific month.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-discount
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Parameters    | Value                     | Description                       |
| :------------ | :------------------------ | :-------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application  |
| appId         | \{\{APP\_ID}}             | Unique Identifier for Gupshup App |
| year          | \{\{YEAR}}                | Year in YYYY format.              |
| month         | \{\{MONTH}}               | Month in MM format.               |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/discount?year={{YEAR}}&month={{MONTH}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
            "dailyAppDiscountList":[
            {
                "appId":"8*****j7-a**3-4**d-8***-c2******7bf**3",
                "cumulativeBill":0,
                "dailyBill":0,
                "day":2,
                "discount":0,
                "gsCap":75,
                "gsFees":0,
                "month":4,
                "partnerId":15,
                "year":2022
            },
            {
                "appId":"8*****j7-a**3-4**d-8***-c2******7bf**3",
                "cumulativeBill":0.014,
                "dailyBill":0.014,
                "day":4,
                "discount":0,
                "gsCap":75,
                "gsFees":0.014,
                "month":4,
                "partnerId":15,
                "year":2022
            }
            ]
        }
```