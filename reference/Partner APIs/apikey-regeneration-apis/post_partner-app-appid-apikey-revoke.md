---
title: revoke secondary api key
excerpt: Use this API to revoke secondary Apikey.
api:
  file: Apikey regeneration APIs.json
  operationId: post_partner-app-appid-apikey-revoke
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

    <tr>
      <td style={{ textAlign: "left" }}>
        key
      </td>

      <td style={{ textAlign: "left" }}>
        Secondary apikey
      </td>

      <td style={{ textAlign: "left" }}>
        sk\_ac93c2a2215d4fa8875

        d612e3c6e79        cc
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/apikey/revoke' \
--header 'Authorization: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key={{SECONDARY_APIKEY}}'
```

## Sample Response

```
{
	"status": "success",
	"keys": 
	[
		{
			"token":
			"sk_ac93c2a2215d4**875d612e3c6e79cc",
			"createdOn": 1736757866285,
			"modifiedOn": 1736757866285
		},
		{
			"token":
			"sk_eaf501c4a85f41c991d****70e89c1e",
			"createdOn": 1736333445002,
			"modifiedOn": 1736333445002
		}
	]
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

        "status": "success","keys":\[
        \{
        "token":
        "sk\_ac93c2a2215d4\*\*875d612e3c6e79cc",
        "createdOn": 1736757866285,
        "modifiedOn": 1736757866285
        },
        \{
        "token":
        "sk\_eaf501c4a85f41c991d\*\*\*\*70e89c1e",
        "createdOn": 1736333445002,
        "modifiedOn": 1736333445002
        }
        ]
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

        "status": "error",\
        "message": Failed to get api keys for appId bf9ee64c-3d4d-4ac4-8668-\*\*\*\*7007c4""
        }
      </td>

      <td>

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

        "status": "error",\
        "message": "Too Many Requests"
        }
      </td>

      <td>
        Rate limit is 10 requests/minute
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>