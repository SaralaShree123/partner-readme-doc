---
title: Create a new WhatsApp template
excerpt: Creates a new template for WhatsApp messaging
api:
  file: Create Auth Template.json
  operationId: post_partner-app-appid-templates
hidden: true
---
## Request Parameters

| Key           | Description                      | Value                   | Data type | Required/Optional | Constraints                                                                                                                              |
| :------------ | :------------------------------- | :---------------------- | :-------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Access Token for the application | `{{PARTNER_APP_TOKEN}}` | String    | Required          | Should be a valid Partner App Access Token                                                                                               |
| appId         | App ID to fetch the access token | `{{APP_ID}}`            | String    | Required          | - The Id should be a valid app Id of Gupshup. - The App must be associated with the account that owns the PARTNER\_APP\_TOKEN being used |
|               |                                  |                         |           |                   |                                                                                                                                          |
|               |                                  |                         |           |                   |                                                                                                                                          |

## Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/{APP_ID}/templates' \
--header 'accept: application/json' \
--header 'content-type: application/x-www-form-urlencoded' \
--header 'token: sk_4087b15819a34606be15483456dcf636' \
--data-urlencode 'elementName=march21templateee' \
--data-urlencode 'content=your otp is welcome' \
--data-urlencode 'category=AUTHENTICATION' \
--data-urlencode 'vertical=Internal_vertical' \
--data-urlencode 'templateType=TEXT' \
--data-urlencode 'example=your otp is 1234' \
--data-urlencode 'footer=This is footer' \
--data-urlencode 'allowTemplateCategoryChange=false' \
--data-urlencode 'buttons=[{"type":"OTP","otp_type":"COPY_CODE","text":"Copy Code"}]' \
--data-urlencode 'languageCode=en'
```

## Sample Response

```
{
	"status": "success",
	"template": 
	{
		"appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
		"buttonSupported": "OTP",
		"category": "AUTHENTICATION",
		"containerMeta": "
		{
			\"appId\":\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\",
			\"data\":\"your otp is welcome\",\"buttons\":
			[
				{
					\"type\":\"OTP\",\"text\":\"Copy Code\",
					\"otp_type\":\"COPY_CODE\"
				}
			],
			\"footer\":\"This is footer\",\"sampleText\":\"your otp is 1234\",
			\"enableSample\":true,\"editTemplate\":false,
			\"allowTemplateCategoryChange\":false,
			\"addSecurityRecommendation\":false}",
			"createdOn": 1742535028869,
			"data": "your otp is welcome\nThis is footer | [Copy Code]",
			"elementName": "march21templateee",
			"id": "695c9c0f-899d-40db-920d-987138230504",
			"languageCode": "en",
			"languagePolicy": "deterministic",
			"meta": "{\"example\":\"your otp is 1234\",\"newAuthTemplate\":true}",
			"modifiedOn": 1742535028869,
			"namespace":"9c7fe92f_2a48_40ec_83d0_69c62a772433",
			"priority": 3,
			"quality": "UNKNOWN",
			"retry": 0,
			"stage": "NONE",
			"status": "PENDING",
			"templateType": "TEXT",
			"vertical": "Internal_vertical",
			"wabaId": "104505526065633"
		}
	}	
}
```

<br />

## Status Codes

<Table align={["left","left","left","left"]}>
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

      <th>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        200
      </td>

      <td>
        \{

        &#x9;"status": "success",

        &#x9;"template":
        &#x9;\{
        &#x9;	"appId": "a41b30f4-d202-4fdb-911e-3a8fbfbfb797",
        &#x9;	"buttonSupported": "OTP",
        &#x9;	"category": "AUTHENTICATION",
        &#x9;	"containerMeta": "
        &#x9;	\{
        &#x9;		\\"appId\\":\\"a41b30f4-d202-4fdb-911e-3a8fbfbfb797\\",
        &#x9;		\\"data\\":\\"your otp is welcome\\",\\"buttons\\":
        &#x9;		\[
        &#x9;			\{
        &#x9;				\\"type\\":\\"OTP\\",\\"text\\":\\"Copy Code\\",
        &#x9;				\\"otp\_type\\":\\"COPY\_CODE\\"
        &#x9;			}
        &#x9;		],
        &#x9;		\\"footer\\":\\"This is footer\\",\\"sampleText\\":\\"your otp is 1234\\",
        &#x9;		\\"enableSample\\":true,\\"editTemplate\\":false,
        &#x9;		\\"allowTemplateCategoryChange\\":false,
        &#x9;		\\"addSecurityRecommendation\\":false}",
        &#x9;		"createdOn": 1742535028869,
        &#x9;		"data": "your otp is welcome\nThis is footer | \[Copy Code]",
        &#x9;		"elementName": "march21templateee",
        &#x9;		"id": "695c9c0f-899d-40db-920d-987138230504",
        &#x9;		"languageCode": "en",
        &#x9;		"languagePolicy": "deterministic",
        &#x9;		"meta": "\{\\"example\\":\\"your otp is 1234\\",\\"newAuthTemplate\\":true}",
        &#x9;		"modifiedOn": 1742535028869,
        &#x9;		"namespace":"9c7fe92f\_2a48\_40ec\_83d0\_69c62a772433",
        &#x9;		"priority": 3,
        &#x9;		"quality": "UNKNOWN",
        &#x9;		"retry": 0,
        &#x9;		"stage": "NONE",
        &#x9;		"status": "PENDING",
        &#x9;		"templateType": "TEXT",
        &#x9;		"vertical": "Internal\_vertical",
        &#x9;		"wabaId": "104505526065633"
        &#x9;	}
        &#x9;}
        }
        }&#x9;
        }
      </td>

      <td>

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

      <td>

      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        `{     "status": "error",     "message": "Too Many Requests"   }`
      </td>

      <td>
        10 Requests per Minute
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `{     "status": "error",     "message": "Internal server error. Please try again later and if the Issue still persists then contact Gupshup Dev Support"   }`
      </td>

      <td>
        For any Internal Error
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>