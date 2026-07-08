---
title: Get Quality Rating
excerpt: >-
  Use this API to retrieve the quality rating and messaging tier information for
  your WhatsApp Business API (WABA) application. This endpoint provides insights
  into your phone number's quality status, current messaging limits, and any
  recent tier changes.
api:
  file: partner-portal-public-apis-1.json
  operationId: get_partner-app-appid-ratings
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  Note:

  You can use this API to check the Quality Rating, and Messaging Limits of your App. For an App, API requests are limited to once every 24 hours. To know more about Messaging Limits, [click here](https://developers.facebook.com/docs/whatsapp/messaging-limits). To learn about how you can determine the Quality Rating of your WABA i.e. Green, Yellow and Red, [click here](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits).
</Callout>

### Parameters

| Parameters    | Value                   | Description                       |
| :------------ | :---------------------- | :-------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application  |
| appId         | `{{APP_ID}}`            | Unique Identifier for Gupshup App |

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/ratings' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
{
    "oldLimit": "TIER_10K",
    "currentLimit": "TIER_10K",
    "event": "ONBOARDING",
    "eventTime": 123455556,
    "phoneQuality": "GREEN"
}
```

or,

```json
{  
    "message": "no event update available",  
    "status": "success"  
}
```

### Response Codes

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
        `{       "oldLimit": "TIER_10K",       "currentLimit": "TIER_10K",       "event": "ONBOARDING",       "eventTime": 123455556,       "phoneQuality": "GREEN"   }`
      </td>

      <td>
        If we have received an event for the WABA
      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        `{     "message": "no event update available",     "status": "success" }`
      </td>

      <td>
        If the API request is successful, but we have not received an event for the WABA's capacity and message limit.
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
        `{   "status": "error",   "message": "Too Many Requests" }`
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
        `{   "status": "error",   "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support" }`
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `{
                  "status": "error",
                  "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"
                }`
      </td>

      <td>
        If invalid AppId/Token
      </td>
    </tr>
  </tbody>
</Table>
