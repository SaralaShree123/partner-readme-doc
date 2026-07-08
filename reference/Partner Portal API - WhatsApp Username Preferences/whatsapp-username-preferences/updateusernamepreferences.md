---
api:
  file: partner_app_username_preferences_api_spec.json
  operationId: updateUsernamePreferences
hidden: true
---
## Request Parameters

<br />

| Parameters          | Type   | Required | Description                   |
| :------------------ | :----- | :------- | :---------------------------- |
| appId               | String | Yes      | Partner application ID        |
| usernamePreference1 | String | Yes      | Primary username preference   |
| usernamePreference2 | String | No       | Secondary username preference |
| usernamePreference3 | String | No       | Tertiary username preference  |

<br />

| Parameter     | Type   | Required | Description                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

<br />

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/username/preferences' \
  --header 'Authorization: {{APP_TOKEN}}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'usernamePreference1=mybrand' \
  --data-urlencode 'usernamePreference2=mybrand2' \
  --data-urlencode 'usernamePreference3=mybrand3'
```

<br />

## Response Format

```json
{
  "status": "success",
  "message": "Username preferences submitted successfully",
  "data": {
    "businessPhoneNumber": "91858809xxxx",
    "usernamePreference1": "testuser",
    "submissionStatus": "SubmittedToGupshup"
  }
}
```