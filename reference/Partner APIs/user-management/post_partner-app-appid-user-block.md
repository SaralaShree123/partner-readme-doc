---
title: Block Users
excerpt: >-
  This API endpoint allows you to block one or more WhatsApp users from sending
  messages to your WhatsApp Business application. Blocked users will not be able
  to send messages, and your app will not receive any incoming messages from
  them. This is useful for preventing spam, harassment, or unwanted
  communication. Use the unblock endpoint to restore messaging for previously
  blocked users.
api:
  file: block_usersApi_openapi3.json
  operationId: post_partner-app-appid-user-block
hidden: false
---
> ℹ️ [Meta documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/block-users/)

**When you block a WhatsApp user, the following happens:**

* The user cannot contact your business or see that you are online.
* Your business cannot message the user. If you do, you will encounter an error.
* You cannot use this API to block another WhatsApp Business

Errors on the API occur per-number since blocks might be successful on some numbers and not others.

The Block Users API is synchronous.

## Request Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Value
      </th>

      <th>
        Data type
      </th>

      <th>
        Required/Optional
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorization
      </td>

      <td>
        Access Token for the application
      </td>

      <td>
        `{{PARTNER_APP_TOKEN}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td>
        appId
      </td>

      <td>
        App ID to fetch the access token
      </td>

      <td>
        `{{APP_ID}}`
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        * The Id should be a valid app Id of Gupshup.
        * The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used.
      </td>
    </tr>

    <tr>
      <td>
        messaging\_product
      </td>

      <td>

      </td>

      <td>
        whatsapp
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        Messaging service used for the request. Must be "whatsapp". [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api)  only.
      </td>
    </tr>

    <tr>
      <td>
        block\_users
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>
        Object
      </td>

      <td>
        Required
      </td>

      <td>
        List of user(s) to block.\
        Each element contains a user field.
      </td>
    </tr>

    <tr>
      <td>
        user
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>

      <td>
        The phone number or WhatsApp ID to be blocked.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/user/block' \
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
    "block_users": 
	{
        "added_users": 
		[
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

        "block\_users":

        \{"added\_users":\[\{"input": "919163805873","wa\_id": "919163805873"}]
        },
        "messaging\_product": "whatsapp",
        "status": "success"
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
        400
      </td>

      <td>
        \{

        "messaging\_product": "whatsapp",

        "block\_users": \{"added\_users": \[\{"input": "\<PHONE\_NUMBER> or \<WA\_ID>","wa\_id": "\<WA\_ID>"},\{"input": "\<PHONE\_NUMBER> or \<WA\_ID>",
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