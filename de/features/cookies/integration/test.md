---
description: Erfahren Sie, wie Sie die Integration eines Einwilligungsbanners testen.
---

# Banner-Integration testen

## Den Vorschau-Modus aktivieren

Öffnen Sie im Abschnitt **Konfiguration** des Banners den Block mit den erweiterten Einstellungen und aktivieren Sie **Vorschau-Modus**.

<figure><img src="../../../.gitbook/assets/cookies-test-1.png" alt="Der Schalter Vorschau-Modus im Abschnitt Konfiguration"><figcaption><p>Der Schalter „Vorschau-Modus“</p></figcaption></figure>

Der Vorschau-Modus deaktiviert den Cache der Bannerkonfiguration: Sie sehen Ihre Änderungen live. Außerdem deaktiviert er die Erfassung von Statistiken.

{% hint style="warning" %}
Lassen Sie den Vorschau-Modus nicht in der Produktion aktiviert: Er beeinträchtigt die Leistung des Banners.
{% endhint %}

`localhost`-Adressen mit Port, zum Beispiel `http://localhost:3000`, werden immer akzeptiert, mit oder ohne Vorschau-Modus.

## Das Banner auf Ihrer Website in der Vorschau ansehen

Klicken Sie oben im Editor auf **Vorschau**. Die Schaltfläche ist deaktiviert, solange in **Zulässige URLs (CORS)** keine Adresse eingetragen ist. Wählen Sie die Website aus, geben Sie den Pfad einer Seite und bei Bedarf die Sprache ein und klicken Sie dann auf **Vorschau verfügbar**. Der Banner-Code muss auf der betreffenden Website bereits installiert sein.

## Den folgenden API-Schlüssel verwenden

```
dastra00-0testing1-key
```

{% hint style="info" %}
Dieser Schlüssel zeigt ein Beispiel-Einwilligungsbanner an. Seine Konfiguration können Sie nicht ändern. Er dient für Integrationstests, zum Beispiel in einem jsFiddle.
{% endhint %}
