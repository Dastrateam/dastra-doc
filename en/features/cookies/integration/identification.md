---
description: >-
  This page explains how to trace the organization's internal identifiers in the
  proof of consent.
---

# User identification

## How it works

You send the **unique identifier of the authenticated user** of your intranet to the Dastra banner, which passes this identifier when collecting the user's consent. You can then match the proof of consent with your customer base (CRM, customer repository, etc.). The identifier you passed is displayed in the area where you view proof of consent.

## Step 1: Choose the user ID

To make this match, choose a pseudonymous identifier to pass to the banner, such as the customer's internal ID or CRM ID. This variable must be available in the web page and is sent in plain text: it must not contain any direct personal data (last name, first name, email address), not even base64-encoded, since base64 can be reversed.

## Step 2: Adapt the integration code

```html
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent',
    userId: '{your user pseudonymous id}'
}]);
</script>
```

{% hint style="info" %}
Depending on the hosting region of your organization, the address of the script changes (`cdn-bleu.dastra.eu` instead of `cdn.dastra.eu`). Use the address of the code copied from the **Installation** section of the banner.
{% endhint %}
