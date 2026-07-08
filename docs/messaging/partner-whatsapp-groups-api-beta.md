---
summary: Partner WhatsApp Groups API (Beta)
title: Partner WhatsApp Groups API (Beta)
deprecated: false
hidden: true
metadata:
  robots: index
---
# Overview

The WhatsApp Groups API allows partners to manage WhatsApp Groups programmatically throughout their lifecycle — from creation to participant management and deletion.

When a new group is created, an invite link is automatically generated, which can be used to onboard participants.

<Callout icon="⚠️" theme="warn">
  This feature is currently in Beta. Please set expectations accordingly when enabling it for customers.
</Callout>

<Callout icon="ℹ️" theme="info">
  For any questions, clarifications, or issues related to this feature, do not raise a support ticket with Partner Support.
  Instead, please reach out to: [aig.product@gupshup.io](mailto:aig.product@gupshup.io)
</Callout>

Before using the Groups APIs, you must configure Webhooks to receive group-related events.

# Subscribing to Events

Use the <Anchor label="Subscribe to Events API" target="_blank" href="https://partner-docs.gupshup.io/reference/setsubscription-api-v3">Subscribe to Events API</Anchor> to enable webhook notifications.

When working with WhatsApp Groups, there are two types of webhook events:

## 1. Group Account Events

Subscription version must be set to v3

**Mode:** `GROUP_ACCOUNT_EVENTS`

This will notify you about account-level group updates such as:

* `group_lifecycle_update ` - Triggered when a group is created, updated, or deleted.
* `group_participants_update ` - Triggered when a participant is added to or removed from a group.

## 2. Group Messaging Events

Subscription version must be set to v3

**Mode:** `GROUP_MESSAGING_EVENTS`

This will notify you about: Sent, Delivered, Read Receipts, Failed messages events.

Check the list of Sample Events <Anchor label="here" target="_blank" href="https://partner-docs.gupshup.io/docs/whatsapp-groups-sample-events">here</Anchor>.

# Getting Started with Groups Creation and Genrating Groups Invite

Follow the steps below to start managing WhatsApp Groups.

## Step 1: Create a Group

Use the <Anchor label="Create Group API" target="_blank" href="https://partner-docs.gupshup.io/reference/creategroup">Create Group API</Anchor> to create a new WhatsApp group.

Once the group is created: A Group ID is generated.

## Step 2: Retrieve the Group ID

Use the <Anchor label="Get All Groups API" target="_blank" href="https://partner-docs.gupshup.io/reference/getallgroups">Get All Groups API</Anchor> to fetch the list of active groups and retrieve the groupId.

This API will give all the groups create for the app

## Step 3: Generate or Access the Invite Link

Use the <Anchor label="Create Invite Link API" target="_blank" href="https://partner-docs.gupshup.io/reference/creategroupinvitelink">Create Invite Link API</Anchor> to invite users

**The invite link will be returned via:**

1. In the API response
2. Through Webhook events

You can now share this link with users so they can join the group.

# Additional Group Management APIs

The following APIs help automate and manage the group lifecycle:

* [Get Groups by ID](https://partner-docs.gupshup.io/reference/getgroupbyid) – Retrieve the group details by Group ID
* <Anchor label="Update Group Details" target="_blank" href="https://partner-docs.gupshup.io/reference/updategroupprofile">Update Group Details</Anchor> - Update a group name or descirption
* <Anchor label="Delete Group" target="_blank" href="https://partner-docs.gupshup.io/reference/deletegroup">Delete Group</Anchor> – Permanently delete a group
* [Remove Group Participants](https://partner-docs.gupshup.io/reference/removegroupparticipants) – Remove one or more users from a group

These APIs allow full control over group operations and help streamline automation workflows.

# Sending Message to Groups

Now let start sending messages in Groups.

Group messaging allows multiple users to communicate simultaneously within a single conversation.

**Supported message types: Text, media, text-based templates, and media-based templates**

## Example Text Message :

In the to parameter just keep the `Group ID` rather than the user phone number.

```curl Send Text Group Message
curl --location 'https:partner.gupshup.io/partner/app/{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data '{
    "messaging_product": "whatsapp",
    "recipient_type": "group",
    "to": "{{GROUP_ID}}",
    "type": "text",
    "text": {
        "body": "<Text>"
    }
}'
```

The type parameter would change according to which message is to be sent i.e. text, interactive and template

<br />
