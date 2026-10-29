---
description: This page explains how to manage the languages of the consent banner.
---

# Language management

## Add languages to the banner

1. In the menu, click **Cookie consent** > **Banners**, then click your banner.
2. Expand the **Texts and localizations** section.
3. Click **Add a language**, choose the language in the list, then click **Add a language**.

<figure><img src="../../../.gitbook/assets/cookies-languages-1.png" alt="The Texts and localizations section with the list of banner languages and their badges"><figcaption><p>The "Texts and localizations" section</p></figcaption></figure>

The first language in the list is the default language. To choose another one, click **Set as default** next to the language. Click **Edit** to adapt the texts of a language.

In the selection list, the languages in the **Translated languages** group are already translated by Dastra: English (US), English (UK), French, German, Spanish, Italian, Dutch, Greek, Polish and Portuguese. The other languages are in the **Not translated languages** group: you enter the texts yourself.

Each language you add carries a badge:

* **Pre-translated**: the language is one of those Dastra translates;
* **Need translation**: some texts of the language are still empty;
* **Fully translated**: all the texts are filled in.

A counter shows the number of custom texts out of the total number of texts.

## How is the banner language detected?

By default, the banner uses the language set by the `lang` attribute of the page's `<html>` tag. If this attribute is missing, it uses the browser language.

If this language (or its main language, for example `fr` for `fr-FR`) is not in the banner's list, the banner appears in the first language of the list.

## How to force the language of the banner?

To force the language, add the `data-lang` attribute to the banner's `div`:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}" data-lang="fr"></div>
```

If you load the banner with the `loadCookieConsent` method, pass the `lang` option instead:

```javascript
dastra.push(['loadCookieConsent', {
    widgetId: {your_widget_id},
    selector: '#cookie-consent',
    lang: 'fr'
}]);
```
