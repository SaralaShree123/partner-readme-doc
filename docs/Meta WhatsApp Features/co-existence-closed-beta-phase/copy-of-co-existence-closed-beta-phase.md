---
title: Co-Existence - Closed Beta Phase - Enable for Onboarding APIs
excerpt: >-
  Co-existence allows you to connect your existing WhatsApp Business App number
  to Gupshup.
deprecated: false
hidden: true
metadata:
  robots: index
---
## The below API will help to enable API app level which is recommended when using Gupshup Onboarding APIs.

**Request**

```json
curl --location --request PUT 'https://partner.gupshup.io/partner/app/:appId/config' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
	"coexistenceEnabled" : true
}'
```

**Params**

| Key                | Description                                        | Constraints                                                               |
| :----------------- | :------------------------------------------------- | :------------------------------------------------------------------------ |
| Headers            |                                                    |                                                                           |
| PARTNER_APP_TOKEN  | Partner app access token issued post partner login | Should be a valid Partner app access token belonging to the passed app ID |
|                    |                                                    |                                                                           |
| Request Params     |                                                    |                                                                           |
| coexistenceEnabled | Co Existence flag                                  | Boolean. Value - true / false                                             |
| Path Params        |                                                    |                                                                           |
| appId              | App ID for the app                                 | Valid app ID                                                              |

**Response**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
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
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        "status": "success"
      </td>

      <td>
        Successfully updated config
      </td>
    </tr>

    <tr>
      <td>
        Error
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
        "status":"error",
        "messagedata":"Specific to API"
      </td>

      <td>
        Error with respect to API
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        "status":"error",
        "message":"Unauthorized Access"
      </td>

      <td>
        When authentication fails
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        Too Many Requests
      </td>

      <td>
        When rate limit is hit
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        "status": "error",
        "message": "Internal Server Error"
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

<br />