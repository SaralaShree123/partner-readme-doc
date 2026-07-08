---
title: Send template message
excerpt: Sends a template message to a specified destination
api:
  file: Send  auth message.json
  operationId: post_partner-app-appid-template-msg
hidden: true
---
## Request Parameters

| Key           | Description                                | Value                                                               | Data type | Required/Optional | Constraints                                   |
| :------------ | :----------------------------------------- | :------------------------------------------------------------------ | :-------- | :---------------- | :-------------------------------------------- |
| Authorization | Access Token for the application           | `{{PARTNER_APP_TOKEN}}`                                             | String    | Required          | Should be a valid Partner App Access Token    |
| appId         | App ID to fetch the access token           | `{{APP_ID}}`                                                        | String    | Required          | - The Id should be a valid app Id of Gupshup. |
| source        | source number (phone number of the app)    | 915667xx4576                                                        | String    | Required          | Phone number linked with the app              |
| src.name      | App name that the source number belongs to | APP\_NAME                                                           | String    | Required          | Valid name of the linked app. Required field  |
| destination   | destination phone number                   | 918667xx5586                                                        | String    | Required          | Phone number with country code                |
| sandbox       | Should be boolean value                    | false                                                               | Boolean   | Optional          |                                               |
| template      | Should have templateId and required params | \{"id": "8f86c262-2700-4013-a595- 250ae0724abb","params": \["123"]} | Object    | Required          |                                               |

<br />

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/template/msg' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'source=91892**74278' \
--data-urlencode 'sandbox=false' \
--data-urlencode 'destination=919422032**0' \
--data-urlencode 'template={"id": "<TEMPLATE_ID>","params": ["123"]}' \
--data-urlencode 'src.name=august18'
```

## Sample Response

```
{
	"status": "submitted",
	"messageId":"messageId"
}
```

## Status Codes

<Table align={["left","left","left","left"]}>
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

      <th>

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
        \{
        "status": "submitted",
        "messageId": "messageId"
        }
      </td>

      <td>
        When destination is missing.
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
        \{
        "message": "Invalid Destination",
        "status": "error"
        }
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
        "message": "Invalid App Details",
        "status": "error"
        }
      </td>

      <td>
        If the source is missing or app details are not found
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{
        "status": "error",
        "message": "Internal server error. Please try again later and if the Issue still persists then contact Gupshup Dev Support"
        }
      </td>

      <td>
        For any Internal Error
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>