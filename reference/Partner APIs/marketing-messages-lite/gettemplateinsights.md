---
title: Get template Ad Insight
excerpt: This API returns the details around the marketing template insights.
api:
  file: mm-lite-insight.json
  operationId: getTemplateInsights
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

    <tr>
      <td style={{ textAlign: "left" }}>
        date\_preset
      </td>

      <td style={{ textAlign: "left" }}>
        Represents a relative time range. This field is ignored if time\_range or time\_ranges is specified.
      </td>

      <td style={{ textAlign: "left" }}>
        enum{"'today', 'yesterday', 'this_month', 'last_month', 'this_quarter', 'maximum', 'data_maximum', 'last_3d', 'last_7d', 'last_14d', 'last_28d', 'last_30d', 'last_90d', 'last_week_mon_sun', 'last_week_sun_sat', 'last_quarter', 'last_year', 'this_week_mon_today', 'this_week_sun_today', 'this_year'"}
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Default - last\_30d
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fields
      </td>

      <td style={{ textAlign: "left" }}>
        Comma separated list of metrics
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/template/:templateId/insights' \
--header 'Accept: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
{
    "status": "success",
    "template_insights": [
        {
            "date_start": "2024-11-15",
            "date_stop": "2025-02-12",
            "marketing_messages_cost_per_delivered": "0.153",
            "marketing_messages_cost_per_link_btn_click": "9.18",
            "marketing_messages_delivered": "60",
            "marketing_messages_delivery_rate": "100",
            "marketing_messages_link_btn_click": "1",
            "marketing_messages_link_btn_click_rate": "1.666667",
            "marketing_messages_read": "22",
            "marketing_messages_read_rate": "36.666667",
            "marketing_messages_sent": "60",
            "marketing_messages_spend": "9.18"
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

        \{"status": "success",
        "template\_insights": \[
        \{
        "date\_start": "2024-11-15",
        "date\_stop": "2025-02-12",
        "marketing\_messages\_cost\_per\_delivered": "0.153",
        "marketing\_messages\_cost\_per\_link\_btn\_click": "9.18",
        "marketing\_messages\_delivered": "60",
        "marketing\_messages\_delivery\_rate": "100",
        "marketing\_messages\_link\_btn\_click": "1",
        "marketing\_messages\_link\_btn\_click\_rate": "1.666667",
        "marketing\_messages\_read": "22",
        "marketing\_messages\_read\_rate": "36.666667",
        "marketing\_messages\_sent": "60",
        "marketing\_messages\_spend": "9.18"
        }
        ]
        }
      </td>

      <td>
        Based on the query parameters fields, insights will be shown.
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

        "status": "error","message": "MM lite is not enabled for this app"\
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
        \{

        "status":"error","message":"Invalid template id provided."\
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
        \{

        "status":"error","message":"Unauthorised access to the resource. Please review request parameters and headers and retry"\
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Insights Fields:

All available insights fields are listed below:

* Sent, Read, Delivered, Click
  * marketing\_messages\_sent
  * marketing\_messages\_read
  * marketing\_messages\_delivered
  * marketing\_messages\_link\_btn\_click
* Rates
  * marketing\_messages\_delivery\_rate
  * marketing\_messages\_read\_rate
  * marketing\_messages\_link\_btn\_click\_rate
* Spend metrics
  * marketing\_messages\_spend
  * marketing\_messages\_cost\_per\_delivered
  * marketing\_messages\_cost\_per\_link\_btn\_click
* Conversion events
  * marketing\_messages\_website\_add\_to\_cart
  * marketing\_messages\_website\_initiate\_checkout
  * marketing\_messages\_website\_purchase
  * marketing\_messages\_website\_purchase\_values
  * marketing\_messages\_app\_add\_to\_cart
  * marketing\_messages\_app\_initiate\_checkout
  * marketing\_messages\_app\_purchase
  * marketing\_messages\_app\_purchase\_values