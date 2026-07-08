---
title: Get Templates
excerpt: >-
  Using this API you can get the list of templates for a an app. You will get
  the rejection reason for templates. The response in which inside containerMeta
  there will be a field correctCategory if meta has identified the
  miscategorization for this template.
api:
  file: Get Templates.json
  operationId: get_partner-app-appid-templates
hidden: true
---
<Callout icon="📘" theme="info">
  **Note** - Starting June 1, 2024, to ensure that all templates are correctly categorized, Meta has implemented a recurring process that automatically identifies and updates the category of any marketing or utility templates that have been miscategorized, according to their guidelines.

  In this process, meta will now send two webhook events for template_category_update.

  1. The first one is the alert event which informs about the template’s current category and the correct category it belongs to.
  2. The second event (sent on the 1st of the next month after the alert event) is the actual category update event informing that the template’s category has now been updated.
</Callout>

<br />

## Request Parameters

| Key              | Description                                          | Value                | Data type | Required/Optional | Constraints                                                                                                                          |
| :--------------- | :--------------------------------------------------- | :------------------- | :-------- | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Authorization    | Access Token for the application                     | \{PARTNER_APP_TOKEN} | String    | Required          | •	Should be a valid Partner App Access Token                                                                                         |
| **Path Params**  |                                                      |                      |           |                   |                                                                                                                                      |
| appId            | App ID to fetch the access token                     | \{APP_ID}            | String    | Required          | •	The Id should be a valid app Id of Gupshup•	The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |
| **Query Params** |                                                      |                      |           |                   |                                                                                                                                      |
| templateType     | Type of template                                     | \{TEMPLATE_TYPE}     | String    | Optional          |                                                                                                                                      |
| status           | Status of template                                   | \{STATUS}            | String    | Optional          |                                                                                                                                      |
| stage            | List of stages to filter by, separated by commas     | \{STAGES}            | String    | Optional          |                                                                                                                                      |
| useable          | To filter templates which are useable ,i.e, APPROVED | \{USABLE}            | Boolean   | Optional          |                                                                                                                                      |
| startTime        | Time range start time                                | \{START_TIME}        | Long      | Optional          |                                                                                                                                      |
| endTime          | Time range end time                                  | \{END_TIME}          | Long      | Optional          |                                                                                                                                      |
| elementName      | Template element name to filter by                   | \{ELEMENT_NAME}      | String    | Optional          |                                                                                                                                      |
| data             | Template data to filter by                           | \{DATA}              | String    | Optional          |                                                                                                                                      |
| pageNo           | Page number                                          | \{PAGE_NO}           | INT       | Optional          |                                                                                                                                      |
| pageSize         | Page size                                            | \{PAGE_SIZE}         | INT       | Optional          |                                                                                                                                      |

## Sample Request

```curl
curl --location --globoff 'https:partner.gupshup.io/partner/app/{{APP_ID}}/templates?templateType={{TEMPLATE_TYPE}}&status={{STATUS}}&startTime={{START_TIME}}&endTime={{END_TIME}}&pageSize={{PAGE_SIZE}}&pageNo={{PAGE_NO}}&stage={{STATE}}&data={{DATA}}&useable={{USEABLE}}&elementName={{ELEMENT_NAME}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
    "status": "success",
    "templates": [
        {
            "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
            "category": "UTILITY",
            "containerMeta": "{\"appId\":\"bf9ee64c-3d4d-4ac4-8668-732e577007c4\",\"data\":\"This is to remind you that {{1}} is due by {{2}}.\",\"footer\":\"This is footer\",\"sampleText\":\"This is to remind you that {{1}} is due by {{2}}.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
            "createdOn": 1707743909374,
            "data": "This is to remind you that {{1}} is due by {{2}}.\nThis is footer",
            "elementName": "automation_template_2131081",
            "externalId": "1508119726419684",
            "id": "00b8d1ed-7af6-4734-a7a1-e3062f21d7df",
            "languageCode": "en",
            "languagePolicy": "deterministic",
            "meta": "{\"example\":\"This is to remind you that {{1}} is due by {{2}}.\"}",
            "modifiedOn": 1707743915378,
            "namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c",
            "priority": 2,
            "quality": "UNKNOWN",
            "reason": "Invalid Format",
            "retry": 0,
            "stage": "NONE",
            "status": "REJECTED",
            "templateType": "TEXT",
            "vertical": "Internal_vertical",
            "wabaId": "216141188246170"
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
        "status": "success","template":\{"appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4","category": "MARKETING","containerMeta": "\{"appId":"bf9ee64c-3d4d-4ac4-8668-732e577007c4","data":"This is category for copy code button template.","footer":"This is footer","sampleText":"This is category for copy code button template.","enableSample":true,"editTemplate":false,"addSecurityRecommendation":false}","createdOn": 1708205191624,"data": "This is category for copy code button template.\nThis is footer","elementName": "automation_template_2956534","id": "e8e837c2-a3a8-4845-958f-ec7febb54aec","languageCode": "en","languagePolicy": "deterministic","meta": "\{"example":"This is category for copy code button template."}","modifiedOn": 1708205191624,"namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c","priority": 1,"quality": "UNKNOWN","retry": 0,
        "stage": "NONE",
        "status": "APPROVED",
        "templateType": "TEXT",
        "vertical": "Internal_vertical",
        "wabaId": "216141188246170"
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
        429
      </td>

      <td>
        \{

        "status": "error","message": "Too Many Requests"}
      </td>

      <td>
        10 Requests per Minute
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{

        "status": "error","message": "Internal server error. Please try again later and If Issue still persist, then contact Gupshup Dev Support"}
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>