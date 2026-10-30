---
description: >-
  Das Verarbeitungsverzeichnis stützt sich auf Referenzlisten: Assets,
  Stakeholder, Datenkategorien, Datenfelder, Sicherheitsmaßnahmen und
  Betroffenenkategorien. Dastra lässt Sie sie getrennt vom Verzeichnis
  verwalten, um Eingabefehler zu begrenzen.
---

# Metadaten

Um Eingabefehler zu begrenzen, lässt Dastra Sie Referenzlisten unabhängig vom Verarbeitungsverzeichnis verwalten. Die Verarbeitungstätigkeiten des Verzeichnisses verwenden dann die Elemente dieser Referenzlisten wieder.

## Auf die Referenzlisten zugreifen

Klicken Sie im Seitenmenü auf **Metadaten**. Das Menü bietet:

* **Überblick**: die Anzahl der Elemente in jeder Referenzliste.
* **Data Mapping**: eine grafische Darstellung Ihrer Assets und Stakeholder.
* **Assets**, **Stakeholder**, **Datenkategorien**, **Datensätze**, **Maßnahmen** und **Betroffenenkategorie**: die sechs Referenzlisten.

Was Sie tun können, hängt von den Berechtigungen Ihrer Rolle für die Datenkartierung und die Referenzlisten ab. Siehe [Rollen und Berechtigungen](../../settings/roles.md).

## Die sechs Referenzlisten

* [Assets](assets.md): Datenträger, Räumlichkeiten sowie materielle und immaterielle Ausstattung.
* [Stakeholder](stakeholders.md): die Unternehmen und Personen, die mit Ihren Verarbeitungen verbunden sind und sich nicht auf der Plattform anmelden müssen.
* [Datenkategorien](datasets.md): Gruppen von Datenfeldern, die zusammenhängende Einheiten bilden, mit ihren Regeln zur Speicherdauer.
* [Datenglossar](data-glossary.md): die Datenfelder, die kleinste Ebene in Dastra. Der Menüeintrag heißt **Datensätze**.
* [Sicherheitsmaßnahmen](security-measures.md): die technischen oder organisatorischen Vorkehrungen zum Schutz der Daten. Der Menüeintrag heißt **Maßnahmen**.
* [Betroffenenkategorien](subject-categories.md): die Personengruppen, deren Daten Sie verarbeiten. Der Menüeintrag heißt **Betroffenenkategorie**.

Jede Seite beschreibt die Felder des Formulars, wie Sie Elemente erstellen, importieren und zusammenführen und wo die Referenzliste verwendet wird. Wie eine Verarbeitungstätigkeit diese Elemente nutzt, ist einmal in den Seiten der Tätigkeit beschrieben: siehe [Eine Verarbeitung ausfüllen](../../ropa/activity/README.md).

## Gemeinsame Funktionen der Listen

Die Listen der sechs Referenzlisten haben mehrere Funktionen gemeinsam:

* **Erstellen Sie auf der Grundlage von Vorlagen** fügt ein Element aus der Vorlagenbibliothek hinzu. Bei den meisten Referenzlisten entwirft eine KI-Schaltfläche neben der Schaltfläche zum Erstellen ein Element aus einer kurzen Beschreibung, sofern die Funktion für Ihre Organisation aktiviert ist.
* **Importieren** fügt Elemente aus einer Datei hinzu. Siehe [Daten importieren (Excel, CSV)](../../general/import.md).
* **Exportieren** exportiert die Liste oder nur die ausgewählten Zeilen.
* **Datenqualitätswerkzeug** erkennt Duplikate, und **Zusammenführen** fasst sie zusammen. Das Datenqualitätswerkzeug gibt es für Betroffenenkategorien nicht. Siehe [Elemente zusammenführen](../../general/merge.md).
* Filter, benutzerdefinierte Spalten und benutzerdefinierte Ansichten. Siehe [Erweiterte Filter](../../general/filters.md).
* Sammelaktionen für eine Auswahl von Zeilen. Siehe [Listen, Sammelaktionen und Papierkorb](../../general/lists.md). **Felder bearbeiten**, wo angeboten, ändert dasselbe Feld bei allen ausgewählten Elementen.
* Die Tabellen- und die Kartenansicht, für Assets und Stakeholder.

In den Referenzlisten fragt **Löschen** nach einer Bestätigung und löscht das Element endgültig: Der auf der Seite zu den Listen beschriebene Papierkorb gilt hier nicht.

Die Formulare enthalten außerdem die [benutzerdefinierten Felder](../../general/custom-fields.md), außer bei Betroffenenkategorien, und in der Symbolleiste, wo angeboten, die [generischen Beziehungen](../relationships.md) des Elements.

## Überblick und Grafiken

Die Seite **Überblick** zeigt eine Karte pro Referenzliste mit der Anzahl ihrer Elemente. Klicken Sie auf eine Karte, um die zugehörige Liste zu öffnen. Mit der Schaltfläche **Asset erstellen** legen Sie von dieser Seite aus ein Asset an.

Die Seite **Data Mapping** bietet vier Darstellungen, die Sie in der Dropdown-Liste oben links wählen:

* **Kartierung der Datenflüsse zwischen den Assets**: ein Graph der Assets, ihrer Herausgeber, ihrer Datenkategorien und ihrer Tags. [Generische Beziehungen](../relationships.md) erscheinen als Verbindungen.
* **Kartografie der Stakeholder**: ein Graph der Stakeholder, ihrer Assets und ihrer nachfolgenden Auftragsverarbeiter, den Sie nach **Verantwortung** filtern können.
* **Diagramm zur Verteilung der Daten nach Assets** (Sankey-Diagramm): ein Diagramm der Verteilung der Daten nach Asset, das Sie nach Typ filtern können (Datenfelder, Verarbeitungstätigkeiten, Inhaber, Länder, Datenkategorien).
* **Hierarchischer Baum der Assets**.

Die Schaltflächen **Drucken** und **Aktualisieren** stehen oben auf der Seite zur Verfügung.
