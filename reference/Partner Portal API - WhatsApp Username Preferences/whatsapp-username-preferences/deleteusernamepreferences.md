---
api:
  file: partner_app_username_preferences_api_spec.json
  operationId: deleteUsernamePreferences
hidden: true
---
## Parameters

| Parameter | Type   | Required | Discription            |
| :-------- | :----- | :------- | :--------------------- |
| appId     | String | Yes      | Partner application ID |
|           |        |          |                        |

## Header

| Parameter     | Type   | Required | Description                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

<br />

## Request Example

```curl
curl --location --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username/preferences' \
  --header 'Authorization: {{APP_TOKEN}}' \
  --header 'Accept: application/json'
```

<br />

## Response Format

```json
{
  "status": "success",
  "message": "Username preferences deleted successfully"
}
```