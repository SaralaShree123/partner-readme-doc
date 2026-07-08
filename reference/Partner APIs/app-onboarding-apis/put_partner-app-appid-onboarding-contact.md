---
title: Set Contact details for an App
excerpt: Use this endpoint for Contact details.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-onboarding-contact
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Key           | Description                                                             | Constraints                              |
| :------------ | :---------------------------------------------------------------------- | :--------------------------------------- |
| appId         | AppId of the app for which business contact details need to be updated. | Should be a valid appId for the account. |
| contactEmail  | Email id to contact business.                                           | Should be a valid email id.              |
| contactName   | Contact name for business                                               | Should be a valid name for business      |
| contactNumber | Phone number to contact business                                        | Should be a valid phone number.          |

### Sample Request

```curl
curl --location --request PUT '{{partner_portal_base_url}}/partner/app/:appId/onboarding/contact' \
--header 'token: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'contactEmail=&lt;contact_email_id&gt;' \
--data-urlencode 'contactName=&lt;contact_name&gt;' \
--data-urlencode 'contactNumber=&lt;contact_phone_number&gt;'
```

### Sample Response

```
{
	"status" : "success",
	"message" : "contact details updated successfully"
}
```

### Status Codes

| Status Code   | Response                                                                                       | Comment                                                             |
| :------------ | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| _**Success**_ |                                                                                                |                                                                     |
| 200           | `{   	"status" : "success",   	"message" : "contact details updated         successfully"   }` | Successfully updated the contact details for the business.          |
| _**Error**_   |                                                                                                |                                                                     |
| 400           | `{   	"status" : "error",   	"message" : "Invalid app id provided"   }`                        | Provided appId is incorrect.                                        |
| 400           | `{   	"status" : "error",   	"message" : "Please provide valid details"   }`                   | Provided contactEmail or contactName or contactNumber is not valid. |
| 401           | `{       "status": "error",       "message": "Authentication Failed"   }`                      | Either appId or partner_token is incorrect.                         |
| 429           | `{     "status": "error",     "message": "Too Many Requests"   }`                              | When the request rate limit exceeds.                                |