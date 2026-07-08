---
title: Fetch Insights for a Template with Time Range and Fields
api:
  file: mmlitetimerange.json
  operationId: get_partner-app-appid-template-templateid-insights
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
        \{\{PARTNER\_APP\_TOKEN}}
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
        \{\{APP\_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Must be a valid Gupshup App ID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        templateId
      </td>

      <td style={{ textAlign: "left" }}>
        Gupshup Template ID (approved marketing only)
      </td>

      <td style={{ textAlign: "left" }}>
        68f6e094-3208-4a77-xxxx-xxxxxxxx
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Must be an approved marketing template ID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        time\_range
      </td>

      <td style={{ textAlign: "left" }}>
        Encoded JSON string with since

        and until dates
      </td>

      <td style={{ textAlign: "left" }}>
        \{"since":"2025-03-09","until":"2025-04-07"}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Format must match valid ISO date range
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fields
      </td>

      <td style={{ textAlign: "left" }}>
        Comma-separated list of metrics to fetch
      </td>

      <td style={{ textAlign: "left" }}>
        clicks, impressions, campaign\_name,...
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid list of supported insight fields
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{appId}}/template/{{templateId}}/insights?time_range=
{"since":"2025-03-09","until":"2025-04-
07"}&fields=account_currency,account_id,account_name,action_values,actions,ad_click_actions,ad_id,ad_impression
_actions,ad_name,adset_id,adset_name,attribution_setting,auction_bid,auction_competitiveness,auction_max_compet
itor_bid,buying_type,campaign_id,campaign_name,canvas_avg_view_percent,canvas_avg_view_time,clicks,conversion_v
alues,conversions,converted_product_quantity,converted_product_value,converted_promoted_product_quantity,conver
ted_promoted_product_value' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{ 
	"status": "success",
	"template_insights": 
	[ 
		{
			"account_currency": "INR",
			"account_id":
			"3242596802542159",
			"account_name":"DeepanshuWAB (Read-Only)",
			"ad_id":"120216714229190592",
			"ad_name": "pdftemplate",
			"adset_id": "120216714223580592",
			"adset_name": "pdftemplate",
			"buying_type": "AUCTION","campaign_id":"120215865319530592","campaign_name": "TrafficCampaign","canvas_avg_view_percent":"0", "canvas_avg_view_time":"0", "clicks": "0","date_start": "2025-03-09","date_stop": "2025-04-07" 
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

        "status": "success","template\_insights":
        \[
        \{
        "account\_currency": "INR",
        "account\_id":
        "3242596802542159",
        "account\_name":"DeepanshuWAB (Read-Only)",
        "ad\_id":"120216714229190592",
        "ad\_name": "pdftemplate",
        "adset\_id": "120216714223580592",
        "adset\_name": "pdftemplate",
        "buying\_type": "AUCTION","campaign\_id":"120215865319530592","campaign\_name": "TrafficCampaign","canvas\_avg\_view\_percent":"0", "canvas\_avg\_view\_time":"0", "clicks": "0","date\_start": "2025-03-09","date\_stop": "2025-04-07"
        }
        ]
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{\
        "status": "success",
        "template\_insights": \[]
        }
      </td>

      <td>
        Success response but no insights available for the given parameters.
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
        \{ "status": "error", "message": "The template ID provided is invalid." }
      </td>

      <td>
        Triggered when the template ID is not found or malformed
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{ "status": "error", "message": "MM Lite is currently disabled for this application." }
      </td>

      <td>
        MM Lite feature is not enabled for the specified app.
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{ "status": "error", "message": "template insights are only supported for approved marketing templates" }
      </td>

      <td>
        Attempt to fetch insights for a non-approved marketing template.
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{ "status": "error", "message": "Authentication failed" }
      </td>

      <td>
        Invalid or missing authentication token.
      </td>
    </tr>
  </tbody>
</Table>