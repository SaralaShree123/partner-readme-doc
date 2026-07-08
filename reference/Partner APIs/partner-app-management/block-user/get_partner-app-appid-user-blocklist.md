---
title: Get Blocked Users list
excerpt: >-
  This API endpoint retrieves a paginated list of users who have been blocked
  from sending messages to your WhatsApp Business application. The endpoint
  supports cursor-based pagination for efficiently handling large lists of
  blocked users. This is useful for auditing blocked users, managing user
  access, and troubleshooting message delivery issues.
api:
  file: block_usersApi_openapi3.json
  operationId: get_partner-app-appid-user-blocklist
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
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        `{{PARTNER_APP_TOKEN}}`
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
        App ID to fetch the access token
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
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        limit
      </td>

      <td style={{ textAlign: "left" }}>
        Limits the number of blocked users returned in the response.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        \- its optional\
        \- default value is 100 if not specified
        -maximum value is 100
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        after
      </td>

      <td style={{ textAlign: "left" }}>
        Specifies the starting point for the next set of results. (Next page)
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        \- its optional\
        \- the value of this field is present in the response of the get request
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/user/blocklist?limit={{LIMIT}}&after={{AFTER}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
    "data": [
        {
            "messaging_product": "whatsapp",
            "wa_id": "919163805873"
        },
        {
            "messaging_product": "whatsapp",
            "wa_id": "918910864371"
        }
    ],
    "paging": {
        "cursors": {
            "after": "eyJvZAmZAzZAXQiOjEsInZAlcnNpb25JZACI6IjE3NDEyNTc3OTI1NjY1MDAifQZDZD",
            "before": "eyJvZAmZAzZAXQiOjAsInZAlcnNpb25JZACI6IjE3NDEyNTc3OTI1NjY1MDAifQZDZD"
        }
    },
    "status": "success"
}
```

<br />

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

        "data": \[

        \{"messaging\_product": "whatsapp",
        "wa\_id": "919163805873"
        },
        \{
        "messaging\_product": "whatsapp",
        "wa\_id": "918910864371"
        }
        ],
        "paging": \{
        "cursors": \{
        "after": "eyJvZAmZAzZAXQiOjEsInZAlcnNpb25JZACI6IjE3NDEyNTc3OTI1NjY1MDAifQZDZD",
        "before": "eyJvZAmZAzZAXQiOjAsInZAlcnNpb25JZACI6IjE3NDEyNTc3OTI1NjY1MDAifQZDZD"
        }
        },
        "status": "success"
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>