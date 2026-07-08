---
title: Partner Rate Limits
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
As we prepare to give you a much more reliable and safer platform than ever, we've organized and introduced rate limits to our partner APIs. We would like to inform you that all the APIs listed here will be following the below mentioned rate limits effective 28th Sep 2023.

### Rate Limits

| API Endpoint                             | Rate Limit                       |
| :--------------------------------------- | :------------------------------- |
| /partner/app/\{appId}/token              | 10/1 minute/appId                |
| /partner/app/\{appId}/health             | 10/1 minute/appId                |
| /partner/app/\{appId}/capping            | 10/1 minute/appId                |
| /partner/app/                            | 10/1 minute                      |
| /partner/account/login                   | 10/1 minute                      |
| /partner/app/\{appId}/templates          | 10/1 minute/appId                |
| /partner/app/\{appId}/template/analytics | 10 requests per 60 seconds/appId |
| /partner/app/\{appId}/subscription       | 5 requests per 60 seconds/appId  |
| /partner/app/\{appId}/mmlite/msg/enable  | 2/1 hour/appId                   |
| /partner/app/\{appId}/media/             | 10 requests per 1 second/appId   |

For all the rest of the APIs, the rate will be 10 / 1 second.

Cooldown time for the rate limit will be 1 second (in the case of per second API limits) or 1 minute (in the case of per minute API limits) and so on.

We shall update the partner documentation with these limits in the coming few days.

We understand the different ways you consume these APIs and the different kinds of automations you may have built over these. It will be great to understand your requirement, and hear your feedback on the introduced rate limits and if you have any concerns about the same. Feel free to reach out to your local CSMs or write to us at [partner.support@gupshup.io](mailto:partner.support@gupshup.io)
