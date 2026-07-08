---
title: Partner for business verification
excerpt: Use this API for partner business verification.
api:
  file: partner-portal-api-15.json
  operationId: submitBusinessVerification
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

| Key                                        | Data Types            | Require/Optional | Description                                                                           |
| :----------------------------------------- | :-------------------- | :--------------- | :------------------------------------------------------------------------------------ |
| PARTNER_SUPPORT_TOKEN                      | Partner support token | Required         | Should be a valid support token                                                       |
| bspId                                      | Numeric BSP Id        |                  | Meta Business ID                                                                      |
| end_business_id                            | List of app IDs       | Required         | Optional. List of app IDs separated by a comma.                                       |
| partnerId                                  | Numeric partner ID    | Required         | Partner ID for the which document uploading                                           |
| business_documents                         | file type doc         | Required         | Array of file type. it support only upto 3 doc. and these must be pdf, jpg, jpeg, png |
| end_business_address                       | json                  | Optional         | End client’s business address.                                                        |
| average_monthly_revenue_spend_with_partner | json                  | Optional         | Average revenue spent per month (in local currency).                                  |
| end_business_website                       | String                | Optional         | End client’s website                                                                  |
| num_billing_cycles_with_partner            | Integer               | Optional         | Number of billing cycles that the client has paid with the BSP.                       |
| end_business_legal_name                    | String                | Optional         | End client’s legal name                                                               |

## Sample Request

```curl
curl --location 'https://partner-support.gupshup.io/partner/admin/bspsignal/{{bspId}}' \
--header 'Authorization: {{PARTNER_ADMIN_TOKEN}}' \
--header 'Content-Type: application/octet-stream' \
--form 'partner_id={{partnerId}}' \
--form 'end_business_id={{clientBusinessId}}' \
--form 'business_documents=@"filePath1"' \
--form 'business_documents=@"filePath2"' \
--form 'business_documents=@"filePath3"' \
--form 'end_business_website="https://sba.gov.ae/"' \
--form 'end_business_address="{ \"street_address_1\": \"India Gate\", \"street_address_2\": \"STREET ADDRESS 2\", \"city_or_town\": \"Delhi\", \"state_province_or_region\": \"New Delhi\", \"postal_code\": \"111001\", \"country_code\": \"IN\" }"' \
--form 'end_business_legal_name="Dubai Book Authority"' \
--form 'num_billing_cycles_with_partner="1"' \
--form 'average_monthly_revenue_spend_with_partner="{ \"amount\": \"102\", \"currency_code\": \"USD\" }"'
```

## Sample Response

```json
{
  "success": true,
  "message": "Your request has been received and will be reviewed shortly.",
  "verification_attempts": 1
}	
```

## Status Codes

| Status Code | Response                                                                                                                                   | Comments                  |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| **Success** |                                                                                                                                            |                           |
| 200         | `{ "success": true, "message": "Your request has been received and will be reviewed shortly.", "verification_attempts": 1 }` | Success                   |
| **Error**   |                                                                                                                                            |                           |
| 400         | `{ "status":"error", "message/data":"&lt;Specific to API&gt;" }`                                                                       | Error with respect to API |
| 401         | `{ "status":"error", "message":"Unauthorized Access" }`                                                                          | When authentication fails |
| 500         | `{ "status": "error", "message": "Internal Server Error" }`                                                                      | For any Internal Error    |