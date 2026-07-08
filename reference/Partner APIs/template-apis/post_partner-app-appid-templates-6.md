---
title: Apply For Templates
excerpt: Using this API, you can Create a template for a particular app
api:
  file: 2Apply For Templates.json
  operationId: post_partner-app-appid-templates
hidden: true
---
<Callout icon="📘" theme="info">
  Apply for template now supports named parameter syntax in headers and body components.
</Callout>

<br />

## Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        \{PARTNER_APP_TOKEN}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        •	Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        \{APP_ID}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        •	The Id should be a valid app Id of Gupshup•	The App must be associated with the account that owns the PARTNER_APP_TOKEN being used
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        elementName
      </td>

      <td style={{ textAlign: "left" }}>
        The name of a template. Element name is unique for a WABAs namespace.
      </td>

      <td style={{ textAlign: "left" }}>
        \{ELEMENT_NAME}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        •	elementName (not more than 200 char.) Mandatory fields
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        languageCode
      </td>

      <td style={{ textAlign: "left" }}>
        Language code for the template. Refer to all the language codes

        [here](https://support.gupshup.io/hc/en-us/articles/360013321939)

        .
      </td>

      <td style={{ textAlign: "left" }}>
        \{LANGUAGE_CODE}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        optional
      </td>

      <td style={{ textAlign: "left" }}>
        •	languageCode default value : en_US
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        content
      </td>

      <td style={{ textAlign: "left" }}>
        The body of the template. Character limit: 1028. For "Authentication" category the first line should be - \{\{1}} is your verification code.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        •	content (not more than 1024 char.)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        category
      </td>

      <td style={{ textAlign: "left" }}>
        The category of your template. **Possible Values**: AUTHENTICATION, MARKETING and UTILITY.
        If you submit the templates with the any other categories, you will receive an error Invalid category provided, kindly use category from these option AUTHENTICATION, MARKETING, UTILITY.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        •	category (not more than 180 char.)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        vertical
      </td>

      <td style={{ textAlign: "left" }}>
        TEXT
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        vertical (not more than 180 char.)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        templateType
      </td>

      <td style={{ textAlign: "left" }}>
        **TEXT**

        Carousel--data-urlencode 'cards'**LTO**--data-urlencode 'limitedOfferText=
        \{limited offer text}'
        --data-urlencode 'hasExpiration=
        \{true/false}'
        --data-urlencode 'isLTO=true
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        The type of template: TEXT, IMAGE, LOCATION, PRODUCT, CATALOG, LTO, CAROUSEL, VIDEO & DOCUMENTCATALOG, LTO, CAROUSEL templates are not available with the On-premises API

        CATALOG, LTO, CAROUSEL and PRODUCT templates are available for MARKETING & UTILITY category only.Cards to be cards only to be passed if template type is CAROUSEL
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        example
      </td>

      <td style={{ textAlign: "left" }}>
        Template Example
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        enableSample
      </td>

      <td style={{ textAlign: "left" }}>
        Required for creating all types of templates
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        true/false
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        if enableSample is true then exampleMedia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        header
      </td>

      <td style={{ textAlign: "left" }}>
        Header of the template. Applicable for templateType = Text Character limit: 60. Not applicable for "Authentication" category.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        footer
      </td>

      <td style={{ textAlign: "left" }}>
        Footer of the template. Character limit: 60. Not applicable for "Authentication" category, only set based on code_expiration_minutes value
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        buttons
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Array of objects
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        exampleHeader
      </td>

      <td style={{ textAlign: "left" }}>
        This is the header
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        addSecurityRecommendation
      </td>

      <td style={{ textAlign: "left" }}>
        Optionally for "Authentication" category a security disclaimer is added to content - For your security, do not share this code
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>
        true
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        codeExpirationMinutes
      </td>

      <td style={{ textAlign: "left" }}>
        Optionally for "Authentication" category the following text is added to footer - This code expires in \<NUM_MINUTES> minutes. Code expiry time should be between 1 and 90 minutes.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        messageValidity
      </td>

      <td style={{ textAlign: "left" }}>
        If we are unable to deliver a message to a WhatsApp user, we will retry the delivery for a period of time known as a time-to-live, TTL, or the message validity period.
      </td>

      <td style={{ textAlign: "left" }}>
        Valid messageValidity property values
        **Authentication templates**: 30 to 900 seconds (30 secs to 15 mins).
        **Utility templates**: 30 to 43200 seconds (30 secs to 12 hours).
        **Marketing templates**: 43200 to 2592000 (12 hours to 30 days)
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        NA
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        isCPR
      </td>

      <td style={{ textAlign: "left" }}>
        To enable or disable CPR (Call permission request)
      </td>

      <td style={{ textAlign: "left" }}>
        true/false
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        parameterFormat
      </td>

      <td style={{ textAlign: "left" }}>
        `Header component : 
                                Already supports positional ({{1}}) → Now supports named ({{sale_start_date}}).`

        `Body component:  
                                Already supports multiple positional params ({{1}}, {{2}}) → Now supports named ({{order_id}}, {{customer_name}}).`
      </td>

      <td style={{ textAlign: "left" }}>
        NAMED/POSITIONAL  
        Default will be positional
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 NOTE:
>
> * marketing ttl is only available on MM lite, and not available on CAPI.

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'vertical=TEXT' \
--data-urlencode 'content=your ticket has been confirmed for {{customer_name}} persons on date.' \
--data-urlencode 'header=This is the header' \
--data-urlencode 'footer=This is the footer' \
--data-urlencode 'buttons=[{"type":"PHONE_NUMBER","text":"Call Us","phone_number":"+919872329959"},{"type":"URL","text":"Book A Demo","url":"https://bookins.gupshup.io/{{1}}","example":["https://bookins.gupshup.io/abc"]}] or for “Authentication” category: [{"type":"OTP","otp_type":"COPY_CODE","text":"Copy OTP"},{"type":"OTP", “otp-type”: “ONE_TAP”, "text":"Book A Demo", "autofill_text": "Autofill", #One-tap buttons only "package_name": "com.example.myapplication" #One-tap buttons only , "signature_hash": "K8a%2FAINcGX7", #One-tap buttons only }]' \
--data-urlencode 'example=your ticket has been confirmed for 4 persons on date 2020-05-04.' \
--data-urlencode 'enableSample=true' \
--data-urlencode 'messageValidity=43200' \
--data-urlencode 'isCPR=true' \
--data-urlencode 'parameterFormat=NAMED' \
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "57d9179b-7412-4621-bf86-57ee1962fd12",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"57d9179b-7412-4621-bf86-57ee1962fd12\",\"data\":\"Hi user, how is {{customer}} doing?\",\"footer\":\"This code expires in 15 minutes\",\"sampleText\":\"Hi user, how is jane doing?\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"isCPR\":false,\"cpr\":false}",
        "createdOn": 1767003908520,
        "data": "Hi user, how is {{customer}} doing?\nThis code expires in 15 minutes",
        "elementName": "test_22_decemberrr",
        "id": "5da48971-6181-4c45-8de0-c786a93328e7",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Hi user, how is jane doing?\"}",
        "modifiedOn": 1767003908520,
        "namespace": "0fee79c0_9ff8_47dc_a4e7_c07dcc23472e",
        "parameterFormat": "NAMED",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "state": "ACTIVE",
        "status": "PENDING",
        "templateType": "TEXT",
        "vertical": "aaa",
        "wabaId": "256322900902782"
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
        "status": "PENDING",
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
