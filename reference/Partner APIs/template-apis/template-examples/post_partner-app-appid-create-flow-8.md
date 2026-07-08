---
title: Flow
api:
  file: Flow_Template.json
  operationId: post_partner-app-appid-templates
hidden: true
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
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used
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
        \{\{ELEMENT\_NAME}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        elementName (not more than 180char.) Mandatory fields
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        languageCode
      </td>

      <td style={{ textAlign: "left" }}>
        Language code for the template. Refer to all the language codes <Anchor label="here" target="_blank" href="https://support.gupshup.io/hc/en-us/articles/360013321939-Which-languages-are-supported-for-message-templates">here</Anchor>.
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
        languageCode default value : `en\_US`
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
        **Category Type**: `MARKETING  
                                                UTILITY`
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
        DOCUMENT
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
        \{\{EXAMPLE\_HEADER}}
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
        Boolean value. If True, Meta will automatically update the category of the template as per the template content.  Default\
        value is False.
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ALLOW\_TEMPLATE\_CATEGORY\_CHANGE}}
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
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/templates' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data-urlencode 'elementName=test_flows_1' \
--data-urlencode 'languageCode=en' \
--data-urlencode 'content=Hi {{1}},
Today is the last day of the BIg Billion Day'\''s sale. Make the most out of it!' \
--data-urlencode 'category=MARKETING' \
--data-urlencode 'templateType=IMAGE' \
--data-urlencode 'example=Hi Sam,
Today is the last day of the BIg Billion Day'\''s sale. Make the most out of it!' \
--data-urlencode 'enableSample=true' \
--data-urlencode 'allowTemplateCategoryChange=true' \
--data-urlencode 'vertical=Sample template using Flow button with others' \
--data-urlencode 'buttons=
[
	{
		"type": "FLOW",
		"text": "Share Interests",
    "flow_id": "3961313760791090",
    "flow_action": "NAVIGATE",
    "navigate_screen": "SEGMENTS_SCREEN",
		"icon": "PROMOTION"
   }
]' \
--data-urlencode
'exampleMedia=4::aW1hZ3UvanBlZw==:ARYNMS2RLy7ZxeZdLH6MlbuCHz2bm5naXIbAHYwsJjvrQLKCGZ9LPnNmBC4KYhH2j6WxJEHJ7L6u
vxYsIYonRecvTCm_jyObpUJS-BRgFNcxOQ:e:1749806891:2281283925530161:61551923013914:ARbcT9jwPAS_B423dLM'
```

## Sample Response

```json
{
  "status": "success",
  "template": {
    "appId": "d79ad72e-01f0-98e0-aea4-9f3d60ea2c1e",
    "buttonSupported": "FLOW",
    "category": "MARKETING",
    "containerMeta": {
      "appId": "d79ad72e-01f0-98e0-aea4-9f3d60ea2c1e",
      "data": "Hi {{1}}, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!",
      "buttons": [
        {
          "type": "FLOW",
          "text": "Share Interests",
          "flow_id": "2961313360793010",
          "flow_action": "NAVIGATE",
          "navigate_screen": "SEGMENTS_SCREEN"
        }
      ],
      "sampleText": "Hi Sam, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!",
      "sampleMedia": "4::aW1hZ2UvanBlZw==: ARYNMS2RLy9ZxeZdLH3MlbuCHz2bm5naXIbAHYwsJjvrQLKCGZ9LPnNmBC4KYhH2j6WxJEHJ7L6uvxYsIYonRecvTCm_jyObpUJSBRgFNcxOQ:e:2949806891:2181283925530161:61551923013914:ARbcT9jwPAS_B423dLM",
      "enableSample": true,
      "editTemplate": false,
      "allowTemplateCategoryChange": true,
      "addSecurityRecommendation": false,
      "isCPR": false,
      "cpr": false
    },
    "createdOn": 1749550623322,
    "data": "Hi {{1}}, \nToday is the last day of the Big Billion Day's sale. Make the most out of it! | [Share Interests]",
    "elementName": "test_flows_1",
    "id": "b5ec0148-a2e3-1d96-b280-c1d161a5a0e7",
    "languageCode": "en",
    "languagePolicy": "deterministic",
    "meta": {
      "example": "Hi Sam, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!"
    },
    "modifiedOn": 1749550623322,
    "namespace": "8a499b40_4a56_518c_26fa_1f20f1d6aa18",
    "priority": 1,
    "quality": "UNKNOWN",
    "retry": 0,
    "stage": "NONE",
    "status": "PENDING",
    "templateType": "IMAGE",
    "vertical": "Sample template using Flow button with others",
    "wabaId": "145881286517812"
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
        &#x20;&#x20;
        &#x20; "status": "success",
        &#x20; "template": \{
        &#x20;   "appId": "d79ad72e-01f0-98e0-aea4-9f3d60ea2c1e",
        &#x20;   "buttonSupported": "FLOW",
        &#x20;   "category": "MARKETING",
        &#x20;   "containerMeta": \{
        &#x20;     "appId": "d79ad72e-01f0-98e0-aea4-9f3d60ea2c1e",
        &#x20;     "data": "Hi \{\{1}}, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!",
        &#x20;     "buttons": \[
        &#x20;       \{
        &#x20;         "type": "FLOW",
        &#x20;         "text": "Share Interests",
        &#x20;         "flow\_id": "2961313360793010",
        &#x20;         "flow\_action": "NAVIGATE",
        &#x20;         "navigate\_screen": "SEGMENTS\_SCREEN"
        &#x20;       }
        &#x20;     ],
        &#x20;     "sampleText": "Hi Sam, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!",
        &#x20;     "sampleMedia": "4::aW1hZ2UvanBlZw==: ARYNMS2RLy9ZxeZdLH3MlbuCHz2bm5naXIbAHYwsJjvrQLKCGZ9LPnNmBC4KYhH2j6WxJEHJ7L6uvxYsIYonRecvTCm\_jyObpUJSBRgFNcxOQ:e:2949806891:2181283925530161:61551923013914:ARbcT9jwPAS\_B423dLM",
        &#x20;     "enableSample": true,
        &#x20;     "editTemplate": false,
        &#x20;     "allowTemplateCategoryChange": true,
        &#x20;     "addSecurityRecommendation": false,
        &#x20;     "isCPR": false,
        &#x20;     "cpr": false
        &#x20;   },
        &#x20;   "createdOn": 1749550623322,
        &#x20;   "data": "Hi \{\{1}}, \nToday is the last day of the Big Billion Day's sale. Make the most out of it! | \[Share Interests]",
        &#x20;   "elementName": "test\_flows\_1",
        &#x20;   "id": "b5ec0148-a2e3-1d96-b280-c1d161a5a0e7",
        &#x20;   "languageCode": "en",
        &#x20;   "languagePolicy": "deterministic",
        &#x20;   "meta": \{
        &#x20;     "example": "Hi Sam, \nToday is the last day of the Big Billion Day's sale. Make the most out of it!"
        &#x20;   },
        &#x20;   "modifiedOn": 1749550623322,
        &#x20;   "namespace": "8a499b40\_4a56\_518c\_26fa\_1f20f1d6aa18",
        &#x20;   "priority": 1,
        &#x20;   "quality": "UNKNOWN",
        &#x20;   "retry": 0,
        &#x20;   "stage": "NONE",
        &#x20;   "status": "PENDING",
        &#x20;   "templateType": "IMAGE",
        &#x20;   "vertical": "Sample template using Flow button with others",
        &#x20;   "wabaId": "145881286517812"
        &#x20; }
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
        "status": "error",
        "message": "Too Many Requests"
        }
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
        "status": "error",
        "message": "Internal server error. Please try again later and if the Issue still persists then contact Gupshup Dev Support"
        }
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>