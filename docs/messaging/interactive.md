---
summary: Interactive
title: Interactive
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
## User replies to your List message

```json
{
  "app": "DemoApp",
  "timestamp": 1580228523976,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkYaYVSEEAhCzqobr15BdMPcRup1fIXAJ",
    "source": "918x98xx21x4",
    "type": "list_reply",
    "payload": {
            "title": "section 1 row 1",
            "id": "list1",
            "reply":"section 1 row 1 1",
            "postbackText":"section 1 row 1 postback payload",
            "description": "first row of first section description"
        },
    "sender": {
      "phone": "918x98xx21x4",
      "name": "John",
      "country_code": "91",
      "dial_code": "8x98xx21x4"
    },
    "context": {
        "id": "gBEGkYaYVSEEAgnPGGVYGg1uNU4",
        "gsId": "cbdafe39-1023-42a7-89d6-6c01a3388bb5"
    }
  }
}
```

### Payload object description

| Key            | Description                                                                                                               | Example                                |
| :------------- | :------------------------------------------------------------------------------------------------------------------------ | :------------------------------------- |
| `title`        | The section's title of the selected message                                                                               | section 1 row 1                        |
| `id`           | The developer defined message ID i.e. the custom ID(alpha-numeric) provided in API request when sending the list message. | list1                                  |
| `reply`        | The title of the list item selected from the section of the list message along with the index of the list item.           | section 1 row 1 1                      |
| `postbackText` | The developer defined `postback` payload for a particular item in the list.                                               | section 1 row 1 postback payload       |
| `description`  | The description of the selected list item                                                                                 | first row of first section description |

## User replies to Quick Reply message

```json
{
    "app": "DemoApp",
    "timestamp": 1580228523976,
    "version": 2,
    "type": "message",
    "payload": {
        "id": "ABEGkYaYVSEEAhCzqobr15BdMPcRup1fIXAJ",
        "source": "918x98xx21x4",
        "type": "quick_reply",
        "payload": {
            "title": "First",
            "id": "qr1",
            "reply": "First 1"
        },
        "sender": {
            "phone": "918x98xx21x4",
            "name": "John",
            "country_code": "91",
            "dial_code": "8x98xx21x4"
        },
        "context": {
            "id": "gBEGkYaYVSEEAgkvE0f1ZkfXX78",
            "gsId": "123b0fb2-0620-493b-8f7e-5a1ceb6d8c58"
        }
    }
}
```

### Payload object description

| Key     | Description                                                                                                               | Example |
| :------ | :------------------------------------------------------------------------------------------------------------------------ | :------ |
| `title` | The title of the button selected by the user                                                                              | First   |
| `id`    | The developer-defined message ID i.e. the custom ID(alpha-numeric) provided in API request when sending the list message. | qr1     |
| `reply` | The title of the button clicked along with the index of the button                                                        | First 1 |

## User replies to your location request message

```json
{
    "app": "Jeet20",
    "phone": "918452850482",
    "timestamp": 1682505204576,
    "version": 2,
    "type": "message",
    "payload": {
        "id": "ABEGkWIFlHeVAhCz32ByUk3D11ju98UPw_BE",
        "source": "916205947795",
        "type": "location",
        "payload": {
            "longitude": "86.1941876",
            "latitude": "22.7622767"
        },
        "sender": {
            "phone": "916205947795",
            "name": "Vishal Kumar",
            "country_code": "91",
            "dial_code": "6205947795"
        },
        "context": {
            "id": "gBEGkWIFlHeVAglFUZUUf5DKWfc",
            "forwarded": false,
            "frequently_forwarded": false
        }
    }
}
```

### Payload object description

| Key         | Description                                                                                                                   | Example                               |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ |
| `id`        | The developer-defined message ID i.e. the custom ID(alpha-numeric) provided in the API request when sending the list message. | ABEGkWIFlHeVAhCz32ByUk3D11ju98UPw\_BE |
| `longitude` | Longitude of user's location in degrees                                                                                       | 86.1941876                            |
| `latitude`  | Latitude of user's location in degrees                                                                                        | 22.7622767                            |