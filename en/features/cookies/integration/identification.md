---
description: >-
  This page explains how to trace the organization's internal identifiers in the
  proof of consent
---

# User identification

## How it works&#x20;

The principle is the following: you send the **unique identifier of the authenticated user** in your intranet to the dastra widget and it will send this id when collecting the user's consent. This will make it possible to reconcile the proofs of consent with the customer base (CRM, customer base, customer repository or other...). Once in the proofs of consent viewing area, the pushed user id will be displayed.

### Step 1: Choose the user ID&#x20;

To make this match, choose a pseudonymous identifier to pass to the widget, such as the customer's internal ID or CRM ID. This variable must be available in the web page and is sent in plain text: it must not contain any direct personal data (last name, first name, email address), not even base64-encoded, since base64 can be reversed.


### Step 2: Adapt the integration code

```ssml
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>
​
// Dastra's array's initialization
window.dastra = window.dastra || [];
​
// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent',
    userId: {your user's pseudonymous id}
}]);
</script>
```
