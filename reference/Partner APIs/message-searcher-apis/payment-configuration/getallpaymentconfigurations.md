---
title: Fetch all payment configurations
api:
  file: Payment_Configuration_APIs.json
  operationId: getAllPaymentConfigurations
hidden: true
---
Use this API to fetch all payment configurations for a particular app.

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
        App Id of the app for        which callback to be set
      </td>

      <td style={{ textAlign: "left" }}>
        `{{APP_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of
          Gupshup.
        * It should belong to the same account as the apikey.
        * Required
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APPID}}/payment/configurations/' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```
{
  "data": 
  [
    {
      "payment_configurations": 
	  [
        {
          "configuration_name": "test-paymentconfiguration",
          "merchant_category_code": 
		  {
            "code": "0000",
            "description": "Test MCC Code"
          },
          "purpose_code": 
		  {
            "code": "00",
            "description": "Test Purpose Code"
          },
          "status": "Active",
          "provider_mid": "test-payment-gateway-mid",
          "provider_name": "RazorPay",
          "created_timestamp": 1720203204,
          "updated_timestamp": 1721088316,
        }
      ]
    }
  ]
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
        "data":
        \[
        \{
        "payment\_configurations":
        \[
        \{
        "configuration\_name": "test-paymentconfiguration",
        "merchant\_category\_code":
        \{
        "code": "0000",
        "description": "Test MCC Code"
        },
        "purpose\_code":
        \{
        "code": "00",
        "description": "Test Purpose Code"
        },
        "status": "Active",
        "provider\_mid": "test-payment-gateway-mid",
        "provider\_name": "RazorPay",
        "created\_timestamp": 1720203204,
        "updated\_timestamp": 1721088316,
        }
        ]
        }
        ]
        }
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