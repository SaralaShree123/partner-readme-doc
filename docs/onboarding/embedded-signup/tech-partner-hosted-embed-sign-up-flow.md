---
summary: Tech Partner Hosted Embed Sign up flow
title: Tech Partner Hosted Embed Sign up flow
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
<Callout icon="📘" theme="info">
  ## The feature is currently in beta mode and is only available to select partners.
</Callout>

# Objective

As a Tech Provider, you can work with a Solution Provider (Such as Gupshup) to jointly create a solution that allows you and the Solution Partner to jointly manage your customer’s WhatsApp assets. With this joint solution, either the Solution Partner or the Tech Provider can host the embedded Signup on their individual portals for the customers to complete the WhatsApp Business Account (WABA) onboarding process.

This guide is intended for partners who want to host an Embedded Signup flow on their own portal after registering as  [Tech Provider](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers) with Meta

# Prerequisites

1. <Anchor label="Register as a Tech provider" target="_blank" href="/docs/get-solution-id-from-meta">Register as a Tech provider</Anchor> with Meta.
2. [Create a joint solution](/docs/get-solution-id-from-meta) with the Gupshup.
3. Register as a Tech provider with the Gupshup partner portal, and create a new [wallet](https://support.gupshup.io/hc/en-us/articles/29522963720473-WABA-and-Wallet-Management-Guide-for-Partners-onboarded-on-Gupshup-6th-March-24-onwards).
4. [Configure Embedded signup](https://developers.facebook.com/docs/whatsapp/solution-providers/multi-partner-solutions) with the joint Solution ID generated in step 2.
5. Complete a new onboarding with the above configured embedded signup.

> 📘 NOTE:
>
> Post embedded sign-up completion partners or Partner’s customer should **not**:
>
> * Register the WABA using the registration API.
>   * Gupshup will handle the registration process as per the onboarding flow when the partner calls the [App linking API](/docs/tech-partner-hosted-embed-sign-up-flow#step-1-link-an-app).
> * Enable and set 2FA.

6. Follow the steps here to add Embedded Signup to your website. Implementation - W[hatsApp Business Platform - Documentation - Meta for Developers](https://developers.facebook.com/docs/whatsapp/embedded-signup/implementation) . Meta SDK for embed signup details are also present here.
7. Once above it setup, follow steps here to enable Gupshup jointly manage customer assets and provide Gupshup Solution Partner's services. [Multi-Partner Solutions - WhatsApp Business Platform - Documentation - Meta for Developers](https://developers.facebook.com/docs/whatsapp/solution-providers/multi-partner-solutions)

```
Configure Embedded Signup
Assign the solution ID to the solutionID property in the extras.setup object within the launch method and callback registration portion of the Embedded Signup code.

// Launch method and callback registration
const launchWhatsAppSignup = () => {
  FB.login(fbLoginCallback, {
    config_id: '<CONFIGURATION_ID>', // your configuration ID goes here, ensure it is in quotes
    response_type: 'code',
    override_default_response_type: true,
    extras: {
      setup: {
        solutionID: '<SOLUTION_ID>' // add solution ID here, ensure it is in quotes
      },
      featureType: '',
      sessionInfoVersion: '3',
    }
  });
}
Both you and your partner's business portfolio (Business Settings > Business Info) will appear throughout the Embedded Signup flow.


Once configured, surface the customized Embedded SIgnup flow to customers on your platform wherever you feel it is appropriate. Note that if you have multiple active partner solutions, it is your responsibility to inject the correct solution ID into your Embedded Signup configuration and surface it to your intended customers, otherwise a customer could be onboarded using the wrong solution.
```

<br />

8. Complete details on Embedded Signup is mentioned by Meta over here: [Embedded Signup - WhatsApp Business Platform - Documentation - Meta for Developers](https://developers.facebook.com/docs/whatsapp/embedded-signup)

<br />

After all above prerequisites are completed, use the below steps to configure the WABA and phone number to use Gupshup APIs

# Step 1: Link an App

This API creates a Gupshup app, maps the WABA created with the Gupshup app, and attaches the Gupshup credit line to the WABA. The phone number passed by the partner is mapped to the WABA. Additionally, partners can also pass the optional callback URL (they wish to map with the WABA).

Partners will need to call the following APIs to link WABA ID and Phone number and get the status of Gupshup Apps.

## Parameters

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Value
      </th>

      <th>
        Mandatory/Optional
      </th>

      <th>
        Description
      </th>

      <th>
        Constraint
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorization
      </td>

      <td>
        `{{PARTNER_TOKEN}}`
      </td>

      <td>

      </td>

      <td>
        JWT Token issued post partner login
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        name
      </td>

      <td>

      </td>

      <td>
        Mandatory
      </td>

      <td>
        Gupshup app name which is to be created
      </td>

      <td>
        * Should be between 6 - 150 characters. - Should not conflict with any other Gupshup App. - Special Characters are not allowed.
      </td>
    </tr>

    <tr>
      <td>
        wabaId
      </td>

      <td>

      </td>

      <td>
        Mandatory
      </td>

      <td>
        Live WABA ID
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>

      </td>

      <td>
        Mandatory
      </td>

      <td>
        Phone number to be linked with the WABA
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        callbackUrl
      </td>

      <td>

      </td>

      <td>
        Optional
      </td>

      <td>
        Callback URL to be mapped with the WABA
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

## Request

```
curl --request POST --location '{{PARTNER_URL}}/partner/tpp/app' \
--header 'Authorization: <PARTNER_TOKEN>' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name={{appName}}' \
--data-urlencode 'wabaId={{wabaId}}' \
--data-urlencode 'phone={{phoneNumber}}' \
--data-urlencode 'callbackUrl={{callbackUrl}}' (optional)
```

## Response

| Status Code | Response                                                                                         | Comments                                                                                           |
| :---------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                  |                                                                                                    |
| 200         | `{    "status" : "success",    "appId": "\<app_id>" }`                                           |                                                                                                    |
| **Error**   |                                                                                                  |                                                                                                    |
| 409         | `{    "status": "error",    "message": "Bot Already Exists"   }`                                 | When already a bot with the same name exists in Gupshup                                            |
| 400         | `{  "status": "error",  "message": "Invalid characters used in app name" }`                      | When a Special character is added to a name.                                                       |
| 400         | `{  "status": "error",  "message": "App name should be between 6 to 150 characters in length" }` | if the App name is not provided or the App name length is less than 6 or more than 150 characters. |
| 429         | `{  "status": "error",  "message": "Too Many Requests" }`                                        | 10 Requests per Minute                                                                             |
| 500         | `{  "status": "error",  "message": "Unable to create App" }`                                     | For any Internal Error                                                                             |

# Step 2: Get Partner App Token

`This API fetches the <<glossary:Partner app token>> against the <<glossary:Partner token>>.`

## Parameters

| Key           | Value               | Description                         |
| :------------ | :------------------ | :---------------------------------- |
| Authorization | `{{PARTNER_TOKEN}}` | JWT Token issued post partner login |

## Request

```
curl --location '{{PARTNER_URL}}/partner/app/:appId/token' \
--header 'Authorization: <PARTNER_TOKEN>'
```

## Response

```
{
  "name": "Partner_Name",
  "terms_read": true,
  "token": "{{token}}"
}
```

# Step 3: Get Status

This API fetches the status of the Gupshup app creation and the underlying processes, as detailed in the link to app API.

## Parameter

| Key           | Value                   | Description                      |
| :------------ | :---------------------- | :------------------------------- |
| Authorization | `{{PARTNER_APP_TOKEN}}` | Access Token for the application |

## Request

```
curl --location '{{PARTNER_URL}}/partner/app/:appId/pipeline' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Status Codes

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Status Code</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Response</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Comment</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>Success</strong></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">200</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
  <pre><code>{
    "status": "success",
    "whatsapp": {  
      "countryCode": "<countryCode>",
      "createdOn": 1704860430508,
      "creationStage": "WHATSAPP_PROVISIONING_DONE",
      "dialCode": "<phoneNumber>",
      "embedStage": "EMBED_STARTED",
      "id": "<appId>",
      "modifiedOn": 1707947273721,
      "pipeLineStage": "FINALIZE",
      "uiFormStage": "COMPLETE_VERIFICATION",
      "whatsappVerificationStatus": "WHATSAPP_VERIFICATION_DONE"
    }
  }</code></pre>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>Error</strong></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">200</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
  <pre><code>{
    "status": "success",
    "whatsapp": {  
      "countryCode": "<countryCode>",
      "createdOn": 1706694745887,
      "creationStage": "ERROR",
      "dialCode": "<phoneNumber>",
      "embedStage": "EMBED_PENDING",
      "id": "<appId>",
      "modifiedOn": 1707370989543,
      "pipeLineStage": "CREATE_DOCKER",
      "uiFormStage": "GET_WHATSAPP_APPROVAL",
      "whatsappVerificationStatus": "PN_DN_APPROVED"
    }
  }</code></pre>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;">In case of error, the pipeline is retried thrice before failing the attempt</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">400</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <pre><code>{
      "status": "error",
      "message": "Please review the request parameters and retry"
    }</code></pre>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;">Validate the request Parameters Or Authorization token</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">429</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <pre><code>{
      "status": "error",
      "message": "Too Many Requests"
    }</code></pre>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;">10 Requests per Second</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">500</td>
  <td style="border: 1px solid #ddd; padding: 8px;">
    <pre><code>{
      "status": "error",
      "message": "Internal server error. Please try again later and If issue still persists then contact Gupshup Dev Support"
    }</code></pre>
  </td>
  <td style="border: 1px solid #ddd; padding: 8px;">For any Internal Error</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

# Step 4: [Subscription API](/reference/setsubscription-api-v3)

> 📘 Note
>
> This API should be called after the app is successfully linked with Gupshup and is marked live.
>
> Our recommendation is to set a callback during app creation and only set subscription once the live event is received from Gupshup.

<br />

**Partner Portal Setup for Tech Provider** Once you have an approved solutionID, [sign up as a partner](/docs/get-solution-id-from-meta) on the Gupshup partner portal, providing your solution ID. If you are already registered with us on the partner portal, existing ISVs can add their solution details from the settings screen.

**Anything else**, such as service level agreements, services provided, billing processes, etc. This decision will be made jointly by you and Gupshup based on your agreements with Meta.

<br />

## Live Event

### Live event payload

```
{
  "app": "<App Name>",
  "appId": "<App UUID>",
  "phone": "<App Phone Number>"
  "timestamp": 1636986446609,
  "version": 2,
  "type": "onboarding-event",
  "payload": {
    "type" : "docker-status-event",
    "payload" :{
       "status": "live"
       "waId" : "<Phone Number as on Whatsapp>"
    }
  }
}
```
