---
description: >-
  Der Validierungsprozess eines Fragebogens in Dastra: Genehmigungen der Prüfer,
  endgültige Validierung, Korrekturanforderung und Abbruch.
---

# Einen Fragebogen validieren

Die Validierung ist der Prüfschritt, der auf die Finalisierung eines Fragebogens durch die Befragten folgt. Die benannten Prüfer kontrollieren dabei jede Antwort, fordern bei Bedarf Korrekturen an und genehmigen und veröffentlichen anschließend den Fragebogen.

## Lebenszyklus einer Antwort

1. **Warten auf Befragte / Gestartet** — die Befragten füllen das Formular aus.
2. **Warten auf Validierung** — sobald alle **erforderlichen** Befragten auf **Finalisieren** geklickt haben, wechselt die Antwort in diesen Status und die Prüfer werden benachrichtigt.
3. **Validiert** — nachdem alle erforderlichen Prüfer genehmigt haben und die endgültige Validierung erfolgt ist.

Aus dem Status „Warten auf Validierung“ sind drei Ausgänge möglich: **validieren**, **eine Überprüfung anfordern** (Zurücksenden an die Befragten) oder den Fragebogen **abbrechen**.

{% hint style="info" %}
Wenn keine Schaltfläche verfügbar ist, prüfen Sie, ob die Antwort tatsächlich den Status „Warten auf Validierung“ hat. In allen anderen Status sind die Validierungsaktionen gesperrt.
{% endhint %}

## Wer validiert?

Die Prüfer werden bei der Planung des Fragebogens festgelegt (siehe [Einen Fragebogen planen](planifier-un-audit.md)), im Abschnitt **Verantwortliche**:

* **Erforderliche Prüfer** — alle müssen den Fragebogen genehmigen, bevor er validiert werden kann. Mindestens ein erforderlicher Prüfer ist Pflicht.
* **Optionale Prüfer** — aktivieren Sie die Option für optionale Prüfer, um Personen einzubeziehen, deren Genehmigung nachverfolgt wird, aber **nicht blockierend** ist.

Nur diese Nutzer können genehmigen, validieren, eine Überprüfung anfordern oder die Antwort abbrechen.

{% hint style="success" %}
Sie können diesen Schritt bei der Planung vollständig deaktivieren (Option „Schritt zur Korrektur deaktivieren“). Die Antwort wird dann direkt mit der Finalisierung durch die Befragten veröffentlicht.
{% endhint %}

## Der Prüfbildschirm

Klicken Sie in der Antwort auf **„Überprüfen und bestätigen Sie den Fragebogen“**. Der Prüfbildschirm entspricht dem Aufbau des Fragebogens: Abschnittsnavigation links, Fragen und Antworten in der Mitte, Validierungsaktionen rechts.

### Jede Antwort bewerten

Jede Frage kann einen Bewertungsstatus erhalten:

* **Kein Status** — die Frage wurde nicht bewertet (Standard, nicht blockierend)
* **Validiert** — die Antwort wird akzeptiert
* **Korrekturen erforderlich** — die Antwort muss ergänzt oder korrigiert werden
* **Abgelehnt** — die Antwort wird zurückgewiesen

Ein Selektor am Anfang jedes Abschnitts weist allen angezeigten Fragen in einem Schritt denselben Status zu.

Zu jeder Frage können Sie zusätzlich:

* **Eine Anmerkung hinzufügen** — interner Austausch mit den Befragten und den anderen Prüfern
* **Eine Aufgabe hinzufügen** — fließt direkt in den Aktionsplan ein
* **Die Begründung ergänzen** und **einen Anhang hinzufügen**
* **Ein Risiko qualifizieren**, wenn die Frage mit einem Risiko verknüpft ist

{% hint style="warning" %}
Ist mindestens eine Frage als „Korrekturen erforderlich“ oder „Abgelehnt“ markiert, sind Genehmigung und Validierung gesperrt: Nutzen Sie **„Überprüfung beantragen“**, um den Fragebogen an die Befragten zurückzusenden.
{% endhint %}

