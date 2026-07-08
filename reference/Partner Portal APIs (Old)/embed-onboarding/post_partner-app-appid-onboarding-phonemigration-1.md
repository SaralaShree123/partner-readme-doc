---
title: Mark App for Migration
excerpt: >-
  Use this API to mark an app as migrated from another BSP to Gupshup. The flag
  indicates that this is a migration use case.
api:
  file: onboarding-api.json
  operationId: post_partner-app-appid-onboarding-phonemigration
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

| Key             | Value             | Description                                                             | Constraints                                                                                                                                      |
| :-------------- | :---------------- | :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| PARTNER_TOKEN   | `{{PARTNER_TOKEN}}` | JWT Token issues post Partner login                                     | Should be a valid Partner JWT Token.                                                                                                             |
| appId           | `{{APP_ID}}`        | AppId of the app for which business contact details need to be updated. | Should be a valid appId for the account.                                                                                                         |
| migrationStatus |                   | META_EMBED_MIGRATION / MIGRATED_IN                                      | - If the app is yet to be made live set migrationStatus as META_EMBED_MIGRATION. - If the app is already live set migrationStatus as MIGRATED_IN |

## Sample Request

```curl
curl --location --request POST '{{partner_portal_base_url}}/partner/app/:appId/onboarding/phoneMigration' \
--header 'token: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'migrationStatus=META_EMBED_MIGRATION/MIGRATED_IN' 
```

## Sample Response

```json
{
	"status": "success",
    "whatsapp": {
        "businessId": "*******",
        "countryCode": 91,
        "createdOn": 1713430478907,
        "creationStage": "DOCKER_PROVISIONING",
        "dialCode": "*****",
        "displayName": "appName",
        "embedLiveCheckTimestamp": 0,
        "embedStage": "EMBED_PHONE_SELECTION",
        "fbBusinessId": "******",
        "fbVerificationBypassed": false,
        "formattedPhoneNumber": "******",
        "goLiveProcessRequestEmailSent": false,
        "id": "<appId>",
        "lastPNDNCheckTimestamp": 0,
        "lastWABACheckTimestamp": 0,
        "migrationStatus": "META_EMBED_MIGRATION",
        "migrationTime": 1719297738982,
        "modifiedOn": 1719297738982,
        "normalizedPhoneNumber": "****",
        "pipeLineStage": "GET_CERTIFICATE",
        "pndnApprovalTimestamp": 0,
        "preferredCurrency": "INR",
        "preferredLocale": "en_US",
        "preferredTimezone": "71",
        "providedAccessToGupshup": false,
        "regionCode": "IN",
        "stageRetries": 0,
        "uiFormStage": "GO_LIVE_FLOW_SELECTED",
        "wabaApprovalTimestamp": 0,
        "whatsappVerificationStatus": "WABA_APPROVED"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Comments                                                    |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                             |
| 200         | `{   	"status": "success",       "whatsapp": {           "businessId": "**\*\*\***",           "countryCode": 91,           "createdOn": 1713430478907,           "creationStage": "DOCKER_PROVISIONING",           "dialCode": "**\***",           "displayName": "appName",           "embedLiveCheckTimestamp": 0,           "embedStage": "EMBED_PHONE_SELECTION",           "fbBusinessId": "**\*\***",           "fbVerificationBypassed": false,           "formattedPhoneNumber": "**\*\***",           "goLiveProcessRequestEmailSent": false,           "id": "<appId>",           "lastPNDNCheckTimestamp": 0,           "lastWABACheckTimestamp": 0,           "migrationStatus": "META_EMBED_MIGRATION",           "migrationTime": 1719297738982,           "modifiedOn": 1719297738982,           "normalizedPhoneNumber": "\*\*\*\*",           "pipeLineStage": "GET_CERTIFICATE",           "pndnApprovalTimestamp": 0,           "preferredCurrency": "INR",           "preferredLocale": "en_US",           "preferredTimezone": "71",           "providedAccessToGupshup": false,           "regionCode": "IN",           "stageRetries": 0,           "uiFormStage": "GO_LIVE_FLOW_SELECTED",           "wabaApprovalTimestamp": 0,           "whatsappVerificationStatus": "WABA_APPROVED"   }` | Successfully set the app for migration                      |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                             |
| 400         | `{   	"status" : "error",   	"message" : "Application not found"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Provided appId is incorrect.                                |
| 400         | `{   	"status" : "error",   	"message" : "Please provide valid details"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | migrationStatus is neither META_EMBED_MIGRATION/MIGRATED_IN |
| 401         | `{       "status": "error",       "message": "Authentication Failed"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Either appId or partner_token is incorrect.                 |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | When the request rate limit exceeds.                        | 