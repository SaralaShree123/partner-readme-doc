---
title: wallet balance transfer
excerpt: Use this API to transfer the balance from self owned wallet.
api:
  file: wallet_balance_transfer_open_api.json
  operationId: post_partner-account-api-wallet-balance-transfer
hidden: true
---
## Request Parameters

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        PARTNER\_TOKEN
      </td>

      <td style={{ textAlign: "left" }}>
        JWT Token issued post partner login
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER\_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner JWT Token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        walletName
      </td>

      <td style={{ textAlign: "left" }}>
        Name for the wallet
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * If linked using apiKey the name would be “Default Wallet”
          •	Can be retrieved from Partner wallet tab if feature is enabled.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        customerId
      </td>

      <td style={{ textAlign: "left" }}>
        CustomerId for the wallet to which the balance should be transferred
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        amount
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * double
        * Amount to be transferred upto 3 decimal places.
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request POST '{{partner_portal_base_url}}/partner/account/api/wallet/balance/transfer
--header 'token: {{PARTNER_TOKEN}}' \ 
--header 'Content-Type: application/x-www-form-urlencoded' \ 
--data-urlencode 'walletName={{WALLET_NAME}}' \
--data-urlencode 'customerId={{CUSTOMER_ID}}' \ 
--data-urlencode 'amount'={{AMOUNT}}
```

## Sample Response

```json
{
    "message": "Amount has been transferred successfully"
}
```

## Status Codes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status Code
      </th>

      <th>
        Response
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Success**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{

        "message": "Amount has been transferred successfully"}
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Error**
      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error","message": "Balance is low for Wallet id: balance: "
        }
      </td>

      <td>
        When balance is low in Partner wallet
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error","message": "Wallet {} is not associated with partner {}"
        }
      </td>

      <td>
        Wallet is not associated with Partner
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error","message": "Customer id is invalid or customer does not have any live app linked to the partner"
        }
      </td>

      <td>
        No live app linked to Partner for the given customerId
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "status": "error","message": "The customer's account currency does not match with wallet currency"
        }
      </td>

      <td>
        Partner and customer’s wallet currency are different
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{

        "status": "error","message": "Amount debited from partner account but not credited into customer's account"
        }
      </td>

      <td>
        Debit done from Partner Wallet but credit to customer wallet fails.
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{

        "status": "error","message": "Failed to transfer amount"
        }
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>