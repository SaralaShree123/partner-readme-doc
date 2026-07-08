---
title: Remove WhatsApp Group Participants
excerpt: Removes one or more participants from a WhatsApp group
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: removeGroupParticipants
hidden: true
---
# Overview

Use this API to remove participants from a WhatsApp group. You can remove up to 8 participants in a single request.

# What This API Does

* Remove Members: Remove participants from WhatsApp groups
* Batch Removal: Remove multiple participants (up to 8) in one request
* Access Control: Manage group membership programmatically
* Admin Operations: Perform admin-level group management tasks
* Member Management: Control who stays in your groups

# Common Use Cases

* Moderation: Remove users who violate group rules
* Access Revocation: Remove users who no longer need access
* Automated Management: Remove inactive or expired members
* Cleanup: Remove test accounts or temporary members
* Security: Remove compromised or suspicious accounts

# Authentication & Authorization

* PARTNER_APP role is mandatory
* Must be authenticated with valid PARTNER_APP_TOKEN in the header

# Request Parameters

## Path Parameters

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Type
      </th>

      <th>
        Required
      </th>

      <th>
        Description
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        appId
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        The unique identifier of the partner application
      </td>

      <td>
        Must be a valid App ID
      </td>
    </tr>

    <tr>
      <td>
        groupId
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        The unique identifier of the WhatsApp group
      </td>

      <td>
        Must be a valid Group ID.

        You can obtain the Group ID from the create group webhook event.
        refer sample webook event
        link
      </td>
    </tr>
  </tbody>
</Table>

## Headers

| Parameter     | Type   | Required | Description                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

## Request Body Parameters

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Type
      </th>

      <th>
        Required
      </th>

      <th>
        Description
      </th>

      <th>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        messaging_product
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        The messaging product
      </td>

      <td>
        Value must be "whatsapp"
      </td>
    </tr>

    <tr>
      <td>
        participants
      </td>

      <td>
        Array
      </td>

      <td>
        Yes
      </td>

      <td>
        Specifies an array of phone number or WhatsApp ID of WhatsApp accounts
      </td>

      <td>
        Maximum of 8 participants allowed in the group.

        The array for participants cannot be empty.

        The business phone number that creates the group is automatically added as the creator and admin.
      </td>
    </tr>

    <tr>
      <td>
        participants[].user
      </td>

      <td>
        String
      </td>

      <td>
        Yes
      </td>

      <td>
        Phone number or WhatsApp ID
      </td>

      <td>
        Valid `<PHONE_NUMBER> or <WA_ID>`
      </td>
    </tr>
  </tbody>
</Table>

# Important Constraints

* ⚠️ Maximum 8 participants can be removed in a single request
* ⚠️ Participants array cannot be empty
* ⚠️ Cannot remove the group creator (business phone number used to create the group)
* ⚠️ Must be a group admin to remove participants

# Request Examples

## Remove Single Participant

```curl
curl --location --globoff --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}/participants' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "messaging_product": "whatsapp",
  "participants": [
    { "user": "<PHONE_NUMBER> or <WA_ID>" }
  ]
}'

```

<br />

## Remove Multiple Participants

```
curl --location --globoff --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}/participants' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "messaging_product": "whatsapp",
  "participants": [
    { "user": "<PHONE_NUMBER> or <WA_ID>" },
    { "user": "<PHONE_NUMBER> or <WA_ID>" }
  ]
}'

```

<br />

# Response Format

```curl
{
    "messaging_product": "whatsapp",
    "request_id": "62430A9835614621494B3485C7BA53B0",
    "status": "success"
}
```

# Response Fields

| Fields            | Type   | Description                               |
| :---------------- | :----- | :---------------------------------------- |
| status            | String | Response status ("success" or "error")    |
| messaging_product | String | The messaging product (always "whatsapp") |
| request_id        | String | Unique identifier for this request        |

# Important Notes

* ✅ Participants are removed immediately
* ✅ Removed participants can rejoin if they have an invite link
* ✅ Removed participants will not receive group messages
* ⚠️ Cannot remove the group creator
* ⚠️ Must be a group admin to remove participants
* ⚠️ Removed participants are notified about the removal

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "request_id": "REQUEST_ID", "status": "success"}`                                                          | Participants removed successfully. The specified participants have been removed from the group immediately.                                                                                           |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Empty participants array, more than 8 participants in request, invalid phone number format, or invalid request body structure.                       |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "Group not found"}`                                                                                           | Not Found - Resource doesn't exist. Common causes: Invalid group ID, group doesn't exist, group has been deleted, or app doesn't have access to the group.                                            |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |