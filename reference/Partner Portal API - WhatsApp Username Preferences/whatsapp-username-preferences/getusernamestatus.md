---
api:
  file: partner_app_username_preferences_api_spec.json
  operationId: getUsernameStatus
hidden: true
---
## Parameters

| Parameter | Type   | Required | Discription            |
| :-------- | :----- | :------- | :--------------------- |
| appId     | String | Yes      | Partner application ID |
|           |        |          |                        |

## Headers

| Parameter     | Type   | Required | Discription                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

<br />

## Request Example

```curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username/status' \
  --header 'Authorization: {{APP_TOKEN}}' \
  --header 'Accept: application/json'
```

<br />

## Response Format

```json
{
  "status": "success",
  "data": {
    "businessPhoneNumber": "91858809xxxx",
    "usernamePreference1": "testuser",
    "submissionStatus": "SubmittedToGupshup"
  }
}
```

<br />