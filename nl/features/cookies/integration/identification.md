---
description: >-
  Deze pagina legt uit hoe u de interne identifiers van de organisatie in het
  bewijs van toestemming kunt traceren.
---

# Gebruikersidentificatie

## Werking

U stuurt de unieke identifier van de geauthenticeerde gebruiker van uw intranet naar de Dastra-banner, die deze identifier doorgeeft bij het verzamelen van de toestemming van de gebruiker. U kunt het bewijs van toestemming dan koppelen aan uw klantenbestand (CRM, klantenregister enzovoort). De identifier die u hebt doorgegeven, wordt weergegeven in het gedeelte waar u de bewijzen van toestemming raadpleegt.

## Stap 1: de gebruikersidentifier kiezen

Kies voor deze koppeling een gepseudonimiseerde identifier om aan de banner door te geven, zoals de interne klant-ID of de CRM-ID. Deze variabele moet beschikbaar zijn op de webpagina en wordt als platte tekst verzonden: ze mag geen directe persoonsgegevens bevatten (achternaam, voornaam, e-mailadres), ook niet base64-gecodeerd, omdat base64 omkeerbaar is.

## Stap 2: de integratiecode aanpassen

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
Afhankelijk van de hostingregio van uw organisatie verandert het adres van het script (`cdn-bleu.dastra.eu` in plaats van `cdn.dastra.eu`). Gebruik het adres van de code die u uit de sectie **Installatie** van de banner hebt gekopieerd.
{% endhint %}
