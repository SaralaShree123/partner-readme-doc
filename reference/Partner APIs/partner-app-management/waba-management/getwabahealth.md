---
api:
  file: Get Waba Info_OpenApi_updated_BM_limit (1).json
  operationId: getWabaHealth
hidden: false
---
# API Request

```
curl --location --request GET '{{partner_portal_base_url}}/partner/app/:appId/waba/info' \
--header 'token: {{PARTNER_APP_TOKEN}}' \
```

<br />

# API Response

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
        Success
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
        ```
        {
            "status": "success",
            "wabaInfo": {
                "accountStatus": "ACTIVE | BANNED",
                "dockerStatus": "CONNECTED | DISCONNECTED | FLAGGED | PENDING | RESTRICTED | UNKNOWN",
                "messagingLimit": "TIER_50 | TIER_250 | TIER_2K | TIER_10K | TIER_100K | TIER_NOT_SET | TIER_UNLIMITED",
                "mmLiteStatus" : "INELIGIBLE | ELIGIBLE | ONBOARDED"
                "ownershipType":"CLIENT_OWNED | ON_BEHALF_OF | SELF"
                "phone": "{phone}",
                "phoneQuality": "GREEN | YELLOW | RED | UNKNOWN",
                "throughput": "HIGH | STANDARD | NOT_APPLICABLE",
                "verifiedName":"{display name}",
                "wabaId": "{waba_id}" ,
                "canSendMessage" : "AVAILABLE | LIMITED | BLOCKED" ,
                "errors": [
                    {
                        "error_code": "141014",
                        "error_description": "<error description>",
                        "possible_solution": "<posible solution>"
                    }
                ],
                "additionalInfo": [
                    "Your display name has not been approved yet. Your message limit will increase after the display name is approved."
                ]
            }
        }
        ```
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Error
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        ```
        {
            "message": "App is not live.",
            "status": "error"
        }
        ```
      </td>

      <td>
        If app is not live
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        ```
        {
            "message": "Waba id not found for the given App",
            "status": "error"
        }
        ```
      </td>

      <td>
        If waba id is not present in DB
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        ```
        {
            "message": "WABA id is invalid or given phone is not associated with WABA",
            "status": "error"
        }
        ```
      </td>

      <td>
        If waba id present in DB is not correct
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        ```
        {
            "message": "Error while getting waba info for given app",
            "status": "error"
        }
        ```
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        ```
        {
            "message": "Authentication Failed",
            "status": "error"
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
        {
          "status": "error",
          "message": "Too Many Requests"
        }
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
        {
          "status": "error",
          "message": "Internal Server Error"
        }
        ```
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Request Params

| Key               | Description                                | Constraints                                                              |
| :---------------- | :----------------------------------------- | :----------------------------------------------------------------------- |
| Headers           |                                            |                                                                          |
| PARTNER_APP_TOKEN | App Access Token issues post Partner login | Should be a valid Partner app access token belonging to the passed appId |
| Path Params       |                                            |                                                                          |
| APP_ID            | appId of the app                           | App Id for the app that is linked to the Partner Account                 |

<br />

# Response Params

<br />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountStatus
      </td>

      <td>
        Waba account status - ACTIVE | BANNED
      </td>
    </tr>

    <tr>
      <td>
        dockerStatus
      </td>

      <td>
        Waba docker status - CONNECTED | DISCONNECTED | FLAGGED | PENDING | RESTRICTED | UNKNOWN
      </td>
    </tr>

    <tr>
      <td>
        messagingLimit
      </td>

      <td>
        messaging tier - TIER_50 | TIER_250 | TIER_2K | TIER_10K | TIER_100K | TIER_NOT_SET | TIER_UNLIMITED

        This is BM level messaging limit
      </td>
    </tr>

    <tr>
      <td>
        mmLiteStatus
      </td>

      <td>
        INELIGIBLE| ELIGIBLE| ONBOARD|INELIGIBLE_ON_BEHALF_OF_WABA | INELIGIBLE_INACTIVE_OR_RESTRICTED |INELIGIBLE_COUNTRY_NOT_SUPPORTED |INELIGIBLE_COUNTRY_NOT_SUPPORTED| PENDING_VALID_PAYMENT_METHOD |PENDING_INTERNAL_SETUP"
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        Phone number
      </td>
    </tr>

    <tr>
      <td>
        phoneQuality
      </td>

      <td>
        Phone number quality - GREEN | YELLOW | RED | UNKNOWN
      </td>
    </tr>

    <tr>
      <td>
        verifiedName
      </td>

      <td>
        Display name for the WABA
      </td>
    </tr>

    <tr>
      <td>
        wabaId
      </td>

      <td>
        Waba Id
      </td>
    </tr>

    <tr>
      <td>
        canSendMessage
      </td>

      <td>
        Message sending is allowed or not - AVAILABLE | LIMITED | BLOCKED
      </td>
    </tr>

    <tr>
      <td>
        errors
      </td>

      <td>
        ```
        {

                        "error_code": Meta Error Code,

                        "error_description": Meta Error Description,

                        "possible_solution": Suggestions on how to solve the error 

        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo
      </td>

      <td>
        Additional information associated with the waba
      </td>
    </tr>
  </tbody>
</Table>