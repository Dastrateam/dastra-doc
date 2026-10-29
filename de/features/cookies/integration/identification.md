---
description: >-
  Diese Seite erklärt, wie Sie die internen Kennungen der Organisation im
  Einwilligungsnachweis nachvollziehbar machen.
---

# Nutzeridentifizierung

## So funktioniert es

Sie senden die **eindeutige Kennung des authentifizierten Nutzers** Ihres Intranets an das Dastra-Banner, das diese Kennung bei der Erfassung der Einwilligung des Nutzers mitgibt. Anschließend können Sie den Einwilligungsnachweis Ihrem Kundenbestand zuordnen (CRM, Kundenverzeichnis usw.). Die von Ihnen übergebene Kennung wird in dem Bereich angezeigt, in dem Sie die Einwilligungsnachweise einsehen.

## Schritt 1: Die Nutzerkennung wählen

Wählen Sie für diese Zuordnung eine pseudonyme Kennung, die Sie an das Banner übergeben, etwa die interne Kunden-ID oder die CRM-ID. Diese Variable muss auf der Webseite verfügbar sein und wird im Klartext gesendet: Sie darf keine direkten personenbezogenen Daten enthalten (Nachname, Vorname, E-Mail-Adresse), auch nicht Base64-kodiert, da sich Base64 umkehren lässt.

## Schritt 2: Den Integrationscode anpassen

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
Je nach Hosting-Region Ihrer Organisation ändert sich die Adresse des Skripts (`cdn-bleu.dastra.eu` statt `cdn.dastra.eu`). Verwenden Sie die Adresse des Codes, den Sie aus dem Abschnitt **Installation** des Banners kopiert haben.
{% endhint %}
