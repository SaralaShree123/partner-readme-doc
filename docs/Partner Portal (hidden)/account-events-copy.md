---
title: Account events (COPY)
deprecated: false
hidden: true
metadata:
  robots: index
---
## Account events

Account events are received when an event occurs in a specific WABA. For example, when a WhatsApp business policy is violated by a WABA, or if the messaging tier limit of a WABA is updated.

### The types of account-events

```json review-event
{
  "app": "jeet20",
  "timestamp": 1636986446609,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "review-event",
    "payload": {
      "status": "approved",
      "actionDate": "January 31,2021"
    }
  }
}
```
```json status-event (account violation)
{
  "app": "jeet20",
  "timestamp": 1636986446609,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "status-event",
    "payload": {
      "status": "ACCOUNT_VIOLATION",
      "violation_type": "GAMBLING"
    }
  }
}
```
```json status-event (account disable)
{
  "app": "<appname>",
  "appId": "<id>",
  "timestamp": 1713531530035,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "status-event",
    "payload": {
      "status": "DISABLE",
      "actionDate": "February28,2024"
    }
  }
}
```
```json status-event (account restriction)
{
   "app":"appname",
   "timestamp":1636986446609,
   "version":2,
   "type":"account-event",
   "phone":"9180xxxxxxxx",
   "payload":{
      "type":"status-event",
      "payload":{
         "status":"ACCOUNT_RESTRICTED",
         "restrictionInfo":[
            {
               "restrictionType":"RESTRICTION_ADD_PHONE_NUMBER_ACTION",
               "expiration":1636986446609
            },
            {
               "restrictionType":"RESTRICTED_BIZ_INITIATED_MESSAGING",
               "expiration":1636986446609
            },
            {
               "restrictionType":"RESTRICTED_CUSTOMER_INITIATED_MESSAGING",
               "expiration":1636986446609
            }
         ]
      }
   }
}
```
```json status-event (reinstate)
{
  "app": "ShipxxxxxxxxxxxxxxxxxxWapp",
  "appId": "e4c9dbe0-b1ef-4add-97a2-a8fdba0666ad",
  "phone": "918xxxxxxxxx2",
  "timestamp": 1717061550941,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "status-event",
    "payload": {
      "status": "REINSTATE",
      "actionDate": "30 May 2024"
    }
  }
}
```
```json pndn-event
{
  "app": "jeet20",
  "timestamp": 1636986446609,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "pndn-event",
    "payload": {
      "status": "approved/rejected",
      "rejectedReason": "INVALID_FORMAT"
    }
  }
}
```
```json tier-event
{
  "app": "jeet20",
  "timestamp": 1636986446609,
  "version": 2,
  "type": "account-event",
  "payload": {
    "type": "tier-event",
    "payload": {
      "event": "onboarding/ upgrade/ downgrade /unflagged/ flagged",
      "oldLimit": "TIER_10K",
      "currentLimit": "TIER_100K"
    }
  }
}
```
```json capability-event
{
   "app":"appname",
   "timestamp":1636986446609,
   "version":2,
   "type":"account-event",
   "payload":{
      "type":"capability-event",
      "payload":{
         "maxDailyConversationPerPhone":100,
         "maxPhoneNumbersPerBusiness":100
      }
   }
}
```

