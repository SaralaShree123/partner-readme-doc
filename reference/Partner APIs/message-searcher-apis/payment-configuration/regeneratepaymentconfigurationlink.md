---
title: Regenerate payment link
api:
  file: Payment_Configuration_APIs.json
  operationId: regeneratePaymentConfigurationLink
hidden: true
---
Use this API to regenerate payment link of a payment configurations for a particular app.

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
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>

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
        App Id of the app for which callback to be set
      </td>

      <td style={{ textAlign: "left" }}>
        `{{APP_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of
          Gupshup.
        * It should belong to the same account as the apikey.
        * Required
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        configuration\_name
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the payment configuration to be used in the OrderDetails message.
      </td>

      <td style={{ textAlign: "left" }}>
        test\_configuration
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
        redirect\_url
      </td>

      <td style={{ textAlign: "left" }}>
        The url which        merchant will be redirected to after successfully linking a payment configuration.
      </td>

      <td style={{ textAlign: "left" }}>
        \[redirect url]\([https://testredirecturl](https://testredirecturl.com))
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
curl --location 'https://partner.gupshup.io/partner/app/{{APPID}}/payment/configuration/regenerate' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
	"configuration_name" : "test-payment-configuration"
}'
```

## Sample Response

```
{
	"oauth_url":"https://www.facebook.com/payment/onboarding/init/",
	"expiration": 1721687287
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

        "oauth\_url":"[https://www.facebook.com/payment/onboarding/init/](https://www.facebook.com/payment/onboarding/init/)","expiration": 1721687287}
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
        401
      </td>

      <td>
        \{\
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
        `{     "status": "error",     "message": "Too Many Requests"   }`
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
        `{     "status": "error",     "message": "Internal server error. Please try again later and if the Issue still persists then contact Gupshup Dev Support"   }`
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>