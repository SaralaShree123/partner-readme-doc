---
title: Link an app
excerpt: Use this API to link a WABA to Gupshup app
api:
  file: partner-portal-api-23.json
  operationId: linkApp
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        PARTNER\_TOKEN
      </td>

      <td style={{ textAlign: "left" }}>
        JWT Token issues post Partner login
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner JWT Token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        name
      </td>

      <td style={{ textAlign: "left" }}>
        Name for the app
      </td>

      <td style={{ textAlign: "left" }}>
        * Should be between 6 - 150 chars
        * Should not conflict with any other Gupshup App               - Special Characters are not allowed
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        wabaId
      </td>

      <td style={{ textAlign: "left" }}>
        Live waba id
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        phone
      </td>

      <td style={{ textAlign: "left" }}>
        Phone number associated with the live waba id
      </td>

      <td style={{ textAlign: "left" }}>
        String  

        phone should be entered without +, - or spaces.\
        For e.g. US phone +1 555-111-2222 should be just entered as 15551112222
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        callbackUrl
      </td>

      <td style={{ textAlign: "left" }}>
        Optionally, set the callback URL for any Account or message related events
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        storageRegion
      </td>

      <td style={{ textAlign: "left" }}>
        Optionally, set the data storage region for an app
      </td>

      <td style={{ textAlign: "left" }}>
        String  

        Storage region must be one amongst\
        [BR, DE, CH, GB, BH, ZA, AE, US, CA, AU, ID, IN, JP, SG, KR]
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --request POST --location 'https://partner.gupshup.io/partner/tpp/app' \
--header 'Authorization: <PARTNER_TOKEN>' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name={{appName}}' \
--data-urlencode 'wabaId={{wabaId}}' \
--data-urlencode 'phone={{phoneNumber}}' \
--data-urlencode 'callbackUrl={{callbackUrl}}' \ (optional)
--data-urlencode 'storageRegion={{storageRegion}}' (optional)
```

## Sample Response

```json
{
    "status" : "success",
    "appId": "<app_id>"
}
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Status Code
      </th>

      <th style={{ textAlign: "left" }}>
        Response
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

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        200
      </td>

      <td style={{ textAlign: "left" }}>
        \`\{\
            "status" : "success",\
            "appId": "\<app\_id>"\
        }
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
        409
      </td>

      <td style={{ textAlign: "left" }}>
        `{     "status": "error",     "message": "Bot Already Exists"   }`
      </td>

      <td style={{ textAlign: "left" }}>
        When already a bot with same name exists in gupshup
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        409
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
            "status": "error",\
            "message" "App e3f5d0a5-6ac4-42e2-8aa2-3c178fcefd9f already exists with phone 919087875656",\
            "appId": "e3f5d0a5-6ac4-42e2-8aa2-3c178fcefd9f"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        When phone number is already associated to another app
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "status": "error",\
          "message": "Invalid characters used in app name"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        When Special character is added in name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "status": "error",\
          "message": "App name should be between 6 to 150 charecters in length"\
        }
      </td>

      <td style={{ textAlign: "left" }}>
        if App name is not provided or App name length is less than 6\
        or more than 150 characters.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
       `{
            "status": "error",
            "appId": "<appId>",
            "message": "App created, but failed to set callback on the application"
        }`
      </td>

      <td style={{ textAlign: "left" }}>
        When callback url failed to set
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        429
      </td>

      <td style={{ textAlign: "left" }}>
        `{     "status": "error",     "message": "Too Many Requests"   }`
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
        `{     "status": "error",     "message": "Unable to create App"   }`
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>