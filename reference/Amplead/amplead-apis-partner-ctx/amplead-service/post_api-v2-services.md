---
title: Create a new service
excerpt: This API allows the creation of a new service for Partner-CTX.
api:
  file: partner-ctx-api.json
  operationId: post_api-v2-services
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Please note that this is an outdated document. Refer to the updated documentation [here](/reference/enablectxforpartner#/).

### Callback URL

```json Webhook Example
{  
"leadId":"\<leadid_example>",  
"serviceId":"\<serviceId_example>",  
"status":"OPEN",  
"currentMilestoneIndex":null,  
"fepMessageTimestamp":1725379603579,  
"customerPhoneNumber":0099000099,  
"conversationId":null,  
"ctwa_clid":null,  
"adId":null,  
"externalAdId":"120205115247920650",  
"templateId":"templateId_example",  
"retargetSentTimestamp":1725379800573,  
"partnerId":"1",  
"selfServeAppId":"\<selfServeAppId_example>",  
"countRetargetingSent":1  
}
```