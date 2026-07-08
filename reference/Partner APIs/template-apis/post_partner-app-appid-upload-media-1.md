---
title: Upload Template Media
excerpt: Use this API to upload your sample media and generate a ***handleId*** for it.
api:
  file: partner-portal-public-apis-1.json
  operationId: post_partner-app-appid-upload-media
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Using the ***handleId***, you can create and submit a template along with a sample media. The handleId is passed in the ***exampleMedia*** parameter of the ***Apply for templates with sample media*** API.

### Parameters

| Key           | Description                                                               | Required/Optional | Type      | Value                     |
| :------------ | :------------------------------------------------------------------------ | :---------------- | :-------- | :------------------------ |
| Authorization | Access Token for the application                                          | Required          | String    | \{\{PARTNER\_APP\_TOKEN}} |
| appId         | Unique identifier of the app.                                             | Required          | String    | \{\{APP\_ID}}             |
| file          | Upload a file from your local machine or add the public URL to the media. | Required          | File path | \{\{FILE\_PATH}}          |
| file type     | Upload a file from your local machine.                                    | Required          | String    | \{\{FILE\_TYPE}}          |

### Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/upload/media' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'file_type="{{FILE_TYPE}}"' \
--form 'file=@"{{FILE_PATH}}'
```

OR

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/upload/media' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'file_type="{{FILE_TYPE}}"' \
--form 'file="{{MEDIA_URL}}'
```

### Sample Response

```json
   {
        "handleId": {
        "message": "4::aW1h*****G5n:ARYY-6d3******0RG7nG1d-Rie7-q4*****M_Fcffdkv7glkYgGa0IxKLc9DqlyuVIQD18KxYmgaEfuiUuQSdbYMpjce0jPgI5*****5e5Q:e:1634970144:2******925530161:100033****35566:A*****lB5Nu6A5KJaI"
        },
        "status": "success"
   }
```
