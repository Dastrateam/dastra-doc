---
description: Erfahren Sie, wie Sie eine Datenschutz-Folgenabschätzung (DSFA/PIA) mit Dastra durchführen.
---

# Datenschutz-Folgenabschätzung (DSFA / PIA)

## Was ist eine DSFA / PIA?

Eine Datenschutz-Folgenabschätzung (DSFA), auch Privacy Impact Assessment (PIA) genannt, ist ein Verfahren, das gemäß Artikel 35 der DSGVO erforderlich ist, wenn eine Verarbeitung voraussichtlich ein hohes Risiko für die Rechte und Freiheiten betroffener Personen mit sich bringt.

Die DSFA muss vor der Umsetzung der betreffenden Verarbeitung durchgeführt und überprüft werden, sobald sich die Art der Verarbeitung wesentlich ändert.

## Erfordert diese Verarbeitung eine DSFA?

In Dastra hilft Ihnen die Registerkarte **Folgenabschätzung** jeder Verarbeitung zu bestimmen, ob eine DSFA erforderlich ist. Sie bewertet 9 vom EDSA definierte Risikokriterien:

* Bewertung oder Scoring einschließlich Profiling und Vorhersageaktivitäten
* Automatisierte Entscheidungsfindung mit erheblichen Auswirkungen
* Systematische Überwachung
* Sensible personenbezogene Daten
* Datenverarbeitung in großem Umfang
* Kombination, Abgleich oder Verknüpfung von Daten
* Daten zu schutzbedürftigen Personen
* Innovative Nutzung oder Anwendung neuer Technologien
* Verarbeitung, die betroffene Personen an der Ausübung ihrer Rechte hindert

Wählen Sie für jedes Kriterium "Ja", "Nein" oder "Nicht zutreffend". **Zwei "Ja"-Antworten reichen in der Regel aus**, um die Pflicht zur Durchführung einer DSFA auszulösen, wobei je nach Kontext auch ein einzelnes Kriterium ausreichend sein kann.

{% hint style="info" %}
Die Liste der Verarbeitungen, die eine DSFA erfordern, hängt von den Empfehlungen Ihrer nationalen Aufsichtsbehörde ab. Dastra bietet einen DSFA-Leitfaden mit länderspezifischen Empfehlungen, um Ihnen bei der Identifizierung Ihrer Pflichten zu helfen.
{% endhint %}

Dastra zeigt eines der beiden folgenden Ergebnisse an:

* **"Eine DSFA ist nicht erforderlich"** — die Verarbeitung erreicht die Schwelle nicht
* **"Sie müssen eine Datenschutz-Folgenabschätzung (DSFA) durchführen"** — eine Schaltfläche "DSFA erstellen" erscheint, um die Analyse direkt zu starten

## Die DSFA-Vorlagen in Dastra

Mehrere PIA/DSFA-Vorlagen sind in der Dastra-Bibliothek verfügbar, darunter:

* **PIA (CNIL) - Datenschutz-Folgenabschätzung** (57 Fragen): die Standardvorlage der CNIL für eine einzelne Verarbeitung
* **PIA (CNIL) - Datenschutz-Folgenabschätzung (mehrere Verarbeitungen)** (57 Fragen): die CNIL-Vorlage, angepasst für Analysen, die mehrere Verarbeitungen abdecken
* **Privacy impact assessment (PIA)** (114 Fragen): eine umfassende generische PIA-Vorlage
* **EDPB DPIA Template 2026** (82 Fragen): die vom Europäischen Datenschutzausschuss empfohlene Vorlage
* **DPIA Template for AI Systems** (90 Fragen): für Verarbeitungen mit KI-Systemen mit hohem Risiko (DSGVO + KI-Verordnung)
* **DPC DPIA Questionnaire - Irland** (9 Fragen): die Vorlage der irischen Aufsichtsbehörde
* **DPIA Questionnaire (ICO)** (9 Fragen): die Vorlage der britischen Aufsichtsbehörde

