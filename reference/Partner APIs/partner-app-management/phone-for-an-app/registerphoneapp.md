---
title: Register phone for an app
excerpt: >-
  This API endpoint enables partners to register their Phone Number (PN) for
  WhatsApp Business onboarding. This is a critical operation that initiates the
  registration process with WhatsApp services, linking a phone number to the
  partner application.
api:
  file: RegisterPhoneApiVer1.json
  operationId: registerPhoneApp
hidden: false
---
## Request Parameters

| Key           | Description                                        | Value                     | Data type | Required/Optional | Constraints                                                                |
| :------------ | :------------------------------------------------- | :------------------------ | :-------- | :---------------- | :------------------------------------------------------------------------- |
| Authorization | Partner app access token issued post partner login | \{\{PARTNER\_APP\_TOKEN}} | String    | Required          | Should be a valid Partner app access token belonging to the passed app ID. |
| appId         | App ID to fetch the access token                   | \{\{APP\_ID}}             | String    | Required          | Valid app ID                                                               |
| region        | Data Localization Region for the app               |                           |           | Optional          | Default is IN.                                                             |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/onboarding/register' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'region=IN'
```

## Sample Response

```json
{
	"status": "success",
	"success": true
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
        \{
        "status": "success",
        "success": true
        }
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
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status":"error",
        "message/data":"\<Specific to API>"
        }
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
        \{
        "status":"error",
        "message":"Unauthorized Access"
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