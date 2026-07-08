---
title: Send MM Lite message with GIF template
excerpt: Sends a marketing WhatsApp message using a GIF-based template.
api:
  file: send-mm-lite-gif-template-swagger.yaml
  operationId: sendMMLiteGifTemplateMessage
hidden: false
---
# API Request

```
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/onboarding/marketing/msg' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "recipient_type": "individual",
    "messaging_product": "whatsapp",
    "to": "{{DESTINATION}}",
    "type": "template",
    "template": {
        "name": "{{TEMPLATE_NAME}}",
        "language": {
            "policy": "deterministic",
            "code": "{{LANGUAGE_CODE}}"
        },
        "namespace": "{{NAMESPACE}}",
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "GIF",
                        "gif": {
                            "link": "{{GIF_URL}}"
                        }
                    }
                ]
            },
            {
                "type": "body"
            }
        ]
    }
}'
```

<br />

# Response

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status code
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
        200
      </td>

      <td>
        ```
        {
            "messages": [
                {
                    "id": "1ceeb739-06cd-4434-a1e0-8afac154ede4"
                }
            ],
            "messaging_product": "whatsapp",
            "contacts": [
                {
                    "input": "9188889945",
                    "wa_id": "9188898545"
                }
            ]
        }
        ```
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        ```
        {"status": "error", "message": "Too Many Requests"} 
        ```
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
        ```
        {"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"} 
        ```
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

<br />

# &#x20;Request Parameters

**Headers**

| Key           | Description                      | Value                   | Data Type | Required/ Optional | Constraints                                |
| :------------ | :------------------------------- | :---------------------- | :-------- | :----------------- | :----------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String    | Required           | Should be a valid Partner App Access Token |

**Path Parameters**

| Key    | Description                      | Value        | Data Type | Required/ Optional | Constraints                                                                                                                        |
| :----- | :------------------------------- | :----------- | :-------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| APP_ID | App ID to fetch the access token | `{{APP_ID}}` | String    | Required           | The Id should be a valid app Id of Gupshup. The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

**JSON Body Parameters**

| Key               | Description                                 | Value                        | Data Type | Required/ Optional | Constraints                                            |
| :---------------- | :------------------------------------------ | :--------------------------- | :-------- | :----------------- | :----------------------------------------------------- |
| recipient_type    | Type of recipient                           | `individual`                 | String    | Required           | Must be "individual" for single recipient              |
| messaging_product | Messaging platform                          | `whatsapp`                   | String    | Required           | Must be "whatsapp"                                     |
| to                | Destination Phone Number                    | `{{DESTINATION}}`            | String    | Required           | Valid phone number with country code                   |
| type              | Message type                                | `template`                   | String    | Required           | Must be "template" for template messages               |
| template          | Template object containing template details | See template structure below | Object    | Required           | Must include name, language, namespace, and components |

<br />

**Template Object Structure**

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Value
      </th>

      <th>
        Data Type
      </th>

      <th>
        Required/ Optional
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
      </td>

      <td>
        Template name
      </td>

      <td>
        `{{TEMPLATE_NAME}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Must be an approved template name t
      </td>
    </tr>

    <tr>
      <td>
        language
      </td>

      <td>
        Language object
      </td>

      <td>
        `{"policy": "deterministic", "code": "en"} `
      </td>

      <td>
        Object
      </td>

      <td>
        Required
      </td>

      <td>
        Contains policy and language code
      </td>
    </tr>

    <tr>
      <td>
        namespace
      </td>

      <td>
        Template namespace
      </td>

      <td>
        `{{NAMESPACE}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        WABA namespace for the template
      </td>
    </tr>

    <tr>
      <td>
        components
      </td>

      <td>
        Array of template components
      </td>

      <td>
        ```
        {
          "components": [
            {
              "type": "header",
              "parameters": [
                {
                  "type": "GIF",
                  "gif": {
                    "link": "{{GIF_URL}}"
                  }
                }
              ]
            },
            {
              "type": "body"
            }
          ]
        }

        ```
      </td>

      <td>
        Array
      </td>

      <td>
        Required
      </td>

      <td>
        Must include header and body components
      </td>
    </tr>
  </tbody>
</Table>

<br />