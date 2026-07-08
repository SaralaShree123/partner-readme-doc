---
title: Whatsapp Pay for Partners
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Audience

This document is intended for partners/ISVs who want to use WhatsApp pay APIs. WhatsApp Pay allows customers to pay the businesses without leaving WhatsApp.

# Prerequisites

1. Partners must be approved ISVs listed on Gupshup’s partner portal.
2. Apps must be hosted on Meta Cloud, as WhatsApp Pay is currently available only on the Cloud API with Gupshup.
3. Clients are required to enable callback billing, which is managed internally by the support team.
4. A new v3 callback subscription is required to receive incoming events in the Meta format.
5. Ensure the WABA has a payment configuration in place to send messages containing order details. Partners can set up the payment configuration by choosing the payment gateway on the customer's Facebook Business account.
6. The business owner has administrative access to their Razorpay or PayU payment gateway account.

# Limitations/Out of Scope

1. Payment templates (Order details and order Status) must be created directly on the client's Business Manager UI.
2. The native integration includes passing through the payment webhook to the client's callback. An API for payment status is also available, but the client is responsible for reconciling the payments directly with the PG. Currently, no additional payment reports are provided.
3. It is the responsibility of businesses to validate or sanitize the API responses or webhooks to safeguard against SSRF attacks.

# Payment Configuration

Businesses create a new payment configuration using the WhatsApp Business Manager.  In future, we will also provide APIs to do payment configuration without BM.

## Selection Payment Configuration from QABM

<Image align="center" className="border" border={true} width="70% " src="https://files.readme.io/9553604-aaa.png" />

## Flow Diagram

<Image align="center" className="border" border={true} width="80% " src="https://files.readme.io/208cbc9174db927d816c026402aa90e2918fb11131c32ef1e14f01cc330281ed-Picture1.png" />

# APIs

* <Anchor label="Send Message API" target="_blank" href="https://partner-docs.gupshup.io/reference/passthrough-apis#/">Send Message API</Anchor>
* <Anchor label="Order Details" target="_blank" href="https://partner-docs.gupshup.io/reference/order-details">Order Details</Anchor>
* <Anchor label="Order Status" target="_blank" href="https://partner-docs.gupshup.io/reference/order-status">Order Status</Anchor>
* <Anchor label="Payment Status Check API" target="_blank" href="https://partner-docs.gupshup.io/reference/get_partner-app-appid-payments-payment-configuration-reference-id#/">Payment Status Check API</Anchor>
* <Anchor label="Payment Refund API" target="_blank" href="https://partner-docs.gupshup.io/reference/post_partner-app-appid-payments-refund#/">Payment Refund API</Anchor>
* <Anchor label="Subscription API - V3" target="_blank" href="https://partner-docs.gupshup.io/reference/setsubscription-api-v3#/">Subscription API - V3</Anchor>
* <Anchor label="Event Payloads" target="_blank" href="https://partner-docs.gupshup.io/reference/event-payloads#/">Event Payloads</Anchor>