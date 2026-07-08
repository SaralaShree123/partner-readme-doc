---
title: Download Media
excerpt: >-
  Use this API to download or retrieve media files using their media ID. This
  endpoint allows you to access media files that were previously uploaded
  through the Generate Media ID API, enabling you to download images, videos,
  documents, and audio files.
api:
  file: DownloadMediaVer3.json
  operationId: downloadMedia
hidden: true
---
> ℹ️ Important Note:
>
> 1. Valid media ID required (obtained from media upload API)
> 2. Media must belong to the requesting app
> 3. Rate limit: **5 requests per hour** (3600 seconds)

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
        fileName
      </td>

      <td style={{ textAlign: "left" }}>
        Name of the file where the media is being dowloaded
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Valid file name
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        mediaId
      </td>

      <td style={{ textAlign: "left" }}>
        Media ID of the media which is being downloaded
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Valid media ID associated with the given app ID
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/media/:mediaId' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--output {{fileName}}
```

## Sample Response

```json
Downloaded media stream
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
        Downloaded media stream
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

        "status":"error","message/data":"Specific to API"}
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

        "status":"error","message":"Unauthorized Access"}
      </td>

      <td>
        When authentication fails
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
