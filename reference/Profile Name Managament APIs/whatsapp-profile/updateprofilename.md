---
title: Update WhatsApp Profile Display Name
excerpt: 'This API updates the display name for a WhatsApp application. '
api:
  file: Profile Name Managament APIs.json
  operationId: updateProfileName
hidden: true
---
<Callout icon="📘" theme="info">
  Rate limited to 3 requests per day
</Callout>

# Request Example

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/profile/displayName' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'newDisplayName=Updated Business Name'
```

# Request Example

```curl
{
    "status": "success"
}
```

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
        200
      </td>

      <td>
        `{ 
              "status": "success" 
          }`
      </td>

      <td>
        Successfully updated display name
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
              "status": "error",
              "error": "Display name cannot be empty"
          }`
      </td>

      <td>
        Display Name validations
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
               "status": "error",
               "error": "Display name must be at least 3 characters long"
          }`
      </td>

      <td>
        Display Name validations
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
               "status": "error",
               "error": "Display name must be less than 250 characters"
          }`
      </td>

      <td>
        Display Name validations
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
                "status": "error",
                "error": "Display name can only contain letters, numbers, spaces, hyphens, underscores, and parentheses"
          }`
      </td>

      <td>
        Display Name validations
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
                "status": "error",
                "error": "Display name cannot be all uppercase. It must contain at least one lowercase letter or number"
           }`
      </td>

      <td>
        Display Name validations
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `{ 
                "status": "error", 
                "code": "INTERNAL_SERVER_ERROR", 
                "message": "An unexpected error occurred" 
          }`
      </td>

      <td>
        For any internal error
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Request Parameters

| Key                 | Description                                       | Values                               | Data Type | Required/Optional | Constraints                                         |
| :------------------ | :------------------------------------------------ | :----------------------------------- | :-------- | :---------------- | :-------------------------------------------------- |
| **Path Parameters** |                                                   |                                      |           |                   |                                                     |
| appId               | The unique identifier of the WhatsApp application | 57d9179b-7412-4621-bf86-57ee1962fd12 | String    | Required          | Must be a valid app ID                              |
| **Form Parameters** |                                                   |                                      |           |                   |                                                     |
| newDisplayName      | The new display name for the WhatsApp application | Updated Business Name                | String    | Required          | Must comply with WhatsApp display name requirements |
| **Request Headers** |                                                   |                                      |           |                   |                                                     |
| Authorization       | Partner App token for authentication              | sk_226b25558a19407c9d34845****b6b88  | String    | Required          | Must be a valid JWT token with PARTNER_APP role     |

<br />