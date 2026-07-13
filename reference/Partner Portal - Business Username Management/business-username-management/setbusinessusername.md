---
api:
  file: username_management_apis.json
  operationId: setBusinessUsername
hidden: true
---
## Sample Request:

```
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=<USERNAME>' \
--data-urlencode 'transfer_action=none'
```

<br />

## Sample Response:

```
{
  "status": "reserved"
}
```

<br />

| Key              | Description                      | Value                                     |
| :--------------- | :------------------------------- | :---------------------------------------- |
| Authorization    | Access token for the application | sk\_\*\*\*\*\*                            |
| Content-Type     | Request media type               | application/x-www-form-urlencoded         |
| APP\_ID          | App ID (path param)              | e.g. 04e6c66b-bb95-4bfc-b75e-4e7391ddc680 |
| username         | Desired business username        | e.g. mybusiness                           |
| transfer\_action | Username transfer action         | none, force\_transfer                     |

<br />
