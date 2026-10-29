---
description: >-
  Erfahren Sie, wie Sie die Antworten auf Fragebögen überwachen und die
  Ergebnisse in Dastra analysieren.
---

# Fragebögen überwachen

## Dashboard der Antworten

Klicken Sie unter **Vorlagen** auf eine Vorlage, um ihr Antwort-Dashboard zu öffnen. Es bietet fünf Ansichten:

* **Antworten**: Liste aller Antworten mit ihrem Status (wartet auf Befragte, gestartet, zur Freigabe vorgelegt, validiert, abgebrochen, Frist überschritten), ihrer Bewertung und dem verknüpften Objekt;
* **Matrix**: Vergleich aller Antworten nebeneinander nach Kategorie und Bewertung, nützlich für ein Benchmarking über Entitäten oder Verarbeitungstätigkeiten hinweg;
* **Statistiken**: aggregierte Statistiken über alle Antworten dieser Vorlage;
* **Details**: Konfiguration und Metadaten der Vorlage;
* **Fragebogen**: der Inhalt der Vorlage, den Sie drucken oder exportieren können.

Um die Antworten aller Vorlagen auf einmal zu verfolgen, öffnen Sie **Alle Fragebögen**.

<figure><img src="../../.gitbook/assets/questionnaires-monitor-1.png" alt="Dashboard einer Vorlage mit ihren Tabs, ihren Statistikkacheln und einer Liste von Antworten, die auf Befragte warten"><figcaption><p>Das Antwort-Dashboard einer Vorlage</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/questionnaire-state-badges.png" alt="Statusbadges der Fragebogenantworten"><figcaption><p>Die Status der Antworten, einschließlich „Abgebrochen“ (rotes Badge)</p></figcaption></figure>

## Auswertung einer einzelnen Antwort

Wenn Sie eine Antwort öffnen, erhalten Sie eine detaillierte Auswertungsansicht:

* **Status**: Fortschritt vom Warten auf die Befragten über „Gestartet“ und „Zur Freigabe vorgelegt“ bis „Validiert“;
* **Bewertung**: Gesamtbewertung aus der maximalen Punktzahl;
* **Abgeschlossen**: Anzahl der beantworteten Fragen im Verhältnis zur Gesamtzahl;
* **Reaktionszeit**: wie lange das Ausfüllen des Fragebogens gedauert hat;
* **Wichtige Punkte**: Antworten, die anhand der Konfiguration der Vorlage automatisch als aufmerksamkeitsbedürftig markiert werden;
* **Analysen-Ergebnisse**: automatische Analyseblöcke, die aus den Antworten erzeugt werden (Compliance-Niveau, Risikobewertung usw.);
* **Bewertungen nach Kategorien**: dargestellt als Radar- oder Balkendiagramm.

Antworten auf Multiple-Choice-Fragen werden verdichtet angezeigt:

* Es werden nur die vom Befragten gewählten Optionen angezeigt;
* der Link **Alle Optionen anzeigen** unter jeder Frage zeigt die nicht gewählten Optionen dieser Frage an, der Link **Optionen ausblenden** kehrt zur verdichteten Anzeige zurück;
* eine unbeantwortete Frage ist mit einem Bindestrich (-) markiert, ohne Liste der Optionen.

<figure><img src="../../.gitbook/assets/audit-questionnaire-response-condensed-view.png" alt="Antworten eines Fragebogens in verdichteter Anzeige"><figcaption><p>Es werden nur die gewählten Optionen angezeigt; die anderen Optionen bleiben Frage für Frage abrufbar</p></figcaption></figure>

## Aktionen für Antworten

Das Menü neben der Hauptschaltfläche der Antwort fasst je nach Status der Antwort und Ihren Berechtigungen die folgenden Aktionen zusammen:

* **Bitte füllen Sie diesen Fragebogen erneut aus.**: erneuert die Antwort, siehe [Einen Fragebogen planen](schedule.md);
* **Fragebogen exportieren**: siehe [Einen Bericht exportieren](export.md);
* **Einladungen versenden**: lädt die Befragten erneut ein, solange die Antwort auf Befragte wartet oder gestartet ist;
* **Den Fragebogen abbrechen**;
* **Bericht teilen**: teilt den Bericht per Link, nur wenn die Antwort validiert ist;
* **Vorlage bearbeiten**;
* **Workflow-Regel**;
* **In den Papierkorb verschieben**: siehe [Einen Fragebogen oder eine Vorlage löschen](delete.md).

### Workflow-Regeln

Antworten auf Fragebögen können Workflow-Regeln auslösen. Die Aktion **Workflow-Regel** im Menü der Antwort listet die Regeln auf, die für Antworten gelten, mit ihrem Status und ihrem Verlauf, und ermöglicht Ihnen mit **Erstellen Sie eine Workflow-Regel**, eine neue Regel anzulegen. Wählen Sie im Regeleditor die Entität **Responding to a questionnaire**. Wie Regeln funktionieren, lesen Sie unter [Workflow-Regeln](../settings/workflow-rules.md).

## KI-Analyse (Beta)

Starten Sie in der Auswertungsansicht einer Antwort eine **KI-Analyse**, um Folgendes zu erhalten:

* eine Gesamtbewertung zu Compliance oder Risiko;
* eine schriftliche Zusammenfassung der wichtigsten Feststellungen;
* eine Aufschlüsselung nach Kriterien (Vollständigkeit, Rechtsgrundlage, Sicherheitsmaßnahmen usw.);
* vorgeschlagene Aufgaben, um die festgestellten Lücken zu schließen.

