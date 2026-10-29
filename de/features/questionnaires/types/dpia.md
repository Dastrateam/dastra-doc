---
description: >-
  Erfahren Sie, wie Sie mit Dastra eine Datenschutz-Folgenabschätzung (DSFA
  oder PIA) durchführen.
---

# DSFA / PIA

## Die DSFA / PIA im Überblick

Eine Datenschutz-Folgenabschätzung (DSFA), im Englischen auch Privacy Impact Assessment (PIA) genannt, ist ein Verfahren, das nach Artikel 35 der DSGVO erforderlich ist, wenn eine Verarbeitungstätigkeit voraussichtlich ein hohes Risiko für die Rechte und Freiheiten natürlicher Personen zur Folge hat.

Eine DSFA muss durchgeführt werden, bevor eine Verarbeitungstätigkeit mit solchen Risiken beginnt, und überprüft werden, sobald sich die Art der Verarbeitung wesentlich ändert.

## Prüfen, ob eine DSFA erforderlich ist

In Dastra hilft Ihnen der Tab **Folgenabschätzung** jeder Verarbeitungstätigkeit festzustellen, ob eine DSFA erforderlich ist. Er bewertet 9 Risikokriterien, die der Europäische Datenschutzausschuss (EDSA) festgelegt hat:

* Bewertung oder Scoring, einschließlich Profiling und Prognosen
* Automatisierte Entscheidungsfindung mit erheblichen Auswirkungen
* Systematische Überwachung
* Sensible personenbezogene Daten
* Datenverarbeitung in großem Umfang
* Abgleichen oder Zusammenführen von Datensätzen
* Daten zu schutzbedürftigen Personen
* Innovative Nutzung oder Anwendung neuer Technologien
* Verarbeitung, die betroffene Personen an der Ausübung ihrer Rechte hindert

Wählen Sie für jedes Kriterium **Ja**, **Nein** oder **Nicht zutreffend**. Zwei Antworten mit **Ja** genügen in der Regel, um eine DSFA-Pflicht auszulösen, wobei je nach Kontext auch ein einzelnes Kriterium ausreichen kann.

Um Zeit zu sparen, klicken Sie neben dem Titel **Bewertung der 9 Kriterien der AIPD (EDSB)** auf **Bewertung erstellen**: Der KI-Assistent schlägt für jedes Kriterium eine Antwort mit Begründung vor, auf Grundlage der Informationen, die bereits in der Verarbeitungstätigkeit erfasst sind. Sie prüfen den Vorschlag, bevor Sie ihn auf das Formular anwenden, und jede Antwort bleibt bearbeitbar. Das genaue Vorgehen finden Sie auf der Seite [Datenschutz-Folgenabschätzung](../../ropa/activity/impact-analysis.md).

{% hint style="info" %}
Welche Verarbeitungstätigkeiten eine DSFA erfordern, hängt von den Empfehlungen Ihrer nationalen Aufsichtsbehörde ab. Dastra stellt einen DSFA-Leitfaden mit länderspezifischen Empfehlungen bereit, der Ihnen hilft, Ihre Pflichten zu erkennen.
{% endhint %}

Dastra zeigt eines von zwei Ergebnissen an:

* **Die DSFA ist nicht obligatorisch.** Die Verarbeitungstätigkeit erreicht den Schwellenwert nicht
* Eine DSFA ist erforderlich: Es erscheint die Schaltfläche **Erstellen Sie eine DSFA**, mit der Sie die Bewertung direkt starten

## DSFA- und PIA-Vorlagen in Dastra

In der Dastra-Bibliothek sind mehrere PIA- und DSFA-Vorlagen verfügbar, darunter:

