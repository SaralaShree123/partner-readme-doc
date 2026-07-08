---
title: Limited Time Offer (LTO)
excerpt: Use this API to create a LTO template.
api:
  file: lto-template-text-type.json
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CAROUSEL</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{TEMPLATE_TYPE}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of template: CAROUSEL  </p>
<p> Cards only to be passed if template type is CAROUSEL</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>buttons</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>buttons list</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>[{&quot;type&quot;:&quot;COPY_CODE&quot;,&quot;example&quot;:&quot;250FF&quot;},{&quot;type&quot;:&quot;URL&quot;,&quot;text&quot;:&quot;Shop Now&quot;,&quot;url&quot;:&quot;&lt;https://www.luckyshrub.com/shop?promo={{1}}&quot;,&quot;example&quot;:[&quot;summer2023&quot;]},{&quot;type&quot;:&quot;URL&quot;,&quot;text&quot;:&quot;Website&quot;,&quot;url&quot;:&quot;https://www.luckyshrub.com/shop?promo={{1}}&quot;,&quot;example&quot;:[&quot;summer2023&quot;]},{&quot;type&quot;:&quot;PHONE_NUMBER&quot;,&quot;text&quot;:&quot;Call&quot;,&quot;phone_number&quot;:&quot;918016337728&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;Yes&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;No&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;Unsubscribe&gt; from Promos&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;Red&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;Blue&quot;},{&quot;type&quot;:&quot;QUICK_REPLY&quot;,&quot;text&quot;:&quot;Green&quot;}]</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hasExpiration</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Set true to add expiration to LTO templates</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{HAS_EXPIRATION}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Copy code button component required if &quot;has_expiration&quot; is set to true.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isLTO</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>LTO creation param</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{ISLTO}}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Needs to be true to create LTO templates</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>limitedOfferText</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>LTO creation param</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{LIMITED_OFFER_TEXT}}</p>
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
curl --request POST \
     --url https://partner.gupshup.io/partner/app/{{APP_ID}}/templates \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --header 'Authorization: sk_8eb35b1f81c24af293a405164a392f30' \
     --data hasExpiration=true \
     --data isLTO=true \
     --data elementName=lto_temp_1 \
     --data languageCode=en \
     --data 'content=Hi All, Here are our products.' \
     --data category=MARKETING \
     --data vertical=aaa \
     --data templateType=TEXT \
     --data 'example=Hi All, Here are our products.' \
     --data allowTemplateCategoryChange=false \
     --data enableSample=false \
     --data 'buttons=[{"type":"COPY_CODE","example":"250FF"},{"type":"URL","text":"Shop Now","url":"https://www.luckyshrub.com/shop?promo={{1}}","example":["summer2023"]},{"type":"URL","text":"Website","url":"https://www.luckyshrub.com/shop?promo={{1}}","example":["summer2023"]},{"type":"PHONE_NUMBER","text":"Call","phone_number":"918016337728"},{"type":"QUICK_REPLY","text":"Yes"},{"type":"QUICK_REPLY","text":"No"},{"type":"QUICK_REPLY","text":"Unsubscribe from Promos"},{"type":"QUICK_REPLY","text":"Red"},{"type":"QUICK_REPLY","text":"Blue"},{"type":"QUICK_REPLY","text":"Green"}]' \
     --data 'limitedOfferText=offer limited'
```

## Sample Response

```json
{
  "status": "success",
  "template": {
    "appId": "07c7c72d-xxxx-xxxx-xxxx-14d1186eeec8",
    "buttonSupported": "CC,PN,QR,URL",
    "category": "MARKETING",
    "containerMeta": "{\"appId\":\"07c7c72d-xxxx-xxxx-xxxx-14d1186eeec8\",\"data\":\"Hi All, Here are our products.\",\"buttons\":[{\"type\":\"COPY_CODE\",\"example\":\"250FF\"},{\"type\":\"URL\",\"text\":\"Shop Now\",\"url\":\"https://www.luckyshrub.com/shop?promo={{1}}\",\"example\":[\"summer2023\"]},{\"type\":\"URL\",\"text\":\"Website\",\"url\":\"https://www.luckyshrub.com/shop?promo={{1}}\",\"example\":[\"summer2023\"]},{\"type\":\"PHONE_NUMBER\",\"text\":\"Call\",\"phone_number\":\"918016337728\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Yes\"},{\"type\":\"QUICK_REPLY\",\"text\":\"No\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Unsubscribe from Promos\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Red\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Blue\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Green\"}],\"sampleText\":\"Hi All, Here are our products.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"limitedTimeOffer\":{\"text\":\"offer limited\",\"has_expiration\":true}}",
    "createdOn": 1720520894377,
    "data": "Hi All, Here are our products.\noffer limited | true | [Copy offer code,{{1}}] | [Shop Now,https://www.luckyshrub.com/shop?promo={{1}}] | [Website,https://www.luckyshrub.com/shop?promo={{1}}] | [Call,918016337728] | [Yes] | [No] | [Unsubscribe from Promos] | [Red] | [Blue] | [Green]",
    "elementName": "lto_temp_2",
    "id": "fe6be44e-11f1-4c31-8ea3-08c06b51ded9",
    "languageCode": "en",
    "languagePolicy": "deterministic",
    "meta": "{\"example\":\"Hi All, Here are our products.\"}",
    "modifiedOn": 1720520894377,
    "namespace": "5ff5f84e_789b_44df_80dd_6844d48a6a4a",
    "priority": 1,
    "quality": "UNKNOWN",
    "retry": 0,
    "stage": "NONE",
    "status": "PENDING",
    "templateType": "TEXT",
    "vertical": "aaa",
    "wabaId": "116676371511027"
  }
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Comment                |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                        |
| 200         | `{     "status": "success",     "template": {       "appId": "07c7c72d-20e3-4ff9-a5a1-14d1186eeec8",       "buttonSupported": "CC,PN,QR,URL",       "category": "MARKETING",       "containerMeta": "{\"appId\":\"07c7c72d-20e3-4ff9-a5a1-14d1186eeec8\",\"data\":\"Hi All, Here are our products.\",\"buttons\":\[{\"type\":\"COPY_CODE\",\"example\":\"250FF\"},{\"type\":\"URL\",\"text\":\"Shop Now\",\"url\":\"<https://www.luckyshrub.com/shop?promo={{1}}\",\"example\":[\"summer2023\"]},{\"type\":\"URL\",\"text\":\"Website\",\"url\":\"https://www.luckyshrub.com/shop?promo={{1}}\",\"example\":[\"summer2023\"]},{\"type\":\"PHONE_NUMBER\",\"text\":\"Call\",\"phone_number\":\"918016337728\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Yes\"},{\"type\":\"QUICK_REPLY\",\"text\":\"No\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Unsubscribe> from Promos\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Red\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Blue\"},{\"type\":\"QUICK_REPLY\",\"text\":\"Green\"}],\"sampleText\":\"Hi All, Here are our products.\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"limitedTimeOffer\":{\"text\":\"offer limited\",\"has_expiration\":true}}",       "createdOn": 1720520894377,       "data": "Hi All, Here are our products.\\noffer limited \| true \| [Copy offer code,{{1}}] \| [Shop Now,https://www.luckyshrub.com/shop?promo={{1}}] \| [Website,https://www.luckyshrub.com/shop?promo={{1}}] \| [Call,918016337728] \| [Yes] \| [No] \| [Unsubscribe from Promos] \| [Red] \| [Blue] \| [Green]",       "elementName": "lto_temp_2",       "id": "fe6be44e-11f1-4c31-8ea3-08c06b51ded9",       "languageCode": "en",       "languagePolicy": "deterministic",       "meta": "{\"example\":\"Hi All, Here are our products.\"}",       "modifiedOn": 1720520894377,       "namespace": "5ff5f84e_789b_44df_80dd_6844d48a6a4a",       "priority": 1,       "quality": "UNKNOWN",       "retry": 0,       "stage": "NONE",       "status": "PENDING",       "templateType": "TEXT",       "vertical": "aaa",       "wabaId": "116676371511027"     }   }` |                        |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 10 Requests per Minute |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | For any Internal Error |