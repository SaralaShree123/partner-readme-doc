---
title: Update WhatsApp Group Profile
excerpt: Updates WhatsApp group profile information
api:
  file: GroupManagmentFunctionality_OpenApi.json
  operationId: updateGroupProfile
hidden: true
---
# Overview

Use this API to update WhatsApp group profile information including the group name (subject), description, and profile picture. This API allows you to keep group information current and relevant.

# What This API Does

* Update Group Name: Change the group subject/name
* Update Description: Modify group description
* Update Profile Picture: Change group profile image
* Bulk Updates: Update multiple fields in a single request
* Profile Management: Keep group information up-to-date

# Common Use Cases

* Rebranding: Update group name and image for rebranding
* Information Updates: Keep group description current
* Seasonal Changes: Update profile for seasonal campaigns
* Event Updates: Modify group info for different event phases
* Organization Changes: Reflect organizational changes in group profile
* Compliance: Update group information as per policies

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

## Form Data Parameters

| Parameter         | Type   | Required | Description                                            | Constraints                                                                                                                                              |
| :---------------- | :----- | :------- | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| messaging_product | String | Yes      | The messaging product                                  | Value must be "whatsapp"                                                                                                                                 |
| subject           | String | No       | The new subject for the group                          | Optional. Max length: 128 characters. Must not be empty if provided                                                                                      |
| description       | String | No       | The new description for the group                      | Optional. Max length: 2048 characters                                                                                                                    |
| file_type         | String | No       | MIME type of the profile picture                       | Optional. Only supports "image/jpeg"                                                                                                                     |
| file              | File   | No       | A path to an image file stored in your local directory | Optional. Group profile picture. Only supports MIME type image/jpeg. Maximum size: 5MB. Image should be square (height = width). Minimum size: 192 x 192 |

<br />

# Important Constraints

* ⚠️ At least one field must be updated (subject, description, or file)
* ⚠️ Maximum subject length: 128 characters
* ⚠️ Subject must not be empty if provided
* ⚠️ Maximum description length: 2048 characters
* ⚠️ Profile picture requirements
  * Only supports MIME type: image/jpeg
  * Maximum size: 5MB
  * Image must be square (height = width)
  * Minimum size: 192 x 192 pixels
* ⚠️ Must be group admin to update profile

# Request Examples

## Update Subject Only

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}' \
--header 'Content-Type: multipart/form-data' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'messaging_product="whatsapp"' \
--form 'subject="Updated Group Name"'
```

## Update Subject and Description

```
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}' \
--header 'Content-Type: multipart/form-data' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'messaging_product="whatsapp"' \
--form 'subject="Updated Group Name"' \
--form 'description="Updated group description with new information"'
```

<br />

## Update Profile Picture

```
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/group/{{GROUP_ID}}' \
--header 'Content-Type: multipart/form-data' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--form 'messaging_product="whatsapp"' \
--form 'file_type="image/jpeg"' \
--form 'file=@"/path/to/image.jpg"'
```

<br />

## Update All Fields

```
curl --location --request PUT 'http://localhost:8080/partner/app/a41b30f4-d202-4fdb-911e-3a8fbfbfb797/group/' \
--header 'Authorization: sk_4087b15819a34606be15483456dcf636' \
--form 'messaging_product="whatsapp"' \
--form 'subject="New Partner Group"' \
--form 'description="This Group is only for testing"' \
--form 'file_type="image/jpeg"' \
--form 'file=@"/home/rahuls/Downloads/media_3794083404147421.jpeg"'
```

<br />

# Response Format

```curl
{
    "messaging_product": "whatsapp",
    "request_id": "9B47474A35EFC2A6139B41457E4C10BB",
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

* ✅ Changes are applied immediately to the group
* ✅ All group participants see the updated information
* ✅ Update history is maintained by WhatsApp
* ✅ Can update one or multiple fields in a single request
* ✅ Profile picture must be square format (height = width)
* ✅ Minimum image dimensions: 192 x 192 pixels
* ⚠️ Must be group admin to update profile
* ⚠️ Only JPEG format is supported for profile pictures
* ⚠️ Subject must not be empty if provided

# Response Status Codes

| Status Code | Status  | Response                                                                                                                                      | Description                                                                                                                                                                                           |
| :---------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Success | `{"messaging_product": "whatsapp", "request_id": "REQUEST_ID", "status": "success"}`                                                          | Group profile updated successfully. The group information has been updated and all participants can see the changes immediately.                                                                      |
| 400         | Error   | `{"status": "error", "message": "Please review the request parameters and retry"}`                                                            | Bad Request - Invalid parameters. Common causes: No fields provided for update, subject exceeds 128 characters, description exceeds 2048 characters, invalid image format, or image size exceeds 5MB. |
| 401         | Error   | `{"status": "error", "message": "Unauthorised access to the resource. Please review request parameters and headers and retry"}`               | Unauthorized - Authentication failed. Common causes: Missing or invalid PARTNER_APP_TOKEN, expired token, or token doesn't match the app.                                                             |
| 403         | Error   | `{"status": "error", "message": "Forbidden Access"}`                                                                                          | Forbidden - Insufficient permissions. Common causes: User doesn't have permission to create groups, app doesn't have group creation privileges, or WhatsApp Business Account not properly configured. |
| 404         | Error   | `{"status": "error", "message": "Group not found"}`                                                                                           | Not Found - Resource doesn't exist. Common causes: Invalid group ID, group doesn't exist, group has been deleted, or app doesn't have access to the group.                                            |
| 500         | Error   | `{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | Internal Server Error - System issue. Common causes: Temporary service disruption, WhatsApp API unavailable, or system maintenance. Retry the request after some time.                                |