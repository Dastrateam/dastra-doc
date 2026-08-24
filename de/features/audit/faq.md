# Häufig gestellte Fragen

## Kann ich eine PIA für mehrere Verarbeitungen durchführen?

Eine Datenschutz-Folgenabschätzung kann sich auf eine Verarbeitung oder eine Reihe ähnlicher Verarbeitungen beziehen. **Eine einzige DSFA kann zur Bewertung mehrerer ähnlicher Verarbeitungsvorgänge in Bezug auf Art, Umfang, Kontext, Verarbeitungszwecke und Risiken verwendet werden.**

Beispielsweise:

* Kommunen, die jeweils ein ähnliches Videoüberwachungssystem einrichten, könnten eine einzige Analyse durchführen, die dieses System betrifft, auch wenn es später von verschiedenen Verantwortlichen umgesetzt wird;
* ein Eisenbahnunternehmen (einzelner Verantwortlicher) könnte eine einzige Folgenabschätzung für die Videoüberwachung durchführen, die in mehreren Bahnhöfen eingesetzt wird.

In Dastra ist die Standard-PIA-Vorlage an eine einzelne Verarbeitung gebunden. **Es ist möglich, die Vorlage so zu ändern, dass die PIA nicht an eine Verarbeitung gebunden ist**. In diesem Fall können Sie die PIA durchführen, exportieren und in die Dokumentation der betreffenden Verarbeitungen aufnehmen.

## Kann man bei der Erstellung eines Fragebogens automatisch eine E-Mail-Vorlage einrichten?

Sie können eine E-Mail-Vorlage erstellen, die in den Einladungen zu Fragebögen verwendet werden kann. Es ist nicht möglich, automatisierte Aktionen beispielsweise über Workflows durchzuführen. Fragebögen können nämlich nicht als auslösende Elemente verwendet werden.

## Kann ich als externer Befragter Bilder in die Antworten einfügen?

Nein, das ist nicht möglich. Diese Möglichkeit steht Ihnen zur Verfügung, wenn Sie ein interner Befragter (Nutzer von Dastra) sind.

## Ist es möglich, automatisch eine Aufgabe aus der Antwort eines Fragebogens vorzuschlagen?

Ja, das ist möglich über den Fragetyp "Langer Text", indem Sie das Kontrollkästchen "Automatisch Aufgabe(n) aus der Antwort vorschlagen" aktivieren.

## Ist es möglich, eine Fragebogenvorlage für alle Dastra-Nutzer zu veröffentlichen?

Ja, das ist möglich über die Fragebogenvorlage, indem Sie auf "Beitragen" klicken:<br>

<div align="left"><figure><img src="../../.gitbook/assets/screenshot-2024-07-26-120545.png" alt=""><figcaption></figcaption></figure></div>

## Was bedeuten die Farben in den Fragebogenantworten?

In den Abschnitten des Fragebogens sind den Fragensymbolen Farben zugeordnet.

Hier ist die Farbzuordnung:

| Farbe                    | Bild                                                                          | Beschreibung                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Grau mit rotem Rand      | ![](<../../.gitbook/assets/image-385.png>)                                  | Pflichtfrage nicht beantwortet                                                                |
| Schwarz mit rotem Rand   | ![](<../../.gitbook/assets/image-386.png>)                                  | Pflichtfrage beantwortet                                                                      |
| Grau                     | ![](<../../.gitbook/assets/image-388.png>)                                  | Optionale Frage nicht beantwortet                                                             |
| Grün                     | ![](<../../.gitbook/assets/image-389.png>)                                  | Alle Fragen des Abschnitts haben eine Antwort. Optionale Frage beantwortet                   |
| Grün mit rotem Rand      | <img src="../../.gitbook/assets/image-391.png" alt="" data-size="original"> | Alle Fragen des Abschnitts haben eine Antwort. Pflichtfrage beantwortet                      |
| Schwarz                  | <img src="../../.gitbook/assets/image-390.png" alt="" data-size="original"> | Optionale Frage beantwortet. Es gibt noch unbeantwortete Fragen im Abschnitt.                |

### Was tun bei der Fehlermeldung "Error: there is a duplicate slug for the following questions" beim Speichern eines Fragebogens? <a href="#slug-error" id="slug-error"></a>

<figure><img src="../../.gitbook/assets/screenshot-2024-11-04-170330.png" alt=""><figcaption></figcaption></figure>

\
Diese Meldung weist darauf hin, dass eine oder mehrere Fragen im Fragebogen exakt denselben "Variablennamen" tragen, was den Fehler verursacht.

<div align="left"><figure><img src="../../.gitbook/assets/screenshot-2024-11-04-163831.png" alt=""><figcaption></figcaption></figure></div>

Die Fragen mit demselben "Variablennamen" sind durch die Fehlermeldung "Der Variablenname ist in einer anderen Frage vorhanden" identifizierbar, die über ihnen angezeigt wird.

<div align="left"><figure><img src="../../.gitbook/assets/screenshot-2024-11-04-164534.png" alt=""><figcaption></figcaption></figure></div>

Um dieses Problem zu lösen, müssen Sie den "Variablennamen" jeder Frage mit demselben "Variablennamen" so ändern, dass er für jede Frage eindeutig ist, beispielsweise indem Sie am Ende jedes "Variablennamens" ein \_ und eine aufsteigende Nummer hinzufügen.

<figure><img src="../../.gitbook/assets/screenshot-2024-11-04-165757.png" alt=""><figcaption></figcaption></figure>

Sobald der Fragebogen keine doppelten "Variablennamen" mehr enthält, kann er normal gespeichert werden.<br>

### Was tun bei der Meldung "Blockiert wegen zu vieler Einladungen" beim Versand von E-Mail-Einladungen an die Befragten des Fragebogens?

<figure><img src="../../.gitbook/assets/screenshot-2026-02-05-091717.png" alt=""><figcaption></figcaption></figure>

\
Diese Meldung erscheint, wenn bereits 5 E-Mail-Einladungen an einen Befragten aus demselben Fragebogen gesendet wurden.\
\
Wenn diese Meldung erscheint, können Sie den Befragten weiterhin einladen, indem Sie ihm den Einladungslink zum Fragebogen übermitteln, der hier verfügbar ist:

<figure><img src="../../.gitbook/assets/screenshot-2026-02-05-092802.png" alt=""><figcaption></figcaption></figure>

### Was tun, wenn ich den "Fragebogen prüfen und validieren" nicht kann, obwohl ich Verantwortlicher bin?

Dies kann vorkommen, wenn der Befragte seinen Fragebogen noch nicht abgeschlossen hat, indem er nach der Beantwortung auf die Schaltfläche "Abschließen" klickt.\
\
In diesem Fall haben Sie als Verantwortlicher die Möglichkeit, den Stand des Fragebogens auf der Seite des Befragten zu überprüfen, indem Sie den Zugangslink des Befragten verwenden, der hier verfügbar ist:

<figure><img src="../../.gitbook/assets/screenshot-2026-02-24-164321.png" alt=""><figcaption></figcaption></figure>
