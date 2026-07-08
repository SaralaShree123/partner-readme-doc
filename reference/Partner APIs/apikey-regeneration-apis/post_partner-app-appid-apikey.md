---
title: Create secondary api key
excerpt: Use this API to create secondary Apikey.
api:
  file: Apikey regeneration APIs.json
  operationId: post_partner-app-appid-apikey
hidden: true
---
## Request Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        Partner Token
      </td>

      <td style={{ textAlign: "left" }}>
        `{{PARTNER_TOKEN}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App ID for which api key should be created
      </td>

      <td style={{ textAlign: "left" }}>
        `{{APP_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the partner account.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/apikey/' \
--header 'Authorization: {{PARTNER_TOKEN}}'
```

## Sample Response

```
{
	"status": "success",
	"key": 
	{
		"token":
		"sk_ac93c2a***a8875d612e3c6e79cc",
		"createdOn": 1736757866285,
		"modifiedOn": 1736757866285
	}
}
```

<br />

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
        "status": "success",
        "key":
        \{
        "token":
        "sk\_ac93c2a\*\*\*a8875d612e3c6e79cc",
        "createdOn": 1736757866285,
        "modifiedOn": 1736757866285
        }
        }
      </td>

      <td>
        Success response
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

        "status": "error","message": "Error: Maximum limit reached for secondary api keys.  Please delete to create a new one"}
      </td>

      <td>
        One app can have max 2app level apikeys. If limit exceeds, you will get this error.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        \{

        "status": "error","message": "Too Many Requests"}
      </td>

      <td>
        Rate limit is 2 requests/minute
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>