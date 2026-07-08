---
title: Update Pre-filled Data
excerpt: >-
  Use this API to update the pre-filled data for an app, which will be shown to
  the user during the ES flow.
api:
  file: partner-prefillied-data.json
  operationId: put_partner-app-appid-onboarding-embed-prefilled
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Constraints</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ID of the app.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid app ID.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>apikey</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Apikey of the account where the app is to be created</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Apikey of the account where the app is to be created</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>businessName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name of the business.<br>Will be forwarded to meta in ES flow as: <code>business.name</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Less than 100 characters.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name of the business.<br>Will be forwarded to meta in ES flow as: <code>business.email</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be a valid email ID.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>website</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Website of the business.<br>Will be forwarded to meta in ES flow as: <code>business.website</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Must be a valid URL.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>businessPhoneCode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone country code of the business.<br>Will be forwarded to meta in ES flow as: <code>business.phone.code</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Must be a valid phone county code.</li>
<li>Must not be empty if the business phone number is non-empty.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>businessPhoneNumber</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone number of the business without country code.<br>Will be forwarded to meta in ES flow as: <code>business.phone.number</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Must be a valid phone number without a dial code.</li>
<li>Must not be empty if the business phone code is non-empty.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>streetAddress1</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Street address 1 of the business.<br>Will be forwarded to meta in ES flow as: <code>business.address.streetAddress1</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>streetAddress2</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Street address 2 of the business.<br>Will be forwarded to meta in ES flow as: <code>business.address.streetAddress2</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>city</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>City of the business.<br>Will be forwarded to meta in ES flow as: <code>business.address.city</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>state</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>State of the business.<br>Will be forwarded to meta in ES flow as: <code>business.address.state</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipPostal</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Zip code of the business.<br>Will be forwarded to meta in ES flow as: <code>business.address.zipPostal</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>country</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Country of the business.<br>Will be forwarded to meta in ES flow as <code>business.address.country</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>should be in<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2?fbclid=IwZXh0bgNhZW0CMTEAAR3MSwSgzuMTeyUOr9kFmQnGRcLJehFbFP9W_4ZYKzJ9CM3_Ayh4FxXfOzg_aem_jlv4bpO-eH_j0ALI2cB0hQ#Officially_assigned_code_elements"> ISO 3166-1 alpha-2 country code</a> format<br>example: IN</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>timezone</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Timezone of the business.<br>Must be a valid UTC time zone in the format UTC{offset}.<br>Exampl: UTC+05:30<br>Will be forwarded to meta in ES flow as: <code>business.timezone</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones?fbclid=IwZXh0bgNhZW0CMTEAAR2u2JQakhNQzI7W18oDXoftqsEszYiDS0eZ4FXhevwnehDnSW7HVZjz9Kc_aem_rykBKW--TTXT1StrN4-j2g">UTC Offset format</a>. For example: UTC+05:30</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phoneDisplayName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Display the name of the phone number.  </p>
<p>Will be forwarded to meta in ES flow as: <code>phone.displayName</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String following <a href="https://www.facebook.com/business/help/338047025165344#display-name-guidelines">display name guidelines</a>.<br>Example: Gupshup</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phoneCategory</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Category of the phone number.<br>should be one of the below category :<br>( TRAVEL, EVENT_PLAN, ENTERTAIN, BEAUTY, APPAREL, FINANCE, AUTO, PROF_SERVICES, RESTAURANT, EDU, HEALTH, GROCERY, GOVT, NONPROFIT, RETAIL, HOTEL, OTHER )Will be forwarded to meta in ES flow as: <code>phone.category</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phoneDescription</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Description of the phone number.<br>Will be forwarded to meta in ES flow as: <code>phone.description</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Less than 256 characters.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request PUT 'https://partner.gupshup.io/partner/app/{{APP_ID}}/onboarding/embed/prefilled' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data-urlencode 'businessName={{BUSINESS_NAME}}' \
--data-urlencode 'email={{EMAIL}}' \
--data-urlencode 'website={{WEBSITE}}' \
--data-urlencode 'businessPhoneCode={{BUSINESS_PHONE_CODE}}' \
--data-urlencode 'businessPhoneNumber={{BUSINESS_PHONE_NUMBER}}' \
--data-urlencode 'streetAddress1={{STREET_ADDRESS_1}}' \
--data-urlencode 'streetAddress2={{STREET_ADDRESS_2}}' \
--data-urlencode 'city={{CITY}}' \
--data-urlencode 'state={{STATE}}' \
--data-urlencode 'zipPostal={{ZIP_POSTAL}}' \
--data-urlencode 'country={{COUNTRY}}' \
--data-urlencode 'timezone={{TIMZONE}}' \
--data-urlencode 'phoneDisplayName={{PHONE_DISPLAY_CODE}}' \
--data-urlencode 'phoneCategory={{PHONE_CATEGORY}}' \
--data-urlencode 'phoneDescription={{PHONE_DISCRIPTION}}'
```

## Sample Response

```json
{
    "appId": "<app_id>",
    "businessName": "<business_name>",
    "businessPhoneCode": "<business_phone_code>",
    "businessPhoneNumber": "<business_phone_number>",
    "city": "<city>",
    "country": "<contry>",
    "email": "<business_email>",
    "phoneCategory": "<phone_category>",
    "phoneDescription": "<phone_description>",
    "phoneDisplayName": "<phone_displayname>",
    "state": "<state>",
    "status": "<status>",
    "streetAddress1": "<streetAddress1>",
    "streetAddress2": "<streetAddress2>",
    "timezone": "<timezone>",
    "website": "<business_website>",
    "zipPostal": "<business_postal_code>"
}
```

## Status Codes

| Status Code | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Comments                                                                                                                                                                                                                                                                                               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                        |
| 200         | `{       "appId": "\<app_id>",       "businessName": "\<business_name>",       "businessPhoneCode": "\<business_phone_code>",       "businessPhoneNumber": "\<business_phone_number>",       "city": "<city>",       "country": "<contry>",       "email": "\<business_email>",       "phoneCategory": "\<phone_category>",       "phoneDescription": "\<phone_description>",       "phoneDisplayName": "\<phone_displayname>",       "state": "<state>",       "status": "<status>",       "streetAddress1": "<streetAddress1>",       "streetAddress2": "<streetAddress2>",       "timezone": "<timezone>",       "website": "\<business_website>",       "zipPostal": "\<business_postal_code>"   }` |                                                                                                                                                                                                                                                                                                        |
| **Error**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                        |
| 400         | `{       "message": "Business name must be less than 100 characters",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | When a business name contains more than 100 characters.                                                                                                                                                                                                                                                |
| 400         | `{       "message": "Invalid Email address",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Invalid email address                                                                                                                                                                                                                                                                                  |
| 400         | `{       "message": "Invalid website url",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | When invalid business website is present.                                                                                                                                                                                                                                                              |
| 400         | `{       "message": "Business phone code/number is empty",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | When adding a phone number, both the business phone code and the business phone number must be provided. If either one is provided without the other, or if one is empty, you will receive an error.                                                                                                   |
| 400         | `{       "message": "Invalid Country",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | When an invalid country type is provided.  Valid country type :  [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2?fbclid=IwZXh0bgNhZW0CMTEAAR3MSwSgzuMTeyUOr9kFmQnGRcLJehFbFP9W_4ZYKzJ9CM3_Ayh4FxXfOzg_aem_jlv4bpO-eH_j0ALI2cB0hQ#Officially_assigned_code_elements) |
| 400         | `{       "message": "Invalid phone category.The list of supported categories are : [TRAVEL, EVENT_PLAN, ENTERTAIN, BEAUTY, APPAREL, FINANCE, AUTO, PROF_SERVICES, RESTAURANT, EDU, HEALTH, GROCERY, GOVT, NONPROFIT, RETAIL, HOTEL, OTHER]",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                               | When an invalid phone category is provided.                                                                                                                                                                                                                                                            |
| 400         | `{       "message": "Invalid phone description",       "status": "error"   }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | When the description length is more than 256 character.                                                                                                                                                                                                                                                |