---
title: Get analytics for a specific webhook subscription of an app
excerpt: >-
  Fetch callback health analytics such as latency, success and failure rates for
  a specific webhook subscription.
api:
  file: GetSubscriptionAnalytics.json
  operationId: getSubscriptionAnalytics
hidden: true
---
# Rate Limiting

**⚠️ IMPORTANT: Rate limiting applied**

1. Limit: 10 requests per 60 seconds
2. Purpose: Prevents abuse of operations
3. Exceeded: Returns 429 Too Many Requests

<br />

# API Request:

```
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/subscription/{{SUBSCRIPTION_ID}}/analytics?aggBy=15m' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

# API Response:

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
        200
      </td>

      <td>
        ```
        {
            "analytics": {
                "series": [
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765432200000
                    },
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765432800000
                    },
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765433400000
                    },
                    {
                        "averageLatency": 355,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 580,
                        "successCount": 6,
                        "timestamp": 1765434000000
                    },
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765434600000
                    },
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765435200000
                    },
                    {
                        "averageLatency": 0,
                        "failureCount": 0,
                        "failureRate": 0,
                        "maxLatency": 0,
                        "successCount": 0,
                        "timestamp": 1765435800000
                    }
                ],
                "summary": {
                    "averageLatency": 355,
                    "failureCount": 0,
                    "failureRate": 0,
                    "maxLatency": 580,
                    "successCount": 6,
                    "timestamp": 1765436101084
                }
            },
            "status": "success"
        }
        ```
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `{
          "status": "error",
          "message": "<Subscription specific error message>"
        }`
      </td>

      <td>
        Error details
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        `{
          "status": "error",
          "message": "Too Many Requests"
        }`
      </td>

      <td>
        Rate limit errors
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `{
            "message": "Error while getting analytics",
            "status": "error"
        }`
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<br />

# Request Params

<br />

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Value
      </th>

      <th>
        Data Type
      </th>

      <th>
        Required / Optional
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorization
      </td>

      <td>
        Access Token for the application
      </td>

      <td>
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td>
        APP_ID
      </td>

      <td>
        App ID to fetch the access token
      </td>

      <td>
        `{{APP_ID}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        The Id should be a valid app Id of Gupshup  

        The App must be associated with the account that owns the PARTNER_APP_TOKEN being used
      </td>
    </tr>

    <tr>
      <td>
        SUBSCRIPTION_ID
      </td>

      <td>

      </td>

      <td>
        `{{SUBSCRIPTION_ID}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Id of the subscription to get analytics
      </td>
    </tr>

    <tr>
      <td>
        aggBy
      </td>

      <td>
        Aggregated By field for the timeline
      </td>

      <td>

      </td>

      <td>
        String
      </td>

      <td>
        Optional
      </td>

      <td>
        Default value - 1 hr
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