* **PIA (CNIL) - Privacy Impact Analysis** (57 Fragen): das Standard-PIA-Modell der französischen Datenschutzbehörde, für eine einzelne Verarbeitungstätigkeit
* **PIA (CNIL) - Privacy Impact Analysis (multi-processing)** (57 Fragen): das CNIL-Modell, angepasst für Bewertungen, die mehrere Verarbeitungstätigkeiten abdecken
* **Privacy impact assessment (PIA)** (114 Fragen): eine vollständige generische PIA-Vorlage
* **EDPB DPIA Template 2026** (82 Fragen): die vom Europäischen Datenschutzausschuss empfohlene Vorlage
* **DPIA Template for AI Systems** (90 Fragen): für Verarbeitungstätigkeiten mit Hochrisiko-KI-Systemen (DSGVO + EU-KI-Verordnung)
* **DPC DPIA Questionnaire - Ireland** (9 Fragen): die Vorlage der irischen Datenschutzbehörde
* **DPIA Questionnaire (ICO)** (9 Fragen): die Vorlage der britischen Datenschutzbehörde
* **US PIA (cross-state)** (86 Fragen): für Verarbeitungstätigkeiten in den USA

Um auf diese Vorlagen zuzugreifen, öffnen Sie **Fragebögen** > **Vorlagen**, klicken Sie auf **Vorlage erstellen** und dann auf **Basierend auf einer Vorlage** und filtern Sie mit **Typen** auf **DSFA (PIA)**.

## Aufbau des Fragebogens PIA (CNIL)

Die Vorlage PIA (CNIL) ist in drei Hauptteile gegliedert:

1. **Kontext**: Beschreiben Sie die Verarbeitungstätigkeit: allgemeine Angaben, Zweck, betroffene Daten, Beteiligte (Verantwortlicher, Auftragsverarbeiter, gemeinsam Verantwortliche)
2. **Grundlegende Prinzipien**: Bewerten Sie die Verhältnismäßigkeit und die Erforderlichkeit der Daten und dokumentieren Sie die Maßnahmen zum Schutz der Rechte der Personen
3. **Risiken im Zusammenhang mit der Datensicherheit**: Bewerten Sie die Risiken in vier Bedrohungskategorien: umgesetzte Sicherheitsmaßnahmen, unrechtmäßiger Zugriff auf Daten, unerwünschte Veränderung von Daten und Verlust von Daten

{% hint style="info" %}
Der Fragebogen PIA (CNIL) bietet zwei Antwortmodi. Der Unterschied zwischen den beiden Modi besteht allein in der Sichtbarkeit zusätzlicher Felder pro Frage: Im erweiterten Modus werden für jede Frage die Felder **Begründung der Antwort**, **Anhänge** und **Anmerkungen** angezeigt. Im einfachen Modus sind diese Felder ausgeblendet. Sie können jederzeit zwischen den Modi wechseln.
{% endhint %}

## Eine DSFA mit einer Verarbeitungstätigkeit verknüpfen

Um die DSFA-Funktionen in Dastra optimal zu nutzen, konfigurieren Sie Ihre DSFA-Vorlage wie folgt:

1. Stellen Sie die **Art des Fragebogens** auf **DSFA (PIA)**: Dadurch wird die Risiko-Heatmap im Dashboard des Fragebogens aktiviert und die Daten der verknüpften Verarbeitungstätigkeit werden einbezogen.
2. Wählen Sie unter **Verwandtes Thema** die Verarbeitungstätigkeit: Dadurch wird jede DSFA-Antwort mit einer bestimmten Verarbeitungstätigkeit verknüpft, und das **Datum der letzten DSFA** der Verarbeitungstätigkeit wird automatisch aktualisiert, wenn die DSFA veröffentlicht wird (siehe „Das Datum der letzten DSFA aktualisieren“ weiter unten).

{% hint style="info" %}
Sobald eine DSFA mit einer Verarbeitungstätigkeit verknüpft ist, können Sie sie direkt im Schritt **Folgenabschätzung** dieser Verarbeitungstätigkeit aufrufen und mit der Schaltfläche **Erstellen Sie eine DSFA** starten, wenn der Schwellenwert erreicht ist.
{% endhint %}

