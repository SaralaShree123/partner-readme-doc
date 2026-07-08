---
title: Product
excerpt: ''
api:
  file: product-type-template-1.json
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
        Data Type
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
        \{\{PARTNER\_APP\_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        elementName
      </td>

      <td style={{ textAlign: "left" }}>
        The name of a template. The element name is unique for a WABAs namespace.
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ELEMENT\_NAME}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        elementName (not more than 180 char.) Mandatory fields
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        languageCode
      </td>

      <td style={{ textAlign: "left" }}>
        Language code for the template. Refer to all the language codes [here](https://support.gupshup.io/hc/en-us/articles/360013321939).
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{LANGUAGE\_CODE}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional 
      </td>

      <td style={{ textAlign: "left" }}>
        languageCode default value : `en_US`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        content
      </td>

      <td style={{ textAlign: "left" }}>
        The body of the template.
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{CONTENT}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        content (not more than 1024 char.)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        category
      </td>

      <td style={{ textAlign: "left" }}>
        The category of your template.
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{CATEGORY}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Category Type: MARKETING UTILITY
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
         \{\{VARTICAL}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
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
        PRODUCT
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{TEMPLATE\_TYPE}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        The type of template: PRODUCT
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
         \{\{EXAMPLE}}
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

    <tr>
      <td style={{ textAlign: "left" }}>
        enableSample
      </td>

      <td style={{ textAlign: "left" }}>
        Required for creating all types of templates
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{ENABLE\_SAMPLE}}
      </td>

      <td style={{ textAlign: "left" }}>
        true/false
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
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
        Header of the template.
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{HEADER}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        footer
      </td>

      <td style={{ textAlign: "left" }}>
        Footer of the template. Character limit: 60.
      </td>

      <td style={{ textAlign: "left" }}>
         \{\{FOOTER}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
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
        \{\{ENABLE\_HEADER}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        allowTemplateCategoryChange
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean value. If True, Meta will automatically update the template category as per the template content. The default value is False.
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ALLOW\_TEMPLATE\_CATEGORY\_CHANGE}}
      </td>

      <td style={{ textAlign: "left" }}>
        true/false
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>

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
        \{\{APP\_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        The Id should be a valid app Id of Gupshup  

        The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName=automation_template_439231' \
--data-urlencode 'languageCode=en' \
--data-urlencode 'content=Dear Customer, Here are our products. \nThanks for shopping with us' \
--data-urlencode 'category=MARKETING' \
--data-urlencode 'vertical=Internal_vertical' \
--data-urlencode 'templateType=PRODUCT' \
--data-urlencode 'example=Dear Customer, Here are our products. \nThanks for shopping with us' \
--data-urlencode 'allowTemplateCategoryChange=true' \
--data-urlencode 'enableSample=false' \
--data-urlencode 'exampleHeader=Hi All' \
--data-urlencode 'header=Hi All' \
--data-urlencode 'footer=This is footer'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
        "buttonSupported": "MPM",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\",\"buttons\":[{\"type\":\"MPM\",\"text\":\"View items\"}],\"header\":\"Hi All\",\"footer\":\"This is footer\",\"sampleText\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\",\"sampleHeader\":\"Hi All\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
        "createdOn": 1710799689011,
        "data": "Hi All\nDear Customer, Here are our products. \\nThanks for shopping with us\nThis is footer | [View items]",
        "elementName": "automation_template_439231",
        "id": "1f7871fc-2933-41dd-8f67-ab2a75f055fa",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\"}",
        "modifiedOn": 1710799689011,
        "namespace": "9c7fe92f_2a48_40ec_83d0_69c62a772433",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "PRODUCT",
        "vertical": "Internal_vertical",
        "wabaId": "104505526065633"
    }
}
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Status Code
      </th>

      <th style={{ textAlign: "left" }}>
        Response
      </th>

      <th style={{ textAlign: "left" }}>
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **Success**
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        200
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
           "status":"success",\
           "template":\{\
              "appId":"a41b30f4-d202-4fdb-911e-3a8fbfbfb797",\
              "buttonSupported":"MPM",\
              "category":"MARKETING",\
              "containerMeta":`"\{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\",\"buttons\":[\{\"type\":\"MPM\",\"text\":\"View items\"}][{\\"type\\":\\"MPM\\",\\"text\\":\\"View items\\"}],\"header\":\"Hi All\",\"footer\":\"This is footer\",\"sampleText\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\",\"sampleHeader\":\"Hi All\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",\`
              "createdOn":1710799689011,\
              "data":"Hi All\\nDear Customer, Here are our products. \\nThanks for shopping with us\\nThis is footer | [View items]",\
              "elementName":"automation\_template\_439231",\
              "id":"1f7871fc-2933-41dd-8f67-ab2a75f055fa",\
              "languageCode":"en",\
              "languagePolicy":"deterministic",\
              "meta":"\{\"example\":\"Dear Customer, Here are our products. \\\\nThanks for shopping with us\"}",\
              "modifiedOn":1710799689011,\
              "namespace":"9c7fe92f\_2a48\_40ec\_83d0\_69c62a772433",\
              "priority":1,\
              "quality":"UNKNOWN",\
              "retry":0,\
              "stage":"NONE",\
              "status":"PENDING",\
              "templateType":"PRODUCT",\
              "vertical":"Internal\_vertical",\
              "wabaId":"104505526065633"\
           }\
        }
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Error**
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        429
      </td>

      <td style={{ textAlign: "left" }}>
        `{     "status": "error",     "message": "Too Many Requests"   }`
      </td>

      <td style={{ textAlign: "left" }}>
        10 Requests per Minute
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        500
      </td>

      <td style={{ textAlign: "left" }}>
        `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }`
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>