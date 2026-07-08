---
title: Grant or Revoke User Access
excerpt: Use this API to grant or revoke access to the user.
api:
  file: user-managemnet-apis.json
  operationId: put_partner-users-userid-active
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
        Data Type
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
        JWT Token issues post Partner login
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER\_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        It should be a valid Partner JWT Token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        userId
      </td>

      <td style={{ textAlign: "left" }}>
        User ID of the user
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{USER\_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        email
      </td>

      <td style={{ textAlign: "left" }}>
        Email ID of the user
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{EMAIL}}
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
        active
      </td>

      <td style={{ textAlign: "left" }}>
        To set the user as active
      </td>

      <td style={{ textAlign: "left" }}>
        True/False
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        To grant access, active should be true.  

        To revoke access, active should be false
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request PUT 'http://{{BASE_URL}}/partner/users/{{USER_ID}}/active' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: {{PARTNER_TOKEN}}' \
--data-urlencode 'email={{EMAIL}}' \
--data-urlencode 'active={{active}}'
```

## Sample Response

```json
{
    "status": "success",
    "message": "Access has been granted for user kajal"
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
        If active is true:\
        ```
        {  
            "status": "success",  
            "message": "Access has been granted for user kajal"  
        }
        ```  

        If active is false:\
        ```
        {  
            "status": "success",  
            "message": "Access has been revoked for user kajal"  
        }
        ```
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
        400
      </td>

      <td style={{ textAlign: "left" }}>
        ```
        {  
            "status": "error",  
            "message": "Input parameters does not match"  
        }
        ```
      </td>

      <td style={{ textAlign: "left" }}>
        If email and user ID does not match
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        429
      </td>

      <td style={{ textAlign: "left" }}>
        ```
        {  
          "status": "error",  
          "message": "Too Many Requests"  
        }
        ```
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
        ```
        {  
          "status": "error",  
          "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"  
        }
        ```
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>
