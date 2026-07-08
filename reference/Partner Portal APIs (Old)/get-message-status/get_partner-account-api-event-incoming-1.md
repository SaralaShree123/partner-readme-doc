---
title: Get Inbound Message Status
excerpt: ''
api:
  file: partner-portal-public-apis-1.json
  operationId: get_partner-account-api-event-incoming
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
        Access Token for the application
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Id (optional)
      </td>

      <td style={{ textAlign: "left" }}>

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
        date in DD-MM-YYYY format.
        Note: Data only gets updated every day at 8am IST / 11.30pm Brazil time / 4.30am Zimbabwe time. Hence you will not get logs for current day.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        start
      </td>

      <td style={{ textAlign: "left" }}>
        1651500199740
      </td>

      <td style={{ textAlign: "left" }}>
        The start time in EPOCH format. The difference between start and end time must be less than or equal to 10 minutes/ 600000 milliseconds.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        end
      </td>

      <td style={{ textAlign: "left" }}>
        1651500799740
      </td>

      <td style={{ textAlign: "left" }}>
        The end time in EPOCH format
      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl --location 'https://partner.gupshup.io/partner/account/api/event/incoming?id=%3Cstring%3E&appId=%3Cstring%3E&date=%3Cstring%3E&start=%3Cinteger%3E&end=%3Cinteger%3E' \
--header 'token: <string>' \
--header 'Accept: application/json'
```

### Sample Response

```json
{
  "eventList":[
    {
      "delay":56,
      "dest":"91832975XXXX",
      "endTime":1650525824281,
      "eventDescription":"Enqueued event sent to the Callback URL",
      "eventId":"569ca252-0e5b-42fb-b5e5-82270e243d",
      "source":"appname",
      "startTime":1650525824225
    }
  ]
}
```