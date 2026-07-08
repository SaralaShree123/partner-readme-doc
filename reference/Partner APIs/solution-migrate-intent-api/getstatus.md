---
title: Get solution migrate status
excerpt: Use this API to fetch the solution migrate status.
api:
  file: partner-portal-api-36.json
  operationId: getStatus
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

| Key           | Value             | Description                                                         | Constraints                                     |
| :------------ | :---------------- | :------------------------------------------------------------------ | :---------------------------------------------- |
| PARTNER_TOKEN | `{PARTNER_TOKEN}` | Partner token                                                       | Should be a valid partner token                 |
| email         |                   | Email ID to be used for notifications with respect to the migration | Should be a valid appId for the account.        |
| app_list      |                   | List of app IDs                                                     | Optional. List of app IDs separated by a comma. |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/solution/migrate/intent' \
--header 'Authorization: {PARTNER_TOKEN}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'email={EMAIL}' \
--data-urlencode 'app_list={APP_ID_LIST}'
```

## Sample Response

```json
{
	"status": "success",
	"message": "Solution migrate intent has been started."
}
```

## Status Codes

| Status Code | Response                                                                                  | Comments                                   |
| :---------- | :---------------------------------------------------------------------------------------- | :----------------------------------------- |
| **Success** |                                                                                           |                                            |
| 200         | `{ "status": "success", "message": "Solution migrate intent has been started." }` | Success when migration has been triggered. |
| **Error**   |                                                                                           |                                            |
| 400         | `{ "status":"error", "message/data":"<Specific to API>" }`                        | Error with respect to API                  |
| 401         | `{ "status":"error", "message":"Unauthorized Access" }`                           | When authentication fails                  |
| 500         | `{ "status":"error", "message":"Internal Server Error" }`                         | For any Internal Error                     |