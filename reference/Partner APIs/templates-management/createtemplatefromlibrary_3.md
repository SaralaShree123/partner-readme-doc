---
title: Create Template from Template Library
excerpt: API to create template from pre approved Meta Library Template
api:
  file: metalibrary_3_0.json
  operationId: createTemplateFromLibrary_3
hidden: false
---
# Rate Limit

10 Requests per Minute

<br />

# Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/:appId/template/metalibrary' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'elementName={{NEW_ELEMENT_NAME}}' \
--data-urlencode 'category=UTILITY' \
--data-urlencode 'languageCode={{LANGUAGE_CODE_OF_LIBRARY_TEMPLATE}}' \
--data-urlencode 'libraryTemplateName={{NAME_OF_LIBRARY_TEMPLATE}}' \
--data-urlencode 'buttons={{BUTTONS_IN_SAME_FORMAT_LIKE_LIBRARY_TEMPLATE}}}'
```

# Sample Response

```curl
      {
  "status": "success",
  "templates": {
    "buttonSupported": "URL",
    "category": "UTILITY",
    "containerMeta": "{\"data\":\"Hei, {{1}}\\n\\nDen nye kontoen din er opprettet.\\n\\nBekreft {{2}} hello.\",\"buttons\":[{\"type\":\"URL\",\"text\":\"Bekreft konto\",\"url\":\"https://www.example.com/\"}],\"header\":\"hello\",\"sampleText\":\"Hei, John\\n\\nhello.\\n\\nhello.\",\"sampleHeader\":\"hello\",\"enableSample\":true,\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false}",
    "createdOn": 1721897898300,
    "data": "Fullfør konfigurering av konto\nHei, {{1}}\n\nhellot.\n\nhello {{2}} hello",
    "elementName": "jul23libtest1_8",
    "externalId": "399568216474711",
    "id": "0cc281c9-dc45-4ea3-bf50-411e9b8ff9b3",
    "languageCode": "nb",
    "languagePolicy": "deterministic",
    "meta": "{\"example\":\"Hei, John\\n\\nhello.\\n\\nhello\"}",
    "modifiedOn": 1721897898300,
    "namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c",
    "quality": "UNKNOWN",
    "status": "APPROVED",
    "templateType": "TEXT",
    "wabaId": "216141188246170"
  }
}
```

# Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Headers**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        PARTNER\_APP\_TOKEN
      </td>

      <td>
        App Access Token issued post partner login
      </td>

      <td>
        Should be a valid partner app access token belonging to the passed appId
      </td>
    </tr>

    <tr>
      <td>
        **Form Params**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        elementName
      </td>

      <td>
        Name of new element name to be created
      </td>

      <td>
        Template name
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        Category name
      </td>

      <td>
        Currently only UTILITY and AUTHENTICATION is supported
      </td>
    </tr>

    <tr>
      <td>
        languageCode
      </td>

      <td>
        Meta language code
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        libraryTemplateName
      </td>

      <td>
        Name of meta library template used as base template
      </td>

      <td>
        Element name of meta library template
      </td>
    </tr>

    <tr>
      <td>
        buttons
      </td>

      <td>
        Buttons list for new template
      </td>

      <td>
        Buttons list of meta library template
      </td>
    </tr>

    <tr>
      <td>
        libraryTemplateBodyInputs
      </td>

      <td>
        Provide authentication related details.

        (AUTHENTICATION)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Path Params**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        appId
      </td>

      <td>
        App Id for the app that is linked to the Partner Account
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# Status Codes

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
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{
        "message": "Authentication Failed",
        "status": "error"
        }
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
        "message": "Internal Server Error"
        }
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": "Language is missing"
        }
      </td>

      <td>
        If languageCode is not provided
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": "Library Template Name is missing"
        }
      </td>

      <td>
        If libraryTemplateName is not provided
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": " The parameter library\_template\_button\_inputs\[0]\['type'] is required. - null, null"
        }
      </td>

      <td>
        If button type is not provided
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": "Template Already exists with same namespace and elementName and languageCode"
        }
      </td>

      <td>
        If name of template already exists
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": "Category is missing"
        }
      </td>

      <td>
        If category is not provided
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{
        "status": "error",
        "message": "Template Name is missing"
        }
      </td>

      <td>
        If elementName is not provided
      </td>
    </tr>
  </tbody>
</Table>