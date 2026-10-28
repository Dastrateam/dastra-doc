---
description: >-
  Dastra unterstützt nativ den Google Consent Mode V2. Diese Seite beschreibt
  die Voraussetzungen und die Schritte zur Aktivierung auf den Diensten Ihres
  Cookie-Widgets.
---

# Google Consent Mode V2

Dastra unterstützt nativ den **Google Consent Mode V2**. Diese Integration sendet ein `consent_update`-Signal an Google Tag Manager (GTM), sobald ein Nutzer seine Einwilligung ausdrückt, damit die Google-Tags diese Wahl respektieren, bevor ein Tracking ausgelöst wird.

## Voraussetzungen

* Das Standard-Einwilligungs-Snippet (siehe Schritt 2) muss im `<head>` Ihrer Website eingefügt werden, **bevor** Google Tag Manager geladen wird.
* Konfigurieren Sie in Google Tag Manager ein **„Google Tag"**, das auf allen Seiten ausgelöst wird.
* Die Integration funktioniert mit **Google Ads** (ohne Personalisierung) und **Google Analytics**.
* Wenn Sie Google Ads Conversion-Tracking- oder Remarketing-Tags verwenden, stellen Sie sicher, dass diese Tags erst nach der Einwilligung ausgelöst werden, mithilfe eines benutzerdefinierten Ereignisses wie `dastra:consent:{service-slug}` (Beispiel: `dastra:consent:googleleads`).

## Schritt 1 — Consent Mode V2 für den Dienst aktivieren

Bearbeiten Sie in der Widget-Integration den betreffenden Dienst (z. B. Google Analytics, Google Ads) und aktivieren Sie den Schalter **„Consent mode V2"**. Nach der Aktivierung sendet das Dastra-Banner automatisch das `consent_update`-Signal an GTM, sobald ein Nutzer mit dem Einwilligungsbanner interagiert.

Wählen Sie anschließend die **Einwilligungstypen** aus, die für diesen Dienst gesteuert werden sollen (standardmäßig alle aktiviert):

* `ad_storage`
* `analytics_storage`
* `ad_user_data`
* `ad_personalization`

<figure><img src="../../../../.gitbook/assets/cookies-service-consent-mode-v2.png" alt=""><figcaption><p>Aktivierung des Consent Mode V2 für einen Dienst des Cookie-Widgets</p></figcaption></figure>

Das einzufügende Standard-Einwilligungs-Snippet wird direkt in der Oberfläche angezeigt: Verwenden Sie die Schaltfläche **Kopieren**, um es zu übernehmen, und folgen Sie dann Schritt 2.

## Schritt 2 — Den Standard-Einwilligungscode vor GTM platzieren

Damit die Google-Tags auf das Einwilligungssignal warten, bevor sie ausgelöst werden, fügen Sie das folgende Snippet **vor** dem GTM-Initialisierungscode in Ihre Seite ein:

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments) }
  gtag('consent', 'default', {
    ad_storage: 'denied',
    analytics_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    wait_for_update: 500
  });
</script>
```

Dieses Snippet weist die Google-Tags an, maximal 500 ms auf das `consent_update`-Signal zu warten, bevor das Tracking ausgeführt wird. Akzeptiert der Nutzer die betreffenden Dienste, löst das Dastra-Banner dieses Signal automatisch aus und die Tags können ausgeführt werden.

{% hint style="warning" %}
Dieses Snippet muss unbedingt **vor** der GTM-Initialisierung platziert werden. Wird es danach geladen, können die Google-Tags ausgelöst werden, ohne auf die Einwilligung zu warten.
{% endhint %}

## Weiterführende Informationen

Für das Auslösen von Tags in Abhängigkeit von den Einwilligungen (dataLayer-Ereignisse, Blocking Triggers...) siehe die Seite zu Google Tag Manager:

{% content-ref url="google-tag-manager.md" %}
[google-tag-manager.md](google-tag-manager.md)
{% endcontent-ref %}
