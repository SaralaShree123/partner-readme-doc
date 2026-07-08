---
title: INR-Wallet Creation & KYC Flow Guide
excerpt: >-
  This document outlines the complete flow for **Wallet Creation and KYC
  verification** for partners
deprecated: false
hidden: true
metadata:
  robots: index
---
<Callout icon="❗️">
  Do not create wallet directly after partner account creation

  Once a partner account is successfully created, do not proceed to create a wallet immediately. 
</Callout>

<Callout icon="❗️">
  Reporting limitation — next 10 days

  Partner Portal reports will not reflect exact figures based on actual INR cost for the next 10 days. Volumes should be correct, but cost-based reporting may be inaccurate during this period. 
</Callout>

# INR-Wallet Creation & KYC Flow Guide

## 📌 Overview

Wallet creation varies based on user persona:

| User Type     | Interface                            |
| ------------- | ------------------------------------ |
| Partner Users | Partner Portal (Wallet Listing Page) |

***

## &#x20;Wallet Creation Flow

### &#x20;Entry Point

* Navigate to **Wallet Listing Page**
* Click **"Create Wallet"**

### ⚙️ Steps

![](https://files.readme.io/2245bc45901e577d751659b8a378484f2d2c6ae26d55dfc5ce62ee5e5ee7311a-image.png)

***

## 1. KYC Verification Process

### Requirements

* Name
* Phone number
* Email
* GST Number

***

## GSTIN Structure

Example: 22AAAAA0000A1Z5

| Part           | Meaning            |
| :------------- | :----------------- |
| First 2 digits | State Code         |
| Next 10 digits | PAN                |
| 13th digit     | Registration count |
| 14th digit     | Default "Z"        |
| Last digit     | Check code         |

![](https://files.readme.io/550154a47d7f06714ea77a161e6add9ef68f5e1d21f3436a865e6f627a61b56e-image.png)

<Callout icon="❗️" theme="error">
  GST number cannot be changed after verification is completed.
</Callout>

***

### Validation

* GST is verified
* Invalid GST → Error
* Valid GST → KYC completed

***

### Outcome

* Recharge button enabled
* Business details auto-filled in billing 1. KYC Verification Process

  ![](https://files.readme.io/7c7ea4765fb60b97bf4963c181a17d10eb6e74ecc4dbb86515b6f236e86a957c-image.png)

  ***

  <br />

  ## 2. Recharge Process

  ### Steps

  1. Complete KYC
  2. Click Recharge
  3. Enter amount (Minimum: 100 credits)
  4. Click Pay & Confirm
  5. Select payment method (e.g., net banking)
* <Callout icon="❗️" theme="error">
    Adds 18% GST
  </Callout>
* <Image align="center" border={true} width="1230px" src="https://files.readme.io/8d6901d25a00d326b1435f486137c50d5f1c5b7cbe3aadd271366d42ad250eb5-image.png" className="border" />

  <br />

<Image align="center" border={true} src="https://files.readme.io/b14d27affde68a57562557278d8841adb07887f19f39e751befefc898f31ad03-image.png" className="border" />

<Image align="center" border={true} src="https://files.readme.io/006eb6007d049aaebf0f263145ec403f076e4f7f20a86791d94fba39c1b5fcd0-image.png" className="border" />

<Image align="center" border={true} src="https://files.readme.io/d740ed76bb8d23f8459d894d6fb77fde1d1a35ed7930062bec38fc3b2c1b4746-image.png" className="border" />

***

### Result

* Successful payment → Wallet updated
* Entry added in recharge history
  * Successful payment → Wallet updated
  * Entry added in recharge history

<Image align="center" border={true} src="https://files.readme.io/2b94e2ca9dc9a718732ab766454be1c5cf2148c1e56b99c2ca22b6c86dfaf128-image.png" className="border" />

***

### Additional

* Invoice sent via email automatically

<Image align="center" border={true} src="https://files.readme.io/20e3134a48e925f6c5fb1951366698187473dbae768b82b213a38e8d74bd6836-image.png" className="border" />

***

## 6. Key Takeaways

* KYC is mandatory
* GST ensures correct billing
* Minimum recharge: 100 credits
  * KYC is mandatory
  * GST ensures correct billing

***

<br />
