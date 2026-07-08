---
summary: Partner - Wallet Balance Transfer (COPY)
title: Partner - Wallet Balance Transfer (COPY)
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
# Objective

This document provides comprehensive information on the use case, guidelines, rate limits, authentication, request/response formats, and other essential aspects of using our API to transfer wallet balance from an ISV wallet to an end customer account.

# Introduction

## Use Case

In the scenarios where an ISV has its own wallet but customers of that ISV have created accounts on [Gupshup](https://www.gupshup.io/partners) and hence get a separate wallet, ISVs need an effective way to transfer the balance from their own wallet to their end customer's wallet. This is required as the ISV is responsible for recharges and customers consume the wallet associated with their own customer ID.

## Prerequisites

1. You should have your own wallet as an ISV on gupshup.io which will be marked as the source wallet (partner wallet) in step 2.
2. The support team should be able to enable the functionality for you. Please reach out [partner.support@gupshup.io](mailto:partner.support@gupshup.io) to activate the wallet transfer for you.
3. After the above steps are completed, when you want to transfer the balance from the source wallet to the destination wallet, you should have at least one live WABA app in the destination wallet which should be linked to your partner ID.

# Do's and Don’ts

* You should have a positive balance in your partner's (source) wallet to transfer money. No negative balance transfer is allowed, even if there is an overdraft available. (In future, we will also be restricting transferring only positive balance in the wallet above 5 USD, as it is the complementary credit provided by Gupshup when the wallet is created).
* This API only helps transfer money from the Partner (source) wallet to their customer’s wallet (basis criteria are met as per step 3 above). It will NOT work in cases to transfer the balance from a regular customer to a regular customer wallet or back to the partner’s source wallet.
* The API needs to be handled very carefully, Gupshup is not RESPONSIBLE for transferring ANY amount to another wallet with the use of this API, and ISV will be totally responsible for this transfer at their own risk. Gupshup will not reverse transactions done through this API or rectify errors if any in this process.
* ALERT FOR PORTUGUESE AND SPANISH DEVELOPERS: You should ONLY be using decimal as in English script - “.”; NO commas or other characters should be used as in Spanish and Portuguese script for decimal. The amount field ONLY supports English script.
* Handle errors gracefully.
* Ensure the proper management of your partner's JWT token to prevent unauthorized access.
* Once this document is shared with ISV, it is confirmed that ISV is aware of the risks involved in the usage of this API and agrees to the mentioned Do’s and Dont’s.

## API Endpoint - Initiate Transfer (link to API reference)
