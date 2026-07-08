---
title: Delete Template By Template ID and Element Name
excerpt: Use this API to delete a template using the templateId and elementName.
api:
  file: delete-template-by-template-id-and-element-name.json
  operationId: delete_partner-app-appid-template-elementname-templateid
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note
> 
> This action is irreversible. Once a template has been deleted, it cannot be restored.

## Request Parameters

| Key           | Description                                 | Values                                 | Data Types | Required/Optional | Constraints                                |
| :------------ | :------------------------------------------ | :------------------------------------- | :--------- | :---------------- | :----------------------------------------- |
| Authorization | Access Token for the application            | `{PARTNER_APP_TOKEN}`                  | String     | Required          | Should be a valid Partner App Access Token |
| appId         | App id of the app                           | `bf9ee64c-3d4d-4ac4-xxxx-732e577007c4` | String     | Required.         | The Id should be a valid app Id of Gupshup |
| elementName   | element name for the template to be deleted | `{ELEMENT_NAME}`                       | String     | Required          |                                            |

## Sample Request

```curl
curl --location --request DELETE 'http://partner.gupshup.io/partner/app/{{APP_ID}}/template/{{ELEMENT_NAME}}/{{TEMPLATE_ID}}' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}'
```

## Sample Response

```json
{
  "status": "success"
}
```

## Status Codes

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Status Code</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Response</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Comments</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>Success</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>200</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{       &quot;status&quot;: &quot;success&quot;   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>Error</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{       &quot;status&quot;:&quot;error&quot;,       &quot;message&quot;:&quot;Invalid App ID&quot;   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The provided appId is not valid.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{       &quot;status&quot;:&quot;error&quot;,       &quot;message&quot;:&quot;Template ID and template name does not match&quot;   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>If  template Id and template name does not match</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{       &quot;status&quot;:&quot;error&quot;,       &quot;message&quot;:&quot;Delete Operation is not allowed for sandbox apps&quot;   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App is not live</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;status&quot;:&quot;error&quot;,<br>    &quot;message&quot;:&quot;Please Check If App Has been approved&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App is not approved</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;status&quot;:&quot;error&quot;,<br>    &quot;message&quot;:&quot;Template Does not exists.&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>No template found for the provided element name.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;status&quot;:&quot;error&quot;,<br>    &quot;message&quot;:&quot;Template Cannot be deleted&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Not a master template</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;status&quot;:&quot;error&quot;,<br>    &quot;message&quot;:&quot;Unable to delete the template, please try after sometime and if issue still exists than contact dev support&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Error occured while deleting template.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>403</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>    &quot;status&quot;:&quot;error&quot;,<br>    &quot;message&quot;:&quot;Not App Owner&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId provided is not associated with the provided api key.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>500</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>  &quot;status&quot;: &quot;error&quot;,<br>  &quot;message&quot;: &quot;Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support&quot;<br>}</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>For any Internal Error</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>