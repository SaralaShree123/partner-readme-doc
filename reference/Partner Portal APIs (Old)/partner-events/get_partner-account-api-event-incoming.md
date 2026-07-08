---
title: Get Inbound Message Events
excerpt: Use this API to get the inbound message logs for the specified duration.
api:
  file: partner-events-apis.json
  operationId: get_partner-account-api-event-incoming
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

| Key   | Value             | Description                                                                                                                                          | Data Types | Require/Optional | Constraints                               |
| :---- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------------- | :---------------------------------------- |
| Token | `{{PARTNER_TOKEN}}` | JWT Token issued post partner login                                                                                                                  | String     | Required         |                                           |
| appId | `{{App_ID}}`        | App ID to fetch the access token                                                                                                                     | String     | Required         | The ID should be a valid appId of Gupshup |
| ID    |                   | Unique identifier for a message                                                                                                                      |            | Optional         |                                           |
| date  | 02-05-2022        | **Note**: Data only gets updated every day at 8am IST / 11.30pm Brazil time / 4.30am Zimbabwe time. Hence you will not get logs for the current day. |            |                  |                                           |
| start | 1651500199740     | The start time in EPOCH format. The difference between start and end time must be less than or equal to 10 minutes/ 600000 milliseconds.             |            |                  |                                           |
| end   | 1651500799740     | The end time in EPOCH format                                                                                                                         |            |                  |                                           |

## Sample Request

```curl

```

## Sample Response

```json
{
  "eventList":[
	{
    "delay":56,
    "dest":"91832975XXXX",
    "endTime":1650525824281,
    "eventDescription":"Enqueued event sent to the Callback URL",
    "eventId":"569ca252-0e5b-42fb-b5e5-82270e243d",
    "source":"appname",
    "startTime":1650525824225
  }
  ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                     | Comments |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| **Success** |                                                                                                                                                                                                                                                                                                              |          |
| 200         | `{ "eventList":[ { "delay":56, "dest":"91832975XXXX", "endTime":1650525824281, "eventDescription":"Enqueued event sent to the Callback URL", "eventId":"569ca252-0e5b-42fb-b5e5-82270e243d", "source":"appname", "startTime":1650525824225 } ] }` |          |