---
title: Send message with GIF template
excerpt: 1. Send Message With GIF Template
hidden: true
---
```curl
curl --location --request POST 'https://partner.gupshup.io/partner/app/{{APP_ID}}/template/msg' \
--header 'Connection: keep-alive' \
--header 'Authorization: {{PARTNER_APP_TOKEN}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'source={{SOURCE}}' \
--data-urlencode 'sandbox={{SANDBOX}}' \
--data-urlencode 'destination={{DESTINATION}}' \
--data-urlencode 'template={"id":"{{TEMPLATE_ID}}","params":{{template_param_list}},"expiration":{{expiration_time_in_UNIX_timestamp_in_milliseconds.}} }' \
--data-urlencode 'src.name={{APP_NAME}}'
```

Status Codes:

<br />

| Status Code | Response                                                                                                                                       | Comments               |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Success** |                                                                                                                                                |                        |
| 200         | `{"status": "submitted", "messageId": "db4*****-8ccc-3a438288e72f"}`                                                                           |                        |
| **Error**   |                                                                                                                                                |                        |
| 429         | `{"status": "error", "message": "Too Many Requests"}`                                                                                          | 10 Requests per Minute |
| 500         | `	{"status": "error", "message": "Internal server error. Please try again later and If Issue still persist then contact Gupshup Dev Support"}` | For any Internal Error |

<br />
