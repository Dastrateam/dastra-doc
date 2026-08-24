---
description: >-
  Bevor Sie mit der technischen Implementierung des Dastra-Widgets beginnen,
  empfehlen wir Ihnen, zunächst ein Cookie-Audit Ihrer Websites durchzuführen.
---

# Voruntersuchung

## 1. Wenden Sie sich an Ihren Webmaster oder Ihre Webagentur

Bevor Sie das Dastra-Widget implementieren, empfehlen wir Ihnen, sich an die Person zu wenden, die für die Integration der Tags und anderer Marker auf Ihrer Website verantwortlich ist, und sie in Ihren Mandanten einzuladen. Diese Person kann dann die von Dastra generierten Code-Elemente abrufen, die für die Durchführung der verschiedenen technischen Maßnahmen erforderlich sind (Einrichtung des Banners, effektive Blockierung von Cookies bei fehlender Einwilligung...).

## 2. Führen Sie ein Mini-Audit der Cookies Ihrer Website oder Web-App durch

Für dieses Audit können Sie sich auf die folgende Excel-Dateivorlage stützen:

{% file src="../../../.gitbook/assets/template-audit.xlsx" %}

Dieses Mini-Audit wird die Integrationsarbeit des technischen Teams erheblich erleichtern.

### Listen Sie die Dienste/Cookies auf, die mit Ihrer Domain verbunden sind

Zur Unterstützung können Sie unser schlüsselfertiges Cookie-Scan-Tool verwenden: [https://app.dastra.eu/workspace/19/cookie-widget/integration/scan](https://app.dastra.eu/workspace/19/cookie-widget/integration/scan)\
Damit können Sie die auf Ihrer Website installierten Dienste anhand unserer Cookie-Datenbank direkt identifizieren.

{% content-ref url="scannez-les-cookies-deposes-sur-votre-site-web.md" %}
[scannez-les-cookies-deposes-sur-votre-site-web.md](scannez-les-cookies-deposes-sur-votre-site-web.md)
{% endcontent-ref %}

Ergänzend wird empfohlen, alle auf Ihrer Website installierten Dienste genau zu untersuchen (Prüfung des Quellcodes der Seite, Inspektion der Cookies...). Tools wie [https://builtwith.com/](https://builtwith.com/) können Ihnen ebenfalls bei der Auflistung dieser Dienste helfen.

Für jede Domain oder Website, die Sie erfassen möchten, empfehlen wir Ihnen, eine vollständige Liste der Drittanbieterdienste zu erstellen, die Tracker verwenden.

Sobald Sie die Liste der mit Ihrer Website verbundenen Dienste haben, müssen Sie die anzuwendende Blockierungsstrategie festlegen.

### Definition der Verarbeitungszwecke

Jeder identifizierte Dienst muss in eine dieser Kategorien eingeordnet werden:&#x20;

| Typ                       | Id |
| ------------------------- | -- |
| Unbedingt erforderlich    | 0  |
| Präferenzen               | 1  |
| Analytisch                | 2  |
| Marketing                 | 3  |
| Sonstige                  | 4  |

### Identifikation der Integrationsart des Dienstes

Für jeden Dienst müssen Sie feststellen, wie das JS-Tag in die Seite integriert ist:

* JavaScript-Tag direkt in der Seite
* Integration im JS-Code der Seite (interne Entwicklung)
* Integration in einem Tag-Management-Tool (Google Tag Manager)
* Sonstige: iframe, ...

### Definition der anzuwendenden Blockierungsstrategie

Um Cookies standardmäßig zu blockieren, gibt es mehrere mögliche Strategien, die von Ihren Anforderungen abhängen:

* **Nicht mehr verwenden**: Diese Bibliothek ist tatsächlich nicht notwendig, Sie können sie daher vollständig aus den Quellen der Website entfernen;
* **Vollständig blockieren**: Die Ausführung des Tags wird vollständig blockiert, solange der Nutzer die Cookies nicht akzeptiert hat;
* **Teilweise blockieren**: Nur die Tracking-Funktionen werden blockiert (sofern die Bibliothek dies ermöglicht). Einige Bibliotheken können nämlich in einem vollständig degradierten Modus ohne Leistungseinbußen funktionieren.

{% content-ref url="scannez-les-cookies-deposes-sur-votre-site-web.md" %}
[scannez-les-cookies-deposes-sur-votre-site-web.md](scannez-les-cookies-deposes-sur-votre-site-web.md)
{% endcontent-ref %}

