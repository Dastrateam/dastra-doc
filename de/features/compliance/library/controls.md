---
description: Kontrollen sind das zentrale Element des Compliance-Modells von Dastra.
---

# Kontrollen

Kontrollen übersetzen die Anforderungen eines Frameworks in **konkrete Maßnahmen**, die messbar und auditierbar sind, und ermöglichen es, die Wirksamkeit der Compliance im Zeitverlauf nachzuweisen.

Eine Kontrolle kann:

* **eine oder mehrere Anforderungen** abdecken
* von **mehreren Frameworks** gemeinsam genutzt werden
* mit **Tests** und **Risiken** verknüpft werden

***

## Kontrollen verfolgen und verwalten

<figure><img src="../../../.gitbook/assets/image-480.png" alt="Tab Kontrollen eines Frameworks mit der Liste der Kontrollen und ihrer Art der Behebung"><figcaption></figcaption></figure>

Kontrollen lassen sich über zwei sich ergänzende Einstiegspunkte verfolgen.

***

### 1. Vom Framework aus

Im Tab **Kontrollen** eines Frameworks sehen Sie:

* die Kontrollen, die den Anforderungen des Frameworks zugeordnet sind
* ihre Art der Behebung
* die abgedeckten Anforderungen
* die zugehörigen Tests und Risiken

Diese Ansicht ist nützlich, um:

* die Abdeckung eines Frameworks zu verstehen
* die Schlüsselkontrollen zu identifizieren
* die Compliance nach Framework zu steuern

***

### 2. Aus der Kontrollbibliothek

<figure><img src="../../../.gitbook/assets/image-481.png" alt="Kontrollbibliothek mit den Filtern und der Liste aller Kontrollen"><figcaption></figcaption></figure>

Die **Kontrollbibliothek** zentralisiert alle Kontrollen der Organisation, über sämtliche Frameworks hinweg.

Diese Ansicht ermöglicht es,

* **globale Statistiken** zu nutzen (Kontrollen mit Tests, Risiken, Mehrfachzuordnungen, verwaiste Kontrollen)
* Kontrollen zu identifizieren, die in mehreren Frameworks wiederverwendet werden
* die **Qualität und Kohärenz** der Kontrollbibliothek zu verbessern


***

## Bearbeitungsfenster einer Kontrolle

{% columns %}
{% column %}
Im Bearbeitungsfenster legen Sie die Rolle der Kontrolle und ihre Verbindungen zum übrigen Framework-Bestand genau fest.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-440.png" alt="Bearbeitungsfenster einer Kontrolle mit Bezeichnung, Referenz und Art der Behebung"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

### Bezeichnung und Referenz der Kontrolle

* **Bezeichnung der Kontrolle**\
  Beschreibt klar die umgesetzte Aktion oder Maßnahme.
* **Referenz der Kontrolle**\
  Eindeutige Kennung der Kontrolle in der Bibliothek.

{% columns %}
{% column %}
Ein **Referenzgenerator** schlägt automatisch eine Referenz vor, die stimmig ist mit:

* dem Kontext der Kontrolle
* den Namenskonventionen
* den zugehörigen Frameworks

Sie können die vorgeschlagene Referenz frei anpassen.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-441.png" alt="Referenzgenerator, der eine stimmige Referenz für die Kontrolle vorschlägt"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

### Art der Behebung

Jede Kontrolle muss einer **Art der Behebung** zugeordnet werden, die ihre Natur festlegt:

* **Präventiv**\
  Die Kontrolle zielt darauf ab, den Eintritt eines Risikos zu **verhindern**\
  _(z. B. Schulung, Zugriffsregeln, Freigabe vor der Produktivsetzung)_
* **Minderung**\
  Die Kontrolle zielt darauf ab, **Auswirkung oder Eintrittswahrscheinlichkeit** eines bereits bestehenden Risikos **zu verringern**\
  _(z. B. Überwachung, Erkennung, Minderungsplan)_

Diese Unterscheidung dient dazu,

* die Strategie des Risikomanagements zu analysieren
* Prävention und Erkennung auszubalancieren
* den Reifegrad der Compliance zu steuern

***

### Tags

Tags ermöglichen es,

* Kontrollen zu kategorisieren (z. B. Schulung, KI, Sicherheit, Überwachung)
* die Suche und das Filtern zu erleichtern
* die vorherrschenden Themen der Bibliothek zu analysieren

***

## Tests zuordnen

[**Tests**](tests.md) ermöglichen es, das Vorhandensein, die Anwendung und die Wirksamkeit einer Kontrolle zu überprüfen.

### Zuordnung mit KI-Unterstützung

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image-442.png" alt="Liste der einer Kontrolle zugeordneten Tests"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Die KI-Unterstützung schlägt vor:

* **bestehende Tests** der Bibliothek, die für die Kontrolle relevant sind
* bei Bedarf die **Erstellung neuer Tests**

Dieser Ansatz gewährleistet:

* Kohärenz zwischen Kontrollen und Tests
* Zeitersparnis
* Vereinheitlichung der Auditmethoden
{% endcolumn %}
{% endcolumns %}

***

## Anforderungen zuordnen

{% columns %}
{% column %}
Eine Kontrolle kann zugeordnet werden:

