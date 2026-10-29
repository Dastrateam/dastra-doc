---
description: >-
  Learn how to integrate the Dastra cookie banner into a web page using the
  JavaScript SDK.
---

# Quick start

## Prerequisite: get a public API key

The banner needs a public API key. Click the gear icon in the top bar (**Organization settings**), then **Api keys & MCP** in the left menu. See [API key management](../../../settings/api-keys.md).

<figure><img src="../../../../.gitbook/assets/cookies-quickstart-1.png" alt="The Api keys & MCP page with the list of keys"><figcaption><p>The "Api keys & MCP" page</p></figcaption></figure>

## Configure your banner

Configure your banner by following the guide below:

{% content-ref url="../../banner/README.md" %}
[README.md](../../banner/README.md)
{% endcontent-ref %}

## Insert the HTML integration code

Insert the HTML code available in the **Installation** section of the banner, **JavaScript** card, **before the closing `</body>` tag** of your website, on all pages. You can use Google Tag Manager to insert this code dynamically on each page.

{% hint style="info" %}
For the code to work, the public API key must be configured beforehand.
{% endhint %}

Here is the banner integration code:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={your_public_key}" async></script>
```

The `div` with the id `dastra-cookie-consent` is where the banner is rendered. The `data-widgetid` attribute identifies the banner: it is an integer. `{your_public_key}` is your public API key, available in **Api keys & MCP**.

{% hint style="info" %}
Always copy the code from the application. Depending on the hosting region of your organization, the address of the script (`cdn-bleu.dastra.eu` instead of `cdn.dastra.eu`) and the address of the API (`api-bleu.dastra.eu` instead of `api.dastra.eu`) change.
{% endhint %}

Once the code is inserted before the `</body>` tag of your website, the banner appears.

{% hint style="warning" %}
For better performance, the browser caches the banner in the `sessionStorage`.
{% endhint %}

## Reopen the banner from a button

Withdrawing consent must be as easy as giving it. Add a button that reopens the banner to your website, for example in the footer. The same snippet is shown in the **Installation** section of the banner:

```html
<button type="button" onclick="dastra.openCookieConsent()">Check your cookie consent</button>
```

## WordPress

If you use WordPress, the following page explains how to install the banner with the Dastra plugin.

{% content-ref url="wordpress.md" %}
[wordpress.md](wordpress.md)
{% endcontent-ref %}

Once the banner is integrated, move on to the testing phase.

{% content-ref url="../test.md" %}
[test.md](../test.md)
{% endcontent-ref %}
