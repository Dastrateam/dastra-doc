---
description: >-
  Pflegen Sie die Liste der Datenfelder, der kleinsten Ebene der
  Datenkartierung, mit ihrer Kategorie und Sensibilitätsstufe.
---

# Datenglossar

Ein Datenfeld ist eine einzelne Information, etwa ein Name, eine E-Mail-Adresse oder eine Gesundheitsnummer. Es ist die kleinste Ebene der Kartierung: [Datenkategorien](datasets.md) bestehen aus Datenfeldern. In der Anwendung heißt diese Referenzliste im Menü **Datensätze**.

Führen Sie jedes Feld einmal in diesem Glossar auf, damit jede Datenkategorie dieselben Daten auf dieselbe Weise beschreibt.

## Ein Datenfeld hinzufügen

Öffnen Sie **Metadaten** > **Datensätze**. Sie haben folgende Möglichkeiten:

* Klicken Sie auf **Daten erstellen**, um ein leeres Formular zu öffnen;
* klicken Sie auf den Pfeil neben **Daten erstellen** und dann auf **Erstellen Sie auf der Grundlage von Vorlagen**, um Felder der Bibliothek zu kopieren;
* importieren Sie Felder aus einer Datei: Pfeil neben **Daten erstellen** und dann **Importieren**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md).

Sie können ein Feld auch direkt im Abschnitt **Felder für personenbezogene Daten** einer Datenkategorie erstellen.

## Das Formular des Datenfelds ausfüllen

| Feld | Inhalt |
| --- | --- |
| **Name** | Der Name des Felds, erforderlich. |
| **Interne Referenz** | Ihre Referenz. |
| **Datenkategorie personenbezogener Daten** | Die Kategorie personenbezogener Daten, zu der das Feld gehört. |
| **Sensibilität** | **Standard** (Name, Vorname, Telefonnummer), **Daten höchstpersönlicher Natur** (Finanzdaten, Standortdaten, Kommunikation) oder **Besondere Kategorien (sensibel)** (rassische oder ethnische Herkunft, politische Meinungen, Religion, Gesundheit, sexuelle Orientierung). |
| **Rechtsgrundlage für die Datenerhebung**, **Begründung für die Datenerhebung sensibler Daten** | Nur bei der Stufe **Besondere Kategorien (sensibel)** angezeigt: die in der Liste gewählte Rechtsgrundlage und Ihre Begründung. |
| **Beschreibung der Daten**, **Technische Beschreibung** | Eine freie Beschreibung und die technische Definition des Felds. |
| **Datentypen** | Der allgemeine Typ der Daten. |

Die für Datenfelder definierten [benutzerdefinierten Felder](../../general/custom-fields.md) werden dem Formular hinzugefügt. Die Symbolleiste gibt Zugriff auf die Kommentare und Aufgaben, die mit dem Feld verknüpft sind, auf den Aktivitätsverlauf und, wenn Workflow-Schritte definiert sind, auf den Workflow-Schritt. Die Schaltfläche mit dem Datenbanksymbol listet die Datenkategorien auf, die das Feld enthalten.

Das Aktionsmenü des Formulars bietet **Zusammenführen** und **Löschen**.

## Datenfelder in der Liste finden

Die Filter sind **Datenkategorie personenbezogener Daten** und **Datentypen**. Die standardmäßig ausgeblendete Spalte **Datensätze** unter **Spalten anpassen** lässt sich mit **Ist leer** oder **Ist nicht leer** filtern: Damit finden Sie die Felder, die zu keiner Datenkategorie gehören.

Bei einer Auswahl können Sie **Prozessschritt umschalten**, **Felder bearbeiten**, **Zusammenführen**, **Exportieren** und **Löschen**. Das **Datenqualitätswerkzeug** im Menü von **Daten erstellen** erkennt Duplikate. Siehe [Elemente zusammenführen](../../general/merge.md).

## Wo Datenfelder verwendet werden

Datenfelder gelangen über Datenkategorien in Ihre Verarbeitungstätigkeiten. Siehe [Daten und Speicherdauer](../../ropa/activity/datasets.md), wo Sie auch die Felder einer Datenkategorie zu einer Verarbeitungstätigkeit hinzufügen können.

{% hint style="warning" %}
Das Löschen eines Datenfelds entfernt endgültig alle seine Verweise auf Datenkategorien. Die verknüpften Unterhaltungen werden gelöscht.
{% endhint %}
