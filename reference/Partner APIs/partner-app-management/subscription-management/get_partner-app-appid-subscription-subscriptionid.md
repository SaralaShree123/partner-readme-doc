---
title: Get Specific App Subscription
excerpt: >-
  This API endpoint retrieves detailed information about a specific webhook
  subscription by its unique subscription ID. Unlike the general subscription
  endpoint, this provides granular access to individual subscription
  configurations with enhanced response fields including human-readable event
  modes array, latency bucket information, and complete subscription metadata.
api:
  file: getAppSubscriptionOpenApi.json
  operationId: get_partner-app-appid-subscription-subscriptionid
hidden: true
---
## Request Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        `{{APP_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        \- The Id should be a valid app Id of Gupshup.
        \- The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        SUBSCRIPTION\_ID
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        2xxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier for the subscription to retrieve.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/subscription/{{SUBSCRIPTION_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
  "status" : "success",
  "subscription" : 
  {
    "active" : true,
    "appId" : "657c0203-0b4d-4ba1-bbf5-a679cfa35a16",
    "createdOn" : 1739862125507,
    "id" : "32595",
    "latencyBucket" : "lt_1_s",
    "mode" : 1025,
    "modes" : [ "SENT", "ENQUEUED" ],
    "modifiedOn" : 1739870558358,
    "showOnUI" : false,
    "tag" : "V33i4",
    "url" : "https://01hqjda5pbywgv7xw5e9ckd5e800-51132d4cc32709e9078d.requestinspector.com",
    "version" : 2
  }
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

        "status" : "success","subscription" :
        \{
        "active" : true,
        "appId" : "657c0203-0b4d-4ba1-bbf5-a679cfa35a16",
        "createdOn" : 1739862125507,
        "id" : "32595",
        "latencyBucket" : "lt\_1\_s",
        "mode" : 1025,
        "modes" : \[ "SENT", "ENQUEUED" ],
        "modifiedOn" : 1739870558358,
        "showOnUI" : false,
        "tag" : "V33i4",
        "url" : "[https://01hqjda5pbywgv7xw5e9ckd5e800-51132d4cc32709e9078d.requestinspector.com](https://01hqjda5pbywgv7xw5e9ckd5e800-51132d4cc32709e9078d.requestinspector.com)",
        "version" : 2
        }
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
        400
      </td>

      <td>
        \{

        "status": "error","message": "API key is not associated with partner"
        }
      </td>

      <td>
        when API key not found on partner DB
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error","message": "Subscription Does Not Exist"
        }
      </td>

      <td>
        When a subscription does not exist with the provided subcriptionId
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{

        "status": "error","message": "Authentication Failed"
        }
      </td>

      <td>
        When authentication fails
      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        \{

        "status": "error","message": "Not Subscription Owner"
        }
      </td>

      <td>
        When the requested subscription is not associated with the provided appId
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        \{

        "status": "error","message": "Too Many Requests"
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>