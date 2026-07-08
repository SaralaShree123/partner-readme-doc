---
title: Send msg With Template ID
excerpt: Use this API to send messages with Template ID.
api:
  file: partner-portal-public-apis-1.json
  operationId: post_partner-app-appid-template-msg
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note:
> 
> 1. In case of Carousel template, the postback texts are added to the Cards of the Carousel template. 
> 2. If the template has a quick reply button, then the postback texts can be added to the Callback URL.

### Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Key</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Required/Optional</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Type</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Value</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Access Token for the application</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{PARTNER_APP_TOKEN}}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>appId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique Identifier for Gupshup App</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{{APP_ID}}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>source</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone number to send a message from.  </p>
<p>Required phone Number With Country Code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>91891056XXXX</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>src.name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Appname1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>sandbox</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a boolean value</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Boolean</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>destination</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone number of the customer to send the message to.  </p>
<p>Required phone Number With Country Code.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>918286836XXX</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>template</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><strong>MPM Template</strong><br>For the MPM template, params must include all params including a product ID (which is to be used as a thumbnail (last in the list)).<br>For MPM template messages template section must be provided with valid Ids <code>template={ &quot;id&quot;:&quot;3b9bf65b-979c-44d3-a269-dec2f20c4e52&quot;, &quot;params&quot;:[ &quot;zqc2qfz5fm&quot; ], &quot;mpm&quot;:{ &quot;sections&quot;:\[{ &quot;title&quot;:&quot;Products&quot;, &quot;products&quot;:[ &quot;zqc2qfz5fm&quot; ] }, { &quot;title&quot;:&quot;Products2&quot;, &quot;products&quot;:[ &quot;xyli96fcbn&quot; ] }] } }</code>  </p>
<p><strong>Catalog Template</strong><br>The catalog template is only supported on CAPI.<br>For catalog template Params should contain the productId which will be sent as thumbnail for the catalog (Must be the last element in templateParams list).  </p>
<p><strong>LTO Template</strong><br>When the template type is LTO,  we can specify the expiration period.<br><code>{&quot;id&quot;:&quot;{template_id}&quot;,&quot;params&quot;:[&quot;template_params_list&quot;],&quot;expiration&quot;:{expiration_time_in_UNIX_timestamp_in_milliseconds}}</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{&quot;id&quot;: &quot;007b7c0e-fc8d-4698-a9a8-3938151dd5da&quot;,&quot;params&quot;: [&quot;monday&quot;,&quot;2020-12-20&quot;,&quot;apps&quot;]}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>src.name</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>App name, whose appId used while creating template</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>GupshupDevAssistant01</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>For the carousel, message JSON along with the media id/link will also contain the postbackTexts here index is the button index (starts from 0) and text is the postback text for that button.<br><code>{     &quot;type&quot;: &quot;carousel&quot;,     &quot;cardHeaderType&quot;: &quot;\&lt;IMAGE/VIDEO&gt;&quot;,     &quot;cards&quot;: \[       {         &quot;id/link&quot;: &quot;\&lt;image_id or image_link/video_id or video_link&gt;&quot;,         &quot;postbackTexts&quot;:[{&quot;index&quot;:0,&quot;text&quot;:&quot;hello&quot;}]       },     ]   }</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{ &quot;type&quot;: &quot;carousel&quot;, &quot;cardHeaderType&quot;: &quot;IMAGE&quot;, &quot;cards&quot;: \[ { &quot;link&quot;: &quot;&lt;https://fastly.picsum.photos/id/13/2500/1667.jpg?hmac=SoX9UoHhN8HyklRA4A3vcCWJMVtiBXUg0W4ljWTor7s&quot;&gt;, &quot;postbackTexts&quot;: [ { &quot;index&quot;: 1, &quot;text&quot;: &quot;hello&quot; } ] }]</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>postbackTexts</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Add Postback Text for quick reply button<br><code>[     {       &quot;index&quot;: 3, // button index starts from 0       &quot;text&quot;: &quot;hello&quot; //postback text for the button     }   ]</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>[{&quot;index&quot;:4,&quot;text&quot;:&quot;hello&quot;},{&quot;index&quot;:5,&quot;text&quot;:&quot;hey&quot;}]</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>channel</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Messaging channel to send message on.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Optional</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>whatsapp</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your app token, please refer Get access token api to get the token from partner documentation.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Required</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>sk_61b3021c97xxx4370b341f8baaae0xxxx</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Sample Request

```curl
curl --location '{{partner_base_url}}/partner/app/{{APP_ID}}/template/msg' \
--header 'Connection: keep-alive' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'channel=whatsapp' \
--data-urlencode 'source={{SOURCE_NUMBER}}' \
--data-urlencode 'sandbox=false' \
--data-urlencode 'destination={{DESTINATION_NUMBER}}' \
--data-urlencode 'template={"id": "{{TEMPLATE_ID}}","params":[]' \
--data-urlencode 'src.name={{APP_NAME}}' \
--data-urlencode 'message={{MESSAGE}}' \
--data-urlencode 'postbackTexts=[{"index":4,"text":"Hello"}]'
```

### Sample Response

```json
    {
      "status": "submitted",
      "messageId": "b****acb-3***-4***-98**-64*****ea9**"
    }             
```

#### Expected Response on Callback

```json
{
  "app": "{{app_name}}",
  "timestamp": 1716900845926,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "wamid.HBgMOTE4ODg4OTk4NTQ1FQIAEhgUM0EzODA1NkE2OENBNEFGQjFFQjkA",
    "source": "{{phone_number}}",
    "type": "quick_reply",
    "payload": {
      "text": "Yes",
      "type": "button",
      "postbackText": "hello"
    },
    "sender": {
      "phone": "{{phone_number}}",
      "name": "{{name}}",
      "country_code": "91",
      "dial_code": "{{phone_number}}"
    },
    "context": {
      "id": "3847e304-2b9f-4cef-a72d-29aca93f95ce",
      "gsId": "3d749fe7-36fb-44b6-8209-f79efed697f9",
      "forwarded": false,
      "frequently_forwarded": false
    }
  }
}
```

### Status Codes

| Status Code | Response                                                                                                                                                  | Comment                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **Success** |                                                                                                                                                           |                                                                                                                                |
| 200         | `{       "status": "submitted",       "messageId": <messageId>   }`                                                                                       |                                                                                                                                |
| **Error**   |                                                                                                                                                           |                                                                                                                                |
| 400         | `{       "message": "Invalid Destination",       "status": "error"   }`                                                                                   | If the destination is missing.                                                                                                 |
| 400         | `{       "message": "Invalid App Details",       "status": "error"   }`                                                                                   | If the source is missing or app details are not found"If the source is unavailable or the application details cannot be found. |
| 500         | `{     "status": "error",     "message": "Internal server error. Please try again later and If Issue still persist than contact Gupshup Dev Support"   }` | For any Internal Error                                                                                                         |