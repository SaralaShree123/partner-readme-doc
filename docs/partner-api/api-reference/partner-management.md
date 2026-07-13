---
title: Partner Management
icon: fa-duotone fa-user-gear
summary: Endpoints for managing partner accounts, authentication, and app linking.
excerpt: Endpoints for managing partner accounts, authentication, and app linking.
deprecated: false
hidden: false
metadata:
  robots: index
slug: partner-management
---

# Partner Management

Use these APIs to authenticate as a partner, list linked apps, and link a Gupshup application to your partner account. Start here before calling app-scoped messaging or WABA APIs — most other Partner APIs require a partner token from this category.

## Get Partner Token

> Authenticate with your partner email and client secret to obtain a partner token. Use this token as authorization for other Partner APIs (token expiry is time-limited).

→ Full endpoint & Try It: [/reference/post_partner-account-login](/reference/post_partner-account-login)

## Get Partner Apps

> Retrieve the list of applications linked to the authenticated partner account, including health and capping details where available.

→ Full endpoint & Try It: [/reference/get_partner-account-api-partnerapps](/reference/get_partner-account-api-partnerapps)

## Link App with Partner

> Link a Gupshup application to your partner account using an API key and app name so you can manage it via Partner APIs.

→ Full endpoint & Try It: [/reference/post_partner-account-api-applink](/reference/post_partner-account-api-applink)
