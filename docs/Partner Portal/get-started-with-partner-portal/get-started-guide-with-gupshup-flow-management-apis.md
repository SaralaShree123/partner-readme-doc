---
title: Get Started Guide with Gupshup Flow Management APIs
excerpt: >-
  This guide will tell you how to use Gupshup Flow management APIs - Partner
  APIs.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ℹ️ Only flow without endpoint is supported. Flow with endpoint is not supported.

WhatsApp Flows is a way to build structured interactions for business messaging. With Flows, businesses can define, configure, and customize messages with rich interactions that give customers more structure in the way they communicate.

You can use Flows to generate leads, recommend products, get new sales leads, or anything else where structured communication is more natural or comfortable for your customers.

Read more about flow [here](https://developers.facebook.com/docs/whatsapp/flows).

**Steps to create a Flow using Gupshup Partner APIs:**

1. **Create a flow**\
   [Create Flow API](https://partner-docs.gupshup.io/reference/createflow) allows the user to create a flow by specifying the flow's name and categories.
   **Note the flow will be created in Draft status.**
2. **Now let’s add components to the Flow**\
   Components are the form elements in flows, how or where will you get the components from?
   * You can just generate the JSON from [Meta Playground](https://developers.facebook.com/docs/whatsapp/flows/playground) - this is an easy way as this provides a UI builder, but please keep in mind that this is not linked to WhatsApp Business Manager.
   * Build your own by using the meta documentation [here](https://developers.facebook.com/docs/whatsapp/flows/reference/components).
3. **Save as .json**
   * Once you have your JSON code please save it with a “.json” extension. Now to attach the JSON to the pre-created flow use the [Update Flow Json API.](https://partner-docs.gupshup.io/reference/updateflowjson)
   * If you want to preview the Flow created use the [Get Preview URL API](https://partner-docs.gupshup.io/reference/getpreviewurl) - This endpoint is used to retrieve the preview URL for a specific flow in an application.
4. **Publish flow**\
   [Publish Flow API](https://partner-docs.gupshup.io/reference/publishflow) is used to make a flow live now the status of the flow will be published.

**Note: Once a Flow is Published it cannot be edited.**

Now your flow is ready to send as a flow message.

**How to Send Flows?**

There are two ways of sending flows

1. **Send flows via Session Message**\
   Use this [API](https://partner-docs.gupshup.io/reference/post_partner-app-appid-v3-flow-message) keep `type` parameter as `individual`
2. **Send flows via Template Message**\
   Keep `type` parameter as `Template`

**Note:**

In both cases, you will need a flow token which you can get from WhatsApp Manager under Flows session Flow ID has to be used as Flow Token.

<Image align="center" className="border" border={true} src="https://files.readme.io/c65af2aafb5974c7a357409cf5274a3f01bb817069826d14c2f9f3d39c737c6c-image.png" />

**Below are some APIs that can come in handy when working with Flows:**

[Get Flow API](https://partner-docs.gupshup.io/reference/getflowbyid) - To retrieve detailed information about a specific flow.

[Get All Flow API](https://partner-docs.gupshup.io/reference/getallflow) - To retrieve a list of all flows associated with a specific appID, the Get All Flow API is used.

[Update Flow API](https://partner-docs.gupshup.io/reference/updateflow) - Used to modify an existing flow within an application by providing the app ID and flow ID.

[Get Flow Json API](https://partner-docs.gupshup.io/reference/getflowjson) - This endpoint is used to retrieve the JSON assets of specific app flows.

[Deprecate Flow API](https://partner-docs.gupshup.io/reference/deprecateflow) - Used to deprecate the flow.

[Delete Flow API](https://partner-docs.gupshup.io/reference/deleteflow) - Used to delete a specific flow in an application by providing the app ID and flow ID. Successful deletion returns a status of "success" with a true value. - Using this API will also remove the Flow from WhatsApp Business Manager

**Subscription**

To manage the subscription effectively, use [subscription API](https://partner-docs.gupshup.io/reference/subscription-api-v3).

Please explicitly subscribe to Flow events to receive all the flow releated events.