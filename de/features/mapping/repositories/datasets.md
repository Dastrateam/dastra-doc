---
description: >-
  Fassen Sie Datenfelder zu zusammenhängenden Einheiten zusammen, mit den
  Regeln zur Speicherdauer, die für ihren Lebenszyklus gelten, und
  verwenden Sie sie in Ihren Assets und Verarbeitungstätigkeiten wieder.
---

# Datenkategorien

Eine Datenkategorie (im Englischen „Dataset“) fasst Datenfelder, sensibel oder nicht, mit den Regeln zur Speicherdauer zusammen, die für ihren Lebenszyklus gelten. Gehaltsabrechnungen auf Papier oder die Kundendatensätze eines CRM sind Beispiele für Datenkategorien.

Definieren Sie eine Datenkategorie einmal in dieser Referenzliste und verwenden Sie sie dann in den Assets, die sie enthalten, und in Ihren Verarbeitungstätigkeiten wieder. So bleibt das Inventar Ihrer Daten konsistent, und Sie finden für ein Asset alles, was es enthält.

## Eine Datenkategorie hinzufügen

Öffnen Sie **Metadaten** > **Datenkategorien**. Sie haben folgende Möglichkeiten:

* Klicken Sie auf **Datensatz erstellen**, um den **Assistent zur Erstellung von Datensätzen** zu öffnen, und wählen Sie dann **Von Grund auf neu erstellen**, **Erstellen mit KI-Assistent** (diese Option hängt von den Funktionen ab, die für Ihre Organisation aktiviert sind) oder die Schritt-für-Schritt-Anleitung, bei der Sie zuerst die Datenfelder der Datenkategorie auswählen. **Importer von Filerskeepers** erscheint, wenn die Integration [Filerskeepers](../../integrations/filerskeepers.md) aktiviert ist;
* klicken Sie auf die KI-Schaltfläche links von **Datensatz erstellen**, um die Datenkategorie zu beschreiben und den Assistenten einen Entwurf erstellen zu lassen;
* klicken Sie auf den Pfeil neben **Datensatz erstellen** und dann auf **Erstellen Sie auf der Grundlage von Vorlagen**, um eine Datenkategorie der Bibliothek zu kopieren;
* importieren Sie Datenkategorien mit ihren Datenfeldern aus einer Datei: Pfeil neben **Datensatz erstellen** und dann **Importieren**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-datasets-1.png" alt="Liste der Datenkategorien mit geöffnetem Bereich Filter"><figcaption><p>Die Liste der Datenkategorien</p></figcaption></figure>

## Das Formular der Datenkategorie ausfüllen

| Abschnitt | Feld | Inhalt |
| --- | --- | --- |
| **Allgemeine Informationen** | **Name des Datensatzes** | Der Name der Datenkategorie, erforderlich. |
| | **Verbundener Asset** | Das Asset, das die Datenkategorie enthält. Sie können aus diesem Feld ein Asset erstellen. Eine Datenkategorie ohne Asset ist verwaist (Orphan). |
| | **Kategorien betroffener Personen** | Die [Betroffenenkategorien](subject-categories.md), auf die sich die Daten beziehen. Sie können aus diesem Feld eine Kategorie erstellen. |
| | **Interne Referenz**, **Zusammenfassung** | Ihre Referenz und eine freie Beschreibung. |
| **Felder für personenbezogene Daten** | | Die Datenfelder der Datenkategorie. Wählen Sie ein Feld in der Liste aus oder erstellen Sie eines, füllen Sie dann die **Anmerkungen** aus und aktivieren Sie **Pflichtfeld**, wo das Feld verpflichtend ist. Jedes Feld zeigt seine Sensibilitätsstufe und seine Kategorie. |
| **Speicherdauer** | **Nutzung**, **Archivierung** | Jeweils: die **Speicherdauer**, die Regel (**Bitte beschreiben Sie die Regel (Dauer, Bedingungen usw.).**) und ihre **Begründung**. |
| | **Löschung** | Die Beschreibung der Löschregel und ihre **Begründung**. |
| **Herkunft der Datenerhebung** | **Herkunft der Datenerhebung**, **Beschreibung der Herkunft der Datenerhebung** | Woher die Daten erhoben werden. |

Die für Datenkategorien definierten [benutzerdefinierten Felder](../../general/custom-fields.md) und die [Tags](../../general/tags.md) werden dem Formular hinzugefügt.

Die Symbolleiste des Formulars gibt je nach Ihren Berechtigungen und den aktivierten Funktionen Zugriff auf die Kommentare, Fragebögen, Aufgaben und KI-Systeme, die mit der Datenkategorie verknüpft sind. Sie enthält außerdem:

* **Verknüpfte Elemente**: die [generischen Beziehungen](../relationships.md) der Datenkategorie;
* **Mit einer Datenverarbeitung verknüpfen**: die Verarbeitungstätigkeiten, die die Datenkategorie verwenden, und den Link, um weitere hinzuzufügen.

Das Aktionsmenü des Formulars bietet **Duplizieren**, **Zusammenführen** und **Löschen**.

## Datenkategorien in der Liste finden

Zu den Filtern der Liste gehören **Assets**, **Typen**, **Nach Tags filtern**, **Betroffenenkategorie**, **Datenkategorie** und **Sensible Daten**. Aktivieren Sie **Siehe „Orphan“ (ohne Asset)**, um die Datenkategorien aufzulisten, die keinem Asset zugeordnet sind, und ordnen Sie sie dann über das Feld **Verbundener Asset** zu.

Bei einer Auswahl können Sie **Felder bearbeiten**, **Zusammenführen**, **Exportieren** und **Löschen**. Das **Datenqualitätswerkzeug** im Menü von **Datensatz erstellen** erkennt Duplikate. Siehe [Elemente zusammenführen](../../general/merge.md).

## Wo Datenkategorien verwendet werden

* In einer Verarbeitungstätigkeit fügen Sie die Datenkategorien hinzu, die die Verarbeitung behandelt, und Sie können ihre Speicherdauer nur für diese Tätigkeit anpassen. Siehe [Daten und Speicherdauer](../../ropa/activity/datasets.md).
* In einem Asset listet der Abschnitt **Datensätze** die Datenkategorien auf, die es enthält. Siehe [Assets](assets.md).
* In Betroffenenkategorien: Das Formular einer Kategorie listet ihre Datenkategorien auf. Siehe [Betroffenenkategorien](subject-categories.md).
* In KI-Systemen über den Tab **KI-Systeme** der Datenkategorie.

{% hint style="warning" %}
Das Löschen einer Datenkategorie entfernt ihre Verknüpfungen zu Datenfeldern, Anhängen, Verarbeitungstätigkeiten und Assets. Die Unterhaltungen und die Bearbeitung zugehöriger Anfragen zur Ausübung von Rechten werden endgültig gelöscht. Fragebögen und zugehörige Aufgaben bleiben erhalten.
{% endhint %}
