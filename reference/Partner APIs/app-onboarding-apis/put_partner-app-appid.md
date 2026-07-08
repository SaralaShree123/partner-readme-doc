---
title: Update application from Partner Portal
excerpt: Use this API to update the WABA onboarding outside of Gupshup UI.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PARTNER_TOKEN</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JWT Token issues post Partner login</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner JWT Token.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>templateMessaging</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Toggle template messaging feature, initial default value is false.<br>If not passed the value is not updated.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>boolean</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>storageRegion</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Supported regions  </p>
<p>IN - India<br>DE - Germany<br>BR -  Brazil,<br>CH - Switzerland,<br>GB - Great Britain,<br>BH - Bahrain,<br>ZA - South Africa,<br>AE - United Arab Emirates,<br>US - USA,<br>CA - California,<br>AU - Australia,<br>ID - Indonesia,<br>JP - Japan,<br>SG - Singapore,<br>KR - South Korea</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Can only be changed before adding the WABA id.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>disableOptinPrefUrl</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Use this flag to toggle Optin Preference URL</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request PUT '{{partner_portal_base_url}}/partner/app/:appId' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'token: {{PARTNER_TOKEN}}'
--data-urlencode 'templateMessaging=<true/false>' \
--data-urlencode 'storageRegion=<BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR>' \
--data-urlencode 'disableOptinPrefUrl=<true/false>' \
```

## Sample Response

```json
{
    "app": {
        "id": "<app_id>",
        "customerId" : <customerId>,
        "customerType" : <SALES_LED,DEFAULT,PARTNER>
        "billingType" : <POSTPAID,PREPAID>
        "createdOn": <epoch_timestamp>,
        "phone" : <phone_number_with_country_code>,
        "callbackUrl": "<callback_url>", //if set
        "disableOptinPrefUrl": <true/false>,
        "federated": <true/false>,
        "live": <true/false>,
        "modifiedOn": <epoch_timestamp>,
        "name": "<APP_NAME>",
        "stopped": <true/false>,
        "templateMessaging": <true/false>,
        "type": "apicallbackpost",
        "storageRegion" : "US"
        "version": <0,1,2>
    },
    "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Comments                              |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                       |
| 200         | `{       "app": {           "id": "\<app_id>",           "customerId" : <customerId>,           "customerType" : \<SALES_LED,DEFAULT,PARTNER>           "billingType" : \<POSTPAID,PREPAID>           "createdOn": \<epoch_timestamp>,           "phone" : \<phone_number_with_country_code>,           "callbackUrl": "\<callback_url>", //if set           "disableOptinPrefUrl": \<true/false>,           "federated": \<true/false>,           "live": \<true/false>,           "modifiedOn": \<epoch_timestamp>,           "name": "\<APP_NAME>",           "stopped": \<true/false>,           "templateMessaging": \<true/false>,           "type": "apicallbackpost",           "storageRegion" : "US"           "version": \<0,1,2>       },       "status": "success"   }` |                                       |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                       |
| 400         | `{     "status": "error",     "message": "Cannot Change Region After Go live"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | trying to update region after go live |
| 400         | `{     "status": "error",     "message": "Invalid Region Passed"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Invalid region code                   |
| 400         | `{     "status": "error",     "message": "Fields to be updated not provided."   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | When no fields are passed             |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10 Requests per Second                |
| 500         | `{     "status": "error",     "message": "Unable to update      details. Please try again or      contact support."   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | For any Internal Error                |