---
title: Subscribe Event
api:
  file: 1enable-voice-v3-subscription.json
  operationId: subscribeIncomingEvent
hidden: true
---
## Request Parameters

| Key           | Description                      | Value                   | Data type | Required/Optional | Constraints                                |
| :------------ | :------------------------------- | :---------------------- | :-------- | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String    | Required          | Should be a valid Partner App Access Token |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/<APP_ID>/subscription' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: <PARTNER_APP_TOKEN>\
--data-urlencode 'modes=VOICE' \
--data-urlencode 'tag=Deep V3 Subscriptions' \
--data-urlencode 'showOnUI=false' \
--data-urlencode 'version=3' \
--data-urlencode 'url=<CALLBACK_URL>'
```

## Sample Response

```
{
    "status": "success",
    "subscription": 
	{
        "active": true,
        "appId": "b6016edd-12fb-4da1-8e96-e5bb634e271f",
        "createdOn": 1737717686910,
        "id": "30190",
        "mode": 1631,
        "modifiedOn": 1737717686910,
        "showOnUI": false,
        "tag": "Deep V3 Subscriptionss",
        "url": "https://webhook.site/0872e993-f7f1-434d-8c05-45a98ce1b42e",
        "version": 3
    }
}
```

<br />

## Status Codes

<Table align={["left","left","left","left"]}>
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

      <th>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{

        "status": "success","subscription":\{"active": true,
        "appId": "b6016edd-12fb-4da1-8e96-e5bb634e271f",
        "createdOn": 1737717686910,
        "id": "30190",
        "mode": 1631,
        "modifiedOn": 1737717686910,
        "showOnUI": false,
        "tag": "Deep V3 Subscriptionss",
        "url": "[https://webhook.site/0872e993-f7f1-434d-8c05-45a98ce1b42e](https://webhook.site/0872e993-f7f1-434d-8c05-45a98ce1b42e)",
        "version": 3
        }
        }
      </td>

      <td>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error",\
        "message": "Maximum of 5 subscriptions are allowed per app."
        }
      </td>

      <td>
        When API key authentication fails
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

        "status": "error",\
        "message": "Whatsapp voice subscription already exists"
        }
      </td>

      <td>
        When voice subscription already exists
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
        "message": "Authentication Failed"
        "status": "error",
        }
      </td>

      <td>
        When API key authentication fails
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>