---
title: Other
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
## User shares location 

```json location
{   
  "app": "DemoApp", 
  "timestamp": 1580228767338,   
  "version": 2, 
  "type": "message",    
  "payload": {  
    "id": "ABEGkYaYVSEEAhCIxTq7KXQIqby1Uo-IO7_E",   
    "source": "918x98xx21x4",   
    "type": "location", 
    "payload": {    
      "longitude": "72.8552172",    
      "latitude": "19.1453658"  
    },  
    "sender": { 
      "phone": "918x98xx21x4",  
      "name": "Smit",   
      "country_code": "91", 
      "dial_code": "8x98xx21x4" 
    }   
  } 
}
```

### Payload object description

| Key         | Description                   | Example    |
| :---------- | :---------------------------- | :--------- |
| `longitude` | The longitude of the location | 72.8552172 |
| `latitude`  | The latitude of the location  | 19.1453658 |

## The user shares a contact card

```json contact card
{
  "app": "DemoApp",
  "timestamp": 1584898884710,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkYaYVSEEAhD9cTZVyPlOGYZJOnviI7OJ",
    "source": "918x98xx21x4",
    "type": "contact",
    "payload": {
      "contacts": [
        {
          "addresses": [
            {
              "city": "Menlo Park",
              "country": "United States",
              "countryCode": "us",
              "state": "CA",
              "street": "1 Hacker Way",
              "type": "HOME",
              "zip": "94025"
            },
            {
              "city": "Menlo Park",
              "country": "United States",
              "countryCode": "us",
              "state": "CA",
              "street": "200 Jefferson Dr",
              "type": "WORK",
              "zip": "94025"
            }
          ],
          "emails": [
            {
              "email": "test@ab.com",
              "type": "WORK"
            },
            {
              "email": "test@whatsapp.com",
              "type": "WORK"
            }
          ],
          "ims": [

          ],
          "name": {
            "first_name": "Dev",
            "formatted_name": "Dev Support",
            "last_name": "Support"
          },
          "org": {
            "company": "Dev Support"
          },
          "phones": [
            {
              "phone": "+91 77383 05433",
              "type": "Mobile"
            }
          ],
          "urls": [
            {
              "url": "https://www.facebook.com",
              "type": "WORK"
            }
          ]
        }
      ]
    },
    "sender": {
      "phone": "918x98xx21x4",
      "name": "Smit",
      "country_code": "91",
      "dial_code": "8x98xx21x4"
    }
  }
}
```

### Payload object description

| Key         | Type                          | Description                                                                                                                                        | Example                                                                                                                                              |
| :---------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| `addresses` | array                         | Full contact address(es). This field can contain `street`, `city`, `state`, `zip`, `country`, `country_code`, and `type` fields.                   | `{ "city": "Menlo Park", "country": "United States", "countryCode": "us", "state": "CA", "street": "1 Hacker Way", "type": "HOME", "zip": "94025" }` |
| `email`     | array                         | Contact email address(es). This field can contain the `email` and `type` fields.                                                                   | `{ "email": "test@fb.com", "type": "WORK" }`                                                                                                         |
| `birthday`  | `YYYY-MM-DD` formatted string | Contacts birthday                                                                                                                                  | 1995-10-06                                                                                                                                           |
| `ims`       | array                         | Messaging contact information. This field contains the `service` and `user_id` fields.                                                             |                                                                                                                                                      |
| `name`      | array                         | Full contact name. This field can contain the `first_name`, `middle_name`, `last_name`, `formatted_name`, `name-prefix`, and `name_suffix` fields. | `{"first_name":"Dev","formatte name": "Dev Support","last_name": "Support"}`                                                                         |
| `org`       | array                         | Contact organization information. This field can contain the `company`, `department`, and `title` fields.                                          | `{"company":"Dev Support"}`                                                                                                                          |
| `phones`    | array                         | Contact phone number(s). This field can contain the `phone`, `wa_id`, and `type` fields.                                                           | `[{"phone":"+917738305433","type":"Mobile"}]`                                                                                                        |
| `urls`      | array                         | Contact URL(s). This field can contain the `url` and `type` fields.                                                                                | `[{"url":"https://www.facebook.com", "type": "WORK" }]`                                                                                              |

## Referral Conversation

This event occurs when a user clicks on an Ad that takes them to the WhatsApp application to send a message to your business. The inbound event includes the ad's information.

