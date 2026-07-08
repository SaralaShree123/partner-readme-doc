---
title: Unblock Users
excerpt: >-
  This API endpoint allows you to unblock one or more WhatsApp users who were
  previously blocked from sending messages to your WhatsApp Business
  application. Unblocking restores messaging capabilities, allowing users to
  send messages again and your app to receive messages from them. This reverses
  the effect of the block operation.
api:
  file: block_usersApi_openapi3.json
  operationId: post_partner-app-appid-user-unblock
hidden: true
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
        App ID to fetch the access token
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
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        messaging\_product
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        whatsapp
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Messaging service used for the request. Must be "whatsapp". [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api)  only.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        block\_users
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Object
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        List of user(s) to block.\
        Each element contains a user field.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        user
      </td>

      <td style={{ textAlign: "left" }}>

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
        The phone number or WhatsApp ID to be blocked.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/user/unblock' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
    "messaging_product": "whatsapp",
    "block_users": [
        {
            "user": "<PHONE_NUMBER>"
        }
    ]
}'
```

## Sample Response

```
{
    "block_users": {
        "removed_users": [
            {
                "input": "919163805873",
                "wa_id": "919163805873"
            }
        ]
    },
    "messaging_product": "whatsapp",
    "status": "success"
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

        "block\_users":\{"removed\_users":\[\{
        "input": "919163805873",
        "wa\_id": "919163805873"
        }
        ]
        },
        "messaging\_product": "whatsapp",
        "status": "success"
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
        400
      </td>

      <td>
        \{

        "messaging\_product": "whatsapp",

        "block\_users": \{
        "added\_users": \[
        \{
        "input": "\<PHONE\_NUMBER> or \<WA\_ID>",
        "wa\_id": "\<WA\_ID>"
        },
        \{
        "input": "\<PHONE\_NUMBER> or \<WA\_ID>",
        "wa\_id": "\<WA\_ID>"
        },
        ...
        ],
        "failed\_users": \[
        \{
        "input": "\<PHONE\_NUMBER> or \<WA\_ID>",
        "wa\_id": "\<WA\_ID>"
        },
        \{
        "input": "\<PHONE\_NUMBER> or \<WA\_ID>",
        "wa\_id": "\<WA\_ID>"
        },
        ...
        "errors": \[\{
        "message": "\<MESSAGE>",
        "code": "\<CODE>",
        "error\_data": \{
        "details": "\<DETAILS>""
        }]
        }
        }
        ]
        },
        "error": \{
        "message": "(#139100) Failed to block/unblock users",
        "type": "OAuthException",
        "code": 139100,
        "error\_data": \{
        "details": "Failed to block some users, see the block\_users response list for details"
        },
        "fbtrace\_id": "\<FBTRACE\_ID>"
        }
        }
        }
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>