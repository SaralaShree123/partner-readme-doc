---
summary: AmpLead Get Started Guide
title: AmpLead Get Started Guide
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
# Prerequisites

## Mandatory Assets

* Facebook Page (to promote ads)
* [Facebook Ad Manager](https://adsmanager.facebook.com/) (where you want to create ads and link to WABA)
* [Facebook Business Manager](https://business.facebook.com/) (to have access to WABA and Ad Manager)
* [WhatsApp Business Account (On Gupshup Self Serve)](https://support.gupshup.io/hc/en-us/articles/26252706316441-How-to-Create-a-Gupshup-App-and-Go-Live-with-a-WhatsApp-Business-Account-for-a-fresh-phone-number)

## Partner Prerequisites to Follow

1. ### WABA Onboarding
   To use AmpLead you need to have a WABA account so that you can use Gupshup. (Read more [here](https://support.gupshup.io/hc/en-us/articles/26252706316441-How-to-Create-a-Gupshup-App-and-Go-Live-with-a-WhatsApp-Business-Account-for-a-fresh-phone-number))

> 🚧 Note: WABA is recommended to be in the Cloud hosted API by Meta.

2. ### Connect a Facebook Page to your WhatsApp
   The main goal is to redirect the customer from Facebook to WhatsApp so for that we’ll have to link our Facebook Page to WhatsApp Business Account.

> 📘 [Create a new Facebook page](https://www.facebook.com/business/tools/facebook-pages?content_id=kUqLGAyy9jcLekq\&ref=sem_smb\&utm_term=how%20to%20market%20on%20facebook\&gclid=Cj0KCQjwjY64BhCaARIsAIfc7YYOLfKCbI0d8dv8zxLbJdL5dZ1jjFJpc1sutwRWBAqlJcOl4XyvpPcaAiH7EALw_wcB\&gad_source=1), if you already have one, skip this step.

Link the Facebook page with the phone number onboarded:

1. Go to [Facebook](https://www.facebook.com)
2. Under Pages select the page you want to work with
3. Go to Settings
4. Go to Linked Accounts
5. Go to WhatsApp and enter the phone number.
6. Complete this step with OTP verification.

> 📘 Amplead is **not compatible** with WhatsApp Desktop or WhatsApp Web.

# Get Started AmpLead

## Ad Creation (usual steps for ads)

* [Create an ad account](https://www.facebook.com/business/tools/ads-manager?content_id=myylAZBiY6yidw0\&ref=sem_smb\&utm_term=creating%20facebook%20ad%20account\&gclid=CjwKCAiAivGuBhBEEiwAWiFmYZxRoYgPMqjf2P1uolrOUpx8Ffws6mbjJI7Gy8h-W02bq6JDOACqQBoC3MwQAvD_BwE\&gad_source=1) if you don’t have any
* Create an ad campaign and link it to the page you just created
* While creating the ad, do the Click to WhatsApp steps mentioned above

## Onboarding

Once you have completed the ad creation process, set up your AmpLead app on Gupshup.

APIs Docs [here](/reference/amplead-apis-partner-ctx)

**This will require -**

* Self-serve API key
* The app ID (on self-serve)
* Partner ID

**As you complete this, you will receive -**

* AmpLead service ID
* AmpLead API key
* Latest Goal ID (know more about goals below)

## Goal and tracker setting

Goals represent significant milestones in the lead's journey through the bot, while trackers are the sub-steps or checkpoints within each goal. They help you pinpoint exactly where a lead may have dropped off during the bot interaction. To implement goals and trackers, you can create and manage them using the onboarding APIs. Through these APIs, you can define the names and settings for each goal and tracker, and make updates when needed via the Update AmpLead API.

During the bot journey, you should track the lead's progress by calling the Achieved Milestone API, which records the most recent tracker the user has completed. You can define multiple goals and trackers for your bot, with at least one goal required. Any tracker, typically the final one in the last goal, can be set as the milestone to mark a ‘Qualified Lead’—indicating the user has successfully navigated through the expected bot journey.

API Docs [here](/reference/goal).

### Build the Bot

Build the bot on your preferred platform and call the API Milestone achieved (API docs here) events every time a goal is reached in your journey. Link your bot to the WABA. By setting the callback in Gupshup Self-Serve

## Retargeting

Retargeting is a powerful tool for re-engaging leads who did not complete their interactions with a bot, within the free 72-hour window provided by Meta for C2WA users. Retargeting can be done based on the goals and trackers set in the onboarding APIs and within your bot, within a fixed time of C2WA event or dynamic. The leads who met a certain tracker, except the last one, will then be triggered by the template defined by you in the onboarding APIs. With this approach, it's possible to reach out to these leads up to 2 times with the same template.

API docs [here](/reference/retargeting).

You can set a callback to recieve webhook events when the retargeting messages are sent.

```json Webhook Example
{  
"leadId":"\<leadid_example>",  
"serviceId":"\<serviceId_example>",  
"status":"OPEN",  
"currentMilestoneIndex":null,  
"fepMessageTimestamp":1725379603579,  
"customerPhoneNumber":0099000099,  
"conversationId":null,  
"ctwa_clid":null,  
"adId":null,  
"externalAdId":"120205115247920650",  
"templateId":"templateId_example",  
"retargetSentTimestamp":1725379800573,  
"partnerId":"1",  
"selfServeAppId":"\<selfServeAppId_example>",  
"countRetargetingSent":1  
}
```

> 📘 Have to use a pre-approved text-based template here.

# Meta Ad Account Linking

By linking your Meta Ad Account, you can access features such as the Meta Conversions API, the Campaign Level API, and the UI Analytics SDK.

**Prerequisites for Using Ad Manager:**

**User-Level Checks:**

* Ensure users have full control over the Ad Account.
* Make sure Ad Account does not have any user restrictions which you are attempting to link.

**Ad Account Level Checks:**

* Verify whether the Ad Account is banned or has any restrictions. If so, the linking flow will not function correctly.\
  Typically, account bans are indicated by a banner at the top of the page.

You can navigate <Anchor label="here" target="_blank" href="https://business.facebook.com/business-support-home/?landing_page=account_overview">here</Anchor> to check the same.

> ❗️ If you have any restrictions on user level or account level your Ad Manager Linking will fail.

**Possible solutions include**

* Add a new admin user with full control to Ad Manager and try the follow.
* If Ad manager is banned or has any restrictions please write to Meta and resolve it before trying to link your Ad manager Account.

> 📘 To use this feature, please fill out the <Anchor label="form" target="_blank" href="https://forms.gle/ePu4AVmUd47T8bkj7">form</Anchor> to get started. You will receive an automated email from us. Please ensure you have the login credentials for the Facebook Business Manager ready, as the link will expire in an hour.

# Analytics

1. **Lead Analytics**\
   Use the Fetch lead by service ID API or Ad ID API to get the list of leads (phone numbers) along with their tracker status and retargeting details, if any. You can use this to analyze the retargeting funnel or even re-engage with these customers at a later stage.
2. **Ad Campaign Analytics**\
   By linking your Ad Manager with our AmpLead App, you'll unlock valuable insights that can enhance your campaigns. This will unlock the ability to fetch ROI data directly from your Linked Meta Ad Account.

## Analytics SDK

The Analytics SDK is a JavaScript code snippet that you can integrate into your website to gain valuable insights.

> 🚧 This will work only if the Ad Account is linked.

**UI Analytics SDK**\
The Embedded Analytics UI can offer your customer a more visually engaging experience for Lead Analytics, allowing you to filter data easily by Ad or Date. You can now view analytics, track your Leads Status, Leads Trend, and much more.

**Ad Comparision Analytics**

Ad Comparision Analytics gives you insights of your ads. You can comapre up to 4 Ads at a time.

<Image align="center" className="border" border={true} src="https://files.readme.io/cd8e64d0729ec8a8487fb4149e590a5bd9565ae25d979d0b63a09c9f084e0b4a-image.png" />

For more information, please refer to the guide [here](/docs/amplead-analytics-sdk-guide).

> 📘 To use this feature, please fill out the <Anchor label="form" target="_blank" href="https://forms.gle/8K1eprohUU81ex1E6">form</Anchor> to get started. You will receive an automated email from us.

# Conversions API

The Conversions API is designed to create a connection between an advertiser’s marketing data (in this case Qualified Lead) to Meta systems that optimize ad targeting, decrease cost per result and measure outcomes.\
Gupshup will help in sharing your WhatsApp event with Meta which will improve your business.

> 📘 Please pass the flag in the Onboarding API (while creating a AmpLead API) isCAPIEnabled to enable conversions API.

# Amplead Integration Checklist

## Step 1: Create a Service

* Use your Gupshup App ID and Authentication to create a service.
* Link your Meta (Facebook) Ad account to Amplead for deeper insights and analytics.
  * Fill out the <Anchor label="form" target="_blank" href="https://forms.gle/ePu4AVmUd47T8bkj7">form</Anchor> to receive the LINK to connect your Meta Ad account.

## Step 2: Integrate Our APIs

* Set specific goals and milestones to track your progress.
* Utilize the Mark Goals API in your bot to automatically mark these goals.
* Implement retargeting strategies: you can set default retargeting or make it goal-specific.

## Step 3: Build Your Analytics

**Explore our SDK:**

* Fill out the <Anchor label="form" target="_blank" href="https://forms.gle/8K1eprohUU81ex1E6">form</Anchor> to receive the SDK code.

OR

* Build your own analytics via our APIs:
  Construct an interactive UI and populate data using our API.

## Step 4: Launch Your Campaign

Run an ad campaign to start generating amplified leads.