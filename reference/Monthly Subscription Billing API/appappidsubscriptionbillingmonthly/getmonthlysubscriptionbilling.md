---
api:
  file: monthly-subscription-billing-api.yaml
  operationId: getMonthlySubscriptionBilling
hidden: true
---
# API Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/subscription/billing/monthly?year=2025&month=1' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Request Parameters

### Headers

| Key           | Description                      | Value                 | Data Type | Required/Optional | Constraints                                        |
| ------------- | -------------------------------- | --------------------- | --------- | ----------------- | -------------------------------------------------- |
| Authorization | Access Token for the application | {{PARTNER_APP_TOKEN}} | String    | Required          | Should be a valid Partner App Access Token (sk\_…) |

### Path Parameters

| Key     | Description                                  | Value                                | Data Type | Required/Optional | Constraints                                                |
| ------- | -------------------------------------------- | ------------------------------------ | --------- | ----------------- | ---------------------------------------------------------- |
| APP\_ID | App ID to fetch monthly subscription billing | 57d9179b-7412-4621-bf86-57ee1962fd12 | String    | Required          | Must be a valid app ID linked to the authenticated partner |

### Query Parameters

| Key   | Description                       | Value | Data Type | Required/Optional | Constraints                                                               |
| ----- | --------------------------------- | ----- | --------- | ----------------- | ------------------------------------------------------------------------- |
| year  | Calendar year for billing lookup  | 2025  | Integer   | Required          | Must be a valid year; cannot be a future month when combined with month   |
| month | Calendar month for billing lookup | 1     | Integer   | Required          | Must be between 1 and 12; current month and future months are not allowed |

## Response Codes

### Success

| Status Code | Response                                                                                                                                                                                             | Comments                                                                                             |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 200         | `json { "status": "PROCESSED", "appId": "57d9179b-7412-4621-bf86-57ee1962fd12", "partnerId": "568", "year": "2025", "month": "1", "monthlyGsFee": "4.50", "currency": "USD", "liveDaysCount": "3" }` | Monthly billing record found. status reflects billing deduction state: PENDING, PROCESSED, or ERROR. |

### Error

| Status Code | Response                                                                                                                                             | Comments                                                                                         |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 400         | `json { "status": "error", "message": "year and month are required" }`                                                                               | year or month is null.                                                                           |
| 400         | `json { "status": "error", "message": "month must be between 1 and 12" }`                                                                            | Invalid month value.                                                                             |
| 400         | `json { "status": "error", "message": "current month data not available , will be available after 8th of next month." }`                             | Requested period is the current calendar month.                                                  |
| 400         | `json { "status": "error", "message": "Cannot request billing for a future month" }`                                                                 | Requested period is in the future.                                                               |
| 400         | `json { "status": "error", "message": "Application is not linked to the partner" }`                                                                  | App is not linked to the authenticated partner.                                                  |
| 400         | `json { "status": "error", "message": "Required request parameter 'year' for method parameter type Integer is not present" }`                        | year query parameter is missing.                                                                 |
| 400         | `json { "status": "error", "message": "Required request parameter 'month' for method parameter type Integer is not present" }`                       | month query parameter is missing.                                                                |
| 400         | `json { "status": "error", "message": "Please review the request parameters and retry" }`                                                            | year or month is not a valid integer.                                                            |
| 401         | `json { "status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry" }`               | Missing, invalid, or expired Partner App token.                                                  |
| 403         | `json { "status": "error", "message": "Forbidden Access" }`                                                                                          | Authenticated but not authorized for this resource.                                              |
| 403         | `json { "status": "error", "message": "Authentication Failed" }`                                                                                     | IP not whitelisted or X-Forwarded-For header missing (when IP whitelist is enabled for the app). |
| 404         | `json { "status": "error", "message": "No monthly subscription billing record found for this app and period." }`                                     | No billing record exists for the given app, partner, year, and month.                            |
| 429         | `json { "status": "error", "message": "Too Many Requests" }`                                                                                         | Rate limit exceeded (20 requests per 60 seconds).                                                |
| 500         | `json { "status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support" }` | Unhandled server error.                                                                          |

##

<br />