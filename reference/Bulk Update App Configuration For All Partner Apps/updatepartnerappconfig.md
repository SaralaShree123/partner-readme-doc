---
api:
  file: partner_apps_config_update_api.json
  operationId: updatePartnerAppConfig
hidden: true
---
## Parameters

<br />

| Parameter | Type    | Required | Description                                   |
| :-------- | :------ | :------- | :-------------------------------------------- |
| partnerId | Integer | Yes      | Partner ID (must match authenticated partner) |

## Request Body

```json
{
  "enableBSUIDV3": <true/false>
}
```

## &#x20; Sample Request 

```curl
curl -X PUT 'https://partner.gupshup.io/partner/account/apps/config?partnerId={{PARTNER_ID}}' \
  -H 'Authorization: {PARTNER_JWT}' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{"enableBSUIDV3": true}'
```

## &#x20; Response Example

```json
{
  "status": "success",
  "message": "App config update queued for partner 4826. A summary will be emailed to the partner admin when processing completes.",
  "partnerId": "48xx",
  "totalApps": "221"
}
```

<br />