---
title: Update Inbound Events on App's Callback
excerpt: >-
  Use this API to update the type of events you receive on your callback URL for
  your Gupshup app.
api:
  file: partner-portal-public-apis-4.json
  operationId: put_partner-app-appid-callback-mode
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 🚧 ⚠We are going to be deprecating this API soon, we request you that you start using the [subscription API](/reference/setsubscription-api-v3#/), as it provides you with a granular control for event management on your callback URL

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner App Access Token</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId for the app whose business email need to verify.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>The ID should be a valid app Id of Gupshup</li>
<li>It should belong to the same account as the apikey</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>modes</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{MODES}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Update inbound events that you want to receive on your App&#39;s callback URL. You may provide all the values for which you want to receive events. If no values are provided, all events will be deselected.<br>Possible values - DLR events: DELIVERED, READ, SENT, DELETED, and OTHERS.<br>System events: TEMPLATE and ACCOUNT.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/callback/mode' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'modes={{MODES}}'	
```

## Sample Response

```json
{
    "callback": {
        "custom": false,
        "modes": [
            "SENT",
            "DELIVERED",
            "READ",
            "DELETED"
        ]
    },
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                                        | Comments               |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                 |                        |
| 200         | `{ "callback": { "custom": false, "modes": [ "SENT", "DELIVERED", "READ", "DELETED" ] }, "status": "success" }`                                 |                        |
| **Error**   |                                                                                                                                                 |                        |
| 429         | `{ "status": "error", "message": "Too Many Requests" }`                                                                                         | 10 Requests per Minute |
| 500         | `{ "status": "error", "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support" }` | For any Internal Error |