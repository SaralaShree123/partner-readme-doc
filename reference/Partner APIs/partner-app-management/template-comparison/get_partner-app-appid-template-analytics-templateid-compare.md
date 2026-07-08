---
title: Template Comparison API
excerpt: >-
  Use this API to compare templates. This endpoint allows you to analyze and
  compare the performance of multiple WhatsApp message templates side by side,
  providing insights into metrics like block rate, message sends, and block
  reasons.
api:
  file: partner-release-85-apis.json
  operationId: get_partner-app-appid-template-analytics-templateid-compare
deprecated: false
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
> 1. The API needs at least **1,000 messages** sent per template in the given time frame to work
> 2. The difference between the start and end timestamps must be **exactly** 604800 (7 days), 2592000 (30 days), 5184000 (60 days), or 7776000 (90 days) seconds.
> 3. All templates must be in **approved** status.
> 4. You must be the **owner** of all templates being compared.
> 5. Rate limit: **10 requests per hour** (3600 seconds).
> 6. **Common Use Cases:**   
>    * A/B testing to determine which template variant performs better. 
>    * Template optimization to identify templates needing improvement.
>    *  Quality monitoring to track template quality over time. 
>    * Campaign planning to choose best-performing templates

## Request Parameters

| Key             | Description                                                      | Constraints                                             |
| :-------------- | :--------------------------------------------------------------- | :------------------------------------------------------ |
| Authorization   | Access Token for the application                                 | Should be a valid Partner App Access Token              |
| appId           | AppId of the app for which the embed link needs to be generated. | Should be a valid appId associated with the account.    |
| gsTemplateId Id | ID of the WhatsApp Message Template to target.                   | Should be a valid template ID                           |
| template_ids    | Array of template Ids to compare.                                | The array should contain exactly one valid template id. |
| start_timestamp | Start time                                                       | start time is in **seconds** in long form               |
| end_timestamp   | End time                                                         | end time is in **seconds** in long form                 |

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/3c7a7716-e731-45db-9478-f93fb011af7d/template/analytics/88dcc6a4-deb7-4785-9ce5-f8c6fa09b745/compare?templateList=c0222c17-7d49-49c6-ab1c-f0be0796fb77&end=1717113600&start=1709337600' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
    "data": [
        {
            "metric": "BLOCK_RATE",
            "order_by_relative_metric": [ {{list_of_gs_templateId}} ],
            "type": "RELATIVE"
        },
        {
            "metric": "MESSAGE_SENDS",
            "number_values": [
                {
                    "key": "{{gs_template_id_1}}",
                    "value": {{Number_of_messages_sent}}
                },
                {
                    "key": "{{gs_template_id_2}}",
                    "value": {{Number_of_messages_sent}}
                }
            ],
            "type": "NUMBER_VALUES"
        },
        {
            "metric": "TOP_BLOCK_REASON",
            "string_values": [
                {
                    "key": "{{gs_template_id}}",
                    "value": "{{block_reason}}"
                },
                {
                    "key": "{{gs_template_id}}",
                    "value": "{{block_reason}}"
                }
            ],
            "type": "STRING_VALUES"
        }
    ],
    "status": "success"
}
```

## Status Code

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Comment                                                                                                     |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                             |
| 200         | `{       "data": \[           {               "metric": "BLOCK_RATE",               "order_by_relative_metric": [ {{list_of_gs_templateId}} ],               "type": "RELATIVE"           },           {               "metric": "MESSAGE_SENDS",               "number_values": [                   {                       "key": "{{gs_template_id_1}}",                       "value": {{Number_of_messages_sent}}                   },                   {                       "key": "{{gs_template_id_2}}",                       "value": {{Number_of_messages_sent}}                   }               ],               "type": "NUMBER_VALUES"           },           {               "metric": "TOP_BLOCK_REASON",               "string_values": [                   {                       "key": "{{gs_template_id}}",                       "value": "{{block_reason}}"                   },                   {                       "key": "{{gs_template_id}}",                       "value": "{{block_reason}}"                   }               ],               "type": "STRING_VALUES"           }       ],       "status": "success"   }` | The speed_processed may not be the same as the one sent in the request as it depends on the payment gateway |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                             |
| 400         | `{           "status": "error",           "message": "Authentication Failed"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                             |
| 400         | `{       "status": "error",       "message": "Invalid parameter - Templates not eligible for comparison, Templates must have been sent at least 1,000 times in the specified time frame."   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                             |
| 400         | `{     "status": "error",     "message": "(#100) The parameter template_ids is required. - null, null" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                             |
| 400         | `{       "message": "The difference between start and end times should be the number of seconds in 604800(7 days), 2592000(30 days), 5184000(60 days), 7776000(90 days).",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                             |
| 400         | `{       "message": "One or more templates in the list is not approved.",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                             |
| 400         | `{       "message": "The parameter start_timestamp should be less than end_timestamp.",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                             |
| 400         | `{ "message": "Not Template Owner", "status": "error" }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                             |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | When request rate limit exceeds.                                                                            |
