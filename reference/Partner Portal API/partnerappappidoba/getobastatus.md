---
title: Get OBA status for an app
excerpt: ' This is an app level API to get OBA status.'
api:
  file: GetOBAStatusVer1.json
  operationId: getObaStatus
hidden: true
---
# Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/oba' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

# Response

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
        `{
            "id": "421935614325838",
            "official_business_account": {
                "oba_status": "NOT_STARTED"
            },
            "status": "success"
        }`
      </td>

      <td>
        `NOT_STARTED`: No verification process has been initiated.

        <br />

        `PENDING`: Verification is under review.

        <br />

        `APPROVED`: Verification has been completed successfully.

        <br />

        `REJECTED`: Verification was not successful.

        <br />

        `IN_PROGRESS`: The verification process is ongoing.
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
        `{
          "status":"error",
          "message/data":"<Specific to API>"
        }`
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
        `{
          "status":"error",
          "message":"Unauthorized Access"
        }`
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
        `Too Many Requests`
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
        `{
          "status": "error",
          "message": "Internal Server Error"
        }`
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

# Parameters

<br />

| Key               | Description                                        | Constraints                                                               |
| :---------------- | :------------------------------------------------- | :------------------------------------------------------------------------ |
| **Headers**       |                                                    |                                                                           |
| PARTNER_APP_TOKEN | Partner app access token issued post partner login | Should be a valid Partner app access token belonging to the passed app ID |
| **Path Params**   |                                                    |                                                                           |
| appId             | App ID for the app                                 | Valid app ID                                                              |