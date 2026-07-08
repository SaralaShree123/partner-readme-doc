---
title: Authentication
summary: Partner API authentication with secret and token.
excerpt: Partner API authentication with secret and token.
deprecated: false
hidden: false
metadata:
  robots: index
---

# Authentication

Partner APIs use a **partner token** obtained via your client secret.

1. Generate a secret in Partner Portal → [Generate Secret and Token](/docs/generate-secret-and-token)
2. Exchange secret for token via [Get Partner Token](/reference/post_partner-account-login)
3. Pass token in API requests as documented per endpoint
