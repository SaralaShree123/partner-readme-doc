---
title: Sync Templates for an App
excerpt: This is an app level API used to sync the templates on Gupshup platform
api:
  file: TemplateSyncApiVer.json
  operationId: syncTemplate
hidden: true
---
# Rate Limit

1 request per hour

<br />

# Request Parameters

| Key                 | Description                                        | Constraints                                                               |
| :------------------ | :------------------------------------------------- | :------------------------------------------------------------------------ |
| PARTNER\_APP\_TOKEN | Partner app access token issued post partner login | Should be a valid Partner app access token belonging to the passed app ID |
|                     |                                                    |                                                                           |

<br />

# Path Parameters

| Key   | Description        | Constraints  |
| :---- | :----------------- | :----------- |
| appId | App ID for the app | Valid app ID |

<br />

# Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/template/sync' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

# Sample Response

```
202 Accepted
```

<br />

<br />

# Status Codes

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
        Success
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        202
      </td>

      <td>

      </td>

      <td>
        Successfully accepted sync request
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
        \{
        "status": "error",
        "message/data": "Specific to API"
        }
      </td>

      <td>
        Error with respect to the API
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{
        "status": "error",
        "message": "Unauthorized Access"
        }
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
        \{
        "status": "error",
        "message": "Too Many Requests"
        }
      </td>

      <td>
        When the rate limit is hit
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{
        "status": "error",
        "message": "Internal Server Error"
        }
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>