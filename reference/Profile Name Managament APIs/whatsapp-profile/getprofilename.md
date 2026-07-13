---
title: Get WhatsApp Profile Display Name
excerpt: 'This API retrieves the current display name for a WhatsApp application. '
api:
  file: Profile Name Managament APIs.json
  operationId: getProfileName
hidden: true
---
# Request Example

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/profile/displayName' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

# Response Example

```curl
{
  "displayNameInfo": {
    "verifiedNameStatus": "",
    "requestedName":"",
    "requestedNameStatus":"",
    "verifiedName":""
  },
  "status": "success"
}
```

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
        200
      </td>

      <td>
        `{
                          "displayNameInfo": {
                            "verifiedNameStatus": "",
                            "requestedName":"",
                            "requestedNameStatus":"",
                            "verifiedName":""
                          },
                          "status": "success"
                  }`
      </td>

      <td>
        `verifiedName` - current name if `verifiedNameStatus` is APPROVED

        `requestedName` - display name requested in update display name call

        `requestedNameStatus` - requested display name status
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{ 
                          "status": "error", 
                          "message": "Invalid request parameters" 
                  }`
      </td>

      <td>
        Missing or invalid parameters
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `{ 
                          "status": "error", 
                          "message": "Unauthorized" 
                 }`
      </td>

      <td>
        Invalid or missing authentication token
      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `{ 
                          "status": "error", 
                          "message": "Forbidden - no permissions to access resource" 
                  }`
      </td>

      <td>
        User does not have admin privileges
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

<br />

# Request Parameters

<br />

| Key                 | Description                               | Values                                | Data Type | Required/Optional | Constraints                                     |
| :------------------ | :---------------------------------------- | :------------------------------------ | :-------- | :---------------- | :---------------------------------------------- |
| **Path Parameters** |                                           |                                       |           |                   |                                                 |
| appId               | The unique identifier for the application | 57d9179b-7412-4621-bf86-57ee1962fd12  | String    | Required          | Must be a valid app ID                          |
| **Request Headers** |                                           |                                       |           |                   |                                                 |
| Authorization       | Partner App token for authentication      | sk_JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 | String    | Required          | Must be a valid JWT token with PARTNER_APP role |