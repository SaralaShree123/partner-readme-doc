---
title: Update Profile Details
excerpt: >-
  Updates the WhatsApp Business profile information for a specific partner
  application. You can update multiple profile fields in a single request
  including address, description, email, website, and industry vertical. All
  updates are immediately reflected on your WhatsApp Business profile.
api:
  file: partner-portal-public-apis.json
  operationId: put_partner-app-appid-business-profile
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

| Parameters    | Value                     | Description                                    |
| :------------ | :------------------------ | :--------------------------------------------- |
| Authorization | \{\{PARTNER\_APP\_TOKEN}} | Access Token for the application               |
| addLine1      | string                    | Address of the business                        |
| addLine2      | string                    | Address of the business                        |
| city          | string                    | City where business is situated                |
| state         | string                    | State where business is situated               |
| pinCode       | string                    | Pincode of the city where business is situated |
| country       | string                    | Country where business is situated             |
| vertical      | string                    | Pincode of the city where business is situated |
| website1      | string                    | Website of business                            |
| website2      | string                    | Website of business                            |
| desc          | string                    | Description of the business                    |
| profileEmail  | string                    | Email of business                              |

### Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/business/profile' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'addLine1={{ADDRESS_LINE_1}}' \
--data-urlencode 'addLine2={{ADDRESS_LINE_2}}' \
--data-urlencode 'city={{CITY}}' \
--data-urlencode 'state={{STATE}}' \
--data-urlencode 'pinCode={{PINCODE}}' \
--data-urlencode 'country={{COUNTRY}}' \
--data-urlencode 'vertical={{VERTICAL}}' \
--data-urlencode 'website1={{WEBSITE1}}' \
--data-urlencode 'website2={{WEBSITE2}}' \
--data-urlencode 'desc={{DESCRIPTION}}' \
--data-urlencode 'profileEmail={{PROFILE_EMAIL}}'
```

### Sample Response

```json
{
            "profile": {
                "address": "<address>",
                "profileEmail": "<emailId>",
                "desc": "<description>",
                "vertical": "<vertical>",
                "website1": "<website1>",
                "website2": "<website2>"
            },
            "status": "success"
        }
```