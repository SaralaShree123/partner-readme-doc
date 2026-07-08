---
title: Coexistence
excerpt: >-
  Co-existence allows you to connect your existing WhatsApp Business App number
  to Gupshup.
deprecated: false
hidden: false
metadata:
  robots: index
---
* WhatsApp business App users can connect to Cloud API and take advantage of the automations
* You can still use the WhatsApp Business App as usual
* Chat history remains synced between both

## Know Limitations from Meta

### No Payment attached to the WhatsApp Business App

* Please ensure that no payment method (card or any other local payment option) is linked to your WhatsApp Business App.
  * This will not allow Gupshup to attach our credit line.
  * Recommedation here is that you remove all the payment method before proceeding.

## Known Meta Issues

1. Phone number not eligible for Co-existence
   * Meta has not yet shared the eligibility criteria for phone numbers
   * No workaround or resolution has been provided so far
2. “Error Object” while submitting phone number
   * Occurs during the onboarding flow
   * Meta has not shared updates or a fix yet
3. Multiple or inconsistent onboarding errors
   * Errors may appear at different steps of the flow
   * Currently under Meta investigation, with no confirmed timeline
4. Inconsitent Events

   The blow-mentioned webhooks/features are currently experiencing issues from Meta’s end.

   1. History events
   2. Contact sync
   3. Smb_message_echoes

<Callout icon="🚧" theme="warn">
  For all the above-mentioned issues, we will update the documentation or share additional information once we receive further clarification from Meta.
</Callout>

<Callout icon="ℹ️" theme="info">
  Note: All apps will receive DRL events as they used to.
</Callout>

## Before You Start (Quick Checklist)

Please make sure:

* Your WhatsApp Business App version is 2.24.17 or higher
* Your phone number country is supported
* Facebook login with Business Manager access
* Ability to scan a QR code from your WhatsApp Business App
* Your Whatsapp account in business App should be 3 months old with active messaging

## Countries currently not supported

**Nigeria and South Africa**

## Enablement

There is no enablement required. You can continue creating apps through Self Serve or the Partner Portal. Apps created via the Onboarding API also do not require any enablement.

## Onboarding Steps

1. Click the App Golive button to start the Golive flow:

   <Image align="center" src="https://files.readme.io/d7fd64a9eada5d3caba505474be3f9f722c8b815087e6a13a7c55df8831c7e28-1.png" />
2. If the Coex feature is enabled, you will see an option to use an existing WhatsApp Business App number, select use existing WhatsApp Business   **Note: If you are unable to see this option, but your app is enabled for CoEx, please proceed you will see the CoEx steps in the Facebook flow (Step 7) of this guide.**

   <Image align="center" border={true} src="https://files.readme.io/2f38cb61464def1b1e27835d3c97a3b3ef2fde84331808f26b494917b29817c2-2.png" className="border" />
3. Select your local storage region and click Next
4. Enter the contact details, select the terms and conditions, and click Next.

   <Image align="center" src="https://files.readme.io/7caa61de32efa66c7d62f7ef49eb0edd7a227c7eeb8e7634cc4fad10aa23d7e4-4.png" />
5. Confirm Contact details
6. Click on Continue with Facebook or use embed signed link to process

   <Image align="center" src="https://files.readme.io/dbaeea5eef3e4475a7bb6aada9e866ffccacb364e52af5ba34f36ba65ba2b572-6.png" />
7. Click Continue, select Business portfolio then Connect a WhatsApp Business app from the WhatsApp Business account tab, and click Next.

   <Image align="center" border={true} src="https://files.readme.io/42cecdd4af9ecd25bc352961a7404925c6e3143f62bec801b2743c7947206621-co.png" className="border" />
8. Enter a WhatsApp Business app phone number and click Next

   <Image align="center" src="https://files.readme.io/6a92642fa5215ef6fd3626e4d92edc8f095ab68f2fc08189983dc7049ab54c9b-8.png" />
9. Businesses that select this option and enter their WhatsApp Business app phone number will see a QR code and instructions to check for new WhatsApp Business app messages:

   <Image align="center" src="https://files.readme.io/8878c82b0a91b086922522512a883cbc73958b0e41829164a059a45dbc2b03c5-9.png" />
10. The WhatsApp message instructs the business to use the app to scan the QR code displayed in Embedded Signup:

    <Image align="center" src="https://files.readme.io/a8a6cd7ecd99adddce08cb15dba8a2793e35f487481742945db230c450fd0d3d-10.png" />
