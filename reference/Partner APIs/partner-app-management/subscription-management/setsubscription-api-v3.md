---
api:
  file: 2SetSubscription.json
  operationId: subscriptionForApp
hidden: true
---
<Callout icon="📘" theme="info">
  Subscriptions can now be set for sandbox apps as well. Once the app goes live, the current subscription will be retained.
</Callout>

### Request Parameters

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Mandatory/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraint
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        PARTNER_APP_TOKE

        N
      </td>

      <td style={{ textAlign: "left" }}>
        Access Token for the application
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner App Access Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [modes](/reference/setsubscription-api-v3#/modes)
      </td>

      <td style={{ textAlign: "left" }}>
        Stages in subscription processing
      </td>

      <td style={{ textAlign: "left" }}>
        Mandatory
      </td>

      <td style={{ textAlign: "left" }}>
        Should be one of the following : NONE, READ, DELIVERED, SENT, DELETED, FLOWS_MESSAGE,PAYMENTS, ALL, OTHERS,COEXISTENCE,TEMPLATE,ACCOUNT
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        tag
      </td>

      <td style={{ textAlign: "left" }}>
        Name tag for URL
      </td>

      <td style={{ textAlign: "left" }}>
        Mandatory
      </td>

      <td style={{ textAlign: "left" }}>
        Must be unique and mandatory for each app
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        url
      </td>

      <td style={{ textAlign: "left" }}>
        Callback URL
      </td>

      <td style={{ textAlign: "left" }}>
        Mandatory
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid URL
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        version
      </td>

      <td style={{ textAlign: "left" }}>
        Version
      </td>

      <td style={{ textAlign: "left" }}>
        Mandatory
      </td>

      <td style={{ textAlign: "left" }}>
        Should be one of the following : 2,3
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        showOnUI
      </td>

      <td style={{ textAlign: "left" }}>
        Used internally
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        Default value is false
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta
      </td>

      <td style={{ textAlign: "left" }}>
        meta json string (meta json key and value

        will be passed to the subscription URL as headers , users can set custom headers for the URL which can be used for authentication)
      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/app/:appId/subscription' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--data-urlencode 'modes={{modes}}' \
--data-urlencode 'tag={{tagName}}' \
--data-urlencode 'showOnUI={{true/false}}' \
--data-urlencode 'version={{versionNumber}}' \
--data-urlencode 'url={{url}}'
--data-urlencode 'meta={{meta}}'
```

### Sample Response

```json
{
	"status": "success",
	"subscription": 
	{
		"active": true,
		"appId": "bf9ee64c-xxxxxxxx-xxxx-xxxx577007c4",
		"createdOn": 1705574838954,
		"id": "8166",
		"mode": 2047,
		"meta": "{\"headers\":
		{
		\"Authorisation\":\"Bearer eyJhbGciOiJIxxxxxxxxxxxxxxxxxxxxxxxxxx6biZ7Sbhl0N0u_aI\"}
		}"
		"modifiedOn": 1705574838954,
		"showOnUI": false,
		"tag": "V3 Subscription",
		"url":"https://webhook.site/0b092322-b55b-419e-9c74-eb92f2b38553",
		"version": 3
	}
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

        "status": "success",

        "subscription":	\{		"active": true,
         "appId": "bf9ee64c-xxxxxxxx-xxxx-xxxx577007c4",
         "createdOn": 1705574838954,
         "id": "8166",
         "mode": 2047,
         "meta": "\{"headers":
         \{
         "Authorisation":"Bearer eyJhbGciOiJIxxxxxxxxxxxxxxxxxxxxxxxxxx6biZ7Sbhl0N0u_aI"}
         }"
         "modifiedOn": 1705574838954,
         "showOnUI": false,
         "tag": "V3 Subscription",
         "url":"[https://webhook.site/0b092322-b55b-419e-9c74-eb92f2b38553](https://webhook.site/0b092322-b55b-419e-9c74-eb92f2b38553)",
         "version": 3
         }
         }
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
        "status": "error", "message": "Invalid URL Passed" }
      </td>

      <td>
        The URL is not valid
      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        \{  
        "status": "error", "message": "Authentication Failed" }
      </td>

      <td>
        When authentication fails
      </td>
    </tr>

    <tr>
      <td>
        429
      </td>

      <td>
        \{  
        "status": "error", "message": "Too Many Requests" }
      </td>

      <td>
        When the rate limit is exceeded
      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        \{  
        "status": "error", "message": "Unable To Create Subscription" }
      </td>

      <td>
        When error occurred while creating the subscription
      </td>
    </tr>
  </tbody>
</Table>

## Modes

* **TEMPLATE**: The template events get forwarded to subscriptions if TEMPLATE mode is subscribed.
* **ACCOUNT**: The account events get forwarded to subscriptions if ACCOUNT mode is subscribed.
* **PAYMENTS**: Incoming Whatsapp pay events get forwarded to subscriptions if PAYMENTS mode is subscribed. [Only for v3].
* **FLOWS_MESSAGE**: Incoming flow messages get forwarded to subscriptions if FLOWS_MESSAGE mode is subscribed. [Only for v3].
* **MESSAGE**: All incoming messages (not events) except flow messages get forwarded to subscriptions if MESSAGE mode is subscribed.
* **OTHERS**: All incoming new events whose exclusive mode is not present (eg read, delivered, sent, payments) get forwarded to subscriptions if OTHERS mode is subscribed [Only for v3].
* **ALL**: All incoming messages (not events) get forwarded to subscriptions if ALL mode is subscribed [Only for v3].
* **BILLING**: Billing events get forwarded to subscriptions if billing mode is subscribed.
* **FAILED**: The failed events get forwarded to subscriptions if failed mode is subscribed.
* **SENT**: Sent events get forwarded to subscriptions if sent mode is subscribed.
* **DELIVERED**: Delivered events get forwarded to subscriptions if delivered mode is subscribed.
* **READ**: Read events get forwarded to subscriptions if read mode is subscribed.
* **ENQUEUED** Enqueued events get forwarded to subscriptions if enqueued mode is subscribed.
* **COEXISTENCE** Messages sent from mobile app as an event (smb_message_echoes events)
