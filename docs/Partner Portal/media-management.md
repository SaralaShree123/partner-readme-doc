---
title: Media Management
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
> ℹ️ Media preview is not working at the moment as on Jan 2025, We are looking at bringing it back as soon as possible.

Media Management is a critical piece that partners must handle to avoid disruptions. Here's what you should do with a media message -

1. Once you receive a media message, you must to store that resource/media in your own system (S3, Cloud Storage or any other storage system you prefer).
2. If you need that resource, then you must get that from the URL in your storage system. By this way you can store it as long as you want/need.
3. If you can't access the URL from AWS, do not call the Gupshup File Manager service as it expires.
4. Also, store the expiry timestamp of media to avoid calling invalid media

Also, if your apps got migrated from on-prem to CAPI, old media will not work hence should not be called at all.

### Rate Limit: (introduced in Jan 2025)

1. To help identify and manage invalid media calls, the FileManager URL will return the following error response for invalid media when rate limit is not hit HTTP Code: 400 / 404  
   Error Body: \{"status": "error","message": "Invalid Media Id"}
   **RECOMMENDED** : We encourage you to use these error codes and message to detect invalid media IDs and avoid making further calls for such media. We kindly request you to avoid fetching outdated media (media older than 7 days for Cloud API and On-premise).
2. If you make 20+ invalid media calls per hour you will hit the rate limit on fetching the media via File manager URL or media ID API with a cooldown period of 1 hour.  
   HTTP code: 429
   Message body: Api rate limit reached due to multiple invalid calls. New quota will be available on \{\{Time_in_epoch}}
