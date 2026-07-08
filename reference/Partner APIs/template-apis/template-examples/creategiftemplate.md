---
title: GIF
excerpt: Creates a new GIF template for WhatsApp Business API messaging
api:
  file: gif-template-api-swagger.yaml
  operationId: createGifTemplate
hidden: true
---
# Rate Limit:

10 requests per minute

# Important Notes:

The template will be created with status "PENDING" and requires approval- elementName must be unique for the WABA's namespace-

# Media size constraints:

Videos must be under 3.5 MB to be accepted.

# Rendering behaviour:

Depending on platform rollout and client support, the same media asset may be rendered as a GIF, static image, or video for end users. This behaviour is controlled by Meta and may vary over time.

# API Request

```
curl --request POST \
  --url https://qa-partner-api.smsgupshup.dev/partner/app/bf9ee64c-3d4d-4ac4-8668-732e577007c4/templates \
  --header 'Authorization: sk_852356fadaab4eefb679845237c85213' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data elementName=avida_gif_template \
  --data languageCode=en \
  --data 'content=This is my first GIF template' \
  --data 'footer=Hello GIF' \
  --data category=MARKETING \
  --data templateType=GIF \
  --data vertical=update_shop \
  --data 'example=This is my first GIF template' \
  --data mediaId=8fa96b2c-744e-4acf-bc98-9d4cd66bdd34 \
  --data 'mediaUrl="https://d2kq6t3nveviav.cloudfront.net/0/public/0/0/gupshup/918097424541/8fa96b2c-744e-4acf-bc98-9d4cd66bdd34/1767777627749_sample01.mp4"' \
  --data enableSample=true
```

<br />

# API Response

```
{
  "status": "success",
  "templates": [
    {
      "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
      "category": "MARKETING",
      "containerMeta": "{\"appId\":\"bf9ee64c-3d4d-4ac4-8668-732e577007c4\",\"data\":\"This is my first GIF template\",\"footer\":\"Hello GIF\",\"sampleText\":\"This is my first GIF template\",\"enableSample\":true,\"mediaId\":\"8fa96b2c-744e-4acf-bc98-9d4cd66bdd34\",\"mediaUrl\":\"https://d2kq6t3nveviav.cloudfront.net/0/public/0/0/gupshup/918097424541/8fa96b2c-744e-4acf-bc98-9d4cd66bdd34/1767777627749_sample01.mp4\",\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"isCPR\":false,\"cpr\":false}",
      "createdOn": 1769600654568,
      "data": "This is my first GIF template\nHello GIF",
      "elementName": "avida_gif_template",
      "externalId": "869249462577731",
      "id": "2ae16d34-f644-4c14-9396-568b89450ff2",
      "internalCategory": 0,
      "internalType": 0,
      "languageCode": "en",
      "languagePolicy": "deterministic",
      "meta": "{\"example\":\"This is my first GIF template\",\"mediaId\":\"8fa96b2c-744e-4acf-bc98-9d4cd66bdd34\",\"mediaUrl\":\"https://d2kq6t3nveviav.cloudfront.net/0/public/0/0/gupshup/918097424541/8fa96b2c-744e-4acf-bc98-9d4cd66bdd34/1767777627749_sample01.mp4\"}",
      "modifiedOn": 1769600757736,
      "namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c",
      "parameterFormat": "POSITIONAL",
      "priority": 1,
      "quality": "UNKNOWN",
      "retry": 0,
      "stage": "NONE",
      "state": "ACTIVE",
      "status": "APPROVED",
      "templateType": "GIF",
      "vertical": "update_shop",
      "wabaId": "216141188246170"
    }
}
```

<br />

# Response

