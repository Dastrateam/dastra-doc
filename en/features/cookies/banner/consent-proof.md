---
description: Learn how to collect, view and export proof of cookie consent with Dastra, and how to follow the banner statistics.
---

# Collect proof of cookie consent

Once the cookie consent banner is installed on your website, the **Cookie consent** module collects, keeps and exports **proof of consent**. It also shows the **statistics** of the banner.

## Prerequisites

You must have installed the banner on your website.

{% content-ref url="configure.md" %}
[configure.md](configure.md)
{% endcontent-ref %}

## View the proof of consent

Once the banner is installed, Dastra automatically collects proof of consent from the visitors of your website. To view it:

1. In the menu, click **Cookie consent** > **Cookie consents**.
2. Use the filters above the list: the period (the last 7 days by default), the banner (**All banners**) and, once a banner is chosen, the consented services.
3. Click a row to open the proof.

<figure><img src="../../../.gitbook/assets/cookies-consent-proof-1.png" alt="The list of consents with the period and banner filters"><figcaption><p>The list of consents</p></figcaption></figure>

The cookie consent proof shows the date, the country, the consent fingerprint and the list of services, each marked **Consented** or **Refused**. You can print or delete it.

<figure><img src="../../../.gitbook/assets/cookies-consent-proof-2.png" alt="The detail of a proof of consent"><figcaption><p>The detail of a proof of consent</p></figcaption></figure>

From the list, the **Export** button downloads the proof for the selected period and banner. To delete proof, use the row menu or the **Delete** batch action.

The lifespan of the proof of consent is one year.

{% hint style="info" %}
The collection of proof depends on the **Save consent proof** option in the **Settings** section of the banner. When it is disabled, no proof is kept. To match a proof with a user of your system, see [User identification](../integration/identification.md).
{% endhint %}

## View the statistics

The **Reporting** page follows the activity of your banners.

1. In the menu, click **Cookie consent** > **Reporting**. You can also open the menu of a banner in the list of banners and choose **Stats report**.
2. Choose the period (the last 7 days by default) and, if needed, a banner in **All banners**.

Three charts are displayed, each compared with the previous period:

* **Collected consents**: the volume of choices recorded, with the **Total**, **Full consent**, **Partial consent** and **Refused** indicators;
* **Widget's display**: the number of sessions during which the banner was displayed. The counter increases once per visitor session, and a session lasts at least one hour;
* a third chart counts the times a visitor closed the banner with the close cross.

{% hint style="info" %}
In preview mode, no statistics are collected. Displays are also not counted when the **Save consent proof** option is disabled.
{% endhint %}

To actually apply visitors' choices on your website, go to the next page:

{% content-ref url="go-further.md" %}
[go-further.md](go-further.md)
{% endcontent-ref %}
