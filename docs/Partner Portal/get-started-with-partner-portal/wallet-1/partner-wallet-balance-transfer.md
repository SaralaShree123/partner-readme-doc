---
title: Partner - Wallet Balance Transfer
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

This guide is designed to help you effectively use our API for transferring wallet balances from your ISV wallet to your customers' accounts.

If you're a TP with a wallet on Gupshup and your customers have their own separate wallets, this API is your solution.  It allows you to seamlessly transfer funds from your ISV wallet to your customers' wallets, ensuring they have the balance they need for their accounts.

# Prerequisites

1. **ISV Wallet**: Ensure you have an ISV wallet on [Gupshup](https://www.gupshup.io/partners), which acts as your source wallet for transfers.
2. **Activate Transfer Functionality**: Contact your local CSM and Sales to enable wallet transfer capabilities.
3. **Linked WABA App**: Before transferring funds, ensure you have at least one live WABA app linked to your ISV partner ID in the destination wallet.

# Do's and Don’ts

* **Positive Balance Required**: Ensure your source wallet balance is positive.  Negative balance transfers are not allowed, even if an overdraft is available.  In the future, transfers will be restricted to amounts above $5, aligning with Gupshup's complimentary credit policy.
* **Transfer Scope**: This API is meant solely for transferring funds from your ISV source wallet to your customers’ wallets, provided the prerequisites are met.  It cannot be used for transfers between regular customer wallets or back to the ISV wallet.
* **Risk Management**: Use the API with caution.  Gupshup is not responsible for transfers executed via this API.  All transactions are at your own risk, and Gupshup will not reverse or rectify any issues.
* **Decimal Handling for International Developers**: Use a decimal point (".") as per the English script for amounts.  Commas or other characters from Spanish and Portuguese scripts are not supported.
* **Error Handling and Security**: Handle errors gracefully and manage your JWT token securely to prevent unauthorized access.

## API Endpoint

Refer to the [Wallet Balance Transfer API](https://partner-docs.gupshup.io/reference/post_partner-account-api-wallet-balance-transfer#/).

## Security

All API requests and responses are encrypted using SSL/TLS to ensure data security during transmission.