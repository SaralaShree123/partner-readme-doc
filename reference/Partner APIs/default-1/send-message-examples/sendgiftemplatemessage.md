---
title: GIF
excerpt: This API is used to send messages with the GIF template.
api:
  file: send-gif-template-swagger.yaml
  operationId: sendGifTemplateMessage
hidden: false
---
# API Request

```
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/template/msg' \
--header 'Connection: keep-alive' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'source={{SOURCE}}' \
--data-urlencode 'sandbox={{SANDBOX}}' \
--data-urlencode 'destination={{DESTINATION}}' \
--data-urlencode 'template={"id":"{{TEMPLATE_ID}}","params":{{TEMPLATE_PARAMS_LIST}}' \
--data-urlencode 'message={"type":"gif","gif":{"link":"{{GIF_URL}}"}}' \
--data-urlencode 'src.name={{APP_NAME}}'
```

<br />

# Response

<br />

| Status code | Response                                                                                                                                       | Comments               |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| 200         | `{"status": "submitted", "messageId": "db4*****-8ccc-3a438288e72f"} `                                                                          |                        |
| 429         | `{"status": "error", "message": "Too Many Requests"} `                                                                                         | 10 Requests per Minute |
| 500         | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"} ` | For any Internal Error |

<br />

# Request Parameters

**Headers**

| Key           | Description                      | Value                   | Data Type | Required/ Optional | Constraints                                |
| :------------ | :------------------------------- | :---------------------- | :-------- | :----------------- | :----------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String    | Required           | Should be a valid Partner App Access Token |

<br />

**Path Parameters**

| Key    | Description                      | Value        | Data Type | Required/ Optional | Constraints                                                                                                                        |
| :----- | :------------------------------- | :----------- | :-------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| APP_ID | Access Token for the application | `{{APP_ID}}` | String    | Required           | The Id should be a valid app Id of Gupshup. The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

<br />

**Form Parameters**

| Key         | Description                      | Value                                                           | Data Type | Required/ Optional | Constraints                                                                        |
| :---------- | :------------------------------- | :-------------------------------------------------------------- | :-------- | :----------------- | :--------------------------------------------------------------------------------- |
| source      | Source Phone Number              | `{{SOURCE}}`                                                    | Integer   | Required           |                                                                                    |
| sandbox     | Boolean value                    | `{{SANDBOX}}`                                                   | Boolean   | Optional           |                                                                                    |
| destination | Destination Phone Number         | `{{DESTINATION}}`                                               | Integer   | Required           |                                                                                    |
| template    | Json containing template details | `{"id":"{{TEMPLATE_ID}}","params":[{{TEMPLATE_PARAMS_LIST}}]} ` | String    | Required           | Must include valid template id                                                     |
| message     | Message Format for GIF           | `{"type":"gif","gif":{"link":"{{GIF_URL}}"}} `                  | String    | Required           | Must be a valid JSON with type as "gif" and gif object containing link to GIF file |
| src.name    | App Name                         | `{{APP_NAME}}`                                                  | String    | Required           |                                                                                    |