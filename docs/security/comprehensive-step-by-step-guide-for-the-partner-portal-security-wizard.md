---
summary: >-
title: Comprehensive Step-by-Step Guide for the Partner Portal Security Wizard
excerpt: >-
  This document helps a partner with steps to follow and prerequisites to keep
  in mind, once the security wizard is enabled for them on partner portal. The
  security wizard will help them make their Gupshup platforms secure and safe.
deprecated: false
hidden: true
metadata:
  robots: index
---
# STEPS OVERVIEW

The major steps in the wizard include the below -

First 3 steps will keep the partner portal inaccessible for all partner portal users, till they are completed -

1. **Mandatory password reset** of all Partner Portal users
2. **Mandatory MFA set via authenticator** of all Partner portal users
3. [MINOR CHANGE NEEDED IN YOUR SYSTEMS] **Mandatory migration of partner token generation method** - from username/password you move to client secret.

Developers must set/reset client secret as per desired expiry (recommended : 3 months).

Non-developers must set/reset client secret for immediate expiry.

Admin can get the visibility of their partner portal users activities on above steps to guide them further. They must revoke users too if the users will no longer be working on Gupshup partner portal.

From next step onwards, the partner portal becomes accessible again. Below steps 4, 5 and 6 are only applicable for the admin- recommended to finish at the earliest.

4. **Submitting a public key** to Gupshup followed by JWT test
5. [DISRUPTIVE] **Bulk Account level API key rotation** for all linked apps
6. [DISRUPTIVE] **Bulk App level API key & partner app token rotation** for all linked apps

<br />

In parallel from 1st step, below steps will also be required in gupshup.ai before the gupshup.ai portal can be used further.

7. **Mandatory password reset** of all linked gupshup.ai accounts
8. **Mandatory MFA set via authenticator** of all linked gupshup.ai accounts

<br />

<br />

# PRE-REQUISITES

To ensure a successful transition through the Security Wizard, all users must satisfy the following prerequisites:

1. Possession of a dedicated mobile device equipped with a recognized authenticator application (e.g., Google Authenticator or Microsoft Authenticator) to facilitate Multi-Factor Authentication (MFA) setup - on Partner Portal and Gupshup.ai
2. Completion of a mandatory password reset in accordance with updated security protocols.
3. Acknowledgment of access restrictions: Access to the Partner Portal shall remain suspended until the mandatory MFA, Password Reset, and Client Secret configuration steps are finalized.
4. Access to the Gupshup.ai shall remain suspended until the mandatory MFA and Password Reset.

<br />

<br />

# STEP BY STEP WIZARD GUIDE

## I. Mandatory Login Security Update

