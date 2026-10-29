---
description: >-
  In diesem Kapitel erfahren Sie, wie Sie die Einwilligungen unseres
  Cookie-Widgets programmatisch verwalten.
---

# Einwilligung programmatisch verwalten

## Speicherort der Einwilligungen

Standardmäßig werden die Einwilligungen 180 Tage lang als serialisiertes JSON in einem Browser-Cookie mit dem Namen `consent-eu` gespeichert. In der Konfiguration des Banners können Sie:

* den Namen dieses Cookies ändern (**Name des Cookies zur Speicherung der Einwilligung**);
* seine Lebensdauer (**Lebensdauer des Einwilligungs-Cookies**) und seine Domäne (**Cookie-Domäne**) ändern;
* die Einwilligungen stattdessen im localStorage speichern (**Aktivieren Sie den localStorage-Speicher für Einwilligung-Cookies**). Der Schlüssel lautet dann `dastra-consents` oder entspricht dem für das Cookie gewählten Namen.

{% hint style="info" %}
Die Weitergabe der Einwilligungen hängt von diesen Daten ab: Ändern Sie sie nicht direkt. Verwenden Sie das Dastra-JavaScript-SDK.
{% endhint %}

### Zugriff auf den Einwilligungsdienst

Auf den Dastra-Einwilligungsdienst können Sie wie folgt zugreifen:

```javascript
<script>
  window.dastra = window.dastra || [];
  window.dastra.push(['cookieReady',function(manager)
  {console.log(manager.consent)}]);
</script>
```

### Liste der im Einwilligungs-Manager verfügbaren Methoden

In `manager.consent` stehen Ihnen die folgenden Methoden zur Verfügung:

- getAllConsents(): alle Einwilligungen abrufen
- hasConsented(): gibt `true` zurück, wenn der Nutzer bereits eine ausdrückliche Einwilligung erteilt hat
- getPurposeConsent(purposeLabel:string): die Einwilligung für eine Cookie-Kategorie abrufen
- setPurposeConsent(purposeLabel:string, consent:bool): die Einwilligung für eine Kategorie festlegen
- getServiceConsent(serviceShortName:string): die Einwilligung für einen bestimmten Dienst abrufen
- setServiceConsent(serviceShortName:string, consent:bool): die Einwilligung für einen bestimmten Dienst festlegen
- save(): speichert die Einwilligungen und löst die Ereignisse aus
- dispatchEvents(): wendet die aktuellen Einwilligungen an (Ereignisse, Google Consent Mode, Skripte), ohne sie zu speichern

Um das Widget zu öffnen oder zu schließen, verwenden Sie `manager.open()` und `manager.close()`. Außerhalb des `cookieReady`-Callbacks verwenden Sie `dastra.push(['openCookieConsent'])` und `dastra.push(['closeCookieConsent'])`.

### Die Einwilligungen des Nutzers abrufen (getAllConsents)

Sobald Sie Zugriff auf den Einwilligungs-Manager haben, lassen sich die Einwilligungen des aktuellen Nutzers abrufen:

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager){
    // Get the complete consent services list
    var consents = manager.consent.getAllConsents()
}]);
</script>
```

{% hint style="warning" %}
Um `getAllConsents()` **außerhalb des `cookieReady`-Callbacks** aufzurufen (zum Beispiel aus Ihrem eigenen Code, nachdem das Widget geladen wurde), verwenden Sie den vollständigen Pfad:

```javascript
var consents = window.dastra.cookieConsent.consent.getAllConsents();
```

Die alte Syntax auf oberster Ebene `dastra.getAllConsents()` wird nicht mehr unterstützt.
{% endhint %}

Die obige Methode gibt eine Liste aller Einwilligungen des Nutzers zurück:

```javascript
[
  {
    "id": "000000-0000000-000000",
    "name": "Google Analytics",
    "slug": "google-analytics",
    "consent": true,
    "version": "1",
    "date": "2026-10-28T10:00:00.000Z",
    "purpose": "Analytical"
  },
  ...
]
```

### Einwilligungen nach Kategorie abfragen (getPurposeConsent/setPurposeConsent)

Die Cookie-Kategorien werden durch die folgenden Zeichenketten identifiziert:

| Kategorie             | Label          |
| --------------------- | -------------- |
| Erforderliche Cookies | `Necessary`    |
| Einstellungen         | `Preference`   |
| Statistiken           | `Analytical`   |
| Marketing             | `Marketing`    |
| Weitere Cookies       | `Other`        |
| Unkategorisiert       | `Unclassified` |

{% hint style="warning" %}
Verwenden Sie immer die **Zeichenketten-Labels** (zum Beispiel `'Analytical'`): Zahlenwerte werden von der API nicht unterstützt.
{% endhint %}

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady',function(manager){
    let consents = manager.consent.getPurposeConsent('Analytical');
    manager.consent.setPurposeConsent('Analytical', false);

    // persist consent
    manager.consent.save();
}]);
</script>
```

