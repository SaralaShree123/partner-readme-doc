---
title: Get Partner for business verification Status
excerpt: Use this API to verify your business status with a partner.
api:
  file: partner-portal-api-15.json
  operationId: getBusinessVerificationStatus
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PARTNER_SUPPORT_TOKEN</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Partner support token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid support token</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>end_business_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Email ID to be used for notifications with respect to the migration</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>End client’s business ID on Meta Business Suite.  </p>
<p>If this field is not present, the API call returns all objects associated with the BSP.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bspId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Numeric BSP Id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Meta Business ID</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>



## Sample Request

```curl
curl --location 'https://partner-support.gupshup.io/partner/admin/bspsignal/{{bspId}}/whatsapp_business_submissions_status?end_business_id={{clientBusinessId}}' \
--header 'Authorization: {{PARTNER_ADMIN_TOKEN}}'
```

## Sample Response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1653884675164315,
            "client_business_id": 791808649586927,
            "rejection_reasons": [
                "LEGAL_NAME_NOT_FOUND_IN_DOCUMENTS"
            ],
            "submitted_info": {
                "end_business_legal_name": "India Gate Book Trust",
                "end_business_website": "https://www.india-gate.gov.in/",
                "num_billing_cycles_with_partner": 2,
                "end_business_address": {
                    "street_address_1": "India Gate",
                    "street_address_2": "STREET ADDRESS 2",
                    "city_or_town": "Delhi",
                    "state_province_or_region": "New Delhi",
                    "postal_code": "111001",
                    "country_code": "IN"
                },
                "average_monthly_revenue_spend_with_partner": {
                    "amount": 12,
                    "currency_code": "USD"
                }
            },
            "submitted_time": "2024-12-09T11:07:36+0000",
            "update_time": "2024-12-09T11:09:00+0000",
            "verification_status": "FAILED"
        },
        {
            "id": 1985777845258997,
            "client_business_id": 791808649586927,
            "rejection_reasons": [
                "LEGAL_NAME_NOT_FOUND_IN_DOCUMENTS"
            ],
            "submitted_info": {
                "end_business_legal_name": "India Gate Book Trust",
                "end_business_website": "https://www.india-gate.gov.in/",
                "num_billing_cycles_with_partner": 2,
                "end_business_address": {
                    "street_address_1": "India Gate",
                    "street_address_2": "STREET ADDRESS 2",
                    "city_or_town": "Delhi",
                    "state_province_or_region": "New Delhi",
                    "postal_code": "111001",
                    "country_code": "IN"
                },
                "average_monthly_revenue_spend_with_partner": {
                    "amount": 12,
                    "currency_code": "USD"
                }
            },
            "submitted_time": "2024-12-05T02:18:28+0000",
            "update_time": "2024-12-05T02:19:57+0000",
            "verification_status": "FAILED"
        }
    ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Comments                  |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                           |
| 200         | `{       "status": "success",       "data": \[           {               "id": 1653884675164315,               "client_business_id": 791808649586927,               "rejection_reasons": [                   "LEGAL_NAME_NOT_FOUND_IN_DOCUMENTS"               ],               "submitted_info": {                   "end_business_legal_name": "India Gate Book Trust",                   "end_business_website": "<https://www.india-gate.gov.in/">,                   "num_billing_cycles_with_partner": 2,                   "end_business_address": {                       "street_address_1": "India Gate",                       "street_address_2": "STREET ADDRESS 2",                       "city_or_town": "Delhi",                       "state_province_or_region": "New Delhi",                       "postal_code": "111001",                       "country_code": "IN"                   },                   "average_monthly_revenue_spend_with_partner": {                       "amount": 12,                       "currency_code": "USD"                   }               },               "submitted_time": "2024-12-09T11:07:36+0000",               "update_time": "2024-12-09T11:09:00+0000",               "verification_status": "FAILED"           },           {               "id": 1985777845258997,               "client_business_id": 791808649586927,               "rejection_reasons": [                   "LEGAL_NAME_NOT_FOUND_IN_DOCUMENTS"               ],               "submitted_info": {                   "end_business_legal_name": "India Gate Book Trust",                   "end_business_website": "<https://www.india-gate.gov.in/">,                   "num_billing_cycles_with_partner": 2,                   "end_business_address": {                       "street_address_1": "India Gate",                       "street_address_2": "STREET ADDRESS 2",                       "city_or_town": "Delhi",                       "state_province_or_region": "New Delhi",                       "postal_code": "111001",                       "country_code": "IN"                   },                   "average_monthly_revenue_spend_with_partner": {                       "amount": 12,                       "currency_code": "USD"                   }               },               "submitted_time": "2024-12-05T02:18:28+0000",               "update_time": "2024-12-05T02:19:57+0000",               "verification_status": "FAILED"           }       ]   }` | Success                   |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                           |
| 400         | `{     "status":"error",     "message/data":"<Specific to API>"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Error with respect to API |
| 401         | `{     "status":"error",     "message":"Unauthorized Access"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | When authentication fails |
| 500         | `{     "status": "error",     "message": "Internal Server Error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | For any Internal Error    |