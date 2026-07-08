---
title: Update app solution provider
excerpt: >-
  Updates the solution provider for a partner application. This operation
  removes the existing solution and either associates a new approved solution or
  updates the provider without a solution.
api:
  file: Partner App Update Solution Provider API_openApi.json
  operationId: updateAppSolutionProvider
hidden: true
---
# Overview

This API allows partners to update the solution provider for their linked applications. The API handles three scenarios: approved solution found, no solution found, and unapproved solution found.

<br />

# Rate Limit

3 requests per 60 seconds

<br />

# Request Parameters

**Path Parameters**

| Parameter | Type   | Required | Description                              |
| :-------- | :----- | :------- | :--------------------------------------- |
| appId     | String | Yes      | The unique identifier of the application |

<br />

**Query Parameters**

| Parameter | Type   | Required | Description                 | Example                     |
| :-------- | :----- | :------- | :-------------------------- | :-------------------------- |
| provider  | String | Yes      | The provider name to update | PELOCAL, GUPSHUP, ONEDIRECT |

<br />

# Request Example

```
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/update/solution/provider' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'provider={{PROVIDER}}'

```

<br />

# HTTP Status Codes

<br />

| Status Code | Status Message        | Scenario                         | Response                                                                                                                                                   |
| :---------- | :-------------------- | :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | OK                    | Approved solution found          | `{"status": "success", "message": "Solution associated successfully and provider updated to 'PELOCAL'."}`                                                  |
| 200         | OK                    | No solution found                | `{"status": "success", "message": "Existing app solution removed as the requested provider 'PELOCAL' was not found. Provider updated to 'PELOCAL'."}`      |
| 200         | OK                    | Unapproved solution found        | `{"status": "success", "message": "Existing app solution removed as the solution for provider 'PELOCAL' is not approved. Provider updated to 'PELOCAL'."}` |
| 400         | Bad Request           | Invalid provider value           | `{"status": "error", "message": "Invalid provider: INVALID_PROVIDER. Valid providers are: PELOCAL, GUPSHUP, ONEDIRECT"}`                                   |
| 401         | Unauthorized          | Missing or invalid               | `{"status": "error", "message": "Unauthorized access. Please provide a valid access token."}`                                                              |
| 403         | Forbidden             | Insufficient permissions         | `{"status": "error", "message": "Forbidden - no permissions to access resource"}`                                                                          |
| 404         | Not Found             | App not linked to partner        | `{"status": "error", "message": "Application not linked to partner"}`                                                                                      |
| 404         | Not Found             | API key not found                | `{"status": "error", "message": "API key not associated with partner"}`                                                                                    |
| 429         | Too Many Requests     | Rate limit exceeded (>3 req/60s) | `{"status": "error", "message": "Rate limit exceeded. Maximum 3 requests per 60 seconds."}`                                                                |
| 500         | Internal Server Error | Server error                     | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"}`              |

<br />

<br />
