---
summary: Changes post 1 July 2025, to partner portal and partner APIs
title: Partner PMP Changes
excerpt: Changes post 1 July 2025, to partner portal and partner APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
# Introduction

This guide outlines the recent updates and enhancements to the Partner Portal UI, API changes, and billing/reporting processes following the rollout of Per-Message Pricing (PMP) for WhatsApp Business Platform messages, effective July 1, 2025.

## Partner Portal UI Enhancements

### Dashboard

Introduced a new card, Total Paid Messages, in the dashboard to display the sum of all paid messages to date.

<Image align="center" className="border" border={true} width="70% " src="https://files.readme.io/e737664761f0036c8428deb04c47be93abde0483dccda4e516934718101ef3f5-p1.png" />




### Analytics

Introduced new cards and reports in the Analytics Dashboard and Reports section.

1. Added two new cards: Total Paid Messages and Total Free Messages in the Analytics Dashboard and overview section of Analytics now includes the following cards:

   1. Total Paid messages
   2. Total Free messages
   3. Total PMP cost

   <Image align="center" className="border" border={true} width="70% " src="https://files.readme.io/21f4c3da381bb7a0d6b067eb3a3f3bc93849ebb8d41c2d166e49f262c46f03f0-p2.png" />
2. A new table, Message-Specific Report, including the updated categories, which are downloadable in CSV and PDF formats.  Users can download individual monthly reports for June and July.

<Image align="center" className="border" border={true} width="70% " src="https://files.readme.io/652ebe9be74f9a8e8c809af7b03e37f1d5c05abfbf5cc751a7dda3433458e75f-p3.png" />

## API Enhancements

* The public API endpoint `GET /partner/app/{appId}/usage` reflects the PMP model from July 1, 2025.
* Usage data before July 1 follows the previous structure.

```Text Current Response
\{
  
	"status": "success",
	"partnerAppUsageList": 
	\[
		\{
			"appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
			"appName": "Jan10pass",
			"authentication": 0,
			"cumulativeBill": 0.007,
			"currency": "USD",
			"date": "2024-01-10",
			"discount": 0.0,
			"fep": 0,
			"ftc": 1,
			"gsCap": 75.0,
			"gsFees": 0.007,
			"incomingMsg": 2,
			"outgoingMsg": 4,
			"outgoingMediaMsg": 0,
			"marketing": 0,
			“mmLiteMarketing”: 0,
			"service": 0,
			"templateMsg": 0,
			"templateMediaMsg": 1,
			"totalFees": 0.007,
			"totalMsg": 7,
			"utility": 0,
			"waFees": 0.0,
			"internationalAuthentication": 1
		}
	]
}
```

* Response structure now includes new fields such as utility, freeUtility, and internationalAuthentication for better categorization.

```Text Response after PMP
\{
  
  "status": "success",
  "partnerAppUsageList": [
    \{
      "appId": "bf9ee64c-3d4d-4ac4-8668-732e577007c4",
      "appName": "Jan10pass",
      "authentication": 0,
      "cumulativeBill": 0.007,
      "currency": "USD",
      "date": "2024-01-10",
      "discount": 0.0,
      "fep": 0,
      "ftc": 1,
      "gsCap": 75.0,
      "gsFees": 0.007,
      "incomingMsg": 2,
      "outgoingMsg": 4,
      "outgoingMediaMsg": 0,
      "marketing": 0,
      "mmLiteMarketing": 0,
      "service": 0,
      "templateMsg": 0,
      "templateMediaMsg": 1,
      "totalFees": 0.007,
      "totalMsg": 7,
      "utility": 1,
      "freeUtility": 2,
      "waFees": 0.0,
      "internationalAuthentication": 1
    }
  ]
}
```

* Both WhatsApp fees and Gupshup service (gs) fees are updated to comply with PMP.

## How These Changes Affect Users

* DLR (Delivery Report) events and billing events have changed.
* No charge for utility templates within an open customer service window.
* Message usage and costs are easier to track with the updated Partner Portal UI.
* Billing statements are now more transparent, showing per-message pricing and detailed breakdowns.

These updates are designed to improve transparency, tracking, and compliance with Meta’s WhatsApp Business Platform pricing changes.