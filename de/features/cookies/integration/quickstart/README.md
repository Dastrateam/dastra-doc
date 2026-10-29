---
description: >-
  Erfahren Sie, wie Sie das Dastra-Cookie-Banner mithilfe des JavaScript-SDK in
  eine Webseite integrieren.
---

# Schnellstart

## Voraussetzung: einen öffentlichen API-Schlüssel abrufen

Das Banner benötigt einen öffentlichen API-Schlüssel. Klicken Sie in der oberen Leiste auf das Zahnradsymbol (**Organisationseinstellungen**) und dann im linken Menü auf **API-Schlüssel & MCP**. Siehe [API-Schlüssel verwalten](../../../settings/api-keys.md).

<figure><img src="../../../../.gitbook/assets/cookies-quickstart-1.png" alt="Die Seite API-Schlüssel & MCP mit der Liste der Schlüssel"><figcaption><p>Die Seite „API-Schlüssel & MCP“</p></figcaption></figure>

## Ihr Banner konfigurieren

Konfigurieren Sie Ihr Banner anhand der folgenden Anleitung:

{% content-ref url="../../banner/README.md" %}
[Einrichtung des Banners](../../banner/README.md)
{% endcontent-ref %}

## Den HTML-Integrationscode einfügen

Fügen Sie den HTML-Code aus dem Abschnitt **Installation** des Banners, Karte **Javascript**, auf allen Seiten Ihrer Website **vor dem schließenden `</body>`-Tag** ein. Sie können Google Tag Manager verwenden, um diesen Code dynamisch auf jeder Seite einzufügen.

{% hint style="info" %}
Damit der Code funktioniert, muss der öffentliche API-Schlüssel zuvor konfiguriert worden sein.
{% endhint %}

Hier ist der Integrationscode des Banners:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={your_public_key}" async></script>
```

Das `div` mit der ID `dastra-cookie-consent` ist die Stelle, an der das Banner angezeigt wird. Das Attribut `data-widgetid` identifiziert das Banner: Es ist eine ganze Zahl. `{your_public_key}` ist Ihr öffentlicher API-Schlüssel, den Sie unter **API-Schlüssel & MCP** finden.

{% hint style="info" %}
Kopieren Sie den Code immer aus der Anwendung. Je nach Hosting-Region Ihrer Organisation ändern sich die Adresse des Skripts (`cdn-bleu.dastra.eu` statt `cdn.dastra.eu`) und die Adresse der API (`api-bleu.dastra.eu` statt `api.dastra.eu`).
{% endhint %}

Sobald der Code vor dem `</body>`-Tag Ihrer Website eingefügt ist, erscheint das Banner.

{% hint style="warning" %}
Aus Leistungsgründen speichert der Browser das Banner im `sessionStorage` zwischen.
{% endhint %}

## Das Banner über eine Schaltfläche erneut öffnen

Das Widerrufen einer Einwilligung muss so einfach sein wie das Erteilen. Fügen Sie Ihrer Website eine Schaltfläche hinzu, die das Banner erneut öffnet, zum Beispiel in der Fußzeile. Dasselbe Snippet wird im Abschnitt **Installation** des Banners angezeigt:

```html
<button type="button" onclick="dastra.openCookieConsent()">Check your cookie consent</button>
```

## WordPress

Wenn Sie WordPress verwenden, erklärt die folgende Seite, wie Sie das Banner mit dem Dastra-Plugin installieren.

{% content-ref url="wordpress.md" %}
[Wordpress](wordpress.md)
{% endcontent-ref %}

Sobald das Banner integriert ist, gehen Sie zur Testphase über.

{% content-ref url="../test.md" %}
[Banner-Integration testen](../test.md)
{% endcontent-ref %}
