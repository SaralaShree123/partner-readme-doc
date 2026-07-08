---
summary: API based WABA Onboarding
title: API based WABA Onboarding
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Introduction/Audience

This document is designed for partners/ISVs with the technical expertise to perform a new WABA onboarding using Gupshup's APIs. This enables the user to complete the onboarding process independently of the Gupshup UI.

## Scope

1. This service supports only onboarding new WABAs; migration of existing WABAs is not included.
2. The onboarding process is exclusively conducted on Meta's cloud platform, with a default rate of 80 TPS.
3. Onboarding is initiated only via the embedded signup link.

> 📘 Note
>
> 1. The signed link is valid for **5 days only.**

## Pre-requisites

1. Users need to approve and complete partner onboarding through Gupshup's [partner portal](https://www.gupshup.io/partner/login).
2. Partners are required to create an account on gupshup.io to [generate](https://docs.gupshup.io/docs/api-based-waba-onboarding#generate-an-api-key) an API key.
3. Contact the [support](partner.support@gupshup.io) team to link the API key with the Partner ID.

## Steps

### Generate an API key

To generate an API key, ISVs have to create an account on gupshup.io. This is a one-time process, and the token remains valid until a request for invalidation is made to Gupshup support.

1. Go to [https://www.gupshup.io](https://www.gupshup.io)
2. Login using any available login methods. (New users, [signup](https://docs.gupshup.io/docs/getting-started-with-gupshup-integration-platform) with Gupshup to get started).
3. Navigate to your profile in the top right corner and copy the API key.

<Image align="center" className="border" width="1200px" border={true} src="https://files.readme.io/b945f0c-Capture3.png" />

## Request Support for an API key to partner ID linkage

Reach out to [partner.support@gupshup.io](mailto:partner.support@gupshup.io) link your partner ID with the API key before proceeding with the next step of App creation.

## Generate Partner token

To get a new partner token, use the existing [Get Partner Token API](https://docs.gupshup.io/reference/post_partner-account-login) 

### App Management

An app in Gupshup acts as a container associated with a WABA. Before accessing any other APIs from Gupshup, it is mandatory to create an app, since all rely on an app context.

1. **Create App**: This API enables the users to create a new WABA onboarding automatically with the necessary configurations in their platform or service.  Read how to use the [Create App  API](https://docs.gupshup.io/reference/post_partner-app).
2. **Update App**: This API allows the users to update the WhatsApp Business API (WABA) onboarding settings for an app.  Read how to use the [Update App API](https://docs.gupshup.io/reference/put_partner-app-appid).
3. **Get App**: This API retrieves detailed information about a specific partner app using its App ID.  Read how to use the [Get App API](https://docs.gupshup.io/reference/get_partner-app-appid-details).
4. **Get App List**: This API endpoint retrieves a list of all the applications associated with a partner's account on the Gupshup platform.  Read how to use the [Get App List API](https://docs.gupshup.io/reference/get_partner-app-list).
5. **Set CallBack**: This API allows the users to configure a callback URL for an application, enabling the system to send notifications or events to the specified URL when certain actions occur within the app.  Read how to use the [Set CallBack API](https://docs.gupshup.io/reference/put_partner-app-appid-callback) 
6. **Set Contact Details**: Set Contact Details API is used to update or configure a partner app's contact information during the onboarding process using a specified app ID.  Read how to use the [Set Contact Details](https://docs.gupshup.io/reference/put_partner-app-appid-onboarding-contact).
7. **Resend Verification Link**: During the onboarding process, this API enables the user to resend the email verification link to a user's email address.  Read how to use the [Resend Verification Link API](https://docs.gupshup.io/reference/post_partner-app-appid-onboarding-contact-email-resend).
8. **Generate Embed Signed Link**: This endpoint is used to generate an embedded signed link for partner app sign-up.  Read how to use the [Generate Embed Signed Link API](https://docs.gupshup.io/reference/get_partner-app-appid-onboarding-embed-link).
9. **Mark App for Migration**: The ‘Mark App for Migration’ enables a WABA to transfer from one account to another without disruption in operation while retaining all message limits, templates, and business statuses.  Read how to use the [Mark App for Migration API](https://docs.gupshup.io/reference/post_partner-app-appid-onboarding-migration).

## FB Embed Flow

To initiate the embed flow, FB requires some basic details to be filled in.

### Add Email

This is a mandatory step to [add email](https://docs.gupshup.io/reference/post_partner-app) ID (and other contact information) to the business contact details

**Request Body**

```curl
curl --location --request PUT '{{partner_portal_base_url}}/partner/app/:appId/onboarding/contact'  
--header 'token: {{PARTNER_TOKEN}}'  
--header 'Content-Type: application/x-www-form-urlencoded'  
--data-urlencode 'contactEmail=\<contact_email_id>'  
--data-urlencode 'contactName=\<contact_name>'  
--data-urlencode 'contactNumber=\<contact_phone_number>'
```

### Verify Email

Login to this email and verify the email address. If necessary, use the [Resend Verification Email](https://docs.gupshup.io/reference/post_partner-app-appid-onboarding-contact-email-resend) endpoint to resend the email.

### Resend Verification Email (Need basis only)

Use this API to resend the verification email to the stored business contact email id.\
**Request Body**

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/:appId/onboarding/contact/email/resend' \
--header 'token: {{PARTNER_TOKEN}}' \
```

### Generate Signed Link

To generate the embed signed link for the app, use this [endpoint](https://docs.gupshup.io/reference/get_partner-app-appid-onboarding-embed-link).   The ISV customers click on this link to complete their Self-serve embed flow. Once the embed flow is complete, customers can come back to their current interface and wait for the app to go live.

## Post Go Live

### Business Profile Management

Once the app is live, the business profile is managed using the business profile APIs.

### Template Management

Once the app is live, customers have the ability to create and manage templates using Template Management APIs.

### Send Message

The messages are sent through [Send Message APIs](https://docs.gupshup.io/reference/msg).\
For all new features supported on CAPI-only, use this [endpoint](https://docs.gupshup.io/reference/sendmessage) for sending messages.