### The payload object description

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `review-event`
      </td>

      <td>
        This event is received when the submitted WABA is approved or rejected.
        Possible values: `APPROVED`, `REJECTED`.
      </td>
    </tr>

    <tr>
      <td>
        `status-event`
      </td>

      <td>
        This event is received when the status of the WABA has changed.

        Possible values:

        `ACCOUNT_VIOLATION`: The WABA has been flagged due to policy violation, additionally, the reason for the violation is also received.

        `ACCOUNT_DISABLE`: The WABA has been flagged due to the account being disabled.

        `ACCOUNT_VERIFIED`: When an app of type of Embed is updated from Sandbox to Live.

        `ACCOUNT_RESTRICTED`: The WABA has been restricted for its business capabilities due to WhatsApp's policy violations. One or more of the following restriction types may be imposed on your WABA:

        * `RESTRICTION_ADD_PHONE_NUMBER_ACTION` - Restriction on adding phone numbers to WABA.
        * `RESTRICTED_BIZ_INITIATED_MESSAGING` - Restriction on sending business-initiated messages.
        * `RESTRICTED_CUSTOMER_INITIATED_MESSAGING` - Restriction on the ability to respond to customer-initiated messages.Along with the `type`, you will also receive the expiry for the restriction.Learn more about [policy violations](https://faq.whatsapp.com/general/whatsapp-business-api/how-to-comply-with-the-whatsapp-business-and-commerce-policies).
          Learn more about [WABA restrictions](https://developers.facebook.com/docs/whatsapp/overview/track-waba-policy-violations).An email will be sent informing you of violations and restrictions received for your WABA.
      </td>
    </tr>

    <tr>
      <td>
        `pndn-event`
      </td>

      <td>
        This event is received when the status of the submitted Phone number/Display Name is updated.\
        Possible values:
        `INVALID_FORMAT`, `NAME_END_CLIENT_VIOLATION`, `NAME_FORMAT_UNACCEPTABLE`, `NAME_NOT_CONSISTENT`, `NAME_INDIVIDUAL_ISSUE`, and `NAME_ENDCLIENT_NOTRELATED`.
      </td>
    </tr>

    <tr>
      <td>
        `tier-event`
      </td>

      <td>
        This events notifies you when the quality-related status of a phone number has an update.\
        Possible values for events: `ONBOARDING`, `UPGRADE`, `DOWNGRADE`, `UNFLAGGED`, and `FLAGGED`.
        The current tier limit where this account is and the new tier if it has been updated.
        Possible values are: **TIER\_250, TIER\_1K, TIER\_10K, TIER\_100K, and TIER\_UNLIMITED**
      </td>
    </tr>

    <tr>
      <td>
        `capability-event`
      </td>

      <td>
        This event will update you on your WABA's messaging capabilities. It includes:

        * `maxDailyConversationPerPhone` - the maximum number of unique people a phone number can send messages to. See [Messaging Limits](https://developers.facebook.com/docs/whatsapp/api/rate-limits#messaging) for more information.
        * `maxPhoneNumbersPerBusiness` - Includes the maximum number of phone numbers that can belong to a business.  <br /> If there are multiple phone numbers for the apps in a given WABA **maxDailyConversationPerPhone** will show the minimum value to ensure that businesses are aware of the lowest messaging limit across all their phone numbers. For example, if a business has two phone numbers with different limits (e.g., 1K and 10K), showing the minimum value (1K) will help them understand that they need to be mindful of this lower limit when sending messages from either phone number. <br />
      </td>
    </tr>
  </tbody>
</Table>

### Go-Live Event

Go-Live Event is sent to callback URLs whenever an app completes onboarding.

> 📘 Subscribe to ACCOUNT mode using [subscription API](https://partner-docs.gupshup.io/reference/setsubscription-api-v3#/) to receive the Go-Live event on your registered callback

#### Go-Live Event payload

```Text Go-Live Event payload
{
  "app": "APP_NAME",
  "appId": "APP_ID,
  "phone": "PHONE_NUMBER",
  "timestamp": TIMESTAMP,
  "version": 2,
  "type": "onboarding-event",
  "payload": {
    "type": "docker-status-event",
    "payload": {
      "status": "live",
      "waId": "WABA_ID",
      "namespace" : "META-TEMPLATE-NAMESPACE"
    }
  }
}
```

#### The payload key description

| Key       | Description                                                                                          | Example                              |
| :-------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------- |
| app       | App name                                                                                             | august18app                          |
| appId     | App Id for which partner will receive the go-live event.  The Id should be a valid app Id of Gupshup | 57d9179b-7412-4621-bf86-57ee1962fi12 |
| timestamp | Timestamp of the event received                                                                      | 154826527                            |
| version   | Version                                                                                              | 2                                    |
| type      | Type of the event                                                                                    | onboarding-event                     |
| phone     | Phone number of the app                                                                              | 94225252\*\*                         |
| type      | Event type                                                                                           | docker-status-event                  |
| status    | Status of the event                                                                                  | live                                 |
| wabaId    | waba Id of the app                                                                                   | 180593215\*35185                     |

### MM LITE Webhook Event V2 & V3

Upon successful completion of the MM Lite onboarding flow and all associated backend processes, an account\_update webhook will be triggered for each WhatsApp Business Account (WABA) linked to the Business Manager ID (BMID), signifying successful onboarding.

#### V3 Webhook Event

```Text V3 Webhook Event
{
	"entry": 
	[
		{
			"changes": 
				[
					{
						"field": "account_update",
						"value": 
						{
							"event": "AD_ACCOUNT_LINKED",
							"waba_info": 
							{
								"ad_account_id": "521842584195455",
								"owner_business_id": "1998042230628192",
								"waba_id": "216141188246170"
							}
						}
					}
				],
			"id": "216141188246170",
			"time": 1734607255
		}
	],
	"gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
	"object": "whatsapp_business_account"
}
```

##### The payload object description

| Key                 | Sample Value                         | Description                                                                                                          |
| :------------------ | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| field               | account\_update                      | Category of event                                                                                                    |
| event               | AD\_ACCOUNT\_LINKED                  | Specific name of event inside category                                                                               |
| ad\_account\_id     | 521842584195455                      | Once MM lite onboarding is successful an ad account gets generated and a unique ad account id is associated with it. |
| owner\_business\_id | 1998042230628192                     | Meta generated business id per account                                                                               |
| waba\_id            | 216141188246170                      | Whatsapp Business Account Id                                                                                         |
| id                  | 216141188246170                      | Whatsapp Business Account Id                                                                                         |
| time                | 1734607255                           | Unix time stamp of webhook event                                                                                     |
| gs\_app\_id         | bf9ee64c-3d4d-4ac4-8668-732e577007c4 | GupShup app id                                                                                                       |

#### V2 Webhook Event

```Text V2 Webhook Event
{
	"app": "Jan10pass",
	"appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
	"timestamp": 1743508047545,
	"version": 2,
	"type": "account-event",
	"payload": 
	{
		"type": "status-event",
		"payload": 
		{
			"status": "AD_ACCOUNT_LINKED",
			"waba_id": "216141188246170",
			"owner_business_id": "1998042230628192",
			"ad_account_id": "521842584195455"
		}
	}
}
```

##### The payload object description

| Key                 | Sample Value                         | Description                                                                                                          |
| :------------------ | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| app                 | Jan10pass                            | App Name                                                                                                             |
| appId               | bf9ee64c-3d4d-4ac4-8668-732e577007c4 | GupShup App Id                                                                                                       |
| timestamp           | 1734607255                           | Unix timestamp of webhook event                                                                                      |
| type                | account-event                        | Category of event                                                                                                    |
| status              | AD\_ACCOUNT\_LINKED                  | The specific name of an event inside the category                                                                    |
| waba\_id            | 216141188246170                      | Whatsapp Business Account Id                                                                                         |
| owner\_business\_id | 1998042230628192                     | Meta-generated business id per account                                                                               |
| ad\_account\_id     | 521842584195455                      | Once MM lite onboarding is successful an ad account gets generated and a unique ad account id is associated with it. |