<br />

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
          "status": "success",
          "templates": [
            {
              "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
              "category": "MARKETING",
              "containerMeta": "{\"appId\":\"bf9ee64c-3d4d-4ac4-8668-732e577007c4\",\"data\":\"This is my first GIF template\",\"footer\":\"Hello GIF\",\"sampleText\":\"This is my first GIF template\",\"enableSample\":true,\"mediaId\":\"8fa96b2c-744e-4acf-bc98-9d4cd66bdd34\",\"mediaUrl\":\"https://d2kq6t3nveviav.cloudfront.net/0/public/0/0/gupshup/918097424541/8fa96b2c-744e-4acf-bc98-9d4cd66bdd34/1767777627749_sample01.mp4\",\"editTemplate\":false,\"allowTemplateCategoryChange\":false,\"addSecurityRecommendation\":false,\"isCPR\":false,\"cpr\":false}",
              "createdOn": 1769600654568,
              "data": "This is my first GIF template\nHello GIF",
              "elementName": "avida_gif_template",
              "externalId": "869249462577731",
              "id": "2ae16d34-f644-4c14-9396-568b89450ff2",
              "internalCategory": 0,
              "internalType": 0,
              "languageCode": "en",
              "languagePolicy": "deterministic",
              "meta": "{\"example\":\"This is my first GIF template\",\"mediaId\":\"8fa96b2c-744e-4acf-bc98-9d4cd66bdd34\",\"mediaUrl\":\"https://d2kq6t3nveviav.cloudfront.net/0/public/0/0/gupshup/918097424541/8fa96b2c-744e-4acf-bc98-9d4cd66bdd34/1767777627749_sample01.mp4\"}",
              "modifiedOn": 1769600757736,
              "namespace": "18cfa544_9c62_4dcd_b8f3_b3785d8c917c",
              "parameterFormat": "POSITIONAL",
              "priority": 1,
              "quality": "UNKNOWN",
              "retry": 0,
              "stage": "NONE",
              "state": "ACTIVE",
              "status": "APPROVED",
              "templateType": "GIF",
              "vertical": "update_shop",
              "wabaId": "216141188246170"
            }
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
        {"status": "error", "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"} 
        ```
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

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
| APP_ID | App ID to fetch the access token | `{{APP_ID}}` | String    | Required           | The Id should be a valid app Id of Gupshup. The App must be associated with the account that owns the PARTNER_APP_TOKEN being used |

<br />

**Form Parameters**

| Key          | Description                                                                                                                                      | Value               | Data Type | Required/ Optional | Constraints                                            |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ | :-------- | :----------------- | :----------------------------------------------------- |
| elementName  | The name of a template. Element name is unique for a WABAs namespace.                                                                            | `{{ELEMENT_NAME}}`  | String    | Required           | elementName (not more than 180 char.) Mandatory fields |
| languageCode | Language code for the template. Refer to all the language codes here.                                                                            | `{{LANGUAGE_CODE}}` | String    | Optional           | languageCode default value: en_US                      |
| content      | The body of the template. Character limit: 1028. For the "Authentication" category, the first line should be: `{{1}}` is your verification code. | `{{CONTENT}}`       | String    | Required           | content (not more than 1024 char.)                     |
| category     | The category of your template.                                                                                                                   | `{{CATEGORY}}`      | String    | Required           | Valid values: MARKETING, UTILITY, AUTHENTICATION       |
| vertical     | Industry vertical or use case for the template                                                                                                   | `{{VERTICAL}}`      | String    | Required           | vertical (not more than 180 char.)                     |
| footer       | Footer of the template.                                                                                                                          | `{{FOOTER}}`        | String    | Optional           |                                                        |
| templateType | Type of template                                                                                                                                 | `GIF`               | String    | Required           | Must be set to "GIF" for GIF templates                 |
| example      | Template Example with placeholder values filled                                                                                                  | `{{EXAMPLE}}`       | String    | Required           |                                                        |
| mediaId      | Handle Id required to generate media templates                                                                                                   | `{{MEDIA_ID}}`      | String    | Required           | This is handleId. Generate handleId here               |
| mediaUrl     | media URL                                                                                                                                        | `{{MEDIA_URL}}`     | String    | Required           |                                                        |
| enableSample | Required for creating all types of templates                                                                                                     | `{{ENABLE_SAMPLE}}` | Boolean   | Optional           | if enableSample is true then exampleMedia is required  |