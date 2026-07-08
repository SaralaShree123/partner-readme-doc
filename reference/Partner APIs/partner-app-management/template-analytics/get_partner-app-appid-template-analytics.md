---
api:
  file: partner-release-85-apis.json
  operationId: get_partner-app-appid-template-analytics
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note
>
> You will get the results in IST

# Rate Limiting

⚠️ **IMPORTANT**: Rate limiting applied

**Limit**: 5 requests per 60 seconds

**Purpose**: Prevents excessive analytics queries

**Exceeded**: Returns 429 Too Many Requests

<br />

# Important Notes

⚠️ **Key Considerations**

**Required Parameter**: template_ids is mandatory

**Format**: Use comma-separated values for multiple templates

**Timestamps**: Unix epoch milliseconds or YYYY-MM-DD for start/end

**Granularity**: Choose based on analysis needs (AGGREGATED/DAILY)

**Data Freshness**: May have a slight delay from real-time

**Time Zones**: All timestamps in UTC

<br />

# To retrieve offsite conversion metrics, the same Template Analytics API must be invoked with additional parameters and constraints.

## Mandatory Changes for MM Lite

<br />

| Aspect             | Non–MM Lite         | MM Lite                     |
| :----------------- | :------------------ | :-------------------------- |
| product_type       | CLOUD_API (default) | MARKETING_MESSAGES_LITE_API |
| use_waba_timezone  | Optional / false    | Must be true                |
| start, end format  | UNIX timestamp      | YYYY-MM-DD                  |
| Additional metrics | Not supported       | Supported                   |

<br />

## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Type</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner App Access Token</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>start</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>start time of the query</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{START}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Long</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Epoch (If both start and end are not provided, default time corresponding to the last 30 days is populated in-code)</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>end</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>end time of the query</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{END}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Long</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Epoch (If both start and end are not provided, default time corresponding to the last 30 days is populated in-code)</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>granularity</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>granularity of template analytics</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{GRANULARITY}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>DAILY or AGGREGATED<br>Optional, if not provided, AGGREGATED is taken</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>metric_types</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>comma-separated string for metrics to fetch template analytics</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{METRIC_TYPES}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <p>COST

CLICKED

DELIVERED

READ

SENT

APP_ACTIVATIONS (MM Lite only)

APP_ADD_TO_CART (MM Lite only)

APP_CHECKOUTS_INITIATED (MM Lite only)

APP_PURCHASES (MM Lite only)

APP_PURCHASES_CONVERSION_VALUE (MM Lite only)

WEBSITE_ADD_TO_CART (MM Lite only)

WEBSITE_CHECKOUTS_INITIATED (MM Lite only)

WEBSITE_PURCHASES (MM Lite only)

WEBSITE_PURCHASES_CONVERSION_VALUE (MM Lite only)</p>
    <p>Optional, if not provided, all the above-mentioned metrics are considered</p>
  </td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template_ids</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>comma-separated string for gs template ids</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{TEMPLATE_IDS}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Currently supports only 1 template at a time</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>product_type</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <p>The product type of the metrics you want to retrieve. If omitted, only analytics for Cloud API will be returned.</p>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CLOUD_API, MARKETING_MESSAGES_LITE_API</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Enum</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Accepted values are: CLOUD_API, MARKETING_MESSAGES_LITE_API</p></td>
</tr>

<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>limit</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>no. of permitted entries in response per page; submitted during Meta call</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{LIMIT}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <p>Optional, if not provided, default is set to 30</p>
    <p>Currently, the limit is supported up to 30</p>
    <p>Impacts response only if granularity is DAILY</p>
  </td>
  </tr>
  <tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>use_waba_timezone</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional.

Whether to show metrics in the WABA’s configured timezone. If false or omitted, metrics will be shown in UTC.

If true, params start and end must be in the format YYYY-MM-DD.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{USE_WABA_TIMEZONE}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p></td>
 
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId of the app to enable template analytics</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid appId</p></td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request GET '{{BASE_URL}}/partner/app/{{APP_ID}}/template/analytics?start=1711935412&end=1712021812&granularity=DAILY&metric_types=SENT,DELIVERED,READ,CLICKED&template_ids={{TEMPLATE_ID}}&limit=30&product_type=MARKETING_MESSAGES_LITE_API' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
    "product_type": "MARKETING_MESSAGES_LITE_API",
    "status": "success",
    "template_analytics": [
        {
            "clicked": [
                {
                    "button_content": "Shop Now",
                    "count": 1,
                    "type": "unique_url_button"
                },
                {
                    "button_content": "Website",
                    "count": 1,
                    "type": "unique_url_button"
                },
                {
                    "button_content": "Shop Now",
                    "count": 1,
                    "type": "url_button"
                },
                {
                    "button_content": "Website",
                    "count": 1,
                    "type": "url_button"
                }
            ],
            "delivered": 3,
            "end": 1764633600,
            "read": 0,
            "sent": 3,
            "start": 1764547200,
            "template_id": "fb3ccce2-62a8-43b5-abff-824c33d160ec"
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Comments                                                                                                                                                                                                      |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                               |
| 200         | `{       "status": "success",       "template_analytics": \[           {               "clicked": [                   {                       "button_content": "imgurl1",                       "count": 8,                       "type": "url_button"                   },                   {                       "button_content": "imgurl2",                       "count": 6,                       "type": "url_button"                   }               ],               "delivered": 2,               "end": 1706572800,               "read": 1,               "sent": 2,               "start": 1706400000,               "template_id": "2c679517-6450-4556-abff-a64d1355ee7e"           }       ]   }` | Successful response                                                                                                                                                                                           |
| 200         | `{       "status": "success",       "template_analytics": \[]   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | When Meta’s API returns no data_points (this is found to occur when template has no buttons, or template is authentication type, and button clicks are disabled and we query for only CLICKED as metric type) |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                               |
| 401         | `{       "status": "error",       "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Bad request                                                                                                                                                                                                   |
| 400         | `{       "message": "Start time can't be older than 90 days",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                               |
| 404         | `{       "message": "Template Analytics settings for app f3bf7a6b-d694-412e-a5dd-6925c8bb2d15 does not exist",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                               |
