---
title: User events
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## The payload object

```json
{
   "app":"DemoApp",
   "timestamp":1580142086287,
   "version":2,
   "type":"user-event",
   "payload":{
      "phone":"callbackSetPhone"|"918x98xx21x4",
      "type":"sandbox-start"|"opted-in"|"opted-out"
   }
}
```

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `phone`
      </td>

      <td style={{ textAlign: "left" }}>
        The phone number of the customer who has sent the message on WhatsApp, number is in E.164 format
      </td>

      <td style={{ textAlign: "left" }}>
        918x98xx21x4
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        The type of user-event received on your webhook.

        Must be one of these: `sandbox-start`, `opted-in`, `opted-out`.
      </td>

      <td style={{ textAlign: "left" }}>
        Refer to the description given below.
      </td>
    </tr>
  </tbody>
</Table>

## The types of user-events

```json sanbox-start
{
   "app":"DemoApp",
   "timestamp":1580142086287,
   "version":2,
   "type":"user-event",
   "payload":{
      "phone":"callbackSetPhone",
      "type":"sandbox-start"
   }
}
```
```json sandbox-start(Proxy invoked)
{
   "app":"DemoApp",
   "timestamp":1580227393386,
   "version":2,
   "type":"user-event",
   "payload":{
      "phone":"918x98xx21x4",
      "type":"sandbox-start"
   }
}
```
```json opted-in
{
   "app":"DemoApp",
   "timestamp":1584541505908,
   "version":2,
   "type":"user-event",
   "payload":{
      "phone":"918x98xx21x4",
      "type":"opted-in"
   }
}
```
```json opted-out
{
   "app":"DemoApp",
   "timestamp":1584541505908,
   "version":2,
   "type":"user-event",
   "payload":{
      "phone":"918x98xx21x4",
      "type":"opted-out"
   }
}
```

| Type            | Description                                                                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sandbox-start` | This event is received when the app is in Sandbox mode and you have set a callback URL.                                                           |
| `sandbox-start` | This event is received when the app is in Sandbox mode and you have used Gupshup proxy bot to invoke your App using command `Proxy {{app_name}}`. |
| `opted-in`      | This event is received when an end user opt-in to receive notification from a business.                                                           |
| `opted-out`     | This event is received when an end user opt-out from receiving notification from a business.                                                      |