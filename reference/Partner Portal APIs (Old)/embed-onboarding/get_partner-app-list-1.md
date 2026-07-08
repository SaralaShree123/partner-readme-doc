---
title: Filter and get list of Apps for the Partner
excerpt: >-
  Use this API to fetch all the list of apps for the account based on the query
  parameters.
api:
  file: onboarding-api.json
  operationId: get_partner-app-list
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Parameters

| Key           | Description                                                   | Constraints                                               | Required/Optional |
| :------------ | :------------------------------------------------------------ | :-------------------------------------------------------- | :---------------- |
| PARTNER_TOKEN | JWT Token issues post Partner login                           | Should be a valid Partner JWT Token.                      |                   |
| name          | App name to be searched (`Contains Search` will be executed)  | If passed with phone & operation will be executed         | Optional          |
| phone         | Phone to be searched (`Contains Search` will be executed)     | Phone to be searched (`Contains Search` will be executed) |                   |
| pageNo        | Page Number. Default is 1 if not passed                       | greater than zero                                         |                   |
| pageSize      | Number of records in a response. Default is 10 if not passed. | greater than zero                                         |                   |

## Sample Request

```curl
curl --location --request GET '{{partner_portal_base_url}}/partner/app/list?name=&lt;name_like&gt;&phone=&lt;phone_like&gt;&pageNo=&lt;page_Number&gt;&pageSize=&lt;elements_per_page&gt;' \ 
--header 'token: {{PARTNER_TOKEN}}'
```

## Sample Response

```json
[
  {
    "id": "<app_id>",
    "name": "<app_name>",
    "type": "<app_type>",
    "live": <true/false>,
    "phone": <phone_number_with_country_code>,
    "stopped": <true/false>,
    "storageRegion": "<BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR>",
    "uiFormStage": null,
    "pipelineStage": null,
    "creationStage": null,
    "whatsappVerificationStatus": null,
    "version": <0,1,2>,
    "products": ["ANALYTICS", "CUSTOMER_SUPPORT"],
    "createdOn": <epoch_timestamp>,
    "modifiedOn": <epoch_timestamp>
  }
],
"status": "success"
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Comment                                                             |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                     |
| 200         | `{       [{           "id": "<app_id>",           "name" : "<app_name>",           "type" : "<app_type>",           "live": <true/false>,           "phone" : <phone_number_with_country_code>,           "stopped": <true/false>,           "storageRegion" : "<BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR>",           "uiFormStage" : null,           "pipelineStage" : null,           "creationStage" : null,           "whatsappVerificationStatus" : null,           "version": <0,1,2>,           "products" : ["ANALYTICS","CUSTOMER_SUPPORT"],           "createdOn": <epoch_timestamp>,           "modifiedOn": <epoch_timestamp>       }],       "status": "success"   }` |                                                                     |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                     |
| 400         | `{     "status":"error",     "message/data":"<Specific to API>"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Either the request parameter type or HTTP request type is incorrect |
| 401         | `{     "status":"error",     "message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | If the token is incorrect or forbidden.                             |
| 403         | `{     "status":"error",     "message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | When app does not belong to the Partner                             |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | When the rate limit is exceeded                                     |