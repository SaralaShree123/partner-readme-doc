---
summary: >-
title: Delete Service Action API
excerpt: >-
  This API allows you to perform actions (such as delete) on a specific Amplead
  service.
deprecated: false
hidden: true
metadata:
  robots: index
---
# API Details

## Endpoint and Base URL

```curl Base URL
https://partner-ctx.gupshup.io
```

```curl Endpoint
POST /api/v2/services/{ctxServiceId}/actions
```

## cURL Example

```curl
curl --location --globoff 'https://partner-ctx.gupshup.io/api/v2/services/{ctxServiceId}/actions' \
--header 'authorization: {ctxServiceAPIKey}' \
--header 'apiKey: {ctxServiceApiKey}' \
--header 'Content-Type: application/json' \
--data '{
    "action": "delete"
}'
```

## Authentication

This API requires authentication using the following headers:

| Header Name   | Required | Description                         |
| ------------- | -------- | ----------------------------------- |
| authorization | Yes      | Authorization token for the request |
| apiKey        | Yes      | API key associated with the service |
| Content-Type  | Yes      | Must be `application/json`          |

## Path Parameters

| Parameter    | Type   | Required | Description                      |
| ------------ | ------ | -------- | -------------------------------- |
| ctxServiceId | String | Yes      | Unique identifier of the service |

## Request Body and Request Parameters

```json Request Body
{
  "action": "delete"
}
```

<br />

| Field  | Type   | Required | Description                                             |
| ------ | ------ | -------- | ------------------------------------------------------- |
| action | String | Yes      | The action to perform on the service. Example: `delete` |

## Response

```json 200
{
  "status": "success",
  "message": "Service deleted successfully"
}
```

<br />