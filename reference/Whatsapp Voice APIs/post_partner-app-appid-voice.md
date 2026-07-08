---
api:
  file: WA_Voice_Enable_Disable.json
  operationId: post_partner-app-appid-voice
hidden: false
---
## Request Parameters

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Key
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Value
      </th>

      <th style={{ textAlign: "left" }}>
        Data type
      </th>

      <th style={{ textAlign: "left" }}>
        Required/Optional
      </th>

      <th style={{ textAlign: "left" }}>
        Constraints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Authorization
      </td>

      <td style={{ textAlign: "left" }}>
        app Token for the application
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{APP_TOKEN}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        Should be a valid Partner app token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        appId
      </td>

      <td style={{ textAlign: "left" }}>
        App for which the data needs to be updated
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{APP_ID}}
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        App should be in the account whose api key is being used
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        enable
      </td>

      <td style={{ textAlign: "left" }}>
        To enable pass true else pass false.
      </td>

      <td style={{ textAlign: "left" }}>
        \{\{ENABLE}}
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Required
      </td>

      <td style={{ textAlign: "left" }}>
        enable is true/false. Mandatory fields
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        iconVisibility
      </td>

      <td style={{ textAlign: "left" }}>
        * iconVisibility can be used to          show/hide call          button in the          whatsapp app for          end users.
      </td>

      <td style={{ textAlign: "left" }}>
        Supported Values: (a) DEFAULT

        Default Value: Default (Call icon will be visible for end user in the chat)
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        mode
      </td>

      <td style={{ textAlign: "left" }}>
        Mode of usage of whatspp voice
      </td>

      <td style={{ textAlign: "left" }}>
        Supported Values:-

        * GS_SIP
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
        metaData
      </td>

      <td style={{ textAlign: "left" }}>
        SIP configuration data when using GS-SIP
      </td>

      <td style={{ textAlign: "left" }}>
        JSON Array example: mention below request
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Mandatory when using GS-SIP        mode
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        additionalParams
      </td>

      <td style={{ textAlign: "left" }}>
        extra parameters like call_hours
      </td>

      <td style={{ textAlign: "left" }}>
        `{"call_hours":{"status":"ENABLED","timezone_id":"Asia/Kolkata","weekly_operating_hours":[{"day_of_week":"WEDNESDAY","open_time":"0400","close_time":"1020"},{"day_of_week":"TUESDAY","open_time":"0800","close_time":"1020"}],"holiday_schedule":[{"date":"2026-01-01","start_time":"0000","end_time":"2359"}]}}`
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Optional
      </td>

      <td style={{ textAlign: "left" }}>
        1. Calling hours with close time earlier than open time is not allowed
        2. Holiday given in call_hours cannot be a past date
        3. Valid timezone should be used in call_hours
        4. weekly_operating_hours in call_hours cannot be empty
        5. Date format should be followed
        6. More than 2 entries not allowed in weekly_operating_hours schedule in call_hours
        7. Overlapping schedule in call_hours is not allowed
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

### Enablement of voice for an app of a partner (Using WA API)

```
curl --location '{PARTNER_PORTAL_BASE_URL}/partner/app/{appId}/voice' \
--header 'Authorization: {app_token}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'enable={VOICE_STATUS}' \
--data-urlencode 'iconVisibility={ICON_VISIBILITY}' \
--data-urlencode 'mode={VOICE_MODE}' \
--data-urlencode 'metaData={METADATA_FOR_SIP in JSON}'
--data-urlencode 'additionalParams={{ADDITIONAL_PARAMS}}'
```

Below is an example of the SIP configuration metadata format

```Text SIP configuration
[
  {
    "user": "911XXXX258312",
    "username": "911XXXX258312",
    "host": "ip-XX-232-3-XX.ap-XXXXX-1.compute.internal",
    "port": "5071",
    "secret_key": "XXXXXXXXX18fc94ac1488b86c0XXXXXX",
    "force_tcp": false
  }
]
```

## Sample Response

```
{
  "message": "Whatsapp voice status updated to true",
  "status": "success"
}
```

## Status Codes

| Status Code | Response                                                                                                         | Comments                          |    |
| :---------- | :--------------------------------------------------------------------------------------------------------------- | :-------------------------------- | :- |
| **Success** |                                                                                                                  |                                   |    |
| 200         | \{ "message": "Whatsapp voice status updated to true", "status": "success" }                                     |                                   |    |
| **Error**   |                                                                                                                  |                                   |    |
| 401         | \{ "message": "Authentication Failed", "status": "error" }                                                       | When API key authentication fails |    |
| 500         | \{ "message": "Error occurred while updating whatsapp voice status, please try again later.", status": "error" } |                                   |    |

<br />
