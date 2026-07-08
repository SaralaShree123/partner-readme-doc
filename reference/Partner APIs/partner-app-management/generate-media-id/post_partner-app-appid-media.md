---
title: Generate Media ID Using File Uplaod
excerpt: >-
  Use this API to generate media IDs for WhatsApp messaging by uploading files
  directly from your local system. Media IDs are required when sending media
  messages (images, videos, documents, audio) through WhatsApp Business API.
api:
  file: generate-media-id.json
  operationId: post_partner-app-appid-media
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ⚠️ All media files sent through this endpoint are encrypted and persist for 30 days, unless they are deleted earlier.

## Request Parameters

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/media' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'file_type="{{FILE_TYPE}}"' \
--form 'file=@"/path/to/file"'
```

<br />

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/media' \
--header 'token: {{PARTNER_APP_TOKEN}}' \
--form 'file_type="{{FILE_TYPE}}"' \
--form 'file=@"/path/to/file"'
```

## Sample Response

```json
{
    "mediaId": "<mediaId>",
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                        | Comments                                                                              |
| :---------- | :---------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **Success** |                                                                                                 |                                                                                       |
| 200         | `{       "mediaId": "<mediaId>",       "status": "success"   }`                                 |                                                                                       |
| **Error**   |                                                                                                 |                                                                                       |
| 400         | `{       "message": "Only CAPI apps allowed to generate media ID",       "status": "error"   }` | Bad Request when app is non CAPI                                                      |
| 413         | `{       "message": "File size exceeds the maximum limit!",       "status": "error"   }`        | Supported 100 MB file size                                                            |
| 500         | `{       "message": "Unable to upload requested Media",       "status": "error"   }`            | Internal Error occurred. Try after some time. If issue persists contact support team. |
