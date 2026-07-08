---
title: GUPSHUP PARTNER SECURITY ENFORCEMENT STEPS
deprecated: false
hidden: true
metadata:
  robots: index
---
**Frequency**: Rotate API key/partner access (app) token quarterly at most.

**Scope:** All [http://partner.gupshup.io](http://partner.gupshup.io)   and [http://gupshup.ai](http://gupshup.ai)   accounts, including associated partner app tokens and app apikeys

<br />

# Phase 1: Identity & Access Cleanup

Before rotating keys, you must ensure only authorised individuals have access.

<br />

## Part A: Partner Portal checks -

1. Audit User List: Account owner must log into the [http://partner.gupshup.io](http://partner.gupshup.io)   to review the list of all users.
2. Decommission Accounts: Identify and revoke access of all unused, stale, or suspended users (example - employees who do not work within the company any more), as shown in screen below from the Settings > Users section.

<Callout icon="📘" theme="info">
  THINGS TO NOTE : In case you have trouble revoking the access please reachout to support immediately with subject line: 'Partner Id : [[ID]], Revoke access [[email id]]' and notify your regional CSM for escalation. If any of the user’s email accounts have been compromised, please revoke access of the same user on the partner portal until the audit is completed.
</Callout>

![](https://files.readme.io/c0a00f2add233d867edcca893fe623e2ba3a63dfedfc33f1e41d9f9c86a39e8d-image.png)

3. Password Reset: Ask all active users to reset their passwords by logging out (if logged in), selecting “Forgot Password,” and then logging in again

<Callout icon="📘" theme="info">
  THINGS TO NOTE : If you have trouble resetting access, contact support immediately with the subject line: 'Partner Id  : [[ID]], Unable to reset [[email id]],' and notify your regional CSM for escalation.
</Callout>

<br />

4. MFA Enforcement: Ensure your and all active users' MFA is enabled. All users should see the screen below, enable the toggle in the Partner portal's Settings if not done, and follow the steps.

   ![](https://files.readme.io/9e8d1e1ab179fcb97bfd3ba39f2c00e0fb40d9a350b1cb90bb0b1dfc7d5cb6db-image.png)

<Callout icon="📘" theme="info">
  THINGS TO NOTE : Partners with many users can ask CSM to identify users without 2FA
</Callout>

<br />

<br />

## Part B: Gupshup self-serve checks:

In case you are using [http://gupshup.io](http://gupshup.io)  self-serve as well, please complete below steps:

1. Password Reset:

If you log in to [http://gupshup.ai](http://gupshup.ai) using email and password, the account owner must reset the password. To do this, use the 'Forgot Password' option on the logged-out view and then log in.

If you use SSO (Google, Facebook, GitHub), ensure your passwords are secure and change them periodically.

![](https://files.readme.io/cce34dbf6afde96a6662327af52cf4eede0e3d8e0805ec18a259b550c4bed022-image.png)

<br />

2. MFA Enforcement: Ensure that your MFA/2FA is enabled and activated. (Do not SKIP this step): Follow the steps here

If you are NOT using [http://gupshup.io](http://gupshup.io)  (Self-serve) then you can ignore Part B.

<Callout icon="📘" theme="info">
  THINGS TO NOTE : Strongly recommend not moving to Phase 2 until Phase 1 is complete for all active users on the partner portal and, if applicable, your gupshup.io user. To get the current status of these steps for all users, reach out to CSM
</Callout>

# Phase 2: Client Secret Transition (applicable and mandatory for all partner portal users only)

To move away from insecure/basic username/password authentication for API access, follow these steps:

<br />

1. Generate Client Secrets:

Ensure every active user generates a unique Client Secret in their profile. All users, including non-developers, must generate one. If a client secret exists, rotate and replace it.

* Recommended expiry for partner admins and developers: a maximum of 3 months. Establish processes to enforce this.
* Recommended expiry for non-developers: the earliest selectable date, typically the next day

<Callout icon="📘" theme="info">
  Once generated, the client secret is the only way to create a partner token. If it expires, users cannot generate a partner token, even with a username and password. Therefore, non-developer users must generate a client secret with immediate expiry.
</Callout>

![](https://files.readme.io/e8ad617eefc2b019a2f876e45d0cd17dd7a8c89172bf6bdfe2f92e14ce76a1cd-image.png)

![](https://files.readme.io/5a5748428553e3adc65e8953f8b145e6d01745210ec551950ecf42f857cd5e64-image.png)

<br />

2. Deprecate Password Auth: Update all internal scripts, services, or code to stop using username and password for partner token generation API authentication.
3. Validate Secret-Based Auth:

This client secret generates a partner token using the GET partner token API. Pass the client secret in the password parameter to use this API.

The logic is:

Input: Client Secret

Output: Partner Token

<Callout icon="📘" theme="info">
  Once Phase 2 is complete, partners should contact their regional CSMs to confirm completion of phase 2 and request proceeding with phase 3 which will help you with key Rotation and Whitelisting. The Phase 2 completion flag has to be enabled manually by Gupshup. After your CSM confirms this flag is enabled by Gupshup, log out and log back in to the partner portal. Then, you will see a new option, “Advanced Settings” in the left navigation. Carry on with Phase 3 from this moment.
</Callout>

<br />

# Phase 3: Verify your contact phone number on partner portal

This step is done at a partner level - It will involve 2 people from the partner user list -

1. These steps CAN only be done with the help of the ‘Owner user’ of your Gupshup partner ID
2. These steps should only be done by the Developer (consumer of the APIs).

For these steps, you will need a phone number for whitelisting your IPs or bulk token/apikey rotation. This phone number will stay as the authentication mechanism in future for such critical activities - such as the ones in Phase 4 and 5. You can add and verify your contact phone number in the Advanced Settings section.

![](https://files.readme.io/e47ee1a78d344d659fe5f8bc7d869e09f3881cb046731839a3de6e02f4ccffd7-image.png)

You will receive the OTP on WhatsApp

![](https://files.readme.io/d38b019ecf086418e9a6b226aec556fff8ee096e6a797c00eb942c47a58832ee-image.png)

After entering the OTP, you will see the screen below. Please inform your allocated CSM to get approval at this step.

![](https://files.readme.io/99c5b768c65ebd4d4dec3ac91b7f075972a045a9a042bfa4eb8f15b8cde7a5e3-image.png)

Once we verify that you set this phone number, you will see the screen below.

![](https://files.readme.io/f3c4bddb35923e14d11634ad51025e5348ae346a8ae3953db313e9110cef41fe-image.png)

<br />

<br />

# Phase 4: (Optional) IP whitelisting - Secure youraccount and WaBa management when you managing apps for customers - Recommended.

This activity secures all your WaBa and app management tasks by processing requests at Gupshup SS and Partner Portal only from submitted IPs. It covers app management, template management, WaBa management, business profile updates, onboarding, embed signup flow, health info, messaging tier/quality, media management, wallet management APIs— basically all APIs using endpoint apps/[[app_id]]. Keep the number of IPs low to reduce risks.

You can add IPs to whitelist under Advanced Settings. To whitelist your IPs, verify yourself via OTP sent to your email (owner account) and phone number (OTP will be received on WhatsApp) set in Phase 3. When ever you add or remove the IPs you are required to verify via OTP.

![](https://files.readme.io/9900265c776c496c435f7f5a1189cf495d8784a820f4e2b95b4f38c779ad74f3-image.png)

![](https://files.readme.io/44381b5c36199c625a73b8877a84e74e0c3869f36cfbfb90278bea65d26be9eb-image.png)

<br />

<Callout icon="📘" theme="info">
  Messaging is not covered by IP whitelisting. This approach fails for partners with dynamic IPs.
</Callout>

If you have trouble submitting your IPs or need more information, please contact your CSM.

<br />

# Phase 5: App Linking Cleanup

1. Ensure all your apps are linked correctly to your partner account.
2. If you find apps linked to your partner account that aren't yours, report immediately to support with the subject: 'Partner id :  [[ID]], Identified unknown apps linkage.' This can occur when your customers create and manage apps on their own Gupshup accounts.

<br />

<br />

# Phase 6:  [Disruptive] Moving from Account Level API key to App Level API keys (applicable only for api.gupshup.io API usage) + Rotating Partner App Tokens

<Callout icon="📘" theme="info">
  This phase will disrupt your outbound message API calls and any API consuming an API key or partner app token for authorization. Please read carefully and prepare to act quickly during low business hours from this point onward
</Callout>

<br />

## Part A: **[Disruptive]** Invalidate the account-level API key (applicable only for api.gupshup.io API usage)

1. Get your systems ready for app-specific API keys - Account-level API keys that supported authentication for all apps within a customer ID must now be replaced with app-level API keys. Your mapping will change from one-to-many to one-to-one.

<Callout icon="📘" theme="info">
  API signatures remain unchanged and will work with app-level API keys. You must build a provision to replace account-level API keys with app-specific API keys before performing the following steps. Please read Phase 6: Part B before proceeding.
</Callout>

<br />

2. Invalidate Account API Key: by following these steps:
   This is a disruptive step, but necessary for a successful cleanup. Take quick actions as mentioned below in low business hours from this step onwards -

a. Visit [https://www.gupshup.io](https://www.gupshup.io)

b. Log in to your account with MFA

c. Once logged in, go to the following URL: [https://www.gupshup.io/developer/reset-apikey](https://www.gupshup.io/developer/reset-apikey)

d. Click on the "Reset API Key" button.

![](https://files.readme.io/b3106758e3cac7e4bbe47320fa4c5af88c6f18df88d14bec6c637516b8bfa58f-image.png)

e. The invalidation process will start, and after 10 seconds, your current access will be revoked. You will be redirected to the homepage to log in again. You will no longer be able to use the account-level API key.

<br />

## Part B: App-level API key and Token Refresh

<Callout icon="📘" theme="info">
  This phase will disrupt your outbound message API calls and any API consuming an API key or partner app token for authorization. Please read all below steps carefully before starting and prepare to act quickly during low business hours from this point onward
</Callout>

<br />

**Familiarities with terms and concepts**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Term
      </th>

      <th>
        Simple meaning
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Private key
      </td>

      <td>
        A secret file that stays only on your servers. You use it in your code to sign JWTs. Never send this to Gupshup or anyone else.
      </td>
    </tr>

    <tr>
      <td>
        Public key
      </td>

      <td>
        A file you upload into the Gupshup Partner Portal. Gupshup uses it to check that your JWT was really signed by your private key.
      </td>
    </tr>

    <tr>
      <td>
        JWT
      </td>

      <td>
        A JSON Web Token. It is just a string you send in the Authorization header. It proves “this call is from this partner”.
      </td>
    </tr>

    <tr>
      <td>
        RS256
      </td>

      <td>
        The algorithm used to sign the JWT with your RSA private key. Always use RS256 here.
      </td>
    </tr>

    <tr>
      <td>
        kid (key id)
      </td>

      <td>
        A name/identifier for your public key. It goes in the JWT header. Gupshup uses this to find which public key to use to verify your JWT. It can be the key id that the portal shows or the tag/label you set.
      </td>
    </tr>

    <tr>
      <td>
        pid
      </td>

      <td>
        Partner ID. A string inside the JWT body (payload). It must match the [partnerId] in the API URL for APIs that check it.
      </td>
    </tr>

    <tr>
      <td>
        Two logins
      </td>

      <td>
        You log into the Partner Portal with your username/password (and possibly MFA) to configure keys.

        Your backend code calls APIs using JWTs signed with your private key. The JWT is not your portal login session.
      </td>
    </tr>
  </tbody>
</Table>

<br />

This section introduces a new authentication method for the key admin API to secure token and key regeneration. It covers:

* [ ] Create an RSA key pair (private and public) to obtain two files:
  * private_key.pem
  * public_key.pem

* [ ] Upload the public key to the Gupshup Partner Portal by logging in as a user authorized to manage keys. Add your public key in Partner Portal → Advanced Settings:
  * Paste the entire public key, including lines like -----BEGIN PUBLIC KEY-----.
  * Assign a unique tag/label (e.g., prod-rotation-2025).
  * Save it. Note the key id (if shown) and your tag.

* [ ] Create (sign) an RS256 JWT with your private key in your backend app:
  * Load the private key from private_key.pem.
  * Create an RS256 JWT with a short expiry (~60 minutes).
  * Include kid in the JWT header.
  * Include at least pid, iat, and exp in the JWT body.

* [ ] Call the App Key & Token Rotation API using that RS256 JWT in your API header. This API rotates both the partner app token and app API key.

```
Authorization: Bearer <your-jwt>
```

* [ ] Retrieving the rotated tokens and API keys
* [ ] Decrypt the downloaded file containing refreshed/rotated partner app token and API keys using your private key.

If you follow this step-by-step, you should be able to implement it in code.

<br />

### Step 1 – Create the RSA key pair

Depending upon your OS you can decide which approach to follow:

**Approach 1: Generate an RSA key pair on Linux or macOS using OpenSSL.**

Run these commands in a terminal:

<br />

```
# 1. Create private key (keep this SECRET)
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 2. Create public key (this will go to Partner Portal)
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

You will now have:

* private_key.pem – used in your code
* public_key.pem – uploaded to Partner Portal

<br />

**Approach 2: Generate an RSA key pair on Windows**

1. Using Git Bash / WSL / OpenSSL
   Use the same commands as above (Linux/macOS).
2. Pure PowerShell (no OpenSSL):

```
$rsa = [System.Security.Cryptography.RSA]::Create(2048)
$private = [Convert]::ToBase64String($rsa.ExportPkcs8PrivateKey())
"-----BEGIN PRIVATE KEY-----`n$private`n-----END PRIVATE KEY-----" | Out-File private_key.pem
$public = [Convert]::ToBase64String($rsa.ExportSubjectPublicKeyInfo())
"-----BEGIN PUBLIC KEY-----`n$public`n-----END PUBLIC KEY-----" | Out-File public_key.pem
```

After receiving the file, check its format when opening it:

* Private key should start with: -----BEGIN PRIVATE KEY-----
* Public key should start with: -----BEGIN PUBLIC KEY-----

If your existing private key says BEGIN RSA PRIVATE KEY, you need to convert it to PKCS#8:

```
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
  -in private_key.pem -out private_key_pkcs8.pem
```

Then use private_key_pkcs8.pem in your code.

<br />

### Step 2 - Upload the public key in Partner Portal

1. Log into the Partner Portal.
2. Go to Advanced Settings → Signing Secret Encryption.

   ![](https://files.readme.io/7290f5a184edb2794eb9bc15863742ff3f0bbb704f68bb28d52beab13753ee1c-image.png)
3. Click to Add key.
4. Paste the full content of public_key.pem, including:

* -----BEGIN PUBLIC KEY-----
* -----END PUBLIC KEY-----

5. Give it a unique tag/label, e.g. prod-rotation-2025.
6. Save. The portal may show a key id.
   * Note both the key id and tag.

![](https://files.readme.io/9eb869448be2dcb334df03f205528d53ca17b3e72d7bbfd787517e90cabb159f-image.png)

<br />

**Important for later:**
The JWT header kid must be set to either:

* The key id from the portal or
* The tag/label you entered

The key must be active for your partner.

<br />

### Step 3 – Build the RS256 JWT which is required to call the App Key & Token Rotation API

You can create the JWT in your backend using a library as per your preferred coding language. For ease we have shared various language sample code below. First understand what must be inside the JWT.

1. JWT Header (fixed structure)

```
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "<your-key-id-or-tag>"
}
```

<br />

* alg must be exactly RS256
* typ is JWT
* kid = the key ID or tag representing the key you registered is the same key you received in Step #2

<br />

2. JWT Payload (body) – claims

At minimum, you need these:

| Claim | Required?             | Meaning                                                                                                                               |
| :---- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| pid   | Yes (for strict APIs) | Your partner id (string). Must match [partnerId] in the URL.                                                                          |
| iat   | Strongly recommended  | Time when token is created, in Unix seconds.                                                                                          |
| exp   | Strongly recommended  | Expiry time, in Unix seconds. Should be shortly after iat. Keep the expiry short as the rotate credentials API is a limited activity. |

<br />

Example:

```
{
  "pid": "12345",
  "iat": 1711360000,
  "exp": 1711363600
}
```

<br />

There is also an optional expat field (Unix seconds) that the server may use as extra expiry, but you can ignore it initially unless asked to add it.

Token lifetime (how long it should live):

* Recommended: max 60 minutes between iat and exp
* You can:
  * Create a new JWT per request, or
  * Reuse it for a short duration (like 30–60 min) then refresh
  <br />

3. Code samples – how to sign a JWT

Pick the language your team uses:

* Read private_key.pem
* Create a JWT with:
  * header: alg=RS256, kid=\< kid>
  * payload: pid=\< partnerId >, iat, exp
  <br />
* Print the token string (this goes into Authorization: Bearer \< token >)

<br />

Option 1: Java (using Auth0 java-jwt 4.4.0)

Add dependency (Maven):

```
<dependency>
  <groupId>com.auth0</groupId>
  <artifactId>java-jwt</artifactId>
  <version>4.4.0</version>
</dependency>
```

Code:

```
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.interfaces.RSAPrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Base64;
import java.util.Date;

public class JwtGenerator {
  public static void main(String[] args) throws Exception {
    // 1. Read private key file
    String pem = new String(Files.readAllBytes(Paths.get("private_key.pem")))
        .replaceAll("-----\\w+ PRIVATE KEY-----", "")
        .replaceAll("\\s", "");
    byte[] keyBytes = Base64.getDecoder().decode(pem);

    // 2. Build RSAPrivateKey object
    PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
    RSAPrivateKey privateKey =
        (RSAPrivateKey) KeyFactory.getInstance("RSA").generatePrivate(spec);

    // 3. Create JWT
    Algorithm algorithm = Algorithm.RSA256(null, privateKey);
    long now = System.currentTimeMillis();
    String token = JWT.create()
        .withKeyId("<kid>")                   // <-- replace with your key id/tag
        .withClaim("pid", "<partnerId>")      // <-- replace with your partner id
        .withIssuedAt(new Date(now))
        .withExpiresAt(new Date(now + 3_600_000)) // 1 hour
        .sign(algorithm);

    // 4. Print token
    System.out.println(token);
  }
}
```

<br />

Option 2: Python (PyJWT)

Install:

```
pip install PyJWT cryptography
```

Code:

```
import jwt
import time

# 1. Read private key
with open("private_key.pem", "r") as f:
    private_key = f.read()

now = int(time.time())

# 2. Create payload
payload = {
    "pid": "<partnerId>",  # replace with your partner id
    "iat": now,
    "exp": now + 3600,     # 1 hour
}

# 3. Create token
token = jwt.encode(
    payload,
    private_key,
    algorithm="RS256",
    headers={"kid": "<kid>", "typ": "JWT"}  # replace <kid> with your key id/tag
)

print(token)
```

Option 3: Node.js (jsonwebtoken)

Install:

```
npm install jsonwebtoken
```

Code:

```
const jwt = require("jsonwebtoken");
const fs = require("fs");

// 1. Read private key
const privateKey = fs.readFileSync("private_key.pem");

// 2. Create token
const token = jwt.sign(
  { pid: "<partnerId>" },          // payload
  privateKey,                      // private key
  {
    algorithm: "RS256",
    expiresIn: "60m",              // 1 hour
    keyid: "<kid>",                // your key id/tag
  }
);

// 3. Print token
console.log(token);
```

Option 4: Go ([http://github.com/golang-jwt/jwt/v5](http://github.com/golang-jwt/jwt/v5))

```
package main

import (
    "fmt"
    "os"
    "time"

    "github.com/golang-jwt/jwt/v5"
)

func main() {
    // 1. Read private key file
    keyData, err := os.ReadFile("private_key.pem")
    if err != nil {
        panic(err)
    }

    // 2. Parse private key
    privateKey, err := jwt.ParseRSAPrivateKeyFromPEM(keyData)
    if err != nil {
        panic(err)
    }

    // 3. Define claims
    claims := jwt.MapClaims{
       "pid": "<partnerId>",                  // replace with your partner id
       "iat": time.Now().Unix(),
       "exp": time.Now().Add(time.Hour).Unix(), // 1 hour
    }

    // 4. Create token
    t := jwt.NewWithClaims(jwt.SigningMethodRS256, claims)
    t.Header["kid"] = "<kid>"                  // replace with your key id/tag

    // 5. Sign token
    signed, err := t.SignedString(privateKey)
    if err != nil {
        panic(err)
    }

    fmt.Println(signed)
}
```

<br />

### Step 4: The App Key & Token Rotation API

1. What this API does?

=> Rotates (changes) the access tokens for your apps.
=> Old tokens become invalid; new tokens are issued → improves security.

<Callout icon="📘" theme="info">
  This step once performed cannot be undone
</Callout>

##### => Optional extra behavior: if you pass rotateApikey=true, it can also trigger reseting of your self-serve platform app level apikey. This is a must step for partners.

<br />

2. What is the behavior of this API:

=> The API responds fast with HTTP 200 and a jobId. This means the activity has started. An async process runs in the background.  
=> The rotation continues in the background. Only apps linked to your partner id are rotated.  
=> You will receive an email (sample below) when the rotation finishes. Callback/webhook events are coming soon. This email confirms completion and will include:  
a. JobId  
b. Total apps processed  
c. Partner ID  
d. Optionally, a CSV listing app IDs.

<Callout icon="📘" theme="info">
  This phase causes downtime until you download the refreshed partner app token and API keys.
</Callout>

![](https://files.readme.io/eda3b648ea9da8b9370e4ca13eb7490f9869ebdc64410caeb9e5798c6744161d-image.png)

3. The App Key & Token Rotation API and its documentation:

URL Endpoint:

```
https://partner.gupshup.io/partner/account/rotate/keys/partner/[[partnerId]]
```

\< PARTNER_ID > must match the pid inside the JWT, and your actual partner id.

Query/body params:

| Parameter    | Where              | Required | Meaning                                                                                                                                     |
| :----------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| partnerId    | Path               | Yes      | Put in the URL as \< PARTNER_ID >. Must match pid in RS256 JWT.                                                                             |
| appList      | Query or form body | No       | List of application IDs to rotate. If you skip this, all apps for your partner are rotated. You can send multiple IDs as appid1,appid2 etc. |
| rotateApikey | Query or body      | No       | Default false. If true, also triggers reseting of your self-serve platform app level apikey. This is a must step for partners.              |

Authentication header:

```
Authorization: Bearer <RS256_JWT>
```

The \< RS256_JWT > is what you generated in Phase 5 -> Part B -> Step 3 using your private key.

Example:

Request:

```
curl --request POST \
  --url "https://partner.gupshup.io/partner/app/<PARTNER_ID>/key/app/rotate?rotateApikey=false" \
  --header "Authorization: Bearer <RS256_JWT>" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "appList=appid1,appid2"
```

* Replace \< PARTNER_ID > with your partner id.
* Replace \< RS256_JWT > with the token you generate.
* To rotate all apps: simply omit appList.

Success response (HTTP 200)

```
{
  "status": "success",
  "message": "Token rotation started successfully",
  "jobId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

<br />

* Store this jobId in your logs.
* If you contact CSM or support related to this Phase always mention this jobId.

Typical error responses:

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        #
      </th>

      <th>
        Error case
      </th>

      <th>
        HTTP status
      </th>

      <th>
        Example response (code block)
      </th>

      <th>
        Meaning / What to do
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        Invalid app IDs
      </td>

      <td>
        400 Bad Request
      </td>

      <td>
        [
        "status": "error",
        "message": "Invalid appIds: [app999, invalidApp]"
        ]
      </td>

      <td>
        One or more IDs don’t belong to your partner.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        Partner not found
      </td>

      <td>
        400 Bad Request
      </td>

      <td>
        [
        "status": "error",
        "message": "Partner does not exist"
        ]
      </td>

      <td>
        Verify partnerId in URL and pid in JWT.
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        No apps to rotate
      </td>

      <td>
        400 Bad Request
      </td>

      <td>
        [
        "status": "error",
        "message": "No apps found for partner"
        ]
      </td>

      <td>
        No apps linked or appList resolved to none.
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        Rate limit hit
      </td>

      <td>
        429 Too Many Requests
      </td>

      <td>
        [
        "status": "error",
        "message": "Too many requests."
        ]
      </td>

      <td>
        Maybe you called it too many times. Wait until the window resets.
      </td>
    </tr>
  </tbody>
</Table>

<br />

| Problem                       | What to check                                                                                                                    |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Invalid app IDs               | Confirm each ID in appList belongs to your partner.                                                                              |
| Rate limit                    | Maybe you called it too many times. Wait until the window resets. Rate limit is 2/24 hours                                       |
| Authorization errors          | Check JWT: algorithm is RS256, kid matches active key, pid matches URL partnerId, token not expired.                             |
| Got 200 but behavior is       | Your partner has no apps linked or your appList is wrong.                                                                        |
| Issues with rotateApikey=true | Portal tokens may rotate fine; WhatsApp-side steps may still fail. Use support with jobId if you still see WhatsApp auth issues. |

<br />

How the server checks your JWT when you call the API:

1. Read kid from the JWT header.
2. Find the active public key for your partner matching that kid (by key ID or tag).
3. Verify the JWT signature using that public key and the RS256 algorithm.
4. Check that pid in the payload matches the partnerId in the URL (for APIs that enforce this).
5. Confirm the token is not expired (exp, and expat if present).

If any check fails, you’ll get an authorization error.

<br />

### Step 5: Download the Partner app token and SS app-level apikeys

After receiving email confirmation that the activity is complete, follow these steps to download and update your production/staging environments with the new App level apikeys and partner app tokens to prevent service interruption.

1. Go to Advanced settings and click “Download API Keys.”
2. You will receive an encrypted blob file.
3. Use your private key to decrypt the file and retrieve the refreshed App apikeys and Partner app token.
4. Automate decryption, token retrieval, and updating of your relevant systems

<Callout icon="📘" theme="info">
  Please periodically check your account using the steps above to maintain secure and a healthy experience.
</Callout>

Inform your CSM once you have completed these steps.

<br />

### Rotating your signing keys (your keys, not app tokens)

When you want to rotate your signing keys (for JWT):

1. Generate a new RSA key pair (private + public).
2. Add the new public key in Partner Portal → Advanced Settings with a new tag.
3. Update your backend code to:

* Load the new private key
* Use the new kid in JWT header

4. Once the new flow is working, delete the old public key from the portal.

<br />

<br />

### Security Best Practices

* No Hardcoding: Never store the Client Secret or Partner Tokens in source code. Use a Vault like AWS Secrets Manager or HashiCorp Vault.
* The "One-In, One-Out" Rule: When rotating, ensure the new secret works before deleting the old one to avoid downtime (if the platform allows overlap).
* Never share your private key file.
* Never commit the private key to Git or send it by email, Slack, etc.
* Store the private key in a secure secret manager in production.
* Always use HTTPS (TLS) for API calls
* Use short-lived JWTs (1 hour or less).
* If you think a key is compromised:

a. Create a new key pair

b. Add the new public key in Advanced Settings with a new tag

c. Update your code to use the new private key and new kid

d. Remove the old public key from the portal when unused

<br />
