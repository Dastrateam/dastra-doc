---
description: >-
  Erfahren Sie, wie Sie das Dastra-Cookie-Widget mithilfe des JavaScript-SDK in
  eine Webseite integrieren.
---

# Schnellstart

## Voraussetzung: Abruf eines öffentlichen API-Schlüssels

Um einen öffentlichen Schlüssel des Dastra-SDK abzurufen, besuchen Sie diese Seite: [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api)

![](../../../../.gitbook/assets/Cookie12.png)

<figure><img src="../../../../.gitbook/assets/Cookie13.png" alt=""><figcaption></figcaption></figure>

## Konfigurieren Sie Ihr Widget

Konfigurieren Sie Ihr Widget anhand des folgenden Leitfadens

{% content-ref url="../../configuration-du-widget/" %}
[configuration-du-widget](../../configuration-du-widget/)
{% endcontent-ref %}

## Fügen Sie den HTML-Integrationscode ein

Fügen Sie den HTML-Code, der im Bereich „Code" des Dastra Cookie-Einwilligungsmoduls verfügbar ist, **vor dem Ende des \<BODY>-Tags** Ihrer Website auf allen Seiten ein. Sie können den Google Tag Manager verwenden, um diesen Code dynamisch auf jeder Seite einzufügen.

{% hint style="info" %}
Damit der Code korrekt funktioniert, stellen Sie sicher, dass der öffentliche Schlüssel Ihrer API zuvor korrekt konfiguriert ist.
{% endhint %}

So sieht der Integrationscode des Widgets aus

```markup
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://app.dastra.eu/sdk/dastra.js?key={your_public_key}" async>
</script>
```

Das div mit der ID „dastra-cookie-consent" ist der Platzhalter für die Darstellung Ihres Einwilligungs-Widgets. Das Attribut „data-widgetid" identifiziert das aufgerufene Widget, es ist häufig eine Zahl (int32). {your\_public\_key} entspricht Ihrem öffentlichen [API-Schlüssel, der hier abrufbar ist](https://app.dastra.eu/general-settings/api)

Sobald der Code im \<body>-Tag Ihrer Website eingefügt ist, wird das Widget auf Ihrer Website angezeigt.

{% hint style="warning" %}
Für optimale Leistung wird das Widget automatisch vom Browser im sessionStorage zwischengespeichert
{% endhint %}

## WordPress

Wenn Sie WordPress verwenden, finden Sie im folgenden Link weitere Informationen darüber, wie der generierte Code am Ende des HTML-Tags Ihrer Website eingefügt werden kann.

{% content-ref url="wordpress.md" %}
[wordpress.md](wordpress.md)
{% endcontent-ref %}

Sobald das Widget integriert ist, fahren Sie mit der Testphase fort.

{% content-ref url="../comment-tester-lintegration-dun-widget.md" %}
[comment-tester-lintegration-dun-widget.md](../comment-tester-lintegration-dun-widget.md)
{% endcontent-ref %}
