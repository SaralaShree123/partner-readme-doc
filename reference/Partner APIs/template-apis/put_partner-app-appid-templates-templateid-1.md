---
title: Edit Template
excerpt: Use this API to edit a template using *templateId*.
api:
  file: partner-portal-public-apis-1.json
  operationId: put_partner-app-appid-templates-templateid
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  **Note:**Updating carousel templates with Media is not permitted
</Callout>

You will need the below details to start using this API.

1. App Id
2. Template Id

### Parameters

| Key           | Description                                                                                                | Required/Optional | Type    | Value                                                                                                                                                                                                                                                                                         |
| :------------ | :--------------------------------------------------------------------------------------------------------- | :---------------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application                                                                           | Required          | String  | \{\{PARTNER_APP_TOKEN}}                                                                                                                                                                                                                                                                       |
| appId         | Unique identifier of the Gupshup app                                                                       | Required          | String  | \{\{APP_ID}}                                                                                                                                                                                                                                                                                  |
| templateId    | Unique identifier for a template, refer Get templates api                                                  | Required          | String  | fc05da-f2135-45e2-8sad4-dc44xxxx                                                                                                                                                                                                                                                              |
| content       | TEXT: The body of the template. Character limit: 1028                                                      | Optional          | String  | your ticket has been confirmed for \{\{1}} persons on date \{\{2}}.                                                                                                                                                                                                                           |
| templateType  | The type of template: TEXT, IMAGE, VIDEO & DOCUMENT                                                        | Optional          | String  | TEXT                                                                                                                                                                                                                                                                                          |
| example       | TEXT - An example of the template.                                                                         | Optional          | String  | your ticket has been confirmed for 4 persons on date 2020-05-04                                                                                                                                                                                                                               |
| enableSample  | BOOLEAN: True or False. Required for creating all types of templates.                                      | Optional          | Boolean | true                                                                                                                                                                                                                                                                                          |
| header        | Header of the template. Applicable for templateType = Text Character limit: 60                             | Optional          | String  | This is the header                                                                                                                                                                                                                                                                            |
| footer        | Footer of the template. Character limit: 60                                                                | Optional          | String  | This is the footer                                                                                                                                                                                                                                                                            |
| buttons       | Used only if your template has a CTA. An example is also submitted if a URL button has variable parameter. | Optional          | String  | [\{"type":"PHONE_NUMBER","text":"Call Us","phone_number":"+xxxxxxxxxxx"},\{"type":"URL","text":"Book A Demo","url":"[https://bookins.gupshup.io/\{\{1}}","example":["https://bookins.gupshup.io/abc"]}]](https://bookins.gupshup.io/\{\{1}}","example":\["https://bookins.gupshup.io/abc"]}]) |
| exampleMedia  | Get handleId from [here](https://docs.gupshup.io/reference/post_partner-app-appid-upload-media)            | Optional          | String  | `4::aW1hZ2UvcadG5n:ARYaMMMA2QvIXuQZdPjWVXTOqfoBU3n0L1Ftyg4w57yxi9nD105yQDvW2nu3-HNo9HGefxZ-Ig-HAi3YSsckwIsOEUwxSPatsxT0Niob30E63A:e:1634884682:2281283925530161:100033655335566:ARaBAxW-1L-ZRu6SMSg`                                                                                          |
| mediaId       | Media ID                                                                                                   | Optional          | String  | TEXT                                                                                                                                                                                                                                                                                          |
| mediaUrl      | Media URL                                                                                                  | Optional          | String  | TEXT                                                                                                                                                                                                                                                                                          |
| category      | Use category from these option AUTHENTICATION, MARKETING, UTILITY in description.                          | Optional          | String  | AUTHENTICATION                                                                                                                                                                                                                                                                                |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates/{{TEMPLATE_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'content={{CONTENT}}' \
--data-urlencode 'category={{TEMPLATE_CATEGORY}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'example={{EXAMPLE}}' \
--data-urlencode 'exampleMedia={{EXAMPLE_MEDIA}}' \
--data-urlencode 'header={{TEMPLATE_HEADER}}' \
--data-urlencode 'footer={{TEMPLATE_FOOTER}}' \
--data-urlencode 'buttons={{TEMPLATE_BUTTON}}' \
--data-urlencode 'mediaId={{MEDIA_ID}}' \
--data-urlencode 'exampleHeader={{EXAMPLE_HEADER}}'
```

### Sample Response

```json
  {
    "status": "success"
  }           
```

### Status Codes

| Status Code                                          | Response                                                                                                                                                                                                                                                                      | Comments |
| :--------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| **Success**                                          |                                                                                                                                                                                                                                                                               |          |
| 200                                                  | `{     "id": "460001903531489",     "preview": {       "expires_at": "2024-09-08T13:45:06+0000",       "preview_url": "https://business.facebook.com/wa/manage/flows/460001903531489/preview/?token=a926bc93-ce7f-465e-9c61-60800e9befab"     },     "status": "success"   }` |          |
| **Error**                                            |                                                                                                                                                                                                                                                                               |          |
| 400                                                  | `{       "status":"error",       "message":"No Template found for given id"   }`                                                                                                                                                                                              |          |
| Template does not exist for the provided templateId. |                                                                                                                                                                                                                                                                               |          |
|                                                      |                                                                                                                                                                                                                                                                               |          |

<br />