## Den Fragebogen genehmigen

Jeder Prüfer erteilt seine Genehmigung einzeln über die Schaltfläche „Fragebogen genehmigen“:

* Sie können **Prüfkommentare** erfassen: Sie werden gespeichert und **im Berichtsexport übernommen**.
* Eine **E-Mail-Benachrichtigung** wird an die Prüfer gesendet, die noch nicht genehmigt haben.

Das Panel der **erforderlichen Genehmigungen (n/Gesamt)** fasst den Status jedes Prüfers zusammen (genehmigt, mit Datum, oder ausstehend) sowie, falls vorhanden, einen separaten Block für die optionalen Genehmigungen. Die Prüfkommentare der einzelnen Prüfer sind dort einsehbar.

Zwei ergänzende Aktionen:

* **Meine Genehmigung widerrufen** — nimmt Ihre Genehmigung zurück, solange der Fragebogen nicht validiert ist.
* Sind Sie der **letzte erforderliche Prüfer**, schlägt Dastra unmittelbar vor, direkt mit Validierung und Veröffentlichung fortzufahren.

{% hint style="info" %}
Die Beschriftungen der neuen Genehmigungsfunktionen sind derzeit noch nicht ins Deutsche übersetzt und erscheinen in der Oberfläche auf Englisch („Approve questionnaire“, „Required approvals“, „Revoke my approval“).
{% endhint %}

## Validieren und veröffentlichen

Die Schaltfläche **„Den Fragebogen bestätigen“** ist erst aktiv, wenn **alle erforderlichen Prüfer genehmigt haben** und keine Frage zur Korrektur markiert ist. Das Validierungsfenster zeigt:

* die Anzahl der validierten Fragen im Verhältnis zur Gesamtzahl;
* den Stand der Genehmigungen;
* bei einer **DSFA / PIA** die Option, das **Datum der Folgenabschätzung auf die verknüpfte Verarbeitung zu übertragen**;
* die Option, eine **Benachrichtigung** an die Beteiligten zu senden.

Die Antwort erhält anschließend den Status **„Validiert“** mit ihrem Veröffentlichungsdatum, und Sie werden zu ihrem Bericht weitergeleitet. Danach können Sie [den Bericht exportieren](exporter-un-rapport.md), einen Aktionsplan erzeugen oder die Antworten mit dem verknüpften Objekt zusammenführen (siehe [Fragebögen steuern](piloter-les-questionnaires.md)).

## Eine Überprüfung anfordern

Die Aktion **„Überprüfung beantragen“** sendet den Fragebogen an die Befragten zurück:

* die Antwort wechselt zurück auf „In Bearbeitung“ und eine **neue Frist** wird anhand der Frist der Vorlage berechnet (standardmäßig 30 Tage);
* **alle bereits erteilten Genehmigungen werden zurückgesetzt**;
* eine **Korrekturrunde** wird in der Historie der Antwort erfasst;
* jeder Befragte wird benachrichtigt, zusammen mit Ihrer Prüfnachricht — die Sie frei formulieren oder aus einer E-Mail-Vorlage vorbefüllen können.

Sobald die Befragten erneut finalisieren, beginnt der Validierungszyklus von vorn.

## Den Fragebogen abbrechen

Die Aktion zum Abbrechen des Fragebogens beendet den Zyklus ohne Veröffentlichung. Ein optionaler Kommentar erläutert den Grund; er bleibt in der Historie erhalten und ist für die Befragten sichtbar. Die Genehmigungen werden zurückgesetzt und die Antwort erhält den Status **„Abgebrochen“**: Sie ist nicht mehr bearbeitbar und wird nicht in die Ergebnisse einbezogen.

## Zu validierende Fragebögen nachverfolgen

Fragebögen, die auf Ihre Genehmigung warten, sind in Ihren Fragebögen unter „Warten auf meine Bestätigung“ zusammengefasst und in den Listen sowie im Reporting mit dem Kennzeichen „Warten auf Validierung“ versehen.
