---
name: api
---
### Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Value",
    "h-2": "Description",
    "h-3": "Data type",
    "h-4": "Required/Optional",
    "h-5": "Constraints",
    "0-0": "Authorization",
    "0-1": "{{PARTNER_APP_TOKEN}}",
    "0-2": "Access Token for the application",
    "0-3": "String",
    "0-4": "Required",
    "0-5": "Should be a valid  \nPartner App Access  \nToken.",
    "1-0": "appId",
    "1-1": "{{APP_ID}}",
    "1-2": "App ID to fetch the  \naccess token",
    "1-3": "String",
    "1-4": "Required",
    "1-5": "The ID should be a valid app Id of Gupshup.",
    "2-0": "messaging_product",
    "2-1": "whatsapp",
    "2-2": "Messaging product",
    "2-3": "String",
    "2-4": "Required",
    "2-5": "",
    "3-0": "recipient_type",
    "3-1": "individual",
    "3-2": "Recipient type",
    "3-3": "String",
    "3-4": "Required",
    "3-5": "",
    "4-0": "to",
    "4-1": "91785876xxxx",
    "4-2": "Destination phone number where the message needs to be sent",
    "4-3": "String",
    "4-4": "Required",
    "4-5": "Must be a valid phone number",
    "5-0": "type",
    "5-1": "template",
    "5-2": "Messaging type",
    "5-3": "String",
    "5-4": "Required",
    "5-5": "The type should be `template` to send a template message.",
    "6-0": "template",
    "6-1": "{  \n\t\"name\": \"TEMPLATE_N AME\",  \n\t\"language\":  \n\t{  \n\t\t\"code\": \"LANGUAGE_AND_LOCALE_C ODE\"  \n\t},  \n\t\t\"components \": \\[  \n\t\t\"  \n\t\t\t\\<NAMED_PARA METER_INPUT>\" OR  \n\t\t\"  \n\t\t\t\\<POSITIONAL_PARAMETER_ INPUT>\"  \n\t\t]  \n}",
    "6-2": "Template message inside body",
    "6-3": "Object",
    "6-4": "Required",
    "6-5": "\\<NAMED_PARAMETER_  \nINPUT>  \nRequired when you have used named parameters in your  \ntemplate's body text.  \n  \n\\<POSITIONAL_PARAMT  \nER_INPUT>  \n  \nRequired when you have used positional  \nparameters in your template's body text."
  },
  "cols": 6,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### Sample Request

```curl

```

### Sample Response

```json

```

### Status Codes

| Status Code | Response                                                                                                                                                                                                                    | Comments                                       |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
| **Success** |                                                                                                                                                                                                                             |                                                |
| 200         | `{   	"messages": [   		{   			"id": "GUPSHUP_MESSAGE_ID"   		}   	],   	"messaging_product": "whatsapp",   	"contacts": [   		{   			"input": "DESTINATION_PHONE_NO",   			"wa_id": "DESTINATION_PHONE_NO"   		}   	]   }` |                                                |
| **Error**   |                                                                                                                                                                                                                             |                                                |
| 400         | `{   	"message": "Callback Billing must be enabled for this API",   	"status": "error"   }`                                                                                                                                 | if Callback billing is not enabled for the app |
| 400         | `{   	"message": "Invalid App Details",   	"status": "error"   }`                                                                                                                                                           | if app details are not found                   |
| 401         | `{   	"status": "error",   	"message": "Authentication Failed"   }`                                                                                                                                                         | When API key authentication fails              |