---
title: Get template Ad details
excerpt: This API returns the details around the marketing template Ad account.
api:
  file: mm-lite-insight.json
  operationId: getTemplateAdDetails
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
        App ID for which the ad details are required
      </td>

      <td style={{ textAlign: "left" }}>
        `{{App_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        TemplateId
      </td>

      <td style={{ textAlign: "left" }}>
        Marketing template ID for which the ad details are required
      </td>

      <td style={{ textAlign: "left" }}>
        `{{templateId}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Valid Marketing Template Id
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/template/:templateId/ads' \
--header 'Accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
 "status":"success",
 "template_ad_details":
    {
     "ad_account_id":"3242596802542159",
     "ad_adset_id":"120215865443300592",
     "ad_campaign_id":"120215865319530592",
     "ad_id":"120215865446460592",
     "category":"MARKETING",
     "id":"939035207269681"
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

        "status":"success","template\_ad\_details":
        \{
        "ad\_account\_id":"3242596802542159",
        "ad\_adset\_id":"120215865443300592",
        "ad\_campaign\_id":"120215865319530592",
        "ad\_id":"120215865446460592",
        "category":"MARKETING",
        "id":"939035207269681"
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

        "status": "error","message": "MM lite is not enabled for this app"
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{ &#x20;
        "status":"error",
        "message":"Invalid template id provided."
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{ &#x20;
        "status":"error",
        "message":"Unauthorised access to the resource. Please review request parameters and headers and retry"
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>