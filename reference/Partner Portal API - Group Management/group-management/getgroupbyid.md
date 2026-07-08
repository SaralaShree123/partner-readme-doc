---
title: Get WhatsApp Group Details by Group ID
excerpt: Retrieves detailed information about a specific WhatsApp group
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: getGroupById
hidden: true
---
# Overview

API to retrieve metadata about a single group. This API returns comprehensive group details, including subject, description, participants, creation timestamp, and suspension status.

<br />

# What This API Does

* Retrieve Group Details: Get complete information about a specific group
* View Participants: Access the list of group members
* Check Group Settings: View group configuration and metadata
* Monitor Group Status: Track group information and changes
* Verify Group Existence: Confirm if a group exists and is accessible

# Common Use Cases

* Group Management: View and manage group details
* Participant Tracking: Monitor group membership
* Audit and Compliance: Track group information for records
* Integration Sync: Sync group data with external systems
* User Interface Display: Show group information in applications
* Verification: Confirm group exists before performing operations

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

## Query Parameters

| Parameter | Type   | Required | Description                              | Constraints                                                                                                                                                                       |
| :-------- | :----- | :------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fields    | String | No       | Comma-separated list of fields to return | Optional. If no fields are passed in, only the group id is returned. Available fields: subject, description, suspended, creation_timestamp, participants, total_participant_count |

<br />

# Available Fields

| Field                   | Type    | Description                                                                                         | Sample Return Value                                                                                                                |
| :---------------------- | :------ | :-------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| subject                 | String  | The subject for the group                                                                           | "Artificial Intelligence Insights"                                                                                                 |
| description             | String  | The group description, if set during creation time                                                  | "Explore AI developments, share knowledge, and discuss the future of artificial intelligence with fellow enthusiasts and experts." |
| suspended               | Boolean | Returns true if the group has been suspended by WhatsApp                                            | false                                                                                                                              |
| creation_timestamp      | Integer | UNIX timestamp in seconds at which the group was created                                            | 683731200                                                                                                                          |
| participants            | List    | A list of objects `{"wa_id": "<WA_ID>"}, where <WA_ID> `is a participant in the group being queried | `[{"wa_id": "2228675309"}, {"wa_id": "7693349922"}]`                                                                               |
| total_participant_count | Integer | The total number of participants in the group, excluding your business                              | 6                                                                                                                                  |

<br />

# Request Examples

## Get Group ID Only

```curl
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Get Specific Fields

```
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}?fields=subject,description,participants,total_participant_count' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

# Response Format

```curl
{
    "id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYxxxxxxxxxxxxx",
    "messaging_product": "whatsapp",
    "status": "success"
    }
```

```curl
{
    "description": "This is Group for gupshup",
    "id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYzNDIzxxxxxxxxxxx",
    "messaging_product": "whatsapp",
    "participants": [
        {
            "wa_id": "91738518xxxx"
        }
    ],
    "status": "success",
    "subject": "Test PP Grp",
    "total_participant_count": 1
}
```

# Response Fields

| Fields                  | Type    | Description                                                                                      |
| :---------------------- | :------ | :----------------------------------------------------------------------------------------------- |
| id                      | String  | Unique identifier of the group                                                                   |
| messaging_product       | String  | The messaging product (always "whatsapp")                                                        |
| status                  | String  | Response status ("success" or "error")                                                           |
| subject                 | String  | The subject/name of the group (only if requested in fields)                                      |
| description             | String  | Description of the group (only if requested in fields)                                           |
| suspended               | Boolean | True if the group has been suspended by WhatsApp (only if requested in fields)                   |
| participants            | Array   | List of group participants as objects with wa_id property (only if requested in fields)          |
| participants[].wa_id    | String  | WhatsApp ID of participant                                                                       |
| total_participant_count | Integer | Total number of participants in the group, excluding your business (only if requested in fields) |

# Important Notes

* ✅ If no fields parameter is provided, only the group ID is returned
* ✅ Use fields parameter to retrieve specific group information
* ✅ Multiple fields can be requested using comma-separated values
* ✅ Participant count excludes your business phone number

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "id": "GROUP_ID", "subject": "GROUP_NAME", "status": "success"}`                                           | Group details retrieved successfully. Returns complete group information including participants, settings, and metadata.                                                                              |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Invalid group ID format, malformed request, or invalid fields parameter.                                                                             |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "Group not found"}`                                                                                           | Not Found - Resource doesn't exist. Common causes: Invalid group ID, group doesn't exist, group has been deleted, or app doesn't have access to the group.                                            |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |