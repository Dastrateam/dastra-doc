---
description: Integrate the Dastra cookie banner into a hybrid application.
---

# Hybrid applications

A hybrid application displays web pages in a WebView. The SDK then works the same way as on a website.

1. Insert the banner code, copied from the **Installation** section, in the pages loaded by the WebView. See [Quick start](../quickstart/README.md).
2. Add the address of these pages in **Urls authorized (Allowed origins)**, in the **Settings** section of the banner. Without it, the banner does not appear.
3. To match a proof of consent with a user of the application, pass their pseudonymous identifier. See [User identification](../identification.md).
4. To read or change consent from your code, use the JavaScript API of the SDK. See [Manage consent programmatically](../programmatic-consent.md).
5. Add a way to reopen the banner in the application, with `dastra.openCookieConsent()`.

You still need to configure the application's trackers manually. See [Blocking cookies](../blocking/README.md).
