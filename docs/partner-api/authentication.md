---
title: Authentication
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

1. Generate a client secret in Partner Portal → **Settings** → **API client details**
2. Call [Get Partner Token](/reference/post_partner-account-login) with the secret in the `password` parameter
3. Use the returned token in subsequent API requests

See [Generate Secret and Token](/docs/generate-secret-and-token) for step-by-step instructions.

## App access token

For app-level APIs, use [Get Access Token for an App](/reference/get_partner-app-appid-token).

## Security best practices

- Rotate client secrets regularly (recommended: max 3 months)
- See [Security](/docs/security-overview) for MFA and IP allowlisting guides
