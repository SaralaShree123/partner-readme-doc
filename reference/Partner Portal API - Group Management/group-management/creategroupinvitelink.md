---
title: Create WhatsApp Group Invite Link
excerpt: Creates a new invite link for a WhatsApp group
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: createGroupInviteLink
hidden: true
---
# Overview

Use these curl to create a new group invite link. The invite link allows users to join the group by clicking on the generated link.

# What This API Does

* Generate Invite Links: Create new invite links for WhatsApp groups
* Group Access Control: Manage group membership through invite links
* Link Management: Generate fresh links when needed
* Secure Invitations: Create controlled access to group conversations
* Scalable Invites: Share group access with multiple users efficiently

# Common Use Cases

* Community Building: Create invite links for community groups
* Customer Support: Generate links for support group access
* Event Management: Share group links for event participants
* Team Collaboration: Create links for team communication groups
* Marketing Campaigns: Generate links for promotional group access

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

| Parameter         | Type   | Required | Description           | Constraints              |
| :---------------- | :----- | :------- | :-------------------- | :----------------------- |
| messaging_product | String | Yes      | The messaging product | Value must be "whatsapp" |

# Important Constraints

* ⚠️ Must be group admin to create invite links
* ⚠️ Links remain valid until explicitly revoked
* ⚠️ Invite link always begins with [https://chat.whatsapp.com/](https://chat.whatsapp.com/)
* ⚠️ Only the LINK_ID suffix varies in the generated link

# Request Examples

```curl
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}/invite_link' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "messaging_product": "whatsapp"
}'
```

# Response Format

```curl
{
    "invite_link": "https://chat.whatsapp.com/GLGbF3MJVT10PRzma4xxxx",
    "messaging_product": "whatsapp",
    "status": "success"
}
```

# Response Fields

| Fields            | Type   | Description                                                                                                                                                                              |
| :---------------- | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| invite_link       | String | The generated invite link. Note that invite_link always begins with the prefix [https://chat.whatsapp.com/](https://chat.whatsapp.com/). The only variable portion is the LINK_ID suffix |
| messaging_product | String | The messaging product (always "whatsapp")                                                                                                                                                |
| status            | String | Response status ("success" or "error")                                                                                                                                                   |

# Important Notes

* ✅ The invite link always begins with the prefix [https://chat.whatsapp.com/](https://chat.whatsapp.com/)
* ✅ The only variable portion is the LINK_ID suffix
* ✅ Links can be shared via any channel (email, SMS, web, etc.)
* ✅ Users clicking the link will be prompted to join the group
* ⚠️ Links remain valid until explicitly revoked
* ⚠️ Group admins can revoke links at any time

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"invite_link": "https://chat.whatsapp.com/LINK_ID", "messaging_product": "whatsapp", "status": "success"}`                                  | Invite link created successfully. Returns the generated invite link that can be shared with users to join the group.                                                                                  |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Invalid request body format, missing required parameters, or invalid group ID format.                                                                |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "Group not found"}`                                                                                           | Not Found - Resource doesn't exist. Common causes: Invalid group ID, group doesn't exist, group has been deleted, or app doesn't have access to the group.                                            |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |