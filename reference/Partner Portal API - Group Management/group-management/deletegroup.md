---
title: Delete WhatsApp Group
excerpt: Deletes a WhatsApp group permanently
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: deleteGroup
hidden: true
---
# Overview

This API deletes the group and removes all participants, including the business. This action is irreversible and permanently removes the group.

# What This API Does

* Delete Groups: Permanently remove WhatsApp groups
* Cleanup Operations: Remove obsolete or unused groups
* Group Management: Manage group lifecycle
* Access Control: Ensure only authorized deletions

# Common Use Cases

* Group Cleanup: Remove inactive or obsolete groups
* Project Completion: Delete groups after project ends
* Event Conclusion: Remove event-specific groups
* Data Management: Clean up test or temporary groups
* Compliance: Delete groups as per data retention policies
* Resource Management: Free up resources by removing unused groups

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

* ⚠️ Deletion is permanent and cannot be undone
* ⚠️ Must be group admin to delete the group
* ⚠️ Group ID becomes invalid after deletion

# Request Examples

<br />

```curl
curl --location --globoff --request DELETE 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data '{
  "messaging_product": "whatsapp"
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

# Response Fields

| Fields            | Type   | Description                               |
| :---------------- | :----- | :---------------------------------------- |
| status            | String | Response status ("success" or "error")    |
| messaging_product | String | The messaging product (always "whatsapp") |
| request_id        | String | Unique identifier for this request        |

# Important Notes

* ✅ Group is deleted immediately upon successful API call
* ⚠️ This action cannot be undone
* ⚠️ Group ID becomes invalid after deletion
* ⚠️ Any pending invite links are automatically revoked

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "request_id": "REQUEST_ID", "status": "success"}`                                                          | Group deleted successfully. The group has been permanently removed and all participants have been notified. Group ID is now invalid.                                                                  |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Invalid group ID format, missing messaging_product field, or malformed request body.                                                                 |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "Group not found"}`                                                                                           | Not Found - Resource doesn't exist. Common causes: Invalid group ID, group doesn't exist, group has been deleted, or app doesn't have access to the group.                                            |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |