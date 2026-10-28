---
description: >-
  Diese Seite erklärt, wie Sie interne Kennungen der Organisation in die
  Einwilligungsnachweise übertragen
---

# Identifikation der Nutzer

## Funktionsprinzip

Das Prinzip ist folgendes: Sie senden die **eindeutige Kennung des authentifizierten Nutzers** in Ihrem Intranet an das Dastra-Widget, und dieses sendet diese ID bei der Erfassung der Nutzereinwilligung mit. So ist es möglich, die Einwilligungsnachweise mit der Kundendatenbank abzugleichen (CRM, Kundendatenbank, Kundenverzeichnis oder andere...). Im Bereich zur Anzeige der Einwilligungsnachweise wird die übermittelte Nutzerkennung angezeigt.

## Schritt 1: Die Nutzerkennung auswählen

Für diesen Abgleich wählen Sie eine pseudonyme Kennung, die an das Widget übertragen wird, zum Beispiel die interne Kundennummer oder die CRM-Kennung. Diese Variable muss auf der Webseite verfügbar sein und wird im Klartext übertragen: Sie darf keine direkten personenbezogenen Daten enthalten (Name, Vorname, E-Mail-Adresse), auch nicht base64-kodiert, da sich base64 umkehren lässt.


## Schritt 2: Den Integrationscode anpassen

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
