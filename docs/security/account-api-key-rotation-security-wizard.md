---
summary: Account API Key Rotation (Security Wizard)
title: Account API Key Rotation (Security Wizard)
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

## Objective

Rotate partner app tokens and move from account-level API keys to secure app-level API keys.

## Important Notes

* This is a disruptive activity
* Perform during low business hours
* Ensure systems are ready to handle app-level API keys

## Section 1 : Invalidate Account-Level API Key

1. Prepare your system for switching to app level API keys for Self serve APIs

2. Initiate the process of Account level API key rotation during low business hours.  
   **Downtime of ~1 hour is expected**

3. Impact
   * Existing account-level API key becomes invalid within ~1 hour
   * It may take additional time depending on the number of apps which your customers have
   * Messaging traffic will be impacted for ~1 hour for all customer linked with your partner ID

## 2. Rotate App-Level Tokens & Self Serve API Keys

1. Click on Rotate API keys
   * Partner app token, Secondary API key (app level API key) will be rotated

## 3. Download New Keys

* Download API Keys
* Download encrypted file
* Decrypt using your private key

Retrieve:

* New app API keys
* New partner app tokens

## 4. Update Systems

* Replace old tokens & keys with new ones in all environments
* Ensure all services use updated credentials

## Common Checks

* JWT is valid (RS256, correct kid, matching pid)
* Partner ID matches in both JWT and API

## Best Practices

* Do not hardcode keys or tokens
* Store secrets in a secure vault
* Follow “one-in, one-out” during rotation
* Rotate keys quarterly

  <br />

  <br />