```json Referral- On Premise
{
    "app": "DemoApp",
    "timestamp": 1624350395531,
    "version": 2,
    "type": "message",
    "payload": {
        "id": "ABEGkZlpNARoAgo6v1b-zBR7EnX3",
        "source": "918x98xx21x4",
        "type": "text",
        "payload": {
            "text": "I saw this on Facebook..."
        },
        "sender": {
            "phone": "918x98xx21x4",
            "name": "Smit",
            "country_code": "91",
            "dial_code": "8x98xx21x4"
        },
        "referral": {
                "body": "Test post payload",
                "headline": "Demo Gupshup ad",
                "image": {
                    "id": "6a35b528-429d-4fe3-953d-536ef0397ece"
                },
                "source_id": "951242428775548",
                "source_type": "post",
                "source_url": "https://fb.me/2oNXGTsjn"
        }
    }
}
```
```json Referral - Cloud API
{
  "app": "democtwaapp",
  "timestamp": 1712584165510,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "XOMlrzW4gMzj_PXKInEn1Thkp",
    "source": "917735695203",
    "type": "text",
    "payload": {
      "text": "Hello! Can I get more info on this?"
    },
    "sender": {
      "phone": "917735695203",
      "name": "Automation",
      "country_code": "91",
      "dial_code": "7735695203"
    },
    "referral": {
      "headline": "Chat with us",
      "body": "WhatsApp Messenger: More than 2 billion people in over 180 countries use WhatsApp to stay in touch with friends and family, anytime and anywhere. WhatsApp is free and offers simple, secure, reliable messaging and calling, available on phones all over the world.",
      "source_type": "ad",
      "source_id": "6570618339781",
      "source_url": "https://fb.me/3tkSI06bP",
      "media_type": "image",
      "image_url": "https://scontent.xx.fbcdn.net/v/t45.1600-4/355945306_6362276590981_9061280892424810783_n.jpg?stp=c3.122.300.300a_dst-jpg_p306x306&_nc_cat=103&ccb=1-7&_nc_sid=567a6d&_nc_ohc=pYcuA_DcMeUAb4eCSRW&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=00_AfAqx_EFyDb1elHBHbjofACWwoxSytEJt2Aeu5vEyWOdQA&oe=66147417",
      "video_url": "RAW_VIDEO_URL",
      "thumbnail_url": "RAW_THUMBNAIL_URL",
      "ctwa_clid": "ARAHuTtGzmFlOO_WcXezfYBRzrxoH2Emo4kj-mXVvHoMQVU748gp6Sp-IKS2_scLmfnBJSWvvsZpVqjJfMQPM6TJy1_dNFC1ZUztlDk4i1RijetS"
    }
  }
}
```

### Payload object description

| Key             | Description                                                                                                                      | Example                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `source_url`    | The Meta URL that leads to the ad or post clicked by the customer. Opening this URL takes you to the ad viewed by your customer. | `<https://fb.me/3tkSI06bP>`                                            |
| `source_type`   | The Ad's source type. Supported values are ad and post.                                                                          | ad                                                                     |
| `source_id`     | Meta ID for an ad or a post                                                                                                      | 6570618339734                                                          |
| `headline`      | Headline used in the ad or post                                                                                                  | "Chat with us"                                                         |
| `body`          | The body of the Ad or a post.                                                                                                    | "WhatsApp Messenger: More than 2 billion people in over 180 countries" |
| `media_type`    | Media present in the ad or post; image or video.                                                                                 | image                                                                  |
| `image_url`     | URL of the image, when media_type is an image.                                                                                   |                                                                        |
| `video_url`     | URL of the video, when media_type is a video.                                                                                    |                                                                        |
| `thumbnail_url` | URL for the thumbnail, when media_type is a video.                                                                               |                                                                        |
| `ctwa_clid`     | Click ID generated by Meta for ads that click to WhatsApp                                                                        | "ARAHuTtGzmFzrxoH2Emo4kj-1ZUztlDk4i1RijetS"                            |

## Inbound Reactions

End-users on WhatsApp can react to the business's message with an emoji. The payload is sent to the business as an inbound message. This feature is currently available only for CAPI users i.e. users who have WhatsApp docker hosted in Meta Cloud

```json
"body": {
    "app": "sumitqacloudapp",
    "timestamp": 1693819859221,
    "version": 2,
    "type": "message",
    "payload": {
      "id": "wamid.HBgMOTE4MzI5NzUwODAwFQIAEhggMkI4QkY5QjIyOEE4RTE3NDc4M0FBRkIxREY5NTY5N0UA",
      "source": "918329750800",
      "type": "reaction",
      "payload": {
        "id": "9340ac2e-efe7-4836-b379-65a92b281375",
        "gsId": "d8b6b10a-f61e-4ff5-910a-a1ac34b439ef",
        "emoji": "❤️"
      },
      "sender": {
        "phone": "918329750800",
        "name": "~me",
        "country_code": "91",
        "dial_code": "8329750800"
      }
    }
  }
```

### Payload description

| Key   | Description             |
| :---- | :---------------------- |
| id    | WhatsApp msg ID         |
| emoji | Emoji user reacted with |
| gsID  | Gupshup message ID      |