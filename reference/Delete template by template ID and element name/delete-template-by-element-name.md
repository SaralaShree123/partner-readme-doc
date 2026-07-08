---
title: Delete template by element name
excerpt: API to delete template by element name
deprecated: false
hidden: false
metadata:
  robots: index
---
```curl
curl --location --request DELETE '{{api_front_url}}/wa/app/:appId/template/:elementName' \
--header 'apikey: <apikey>'
```

Status codes:

<br />

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Status Code
      </th>

      <th style={{ textAlign: "left" }}>
        Status
      </th>

      <th style={{ textAlign: "left" }}>
        Response
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        200
      </td>

      <td style={{ textAlign: "left" }}>
        Success
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status": "success"
                }`
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Invalid App ID"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        appId provided is not valid
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Delete Operation is not allowed for sandbox apps"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        App is not live
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Please Check If App Has been approved"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        App is not approved
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Template Does not exists."
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        No template found for the provided element name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Template Cannot be deleted"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        Not a master template
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Unable to delete the template, please try after sometime and if issue still exists than contact dev support"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        Error occured while deleting template.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        403
      </td>

      <td style={{ textAlign: "left" }}>
        Error
      </td>

      <td style={{ textAlign: "left" }}>
        `{
                    "status":"error",
                    "message":"Not App Owner"
                }`
      </td>

      <td style={{ textAlign: "left" }}>
        appId provided is not associated with the provided api key.
      </td>
    </tr>
  </tbody>
</Table>

Request Params

| Parameter | Description                                          | Constraints                         |
| :-------- | :--------------------------------------------------- | :---------------------------------- |
| apikey    | Apikey of the account where the app is to be created | Should be a valid gupshup.io apikey |

Path Params

| Parameter   | Description                                 | Constraints |
| :---------- | :------------------------------------------ | :---------- |
| appId       | App id of the app                           |             |
| elemetnName | element name for the template to be deleted |             |

Response Params

| Parameter | Description                             | Constraints |
| :-------- | :-------------------------------------- | :---------- |
| status    | API call status(“success/error”)        |             |
| message   | error message describing failure of API |             |