### Einwilligungen nach Dienst verwalten

Um die Einwilligungen nach Dienst zu verwalten, benötigen Sie den vereinfachten Namen des Dienstes, den Sie in der Dienstverwaltung Ihres Widgets finden.

{% hint style="info" %}
**Wie finde ich den vereinfachten Namen des Dienstes?**\
Öffnen Sie die Dienstverwaltung und bearbeiten Sie einen Dienst: Der vereinfachte Name (Slug) des Dienstes steht unter dem Namen des Cookies.
{% endhint %}

![Position des vereinfachten Cookie-Namens](../../../.gitbook/assets/cookies-service-cookie-name-field.png)

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady',function(manager){
    let cookieService = 'google-analytics';
    let consents = manager.consent.getServiceConsent(cookieService);
    manager.consent.setServiceConsent(cookieService, false);

    // persist consent in cookies
    manager.consent.save();
}]);
</script>
```

### Anwendungsbeispiel

Das folgende Beispiel zeigt, wie Sie programmatisch eine vollständige Ablehnung anwenden, zum Beispiel wenn der Nutzer auf eine von Ihnen erstellte Schaltfläche „Alle ablehnen“ klickt oder wenn Sie ein Datenschutzsignal des Browsers berücksichtigen.

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager) {

  // Only act if the user hasn't already made an explicit choice
  if (!manager.consent.hasConsented()) {

    // Opt out of all non-essential categories
    manager.consent.setPurposeConsent('Preference',   false);
    manager.consent.setPurposeConsent('Analytical',   false);
    manager.consent.setPurposeConsent('Marketing',    false);
    manager.consent.setPurposeConsent('Other',        false);
    manager.consent.setPurposeConsent('Unclassified', false);

    // Persist the choice in the browser
    manager.consent.save();
  }

}]);
</script>
```

Sie können ebenso gezielt zustimmen, zum Beispiel um nur Statistik-Cookies zu akzeptieren:

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager) {

  manager.consent.setPurposeConsent('Analytical', true);
  manager.consent.setPurposeConsent('Marketing',  false);
  manager.consent.save();

}]);
</script>
```

### Auf Änderungen der Einwilligung reagieren (das Ereignis `dastra:consents:updated`)

Jedes Mal, wenn ein Nutzer seine Einwilligungsauswahl ändert, über das Widget oder programmatisch mit `save()`, löst Dastra ein Ereignis `dastra:consents:updated` auf `window` aus. Sie können es abonnieren, um Ihre eigene Logik auszuführen: Skripte von Drittanbietern laden, die Oberfläche aktualisieren, ein Analyse-Ereignis senden usw.

```javascript
window.addEventListener('dastra:consents:updated', function(event) {
  // event.detail contains the updated consents
  console.log('Consents updated', event.detail);

  // Example: reload Google Analytics if the user just accepted analytics
  if (window.dastra.cookieConsent.consent.getPurposeConsent('Analytical')) {
    // load or re-enable your analytics scripts here
  }
});
```

{% hint style="info" %}
Dieses Ereignis wird bei jedem Aufruf von `save()` oder `dispatchEvents()` ausgelöst und außerdem bei jedem Laden der Seite, wenn das Widget die gespeicherte Auswahl anwendet. Um nur auf Änderungen des Besuchers zu reagieren, registrieren Sie den Listener innerhalb von `dastra:consents:ready` (siehe [Google Tag Manager](blocking/google-tag-manager.md)).
{% endhint %}
