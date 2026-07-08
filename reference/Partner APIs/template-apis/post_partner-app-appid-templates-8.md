---
title: 'Pix Template '
excerpt: 'This API creates Pix Templates '
api:
  file: pix_template.json
  operationId: post_partner-app-appid-templates
hidden: false
---
<Callout icon="📘" theme="info">
  If the waba is in Brazil then user has to use sendAsPixTemplate and button text would be Copy Pix code.
</Callout>

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
        The category of your template. **Possible Values**: MARKETING and UTILITY.
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
        TEXT/IMAGE
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
        `[{"type":"ORDER_DETAILS","text":"Copy Pix code"}]`
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
        sendAsPixTemplate
      </td>

      <td style={{ textAlign: "left" }}>
        true
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        parameterFormat
      </td>

      <td style={{ textAlign: "left" }}>
        POSITIONAL
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/926470c5-d617-43b3-aea4-2c2a389dc9d4/templates' \
--header 'accept: application/json, text/plain, */*' \
--header 'content-type: application/x-www-form-urlencoded' \
--header 'Authorization: sk_0b3a6cf96e8axxxxb2' \
--data-urlencode 'elementName=test_copypix_temp' \
--data-urlencode 'languageCode=en' \
--data-urlencode 'content=Please Pay to continue subscription' \
--data-urlencode 'category=MARKETING' \
--data-urlencode 'vertical=Test01' \
--data-urlencode 'templateType=TEXT' \
--data-urlencode 'example=Please Pay to continue subscription' \
--data-urlencode 'exampleHeader=Order' \
--data-urlencode 'enableSample=false' \
--data-urlencode 'parameterFormat=POSITIONAL' \
--data-urlencode 'checkerApprovalRequired=false' \
--data-urlencode 'footer=Thankyou' \
--data-urlencode 'header=Order' \
--data-urlencode 'buttons=[{"type":"ORDER_DETAILS","text":"Copy Pix code"}]' \
--data-urlencode 'sendAsPixTemplate=true'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "926470c5-d617-43b3-aea4-2c2a389dc9d4",
        "buttonSupported": "OD",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"926470c5-d617-43b3-aea4-2c2a389dc9d4\",\"data\":\"Please Pay to continue subscription\",\"buttons\":[{\"type\":\"ORDER_DETAILS\",\"text\":\"Copy Pix code\"}],\"header\":\"Order\",\"footer\":\"Thankyou\",\"sampleText\":\"Please Pay to continue subscription\",\"sampleHeader\":\"Order\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"isCPR\":false,\"cpr\":false}",
        "createdOn": 1765985415929,
        "data": "Order\nPlease Pay to continue subscription\nThankyou | [Copy Pix code]",
        "elementName": "test_copypix_temp_vini",
        "id": "c8d28b6f-0939-4260-9352-d10e76709c9f",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Please Pay to continue subscription\"}",
        "modifiedOn": 1765985415929,
        "namespace": "b01e6d56_443a_419e_9e2f_1559e7b31309",
        "parameterFormat": "POSITIONAL",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "TEXT",
        "vertical": "Test01",
        "wabaId": "914254047448183"
    }
}
```

## Status codes

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