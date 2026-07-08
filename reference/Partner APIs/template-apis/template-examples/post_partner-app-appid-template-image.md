---
title: Image
excerpt: ''
api:
  file: create-image-type-template-1.json
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
        The body of the template. Character limit: 1028. For "Authentication" category the first line should be - \{\{1}} is your verification code.
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
        \{\{VERTICAL}}
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
        footer
      </td>

      <td style={{ textAlign: "left" }}>
        Footer of the template.
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
        templateType
      </td>

      <td style={{ textAlign: "left" }}>
        IMAGE
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
        exampleMedia
      </td>

      <td style={{ textAlign: "left" }}>
        Handle Id required to generate media templates
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ENABLE\_MEDIA}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        This is handleId.  

        Generate handleId [here](https://gupshupinc.atlassian.net/wiki/spaces/UPPIPW/pages/2267807780/Partner+APIs#2-.-Template-Management-APIs:~:text=Get%20HandleId%20For%20Sample%20Media)
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
        allowTemplateCategoryChange
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean value. If True, Meta will automatically update the category of the template as per the template content. Default value is False.
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ALLOW\_TEMPLATE\_CATEGORY\_CHANGE}}
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
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'content={{CONTENT}}' \
--data-urlencode 'footer={{FOOTER}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'vertical={{VERTICAL}}' \
--data-urlencode 'example={{EXAMPLE}}' \
--data-urlencode 'exampleMedia={{EXAMPLE_MEDIA}}' \
--data-urlencode 'enableSample={{ENABLE_SAMPLE}}' \
--data-urlencode 'allowTemplateCategoryChange={{ALLOW_TEMPLATE_CATEGORY_CHANGE}}'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Hi {{1}}.\",\"footer\":\"This is the footer\",\"sampleText\":\"Hi There.\",\"sampleMedia\":\"4::aW1hZ2UvcadG5n:ARYaMMMA2QvIXuQZdPjWVXTOqfoBU3n0L1Ftyg4w57yxi9nD105yQDvW2nu3-HNo9HGefxZ-Ig-HAi3YSsckwIsOEUwxSPatsxT0Niob30E63A:e:1634884682:2281283925530161:100033655335566:ARaBAxW-1L-ZRu6SMSg\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
        "createdOn": 1716282767027,
        "data": "Hi {{1}}.\nThis is the footer",
        "elementName": "image_element",
        "id": "e676c31d-ff1d-42f1-bea1-88049da5b94f",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Hi There.\"}",
        "modifiedOn": 1716282767027,
        "namespace": "9c7fe92f_2a48_40ec_83d0_69c62a772433",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "IMAGE",
        "vertical": "Ticket update",
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
        Comments
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
            "status": "success",\
            "template": \{\
                "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",\
                "category": "MARKETING",\
                "containerMeta": "\{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Hi \{\{1}}.\",\"footer\":\"This is the footer\",\"sampleText\":\"Hi There.\",\"sampleMedia\":\"4::aW1hZ2UvcadG5n:ARYaMMMA2QvIXuQZdPjWVXTOqfoBU3n0L1Ftyg4w57yxi9nD105yQDvW2nu3-HNo9HGefxZ-Ig-HAi3YSsckwIsOEUwxSPatsxT0Niob30E63A:e:1634884682:2281283925530161:100033655335566:ARaBAxW-1L-ZRu6SMSg\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",\
                "createdOn": 1716282767027,\
                "data": "Hi \{\{1}}.\\nThis is the footer",\
                "elementName": "image\_element",\
                "id": "e676c31d-ff1d-42f1-bea1-88049da5b94f",\
                "languageCode": "en",\
                "languagePolicy": "deterministic",\
                "meta": "\{\"example\":\"Hi There.\"}",\
                "modifiedOn": 1716282767027,\
                "namespace": "9c7fe92f\_2a48\_40ec\_83d0\_69c62a772433",\
                "priority": 1,\
                "quality": "UNKNOWN",\
                "retry": 0,\
                "stage": "NONE",\
                "status": "PENDING",\
                "templateType": "IMAGE",\
                "vertical": "Ticket update",\
                "wabaId": "104505526065633"\
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
        \{\
          "status": "error",\
          "message": "Too Many Requests"\
        }
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
        \{\
          "status": "error",\
          "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>