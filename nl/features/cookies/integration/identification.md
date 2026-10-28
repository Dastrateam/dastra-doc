---
description: >-
  Deze pagina legt uit hoe u de interne identifiers van de organisatie kunt traceren
  in de toestemmingsbewijzen
---

# Gebruikersidentificatie

## Hoe het werkt

Het principe is als volgt: u stuurt de **unieke identifier van de geauthenticeerde gebruiker** in uw intranet naar de dastra widget en deze zal deze id versturen bij het verzamelen van de toestemming van de gebruiker. Het is dan mogelijk om het bewijs van toestemming te koppelen aan de klantendatabase (CRM, klantendatabase, klantendatabase, etc.). Eenmaal in het weergavegebied van de toestemmingsbewijzen wordt de geduwde gebruikers-ID weergegeven.

## Stap 1: Kies de gebruikers-ID

Kies hiervoor een gepseudonimiseerde ID om aan de widget door te geven, bijvoorbeeld de interne klant-ID of de CRM-ID. Deze variabele moet beschikbaar zijn op de webpagina en wordt als platte tekst verzonden: ze mag geen directe persoonsgegevens bevatten (achternaam, voornaam, e-mailadres), ook niet base64-gecodeerd, omdat base64 omkeerbaar is.


## Stap 2: Pas de integratiecode aan

```markup
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array's initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent',
    userId: {your user's pseudonymous id}
}]);
</script>
```
