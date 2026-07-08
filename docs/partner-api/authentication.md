---
title: Authentication
icon: fa-duotone fa-lock
summary: How to authenticate Partner API requests.
excerpt: How to authenticate Partner API requests.
deprecated: false
hidden: false
metadata:
  robots: index
slug: authentication
---

# Authentication

## Partner token

1. In Partner Portal go to **Settings → API client details**
2. Generate a **client secret**
3. Call [Get Partner Token](/reference/post_partner-account-login) with the secret in the `password` parameter
4. Use the returned token on subsequent Partner API calls

Step-by-step UI guide: [Generate Secret and Token](/docs/generate-secret-and-token)

## App access token

For app-level APIs, use [Get Access Token for an App](/reference/get_partner-app-appid-token).

## Related

- [Partner Management](/docs/partner-management)
- [Security Overview](/docs/security-overview)
