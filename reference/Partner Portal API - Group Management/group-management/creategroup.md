---
title: Create WhatsApp Group
excerpt: Creates a new WhatsApp group with specified participants and settings
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: createGroup
hidden: true
---
# Overview

Use this API to create a new WhatsApp group programmatically. This API allows you to create groups with a custom name and description for your WhatsApp Business Account.

<br />

# What This API Does

* Create Groups: Create new WhatsApp groups programmatically
* Set Group Name: Define a custom subject/name for the group (up to 128 characters)
* Add Description: Optionally add a group description (up to 2048 characters)
* Automated Group Management: Create groups as part of automated workflows
* Business Operations: Set up groups for customer support, announcements, or communities

<br />

# Common Use Cases

* Customer Support: Create dedicated support groups for customers
* Community Building: Set up community groups for users with common interests
* Event Management: Create groups for event attendees
* Team Collaboration: Set up internal team communication groups
* Automated Onboarding: Create groups as part of user onboarding flows
* Broadcast Groups: Set up groups for announcements and updates

<br />

# Authentication & Authorization

* PARTNER_APP role is mandatory
* Must be authenticated with a valid PARTNER_APP_TOKEN in the header

<br />

# Request Parameters

<br />

## Path Parameters

<br />

| Parameter | Type   | Required | Description                                      | Constraints            |
| :-------- | :----- | :------- | :----------------------------------------------- | :--------------------- |
| appId     | String | Yes      | The unique identifier of the partner application | Must be a valid App ID |

<br />

## Headers

<br />

| Parameter     | Type   | Required | Description                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

<br />

## Request Body Parameters

<br />

| Parameter         | Type   | Required | Description                                 | Constraints                                       |
| :---------------- | :----- | :------- | :------------------------------------------ | :------------------------------------------------ |
| messaging_product | String | Yes      | The messaging product                       | Value must be "whatsapp"                          |
| subject           | String | Yes      | The subject/name of the group being created | Max length: 128 characters. Whitespace is trimmed |
| description       | String | No       | The description of the group                | Max length: 2048 characters. Optional field       |

<br />

# Important Constraints


⚠️ Subject is required and cannot be empty

⚠️ Maximum subject length: 128 characters

⚠️ Maximum description length: 2048 characters

⚠️ Must have a valid WhatsApp Business Account to create groups

<br />

# Request Examples

```curl
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "messaging_product": "whatsapp",
  "subject": "GROUP_NAME",
  "description": "GROUP_DESCRIPTION"
}'
```

<br />

# Response Format

```curl
{
  "messaging_product": "whatsapp",
  "request_id": "REQUEST_ID",
  "status": "success"
}
```

<br />

# Response Fields

| Fields            | Type   | Description                               |
| :---------------- | :----- | :---------------------------------------- |
| messaging_product | String | The messaging product (always "whatsapp") |
| request_id        | String | Unique identifier for this request        |
| status            | String | Response status ("success" or "error")    |

<br />

# Important Notes

* ✅ Group is created immediately upon successful API call
* ✅ The creator (business phone number) is automatically added as admin
* ✅ Group ID will be available in the response for further operations
* ⚠️ You need to add participants separately using the Add Participants API
* ⚠️ Group name and description can be updated later using Update Group API

<br />

# Response Status Codes

<br />

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                                                 |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "request_id": "REQUEST_ID", "status": "success"}`                                                          | Group created successfully. The group has been created and is ready to use. You can now add participants, create invite links, or update group settings.                                                                    |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Missing required field (subject), subject exceeds 128 characters, description exceeds 2048 characters, invalid request body structure, or invalid messaging_product value. |
| 400         | Error   | `{"status": "error", "message": "Group is not enabled for this app"}`                                                                         | Bad Request - Group feature not enabled. The group management feature is not enabled for this application. Contact support to enable group functionality for your app.                                                      |
| 400         | Error   | `{"status": "error", "message": "Feature available only for CAPI apps"}`                                                                      | Bad Request - CAPI only feature. This feature is only available for Cloud API (CAPI) applications. On-premise or other app types cannot use this functionality.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured.                       |
| 404         | Error   | `{"status": "error", "message": "App not found"}`                                                                                             | Not Found - Resource doesn't exist. Common causes: Invalid app ID, app doesn't exist, or app has been deleted.                                                                                                              |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                                      |