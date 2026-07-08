---
api:
  file: deleteMediaId.json
  operationId: delete_partner-app-appid-media-mediaid
hidden: false
---
<Callout icon="📘" theme="info">
  Rate limit: 10 requests per hour
</Callout>

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
        \{\{PARTNER_APP_TOKEN}}
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
        \{\{APP_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER_APP_TOKEN being used
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        mediaId
      </td>

      <td style={{ textAlign: "left" }}>
        Media ID of the media which is being deleted
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{MEDIA_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Valid media ID associated with the given app ID
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/media/{{MEDIA_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Responses

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
                    "message": "Media deleted successfully",
                    "status": "success"
                }`
      </td>

      <td>
        Media successfully deleted from WhatsApp servers
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
                    "message": "Failed to delete media",
                    "status": "error"
                }`
      </td>

      <td>
        Bad Request - Invalid media ID or deletion failed
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
                    "message": "Delete media operations are temporarily blocked for this app due to previous errors. Please try again later.",
                    "status": "error"
                }`
      </td>

      <td>
        Temporary block due to previous errors
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{

        "status": "error","message": "Internal Server Error"}
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>