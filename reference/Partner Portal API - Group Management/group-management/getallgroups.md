---
title: Get All Active WhatsApp Groups
excerpt: Retrieves a paginated list of all active WhatsApp groups
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: getAllGroups
hidden: true
---
# Overview

API to retrieve a list of active groups for a given app. This API supports cursor-based pagination to handle large numbers of groups efficiently.

<br />

# What This API Does

* List All Groups: Retrieve all active groups for your account
* Pagination Support: Handle large group lists with cursor-based pagination
* Bulk Retrieval: Get multiple groups in a single request
* Group Discovery: Find all groups managed by your application
* Monitoring: Track all groups across your organization

<br />

# Common Use Cases

* Dashboard Display: Show all groups in admin dashboards
* Group Management: List groups for bulk operations
* Reporting: Generate reports on group usage
* Audit and Compliance: Track all groups for compliance purposes
* Synchronization: Sync group data with external systems
* Analytics: Analyze group distribution and usage patterns

<br />

# Authentication & Authorization

* PARTNER_APP role is mandatory
* Must be authenticated with valid PARTNER_APP_TOKEN in the header

<br />

<br />

# Request Parameters

## Path Parameters

| Parameter | Type   | Required | Description                                      | Constraints            |
| :-------- | :----- | :------- | :----------------------------------------------- | :--------------------- |
| appId     | String | Yes      | The unique identifier of the partner application | Must be a valid App ID |

## Headers

| Parameter     | Type   | Required | Description                      |
| :------------ | :----- | :------- | :------------------------------- |
| Authorization | String | Yes      | Partner app authentication token |

## Query Parameters

| Parameter | Type    | Required | Description                                           | Constraints                                                   |
| :-------- | :------ | :------- | :---------------------------------------------------- | :------------------------------------------------------------ |
| limit     | Integer | No       | Number of groups to fetch in the request              | Min: 1, Default: 25, Max: 1024                                |
| after     | String  | Yes      | Cursor that points to the beginning of a page of data | Use the cursor from previous response for forward pagination  |
| before    | String  | No       | Cursor that points to the beginning of a page of data | Use the cursor from previous response for backward pagination |

<br />

# Pagination Notes

* Use limit to control the number of results per page
* Use after cursor to get the next page of results
* Use before cursor to get the previous page of results
* Cursors are provided in the response for pagination
* Cannot use both after and before in the same request

<br />

# Request Examples

<br />

## Get First Page (Default)

```curl
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

## With Custom Limit

```
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group?limit=100' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'

```

<br />

## Next Page (Forward Pagination)

```
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group?limit=25&after={{AFTER_CURSOR}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

<br />

## Previous Page (Backward Pagination)

```
curl --location --globoff 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group?limit=25&before={{BEFORE_CURSOR}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'

```

<br />

# Response Format

```curl
{
    "data": [
        {
            "creation_timestamp": 1761886978,
            "id": "Y2FwaV9ncm91cDo5MTg5Mjk4NzQyNzg6MTIwMzYzNDIzMTQ4MDkxNzE2",
            "subject": "Test PP Grp"
        }
    ],
    "paging": {
        "cursors": {
            "after": "eyJvZAmZAzZAXQiOjAsInZAlcnNpb25JZACI6IjE3NjE4ODk4MDUxNDk1Nzg2NDkifQZDZD",
            "before": "eyJvZAmZAzZAXQiOjAsInZAlcnNpb25JZACI6IjE3NjE4ODk4MDUxNDk1Nzg2NDkifQZDZD"
        }
    },
    "status": "success"
}
```

<br />

<br />

# Response Fields

| Fields                    | Type    | Description                                              |
| :------------------------ | :------ | :------------------------------------------------------- |
| data                      | Array   | Array of group objects                                   |
| data[].creation_timestamp | Integer | UNIX timestamp in seconds at which the group was created |
| data[].id                 | String  | Unique identifier of the group                           |
| data[].subject            | String  | Name/subject of the group                                |
| paging                    | Object  | Pagination information                                   |
| paging.cursors            | Object  | Cursor objects for pagination                            |
| paging.cursors.after      | String  | Cursor for next page (forward pagination)                |
| paging.cursors.before     | String  | Cursor for previous page (backward pagination)           |
| paging.next               | String  | Full URL for next page of results (if available)         |
| status                    | String  | Response status ("success" or "error")                   |

# Important Notes

* ✅ Returns paginated list of all active groups for the given app
* ✅ Default limit is 25 groups per page
* ✅ Minimum limit is 1, maximum limit is 1024 groups per page
* ✅ Use after cursor for forward pagination (next page)
* ✅ Use before cursor for backward pagination (previous page)
* ✅ Each group includes creation timestamp, ID, and subject
* ⚠️ Only returns groups accessible to your application
* ⚠️ Deleted or suspended groups are not included in the response
* ⚠️ The next URL is only provided when more pages are available

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "data": [...], "status": "success"}`                                                                       | Groups retrieved successfully. Returns paginated list of all active groups with pagination cursors for navigation.                                                                                    |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: Invalid limit value (exceeds 100), both after and before cursors provided, or malformed pagination cursor.                                           |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "App not found"}`                                                                                             | Not Found - Resource doesn't exist. Common causes: Invalid app ID, app doesn't exist, or app has been deleted.                                                                                        |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |