---
title: Delete Template
excerpt: Use this API to delete a template using the *elementName*.
api:
  file: partner-portal-public-apis.json
  operationId: delete_partner-app-appid-template-elementname
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You will need details below to start using this API.\
**NOTE:** This action is **irreversible**. Once a template has been deleted, it cannot be restored.

1. App ID
2. Partner App Token
3. Element Name

### Parameters

| Key           | Description                                 | Required | Type   | Value                     | Constraints                                |
| :------------ | :------------------------------------------ | :------- | :----- | :------------------------ | :----------------------------------------- |
| Authorization | Access Token for the application            | Required | String | \{\{PARTNER\_APP\_TOKEN}} | Should be a valid Partner App Access Token |
| appId         | App id of the app                           | Required | String | \{\{APP\_ID}}             | The Id should be a valid app ID of Gupshup |
| elementName   | element name for the template to be deleted | Required | String | \{\{ELEMENT\_NAME}}       |                                            |

### Sample Request

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/template/{{ELEMENT_NAME}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

### Sample Response

```json
     {
       "status": "success"
     }
```

### Sample Response

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
        Comment
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
        \{

        "status": "success"}
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
        \{

        "status":"error","message":"Invalid App ID"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        The provided appId is not valid.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{

        "status":"error","message":"Delete Operation is not allowed for sandbox apps"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        App is not live
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
            "status":"error",
            "message":"Please Check If App Has been approved"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        App is not approved
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
            "status":"error",
            "message":"Template Does not exists."
        }
      </td>

      <td style={{ textAlign: "left" }}>
        No template found for the provided element name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
            "status":"error",
            "message":"Template Cannot be deleted"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        Not a master template
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        400
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
            "status":"error",
            "message":"Unable to delete the template, please try after sometime and if issue still exists than contact dev support"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        Error occured while deleting template.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        403
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
            "status":"error",
            "message":"Not App Owner"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        appId provided is not associated with the provided api key.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        500
      </td>

      <td style={{ textAlign: "left" }}>
        \{          
          "status": "error",
          "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"
        }
      </td>

      <td style={{ textAlign: "left" }}>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>