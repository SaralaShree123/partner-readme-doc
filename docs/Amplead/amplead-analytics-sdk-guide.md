---
summary: AmpLead Analytics SDK Guide
title: AmpLead Analytics SDK Guide
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
The Analytics SDK is a JavaScript code snippet that you can integrate into your website to gain valuable insights.

This document provides a comprehensive guide on using the iframe injection plugin. The plugin dynamically injects an iframe into a specified container element or a default container if none is provided. It ensures that the container is styled to occupy full width and height as required.

> 📘 To use this feature, please fill out the <Anchor label="form" target="_blank" href="https://forms.gle/8K1eprohUU81ex1E6">form</Anchor> to get started. You will receive an automated email from us.

Once the support team replies you will be given an code snippet.

```html Script Example
  <script src="/path/to/your/sdk.min.js" data-service-id="yourServiceId" data-user-api-key="yourUserApiKey" data-container-id="custom-container" defer></script>
```

# Usage

## Basic Usage

To use this plugin, include the script in your HTML file with the required `data-service-id` and `data-user-api-key `attributes. Optionally, you can specify a `data-container-id` to inject the iframe into a custom container.

```html Script Inclusion In HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web App with Injected Iframe</title>
</head>
<body>
  <!-- Custom container element -->
  <div id="custom-container"></div>

  <!-- Include the minified SDK script -->
  <script src="/path/to/your/sdk.min.js" data-service-id="yourServiceId" data-user-api-key="yourUserApiKey" data-container-id="custom-container" defer></script>
</body>
</html>
```

## Attributes

* `data-service-id`: (Required) The service ID for the iframe source URL.
* `data-user-api-key`: (Required) The user API key for the iframe source URL.
* `data-container-id`: (Optional) The ID of the custom container where the iframe should be injected.

# Scenarios

## Scenario 1: Injecting into a Custom Container

If a `data-container-id` attribute is provided and the container exists in the DOM, the iframe will be injected into this container. The container will be styled to have full width, no padding or margin, and a minimum height of 800px.

```html Example
<div id="custom-container"></div>
<script src="/path/to/your/sdk.min.js" data-service-id="yourServiceId" data-user-api-key="yourUserApiKey" data-container-id="custom-container" defer></script>
```

## Scenario 2: Custom Container Not Found

If the `data-container-id` attribute is provided but the specified container is not found in the DOM, the plugin will log a warning and fall back to creating a default div#root container. This default container will occupy the full viewport.

```html Example
<!-- Intentionally no custom-container defined -->

<script src="/path/to/your/sdk.min.js" data-service-id="yourServiceId" data-user-api-key="yourUserApiKey" data-container-id="nonexistent-container" defer></script>
```

## Scenario 3: No Custom Container Provided

If no `data-container-id` attribute is provided, the plugin will create and inject the iframe into a default div#root container, ensuring it occupies the full viewport.

```html Example
<script src="/path/to/your/sdk.min.js" data-service-id="yourServiceId" data-user-api-key="yourUserApiKey" defer></script>
```

## Scenario 4: Missing Required Attributes

If either the data-service-id or data-user-api-key attributes are missing, the plugin will log an error and will not proceed with iframe injection.

```html Example
<!-- Missing data-service-id -->

<script src="/path/to/your/sdk.min.js" data-user-api-key="yourUserApiKey" defer></script>
```

## Scenario 5: Styling Considerations

The plugin ensures that the container (custom or default) is styled appropriately:

* Width: 100%
* Height: 100% (default) or minimum 800px (custom)
* Margin and Padding: 0
* Overflow: hidden

This ensures the iframe fits perfectly within the container.

Demo - [Web App with Injected Iframe](https://dev.gupshup.io/partner-analytics/demo/custom.html)