11. Connect to the Business Platform and complete the process    Note : You can either use QR code scan or Use access code

    <Image align="center" src="https://files.readme.io/ce577ada54acf45938bd5b9dd3b76a7605665c6650db0d0e4a781adef608b8d9-11.png" />

    <Image align="center" src="https://files.readme.io/0da52c01ff82e99245751ca3017652d5fec81cab2c556bac2d769b3e1741d91d-12.png" />
12. Please ensure that all chats are shared if you want to receive history events. If chats are not connected here, Meta will not share the history events.

    **Also, if you skip this step now and decide to enable it later, you will need to deregister your WABA from the Cloud API and complete the onboarding process again.**

    Please refer to the Sync API section to learn more about triggering history events. Please ensure that all chats are shared if you want to receive history events. If chats are not connected here, Meta will not share the history events.
13. After All above Successful process, On FB page select the time zone and Complete the shown process on clicking on confirm and finish button

    <Image align="center" src="https://files.readme.io/d2550e76161ce43e9e2dfc2fb785af379c248ac851258a21c7b18dfa1a41fa17-13.png" />

    <Image align="center" src="https://files.readme.io/60d0785941f580ea07443d1750754fe8b91f8d78a899ce19544b655c87d56b63-14.png" />

    <Image align="center" src="https://files.readme.io/1ebb0d3eab64b584ff3ca537035ca8b7ef045acb36137f86b45f9d9ce68a33a2-15.png" />

    <Image align="center" src="https://files.readme.io/18d6f8b3ae038983fcd20bb86ff55720028e17e52e544cff082f899bc055a808-16.png" />
14. After Completion of FB Process Get Back to partner page for waba phone number selection Select phone number and click on confirm

    <Image align="center" border={true} src="https://files.readme.io/a2896675b5fc4dbbe2b6cd0e6412991f085a66c50283c749bc94e54012dd8285-17.png" className="border" />
15. Wait for setup completion, After Successful setup completion, App is ready to use

    <Image align="center" src="https://files.readme.io/b7b45c891a7a330c49d2a7fe762dc616c38cb2cf52000b7cab2f8e70f27d58f4-18.png" />

<Image align="center" src="https://files.readme.io/03fed81db7c152804a1c4d7eb11ae1d67c9ed0b6cbba42e370f9c52d7614587b-19.png" />

## Sync API - To trigger `history` and `smb_app_state_sync`

<Cards>
  <Card title="Sync API Reference" href="https://partner-docs.gupshup.io/reference/initiatecoexsync#/" icon="fa-code">
    API Reference
  </Card>
</Cards>

Both `smb_app_state_sync` and `history` synchronization can be triggered only once, and must be initiated within 24 hours of onboarding. Both `smb_app_state_sync` and `history` synchronization can be triggered only once, and must be initiated within 24 hours of onboarding.

### **Steps to use this API**

1. Make the API call with the desired syncType
2. Then you will receive an event from Meta on the webhook as mentioned in the meta document <Anchor label="here" target="_blank" href="https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users#synchronizing-whatsapp-business-app-data">here</Anchor>.

## Coexistence Webhooks

* Use this <Anchor label="API" target="_blank" href="https://partner-docs.gupshup.io/reference/setsubscription-api-v3">API</Anchor> to subscribe to Coexistence Webhooks
* More information on the Coexistence events <Anchor label="here" target="_blank" href="https://partner-docs.gupshup.io/docs/coexistence-events#/">here</Anchor>

<Callout icon="ℹ️" theme="info">
  **Please note the following regarding Media URLs in events:**

  For CoEx, we forward the v3 events exactly as received from Meta without any modifications. Meta now provides only the Media ID instead of a direct media URL.

  To retrieve the media file using the Media ID, you can use the [Media Retrieval API](https://partner-docs.gupshup.io/reference/downloadmedia).
</Callout>

Now you are ready to start messaging from Whatsapp business app and Whatsapp cloud API.

## Need Support?

For any support requests, questions, or issues, please reach out to [partner.support@gupshup.io](mailto:partner.support@gupshup.io), and our team will assist you with a resolution.

<Callout icon="❗️" theme="error">
  Please note that most Coexistence-related issues originate on Meta's side.

  Kindly set expectations accordingly, as the resolution timeline for such cases may vary and can be dependent on Meta's investigation and response.
</Callout>

<br />
