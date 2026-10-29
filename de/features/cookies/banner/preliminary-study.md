---
description: >-
  Bevor Sie mit der technischen Umsetzung des Dastra-Banners beginnen,
  empfehlen wir ein Cookie-Audit Ihrer Websites.
---

# Vorstudie

## 1. Kontaktieren Sie Ihren Webmaster oder Ihre Webagentur

Bevor Sie das Dastra-Banner umsetzen, empfehlen wir, die Person zu kontaktieren, die für die Einbindung von Tags und anderen Markern auf Ihrer Website zuständig ist, und sie in Ihren Mandanten einzuladen. Diese Person kann dann die von Dastra generierten Codebausteine abrufen, die für die verschiedenen technischen Schritte nötig sind (Einrichtung des Banners, tatsächliches Blockieren von Cookies bei fehlender Einwilligung usw.).

## 2. Führen Sie ein Mini-Audit der Cookies Ihrer Website oder Web-App durch

Für dieses Audit können Sie die folgende Excel-Vorlage verwenden:

{% file src="../../../.gitbook/assets/template-audit.xlsx" %}

Dieses Mini-Audit bereitet die Integrationsarbeit des technischen Teams vor.

### Die mit Ihrem Domainnamen verbundenen Dienste und Cookies auflisten

Zur Unterstützung können Sie das Dastra-Tool zum Scannen von Cookies verwenden: Klicken Sie im Menü auf **Cookie-Banner** > **Banner** > **Banner erstellen** und wählen Sie dann **Website-Analyse**. Es identifiziert die auf Ihrer Website installierten Dienste anhand der Dastra-Cookie-Datenbank.

{% content-ref url="scan.md" %}
[Cookies scannen](scan.md)
{% endcontent-ref %}

Außerdem empfiehlt es sich, alle auf Ihrer Website installierten Dienste genau zu prüfen (Untersuchung des Quellcodes der Seite, Inspektion der Cookies usw.). Tools wie [https://builtwith.com/](https://builtwith.com/) können Ihnen ebenfalls helfen, diese Dienste aufzulisten.

Wir empfehlen, für jede Domain oder Website, die Sie erfassen möchten, eine vollständige Liste der Drittanbieterdienste zu erstellen, die Tracker verwenden.

Sobald Sie die Liste der mit Ihrer Website verbundenen Dienste haben, müssen Sie die Blockierstrategie festlegen.

### Zwecke festlegen

Jeder identifizierte Dienst sollte einer dieser Kategorien zugeordnet werden:

| Typ                           | Id |
| ----------------------------- | -- |
| Unbedingt erforderlich        | 0  |
| Einstellungen                 | 1  |
| Analyse der Besucherzahlen    | 2  |
| Marketing und Nutzererfahrung | 3  |
| Sonstiges                     | 4  |

### Die Art der Integration des Dienstes bestimmen

Für jeden Dienst müssen Sie bestimmen, wie das JS-Tag in die Seite eingebunden ist:

* direktes JavaScript-Tag in der Seite;
* Integration im JS-Code der Seite (interne Entwicklung);
* Integration in einem Tagging-Tool (Google Tag Manager);
* Sonstiges: iframe usw.

### Die anzuwendende Blockierstrategie festlegen

Um Cookies standardmäßig zu blockieren, gibt es mehrere mögliche Strategien, die von Ihren Anforderungen abhängen:

* **Nicht mehr verwenden**: Diese Bibliothek wird tatsächlich nicht benötigt, Sie können sie also vollständig aus den Quellen der Website entfernen;
* **Vollständig blockieren**: Die Ausführung des Tags wird vollständig blockiert, solange der Nutzer die Cookies nicht akzeptiert hat;
* **Teilweise blockieren**: Nur die Tracking-Funktionen werden blockiert (sofern die Bibliothek das erlaubt). Manche Bibliotheken können nämlich in einem vollständig eingeschränkten Modus ohne Leistungseinbußen arbeiten.

{% content-ref url="scan.md" %}
[Cookies scannen](scan.md)
{% endcontent-ref %}
