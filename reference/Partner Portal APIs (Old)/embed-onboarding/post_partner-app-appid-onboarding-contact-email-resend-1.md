---
title: Resend verification link
excerpt: Use this endpoint to resend verification link.
api:
  file: onboarding-api.json
  operationId: post_partner-app-appid-onboarding-contact-email-resend
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Key           | Description                                            | Constraints                                          |
| :------------ | :----------------------------------------------------- | :--------------------------------------------------- |
| PARTNER_TOKEN | JWT Token issues post Partner login                    | Should be a valid Partner JWT Token.                 |
| appId         | appId for the app whose business email need to verify. | Should be a valid appId associated with the account. |

### Sample Request

```curl
curl --location --request POST '{{partner_portal_base_url}}/partner/app/:appId/onboarding/contact/email/ resend' \
--header 'token: {{PARTNER_TOKEN}}'
```

### Sample Response

```
{
	"status" : "success",
	"message" : "mail sent successfully"
}
```

### Status Codes

| Status Code   | Response                                                                                                                                                                                    | Comment                                                          |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| _**Success**_ |                                                                                                                                                                                             |                                                                  |
| 200           | `{ "status" : "success", "message" : "mail sent successfully" }`                                                                                                                            | Email successfully sent to the stored business contact email id. |
| _**Error**_   |                                                                                                                                                                                             |                                                                  |
| 400           | `{ "status" : "error", "message" : "Email is already Verified For This Container" }`                                                                                                        | The email id is already verified.                                |
| 400           | `{ "status" : "error", "message" : "Please set business email first" }`                                                                                                                     | Business email is not present in business information.           |
| 401           | `{ "status": "error", "message": "Authentication Failed" }`                                                                                                                                | Either appId or partner_token is incorrect.                      |
| 429           | `{ "status": "error", "message": "Too Many Requests" }`                                                                                                                                    | When the request rate limit exceeds.                             |