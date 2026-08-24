---
description: >-
  Diese Seite erklärt, wie Sie interne Kennungen der Organisation in die
  Einwilligungsnachweise übertragen
---

# Identifikation der Nutzer

## Funktionsprinzip

Das Prinzip ist folgendes: Sie senden die **eindeutige Kennung des authentifizierten Nutzers** in Ihrem Intranet an das Dastra-Widget, und dieses sendet diese ID bei der Erfassung der Nutzereinwilligung mit. So ist es möglich, die Einwilligungsnachweise mit der Kundendatenbank abzugleichen (CRM, Kundendatenbank, Kundenverzeichnis oder andere...). Im Bereich zur Anzeige der Einwilligungsnachweise wird die übermittelte Nutzerkennung angezeigt.

## Schritt 1: Die Nutzerkennung auswählen

Für diesen Abgleich müssen Sie eine Variable auswählen, die an das Widget übertragen werden soll. Sie können die base64-gehashte E-Mail-Adresse des Nutzers, eine interne Kunden- oder CRM-Kennung verwenden. Diese Variable muss auf der Webseite verfügbar sein und wird im Klartext übertragen. Sie darf keine persönlichen Informationen über den Nutzer enthalten (Name, Vorname, E-Mail im Klartext). &#x20;

{% hint style="info" %}
&#x20;Wenn Sie eine base64-kodierte Zeichenkette senden, wird diese beim Empfang der Nutzereinwilligungen in der Dastra-Datenbank automatisch dekodiert
{% endhint %}

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
    userId: {The userId's variable (email 64bits hash or whatever...)}
}]);
</script>
```

Sie können auch die Methode „set" verwenden

```markup
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array's initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent'
}]);

// Push the userId to dastra's cookies
// It must be pushed after the loadCookieConsent method
dastra.push(['set','cookie:userId',{The userId's variable (email 64bits hash or whatever...)}])
</script>
```
