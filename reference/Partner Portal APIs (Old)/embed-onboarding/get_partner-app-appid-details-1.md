---
title: Get App details based on appId
excerpt: Use this API to fetch the app details based on appId.
api:
  file: onboarding-api.json
  operationId: get_partner-app-appid-details
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Key           | Description                                   | Constraints                                                                                                  | Required/Optional | Type   | Value |
| :------------ | :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :---------------- | :----- | :---- |
| PARTNER_TOKEN | JWT Token issues post Partner login           | Should be a valid Partner JWT Token.                                                                         |                   | String |       |
| appId         | id of the app for which data is to be fetched | - The ID should be a valid appId of Gupshup - App should be in the account whose PARTNER_TOKEN is being used |                   | String |       |

### Sample Request

```curl
curl --location --request GET '{{partner_portal_base_url}}/partner/app/:appId/details' \
--header 'token: {{PARTNER_TOKEN}}'
```

### Sample Response

```json
{ 
	"status": "success",
 	"appDetails": {
 		"billingType": "<POSTPAID,PREPAID>",
 		"createdOn": "<timestamp>",
        "callbackUrl": "<callback_url>", //if set
 		"disableOptinPrefUrl": "<true/false>",
 		"embedAllowed": "<true/false>",
 		"federated": "<true/false>",
 		"id": "<app_id>",
 		"languageCode": "<language_code>", 
		"live": "<true/false>",
 		"liveTs": "<timestamp>",
 		"modifiedOn": "<timestamp>",
 		"name": "<app_name>",
        "phone": "phone",
 		"stopped": "<true/false>",
 		"storageRegion": "<BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR>", 
 		"templateMessaging": "<true/false>", 
 		"type": "apicallbackpost",
 		"version": "<0,1,2>"
	},
 	"app": "true"
}
```

### Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Comment                                                             |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                     |
| 200         | `{   	"status": "success",    	"appDetails": {    		"billingType": "<POSTPAID,PREPAID>",    		"createdOn": "<timestamp>",           "callbackUrl": "<callback_url>", //if set    		"disableOptinPrefUrl": "<true/false>",    		"embedAllowed": "<true/false>",    		"federated": "<true/false>",    		"id": "<app_id>",    		"languageCode": "<language_code>",   		"live": "<true/false>",    		"liveTs": "<timestamp>",    		"modifiedOn": "<timestamp>",    		"name": "<app_name>",           "phone": "phone",    		"stopped": "<true/false>",    		"storageRegion": "<BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR>",    		"templateMessaging": "<true/false>",    		"type": "apicallbackpost",    		"version": "<0,1,2>"   	},    	"app": "true"   }` |                                                                     |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                     |
| 400         | `{     "status":"error",     "message/data":"<Specific to API>"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Either the request parameter type or HTTP request type is incorrect |
| 401         | `{     "status":"error",     "message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | If the token is incorrect or forbidden.                             |
| 403         | `{     "status":"error",     "message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | When app does not belong to the Partner                             |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | When the rate limit is exceeded                                     |