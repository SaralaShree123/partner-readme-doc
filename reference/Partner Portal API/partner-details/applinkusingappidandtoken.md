---
api:
  file: partner_account_api_auth_app_link_api_spec.json
  operationId: appLinkUsingAppIdAndToken
hidden: true
---
# Description

Links a WhatsApp app to the authenticated partner account using the app’s ID and a one-time token (verified via the WhatsApp/SS API).

## Behaviour (high level)

1. Resolves the partner from the JWT/session.
2. Loads partner email and requires MFA to be enabled for that account; otherwise an error is returned.
3. Enforces joint solution rules via checkAllowBypassPartner(partnerId, "appLink") (approved solution or bypass flag).
4. Verifies the one-time token, resolves API keys and app details, and links the app (appLinkToPartnerUsingAppId → linkAppToPartner, source pp-api).

## Security and access

Roles: PARTNER_ADMIN or PARTNER_USER (@PreAuthorize).

## Rate limiting

**10 requests per 60 seconds** per client (exact HTTP behaviour depends on your rate-limit filter; often 429 when exceeded).

<br />

# API request (cURL)

```
curl -X POST 'https://partner.gupshup.io/partner/account/api/auth/appLink' \
  -H 'Authorization: {PARTNER_TOKEN}' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'appId={APP_ID}' \
  --data-urlencode 'token={ONE_TIME_TOKEN}'
```

<br />

# Parameters

| Parameter | Required | Description                                        |
| :-------- | :------- | :------------------------------------------------- |
| appId     | Yes      | WhatsApp / Gupshup app ID to link                  |
| token     | Yes      | One-time token for that app (verified server-side) |

<br />

# Response

HTTP 200 — Success

```
{
  "status": "success",
  "partnerApps": {
    "id": "<app-id>",
    "name": "<app-name>",
    "phone": "<phone>",
    "walletId": null,
    "customerId": "<customer-id>",
    "email": null,
    "live": false,
    "preferredTimezone": null,
    "partnerId": 12345,
    "solutionId": null,
    "createdOn": 1712659200000,
    "modifiedOn": 1712659200000,
    "storageRegion": null,
    "partnerCreated": false,
    "currency": null,
    "cxpEnabled": false,
    "partnerUsage": false,
    "customerOrgId": null,
    "source": "SS",
    "stopped": false,
    "healthy": false,
    "nameSpace": null,
    "cap": 0.0
  }
}
```

<br />

# Error response table

<br />

| HTTP status | When / cause                                                                  | Typical message or notes                                                                                                                                                                                                                                                                                |
| :---------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | InvalidParameterException handled in controller (validation / business rules) | Variable string in message.                                                                                                                                                                                                                                                                             |
| 400         | MFA not enabled for partner email                                             | Please enable MFA for your account, in the settings page, to proceed with creating app (Constants.ApiResponse.MFA_NOT_ENABLED). Thrown as ApplicationException; if the stack relies only on annotation-scoped global handlers, the HTTP status seen by clients may differ—validate in your environment. |
| 400         | No approved joint solution and partner is not allowed to bypass TPP           | Kindly request your partner to submit the Solution ID via the Partner Portal before proceeding with linking an app (ADD_YOUR_JOINT_SOLUTION_BEFORE_APP_LINK).                                                                                                                                           |
| 400         | One-time token verification failed (downstream API)                           | Message derived from SS/WhatsApp API error, e.g. failure text or messages built around Failed to verify token for appId : appId.                                                                                                                                                                        |
| 400         | No API keys / empty primary key / app details missing                         | e.g. No api keys found for appId: ..., Primary api key token is empty for appId: ..., App details not found for appId: ....                                                                                                                                                                             |
| 400         | Missing required query parameter                                              | Spring may return 400 via MissingServletRequestParameterException (handled by global servlet advice where configured).                                                                                                                                                                                  |
| 401         | Not authenticated                                                             | Per OpenAPI / Spring Security (invalid or missing JWT/session).                                                                                                                                                                                                                                         |
| 403         | Authenticated but not PARTNER_ADMIN / PARTNER_USER                            | Access denied.                                                                                                                                                                                                                                                                                          |
| 404         | Listed in OpenAPI                                                             | Routing/resource-not-found scenarios per gateway or app config.                                                                                                                                                                                                                                         |
| 429         | Rate limit exceeded                                                           | Depends on ApiRateLimit implementation (often returned when over 10 calls / 60s).                                                                                                                                                                                                                       |
| 500         | Uncaught Exception in controller                                              | Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support (Constants.ResponseValues.INTERNAL_ERROR_MSG).                                                                                                                                                |
