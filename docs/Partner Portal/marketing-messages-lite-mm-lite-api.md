---
title: Marketing Messages Lite (MM Lite) API
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 PRICING:
>
> MM Lite Meta rate card is available _[here](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/mm-lite-api-pricing#rates)_.

### Overview

Marketing Messages Lite API ("MM Lite API") is an easy-to-use solution for direct marketers built to enhance the customer experience, and drive equal or better results for businesses compared to marketing via Cloud API.

**Key benefits**

1. MM Lite API delivers comparable or a greater number of marketing messages than Cloud API. MM Lite API allows for more dynamic messaging limits, so marketing messages with high engagement (e.g. messages that receive more reads) can reach more customers. In India, MM Lite API marketing messages that receive higher engagement (e.g., reads) observed up to 9% higher messages delivered compared to Cloud API.
2. New features exclusive to MM Lite API and not available on Cloud API. For example, MM Lite offers exclusive comparison benchmarks showing your templates’ performance against similar templates in your region, personalized recommendations for how to improve performance metrics, expiring marketing messages for short-run promotions via a customizable via time-to-live, new conversion reporting to show web and app conversions, and more.
3. Easy-to-transition from Cloud API. Businesses can use existing WhatsApp Business Accounts, phone numbers, and marketing templates. Partners maintain the same billing model as Cloud API, and minimal integration burden

Check <Anchor label="Meta Documentation" target="_blank" href="https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api">Meta Documentation</Anchor>

### STEP 1 : Initiate Onboarding For MM Lite (for apps created till July 2025)

Gupshup has already initiated MM Lite onboarding intent to all WABAs. Refer to [article](https://support.gupshup.io/hc/en-us/articles/43977754744217-MM-Lite-Onboarding) for steps needed by customer. Tech Providers must use GTM resources / webinars to spread awareness on how to accept the MM Lite requests.

The MM Lite Tos acceptance is at a BMID level and hence no WABA or Phone selection/registration is required during the onboarding on MM Lite. All the WABAs under the BM are automatically registered on MM Lite after successfully completing the ES Flow. The link generated can expire in 5 days. If the WABA was on OBO model, it will be moved to a shared model during the ES Flow as a prerequisite of MM Lite API.

As of 16 June 2025, Gupshup switched on the v2 mm lite flag directly, thus routing all marketing messages sent over V2 through MM Lite, if customer accepts the onboarding intent.

FOR APPS CREATED FROM AUG 2025  : MM Lite onboarding happens while go-live.

<br />

### STEP 2 : Confirm onboarding is completed

1. If onboarding is completed by a customer, Meta triggers an event called **tos_signed**.  After an **tos_signed** event is received from _Meta > Gupshup_ it means Onboarding is marked as completed on Gupshup.  [**There could be a known Issue:** _No event received from Meta intermittently_]
2. <Anchor label="V2 users" target="_blank" href="https://partner-docs.gupshup.io/reference/post_partner-app-appid-template-msg#/">V2 users</Anchor> can now jump to next step, while V3 MM Lite endpoint users can use this [API](https://partner-docs.gupshup.io/reference/getwabahealth#/) to check MM Lite Onboarding status.  Click [here](https://partner-docs.gupshup.io/docs/system-events#/mm-lite-webhook-event-v2--v3) for reference.

<br />

### STEP 3: Template creation

No special template creation.  Existing templates created on Cloud API for marketing can be used in MM Lite as well.  Partners can use this [existing API](https://partner-docs.gupshup.io/reference/post_partner-app-appid-templates-6#/) to do the same. Also add deep links in the CTA buttons for your Android apps to be able to track them. Read <Anchor label="more" target="_blank" href="https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/guides/deep-links#template-creation-via-whatsapp-manager">more</Anchor>

**NOTE:** For marketing you can set TTL while you apply templates, which will apply if marketing messages are sent via MM Lite.

<br />

### STEP 4 : Sending MM Lite Messages

There are 2 ways to send marketing messages via MM Lite:

1. #### Option A: _Automatically route marketing messages sent on v2 via MM Lite  (recommended if you use v2 send template endpoints)._Here are the steps for the same:
   After or before step 2 above is completed, partner has to use [this API](https://partner-docs.gupshup.io/reference/post_app-appid-mmlite-msg-enable#/) to enable v2 mmlite messaging.  This API will allow you to enable the MM-Lite Messaging flag (no need to reach out to support)
   > 📘 **NOTE:**
   >
   > [**RATE LIMIT**](https://partner-docs.gupshup.io/update/docs/partner-rate-limits#/) - 2 per hour per app.

As soon as 'tos_signed' webhook is received from Meta & some other checks internally OR new apps are onboarded - marketing messages sent on V2 template endpoint are routed through mm lite endpoint. Thus no extra charge.If event not received, marketing messages sent on v2 template endpoint go via cloud api, thus incurring 6% extra charges over WA fee.

<br />

1. #### Option B: _Send marketing messages via dedicated v3 MM lite endpoint (recommended if you use v3 send template endpoints)._

After step 2 above is completed, run the v3 MM Lite endpoint.  The syntax and payload of MM Lite send message API replicates that of Cloud API [V3 send message API](https://partner-docs.gupshup.io/reference/post_partner-app-appid-v3-text-message#/).  Other messages (Auth, Service, Utility, free form) return an error in this API.

If 'tos_signed' webhook is received from Meta & some other checks internally OR new apps are onboarded --
a. marketing messages sent on Regular V3 template endpoint will go via cloud api, thus incurring 6% extra charges over WA fee

b. marketing messages sent on MM Lite V3 template endpoint will go via MM Lite, thus no extra charge

If 'tos_signed' webhook is NOT received from Meta & some other checks internally prove that MM lite onboarding is not completed - 
a. marketing messages sent on Regular V3 template endpoint will go via cloud api, thus incurring 6% extra charges over WA fee

b. marketing messages sent on MM Lite V3 template endpoint will ALSO go via cloud API, thus incurring 6% extra charges over WA fee [Meta is auto-routing this directly now]

### STEP 5 : **Receiving webhooks / Reporting**

**Webhooks**  
All incoming DLRs should be received and forwarded as per the existing mechanism. Webhooks / DLR payload will be the same as existing on V2 and V3, no change.  Except - delivered, sent, read and billing event will indicate the message category as **Marketing lite**.

**Pricing & Analytics**

* Wallet statement will show 'marketing lite' deductions.
* Partner Analytics APIs response will show the marketing lite counts, while all partner portal reports will reflect marketing lite counts.

### STEP 6 : Viewing metrics

MM Lite Insights can help you track metrics of the marketing campaigns sent on MM Lite such as - Messages sent, delivered, read, Total amount spent, Cost per delivery, CTA URL link clicks. Cost per click, CTA URL link click rate, Add to cart* (Web + App), Checkout initiated* (Web + App), Purchase*, purchase value (Web + App), App Activations*

'*' stands for if conversion event is sent to Meta via Meta Pixel or Conversions API. Read more about it below.

1. Partner API to fetch <Anchor label="MM Lite Ad Insights" target="_blank" href="https://partner-docs.gupshup.io/reference/gettemplateinsights#/">MM Lite Ad Insights</Anchor>.

Here are a few features you can benefit with this API -

a. Benchmark metrics : You can get benchmark metrics via Insights API for read rates and click rates

b. Action metrics - Sent, Read, Delivered, Click

c. Rates metrics - marketing_messages_delivery_rate, marketing_messages_read_rate, marketing_messages_link_btn_click_rate

d. Spend metrics - marketing_messages_spend, marketing_messages_cost_per_delivered, marketing_messages_cost_per_link_btn_click

All analytics for a business’ marketing message templates sent via the MM Lite API are also available at:-

1. Ads Manager, on the **Marketing Messages** tab. Read <Anchor label="here" target="_blank" href="https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/viewing-metrics#view-metrics-via-uis">here</Anchor>
2. The Whatsapp [Template Analytics API](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics#template-analytics) - In app events only, no conversion events.

**Sending conversions back to Meta - **

If Businesses are using [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel) and [Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/app-events) to send conversion events (Add to card, purchase etc.) to Meta after customers are taking such actions on a Marketing message sent via MM API (Gupshup does not provide the Insights API as of now).  
Businesses can use the Meta Pixel and Conversions API for App Events to send signals to Meta when customers take an action on their website or app, after clicking a URL in a marketing message. Note that in-thread conversion optimizations and reporting are not yet available for MM Lite API.

**Conversion events received in Insights - **

marketing_messages_website_add_to_cartmarketing_messages_website_initiate_checkout
marketing_messages_website_purchase
marketing_messages_website_purchase_values
marketing_messages_app_add_to_cart
marketing_messages_app_initiate_checkout
marketing_messages_app_purchase
marketing_messages_app_purchase_values

### Support

For any support on MM Lite, please mention specifically about **MM Lite** for quicker TAT.