{% hint style="warning" %}
Die KI-Analyse ist eine Beta-Funktion. Die Ergebnisse sollten mit Vorsicht interpretiert und von einer qualifizierten Fachperson geprüft werden.
{% endhint %}

## Eine Antwort validieren

Klicken Sie nach der Prüfung der Antwort auf **Überprüfen und bestätigen Sie den Fragebogen**, um sie in den Status **Validiert** zu versetzen. Diese Aktion ist den Genehmigern der Antwort vorbehalten. Genehmigung, Überarbeitungsanfragen und endgültige Validierung sind unter [Einen Fragebogen validieren](validate.md) beschrieben.

## Einen Fragebogen abbrechen

Ein Genehmiger kann einen Fragebogen abbrechen, ohne zur Fragebogenliste zurückzukehren. Die Aktion **Den Fragebogen abbrechen** wird angeboten:

* im Validierungsschritt einer Antwort, die zur Freigabe vorgelegt ist, neben **Den Fragebogen bestätigen** und **Überprüfung beantragen**;
* im Menü der Antwort bei jedem Status, solange die Antwort nicht bereits abgebrochen ist oder sich nicht im Papierkorb befindet.

<figure><img src="../../.gitbook/assets/questionnaire-cancel-button.png" alt="Validierungsaktionen einer Antwort: Bestätigen, Überprüfung beantragen, Den Fragebogen abbrechen"><figcaption><p>Die Aktion „Den Fragebogen abbrechen“ wird im Validierungsschritt angeboten</p></figcaption></figure>

Beim Abbrechen wird eine Bestätigung verlangt, und Sie können optional einen Kommentar eingeben. Der eingegebene Grund wird im Verlauf gespeichert und bleibt für den Befragten sichtbar.

Eine abgebrochene Antwort erhält den Status „Abgebrochen“, der in der Liste, in den Filtern, in der Auswertungsansicht und in den Exporten als rotes Badge angezeigt wird. Sie kann vom Befragten nicht mehr bearbeitet werden und fließt nicht in die Ergebnisse ein.

Um einen abgebrochenen Fragebogen fortzusetzen, öffnen Sie ihn und klicken Sie auf **Fragebogen reaktivieren**. Dastra führt Sie zum Bildschirm der Einladungen, um die Befragten erneut einzuladen.

## Antworten in das verknüpfte Objekt übernehmen

Bei Fragebögen, deren Vorlage vom Typ „Erstellung“ ist (Verarbeitungsprojekt, Datenschutzvorfall, Asset, Vertrag, KI-System oder Erfassung von Stakeholdern), können Sie die **erfassten Antworten in ein Dastra-Objekt übernehmen**. Diese Aktion legt das Objekt an oder aktualisiert das verknüpfte Objekt anhand der im Formular eingegebenen Informationen, ohne zusätzliche manuelle Dateneingabe.

Die Schaltfläche erscheint erst, wenn die Antwort validiert ist, und sie ist für die Genehmiger der Antwort aktiv. Wenn die Antwort bereits mit einem Objekt verknüpft ist, heißt sie **Daten zusammenführen** gefolgt vom Objekttyp, zum Beispiel **Daten zusammenführen (Verarbeitungstätigkeit)**. Andernfalls heißt sie **Anlegen (Verarbeitungstätigkeit)**.

Öffnen Sie die validierte Antwort und klicken Sie auf diese Schaltfläche: Ein Bestätigungsfenster listet die Felder auf, die im Zielobjekt aktualisiert werden.

<figure><img src="../../.gitbook/assets/questionnaire-merge-processing-button.png" alt="Auswertungsansicht einer Fragebogenantwort mit der Schaltfläche „Daten zusammenführen (Verarbeitungstätigkeit)“"><figcaption><p>Die Schaltfläche zum Zusammenführen überträgt die Antworten des Fragebogens in das verknüpfte Dastra-Objekt</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/questionnaire-merge-processing-dialog.png" alt="Bestätigung des Zusammenführens mit den Details der Ziel-Verarbeitungstätigkeit"><figcaption><p>Das Zusammenführen bestätigen und die Verarbeitungstätigkeit aus den erfassten Antworten anlegen</p></figcaption></figure>

Diese Funktion ist besonders nützlich für die externe Erfassung über ein Trust Center, bei der Dritte (Lieferanten, Auftragsverarbeiter) Informationen eintragen, die anschließend in Ihren internen Verzeichnissen erscheinen müssen. Siehe [Verarbeitungsprojekte über ein Trust Center erfassen](../trust-center/creation-questionnaires.md).

## Eine Fragebogenvorlage mit KI übersetzen

Die KI kann alle Abschnitte und Fragen einer Vorlage in eine andere Sprache übersetzen. Das Vorgehen ist unter [Einen Fragebogen mit KI übersetzen](translate.md) beschrieben.

## Einen Maßnahmenplan erstellen

Wenn eine Antwort validiert ist, kann ein Genehmiger in der Auswertungsansicht auf **Erstelle einen Aktionsplan** klicken, um anhand der gegebenen Antworten automatisch Aufgaben anzulegen. Die Aufgaben werden entsprechend der Konfiguration der Vorlage vorgeschlagen und dem Aufgabenverwaltungsmodul von Dastra hinzugefügt.
