---
description: >-
  Pflegen Sie die Kategorien betroffener Personen, kennzeichnen Sie
  schutzbedürftige Personen und sehen Sie die mit jeder Kategorie verknüpften
  Datenkategorien ein oder importieren Sie sie.
---

# Betroffenenkategorien

Eine Betroffenenkategorie fasst Personen zusammen, deren Daten Sie verarbeiten: Beschäftigte, Kunden, Bewerber, Minderjährige und so weiter. Im Menü heißt diese Referenzliste **Betroffenenkategorie**.

Legen Sie jede Kategorie einmal hier an und wählen Sie sie dann in Ihren Datenkategorien, Verarbeitungstätigkeiten, Datenschutzverletzungen und Anfragen aus, damit Ihre Berichte überall dieselben Personengruppen zählen.

## Eine Kategorie hinzufügen

Öffnen Sie **Metadaten** > **Betroffenenkategorie**. Sie haben folgende Möglichkeiten:

* Klicken Sie auf **Personengruppe hinzufügen**, um ein leeres Formular zu öffnen;
* klicken Sie auf den Pfeil neben dieser Schaltfläche und dann auf **Erstellen Sie auf der Grundlage von Vorlagen**, um Kategorien der Bibliothek zu kopieren;
* importieren Sie Kategorien aus einer Datei: Pfeil neben der Schaltfläche und dann **Importieren**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-subject-categories-1.png" alt="Liste der Betroffenenkategorien mit angezeigter Spalte Datensätze"><figcaption><p>Die Liste der Kategorien mit der Spalte Datensätze</p></figcaption></figure>

## Das Formular der Kategorie ausfüllen

| Feld | Inhalt |
| --- | --- |
| **Bezeichnung** | Der Name der Kategorie, erforderlich. |
| **Zusammenfassung** | Eine freie Beschreibung. |
| **Betroffene schutzbedürftige Personen** | Aktivieren Sie die Option, wenn die Kategorie Personen in einer ungleichen Situation zusammenfasst, etwa Minderjährige, Beschäftigte oder ältere Menschen. |

Die Symbolleiste des Formulars gibt je nach Ihren Berechtigungen und den aktivierten Funktionen Zugriff auf die Aufgaben und KI-Systeme, die mit der Kategorie verknüpft sind. Sie enthält außerdem die Verarbeitungstätigkeiten, die die Kategorie verwenden, die Datenkategorien der Kategorie (siehe unten), den Aktivitätsverlauf und, wenn Workflow-Schritte definiert sind, den Workflow-Schritt.

Das Aktionsmenü des Formulars bietet **Zusammenführen** und **Löschen**. Für Kategorien gibt es kein **Datenqualitätswerkzeug**.

## Datenkategorien einer Kategorie

Eine Datenkategorie kann sich auf mehrere Betroffenenkategorien beziehen und eine Betroffenenkategorie auf mehrere Datenkategorien. Diese Verknüpfung hilft Ihnen, für eine bestimmte Personengruppe zu finden, welche Daten Sie halten, zum Beispiel bei einer [Anfrage einer betroffenen Person](../../requests/README.md).

* Um die Datenkategorien einer Kategorie zu sehen, öffnen Sie ihr Formular: Die Schaltfläche mit der Anzahl der Datenkategorien listet sie auf. Klicken Sie auf eine Datenkategorie, um sie zu öffnen. Aktivieren Sie in der Liste der Kategorien unter **Spalten anpassen** die Spalte **Datensätze**: Sie können die Liste auch nach Datenkategorie filtern.
* Um eine Datenkategorie zu verknüpfen oder die Verknüpfung zu lösen, öffnen Sie die Datenkategorie und fügen Sie die Kategorie in ihrem Feld **Kategorien betroffener Personen** hinzu oder entfernen Sie sie. Siehe [Datenkategorien](datasets.md). Die Liste der Datenkategorien lässt sich auch nach **Betroffenenkategorie** filtern.
* Um die Verknüpfungen zu importieren, verwenden Sie die Spalte **Datensätze** der Importdatei der Kategorien. Sie enthält die Namen oder Kennungen von Datenkategorien, getrennt durch einen senkrechten Strich (`|`). Nur die Datenkategorien, die im Mandanten bereits existieren, werden verknüpft: Dastra legt die übrigen nicht an.
* Um die Verknüpfungen zu exportieren, ist die Spalte **Datensätze** im Export der Liste enthalten.

## Kategorien in der Liste finden

Bei einer Auswahl können Sie **Prozessschritt umschalten**, **Zusammenführen** und **Löschen**.

## Wo Kategorien verwendet werden

* In einer Verarbeitungstätigkeit listet der Abschnitt **Betroffene Personen** die betroffenen Kategorien mit ihrem Umfang auf. Siehe [Betroffene Personen](../../ropa/activity/data-subjects.md).
* In Datenkategorien über **Kategorien betroffener Personen**. Siehe [Datenkategorien](datasets.md).

{% hint style="warning" %}
Das Löschen einer Kategorie entfernt alle ihre Verweise in Verarbeitungstätigkeiten, Datenschutzverletzungen, Anfragen zur Ausübung von Rechten und Datenkategorien.
{% endhint %}
