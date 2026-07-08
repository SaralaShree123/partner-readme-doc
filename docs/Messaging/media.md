---
title: Media
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
When the user sends a message with media (image, document, audio, video, or a sticker), the WhatsApp Business API client will download the media. Once the media downloads, our platform sends the event's notification to your Webhook. It contains information for identifying the media object and enables you to download the media file.

## Common payload object description

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
        `caption`
      </td>

      <td style={{ textAlign: "left" }}>
        **Optional**

        The provided caption for the media is only present if specified.
      </td>

      <td style={{ textAlign: "left" }}>
        Purchase receipt
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `name`
      </td>

      <td style={{ textAlign: "left" }}>
        Media file's name as received from the user
      </td>

      <td style={{ textAlign: "left" }}>
        file1.pdf
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `url`
      </td>

      <td style={{ textAlign: "left" }}>
        You can use this link to download the media file sent by the user.
      </td>

      <td style={{ textAlign: "left" }}>
        [https://filemanager.gupshup.io/fm/wamedia/Jeet20/68f1e51b-ac53-4dfb-b970-7b23431ed1d3c](#)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `content-type`
      </td>

      <td style={{ textAlign: "left" }}>
        MIME type of the media file
      </td>

      <td style={{ textAlign: "left" }}>
        application/pdf
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `urlExpiry`
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp for the expiry of the media download `url`
      </td>

      <td style={{ textAlign: "left" }}>
        1624957005482
      </td>
    </tr>
  </tbody>
</Table>

## Different payloads for different types of inbound media messages

```json Image
{
  "app": "docdeck",
  "timestamp": 1718003620228,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago69N5XB9zTUbl-",
    "source": "919XXXXX4",
    "type": "image",
    "payload": {
      "caption": "Sample image",  
      "url": "https://filemanager.gupshup.io/wa/23038a99-929b-408b-80eb-4d30cebb93d4/wa/media/2f997fea-9696-46c4-a2e5-8667fd27988d?download=false",
      "contentType": "image/jpeg",
      "urlExpiry": 1718608420228
    },
    "sender": {
      "phone": "919XXXXXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXXXX4"
    }
  }
}
```
```json Audio
{
  "app": "docdeck",
  "timestamp": 1718003880179,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6nbYEmVczNV4w",
    "source": "91XXXXX4",
    "type": "audio",
    "payload": {
      "url": "https://filemanager.gupshup.io/wa/23038a99-929b-408b-80eb-4d30cebb93d4/wa/media/60830ca4-c005-420a-9574-50a50c9a7736?download=false",
      "contentType": "audio/ogg; codecs=opus",
      "urlExpiry": 1718608680179
    },
    "sender": {
      "phone": "919XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    }
  }
}
```
```json Video
{
  "app": "docdeck",
  "timestamp": 1718004022842,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6tuN0fAfOdlgC",
    "source": "91XXXXX4",
    "type": "video",
    "payload": {
      "url": "https://filemanager.gupshup.io/wa/23038a99-929b-408b-80eb-4d30cebb93d4/wa/media/f272da13-c601-457c-b8a0-d997536f9d2e?download=false",
      "contentType": "video/mp4",
      "urlExpiry": 1718608822842
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    }
  }
}
```
```json Document
{
  "app": "docdeck",
  "timestamp": 1718004253390,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6VPYl8mM5nl8R",
    "source": "91XXXXX4",
    "type": "file",
    "payload": {
      "caption": "Document caption",   
      "name": "IMG_0068.PNG",
      "url": "https://filemanager.gupshup.io/wa/23038a99-929b-408b-80eb-4d30cebb93d4/wa/media/f716a5c0-712d-4462-bcb6-bae95368f8a3?download=false&fileName=IMG_0068.PNG",
      "contentType": "image/png",
      "urlExpiry": 1718609053390
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX74"
    }
  }
}
```
```json Sticker
{
  "app": "docdeck",
  "timestamp": 1718004338015,
  "version": 2,
  "type": "message",
  "payload": {
    "id": "ABEGkZUTIXZ0Ago6P5sn-0FtPEJq",
    "source": "91XXXXX4",
    "type": "sticker",
    "payload": {
      "url": "https://filemanager.gupshup.io/wa/23038a99-929b-408b-80eb-4d30cebb93d4/wa/media/2e1d1147-272f-4e16-8c2a-1d8066b091d1?download=false",
      "contentType": "image/webp",
      "urlExpiry": 1718609138015
    },
    "sender": {
      "phone": "91XXXXX4",
      "name": "SJ",
      "country_code": "91",
      "dial_code": "9XXXXX4"
    }
  }
}
```