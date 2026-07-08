---
summary: Single/Multi Product Messages
title: Single/Multi Product Messages
deprecated: false
hidden: true
metadata:
  robots: index
---
## Inbound Message

```Text Inbound_Message
{
    "app": "Extra9",
    "timestamp": 1637840344966,
    "version": 2,
    "type": "message",
    "payload": {
        "id": "ABEGkZlpNARoAgo-sKGeURk3EWXT",
        "source": "919969340468",
        "type": "text",
        "payload": {
            "text": "Hello"
        },
        "sender": {
            "phone": "919969340468",
            "name": "Omkar Mestry",
            "country_code": "91",
            "dial_code": "9969340468"
        }
    }
}
```

## Order placed

```json Order_Placed
{
    "app": "DemoApp",
    "timestamp": 1590854464792,
    "version": 2,
    "type": "order",
    "payload": {
        "id": "ABEGkYaYVSEEAgo-sMx1DoUoQJRW",
        "source": "918x98xx21x4",
        "type": "text",
        "payload": {
            "text": "hi"
        },
        "sender": {
            "phone": "918x98xx21x4",
            "name": "Smit",
            "country_code": "91",
            "dial_code": "8x98xx21x4"
        },
        "context": {
            "catalog": {
                "id": "",
                "order": {
                    "items": [
                        {
                            "id": "",
                            "currency": "",
                            "amount": "",
                            "quantity": ""
                        },
                        {
                            "id": "",
                            "currency": "",
                            "amount": "",
                            "quantity": ""
                        }
                    ]
                }
            }
        }
    }
```

### Inbound message payload object

| Key            | Description                                                                                                       | Example           |
| :------------- | :---------------------------------------------------------------------------------------------------------------- | :---------------- |
| catalog.id     | Catalog ID for the order the user has sent to the business. Businesses can retrieve this ID via Commerce Manager. | 15981492102855917 |
| order.items    | This will contain the array of items that make up the complete order of the user.                                 |                   |
| items.id       | Unique identifier of the product in a catalog. This can be retrieved via Commerce Manager.                        | c388js91ic3       |
| items.currency | The currency of the amount.                                                                                       | INR               |
| items.amount   | The unit price for each item.                                                                                     | 3000              |
| items.quantity | The quantity of an item.                                                                                          | 2                 |

### Common request payload

| Key         | Description                                                                                 | Example          | Required |
| :---------- | :------------------------------------------------------------------------------------------ | :--------------- | :------- |
| channel     | The channel for where the catalog is to be shared                                           | WhatsApp         | Yes      |
| source      | The source phone number i.e. your approved WhatsApp Business API phone number               | 929827248173     | Yes      |
| destination | The phone number of the user with whom the catalog is to be shared                          | 929827248173     | Yes      |
| message     | Please refer to the message payload object explained below                                  |                  | Yes      |
| catalogId   | ID for the catalog you want to use for this message. Retrieve this ID via Commerce Manager. | 1598140221855917 | Yes      |
| src.name    | The app’s name is registered on Gupshup.                                                    | myfirstapp       | Yes      |

### Message Payload Object Description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        type
      </td>

      <td>
        The type of interactive session message. For catalogs, the value must be product\_details.
      </td>

      <td>
        product\_details
      </td>
    </tr>

    <tr>
      <td>
        subType
      </td>

      <td>
        Multi-product or a single product.
        Possible values:

        * product
          * product\_list
      </td>

      <td>
        product\_list
      </td>
    </tr>

    <tr>
      <td>
        catalogId
      </td>

      <td>
        ID for the catalog you want to use for this message. Retrieve this ID via Commerce Manager.
      </td>

      <td>
        1598140221855917
      </td>
    </tr>

    <tr>
      <td>
        productId
      </td>

      <td>
        The ID of the product catalog to link
      </td>

      <td>
        c358js92ic3
      </td>
    </tr>

    <tr>
      <td>
        body.text
      </td>

      <td>
        **Optional**

        The body of the message. Emojis and markdown are supported.

        *Maximum length: 1024 characters.*
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        header.type
      </td>

      <td>
        Possible values: Text
      </td>

      <td>
        text
      </td>
    </tr>

    <tr>
      <td>
        header.text
      </td>

      <td>
        This is the Text for the header. Formatting allows emojis, but not markdown.

        *Maximum length: 60 characters.*
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        footer.text
      </td>

      <td>
        **Optional**

        The footer of the message. Emojis and markdown are supported.

        *Maximum length: 60 characters.*
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        sections.title
      </td>

      <td>
        **Required if the message has more than one section.**

        It is the title of the section.

        *Maximum length: 24 characters.*
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        sections.productList.productId
      </td>

      <td>
        **Required for Multi-Product Messages.**

        Unique identifier of the product in a catalog. This can be retrieved via Commerce Manager.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>