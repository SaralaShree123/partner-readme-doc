---
title: MM Lite Send Message
excerpt: Use this API to send MM Lite message.
api:
  file: mm-lite-send-message-and-get-link-for-onboarding-live-app-8.json
  operationId: mmLiteSendMessage
deprecated: false
hidden: false
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
        Data Types
      </th>

      <th style={{ textAlign: "left" }}>
        Require/Optional
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
        App ID to fetch the access token
      </td>

      <td style={{ textAlign: "left" }}>
        `{{App_ID}}`
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        to
      </td>

      <td style={{ textAlign: "left" }}>
        to phone number where the message need to be send
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Must be a valid phone no
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        template
      </td>

      <td style={{ textAlign: "left" }}>
        meta template payload
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        json
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        This endpoint only supports marketing template.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        type
      </td>

      <td style={{ textAlign: "left" }}>
        Type in the value of what kind of message the user is sending
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        set it’s value as template
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        messaging\_product
      </td>

      <td style={{ textAlign: "left" }}>
        Messaging product is a constant value i.e., whatsapp
      </td>

      <td style={{ textAlign: "left" }}>

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
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/07c7c72d-20e3-4ff9-a5a1-14d1186eeec8/onboarding/marketing/msg' \
--header 'Authorization: sk_8eb35b1f81c24af293a405164a392f30' \
--header 'Content-Type: application/json' \
--data '{
    "recipient_type": "individual",
    "messaging_product": "whatsapp",
    "to": "918888998545",
    "type": "template",
    "template": {
        "language": {
            "policy": "deterministic",
            "code": "en"
        },
        "namespace": "5ff5f84e_789b_44df_80dd_6844d48a6a4a",
        "name": "cc_temp_prod",
        "components": [
            {
                "type": "body",
                "parameters": []
            },
            {
                "type": "button",
                "sub_type": "copy_code",
                "index": "0",
                "parameters": [
                    {
                        "type": "coupon_code",
                        "coupon_code": "250FF"
                    }
                ]
            },
            {
                "type": "button",
                "sub_type": "url",
                "index": "1",
                "parameters": [
                    {
                        "type": "text",
                        "text": "summer2023"
                    }
                ]
            },
            {
                "type": "button",
                "sub_type": "url",
                "index": "2",
                "parameters": [
                    {
                        "type": "text",
                        "text": "summer2023"
                    }
                ]
            }
        ]
    }
}'
```

## Sample Response

```json
{
  "messages": [
    {
      "id": "6ba08089-bdd1-487f-a29c-0c46056aa1f9"
    }
  ],
  "messaging_product": "whatsapp",
  "contacts": [
    {
      "input": "918888998545Value",
      "wa_id": "918888998545Value"
    }
  ]
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                      | Comments |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------- |
| **Success** |                                                                                                                                                                                                                                                               |          |
| 200         | `{     "messages": [       {         "id": "6ba08089-bdd1-487f-a29c-0c46056aa1f9"       }     ],     "messaging_product": "whatsapp",     "contacts": [       {         "input": "918888998545Value",         "wa_id": "918888998545Value"       }     ]   }` |          |
| **Error**   |                                                                                                                                                                                                                                                               |          |
| 400         | `{       "status": "error",       "message": "MM lite is not enabled for this app"   }`                                                                                                                                                                       |          |
| 400         | `{      "status":"error",       "message":"Unauthorised access to the resource. Please review request parameters and headers and retry"   }`                                                                                                                  |          |