---
description: >-
  Wählen Sie mehrere Elemente aus, wenden Sie Aktionen gleichzeitig auf sie an,
  wählen Sie die Spalten einer Liste und nutzen Sie den Papierkorb, in jedem
  Dastra-Modul.
---

# Listen, Sammelaktionen und Papierkorb

Die Listen von Dastra (Verarbeitungstätigkeiten, Assets, Anfragen, Aufgaben, Verträge und weitere) verhalten sich gleich. Diese Seite beschreibt, wie Sie mehrere Elemente auswählen, Aktionen gleichzeitig auf sie anwenden, die Spalten wählen und den Papierkorb nutzen. Zum Sortieren und Filtern einer Liste siehe [Erweiterte Filter](filters.md).

## Elemente auswählen

Aktivieren Sie das Kästchen am Anfang jeder Zeile oder das Kästchen der Kopfzeile, um **Alle Elemente der Seite auswählen**. Eine Leiste zeigt dann die Anzahl der ausgewählten Elemente.

Enthält die Liste mehr Ergebnisse als die Seite, wählt die Schaltfläche **Alle auswählen** mit der Gesamtzahl in Klammern jedes Ergebnis der aktuellen Suche und der Filter aus, auch die nicht angezeigten Zeilen. Klicken Sie auf **Abwählen**, um die Auswahl aufzuheben.

## Aktionen auf mehrere Elemente anwenden

Sind Elemente ausgewählt, öffnen Sie **Bitte wählen Sie eine Sammelaktion aus** über der Liste oder klicken Sie mit der rechten Maustaste auf eine ausgewählte Zeile. Die Aktionen hängen vom Modul, von Ihren Berechtigungen und von den Funktionen Ihres Tarifs ab. Die häufigsten sind:

<figure><img src="../../.gitbook/assets/general-lists-1.png" alt="Die Liste der Verarbeitungstätigkeiten mit drei ausgewählten Zeilen und geöffnetem Menü der Sammelaktionen"><figcaption><p>Drei ausgewählte Zeilen und das Menü Bitte wählen Sie eine Sammelaktion aus</p></figcaption></figure>

* **Felder bearbeiten**: ändert den Wert eines oder mehrerer Felder bei allen ausgewählten Elementen. Es öffnet sich ein Fenster mit dem Titel **Batch edit** gefolgt von der Anzahl der Elemente. Angeboten werden nur die Felder, die sich gesammelt bearbeiten lassen.
* **Prozessschritt umschalten**: verschiebt alle ausgewählten Elemente in einen anderen Workflow-Schritt, in den Modulen, die Workflow-Schritte verwenden.
* **Exportieren**: exportiert die ausgewählten Elemente.
* **In den Papierkorb verschieben**: siehe [Papierkorb](#papierkorb).

Die vollständige Liste der Aktionen eines Moduls finden Sie auf seiner eigenen Seite, zum Beispiel [Aktionen auf mehrere Verarbeitungstätigkeiten gleichzeitig anwenden](../ropa/README.md#aktionen-auf-mehrere-verarbeitungstatigkeiten-gleichzeitig-anwenden). Ist die Auswahl groß, verarbeitet Dastra sie im Hintergrund und zeigt **Die Verarbeitung der Massen hat begonnen**: Die Listen werden aktualisiert, sobald die Verarbeitung abgeschlossen ist.

## Die Spalten wählen

Klicken Sie in der Kopfzeile der Liste auf **Spalten anpassen**, um Spalten ein- und auszublenden und neu anzuordnen, und speichern Sie das Ergebnis dann in einer benutzerdefinierten Ansicht. Siehe [Spalten anpassen](filters.md#spalten-anpassen) auf der Seite zu den erweiterten Filtern.

## Papierkorb

In jedem Modul wird ein gelöschtes Element zuerst in den Papierkorb verschoben.

1. Wählen Sie das Element oder die Elemente aus und wählen Sie dann **In den Papierkorb verschieben**.
2. Bestätigen Sie. Elemente im Papierkorb erscheinen nicht mehr in den Listen, sind aber nicht endgültig gelöscht.
3. Um sie zu finden, aktivieren Sie **Papierkorb anzeigen** oder **Papierkorb einbeziehen**, je nach Liste.
4. Öffnen Sie das Menü eines Elements im Papierkorb: **Wiederherstellen** setzt es zurück in die Listen, **Dauerhaft löschen** löscht es.

{% hint style="warning" %}
**Dauerhaft löschen** lässt sich nicht rückgängig machen.
{% endhint %}

Löschregeln, sofern ein Modul welche hat, löschen die Elemente des Papierkorbs automatisch: Siehe [Löschregeln für Anfragen](../requests/advanced/purge.md) für Anfragen betroffener Personen.
