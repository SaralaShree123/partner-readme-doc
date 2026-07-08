---
title: Onboarding APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Onboarding APIs enable Tech Providers to efficiently onboard WABAs for their end customers.\
Utilizing these APIs removes the necessity for Tech Providers or end customers to access the Gupshup interface.
Tech Providers can integrate and manage the WABA onboarding process directly within their own platforms.

## Use case for Onboarding API is simple

An ISV can create an automated WABA Onboarding journey in their own platform without having the customer come to the Gupshup interface.

## Prerequisites to use the Onboarding APIs

1. Gupshup Partner Portal account should be with an approved Solution ID.
2. A single Gupshup wallet in a self serve or a partner portal account.

> ℹ️ Users cannot create WABAs in different Gupshup Wallets

## Let's understand the APIs one by one.

Please check out the API Documentation [here](https://partner-docs.gupshup.io/reference/app-onboarding-apis)

* **Create App** - This API is to create an Gupshup App. Please note that your app comes pre-linked to your Partner ID.
* **Set CallBack** - To set call back to receive the events
* **Generate Embed Signed Link** - This will create an embed link for WABA owners to onboard it.
* **Update App** - It helps you to update the templateMessaging, and storageRegion.
* **Get App** - To get details of one App.
* **Get App List** - To get all the list of Apps created.
* **Mark App for Migration** - This API to be used if you are doing migration from another BSP to Gupshup. It will indicate to Gupshup that this is a migration case and will help sync the templates and do the necessary migration related actions
* **Set Contact Details** - Can set contact details for an App here.
* **Resend Verification Link** - Resend Link Email

**Flow in which fashion APIs should be called**

<Image align="center" src="https://files.readme.io/ae33130990c7eddbeb19499cde3a29389923569cbf52ca7eb5eb449a7c42931f-Screenshot_2025-01-17_001719.jpg" />

## Set Live-Event callback

Finally, you can configure the callback event to receive notifications about the app's live events. This will inform you whenever an app goes live through the embedded link refer [here](https://partner-docs.gupshup.io/docs/system-events#/go-live-event)