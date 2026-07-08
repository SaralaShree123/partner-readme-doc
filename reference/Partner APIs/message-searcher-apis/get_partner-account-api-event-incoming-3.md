---
title: Get Inbound Message Events
excerpt: Use this API to get the inbound message logs for the specified duration.
api:
  file: partner-events-apis-2.json
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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Data type</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for an app</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid appId for the account.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9e97a0d-add3-4as557-1535-4cdf47c3fa68</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for a message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>date</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>02-05-2022</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>date in DD-MM-YYYY format.<br><strong>Note:</strong> Data only gets updated every day at 8 am IST / 11.30 pm Brazil time / 4.30 am Zimbabwe time.  Hence you will not get logs for the current day.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>start</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1651500199740</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The start time is in EPOCH format. The difference between start and end time must be less than or equal to 10 minutes/ 600000 milliseconds.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/account/api/event/incoming?
id=&appId=&date=&start=&end=' \
--header 'token: <PARTNER_TOKEN>'
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
| 200         | `{     "eventList":[   	{       "delay":56,       "dest":"91832975XXXX",       "endTime":1650525824281,       "eventDescription":"Enqueued event sent to the Callback URL",       "eventId":"569ca252-0e5b-42fb-b5e5-82270e243d",       "source":"appname",       "startTime":1650525824225     }     ]   }` |          |