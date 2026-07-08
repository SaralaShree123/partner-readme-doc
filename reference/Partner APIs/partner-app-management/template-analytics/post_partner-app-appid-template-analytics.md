---
title: Enable template analytics setting
excerpt: >-
  This API endpoint enables or disables template analytics settings for a
  partner application. Template analytics must be enabled before you can
  retrieve analytics data using the GET template analytics API.
api:
  file: partner-release-85-apis.json
  operationId: post_partner-app-appid-template-analytics
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Description                                     | Value                   | Type    | Required/Optional | Constraints                                |
| :------------ | :---------------------------------------------- | :---------------------- | :------ | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application                | `{{PARTNER_APP_TOKEN}}` | String  | Required          | Should be a valid Partner App Access Token |
| APP_ID        | App ID to fetch the access token                | `{{APP_ID}}`            | String  | Required          | The ID should be a valid app ID of Gupshup |
| enable        | Flag to enable template analytics setting       | True/False              | Boolean | Required          |                                            |
| enableOnUi    | Flag to enable template analytics setting on UI | True/False              | Boolean | Optional          |                                            |

## Sample Request

```curl
curl --location --request POST '{{BASE_URL}}/partner/app/{{APP_ID}}/template/analytics' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'enable=true' \
--data-urlencode 'enableOnUi=true'
```

## Sample Response

```
{
    "status": "success"
}
```

## Status Codes

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
        `{ "status": "success" }`
      </td>

      <td>
        Successful response
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
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{ "status": "error", "message": "Bad Request" }`
      </td>

      <td>
        Bad request
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        `{ "status": "error", "message": "Too Many Requests" }`
      </td>

      <td>
        10 Requests per Minute
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `{ "status": "error", "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support" }`
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `{
          "status": "error",
          "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"
        }`

      </td>

      <td>
        Inavalid/Missing Token or appId.
      </td>
    </tr>
  </tbody>
</Table>

<br />