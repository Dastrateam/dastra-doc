---
description: Learn how to test the integration of a consent banner.
---

# Test the integration of a banner

## Enable the preview mode

In the **Settings** section of the banner, open the advanced settings block and enable **Preview mode**.

<figure><img src="../../../.gitbook/assets/cookies-test-1.png" alt="The Preview mode switch in the Settings section"><figcaption><p>The "Preview mode" switch</p></figcaption></figure>

The preview mode disables the cache of the banner configuration: you see your changes live. It also disables the collection of statistics.

{% hint style="warning" %}
Do not leave the preview mode enabled in production: it degrades the performance of the banner.
{% endhint %}

`localhost` addresses with a port, for example `http://localhost:3000`, are always accepted, with or without the preview mode.

## Preview the banner on your website

Click **Preview banner** at the top of the editor. The button is disabled until an address is set in **Urls authorized (Allowed origins)**. Choose the website, enter the path of a page and the language if needed, then click **Launch preview**. The banner code must already be installed on the targeted website.

## Use the following API key

```
dastra00-0testing1-key
```

{% hint style="info" %}
This key displays an example consent banner. You cannot change its configuration. It is used for integration tests, for example in a jsFiddle.
{% endhint %}
