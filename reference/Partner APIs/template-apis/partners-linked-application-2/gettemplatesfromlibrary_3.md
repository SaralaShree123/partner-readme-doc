---
title: Get Templates from Library
excerpt: API to fetch pre approved Meta Library Templates
api:
  file: metalibrary_3_0.json
  operationId: getTemplatesFromLibrary_3
hidden: true
---
# Rate Limit

10 Requests per Minute

<br />

# Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/template/metalibrary?elementName=&industry=&languageCode=&topic=&usecase=' \
--header 'Authorization : {{PARTNER_APP_TOKEN}}'
```

# Sample Response

```curl
{
    "status": "success",
    "templates": [
        {
            "category": "UTILITY",
            "containerMeta": "sampleData",
            "data": "sampleData",
            "elementName": "account_creation_confirmation_3",
            "industry": "E_COMMERCE,FINANCIAL_SERVICES",
            "languageCode": "nb",
            "topic": "ACCOUNT_UPDATES",
            "usecase": "ACCOUNT_CREATION_CONFIRMATION"
        }
   ]  
}      
```

# Request Parameters

| Key                 | Description                                              | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------ | :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Headers**         |                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PARTNER\_APP\_TOKEN | App Access Token issued post partner login               | Should be a valid partner app access token belonging to the passed appId                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Query Params**    |                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| elementName         | Name of element                                          | Meta library template name - Optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| industry            | Name of industry                                         | Possible values E\_COMMERCE, FINANCIAL\_SERVICES - Optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| languageCode        | Language code of the meta library template               | Optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| topic               | Topic of the meta library template                       | Possible values ACCOUNT\_UPDATES, CUSTOMER\_FEEDBACK, ORDER\_MANAGEMENT, PAYMENTS - Optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| usecase             | Use case of the meta library template                    | Possible values ACCOUNT\_CREATION\_CONFIRMATION, AUTO\_PAY\_REMINDER, DELIVERY\_CONFIRMATION, DELIVERY\_FAILED, DELIVERY\_UPDATE, FEEDBACK\_SURVEY, FIXED\_TEMPLATE\_PRICE\_TEST, FRAUD\_ALERT, LOW\_BALANCE\_WARNING, ORDER\_ACTION\_NEEDED, ORDER\_CONFIRMATION, ORDER\_DELAY, ORDER\_OR\_TRANSACTION\_CANCEL, ORDER\_PICK\_UP, PAYMENT\_ACTION\_REQUIRED, PAYMENT\_CONFIRMATION, PAYMENT\_DUE\_REMINDER, PAYMENT\_NOTICE, PAYMENT\_OVERDUE, PAYMENT\_REJECT\_FAIL, PAYMENT\_SCHEDULED, RECEIPT\_ATTACHMENT, RETURN\_CONFIRMATION, SHIPMENT\_CONFIRMATION, STATEMENT\_ATTACHMENT, STATEMENT\_AVAILABLE, TRANSACTION\_ALERT - Optional |
| **Path Params**     |                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appId               | App Id for the app that is linked to the Partner Account |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# Status Codes

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
        "status": "success",
        "templates": \[
        \{
        "category": "UTILITY",
        "containerMeta": "sampleData",
        "data": "sampleData",
        "elementName": "account\_creation\_confirmation\_3",
        "industry": "E\_COMMERCE,FINANCIAL\_SERVICES",
        "languageCode": "nb",
        "topic": "ACCOUNT\_UPDATES",
        "usecase": "ACCOUNT\_CREATION\_CONFIRMATION"
        },
      </td>

      <td>
        If templates are found for the given filter(s)
      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{
        "status": "success",
        "templates": \[]
        }
      </td>

      <td>
        If no templates are found for the given filter(s)
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
        401
      </td>

      <td>
        \{
        "message": "Authentication Failed",
        "status": "error"
        }
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        \{
        "status": "error",
        "message": "Too Many Requests"
        }
      </td>

      <td>
        10 Requests per Minute
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{
        "status": "error",
        "message": "Internal Server Error"
        }
      </td>

      <td>
        For any Internal Error
      </td>
    </tr>
  </tbody>
</Table>