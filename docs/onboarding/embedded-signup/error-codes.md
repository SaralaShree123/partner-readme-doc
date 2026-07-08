---
summary: Error Codes
title: Error Codes
deprecated: false
hidden: false
metadata:
  robots: index
---
# Gupshup Specific Error Codes

| Error Code | Error Message                  | Details                                                                                                                                    |
| :--------- | :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| 500        | Internal Server Error          | Contact Gupshup Team.                                                                                                                      |
| 1001       | Last Mapped Bot Failed         | Last Mapped Bot Details And Sender Details Mismatch                                                                                        |
| 1002       | Number Not Exist On WhatsApp   | Number Does Not Exist On WhatsApp                                                                                                          |
| 1003       | Wallet Balance Low             | Unable To Send Message / Check your wallet balance.                                                                                        |
| 1004       | Template Disabled Failure      | Message sending failed as the user is inactive for session message, and template messaging is disabled.                                    |
| 1005       | Template Match Failed          | Message sending failed as the user is inactive for session message, and the template did not match.                                        |
| 1006       | Template Opt-in Failure        | Message sending failed as the user is inactive for session message and has not opted in for template message.                              |
| 1007       | Template Opt-in Match Failure  | Message sending failed as the user is inactive for session message, has not opted in for template message, and the template did not match. |
| 1008       | Neither Proxied Nor Opted-in   | User is not opted in and inactive.                                                                                                         |
| 1009       | Required parameter is missing  | Message sending failed because of required parameter missing                                                                               |
| 1010       | Invalid Media Url              | Invalid Media Url                                                                                                                          |
| 1011       | Invalid Media Size             | Invalid Media Size                                                                                                                         |
| 1012       | Number Opted Out               | Message Sending failed as the phone number is opted out.                                                                                   |
| 4001       | API Rate Limited               | Oops! Something went wrong. Please stop sending messages and contact Gupshup Team with your error code.                                    |
| 4002       | Invalid Response From WhatsApp | Invalid Response From WhatsApp                                                                                                             |
| 4003       | No Template Match              | Message Sending failed as the template did not match.                                                                                      |
| 4004       | Only CAPI Feature              | Message type is only supported on Meta hosted cloud API.                                                                                   |
| 4005       | Paused Template                | Message Sending failed as the template is paused.                                                                                          |

# Meta Error Codes

For Meta-related error codes, you can refer to the [Cloud API Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/) and [On-Premises Error Codes](https://developers.facebook.com/docs/whatsapp/on-premises/errors).

Cloud API Error Codes

<Callout icon="❗️" theme="error">
  Meta is sunsetting On-Premises API. Refer to their [On-Premises API Sunset](https://developers.facebook.com/docs/whatsapp/on-premises/sunset) document for details, and to learn how to migrate to the next-generation Cloud API.
</Callout>
