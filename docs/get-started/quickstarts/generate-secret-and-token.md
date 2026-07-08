---
summary: Generate Secret and Token
title: Generate Secret and Token
slug: generate-secret-and-token
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
# API Client Secret

Generate Client Secrets: Ensure every active user generates a unique Client Secret within their profile. This can be done through ‘Settings’ > API client details. Even if they are non-developers, they must generate the same. If client secret is already generated, they must be rotated and changed.
Recommended expiry for partner’s admin/developers:  Maximum of 3 months
Recommended expiry for non-developers : Earliest date

This client secret is used to generate a **partner token** [GET partner token API](https://partner-docs.gupshup.io/reference/post_partner-account-login). You need to pass the client secret in the password parameter.

<Image align="center" border={true} width="% " src="https://files.readme.io/b30cdc1fde75e276269db46c5624b6f12a9eb02c4d9f801adda31e0fc6d2280b-image_14.png" className="border" />

### Steps to generate a client secret

1. Click on **Create client secret**.
2. Choose the desired expiry date for the client secret. It can be chosen from the calendar or set as never.

   <Image align="center" border={true} width="40% " src="https://files.readme.io/306490f1cac66d3438adb398e5f343a74ddb47e9f431afc527a8f76b3ce00e5c-image_15.png" className="border" />
3. Click on **generate secret**.
4. Copy the client's secret or download the file containing the secret.

   <Image align="center" border={true} width="50% " src="https://files.readme.io/7600dcc1a1b4b54aa8428be09c6c51d33d1d2092fac7a1899cd73016648d6574-image_16.png" className="border" />

> 📘 Note :
>
> For older partner portal users, who have been onboarded before 20th Nov'2024, we have configured their current partner portal password as their client secret, they can continue to pass their current password, in the [GET partner token API](https://partner-docs.gupshup.io/reference/post_partner-account-login) to generate partner token. This has been done to ensure that there is no impact to our older partners.
>
> However, in case you change your password, you will need to generate the client secret via the settings page.
>
> Refer to the [API ](https://docs.gupshup.io/reference/enable-mfa-for-partner-account)document.

## Next step

→ [Send your first message](/docs/send-your-first-message)
