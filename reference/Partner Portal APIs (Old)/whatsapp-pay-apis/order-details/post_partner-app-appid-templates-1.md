---
title: Create Order details template
excerpt: Use this API to create an order details template.
api:
  file: partner-whatsapp-pay-apis.json
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
  <th style="border: 1px solid #ddd; padding: 8px;">Data Types</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Require/Optional</th>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Should be a valid Partner App Access Token</li>
</ul>
</td>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>The ID should be a valid app Id of Gupshup.  - The App must be associated with the account that owns the <code>PARTNER_APP_TOKEN</code> being used</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>elementName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The name of a template. Element name is unique for a WABAs namespace.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Language code for the template. Refer to all the language codes <a href="https://support.gupshup.io/hc/en-us/articles/360013321939-Which-languages-are-supported-for-message-templates">here</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{LANGUAGE_CODE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>languageCode default value: <code>en_US</code></p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>Category Type:</strong><br>Must always be <code>UTILITY</code></p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>TEXT/IMAGE</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{TEMPLATE_TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Must be TEXT or IMAGE</li>
<li>If IMAGE, header, and exampleHeader should not be passed.</li>
<li>If TEXT, mediaId should not be passed</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>example</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Template Example</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{EXAMPLE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>for params used in the header</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>header</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The header of the template.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{HEADER}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template header is compulsory for text template</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>footer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The footer of the template.  Character limit: 60.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>exampleHeader</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This is the header</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {{EXAMPLE_HEADER}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template header is compulsory for text template</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>sendAsOrderDetails</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Order Details creation param</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{SEND_AS_ORDER_DETAIL}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>It needs to be true to create Order Details templates</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mediaId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Template image</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{MEDIAID}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>If the template type is IMAGE, then mediaID is required.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'token: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'content={{CONTENT}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'vertical={{VERTICAL}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'example={{EXAMPLE}}' \
--data-urlencode 'exampleHeader={{EXAMPLE_HEADER}}' \
--data-urlencode 'header={{HEADER}}' \
--data-urlencode 'footer={{FOOTER}}' \
--data-urlencode 'sendAsOrderDetails={{SEND_AS_ORDER_DETAIL}}' \
--data-urlencode 'mediaId={{MEDIAID}}'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "ceb2b861-24f6-406c-901f-3f788e02f5ea",
        "category": "UTILITY",
        "containerMeta": "{\"appId\":\"ceb2b861-24f6-406c-901f-3f788e02f5ea\",\"data\":\"Please {{1}} Check your order status\",\"buttons\":[{\"type\":\"ORDER_DETAILS\",\"text\":\"Review and Pay\"}],\"sampleText\":\"Please Rahul Check your order status\",\"enableSample\":true,\"mediaId\":\"00a680ed-e0d1-48a4-8096-431e9d91413b\",\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false}",
        "createdOn": 1708397804112,
        "data": "Please {{1}} Check your order status | [Review and Pay]",
        "elementName": "dev_test_order_details_09",
        "id": "681bf504-c194-4af7-a9c5-29b7458a7f67",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Please Rahul Check your order status\",\"mediaId\":\"00a680ed-e0d1-48a4-8096-431e9d91413b\"}",
        "modifiedOn": 1708397804112,
        "namespace": "6a54628a_7f29_45a7_80b1_46549f39062d",
        "priority": 2,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "IMAGE",
        "vertical": "order_details",
        "wabaId": "103775135696983"
    }
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Comments                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------ |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                       |
| 200         | `{       "status": "success",       "template": {           "appId": "ceb2b861-24f6-406c-901f-3f788e02f5ea",           "category": "UTILITY",           "containerMeta": "{\"appId\":\"ceb2b861-24f6-406c-901f-3f788e02f5ea\",\"data\":\"Please {{1}} Check your order status\",\"buttons\":[{\"type\":\"ORDER_DETAILS\",\"text\":\"Review and Pay\"}],\"sampleText\":\"Please Rahul Check your order status\",\"enableSample\":true,\"mediaId\":\"00a680ed-e0d1-48a4-8096-431e9d91413b\",\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false}",           "createdOn": 1708397804112,           "data": "Please {{1}} Check your order status \| [Review and Pay]",           "elementName": "dev_test_order_details_09",           "id": "681bf504-c194-4af7-a9c5-29b7458a7f67",           "languageCode": "en",           "languagePolicy": "deterministic",           "meta": "{\"example\":\"Please Rahul Check your order status\",\"mediaId\":\"00a680ed-e0d1-48a4-8096-431e9d91413b\"}",           "modifiedOn": 1708397804112,           "namespace": "6a54628a_7f29_45a7_80b1_46549f39062d",           "priority": 2,           "quality": "UNKNOWN",           "retry": 0,           "stage": "NONE",           "status": "PENDING",           "templateType": "IMAGE",           "vertical": "order_details",           "wabaId": "103775135696983"       }   }` |                                       |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                       |
| 400         | `{       "message": "A header is required for order details templates",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | no header                             |
| 400         | `{       "message": "Category should be UTILITY for order details templates",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | incorrect category                    |
| 400         | `{       "message": "Order Details is supported only text and image",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | if template type is not text or image |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 10 Requests per Minute                |