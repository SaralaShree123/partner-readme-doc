---
title: Carousel (Video)
excerpt: ''
api:
  file: carousel-type-templatevideo-2.json
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
        templateType
      </td>

      <td style={{ textAlign: "left" }}>
        CAROUSEL
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
        The type of template: CAROUSEL  

         Cards only to be passed if template type is CAROUSEL
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
        cards
      </td>

      <td style={{ textAlign: "left" }}>
        Card list
      </td>

      <td style={{ textAlign: "left" }}>
        \[\{"headerType":"VIDEO","mediaUrl":null,"mediaId":"6462811350485912","exampleMedia":null,"body":"Time for shopping yay \{\{1}} 😀","sampleText":"Time for shopping yay user 😀","buttons":\[\{"type":"URL","text":"Buy now","url":"[https://www.luckyshrub.com/shop?promo=\{\{1}}","buttonValue":"https://www.luckyshrub.com/shop?promo=","suffix":"exotic\_produce\_2023","example":\["https://www.luckyshrub.com/shop?promo=exotic\_produce\_2023"\]},\{"type":"QUICK\_REPLY","text":"Send](https://www.luckyshrub.com/shop?promo=\{\{1}}","buttonValue":"https://www.luckyshrub.com/shop?promo=","suffix":"exotic_produce_2023","example":\["https://www.luckyshrub.com/shop?promo=exotic_produce_2023"]},\{"type":"QUICK_REPLY","text":"Send) more like this"}]}]
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Either of mediaUrl, mediaId or exampleMedia is required. If exampleMedia is not provided, the handleId / exampleMedia will be generated in the backend using the mediaUrl / mediaId.  

        ```
        [  
          {  
            "headerType": "<VIDEO>",  
            "mediaUrl": "<video url>",  
            "mediaId": "<video id>",  
            "exampleMedia": "<video handle id>",  
            "body": "<card 1 body>",  
            "sampleText": "<card 1 example>",  
            "buttons": <button_list>  
          }  
        ]
        ```
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

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'content={{CONTENT}}' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'vertical={{VERTICAL}}' \
--data-urlencode 'templateType={{TEMPLATE_TYPE}}' \
--data-urlencode 'example={{EXAMPLE}}' \
--data-urlencode 'allowTemplateCategoryChange={{ALLOW_TEMPLATE_CATEGORY_CHANGE}}' \
--data-urlencode 'enableSample={{ENABLE_SAMPLE}}' \
--data-urlencode 'cards=[{"headerType":"VIDEO","mediaUrl":null,"mediaId":"6462811350485912","exampleMedia":null,"body":"Time for shopping yay {{1}} 😀","sampleText":"Time for shopping yay user 😀","buttons":[{"type":"URL","text":"Buy now","url":"https://www.luckyshrub.com/shop?promo={{1}}","buttonValue":"https://www.luckyshrub.com/shop?promo=","suffix":"exotic_produce_2023","example":["https://www.luckyshrub.com/shop?promo=exotic_produce_2023"]},{"type":"QUICK_REPLY","text":"Send more like this"}]}]'
```

## Sample Response

```json
{
    "status": "success",
    "template": {
        "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
        "category": "MARKETING",
        "containerMeta": "{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Hey there new products are here\",\"cards\":[{\"headerType\":\"VIDEO\",\"mediaId\":\"6462811350485912\",\"body\":\"Time for shopping yay {{1}} 😀\",\"sampleText\":\"Time for shopping yay user 😀\",\"buttons\":[{\"type\":\"URL\",\"text\":\"Buy now\",\"url\":\"https://www.luckyshrub.com/shop?promo={{1}}\",\"example\":[\"https://www.luckyshrub.com/shop?promo=exotic_produce_2023\"]},{\"type\":\"QUICK_REPLY\",\"text\":\"Send more like this\"}]}],\"sampleText\":\"Hey there new products are here\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false}",
        "createdOn": 1715666311400,
        "data": "Hey there new products are here",
        "elementName": "mediaidvideotemplate",
        "id": "485d9a3d-851c-4bb1-b9ac-be9713aa347c",
        "languageCode": "en",
        "languagePolicy": "deterministic",
        "meta": "{\"example\":\"Hey there new products are here\"}",
        "modifiedOn": 1715666311400,
        "namespace": "9c7fe92f_2a48_40ec_83d0_69c62a772433",
        "priority": 1,
        "quality": "UNKNOWN",
        "retry": 0,
        "stage": "NONE",
        "status": "PENDING",
        "templateType": "CAROUSEL",
        "vertical": "internal_vertical",
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
            "status": "success",\
            "template": \{\
                "appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",\
                "category": "MARKETING",\
                "containerMeta": "\{\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",\"data\":\"Hey there new products are here\",\"cards\":\[\{\"headerType\":\"VIDEO\",\"mediaId\":\"6462811350485912\",\"body\":\"Time for shopping yay \{\{1}} 😀\",\"sampleText\":\"Time for shopping yay user 😀\",\"buttons\":\[\{\"type\":\"URL\",\"text\":\"Buy now\",\"url\":\"[https://www.luckyshrub.com/shop?promo=\{\{1}}\\",\\"example\\":\[\\"https://www.luckyshrub.com/shop?promo=exotic\_produce\_2023\\"\]},\{\\"type\\":\\"QUICK\_REPLY\\",\\"text\\":\\"Send](https://www.luckyshrub.com/shop?promo=\{\{1}}\\",\\"example\\":\[\\"https://www.luckyshrub.com/shop?promo=exotic_produce_2023\\"]},\{\\"type\\":\\"QUICK_REPLY\\",\\"text\\":\\"Send) more like this\"}]}],\"sampleText\":\"Hey there new products are here\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false}",\
                "createdOn": 1715666311400,\
                "data": "Hey there new products are here",\
                "elementName": "mediaidvideotemplate",\
                "id": "485d9a3d-851c-4bb1-b9ac-be9713aa347c",\
                "languageCode": "en",\
                "languagePolicy": "deterministic",\
                "meta": "\{\"example\":\"Hey there new products are here\"}",\
                "modifiedOn": 1715666311400,\
                "namespace": "9c7fe92f\_2a48\_40ec\_83d0\_69c62a772433",\
                "priority": 1,\
                "quality": "UNKNOWN",\
                "retry": 0,\
                "stage": "NONE",\
                "status": "PENDING",\
                "templateType": "CAROUSEL",\
                "vertical": "internal\_vertical",\
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