### Das Datum der letzten DSFA aktualisieren

Wenn eine mit einer Verarbeitungstätigkeit verknüpfte DSFA veröffentlicht wird, kopiert Dastra ihr Veröffentlichungsdatum in das Feld **Datum der letzten DSFA** im Schritt **Folgenabschätzung** der Verarbeitungstätigkeit. Diese Aktualisierung gilt unabhängig vom Ursprung der DSFA (aus der Verarbeitungstätigkeit gestartet oder aus dem Modul Fragebögen geplant), sofern der Vorlagentyp **DSFA (PIA)** ist und das verwandte Objekt eine Verarbeitungstätigkeit.

Die Veröffentlichung erfolgt:

* wenn der letzte erforderliche Befragte den Fragebogen abschließt, falls der Validierungsschritt deaktiviert ist;
* wenn die Prüfer den Fragebogen validieren, in allen anderen Fällen.

Ein Informationshinweis weist bei der Veröffentlichung darauf hin:

* im Fenster **Den Fragebogen abschließen**: „Das Datum der letzten DSFA für die zugehörige Verarbeitung wird aktualisiert.“ oder, wenn eine Validierung erwartet wird, „Das Datum der letzten DSFA für die zugehörige Verarbeitung wird bei der Validierung dieses Fragebogens aktualisiert.“;
* im Validierungsfenster des Fragebogens: „Das Datum der letzten DSFA für die zugehörige Verarbeitung wird aktualisiert.“

Wenn die Verarbeitungstätigkeit eine DSFA erfordert, zeigt der Schritt **Folgenabschätzung** anschließend die Meldung „Eine DSFA wurde durchgeführt.“ an.

{% hint style="info" %}
Das Veröffentlichungsdatum überschreibt jeden Wert, der bereits im Feld **Datum der letzten DSFA** eingetragen ist.
{% endhint %}

## Eine DSFA aus dem CNIL-Tool importieren

Wenn Sie bereits eine DSFA mit dem speziellen Tool der CNIL durchgeführt haben, können Sie sie direkt in Dastra importieren:

1. Exportieren Sie Ihre DSFA aus dem CNIL-Tool im Format **.json**.
2. Öffnen Sie in Dastra unter **Vorlagen** die Vorlage PIA (CNIL), klicken Sie auf den Pfeil neben **Fragebogen planen** und dann auf **DSFA aus dem DSFA-Tool (CNIL) importieren**. Diese Aktion wird nur für eine Vorlage vom Typ **DSFA (PIA)** angeboten.
3. Wählen Sie die **Organisationseinheit** und unter **Bitte wähle die mit dieser DSFA verbundene Verarbeitung aus** die Verarbeitungstätigkeit und legen Sie dann die .json-Datei ab.
4. Ein großer Teil der Elemente wird automatisch in Dastra importiert.

## Eine DSFA für mehrere Verarbeitungstätigkeiten durchführen

Eine einzelne DSFA kann mehrere Verarbeitungstätigkeiten abdecken, die sich in Art, Umfang, Kontext, Zwecken und Risiken ähneln. Verwenden Sie die Vorlage **PIA (CNIL) - Privacy Impact Analysis (multi-processing)** oder konfigurieren Sie Ihre Vorlage so, dass sie **nicht mit einer bestimmten Verarbeitungstätigkeit verknüpft** ist. Sie können die DSFA dann durchführen, exportieren und der Dokumentation der betreffenden Verarbeitungstätigkeiten beifügen.

## Weiterführende Informationen

{% content-ref url="tia.md" %}
[Transferfolgenabschätzung (TIA)](tia.md)
{% endcontent-ref %}

{% content-ref url="lia.md" %}
[Interessenabwägung (LIA)](lia.md)
{% endcontent-ref %}