1. Access the Partner Portal and Sign In-  
   a. Enter the Partner Portal URL in your browser  
   b. Sign in with your existing credentials. You will see the below screen

   ![](https://files.readme.io/bf3d1774e71e3308b3a88d0fb49c2ba8f19eb824423a9df25bbac2eb3f9724b4-image.png)

   <br />

2. Mandatory Login Security Enforcement  
   a. All users will be forced to complete the following security updates on the Partner Portal, which also apply to all linked accounts on gupshup.io.  
   b. Multi-Factor Authentication (MFA): Set up MFA using a dedicated authenticator application. Note: If MFA was previously set up via email, it will be automatically discontinued.  
   c. Password Reset: You must reset your password to comply with the new security standards.

<br />

<br />

## II. Token Generation Security (Client Secret Update)

Client Secret Generation  
You will be taken to the Client Secret step, where you must generate or regenerate your client secret. The client secret is crucial for generating the short-lived Partner Token.

<br />

**GUIDANCE FOR USERS**  
**Developers**: Generate/regenerate your Client Secret and set the expiry to your desired date. Crucial: From this stage forward, you must use the Client Secret instead of your Username/Password for Partner Token generation.  
**Non-Developers:** Generate your Client Secret and set the expiry for the next day (tomorrow) using the calendar selection.

![](https://files.readme.io/1fefabbe0c05f3007a360b442da126ac4fabe8388889385d4a5696ebccaaac68-image.png)

<br />

![](https://files.readme.io/2d7556d7e772947b63c7f42d6a49dd0d7720ac1e06e8e89c3d59f6f9033c63ca-image.png)

<br />

## III. Administrator Security Dashboard and User Management (Admin Only)

A. Access the Security Dashboard  
Administrators can complete the mandatory steps and monitor the compliance status of all users by navigating to the ‘Security Dashboard’ section.

![](https://files.readme.io/5c6d4dbe4a6ded8679c9aa4c05391ddea1d6a6ec7fa4ad3ccfbf936505877626-image.png)

<br />

B. Review and Track Security Status  
The Admin can review the completion status for both user login security (MFA and password reset) and the Client Secret generation (used for Partner Token generation).

![](https://files.readme.io/f0f38eba92e17f487beb42e4ca87e7cc41a71f0ff79558dbaaa1b0ca8a2d654f-image.png)

<br />

C. Revoke Inactive User Access  
It is mandatory to review the user list and revoke the access of any users who are no longer active within the organization or do not require Partner Portal access.

![](https://files.readme.io/1641b22875b2badbabcad38f9792842e292fb6cd197badcf60024ef8b75dc89b-image.png)

<br />

D. Ensure Full User Compliance  
Make sure all users have successfully cleared the security status. This step is critical to ensure your accounts are secured and continued access to the Partner Portal is granted.

![](https://files.readme.io/4e8abeb89edddc59104d84de3cb97e3a9e8dcc39dd7c584b4be52eaacafdd2d3-image.png)

<br />

E. Resumption of Portal Use  
After all users have completed the steps outlined above, the entire organization can continue to use the Partner Portal.

<br />

## IV. Advanced Key Rotation (Admin Action)

#### Recommended: Administrators should complete the Key Rotation phase within 7 days.

<Callout icon="📘" theme="info">
  WARNING: This is a disruptive step. Here you must read the document carefully and prepare your systems accordingly before execution.
</Callout>

**Phase A: Submit Public Key** 

a. The first action in Key Rotation is submitting a public key to Gupshup

![](https://files.readme.io/3c1b84074c086babbbaefb862a9875328e04e9efe0d8d1a9e2553ad8ef99b27e-image.png)

![](https://files.readme.io/af44176f3d402ab0c73dc96016cf73028600e8b8f7a69f497c8275a9d888a88b-image.png)

**Phase B: Sign JWT Token and Prepare for API Key Rotation**

Next, you will sign the JWT token to proceed with API key rotation.

**Rotate gupshup.ai Account-Level Keys**  

For your gupshup.ai account-level keys, you must rotate them in this

![](https://files.readme.io/c5e6fcd1e842636202b3d42e4e48e5cf850cccc82f91a98400ccef9de1abb2a9-image.png)

<br />

Confirm -

![](https://files.readme.io/c5a53382991668afb3a562d1509a52db3fb58735af8c8c0c0c2a646de140758d-image.png)

Rotation in progress -

![](https://files.readme.io/b4ff73f26cefde324e17822687657720174b791f7a8d6fd2f9e58542f8093eb5-image.png)

<br />

**Bulk Rotation of Partner App and App-Level Keys**

Once the gupshup.ai account-level key rotation is complete, you can proceed to rotate your Partner App tokens and App-level API keys in bulk using the new JWT token.

![](https://files.readme.io/c4efad0b82891bd8310f95ec5380ca3681e1c4c101330934c0f4fe3c7585ce79-image.png)

## V. Post-Completion Security Maintenance

**Continuous Rotation Schedule**

Once all steps are completed, you must establish and adhere to a continuous rotation schedule, ensuring that all API keys and app tokens are rotated at least every 3 months for ongoing security.

<br />

![](https://files.readme.io/d374d1e76de639efb1f6f69f4179634114cd8238cd326f84eacc2808625aede4-image.png)

<br />
