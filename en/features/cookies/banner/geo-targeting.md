---
description: Display a different cookie banner depending on the user's geographic location.
---

# Geo-targeted variants

## Overview

The Dastra consent module lets you create **geo-targeted variants** of your cookie banner. Each variant is a customized version of the banner (appearance, texts, exposed services) that is automatically displayed based on the **user's geographic location**, detected from their IP address.

This feature is useful for organizations operating across multiple countries or regulatory zones, since cookie consent obligations vary by jurisdiction (GDPR and ePrivacy in Europe, CCPA in California, LGPD in Brazil, etc.).

{% hint style="info" %}
**Why this matters legally**

A banner that is compliant in France is not necessarily compliant for a Californian user (opt-out rather than opt-in) or a UK user (after Brexit, the ICO has its own guidelines). Geo-targeted variants let you adapt your banner to each legal context without multiplying banners.
{% endhint %}

Variants depend on your plan: the variants drop-down is disabled if the feature is not included in your subscription.

***

## Create a geo-targeted variant

### 1. Access the configuration

1. In the menu, click **Cookie consent** > **Banners**, then click your banner.
2. At the top right of the editor, open the drop-down that shows **Default configuration**. It lists the existing variants.
3. Click **Create a geo-targeted variation**.

<figure><img src="../../../.gitbook/assets/cookies-geo-targeting-1.png" alt="The variants drop-down in the banner editor"><figcaption><p>The variants drop-down</p></figcaption></figure>

### 2. Name the variant

Enter a descriptive name in the **Geo-targetted variation label** field (80 characters max), for example `Banner - California (CCPA)` or `Banner - EEA zone`.

### 3. Select the targeted geographic zones

In **Countries or geographical regions targeted by the banner**, choose the **countries or regions** the variant applies to. A search is available within the list.

Dastra provides two shortcuts, under **Pre-select**:

* **EU/EEE**: selects all countries in the European Economic Area.
* **All adequate country**: selects the countries recognized as adequate by the European Commission under Article 45 GDPR.

The list is organized by country and lets you target **sub-national regions** (for example French regions or US states). You can, for instance, create a variant specific to California within a more general banner for the United States.

{% hint style="warning" %}
**Variant priority order**

If multiple variants can apply to the same user (for example a user in Île-de-France with a "France" variant and an "Île-de-France" variant), the **most specific** variant (the region) takes priority over the more general one (the country).
{% endhint %}

### 4. Customize the variant

Once the variant is created, it opens in the editor. You can customize:

* **Templating of the banner**: colors, layout, buttons;
* **Texts and localizations**: texts adapted to the local legal context;
* **Services**: you can restrict or extend the list of trackers presented;
* **Triggers**: display conditions specific to the variant.

{% hint style="info" %}
A variant takes the following settings from the default banner: the allowed URLs, the cookie policy generation, the name, domain and lifetime of the consent cookie, the storage mode, the preview mode and the version key. To change them, open the **Default configuration**.
{% endhint %}

### 5. Disable banner display (optional)

In the section of the variant, the **Disable the banner display (all cookies with default consent will be triggered)** option lets you **not display a banner** to users in the targeted zone.

When enabled, no consent window is shown to the relevant visitors. All cookies are then triggered with their **default consent**, as configured for each service.

{% hint style="warning" %}
**For zones without a prior consent requirement only**

This option is relevant for countries where local regulations do not require active consent before placing cookies (for example certain non-EEA countries without equivalent ePrivacy legislation). Never use it for users located in the EU or EEA, the UK, or any other jurisdiction that requires opt-in.
{% endhint %}

{% hint style="info" %}
The default consent of each service is set in the **Services** section of the banner. Check these values before enabling this option.
{% endhint %}

***

## Typical use cases

| Situation                                           | Recommended configuration                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------ |
| European site with US traffic                       | EEA variant (strict opt-in) + US/California variant (CCPA opt-out)       |
| French site with a German subsidiary                | France variant + Germany variant with texts adapted to BfDI requirements |
| Global site with minimal compliance outside the EEA | Default global banner + EEA variant compliant with GDPR                  |

***

## How it works technically

Dastra detects the location from the visitor's **IP address**, with no configuration on your side. The location is used to choose which variant to display. The visitor's consent cookie does not contain their location, but the detected country and the IP address are recorded with the [proof of consent](consent-proof.md).

{% hint style="info" %}
To test the display of a variant from your browser, use a VPN located in the targeted zone.
{% endhint %}
