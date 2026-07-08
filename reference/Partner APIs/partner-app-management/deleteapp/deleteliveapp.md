---
title: Delete Live App
excerpt: Use this API to delete Live app.
api:
  file: partner-portal-api-9.json
  operationId: deleteAppSandbox
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

| Key               | Description                                        | Constraints                                                              |
| :---------------- | :------------------------------------------------- | :----------------------------------------------------------------------- |
| PARTNER_APP_TOKEN | Partner app access token issued post partner login | Should be a valid Partner app access token belonging to the passed appId |
| appId             | App ID for the app to be deleted                   | Valid appId                                                              |
| deleteLiveApp     | true/false                                         | Optional. Default is false                                               |
| comment           | Comment for app deletion                           | Optional                                                                 |
|                   |                                                    |                                                                          |

## Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/:appId?deleteLiveApp=true&comment=Delete app' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
    "message": "App deleted successfully",
    "status": "success"
}

```

## Status Codes

| Status Code | Response                                                                       | Comments                    |
| :---------- | :----------------------------------------------------------------------------- | :-------------------------- |
| **Success** |                                                                                |                             |
| 200         | `{       "message": "App deleted successfully",       "status": "success"   }` | Success when app is deleted |
| **Error**   |                                                                                |                             |
| 400         | `{     "status":"error",     "message/data":"&lt;Specific to API&gt;"   }`     | Error with respect to API   |
| 401         | `{     "status":"error",     "message":"Unauthorized Access"   }`              | When authentication fails   |
| 403         | `{     "status":"error",     "message":"Unauthorized Access"   }`              | Access is not allowed       |
| 429         | `{       "status": "error",       "message": "Too Many Requests"   }`          | 20 calls per minute         |
| 500         | `{     "status": "error",     "message": "Internal Server Error"   }`          | For any Internal Error      |