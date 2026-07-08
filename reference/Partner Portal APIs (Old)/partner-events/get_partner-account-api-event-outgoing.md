---
title: Get Outbound Message Events
excerpt: Use this API to get the outbound message logs for the specified date.
api:
  file: partner-events-apis.json
  operationId: get_partner-account-api-event-outgoing
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
  <th style="border: 1px solid #ddd; padding: 8px;">Data Types</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Require/Optional</th>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{App_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App ID to fetch the access token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ID</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for a message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>date</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>02-05-2022</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>date in DD-MM-YYYY format.<br><strong>Note</strong>: Data only gets updated every day at 8am IST / 11.30pm Brazil time / 4.30am Zimbabwe time. Hence you will not get logs for the current day.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/account/api/event/outgoing?id=&appId=&date='
--header 'token: <PARTNER_TOKEN>'
```

## Sample Response

```json
{
	"eventList":[
	{
		"delay":3,
		"dest":"91991183XXXX",
		"endTime":1650524010311,
		"eventDescription":"Send message request received at Gupshup",
		"eventId":"3b506e13-d87d-482d-abc1-b8ac688b7c",
		"source":"91845XXXX087",
		"startTime":1650524010308
	},
	{
		"delay":16,
		"dest":"91991183XXXX",
		"endTime":1650524010340,
		"eventDescription":"Send message completed",
		"eventId":"3b506e13-d87d-482d-abc1-beb8ac688b7c",
		"source":"91845XXXX087",
		"startTime":1650524010324
	}
	]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comments |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |          |
| 200         | `{   	"eventList":[   	{   		"delay":3,   		"dest":"91991183XXXX",   		"endTime":1650524010311,   		"eventDescription":"Send message request received at Gupshup",   		"eventId":"3b506e13-d87d-482d-abc1-b8ac688b7c",   		"source":"91845XXXX087",   		"startTime":1650524010308   	},   	{   		"delay":16,   		"dest":"91991183XXXX",   		"endTime":1650524010340,   		"eventDescription":"Send message completed",   		"eventId":"3b506e13-d87d-482d-abc1-beb8ac688b7c",   		"source":"91845XXXX087",   		"startTime":1650524010324   	}   	]   }` |          |