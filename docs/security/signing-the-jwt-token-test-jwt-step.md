---
summary: Signing the JWT Token (Test JWT Step)
title: Signing the JWT Token (Test JWT Step)
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

## Objective

Generate and sign a JWT using your private key to authenticate API requests.

## Steps

### 1. Prepare your keys

Ensure you have an RSA key pair:

* `private_key.pem` → Used in your backend (keep secure)
* `public_key.pem` → Already uploaded in Security Wizard

Note the key ID (`kid`) or tag from the portal.

### 2. Create JWT Header

* Algorithm must be `RS256`
* Include your key identifier (`kid`)

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "<kid>"
}
```

<br />

### 3. Create JWT Payload

Include the following fields:

* **pid** → Your Partner ID (must match the API `partnerId`)
* **aid** → App ID for app APIs
* **iat** → Current time (Unix seconds)
* **expat** → Expiry time (recommended: within 60 minutes)

```json
{
  "pid": "<partnerId>",
  "aid": "<appId>",
  "iat": <current_time>,
  "expat": <current_time + 3600>
}
```

<br />

### 4. Sign the JWT

<br />

* Use your private key (`private_key.pem`)
* Use algorithm: `RS256`
* Generate the token using your backend (`Java`, `Python`, `Node.js`, etc.)

### 5. Validate the JWT

* Ensure the following :
  * `kid` matches the uploaded public key
  * `pid` matches your Partner ID
  * `aid` matches your App ID (if applicable)
  * Token is not expired

* Use this token in API requests:

  ```http
  Authorization: Bearer <your-jwt>
  ```

<br />

### Best Practices

* Never expose your private key
* Generate a new token periodically### Best Practices

<br />
