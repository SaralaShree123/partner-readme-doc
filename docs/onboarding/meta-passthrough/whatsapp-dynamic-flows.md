---
summary: This guide helps you to create a WhatsApp Dynamic Flow
title: WhatsApp Dynamic Flows
excerpt: This guide helps you to create a WhatsApp Dynamic Flow
deprecated: false
hidden: false
metadata:
  robots: index
---
## Step 1: Create a basic Flow

Begin by creating a flow with an endpoint using the Gupshup API. Since this involves a flow with an endpoint, ensure that you utilize the Gupshup Create Flow API and specify your endpoint in the `endpoint_uri` parameter within the API request. - [LINK](/reference/createflow#/)

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/flows/' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "{{FLOW_NAME}}",
  "categories": ["{{FLOW_CATEGORY}}"]
  "endpoint_uri" : {{endpoint url}}
}'
```

## Step 2: Generating Keys

### <Anchor label="Openssl " target="_blank" href="https://developers.facebook.com/docs/whatsapp/cloud-api/reference/whatsapp-business-encryption">Openssl </Anchor> - Please follow the steps and generate key.

The above methods of genrating a keys is recommended by Meta but please try it in UAT Env and use a tried and test method in your PROD Env.

> ℹ️ Ensure when setting the business public key, it is a valid 2048-bit RSA public key in PEM format.

## Step 3: Set Key

Having generated your public and private key pair, use the following API to set the public key with your WABA.

### Set Public Key API

**Overview**

This API allows you to add a public key to META for WhatsApp flows. The customer is responsible for generating a public-private key pair, securely storing the private key, and sharing the public key with META using this passthrough API. The private key is utilized for decrypting data exchanged through META in dynamic flows.

**Endpoint**

```curl
POST https://partner.gupshup.io/partner/app/{{APP_ID}}/flows/publicKey
```

**Request Example**

```curl curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/flows/publicKey' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
    "public_key": "{{public_key}}"
}'
```

> ℹ️ Please make sure that the public key is correctly formated before it is send via the API request.
>
> The format means that the line break should be replaced by \n.

**Headers**

| Atrribute                         | Description                                                                                |
| :-------------------------------- | :----------------------------------------------------------------------------------------- |
| **PARTNER\_APP\_TOKEN**: (string) | The Partner Token associated with the Partner/Account where the application is registered. |
| **Content-Type:**                 | Must be set to **application/json**.                                                       |

**Request Body**

| Atrribute        | Description                                                                                              |
| :--------------- | :------------------------------------------------------------------------------------------------------- |
| **public\_key:** | (string) The public key to be added to the application.Constraint: Must be in a valid public key format. |

**Parameters**

| Atrribute | Description                                                                 |
| :-------- | :-------------------------------------------------------------------------- |
| **appId** | The identifier of the application for which the public key needs to be set. |

**Response**

| Status Code | Response                                                | Comment |
| :---------- | :------------------------------------------------------ | :------ |
| 200         | \{"status": "success"}                                  | success |
| 400         | \{"code": "code","details": "reason","status": "error"} | error   |

### Get Public Key API

This API retrieves the public key associated with your application's WhatsApp flows.

**Endpoint**

```curl
SET https://partner.gupshup.io/partner/app/{{APP_ID}}/flows/publicKey
```

**Request Example**

```curl curl
curl --location 'https://partner.gupshup.io/partner/app/{{APP_ID}}/flows/publicKey' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json'
```

**Headers**

| Atrribute                         | Description                                                                                |
| :-------------------------------- | :----------------------------------------------------------------------------------------- |
| **PARTNER\_APP\_TOKEN**: (string) | The Partner Token associated with the Partner/Account where the application is registered. |
| **Content-Type:**                 | Must be set to application/json.                                                           |

**Parameters**

| Atrribute | Description                                                                 |
| :-------- | :-------------------------------------------------------------------------- |
| **appId** | The identifier of the application for which the public key needs to be set. |

**Response**

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
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        200
      </td>

      <td>
        \{

        "encryption": \{

        "business\_public\_key": "public\_key","business\_public\_key\_signature\_status": "public\_key\_status"},"status": "success"}
      </td>

      <td>
        success
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{"code": "code","details": "reason","status": "error"}
      </td>

      <td>
        error
      </td>
    </tr>
  </tbody>
</Table>

## Step 4: Publish the Flow

Execute the Publish API to publish the flow. Once the flow is successfully published, you are ready to send flow messages.