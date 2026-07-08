---
title: Send MM lite message with GIF Template
excerpt: 'This API is used to send marketing messages with GIF template '
hidden: true
---
```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/onboarding/marketing/msg' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "recipient_type": "individual",
    "messaging_product": "whatsapp",
    "to": "{{DESTINATION}}",
    "type": "template",
    "template": {
        "name": "{{TEMPLATE_NAME}}",
        "language": {
            "policy": "deterministic",
            "code": "{{LANGUAGE_CODE}}"
        },
        "namespace": "{{NAMESPACE}}",
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "GIF",
                        "gif": {
                            "link": "{{GIF_URL}}"
                        }
                    }
                ]
            },
            {
                "type": "body"
            }
        ]
    }
}'
```

<br />

Status Codes:

<br />

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
        <code>{'{ "messages": [ { "id": "1ceeb739-06cd-4434-a1e0-8afac154ede4" } ], "messaging_product": "whatsapp", "contacts": [ { "input": "9188889945", "wa_id": "9188898545" } ] }'}</code>
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
        <code>{'{ "status": "error", "message": "MM lite is not enabled for this app" }'}</code>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        <code>{'{ "status":"error", "message":"Unauthorised access to the resource. Please review request parameters and headers and retry" }'}</code>
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<br />
