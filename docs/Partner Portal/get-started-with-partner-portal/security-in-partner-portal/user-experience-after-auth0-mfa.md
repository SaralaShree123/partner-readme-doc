---
title: User Experience After Auth0 & MFA
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
# Using Auth0 & Multi-Factor Authentication (MFA) in the Partner Portal

## Purpose

This is a detailed guide for users to use Multi-Factor Authentication (MFA) via Auth0 when accessing the Partner Portal. We are moving to Auth0 as the authentication mechanism for Partner Portal to enhance the security of partner portal applications. Additionally, MFA enhances security by requiring multiple factors for  verification during login.

## User flows

### Signup on Partner Portal

1. Access the Partner Portal:

   1. Open your web browser and navigate to the [partner portal sign-up](https://partner.gupshup.io) page.

   <Image align="center" className="border" border={true} width="80% " src="https://files.readme.io/c0795084bb9b4d20f951a407b4f797264fbbd059931e5a4e75835318fe22b0a2-image_18.png" />
2. Enter Your Credentials:
   1. Enter your first and last name
   2. Enter email and password in the respective fields.
   3. Enter the given security code (captcha).
3. Click **Signup**.
   1. Click the Signup to proceed.
4. You will need to verify your email address by clicking on the link sent to your registered email address.

<Image align="center" className="border" border={true} width="50% " src="https://files.readme.io/a96367477deaa292440a9c8a3681e76bf2349a8ac6690d30e2b2f7c85cf7ba11-email-verification.png" />

### Forgot your password

To reset the forgot password, follow the below steps:

1. Go to the partner portal login page.
2. Click the Forgot Password link below the login fields.

   <Image align="center" className="border" border={true} src="https://files.readme.io/1c253b9ced298d2b38f8c684bfa71494fd17974702f23202a19b681b6c2f5d10-forgot-pwd.png" />
3. Provide the email address associated with your account.
4. Click the Send verification mail button.
5. Check your email for a password reset link. If you don’t see it, check your spam or junk folder.

   <Image align="center" className="border" border={true} src="https://files.readme.io/8f853093ad6f3b3cd9c8fbc889e296c1f5b06edb9cd06fc1d6752b8b353fd594-image-2.png" />
6. Click the Reset your password link in the email.  It redirects to the password reset page.

   <Image align="center" width="50% " src="https://files.readme.io/48df69b2f0cf648d4dc1479273b263f8567cbef10204c1c87bcd8bc987c9253b-image-17.png" />
7. Enter and confirm a new password, ensuring it meets the password policy requirements (e.g., minimum 8 characters, includes a mix of letters, numbers, and symbols).

   <Image align="center" className="border" border={true} src="https://files.readme.io/362019a83e7514a1aaf69cb9664a7677a091ed9bfee7efb3c558228fe7b78164-image-4.png" />
8. Click **Reset password**.
9. If MFA is enabled for your account, you may be required to verify your identity after resetting your password.
10. Return to the login page and use your new password to access your account.

## Adding Partner Users

> 📘 MFA should be enabled & configured by your partner admin

1. Access the Partner Portal Settings page for a Partner Admin to add a partner user email

<Image align="center" src="https://files.readme.io/3be055c808df1e3c6ad6f72c0405ee91c58ab3f100b42db97bbb1fef884d3dc5-AD_4nXfMc7woCdliiZ5rmGpTxOoh38a3sOy7TS1QpSbN-EpbUV-y2PhSN7Beme31wAY18TSMpmAyD4ZgdxkB0HmaHlRjFTrm9UQWGIYEC5gpjS5LY-Qv42P7aNlg.png" />

2. Click on the Add Button and Partner User will be in the Invited state:

<Image align="center" src="https://files.readme.io/6b0c726adedc05552a323f50caa3527364a0c1dfd376dfaf90f8760b6268d664-AD_4nXcfXxuiGEsgPSnI2gLop0UR9LpSqowLCEw7s2979Mdi128eLVnipJFqBgAdQfyBj0rKG6P3qsCDhmraEW4Qfus-ddOpUfgHWamA_8DjIlU7zKDTg4FmRqKQ.png" />

3. Partner users will receive an invitation email to accept the invitation.

<Image align="center" src="https://files.readme.io/e585dbc112272556475b539d3f04f5ccf6d20e9bd9da5263797c7dbbb4a81892-AD_4nXf-xxhaxNp4pvrcvzt-Zpk6Iux8uOabZQ114RaElMzhKpZ3D-ctt2YWQCQriRLLG535AmG5SlFajXYtAaK9SY2zAXCRgBijEBYxi25VUHWs12OV3lEiU8Ur.png" />

4. Upon clicking the link, the partner user will be redirected to the sign-up page.
   1. Enter your first and last name
   2. Enter the password in the respective fields.
   3. Enter the given security code (captcha).
   4. Click the Signup to proceed.

<Image align="center" src="https://files.readme.io/2f96bc42820e7e086d880ddd2b7ccb7a8e441967021386b0b717222be6658be0-AD_4nXeCMsKxOFo5kFbQF7uS2OkeUTUpTBkZ4TKhvgLdaqD8vz2gthlEHNnBQ9c4ggtk6XQuenP5Otn8gUsKjeRCU14rFIzd4X5CBpDgWHjMNF1J6WI9jfvEP3Lz.png" />

5. After successfully signing up the following page is seen with the Back to Login button:

<Image align="center" src="https://files.readme.io/7505e366fed9f72a56dd4cd6cfdff4d75cc49118ecef68b5e21553cfac0283f4-AD_4nXcXzVHzlncDMCgz9VnHa-14jU83SbnHPTd20HbPJDHPUuGK-TfotZr4KBQ0MCd7gAbFIF0q6akht4WA-oMB58ue2uHhNKsn626oLMv64E-JcQ69BMojCPjV.png" />

6. After successful login, the partner user can log in with valid credentials. Upon successful login, the partner user will be prompted to choose a method for setting up MFA verification

<Image align="center" src="https://files.readme.io/b36f5c27adbb4612f4020aca8358bc01022ee5359402d8d786d137d50cfcae7c-AD_4nXeonXlTXXXEONNln0sOH7hsVyvbCjwha7BZnzyetpIBeJjWH7Dgfzl4uBexn6P1DVEIfTCyBiFK7zQlLvl1Ewe0b6-no83pjCZPaWjoe45q1_wfH2Q1Dj0x.png" />

7. Partner users can choose to log in using an authenticator app.
   1. Scan the QR code to link your partner portal login with the following authenticator app like
      1. Authy
      2. Google Authenticator
      3. Auth0 Guardian
      4. Microsoft Authenticator
   2. Open the authenticator app to retrieve the OTP. (this is a short OTP generated, and valid for 60 seconds).

<Image align="center" src="https://files.readme.io/da72bd4dbbc3649e9e3cee0371ac35a40b958d11e08a0fa82023b4db070ff0fb-AD_4nXcB5nSSzzGoAcxtBontPUXXfZx9SbwulWleKtewBIGGAHKev9sxJiqnvPi4a1yX9fF89nguDkYnQCRZ-DsvsUhWENezq9RtpvXm2r8vyv50-CMVhfII3vqt.png" />

8. If not authenticator code the partner user can choose to set up MFA with verify OTP via email

<Image align="center" src="https://files.readme.io/a20bcbc0e48aa48456b7258c13b36a536823ad7173cc497538862028b386eb74-AD_4nXepmmPXnmKMHVjMGU8CDvijaA9JsxvQxKyoYzVnwo2j6m3PiTkD0GHQ8XqptS4xOjTs0G8AuW_4AZQJYG6RKSNXFyJiwqN7PxZ1wwI-KRsM97GrCFUXviqn.png" />

9. Upon choosing this option, the partner user will receive an OTP on the registered email address.

<Image align="center" src="https://files.readme.io/a4c1a8e6072d4246394389df03905ab809b4b4dd2422371a9452f2c7b2c10cd4-Verification_Code_779359.png" />

## API Client Secret

Developers can generate their client secret from settings page in partner portal. This client secret can be used to generate a partner token using [GET partner token API](https://docs.gupshup.io/reference/post_partner-account-login). You need to pass the client secret in the password parameter.

<Image align="center" className="border" border={true} width="% " src="https://files.readme.io/b30cdc1fde75e276269db46c5624b6f12a9eb02c4d9f801adda31e0fc6d2280b-image_14.png" />

### Steps to generate a client secret

1. Click on **Create client secret**.
2. Choose the desired expiry date for the client secret. It can be chosen from the calendar or set as never.

   <Image align="center" className="border" border={true} width="40% " src="https://files.readme.io/306490f1cac66d3438adb398e5f343a74ddb47e9f431afc527a8f76b3ce00e5c-image_15.png" />
3. Click on **generate secret**.
4. Copy the client's secret or download the file containing the secret.

   <Image align="center" className="border" border={true} width="50% " src="https://files.readme.io/7600dcc1a1b4b54aa8428be09c6c51d33d1d2092fac7a1899cd73016648d6574-image_16.png" />

> 📘 Note :
>
> For older partner portal users, who have been onboarded before 20th Nov, we have configured their current partner portal password as their client secret, they can continue to pass their current password, in the [GET partner token API](https://partner-docs.gupshup.io/reference/post_partner-account-login#/) to generate partner token. This has been done to ensure that there is no impact to our older partners.
>
> However, in case you change your password, you will need to generate the client secret via the settings page.
>
> Refer to the [API ](https://docs.gupshup.io/reference/enable-mfa-for-partner-account)document.

## Step-by-Step Procedure for Partners with MFA enabled

### Step 1: MFA Configuration

> 📘 Note :
>
> MFA will be enabled via support, please write to [partner.support@gupshup.io](mailto:partner.support@gupshup.io) to enable MFA for your partner portal account.

1. Once support has enabled MFA for your partner portal account, after entering your credentials, you will be prompted to choose a  method for additional verification:

   <Image align="center" className="border" border={true} src="https://files.readme.io/1ba62db623d92495a4c7feaebbe6d6ef9c74cf978d1e4941330705366d9dc4a3-image-11.png" />
2. You will receive a One-Time Password (OTP) via email or through your authenticator app.

   1. Check your email.
   2. Enter the OTP in the designated field on the login page.
   3. Click "Verify" to complete the login process.

      <Image align="center" className="border" border={true} width="60% " src="https://files.readme.io/404fc59e211714fa85880ffa6d3c668f1c4b1aa74ada219d52ae48b2e72e3d72-MFA.PNG" />
3. You can choose to login using an authenticator app.
   1. Scan the QR code to link your partner portal login with the following authenticator app like
      1. [Authy](https://docs.gupshup.io/docs/authy-authenticator-app-for-partner-portal)
      2. [Google Authenticator](https://docs.gupshup.io/docs/google-authenticator-for-partner-portal)
      3. Auth0 Guardian
      4. Microsoft Authenticator
4. In case you are unable to scan the QR code, please copy the one-time/i code and enter it in the authenticator app.

   <Image align="center" className="border" border={true} src="https://files.readme.io/6f3b3f02c54134eba58639aff254b7e5f4e74feba1ca5e1c9e74954ac160aca7-image-20241015-050006.png" />
5. Open the authenticator app to retrieve the OTP. (this is a short OTP generated, and valid for 60 seconds).

### Step 2: Login into the Partner Portal after MFA configuration

### Successful Login:

1. If you have configured email OTP, OTP will be triggered to your registered email address.
2. If you have configured an authentication app (for example Microsoft, Google Authenticators), please open the authentication app, and enter the OTP generated in the app.
3. If the OTP is correct, you will be successfully logged into the partner portal, granting access to the necessary resources.

### Failed Authentication:

If the OTP is incorrect or expired, you will receive an error message. You can request a new OTP again.

<Image align="center" alt="For an Authentication app." border={true} caption="For an Authentication app." src="https://files.readme.io/256debf55ee8124b6fe39ad133d0637fca750ff21d1c898df8f01def839949bf-image-12.png" />

<Image align="center" alt="For Email verification" border={true} caption="For Email verification" src="https://files.readme.io/7d410e8d88a20e78059a727570c16c0af4c72756db6d7b0f20c8963e0167c531-image-21.png" />

### Step 3: Troubleshooting and Support

**Common Issues:**

* **Not Receiving OTP**: Ensure your email is correct and check your spam/junk folder. If using an authenticator app, make sure it is synced properly.
* Expired OTP: OTPs have a limited validity period. Request a new one if your code has expired.

> 📘 NOTE:
>
> * If the authenticator app isn't working, opt for email-based OTP verification.
> * If neither option works, open a support ticket. The support team will coordinate with the Auth team to reset MFA.
> * After the reset, the partner has to re-configure the MFA.

## Step-by-Step Procedure for Partners without MFA enabled

### Step 1: Login into the Partner Portal after signup

<Image align="center" className="border" border={true} src="https://files.readme.io/5ed83659b5cd82bff6aac84c05cc684f26c320cbd5fe47fa849c1f8e63e5c297-image-13.png" />

1. For older partner portal users, they can continue to use their password configured.
2. Enter the captcha code displayed on the screen.
3. Click **Login**.

**Need Further Assistance:**

* If you encounter issues that cannot be resolved, contact the Gupshup partner support team or the help desk for further assistance.

## Other Security Improvements

1. You will be logged out of your partner portal session after 24 hours.
2. In case you have enabled MFA for your partner account. you will need to log in again using email OTP/Authenticator app.
3. In case you have not opted for MFA, you will need to login again using your email address and password.

## Conclusion

Implementing Multi-Factor Authentication (MFA) through Auth0 significantly enhances the security of your partner portal access. Always ensure the email and authenticator app is accessible for a smooth login experience.