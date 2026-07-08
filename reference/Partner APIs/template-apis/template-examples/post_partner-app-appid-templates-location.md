---
title: Location
excerpt: ''
api:
  file: location-type-template-1.json
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{CONTENT}}</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{CATEGORY}}</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{VERTICAL}}</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>LOCATION</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{TEMPLATE_TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of template: LOCATION</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>enableSample</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required for creating all types of templates</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{ENABLE_SAMPLE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true/false</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>if enableSample is true then exampleMedia</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>footer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Footer of the template. Character limit: 60.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{FOOTER}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
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
curl --request POST \
     --url https://partner.gupshup.io/partner/app/{{APP_ID}}/templates \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'Authorization: sk_711916ad1d5d4f21a9520fdef20516a1' \
     --data elementName=template_automationk1 \
     --data languageCode=en \
     --data 'content=The place for the event is kothrud,Pune' \
     --data category=UTILITY \
     --data vertical=Internal_vertical \
     --data templateType=LOCATION \
     --data 'example=The place for the event is kothrud,Pune' \
     --data allowTemplateCategoryChange=true \
     --data 'footer=This is footer' \
     --data enableSample=true
```

## Sample Response

```json
{
  "status": "success",
  "template": {
    "appId": "947d28b8-459b-4dfe-9d4c-0ac8c6c245c9",
    "category": "UTILITY",
    "containerMeta": "{\"appId\":\"947d28b8-459b-4dfe-9d4c-0ac8c6c245c9\",\"data\":\"The place for the event is kothrud,Pune\",\"footer\":\"This is footer\",\"sampleText\":\"The place for the event is kothrud,Pune\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
    "createdOn": 1720713893197,
    "data": "The place for the event is kothrud,Pune\nThis is footer",
    "elementName": "template_automationk1",
    "id": "222d0517-b1b3-49ba-8861-e36be991a7a9",
    "languageCode": "en",
    "languagePolicy": "deterministic",
    "meta": "{\"example\":\"The place for the event is kothrud,Pune\"}",
    "modifiedOn": 1720713893197,
    "namespace": "8e58971e_b9b8_476c_b844_64a1aa63a73c",
    "priority": 2,
    "quality": "UNKNOWN",
    "retry": 0,
    "stage": "NONE",
    "status": "PENDING",
    "templateType": "LOCATION",
    "vertical": "Internal_vertical",
    "wabaId": "117529881248706"
  }
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Comment                |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                        |
| 200         | `{     "status": "success",     "template": {       "appId": "947d28b8-459b-4dfe-9d4c-0ac8c6c245c9",       "category": "UTILITY",       "containerMeta": "{\"appId\":\"947d28b8-459b-4dfe-9d4c-0ac8c6c245c9\",\"data\":\"The place for the event is kothrud,Pune\",\"footer\":\"This is footer\",\"sampleText\":\"The place for the event is kothrud,Pune\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",       "createdOn": 1720713893197,       "data": "The place for the event is kothrud,Pune\\nThis is footer",       "elementName": "template_automationk1",       "id": "222d0517-b1b3-49ba-8861-e36be991a7a9",       "languageCode": "en",       "languagePolicy": "deterministic",       "meta": "{\"example\":\"The place for the event is kothrud,Pune\"}",       "modifiedOn": 1720713893197,       "namespace": "8e58971e_b9b8_476c_b844_64a1aa63a73c",       "priority": 2,       "quality": "UNKNOWN",       "retry": 0,       "stage": "NONE",       "status": "PENDING",       "templateType": "LOCATION",       "vertical": "Internal_vertical",       "wabaId": "117529881248706"     }   }` |                        |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | For any Internal Error |