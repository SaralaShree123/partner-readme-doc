---
title: Template Events
excerpt: >-
  The following template-event is sent for approved notifying of the template's
  status update.
deprecated: false
hidden: true
metadata:
  robots: index
---
```json template-event
{
  "entry": [
    {
      "changes": [
        {
          "field": "message_template_status_update",
          "value": {
            "event": "APPROVED",
            "gs_template_id": "293d381f-1b62-42b2-ac8b-f86ac8ee0cdd",
            "message_template_id": 1127813312455383,
            "message_template_language": "en_US",
            "message_template_name": "vision_technology",
            "reason": "NONE"
          }
        }
      ],
      "id": "216141188246170",
      "time": 1762506375
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

The following template-event is sent for notifying of the template's status update.

```json template-event
{
  "entry": [
    {
      "changes": [
        {
          "field": "template_category_update",
          "value": {
            "gs_template_id": "293d381f-1b62-42b2-ac8b-f86ac8ee0cdd",
            "message_template_id": 1127813312455383,
            "message_template_language": "en_US",
            "message_template_name": "vision_technology",
            "new_category": "MARKETING"
          }
        }
      ],
      "id": "216141188246170",
      "time": 1762506316
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

The following template-event is sent for Rejected notifying of the template's status update.

```json template-event
{
  "entry": [
    {
      "changes": [
        {
          "field": "message_template_status_update",
          "value": {
            "event": "REJECTED",
            "gs_template_id": "3669ea9a-615a-446a-8c38-71cd85ba4ee1",
            "message_template_id": 1752898802063711,
            "message_template_language": "en",
            "message_template_name": "ai_industries_limited_id_represent",
            "reason": "INVALID_FORMAT"
          }
        }
      ],
      "id": "216141188246170",
      "time": 1762506085
    }
  ],
  "gs_app_id": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
  "object": "whatsapp_business_account"
}
```

The payload object description

<br />

| **Key**                       | **Description**                                                                                                                                           | **Example**                          |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **event**                     | The type of template status event. Indicates the status change triggered by Meta. Possible values include: `APPROVED`, `REJECTED`, `DELETED`, `DISABLED`. | APPROVED                             |
| **gs_template_id**            | The unique template ID on the Gupshup platform.                                                                                                           | 293d381f-1b62-42b2-ac8b-f86ac8ee0cdd |
| **message_template_id**       | The unique template ID assigned by Meta                                                                                                                   | 1127813312455383                     |
| **message_template_language** | The language of the template.                                                                                                                             | en_US                                |
| **message_template_name**     | The template’s name as registered on Meta.                                                                                                                | vision_technology                    |
| **reason**                    | The reason for template rejection. Will be `"NONE"` in case of APPROVED events.                                                                           | NONE                                 |
| **field**                     | The event type sent from Meta under WhatsApp webhook. In this case always: `message_template_status_update`.                                              | message_template_status_update       |
| **id**                        | The WABA ID from which this event originated.                                                                                                             | 216141188246170                      |
| **time**                      | Unix timestamp (seconds) when the template event occurred.                                                                                                | 1762506375                           |
| **gs_app_id**                 | The Gupshup App ID associated with the event.                                                                                                             | bf9ee64c-3d4d-4ac4-8668-732e577007c4 |
| **object**                    | Indicates this webhook event belongs to a WhatsApp Business Account.                                                                                      | whatsapp_business_account            |
