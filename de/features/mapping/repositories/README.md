---
description: >-
  Das Verarbeitungsverzeichnis stützt sich auf Referenzlisten: Assets,
  Stakeholder, Datenkategorien und Sicherheitsmaßnahmen. Dastra lässt Sie sie
  getrennt vom Verzeichnis verwalten, um Eingabefehler zu begrenzen.
---

# Metadaten

Um Eingabefehler zu begrenzen, lässt Dastra Sie eine oder mehrere Referenzlisten unabhängig vom Verarbeitungsverzeichnis verwalten. Die Verarbeitungstätigkeiten des Verzeichnisses verwenden dann die Elemente dieser Referenzlisten wieder.

## Auf die Referenzlisten zugreifen

Klicken Sie im Seitenmenü auf **Metadaten**. Das Menü bietet:

* **Überblick**: die Anzahl der Elemente in jeder Referenzliste.
* **Data Mapping**: eine grafische Darstellung Ihrer Assets und Stakeholder.
* **Assets**, **Stakeholder**, **Datenkategorien**, **Datensätze**, **Maßnahmen** und **Betroffenenkategorie**: die sechs Referenzlisten.

## Von Dastra bereitgestellte Referenzlisten

* **Assets**: Assets sind die Elemente, die Ihnen bei der Verwaltung von Daten helfen, etwa Datenträger, Räumlichkeiten sowie materielle und immaterielle Ausstattung. Siehe [Assets](assets.md).
* **Stakeholder**: Stakeholder unterscheiden sich von Nutzern, weil sie sich nicht auf der Plattform anmelden müssen.
* **Datenkategorien**: Datenkategorien sind Gruppen von Daten, die zusammenhängende Einheiten bilden, mit ihren Regeln zur Speicherdauer.
* **Datensätze** (im Englischen „Data glossary“): Datenfelder sind die einzelnen Informationen. Sie sind die kleinste Ebene in Dastra.
* **Maßnahmen**: Sicherheitsmaßnahmen sind die technischen oder organisatorischen Vorkehrungen zum Schutz der Daten.
* **Betroffenenkategorie**: Kategorien betroffener Personen fassen Kategorien von Personen zusammen.

## Gemeinsame Funktionen der Listen

Die Listen der sechs Referenzlisten haben mehrere Funktionen gemeinsam:

* **Erstellen Sie auf der Grundlage von Vorlagen** fügt ein Element aus der Vorlagenbibliothek hinzu.
* **Importieren** fügt Elemente aus einer Datei hinzu. Siehe [Ihre Daten importieren (Excel, CSV)](../../general/import.md).
* **Exportieren** exportiert die Liste.
* **Datenqualitätswerkzeug** erkennt Duplikate, und **Zusammenführen** fasst sie zusammen. Das Datenqualitätswerkzeug gibt es für Betroffenenkategorien nicht. Siehe [Elemente zusammenführen](../../general/merge.md).

## Überblick und Grafiken

Die Seite **Überblick** zeigt eine Karte pro Referenzliste mit der Anzahl ihrer Elemente. Klicken Sie auf eine Karte, um die zugehörige Liste zu öffnen. Mit der Schaltfläche **Asset erstellen** legen Sie von dieser Seite aus ein Asset an.

Die Seite **Data Mapping** bietet vier Darstellungen, die Sie in der Dropdown-Liste oben links wählen:

* **Kartierung der Datenflüsse zwischen den Assets**: ein Graph der Assets, ihrer Herausgeber, ihrer Datenkategorien und ihrer Tags. [Generische Beziehungen](../relationships.md) erscheinen als Verbindungen.
* **Kartografie der Stakeholder**: ein Graph der Stakeholder, ihrer Assets und ihrer nachfolgenden Auftragsverarbeiter, den Sie nach **Verantwortung** filtern können.
* **Diagramm zur Verteilung der Daten nach Assets** (Sankey-Diagramm): ein Diagramm der Verteilung der Daten nach Asset, das Sie nach Typ filtern können (Datenfelder, Verarbeitungstätigkeiten, Inhaber, Länder, Datenkategorien).
* **Hierarchischer Baum der Assets**.

Die Schaltflächen **Drucken** und **Aktualisieren** stehen oben auf der Seite zur Verfügung.

## Besonderheiten der einzelnen Referenzlisten

### Stakeholder

Ein Stakeholder kann einer Organisationseinheit zugeordnet werden, was seine Sichtbarkeit auf die Nutzer dieser Einheit beschränkt. Die Schaltfläche **Stakeholder erstellen** bietet an, von einer Vorlage (**Basierend auf einer Vorlage**) oder von Grund auf (**Von Grund auf neu**) zu beginnen.

Im Formular können Sie im Abschnitt **Unterauftragsverarbeiter** die Unterauftragsverarbeiter der Organisation erfassen, die oft im DPA genannt werden, und so die gesamte Unterauftragskette kartieren.

In der Liste findet der Filter **Verantwortung** Stakeholder danach, wie Sie sie verwenden: Software-Herausgeber (Herausgeber von mindestens einem Asset), Anbieter von KI-Modellen (Herausgeber von mindestens einem KI-Modell) oder Empfänger in einer Verarbeitungstätigkeit (Auftragsverarbeiter, gemeinsam Verantwortlicher, öffentliche Stelle usw.).

### Datenkategorien

Eine Datenkategorie fasst Datenfelder, sensibel oder nicht, mit den Regeln zur Speicherdauer zusammen, die für ihren Lebenszyklus gelten: zum Beispiel Gehaltsabrechnungen auf Papier oder Kundendatensätze in einem CRM. Füllen Sie die **Herkunft der Datenerhebung**, die **Nutzung** und die **Archivierung** aus und fügen Sie dann die Daten unter **Felder für personenbezogene Daten** hinzu.

Der Filter **Siehe „Orphan“ (ohne Asset)** listet die Datenkategorien auf, die keinem Asset zugeordnet sind. Sie können sie über das Feld **Verbundener Asset** zuordnen.

### Datensätze

Jedes Datenfeld hat eine **Sensibilität**:

* **Standard**, zum Beispiel Name, Vorname oder Telefonnummer.
* **Daten höchstpersönlicher Natur**, zum Beispiel Finanzdaten, Standortdaten oder Kommunikation.
* **Besondere Kategorien (sensibel)**, zum Beispiel rassische oder ethnische Herkunft, politische Meinungen, Religion, Gesundheit oder sexuelle Orientierung.

Die Stufe **Besondere Kategorien (sensibel)** blendet das Feld **Rechtsgrundlage für die Datenerhebung** ein. Die standardmäßig ausgeblendete Spalte **Datenkategorien** lässt sich mit **Ist leer** oder **Ist nicht leer** filtern: Damit finden Sie die Datenfelder, die zu keiner Datenkategorie gehören.

### Maßnahmen

Eine Maßnahme hat einen Namen, einen **Typ** und optional die Adresse ihrer Dokumentation, zum Beispiel auf der Website der CNIL. Der Filter **Siehe Waisen** listet die Maßnahmen auf, die weder einem Asset noch einer Verarbeitungstätigkeit zugeordnet sind.

### Betroffenenkategorien

Eine Kategorie hat einen Namen und die Option **Betroffene schutzbedürftige Personen**. Aktivieren Sie sie, wenn die Kategorie Personen in einer ungleichen Situation zusammenfasst, etwa Minderjährige, Beschäftigte oder ältere Menschen.
