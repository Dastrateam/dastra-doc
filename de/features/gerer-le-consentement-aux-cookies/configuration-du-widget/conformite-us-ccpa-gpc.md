---
description: Verwalten Sie die Datenschutz-Compliance für Ihre amerikanischen Nutzer (CCPA/CPRA, GPC, DoNotTrack) mit dem Dastra-Einwilligungs-Widget.
---

# US-Compliance: CCPA, GPC und DoNotTrack

## Regulatorischer Kontext

Im Gegensatz zur DSGVO, die ein **Opt-in** (vorherige Einwilligung) vorschreibt, basiert die amerikanische Gesetzgebung hauptsächlich auf einem **Opt-out**-Modell: Tracker können standardmäßig gesetzt werden, aber der Nutzer muss die Möglichkeit haben, dem einfach zu widersprechen.

Die wichtigsten Vorschriften im Überblick:

| Gesetz      | Bundesstaat | Modell  | In Kraft seit |
| ----------- | ----------- | ------- | ------------- |
| CCPA / CPRA | Kalifornien | Opt-out | 2020 / 2023   |
| CPA         | Colorado    | Opt-out | 2023          |
| VCDPA       | Virginia    | Opt-out | 2023          |
| CTDPA       | Connecticut | Opt-out | 2023          |

{% hint style="info" %}
**GPC ist in Kalifornien verpflichtend**

Seit der CPRA (2023) müssen Unternehmen das Signal **Global Privacy Control (GPC)** als Opt-out-Anfrage für den Verkauf und die Weitergabe personenbezogener Daten anerkennen.
{% endhint %}

---

## Empfohlener Ansatz mit Dastra

### 1. Eine geo-zielgerichtete Variante für die USA erstellen

Der einfachste Weg, Ihre amerikanischen Nutzer zu verwalten, ist die Erstellung einer **geo-zielgerichteten Variante** über den Tab **Varianten** Ihres Widgets.

Für **Kalifornien (CCPA/CPRA)** konfigurieren Sie die Variante mit einem Opt-out-Modell: Nicht-essentielle Cookies sind standardmäßig aktiv, der Nutzer kann sich abmelden. Denken Sie auch daran, einen Link **„Meine Daten nicht verkaufen oder teilen"** im Footer Ihrer Website hinzuzufügen, der das Widget direkt öffnet.

Für **andere US-Bundesstaaten** ohne Banner-Pflicht können Sie die Option **„Kein Banner anzeigen"** mit den gemäß Ihrer Richtlinie konfigurierten Standardeinwilligungen aktivieren.

{% content-ref url="variantes-geo-ciblees.md" %}
[variantes-geo-ciblees.md](variantes-geo-ciblees.md)
{% endcontent-ref %}

---

### 2. GPC- und DoNotTrack-Signale beachten

Zwei Browser-Signale ermöglichen es einem Nutzer, seine Ablehnung der Nachverfolgung anzuzeigen, ohne mit einem Banner zu interagieren:

| Signal                           | Standard | Rechtlich bindend (CA) | Beschreibung                                                |
| -------------------------------- | -------- | ---------------------- | ----------------------------------------------------------- |
| **GPC** (`globalPrivacyControl`) | W3C      | ✅ Ja (CPRA)           | Opt-out-Signal für den Verkauf/die Weitergabe von Daten     |
| **DNT** (`doNotTrack`)           | W3C      | ❌ Nein                | „Nicht verfolgen"-Präferenzsignal (rechtlich nicht bindend) |

Dastra erkennt diese Signale nicht nativ. Das folgende Snippet fängt sie **vor der ersten Nutzerinteraktion** ab und wendet automatisch das Opt-out für die Kategorien Analytisch und Marketing an – vorausgesetzt, der Nutzer hat noch keine explizite Einwilligung in seinem Browser gespeichert.

```html
<script>
  var isOptOut =
    navigator.globalPrivacyControl === true ||
    navigator.doNotTrack === '1' ||
    window.doNotTrack === '1'

  if (isOptOut) {
    window.dastra = window.dastra || []
    window.dastra.push([
      'cookieReady',
      function (manager) {
        if (!manager.consent.hasConsented()) {
          manager.consent.setPurposeConsent('Analytical', false)
          manager.consent.setPurposeConsent('Marketing', false)
          manager.consent.dispatchEvent() // applique les choix sans les persister
        }
      }
    ])
  }
</script>
```

{% hint style="info" %}
**`dispatchEvent()` vs `save()` – was ist der Unterschied?**

- **`dispatchEvent()`** wendet die Auswahl für die aktuelle Sitzung an, **ohne etwas** im localStorage des Browsers zu speichern. Das GPC- oder DNT-Signal wird bei jedem Seitenladen erneut erkannt. Wenn der Nutzer GPC in seinem Browser deaktiviert, wird das normale Verhalten automatisch fortgesetzt. Dies ist der empfohlene Ansatz zur Beachtung dieser Signale.
- **`save()`** speichert die Einwilligung dauerhaft im localStorage, als hätte der Nutzer eine explizite Auswahl über das Widget getroffen. Verwenden Sie dies nur, wenn Sie eine sitzungsübergreifende Auswahl speichern möchten.
  {% endhint %}

{% hint style="info" %}
**Wozu dient `hasConsented()`?**

Diese Prüfung stellt sicher, dass das automatische Opt-out keine Einwilligung überschreibt, die der Nutzer bereits explizit über das Widget erteilt hat. Wenn der Nutzer bereits eine Auswahl getroffen hat, wird diese Auswahl respektiert.
{% endhint %}

{% hint style="warning" %}
Dieses Snippet muss **vor** dem Lade-Tag des Dastra-Widgets platziert werden, damit es beim ersten Laden der Seite berücksichtigt wird.
{% endhint %}

Die Kategorie-Labels zur Verwendung mit `setPurposeConsent`:

| Kategorie           | Label          |
| ------------------- | -------------- |
| Erforderlich        | `Necessary`    |
| Präferenzen         | `Preference`   |
| Analytisch          | `Analytical`   |
| Marketing           | `Marketing`    |
| Sonstige            | `Other`        |
| Nicht klassifiziert | `Unclassified` |

---

## Zusammenfassung

| Mechanismus                      | Implementierung   | Rechtlich erforderlich (CA) |
| -------------------------------- | ----------------- | --------------------------- |
| Geo-zielgerichtete CCPA-Variante | Dastra-Oberfläche | ✅ Ja                       |
| GPC-Erkennung                    | JS-Snippet oben   | ✅ Ja (CPRA)                |
| DNT-Erkennung                    | JS-Snippet oben   | ❌ Empfohlen                |