Um darauf zuzugreifen, gehen Sie zur Registerkarte "Fragebogenvorlagen", klicken Sie auf **"Vorlage erstellen"** → **"Automatisierte Fragebögen"** und filtern Sie nach dem Typ "Folgenabschätzung".

## Struktur des PIA-Fragebogens (CNIL)

Die PIA-Vorlage (CNIL) ist in drei große Teile gegliedert:

1. **Kontext** — die Verarbeitung beschreiben: allgemeine Informationen, Verarbeitungszwecke, betroffene Daten, Beteiligte (Verantwortlicher, Auftragsverarbeiter, gemeinsam Verantwortliche)
2. **Grundlegende Prinzipien** — die Verhältnismäßigkeit und Datenminimierung bewerten und die Maßnahmen zum Schutz der Rechte der Personen dokumentieren
3. **Risiken im Zusammenhang mit der Datensicherheit** — die Risiken nach vier Bedrohungskategorien bewerten: umgesetzte Sicherheitsmaßnahmen, unrechtmäßiger Zugriff auf Daten, ungewollte Änderung von Daten, Verlust von Daten

{% hint style="info" %}
Der PIA-Fragebogen (CNIL) bietet zwei Antwortmodi: **Vereinfachter Modus** für eine schlankere Erfahrung und **Expertenmodus** für eine detailliertere Analyse. Sie können jederzeit zwischen den beiden Modi wechseln.
{% endhint %}

## Eine DSFA mit einer Verarbeitung verknüpfen

Um die DSFA-Funktionen in Dastra voll auszunutzen, konfigurieren Sie Ihre Vorlage wie folgt:

1. Setzen Sie den **Vorlagentyp** auf "Folgenabschätzung" — dies aktiviert die Risiko-Heatmap im Fragebogen-Dashboard und integriert die Daten der verknüpften Verarbeitung.
2. Wählen Sie im Abschnitt **Bewertetes Element** "Datenverarbeitung" — dies verknüpft jede Antwort mit einer bestimmten Verarbeitung und aktualisiert automatisch das Datum der letzten DSFA bei der Validierung.

{% hint style="info" %}
Sobald die DSFA mit einer Verarbeitung verknüpft ist, können Sie direkt über die Registerkarte **"Folgenabschätzung"** dieser Verarbeitung darauf zugreifen und sie über die Schaltfläche "DSFA erstellen" starten, wenn die Schwelle erreicht ist.
{% endhint %}

## Eine PIA aus dem CNIL-Tool importieren

Wenn Sie bereits eine PIA mit dem dedizierten Tool der CNIL durchgeführt haben, können Sie diese direkt in Dastra importieren:

1. Exportieren Sie Ihre PIA aus dem CNIL-Tool im **.json**-Format
2. Wählen Sie in Dastra die PIA-Vorlage (CNIL) und klicken Sie auf **"Ihre CNIL-PIA importieren"**
3. Ein sehr großer Teil der Elemente wird automatisch in Dastra übernommen

## Eine DSFA für mehrere Verarbeitungen durchführen

Eine einzige DSFA kann mehrere Verarbeitungen abdecken, die in Bezug auf Art, Umfang, Kontext, Verarbeitungszwecke und Risiken ähnlich sind. Verwenden Sie die Vorlage **PIA (CNIL) - mehrere Verarbeitungen** oder konfigurieren Sie Ihre Vorlage so, dass sie **nicht mit einer bestimmten Verarbeitung verknüpft** ist. Sie können dann die DSFA durchführen, exportieren und der Dokumentation der betreffenden Verarbeitungen zuordnen.

## Weiterführende Informationen

{% content-ref url="../types-de-questionnaires/tia.md" %}
[tia.md](../types-de-questionnaires/tia.md)
{% endcontent-ref %}

{% content-ref url="../types-de-questionnaires/lia.md" %}
[lia.md](../types-de-questionnaires/lia.md)
{% endcontent-ref %}
