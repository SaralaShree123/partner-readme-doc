---
title: Delete specific subscription of an app
excerpt: >-
  This API endpoint enables partners to delete a specific webhook subscription
  by its unique subscription ID. Unlike the general delete subscription endpoint
  that removes all subscriptions for an app, this endpoint provides granular
  control to remove individual subscriptions when multiple webhook
  configurations exist. This is particularly useful for managing
  multi-environment setups, removing deprecated webhooks, or cleaning up test
  subscriptions.
api:
  file: delete-specific-subscription.json
  operationId: delete_partner-app-appid-subscription-subscriptionid
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

| Key              | Value                     | Description                                        | Data Types | Require/Optional | Constraints                                                              |
| :--------------- | :------------------------ | :------------------------------------------------- | :--------- | :--------------- | :----------------------------------------------------------------------- |
| Authorization    | \{\{PARTNER\_APP\_TOKEN}} | Partner app access token issued post partner login | String     | Required         | Should be a valid Partner app access token belonging to the passed appId |
| appId            | \{\{App\_ID}}             | App ID for the app to be deleted                   | String     | Required         | Valid app ID                                                             |
| SUBSCRIPTION\_ID | 2xxxx                     | Subscription ID                                    | String     | Required         | Id of the subscription to be deleted                                     |

## Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/subscription/{{SUBSCRIPTION_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Status Code
      </th>

      <th style={{ textAlign: "left" }}>
        Response
      </th>

      <th style={{ textAlign: "left" }}>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **Success**
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        204
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Success when subscriptions are deleted. No content.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Error**
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "status": "error",\
          "message": "API key is not associated with partner"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        Error with respect to API Key
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        429
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "status": "error",\
          "message": "Too Many Requests"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        Rate limit exceeded
      </td>
    </tr>
  </tbody>
</Table>