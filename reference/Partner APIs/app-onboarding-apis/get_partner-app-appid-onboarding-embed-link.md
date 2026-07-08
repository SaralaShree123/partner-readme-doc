---
title: Generate Embed Signed Link
excerpt: Use this endpoint to generate the embed signed link.
api:
  file: partner-portal-public-apis.json
  operationId: get_partner-app-appid-onboarding-embed-link
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note
> 
> 1. The signed link is valid for 5 days only.

### Parameters

| Key           | Description                                              | Constraints                                          |
| :------------ | :------------------------------------------------------- | :--------------------------------------------------- |
| PARTNER_TOKEN | JWT Token issues post Partner login                      | Should be a valid Partner JWT Token.                 |
| appId         | AppId of the app for which embed link needs to generate. | Should be a valid appId associated with the account. |
| regenerate    | Boolean value specifying regeneration of the embed link. | Default value if false.                              |
| user          | User name                                                | Should be a valid username                           |
| lang          | Language                                                 | Should be a valid language supported.                |

### Sample Request

```curl
curl --location --request GET '{{partner_portal_base_url}}/partner/app/:appId/onboarding/embed/link?regenerate=<BOOLEAN_VALUE>&user=<USER_NAME>&lang=<LANGUAGE>' \
--header 'token: {{PARTNER_TOKEN}}'
```

### Sample Response

```
{
    "status": "success",
    "link" : "<embed_link>"
}
```

### Status Codes

| Status Code   | Response                                                                                                                                                      | Comment                                                                               |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| _**Success**_ |                                                                                                                                                               |                                                                                       |
| 200           | `{       "status": "success",       "link" : "<embed_link>"   }`                                                                                             | Successfully generated embed link.                                                    |
| _**Error**_   |                                                                                                                                                               |                                                                                       |
| 400           | `{       "status": "error",       "message": "Query Params cannot be empty"   }`                                                                              | Either user or lang in the query parameter is empty.                                  |
| 400           | `{       "status": "error",       "message": "Max Links Already sent,  please contact support at [devsupport@gupshup.io](mailto:devsupport@gupshup.io) "   }` | Exceeds the number of times embed links can be generated.                             |
| 400           | `{       "status": "error",       "message": "Link has expired, please regenerate link"   }`                                                                  | Existing Embed token is expired.                                                      |
| 401           | `{       "status": "error",       "message": "Authentication Failed"   }`                                                                                     | Either appId or partner_token is incorrect.                                           |
| 429           | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                             | When the request rate limit exceeds.                                                  |
| 500           | `{       "status": "error",       "message": "Unable to create link"   }`                                                                                     | Error while trying to create an Embed Link.                                           |
| 500           | `{       "status": "error",       "message": "Unable to get link"   }`                                                                                        | Error while getting embed link for the app. Try it after some time.                   |
| 500           | `{       "status": "error",       "message": "Max link already sent"   }`                                                                                     | Can only be regenerated at max 40 times or new links can be generated at max 5 times. |