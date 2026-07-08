---
title: Product
excerpt: Use this API to send message with the Product template.
api:
  file: product-send-message.json
  operationId: post_partner-app-appid-template-msg
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

| Key           | Description                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                           | Data type | Required/Optional | Constraints                                                                                                                                                                                                                                |
| :------------ | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------- | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}`                                                                                                                                                                                                                                                                                                                                                                                                           | String    | Required          | Should be a valid Partner App Access Token                                                                                                                                                                                                 |
| APP_ID        | App ID to fetch the access token | `{{APP_ID}}`                                                                                                                                                                                                                                                                                                                                                                                                                      | String    | Required          | - The Id should be a valid app Id of Gupshup - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used                                                                                                      |
| source        | Source Phone Number              | `{{SOURCE}}`                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer   | Required          |                                                                                                                                                                                                                                            |
| sandbox       | Boolean value                    | `{{SANDBOX}}`                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean   | Optional          |                                                                                                                                                                                                                                            |
| destination   | Destination Phone Number         | `{{DESTINATION}}`                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer   | Required          |                                                                                                                                                                                                                                            |
| template      | Json containing template details | `{      "id":"{{TEMPLATE_ID}}",      "params":[         "{{PRODUCT_ID}}"      ],      "mpm":{         "sections":\[            {               "title":"{{TITLE}}",               "products":[                  "{{PRODUCT_ID}}"               ]            },            {               "title":"{{TITLE1}}",               "products":[                  "{{PRODUCT_ID}}"               ]            }         ]      }   }` | String    | Required          | - Template must have valid template Id  - Params must include all params including a product id  - Sections param must be provided with valid ids`{     "id": "\<template_id>",     "params": [       <list_of_template_parameters>     ]` |
| src.name      | App Name                         | `{{APP_NAME}}`                                                                                                                                                                                                                                                                                                                                                                                                                    | String    | Required          |                                                                                                                                                                                                                                            |
| channel       | Channel                          | `{{CHANNEL_NAME}}`                                                                                                                                                                                                                                                                                                                                                                                                                | String    |                   | Must be Whatsapp                                                                                                                                                                                                                           |
|               |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                 |           |                   |                                                                                                                                                                                                                                            |

## Sample Request

```curl
curl --request POST \
     --url https://partner.gupshup.io/partner/app/947d28b8-459b-4dfe-9d4c-0ac8c6c245c9/template/msg \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'token: sk_711916ad1d5d4f21a9520fdef20516a1' \
     --data source=919643874844 \
     --data destination=918886912227 \
     --data sandbox=true \
     --data src.name=ProdMonitoringCloud \
     --data 'template={
   "id":"3b9bf65b-979c-44d3-a269-dec2f20c4e52",
   "params":[
      "zqc2qfz5fm"
   ],
   "mpm":{
      "sections":[
         {
            "title":"Products",
            "products":[
               "zqc2qfz5fm"
            ]
         },
         {
            "title":"Products2",
            "products":[
               "xyli96fcbn"
            ]
         }
      ]
   }
}' \
     --data channel=whatsapp

```

## Sample Response

```json
{
  "status": "submitted",
  "messageId": "eb152a75-6f6d-41c2-ba9b-ea8dae4d0f63"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                     | Comments               |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                              |                        |
| 200         | `{     "status": "submitted",     "messageId": "eb152a75-6f6d-41c2-ba9b-ea8dae4d0f63"   }`                                                                   |                        |
| **Error**   |                                                                                                                                                              |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                            | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later. If the issue still persists, then contact Gupshup Dev Support"   }` | For any Internal Error |