---
summary: >-
title: Partner Customer Migration to Partner Customer Portal (PCP)
excerpt: >-
  ## Overview  This guide explains how partners can migrate their existing apps
  from the Partner Portal / Self-Serve account to the new Partner Customer
  Portal (PCP) using the Migration API.
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

# Using this API, partners can:

* Migrate existing customer apps into PCP
* Automatically create PCP organizations
* Automatically create projects for migrated apps
* Centrally manage all apps from PCP using a single login

***

# How Migration Works

Once the migration API is triggered:

1. A PCP Organization is created for the provided customer ID
2. A PCP customer account is created
3. An invitation email is sent to the provided email address
4. Projects are automatically created for all apps linked to the customer ID

***

# Important Prerequisites

## Who Can Perform Migration?

Only:

* Partner Portal Owner
* Partner Portal Admin

can perform the migration.

***

# API Endpoint

```bash
POST https://partner.gupshup.io/partner/account/api/customer/migrate/pcp
```

***

# Request Headers

| Header          | Description                                 |
| --------------- | ------------------------------------------- |
| `Content-Type`  | Must be `application/x-www-form-urlencoded` |
| `Authorization` | Partner authentication token                |

***

# API Parameters

## 1. customerId

```bash
customerId=4000188031
```

### Description

Existing customer ID that contains the apps which need to be migrated into PCP.

### Purpose

* Identifies the customer account
* Migrates all apps linked to this customer ID
* Creates projects for all associated apps

### Example

```bash
customerId=4000188031
```

***

## 2. email

```bash
email=partneradmin@example.com
```

### Description

Email address of the Partner Admin / Owner.

### Purpose

* PCP invitation email is sent to this email address
* This email becomes the PCP login email

### Important

* Only admin/owner email should be used
* Same organization will not receive multiple invites

### Example

```bash
email=partneradmin@example.com
```

***

## 3. firstName

```bash
firstName=John
```

### Description

First name of the PCP account user.

### Purpose

Used during PCP account creation.

### Example

```bash
firstName=John
```

***

## 4. lastName

```bash
lastName=Doe
```

### Description

Last name of the PCP account user.

### Purpose

Used during PCP account creation.

### Example

```bash
lastName=Doe
```

***

## 5. orgName

```bash
orgName=ExampleOrg
```

### Description

Name of the PCP organization that will be created.

### Purpose

* Creates organization inside PCP
* Groups all migrated apps under the same organization

### Example

```bash
orgName=ExampleOrg
```

***

## 6. country

```bash
country=IN
```

### Description

Country code of the organization/customer.

### Purpose

Used for:

* Region mapping
* PCP organization setup
* Localization

### Supported Examples

| Country       | Code |
| ------------- | ---- |
| India         | IN   |
| United States | US   |
| Brazil        | BR   |
| Turkey        | TR   |

### Example

```bash
country=IN
```

<Callout icon="❗️">
  Please use the Country Name if the country code does not work or returns an error. 
</Callout>

***

## 7. isPartnerAccount

```bash
isPartnerAccount=true
```

### Description

Indicates whether the customer ID belongs to the partner account.

### Purpose

Used when:

* Wallet is managed from Partner Portal
* Customer ID belongs to the partner itself

### Values

| Value   | Meaning                         |
| ------- | ------------------------------- |
| `true`  | Customer ID belongs to partner  |
| `false` | Customer ID belongs to customer |

### Important

If:

* Customer ID is owned by partner
* Wallet is managed from Partner Portal

Then:

* `isPartnerAccount=true`
* Email must be Partner Admin email

### Example

```bash
isPartnerAccount=true
```

***

# Complete API Example

```bash
curl --location --request POST \
'https://partner.gupshup.io/partner/account/api/customer/migrate/pcp' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: <Partner_Token>' \
--data-urlencode 'customerId=4000188031' \
--data-urlencode 'email=partneradmin@example.com' \
--data-urlencode 'firstName=John' \
--data-urlencode 'lastName=Doe' \
--data-urlencode 'orgName=ExampleOrg' \
--data-urlencode 'country=IN' \
--data-urlencode 'isPartnerAccount=true'
```

***

# Step-by-Step Migration Process

## Step 1 — Trigger Migration API

Partner Admin/Owner calls the migration API with:

* Existing customer ID
* Admin email
* Organization details
* Country
* Partner account flag

***

## Step 2 — Invitation Email

After successful API execution:

* PCP invitation email is sent
* Email is sent to the provided admin email address

***

## Step 3 — Create Password

Partner must:

1. Open invitation email
2. Click activation link
3. Create password

***

## Step 4 — Login to PCP

After password setup:

* Partner can log in to PCP
* Existing customer ID will be available
* Existing apps will be visible
* Projects for apps will already be created

***

# What Gets Migrated?

The migration automatically creates:

| Component        | Migration Behavior        |
| ---------------- | ------------------------- |
| Customer Account | Created in PCP            |
| Organization     | Created in PCP            |
| Existing Apps    | Migrated                  |
| Projects         | Auto-created for each app |
| User Access      | Created via invite email  |

***

# Post Migration

After successful migration, partners can:

* Manage apps from PCP
* Manage projects
* Access organization-level settings
* Use same credentials for all apps under same organization

***

# Important Notes

## Organization-Level Invitation

Invitation is organization-based.

This means:

* Only one invite is sent per organization
* Multiple apps under same organization do not trigger multiple invites

***

## Single Credential Access

Partners can manage:

* All apps
* All projects

using:

* Same PCP account
* Same credentials

***

## New Organization Scenario

If a new organization is created:

* A new invite email is triggered
* New PCP credentials can be created

***

# Summary

Using the Migration API, partners can:

* Seamlessly migrate existing apps to PCP
* Automatically create PCP organizations and projects
* Manage all apps centrally using a single PCP account
* Reuse same credentials across all apps under same organization
* Track migration status through internal migration trackingUsing this API, partners can:
* Migrate existing customer apps into PCP
* Automatically create PCP organizations
* Automatically create projects for migrated apps
* Centrally manage all apps from PCP using a single login
  <br />
  ***
  <br />
