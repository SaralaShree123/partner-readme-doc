---
title: Generate Media ID Using URL
excerpt: >-
  Use this API to generate media IDs for WhatsApp messaging by uploading files
  directly from your local system. Media IDs are required when sending media
  messages (images, videos, documents, audio) through WhatsApp Business API.
api:
  file: generate-media-id-1.json
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
## Request Parameters

```curl
curl --location 'https://partner.gupshup.io/partner/app/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/media' \
--header 'Authorization: sk_f39ed14bd5ea45bebe2603c6bf407d66' \
--form 'file_type="{{FILE_TYPE}}"' \
--form 'file="{{MEDIA_URL}}"'
```

<br />

## Sample Request

```curl
curl --request POST \
     --url https://partner.gupshup.io/partner/app/{APP_ID}/media \
     --header 'accept: application/json' \
     --header 'content-type: multipart/form-data' \
     --header 'token: {PARTNER_APP_TOKEN}' \
     --form file=https://image.jpeg \
     --form file_type=image/jpeg
```

## Sample Response

```json
{
  "mediaId": "1852559851913765",
  "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                        | Comments                                                                                     |
| :---------- | :---------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                 |                                                                                              |
| 200         | `{     "mediaId": "1852559851913765",     "status": "success"   }`                              |                                                                                              |
| **Error**   |                                                                                                 |                                                                                              |
| 400         | `{       "message": "Only CAPI apps allowed to generate media ID",       "status": "error"   }` | Bad Request when app is non CAPI                                                             |
| 413         | `{       "message": "File size exceeds the maximum limit!",       "status": "error"   }`        | Supported 100 MB file size                                                                   |
| 500         | `{       "message": "Unable to upload requested Media",       "status": "error"   }`            | Internal Error occurred. Try after some time. If the issue persists contact the support team |