* mehreren Anforderungen desselben Frameworks
* Anforderungen **verschiedener Frameworks**

Im Abschnitt **Verwandte Anforderungen** des Bearbeitungsfensters sind die Anforderungen nach Framework gruppiert; neben dem Namen steht die Versionsnummer des Quell-Frameworks (z. B. _Version 2_).



Dies ermöglicht es,

* Kontrollen gemeinsam zu nutzen
* eine interne Kontrolle mit einem regulatorischen Framework zu verknüpfen
* Brücken zwischen Frameworks zu schlagen (z. B. Custom AI ↔ AI ISSP)
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-443.png" alt="Fenster zum Zuordnen einer Kontrolle zu Anforderungen"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## Risiken zuordnen

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image-444.png" alt="Fenster einer Kontrolle mit den zugeordneten Risiken"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Kontrollen können zugeordnet werden:

* **bestehenden** [**Risiken**](risks.md)
* oder **neuen Risiken**, die direkt im Datenblatt der Kontrolle erstellt werden

Die Zuordnung ermöglicht es,

* die von einer Kontrolle abgedeckten Risiken anzuzeigen
* die Wirkung der Kontrolle auf das Restrisiko zu bewerten
* ein stimmiges Risikomanagement aufzubauen
{% endcolumn %}
{% endcolumns %}

***

## Kontrollen zusammenführen

Mit der Zeit kann die Kontrollbibliothek redundante oder nahezu identische Kontrollen aus verschiedenen Frameworks enthalten. Die Funktion **Zusammenführen** ermöglicht es, sie in einer einzigen Referenzkontrolle zu konsolidieren.

### So funktioniert die Zusammenführung

Wählen Sie in der Kontrollbibliothek oder in einem Projekt die zusammenzuführenden Kontrollen aus (bis zu 30) und lösen Sie die Zusammenführung über die **Sammelaktionen** aus. Ein Assistent fordert Sie auf, die **Reference version** zu wählen, also die Kontrolle, die erhalten bleibt. Die Zuordnungen der anderen Kontrollen (Nachweise, Anforderungen, Risikoszenarien, abgedeckte Kontrollen) werden ohne Datenverlust auf sie übertragen, anschließend werden die anderen Kontrollen gelöscht.

{% hint style="info" %}
Die Zuordnung erfolgt **vollständig manuell**: Dastra erkennt Duplikate nicht automatisch. Sie wählen selbst die ähnlichen Kontrollen aus, die konsolidiert werden sollen.
{% endhint %}

<figure><img src="../../../.gitbook/assets/fusion-controles-selection.png" alt="Auswahl mehrerer Kontrollen und Menü der Sammelaktionen mit der Option Zusammenführen"><figcaption><p>Wählen Sie bis zu 30 Kontrollen aus und lösen Sie die Zusammenführung über die Sammelaktionen aus</p></figcaption></figure>

Die Vergleichstabelle zeigt die Kontrollen nebeneinander, eine Spalte pro Kontrolle. Wählen Sie die Kontrolle, die erhalten bleiben soll, über die Optionsschaltfläche ihrer Spalte: Sie trägt die Bezeichnung **Reference version**. Die anderen Spalten tragen die Bezeichnung **Keep selected fields**: Nur die Felder, die Sie dort ankreuzen, werden in die Referenzversion übernommen (**Select all** kreuzt die gesamte Spalte an).

<figure><img src="../../../.gitbook/assets/fusion-controles-comparaison.png" alt="Vergleichstabelle der Kontrollen nebeneinander mit Auswahl der zu behaltenden Werte"><figcaption><p>Vergleichen Sie die Kontrollen nebeneinander und wählen Sie Feld für Feld die Werte, die erhalten bleiben sollen: Nachweise, Anforderungen, Risikoszenarien und abgedeckte Kontrollen werden auf die erhaltene Kontrolle übertragen</p></figcaption></figure>

{% hint style="warning" %}
Die Zusammenführung ist unwiderruflich. Prüfen Sie die Zuordnungen jeder Kontrolle, bevor Sie den Vorgang bestätigen.
{% endhint %}

### Typische Anwendungsfälle

* **Deduplizierung**: Mehrere Framework-Importe haben gleichwertige Kontrollen erzeugt: Die Zusammenführung konsolidiert sie ohne Informationsverlust.
* **Übergreifende gemeinsame Nutzung**: Eine Kontrolle, die sowohl ISO 27001 als auch das Framework der KI-Verordnung abdeckt, lässt sich durch Zusammenführen der Kontrollen beider Frameworks gewinnen.
* **Bereinigung der Bibliothek**: Vor einem Audit verbessert das Entfernen verwaister oder redundanter Kontrollen die Lesbarkeit des Compliance-Dashboards.

***

## Zusammenfassung: Warum Kontrollen zentral sind

In Dastra sind Kontrollen der **Konvergenzpunkt** zwischen:

* den Anforderungen (was erwartet wird)
* den Tests (was überprüft wird)
* den Risiken (was gesteuert wird)

Dieser Ansatz ermöglicht:

* eine operative und messbare Compliance
* eine übergreifende Governance
* die Wiederverwendung der Compliance-Anstrengungen
