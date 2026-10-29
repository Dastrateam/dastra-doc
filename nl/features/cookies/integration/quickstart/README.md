---
description: >-
  Leer hoe u de Dastra-cookiebanner met de JavaScript-SDK in een webpagina
  integreert.
---

# Snel aan de slag

## Voorwaarde: een openbare API-sleutel ophalen

De banner heeft een openbare API-sleutel nodig. Klik op het tandwielpictogram in de bovenbalk (**Organisatie-instellingen**) en daarna op **API-sleutels** in het linkermenu. Zie [API-sleutelbeheer](../../../settings/api-keys.md).

<figure><img src="../../../../.gitbook/assets/cookies-quickstart-1.png" alt="De pagina API-sleutels met de lijst met sleutels"><figcaption><p>De pagina "API-sleutels"</p></figcaption></figure>

## Uw banner configureren

Configureer uw banner met de onderstaande gids:

{% content-ref url="../../banner/README.md" %}
[Banner instellen](../../banner/README.md)
{% endcontent-ref %}

## De HTML-integratiecode invoegen

Voeg de HTML-code uit de sectie **Installatie** van de banner, kaart **JavaScript**, op alle pagina's van uw website in, **vóór de afsluitende tag `</body>`**. U kunt Google Tag Manager gebruiken om deze code dynamisch op elke pagina in te voegen.

{% hint style="info" %}
De openbare API-sleutel moet vooraf zijn geconfigureerd om de code te laten werken.
{% endhint %}

Dit is de integratiecode van de banner:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={your_public_key}" async></script>
```

De `div` met het id `dastra-cookie-consent` is de plaats waar de banner wordt weergegeven. Het attribuut `data-widgetid` identificeert de banner: het is een geheel getal. `{your_public_key}` is uw openbare API-sleutel, beschikbaar bij **API-sleutels**.

{% hint style="info" %}
Kopieer de code altijd uit de applicatie. Afhankelijk van de hostingregio van uw organisatie verandert het adres van het script (`cdn-bleu.dastra.eu` in plaats van `cdn.dastra.eu`) en het adres van de API (`api-bleu.dastra.eu` in plaats van `api.dastra.eu`).
{% endhint %}

Zodra de code vóór de tag `</body>` van uw website is ingevoegd, verschijnt de banner.

{% hint style="warning" %}
Voor betere prestaties bewaart de browser de banner in de `sessionStorage`.
{% endhint %}

## De banner vanaf een knop opnieuw openen

Toestemming intrekken mag niet moeilijker zijn dan toestemming geven. Voeg aan uw website, bijvoorbeeld in de voettekst, een knop toe die de banner opnieuw opent. Hetzelfde fragment staat in de sectie **Installatie** van de banner:

```html
<button type="button" onclick="dastra.openCookieConsent()">Check your cookie consent</button>
```

## WordPress

Gebruikt u WordPress, dan legt de volgende pagina uit hoe u de banner met de Dastra-plugin installeert.

{% content-ref url="wordpress.md" %}
[Wordpress](wordpress.md)
{% endcontent-ref %}

Zodra de banner is geïntegreerd, gaat u verder met de testfase.

{% content-ref url="../test.md" %}
[De integratie van een banner testen](../test.md)
{% endcontent-ref %}
