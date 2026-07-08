---
title: Get All Subscriptions
excerpt: >-
  This API endpoint retrieves all the current webhook subscription configuration
  for a partner application. It returns details about the subscribed event
  types, webhook URL, subscription status, and metadata. This is useful for
  verifying webhook configurations, auditing subscription settings, and
  troubleshooting event delivery issues.
api:
  file: GetAllSubscriptions.json
  operationId: get_partner-app-appid-subscription
hidden: true
---
### Request Parameters

| Key           | Description                      | Value                   | Data type | Required/Optional | Constraints                                                             |
| :------------ | :------------------------------- | :---------------------- | :-------- | :---------------- | :---------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String    | Required          | Should be a valid Partner App Access Tokenalid Partner App Access Token |
| appId         | App ID to fetch the access token | `{{APP_ID}}`            | String    | Required          | The Id should be a valid app Id of Gupshup                              |

### Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APPId}}/subscription' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
	"status": "success",
	"subscriptions": [
		{
		"active": true,
		"appId": "57d9179b-7412-4621-bf86-57ee1962fd12",
		"createdOn": 1735818105594,
		"id": "29040",
		"mode": 16383,
		"modes": [
			"SENT",
			"DELIVERED",
			"READ",
			"DELETED",
			"OTHERS",
			"FAILED",
			"MESSAGE",
			"TEMPLATE",
			"ACCOUNT",
			"BILLING",
			"ENQUEUED",
			"FLOWS_MESSAGE",
			"PAYMENTS",
			"ALL"
		],
		"modifiedOn": 1735818105594,
		"showOnUI": false,
		"tag": "mm",
		"url":"https://webhook.site/e1d58c71-2c14-4e82-90ce-4fd4c0caaf96",
		"version": 3
		}
	]
}
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
      </th>

      <th>
        Response
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{
        "status": "success",
        "subscriptions": [
        \{
        "active": true,
        "appId": "57d9179b-7412-4621-
        bf86-57ee1962fd12",
        "createdOn": 1735818105594,
        "id": "29040",
        "mode": 16383,
        "modes": [
        "SENT",
        "DELIVERED",
        "READ",
        "DELETED",
        "OTHERS",
        "FAILED",
        "MESSAGE",
        "TEMPLATE",
        "ACCOUNT",
        "BILLING",
        "ENQUEUED",
        "FLOWS_MESSAGE",
        "PAYMENTS",
        "ALL"
        ],
        "modifiedOn": 1735818105594,
        "showOnUI": false,
        "tag": "mm",
        "url":
        "

        [https://webhook.site/e1d58c71-2c14-4e82-](https://webhook.site/e1d58c71-2c14-4e82-)


        90ce-4fd4c0caaf96",
        "version": 3
        }
        ]
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        \{
        "status": "error",
        "message": "Too Many Requests"
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{
        "status": "error",
        "message": "Internal server error. Please try again later and If issue still persist, then contact Gupshup Dev Support"
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>