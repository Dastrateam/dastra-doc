# Geo-Targeting-Varianten

## Vorstellung

Das Dastra-Einwilligungsmodul ermöglicht es, **geo-targetierte Varianten** Ihres Cookie-Banners zu erstellen. Jede Variante ist eine angepasste Version des Widgets — Erscheinungsbild, Texte, bereitgestellte Dienste —, die automatisch basierend auf dem **geografischen Standort des Nutzers** angezeigt wird, der über seine IP-Adresse erkannt wird.

Diese Funktion ist besonders nützlich für Organisationen, die in mehreren Ländern oder regulatorischen Zonen tätig sind, da die Pflichten zur Cookie-Einwilligung je nach lokaler Gesetzgebung erheblich variieren (DSGVO/ePrivacy in Europa, CCPA in Kalifornien, LGPD in Brasilien usw.).

{% hint style="info" %}
**Warum dies rechtlich wichtig ist**

Ein in Frankreich konformes Banner ist nicht zwangsläufig konform für einen kalifornischen Nutzer (Opt-out statt Opt-in) oder einen britischen Nutzer (post-Brexit hat die ICO eigene Richtlinien). Geo-Targeting-Varianten ermöglichen es Ihnen, Ihre CMP präzise an jeden rechtlichen Kontext anzupassen, ohne die Widgets zu vervielfachen.
{% endhint %}

***

## Eine geo-targetierte Variante erstellen

{% stepper %}
{% step %}
#### Zur Konfiguration navigieren

Wählen Sie im Modul **Cookies** Ihr Widget aus und navigieren Sie zum Reiter **Varianten**.

Klicken Sie auf **"Geo-targetierte Variante erstellen"**.
{% endstep %}

{% step %}
#### Die Variante benennen

Geben Sie eine **Bezeichnung** ein (maximal 80 Zeichen). Wählen Sie einen aussagekräftigen Namen für eine einfache Verwaltung, zum Beispiel: `Banner – Kalifornien (CCPA)` oder `Banner – EWR-Zone`.
{% endstep %}

{% step %}
#### Zielgeografische Zonen auswählen

Wählen Sie die **Länder oder Regionen** aus, für die diese Variante gelten soll. Die Suche ist in der Liste verfügbar.

Dastra bietet zwei Schnellauswahlen:

* **EU/EWR**: wählt automatisch alle Länder des Europäischen Wirtschaftsraums vor.
* **All adequate country**: wählt die Länder vor, die von der Europäischen Kommission im Sinne des Artikels 45 DSGVO als angemessen anerkannt sind.

Die Liste ist nach Ländern organisiert, mit der Möglichkeit, **subnationale Regionen** zu targetieren (z. B.: französische Regionen, US-Bundesstaaten). Dies ermöglicht beispielsweise die Erstellung einer spezifischen Variante nur für Kalifornien innerhalb eines allgemeineren Widgets für die Vereinigten Staaten.

{% hint style="warning" %}
**Prioritätsreihenfolge der Varianten**

Wenn mehrere Varianten auf denselben Nutzer anwendbar sein können (z. B. ein Nutzer in Île-de-France mit einer Variante "Frankreich" und einer Variante "Île-de-France"), hat die **spezifischere** Variante (Region) Vorrang vor der allgemeineren Variante (Land).
{% endhint %}
{% endstep %}

{% step %}
#### Die Variante anpassen

Sobald die Variante erstellt ist, können Sie sie **vollständig unabhängig** vom Haupt-Widget konfigurieren:

* **Erscheinungsbild**: Farben, Layout, Schaltflächen
* **Texte & Übersetzungen**: an den lokalen rechtlichen Kontext angepasste Bezeichnungen
* **Bereitgestellte Dienste**: Sie können die Liste der angezeigten Tracker einschränken oder erweitern
* **Auslöser**: spezifische Anzeigebedingungen
{% endstep %}
{% endstepper %}

***

## Typische Anwendungsfälle

| Situation                                          | Empfohlene Konfiguration                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Europäische Website mit amerikanischem Traffic     | EWR-Variante (striktes Opt-in) + USA/Kalifornien-Variante (CCPA-Opt-out)            |
| Französische Website mit deutscher Niederlassung   | Frankreich-Variante + Deutschland-Variante mit an die BfDI-Anforderungen angepassten Texten |
| Globale Website mit minimaler Compliance außerhalb des EWR | Standard-Widget weltweit + EWR-Variante DSGVO-konform                         |

***

## Technische Funktionsweise

Die geografische Erkennung wird automatisch vom Dastra-SDK anhand der **IP-Adresse** des Nutzers durchgeführt, ohne dass Ihrerseits eine zusätzliche Konfiguration erforderlich ist.

Es werden keine Standortdaten im Einwilligungsprofil des Nutzers gespeichert: Die Geolokalisierung dient ausschließlich zur Auswahl der anzuzeigenden Variante.

{% hint style="info" %}
Um die Anzeige einer bestimmten Variante in Ihrem Browser zu testen, können Sie ein VPN verwenden oder den Dastra-Support kontaktieren, um einen Vorschaumodus nach Zone zu aktivieren.
{% endhint %}

***

## Siehe auch

* [Widget-Erscheinungsbild konfigurieren](/broken/pages/3895867aea5cca94c9192bc3bfbbd348ce81a152)
* [Texte und Übersetzungen](/broken/pages/a2948cf50302184be53cd316c9ea27cc6ebac0c8)
* [Regelmäßige Überprüfung (Aktualität)](/broken/pages/d06b39a1dd12a21c65281f36bbe349e5dcee5c34)
