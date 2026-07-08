---
title: Disable button click analytics
excerpt: >-
  This API endpoint enables or disables button click analytics for a specific
  template. Button click tracking allows you to monitor user interactions with
  buttons in your WhatsApp message templates. This endpoint provides granular
  control over which templates have button click analytics enabled.
api:
  file: partner-release-85-apis.json
  operationId: post_partner-app-appid-template-analytics-buttonclick
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key           | Description                                      | Value                 | Type    | Required/Optional | Constraints                                |
| :------------ | :----------------------------------------------- | :-------------------- | :------ | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application                 | `{{PARTNER_APP_TOKEN}}` | String  | Required          | Should be a valid Partner App Access Token |
| APP_ID        | App ID to fetch the access token                 | `{{APP_ID}}`            | String  | Required          | The ID should be a valid app ID of Gupshup |
| templateId    | gs-template id of template                       | `{{TEMPLATE_ID}}`       | String  | Required          |                                            |
| disable       | flag to disable or enable button click analytics | True/False            | Boolean | Required          |                                            |

## Sample Request

```curl
curl --location --request POST '{{BASE_URL}}/partner/app/{{APP_ID}}/template/analytics/buttonclick' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'templateId={{TEMPLATE_ID}}' \
--data-urlencode 'disable=false'
```

## Sample Response

```
{
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                                        | Comment             |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| **Success** |                                                                                                                                                 |                     |
| 200         | `{     "stauts": "sucess"   }`                                                                                                                  | Successful response |
| **Error**   |                                                                                                                                                 |                     |
| 401         | `{       "status": "error",       "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"   }` |                     |