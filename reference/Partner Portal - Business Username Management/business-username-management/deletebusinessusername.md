---
api:
  file: username_management_apis.json
  operationId: deleteBusinessUsername
hidden: false
---
## Sample Request:

```
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

## Sample Response:

```
{
  "status": "success"
}
```

<br />

<br />

| Key           | Description                      | Value                                     |
| :------------ | :------------------------------- | :---------------------------------------- |
| Authorization | Access token for the application | sk\_\*\*\*                                |
| APP\_ID       | App ID (path param)              | e.g. 04e6c66b-bb95-4bfc-b75e-4e7391ddc680 |

<br />
