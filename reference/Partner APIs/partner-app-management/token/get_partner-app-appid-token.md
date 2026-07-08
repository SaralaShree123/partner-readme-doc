---
title: Get Access Token for an App
excerpt: >-
  This API endpoint enables partners to generate or retrieve an access token for
  their partner application. The token is used for authenticating API calls to
  WhatsApp Business API and other Gupshup services. The endpoint follows an
  idempotent pattern - if a token already exists for the partner-app
  combination, it returns the existing token; otherwise, it generates a new one.
api:
  file: token-apis.json
  operationId: get_partner-app-appid-token
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can use this token to get App’s templates, submit templates, send messages etc.\
You will need below details to start using this API. 

1. Partner token

### Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER\_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>
        JWT Token issued post Partner login 
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        App ID
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{APP\_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        Unique Identifier for Gupshup App. The ID should be a valid App ID of Gupshup  

        The **App must be associated** with the account that owns the PARTNER\_APP\_TOKEN being utilized. 
      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/token/' \
--header 'Authorization: {{PARTNER_TOKEN}}'
```

### Sample Response

```json
{
    "status": "success",
    "token": {
        "token": "sk_20c901e*********2a592484********1",
        "authoriserId": "aac***e8-d**c-****-a93f-**d6d5a***e8",
        "requestorId": "4**2",
        "createdOn": 1705905891100,
        "modifiedOn": 1705905891100,
        "expiresOn": 0,
        "active": true
    }
}
```