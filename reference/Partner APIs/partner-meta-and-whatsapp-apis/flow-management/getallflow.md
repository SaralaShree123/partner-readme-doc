---
title: Get All Flow api
excerpt: Use this API to get a list of all flows.
api:
  file: flowAPIs-a.json
  operationId: getallflow
hidden: true
---
## Request Parameters

| Key           | Description                      | Value                     | Data type | Required/Optional | Constraints                                |
| :------------ | :------------------------------- | :------------------------ | :-------- | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application | \{\{PARTNER\_APP\_TOKEN}} | String    | Required          | Should be a valid Partner App Access Token |
| appId         | App ID to fetch the access token | \{\{APP\_ID}}             | String    | Required          | The Id should be a valid app Id of Gupshup |

## Sample Request

```curl
curl --location --request GET 'https://partner.gupshup.io/partner/app/{{APP_ID}}/flows' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json'
```

## Sample Response

```
[
    {
        "categories": [
            "APPOINTMENT_BOOKING"
        ],
        "id": "460785803057688",
        "name": "Message templates_delivery_failed_form_1_APPOINTMENT_BOOKING_93375",
        "status": "PUBLISHED",
        "validation_errors": []
    },
    {
        "categories": [
            "SIGN_UP"
        ],
        "id": "881255207342075",
        "name": "Message templates_temp_signup_form_MARKETING_e7589",
        "status": "PUBLISHED",
        "validation_errors": []
    },
    {
        "categories": [
            "SIGN_UP"
        ],
        "id": "356169917364619",
        "name": "flow_sign_up",
        "status": "PUBLISHED",
        "validation_errors": []
    }
]
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
        \[
          
            \{
                "categories": [
                    "APPOINTMENT_BOOKING"
                ],
                "id": "460785803057688",
                "name": "Message templates_delivery_failed_form_1_APPOINTMENT_BOOKING_93375",
                "status": "PUBLISHED",
                "validation_errors": []
            },
            \{
                "categories": [
                    "SIGN_UP"
                ],
                "id": "881255207342075",
                "name": "Message templates_temp_signup_form_MARKETING_e7589",
                "status": "PUBLISHED",
                "validation_errors": []
            },
            \{
                "categories": [
                    "SIGN_UP"
                ],
                "id": "356169917364619",
                "name": "flow_sign_up",
                "status": "PUBLISHED",
                "validation_errors": []
            }
        ]
      </td>

      <td>
        Get all flows associated to app ID
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
          
            "status": "error",
            "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"
        }
      </td>

      <td>
        For invalid app Id or partner app token
      </td>
    </tr>
  </tbody>
</Table>