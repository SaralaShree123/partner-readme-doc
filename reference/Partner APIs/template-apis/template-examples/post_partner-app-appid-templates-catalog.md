---
title: Catalog
excerpt: ''
api:
  file: catalog-type-template-1.json
  operationId: post_partner-app-appid-templates
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
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Data Type</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional </th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner App Access Token</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>elementName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The name of a template. The element name is unique for a WABAs namespace.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{ELEMENT_NAME}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>elementName (not more than 180 char.) Mandatory fields</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>languageCode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Language code for the template. Refer to all the language codes <a href="https://support.gupshup.io/hc/en-us/articles/360013321939">here</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{LANGUAGE_CODE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>languageCode default value : <code>en_US</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>content</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The body of the template.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{CONTENT}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>content (not more than 1024 char.)</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>category</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The category of your template.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{CATEGORY}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Category Type: MARKETING UTILITY</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vertical</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>TEXT</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{VERTICAL}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vertical (not more than 180 char.)</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>templateType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CATALOG</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{TEMPLATE_TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of template: CATALOG</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>example</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Template Example</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{EXAMPLE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>allowTemplateCategoryChange</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean value. If True, Meta will automatically update the template category as per the template content. The default value is False.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{ALLOW_TEMPLATE_CATEGORY_CHANGE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true/false</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App ID to fetch the access token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The Id should be a valid app Id of Gupshup  </p>
<p>The App must be associated with the account that owns the PARTNER_APP_TOKEN being used</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'content={{CONTENT}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'vertical={{VERTICAL}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'example={{EXAMPLE}}' \
--data-urlencode 'allowTemplateCategoryChange={{ALLOW_TEMPLATE_CATEGORY_CHANGE}}'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
        "buttonSupported": "CLG",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Dear BatMan, here are our products.\",\"buttons\":[{\"type\":\"CATALOG\",\"text\":\"View catalog\"}],\"sampleText\":\"Dear BatMan, here are our products.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
        "createdOn": 1710799900239,
        "data": "Dear BatMan, here are our products. | [View catalog]",
        "elementName": "automation_template_503642",
        "id": "09c335c2-f9a5-44b7-b544-2e4be761840b",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Dear BatMan, here are our products.\"}",
        "modifiedOn": 1710799900239,
        "namespace": "9c7fe92f_2a48_40ec_83d0_69c62a772433",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "CATALOG",
        "vertical": "Internal_vertical",
        "wabaId": "104505526065633"
    }
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Comment                |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                        |
| 200         | \{       "status": "success",       "template": \{"appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",           "buttonSupported": "CLG",           "category": "MARKETING",           "containerMeta": "\{"appId":"a41b30f4-d202-4fdb-911e-3a8fbfbfb797","data":"Dear BatMan Here are our products.\",\"buttons\":[\{\"type\":\"CATALOG\",\"text\":\"View catalog\"}],\"sampleText\":\"Dear BatMan\\\\nHere are our products.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",           "createdOn": 1715598979361,           "data": "Dear BatMan\\nHere are our products. \| [View catalog]",           "elementName": "auto_cattemplate",           "id": "a4a77e59-f305-4964-bfad-5dcb0a7d1aa9",           "languageCode": "en",           "languagePolicy": "deterministic",           "meta": "\{\"example\":\"Dear BatMan\\\\nHere are our products.\"}",           "modifiedOn": 1715598979361,           "namespace": "9c7fe92f_2a48_40ec_83d0_69c62a772433",           "priority": 1,           "quality": "UNKNOWN",           "retry": 0,           "stage": "NONE",           "status": "PENDING",           "templateType": "CATALOG",           "vertical": "Internal_vertical",           "wabaId": "104505526065633"       }   } |                        |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | For any Internal Error |