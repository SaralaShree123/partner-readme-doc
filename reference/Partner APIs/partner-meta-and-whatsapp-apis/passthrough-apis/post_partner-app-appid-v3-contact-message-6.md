---
api:
  file: Passthrough_contacts (1).json
  operationId: post_partner-app-appid-v3-message
hidden: false
---
Contacts messages allow you to send rich contact information directly to Whats App users, such as names, phone numbers, physical addresses, and email addresses.

#### [Meta Contact Message Doc Link](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/contacts-messages)

<br />

> 📘 Note:
>
> 1. Use the `recipient` parameter only when BSUID is enabled for the app.
> 2. When both `to` and `recipient` fields are used in the payload, the `to` field gets the priority.

## Request Parameters

| Key               | Description                                                 | Value                         | Data type | Required/Optional                                                                                  | Constraints                                       |
| :---------------- | :---------------------------------------------------------- | :---------------------------- | :-------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| Authorization     | Access Token for the application                            | \{\{PARTNER_APP_TOKEN}}       | String    | Required                                                                                           | Should be a valid Partner App Access Token        |
| appId             | App ID to fetch the access token                            | \{\{APP_ID}}                  | String    | Required                                                                                           | The ID should be a valid Gupshup app ID.          |
| messaging_product | Messaging product                                           | whatsapp                      | String    | Required                                                                                           |                                                   |
| recipient_type    | Recipient type                                              | individual                    | String    | Required                                                                                           |                                                   |
| to                | Destination phone number where the message needs to be sent | 91785876xxxx                  | String    | Required (Can be optional if BSUID is enabled for the app and recipient parameter is used instead) | Must be a valid phone number                      |
| recipient         | Destination BSUID where the message needs to be sent        | IN.461449821882xxxx           | String    | Optional                                                                                           | Must be a valid BSUID                             |
| type              | Messaging type                                              | contacts                      | String    | Required                                                                                           | Type should be contacts to send contacts message. |
| contacts          | Add contact body                                            | "contacts":[\<contacts body>] | Array     | Required                                                                                           | Key should be contacts to send contact message.   |

## Sample Request

```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{{APP_ID}}/v3/message' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "messaging_product": "whatsapp",
    "to": "{{WHATSAPP_USER_PHONE_NUMBER}}",
		"recipient": "{{BSUID}}",
    "type": "contacts",
    "contacts": [
        {
            "addresses": [
                {
                    "street": "{{STREET_NUMBER_AND_NAME}}",
                    "city": "{{CITY}}",
                    "state": "{{STATE_CODE}}",
                    "zip": "{{ZIP_CODE}}",
                    "country": "{{COUNTRY_NAME}}",
                    "country_code": "{{COUNTRY_CODE}}",
                    "type": "{{ADDRESS_TYPE}}"
                }
                /* Additional addresses objects go here, if using */
            ],
            "birthday": "{{BIRTHDAY}}",
            "emails": [
                {
                    "email": "{{EMAIL_ADDRESS}}",
                    "type": "{{EMAIL_TYPE}}"
                }
                /* Additional emails objects go here, if using*/
            ],
            "name": {
                "formatted_name": "{{FULL_NAME}}",
                "first_name": "{{FIRST_NAME}}",
                "last_name": "{{LAST_NAME}}",
                "middle_name": "{{MIDDLE_NAME}}",
                "suffix": "{{SUFFIX}}",
                "prefix": "{{PREFIX}}"
            },
            "org": {
                "company": "{{COMPANY_OR_ORG_NAME}}",
                "department": "{{DEPARTMENT_NAME}}",
                "title": "{{JOB_TITLE}}"
            },
            "phones": [
                {
                    "phone": "{{PHONE_NUMBER}}",
                    "type": "{{PHONE_NUMBER_TYPE}}",
                    "wa_id": "{{WHATSAPP_USER_ID}}"
                }
                /* Additional phones objects go here, if using */
            ],
            "urls": [
                {
                    "url": "{{WEBSITE_URL}}",
                    "type": "{{WEBSITE_TYPE}}"
                }
                /* Additional URLs go here, if using */
            ]
        }
    ]
}'
```

## Sample Response

```
{
    "messages": [
        {
            "id": "GUPSHUP_MESSAGE_ID"
        }
    ],
    "messaging_product": "whatsapp",
    "contacts": [
        {
            "input": "DESTINATION_PHONE_NO",
            "wa_id": "DESTINATION_PHONE_NO"
        }
    ]
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

        "messages": [\{"id": "GUPSHUP_MESSAGE_ID"        }        ],        "messaging_product": "whatsapp",        "contacts": [        \{        "input": "DESTINATION_PHONE_NO",        "wa_id": "DESTINATION_PHONE_NO"        }        ]        }
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

        "message": "Callback Billing must be enabled for this API","status": "error"}
      </td>

      <td>
        if Callback billing is not enabled for the app
      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \{

        "message": "Invalid App Details","status": "error"}
      </td>

      <td>
        if app details are not found
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{

        "status": "error","message": "Authentication Failed"}
      </td>

      <td>
        When API key authentication fails
      </td>
    </tr>
  </tbody>
</Table>
