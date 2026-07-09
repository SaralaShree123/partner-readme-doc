---
title: Create App
excerpt: Use this API to create a new WABA onboarding outside of Gupshup UI.
api:
  file: partner-portal-public-apis.json
  operationId: post_partner-app
deprecated: false
hidden: false
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PARTNER_TOKEN</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JWT Token issues post Partner login</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a valid Partner JWT Token.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name for the app</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><ul>
<li>Should be between 6 - 150 chars</li>
<li>Should not conflict with any other Gupshup App               - Special Characters are not allowed</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>templateMessaging</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Toggle template messaging feature, the initial default value is false.<br>If not passed the value is not updated.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>disableOptinPrefUrl</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Use this flag to toggle optin preferences - <a href="/reference/put_partner-app-appid-optin">Mark User Optin or Optout</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request POST '{{partner_portal_base_url}}/partner/app' \
--header 'token: {{PARTNER_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name={{appName}}' \
--data-urlencode 'templateMessaging=<true/false>' \
--data-urlencode 'disableOptinPrefUrl=<true/false>'
```

## Sample Response

```json
{
"appId": "<app_id>"
}
```

## Status Codes

| Status Code | Response                                                                                                      | Comments                                                                                   |
| :---------- | :------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------- |
| **Success** |                                                                                                               |                                                                                            |
| 200         | `{       "appId": "<app_id>"   }`                                                                             |                                                                                            |
| **Error**   |                                                                                                               |                                                                                            |
| 400         | `{     "status": "error",     "message": "Invalid characters used in app name"   }`                           | When a Special character is added in the name.                                             |
| 400         | `{     "status": "error",     "message": "App name  should be between 6     to 150 characters in length"   }` | if App name is not provided or App name length is less than 6 or more than 150 characters. |
| 409         | `{     "status": "error",     "message": "Bot Already Exists"   }`                                            | When already a bot with same name exists in gupshup                                        |
| 429         | `{     "status": "error",     "message": "Too Many Requests"   }`                                             | 10 Requests per Minute                                                                     |
| 500         | `{     "status": "error",     "message": "Unable to create App"   }`                                          | For any Internal Error                                                                     |
