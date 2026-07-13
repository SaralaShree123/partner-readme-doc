---
api:
  file: username_management_apis.json
  operationId: getBusinessUsernameSuggestions
hidden: true
---
## Sample Request:

```
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username/suggestions' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

##

```
{
  "username_suggestions": [
    "gupshup",
    "journeybuilderflowsp",
    "k8sautomation",
    "newapril05",
    "convomatetestqa",
    "qa_cdp_gg",
    "gupshupctm",
    "shashwatgupshuptest"
  ]
}
```

<br />

<br />

| Key           | Description                      | Values                                    |
| :------------ | :------------------------------- | :---------------------------------------- |
| Authorization | Access token for the application | sk\_\*\*\*\*                              |
| APP\_ID       | App ID (path param)              | e.g. 04e6c66b-bb95-4bfc-b75e-4e7391ddc680 |

<br />
