---
api:
  file: updateAppSubscriptionOpneApi.json
  operationId: put_partner-app-appid-subscription-subscriptionid
hidden: false
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
        * The Id should be a valid app Id of Gupshup. - The App must be associated with the account that owns the PARTNER_APP_TOKEN being used
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        SUBSCRIPTION_ID
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
        The identifier for the subscription to updated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [modes](/reference/setsubscription-api-v3#/modes)
      </td>

      <td style={{ textAlign: "left" }}>
        Stages in subscription processing
      </td>

      <td style={{ textAlign: "left" }}>
        \<MODES>
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * Should be one of the following : NONE, READ, DELIVERED, SENT, DELETED, OTHERS - for version 3 TEMPLATE, ACCOUNT, COPY **are not supported**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        tag
      </td>

      <td style={{ textAlign: "left" }}>
        Name tag for URL
      </td>

      <td style={{ textAlign: "left" }}>
        \<name_tag_for_url>
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        tag must be unique for each app
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        url
      </td>

      <td style={{ textAlign: "left" }}>
        Callback URL
      </td>

      <td style={{ textAlign: "left" }}>
        \<callback_url>
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Should be valid URL
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        version
      </td>

      <td style={{ textAlign: "left" }}>
        Version
      </td>

      <td style={{ textAlign: "left" }}>
        \<version>
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Should be one of the following : 2,3
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        doCheck
      </td>

      <td style={{ textAlign: "left" }}>
        For bypassing URL check
      </td>

      <td style={{ textAlign: "left" }}>
        \<for_bypassing_url_check>
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a boolean value : true/false
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        active
      </td>

      <td style={{ textAlign: "left" }}>
        active status of subscription
      </td>

      <td style={{ textAlign: "left" }}>
        \<true/false>
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a boolean value : true/false
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/subscription/{{SUBSCRIPTION_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'url=<callback_url>' \
--data-urlencode 'tag=<name_tag_for_url>' \
--data-urlencode 'version=<Version>' \
--data-urlencode 'modes=<MODES>' \
--data-urlencode 'doCheck=<for_bypassing_url_check>' \
--data-urlencode 'active=<true/false>'
```

## Sample Response

```
{
  "status" : "success",
  "subscription" : {
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

<br />

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

        "status" : "success","subscription" :\{"active" : true,
         "appId" : "657c0203-0b4d-4ba1-bbf5-a679cfa35a16",
         "createdOn" : 1739862125507,
         "id" : "32595",
         "latencyBucket" : "lt_1_s",
         "mode" : 1025,
         "modes" : ["SENT", "ENQUEUED"],
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

        "status": "error","message": "API key is not associated with partner"}
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

        "status": "error","message": "Subscription Does Not Exist"}
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

        "status": "error","message": "Authentication Failed"}
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

        "status": "error","message": "Not Subscription Owner"}
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

        "status": "error","message": "Too Many Requests"}
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
