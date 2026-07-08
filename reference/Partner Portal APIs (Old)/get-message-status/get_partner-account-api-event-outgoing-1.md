---
title: Get Outbound Message Status
excerpt: ''
api:
  file: partner-portal-public-apis-1.json
  operationId: get_partner-account-api-event-outgoing
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameters
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Token
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{PARTNER\_APP\_TOKEN}}
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Id (optional)
      </td>

      <td style={{ textAlign: "left" }}>
        9e97a0d-add3-4as557-1535-4cdf47c3fa68
      </td>

      <td style={{ textAlign: "left" }}>
        Unique identifier for a message
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId 
      </td>

      <td style={{ textAlign: "left" }}>
        as97850d-adad3-4557-1535-4cdf47c3asfa68
      </td>

      <td style={{ textAlign: "left" }}>
        Unique identifier for an app
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        date
      </td>

      <td style={{ textAlign: "left" }}>
        02-05-2022
      </td>

      <td style={{ textAlign: "left" }}>
        date in DD-MM-YYYY format.\
        Note: Data only gets updated every day at 8am IST / 11.30pm Brazil time / 4.30am Zimbabwe time. Hence you will not get logs for current day.
      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/account/api/event/outgoing?id=%3Cstring%3E&appId=%3Cstring%3E&date=%3Cstring%3E' \
--header 'token: <string>' \
--header 'Accept: application/json'
```

### Sample Response

```json
 {
            "eventList":[
            {
                "delay":3,
                "dest":"91991183XXXX",
                "endTime":1650524010311,
                "eventDescription":"Send message request received at Gupshup",
                "eventId":"3b506e13-d87d-482d-abc1-b8ac688b7c",
                "source":"91845XXXX087",
                "startTime":1650524010308
            },
            {
                "delay":16,
                "dest":"91991183XXXX",
                "endTime":1650524010340,
                "eventDescription":"Send message completed",
                "eventId":"3b506e13-d87d-482d-abc1-beb8ac688b7c",
                "source":"91845XXXX087",
                "startTime":1650524010324
            }
            ]
        }
```
