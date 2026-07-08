---
title: Check Health
excerpt: >-
  Use this API to check the health status of your partner application. This
  endpoint provides a quick way to verify if your application is properly
  configured and operational within the Gupshup partner platform.
api:
  file: partner-portal-public-apis-1.json
  operationId: get_partner-app-appid-health
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  Rate limit: **10 requests per 60 seconds**
</Callout>

### Parameters

| Parameters    | Value                 | Description                       |
| :------------ | :-------------------- | :-------------------------------- |
| Authorization | `{PARTNER_APP_TOKEN}` | Access Token for the application  |
| appId         | `{APP_ID}`            | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{APP_ID}/health' \
--header 'Authorization: {PARTNER_APP_TOKEN}'
```

### Sample Response

```json
{
    "status": "success",
    "healthy": "true"
}
```

### Response Codes

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
      </th>

      <th>

      </th>

      <th>
        Response
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success**
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>

      </td>

      <td>
        `{       "status": "success",       "healthy": "true"   }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>

      </td>

      <td>
        `{       "message": "App is not live.",       "status": "error"   }`
      </td>

      <td>
        If APP is not live
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>

      </td>

      <td>
        `{       "message": "Waba id not found for the given App",       "status": "error"   }`
      </td>

      <td>
        If the WABA ID is not present in the DB
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>

      </td>

      <td>
        `{       "message": "WABA id is invalid or given phone is not associated with WABA",       "status": "error"   }`
      </td>

      <td>
        If the WABA ID present in DB is not correct
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>

      </td>

      <td>
        `{       "message": "Error while getting waba info for given app",       "status": "error"   }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>

      </td>

      <td>
        `{       "message": "Authentication Failed",       "status": "error"   }`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>

      </td>

      <td>
        `{
                  "status": "error",
                  "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"
                }`
      </td>

      <td>
        If Invalid appID/token
      </td>
    </tr>
  </tbody>
</Table>

<br />
