---
description: >-
  Antworten auf häufige Fragen zum Risikomanagement-Modul: Menü, Status,
  aktuelles Risiko, Risikoskala und Stapelerstellung.
---

# Häufig gestellte Fragen

## Warum wird das Menü Risikomanagement nicht angezeigt?

Das Modul muss für Ihren Mandanten aktiviert sein, und Ihre Rolle muss den Lesezugriff auf Risiken enthalten. Zum Erstellen oder Bearbeiten eines Risikos ist Schreibzugriff erforderlich. Wenden Sie sich an den Administrator Ihres Mandanten.

## Warum kann ich ein Risiko nicht in den nächsten Schritt verschieben?

Nur der Inhaber eines Risikos kann seinen Status ändern: die Bewertung bestätigen, die Antwort bestätigen, es archivieren oder zu einem vorherigen Schritt zurückkehren. Der Name des Inhabers wird im Abschnitt **Identifizierung** des Risikos angezeigt. Um das Risiko an eine andere Person zu übergeben, ändern Sie den **Inhaber des Risikos** in diesem Abschnitt.

## Was ist der Unterschied zwischen anfänglichem, Rest- und aktuellem Risiko?

Das anfängliche Risiko ist das Risiko vor jeder Kontrollmaßnahme. Das Restrisiko ist dasjenige, das Sie anstreben, sobald die Maßnahmen umgesetzt sind. Das aktuelle Risiko liegt je nach Behebungsrate Ihrer Kontrollpunkte zwischen den beiden. Die Formeln finden Sie im [Glossar](glossary.md).

## Warum ändert sich mein aktuelles Risiko trotz meiner Kontrollpunkte nicht?

Prüfen Sie Folgendes:

* Der Antworttyp ist **Reduzierung und Kontrollen**: Die anderen Optionen berechnen keine Behebungsrate;
* das Risiko hat eine anfängliche und eine Reststufe;
* Kontrollpunkte sind dem Risikotyp zugewiesen und haben eine Antwort erhalten. Ein Kontrollpunkt ohne Antwort zählt null Punkte;
* die Antworten lauten nicht alle **Nicht zutreffend**: Diese Antworten werden von der Berechnung ausgeschlossen.

## Was passiert, wenn ich die Risikoskala ändere?

Das Aktivieren einer anderen Skala ändert die Statistiken aller Risiken des Mandanten, und Dastra bittet vorher um eine Bestätigung. Wählen Sie Ihre Skala, bevor Sie Ihre ersten Risiken erfassen. Siehe [Die Risikoskala konfigurieren](process/assess.md#die-risikoskala-konfigurieren).

## Wie bewerte ich dasselbe Risiko für mehrere Verarbeitungstätigkeiten oder Assets?

Verwenden Sie **Erzeugung von Massenrisiken**: Wählen Sie den Risikotyp und alle betroffenen Objekte aus, und Dastra erstellt pro Objekt ein Risiko. Siehe [Risikomanagement](README.md).
