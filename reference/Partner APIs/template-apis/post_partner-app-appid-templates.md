---
title: Apply For Templates with Sample Media
excerpt: >-
  Use this API to create and submit a template along with sample media for your
  Gupshup App.
api:
  file: partner-portal-public-apis.json
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
You will need below details to start using this API.

1. App Id
2. Partner App Token
3. Handle Id

### Parameters

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Value
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
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER\_APP\_TOKEN}}
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        Unique identifier for a Gupshup App
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        9e97650d-add3-4557-9535-4cdf47c3fa68
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        elementName
      </td>

      <td style={{ textAlign: "left" }}>
        Template element name
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        ticket\_check\_url\_334
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        languageCode
      </td>

      <td style={{ textAlign: "left" }}>
        Template language code
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        en\_US
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        content
      </td>

      <td style={{ textAlign: "left" }}>
        Template Content
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Your verification code is \{\{1}}.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        footer
      </td>

      <td style={{ textAlign: "left" }}>
        Footer of the template. Character limit: 60
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        This is the footer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        category
      </td>

      <td style={{ textAlign: "left" }}>
        The category of your template. **Possible Values:** `AUTHENTICATION`, `MARKETING` and `UTILITY`.
        If you submit the templates with the any other categories, you will receive an error `Invalid category provided, kindly use category from these option AUTHENTICATION, MARKETING, UTILITY.`
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        MARKETING
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        templateType
      </td>

      <td style={{ textAlign: "left" }}>
        Template Type
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        IMAGE
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        vertical
      </td>

      <td style={{ textAlign: "left" }}>
        Template vertical
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Ticket update
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
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Your verification code is 213.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        exampleMedia
      </td>

      <td style={{ textAlign: "left" }}>
        `4::aW1hZ2UvcadG5n:ARYaMMMA2QvIXuQZdPjWVXTOqfoBU3n0L1Ftyg4w57yxi9nD105yQDvW2nu3-HNo9HGefxZ-Ig-HAi3YSsckwIsOEUwxSPatsxT0Niob30E63A:e:1634884682:2281283925530161:100033655335566:ARaBAxW-1L-ZRu6SMSg`
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        This is the [handleId](https://docs.gupshup.io/reference/post_partner-app-appid-upload-media).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        enableSample
      </td>

      <td style={{ textAlign: "left" }}>
        Required when submitting CTA template with variables.
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        true
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        allowTemplateCategoryChange
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean value. If True, Meta will automatically update the category of the template as per the template content. Default value is False. If the category gets updated, you can view the oldCategory from the [Get Templates API](https://partner-docs.gupshup.io/update/reference/get_partner-app-appid-templates#/)
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/templates' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{ELEMENT_NAME}}' \
--data-urlencode 'languageCode={{LANGUAGE_CODE}}' \
--data-urlencode 'content=Your verification code is {{1}}.' \
--data-urlencode 'footer=This is the footer' \
--data-urlencode 'category={{CATEGORY}}' \
--data-urlencode 'templateType=IMAGE' \
--data-urlencode 'vertical=Ticket update' \
--data-urlencode 'appId={{APP_ID}}' \
--data-urlencode 'example=Your verification code is 213.' \
--data-urlencode 'exampleMedia={{HANDLE_ID}}' \
--data-urlencode 'enableSample=true' \
--data-urlencode 'allowTemplateCategoryChange=false'
```

### Sample Response

```json
{
	"status": "success",
	"template": {
    	"appId": <APP_ID>,
    	"category": "MARKETING",
    	"containerMeta": "{\"appId\":\"<APP_ID>\",\"data\":\"Hello I'm your virtual assistant\",\"footer\":\"Footer message\",\"sampleText\":\"Hello I'm your virtual assistant\",\"sampleMedia\":\"4::aW1hZ2UvcG5n:ARbkz3cEPftULo2onMnoculVMN-9ZPp2g6s6CYgkNU3VQwIlPDBhhq5nUDB3Gfcwi7x9rrsMAwpWoZ33NHPKPX3wzmy-4RXNxmu_D_XHTjiBzA:e:1708654057:2281283925530161:100033655335566:ARZYdDSW0Kdy0jXCHPU\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":true,\"addSecurityRecommendation\":false}",
    	"createdOn": 1708333889144,
    	"data": "Hello I'm your virtual assistant\nFooter message",
    	"elementName": "handle_id_1",
    	"id": "d00cca5c-ec89-431f-9421-70952fcd5695",
    	"languageCode": "en",
    	"languagePolicy": "deterministic",
    	"meta": "{\"example\":\"Hello I'm your virtual assistant\"}",
    	"modifiedOn": 1708333889144,
    	"namespace": "713e44ba_6a35_4cc4_ba70_9ab2db948214",
    	"priority": 1,
    	"quality": "UNKNOWN",
    	"retry": 0,
    	"stage": "NONE",
    	"status": "PENDING",
    	"templateType": "IMAGE",
    	"vertical": "media_gs_32",
    	"wabaId": "178402998700036"
	}
}
```

## Status Code

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Status Code
      </th>

      <th style={{ textAlign: "left" }}>

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
        Response
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        200
      </td>

      <td style={{ textAlign: "left" }}>

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
        \{

       '"status": "error","message": "Too Many Requests"}'
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
        \{

        "status": "error","message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"}
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>