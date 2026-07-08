---
title: Initiate solution migrate
excerpt: Use this API to initiate the solution migrate.
api:
  file: partner-portal-api-34.json
  operationId: setSolution
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

| Key           | Value             | Description   | Constraints                     |
| :------------ | :---------------- | :------------ | :------------------------------ |
| PARTNER_TOKEN | `{{PARTNER_TOKEN}}` | Partner token | Should be a valid partner token |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/solution/migrate/intent/status' \
--header 'Authorization: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded'
```

## Sample Response

```json
{  
"status": "success",  
"appStatus": [  
		{  
			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",  
			"partnerId": 173,  
			"status": "SUCCESS"  
		},  
		{  
			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",  
			"partnerId": 173,  
			"status": "ERROR",  
			"reason": "Error validating access token: The session has been invalidated because the user changed their password or Facebook has changed the session for security reasons"  
		},  
		{  
			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",  
			"partnerId": 173,  
			"status": "PENDING"  
		}  
	]  
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Comments                                                 |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                          |
| 200         | `{   "status": "success",   "appStatus": [   		{   			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",   			"partnerId": 173,   			"status": "SUCCESS"   		},   		{   			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",   			"partnerId": 173,   			"status": "ERROR",   			"reason": "Error validating access token: The session has been invalidated because the user changed their password or Facebook has changed the session for security reasons"   		},   		{   			"appId": "6856aae0-d775-48b4-aae2-a89e4e6c2a5a",   			"partnerId": 173,   			"status": "PENDING"   		}   	]   }` | Success when status is fetched and migration is running. |
| 200         | `{   "status": "success",   "appStatus": []   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                          |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                          |
| 400         | `{   	"status":"error",   	"message/data":"&lt;Specific to API&gt;"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Error with respect to API                                |
| 401         | `{   	"status":"error",   	"message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | When authentication fails                                |
| 500         | `{   	"status":"error",   	"message":"Internal Server Error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | For any Internal Error                                   |