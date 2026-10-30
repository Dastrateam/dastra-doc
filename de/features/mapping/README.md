---
description: >-
  Erfahren Sie, wie Sie die personenbezogenen Daten Ihrer Organisation in Dastra
  kartieren
---

# Datenkartierung

## Alles beginnt mit einer Datenkartierung

Bevor Sie Ihre Verarbeitungstätigkeiten erstellen, kartieren Sie die Daten Ihrer Organisation so genau wie möglich. In der Anwendung heißt dieses Modul **Metadaten**. Die Kartierung verknüpft vier Arten von Elementen: den Herausgeber eines Assets, das Asset selbst, die darauf angewandten Sicherheitsmaßnahmen und die Datenkategorien, die es enthält und die aus Datenfeldern bestehen.

<figure><img src="../../.gitbook/assets/mapping-schema-1.png" alt="Diagramm der Datenkartierung: Der Herausgeber stellt Assets bereit, die mit Sicherheitsmaßnahmen und mit Datenkategorien aus Feldern verknüpft sind"><figcaption><p>Struktur der Datenkartierung</p></figcaption></figure>

Um alle personenbezogenen Daten Ihres Informationssystems zu inventarisieren, gehen Sie wie folgt vor:

1. **Die Assets erfassen**: Software, Dateien, Plugins, Server, Maschinen usw.
2. **Den Herausgeber des Assets angeben, sofern zutreffend**: Geben Sie die Angaben des Unternehmens ein, das dieses Asset herstellt. Es kann dann beim Aufbau des Verarbeitungsverzeichnisses unter Ihren Auftragsverarbeitern aufgeführt werden.
3. **Die Daten inventarisieren**: Listen Sie die zugehörigen Datenkategorien auf (Sie können sich auf den mit dem Auftragsverarbeiter unterzeichneten DPA stützen). Weitere Informationen finden Sie unter [Daten und Speicherdauer](../ropa/activity/datasets.md).
4. **Die vorhandenen Sicherheitsmaßnahmen auflisten**.

Diese Kartierung erleichtert die Erstellung von Verarbeitungstätigkeiten, weil Sie von der Realität Ihrer Daten ausgehen.

Wenn Sie dieses Inventar nicht aufbauen möchten oder die von Ihnen genutzte Software Standard ist, erstellen Sie Ihre Asset-Liste aus der Bibliothek vordefinierter Vorlagen, die gängige Assets des Marktes enthält (Salesforce, Jira usw.).

## Auf die Datenkartierung zugreifen

1. [Öffnen Sie Ihren Mandanten](../../getting-started/setup/workspace.md#auf-einen-mandanten-zugreifen).
2. Klicken Sie im Seitenmenü auf **Metadaten**.
3. Die Seite **Überblick** öffnet sich: eine Karte pro Referenzliste mit der Anzahl der darin enthaltenen Elemente.

Klicken Sie dann auf die Referenzliste, die Sie öffnen möchten. Den Zugriffsweg, die gemeinsamen Funktionen der Listen und die Grafiken finden Sie unter [Metadaten](repositories/README.md).

## Die Referenzlisten der Kartierung

Jede Referenzliste hat eine eigene Seite:

* [Assets](repositories/assets.md): die Software, Server und anderen Medien, die Ihre Daten enthalten.
* [Stakeholder](repositories/stakeholders.md): die Auftragsverarbeiter, Herausgeber und anderen Unternehmen und Personen, mit denen Sie arbeiten, und ihre Unterauftragsverarbeiter.
* [Datenkategorien](repositories/datasets.md): die Gruppen von Datenfeldern mit ihren Regeln zur Speicherdauer.
* [Datenglossar](repositories/data-glossary.md): die Datenfelder mit ihrer Kategorie und Sensibilitätsstufe.
* [Sicherheitsmaßnahmen](repositories/security-measures.md): die technischen und organisatorischen Maßnahmen, die die Daten schützen.
* [Betroffenenkategorien](repositories/subject-categories.md): die Personengruppen, deren Daten Sie verarbeiten.

Wie Sie eine Verbindung dokumentieren, die die Plattform nicht selbst ableitet, zum Beispiel ein mit einem Stakeholder verknüpftes Asset, lesen Sie unter [Generische Beziehungen](relationships.md). Wie Sie diese Referenzlisten in Ihrem Verzeichnis wiederverwenden, lesen Sie unter [Verarbeitungsverzeichnis](../ropa/README.md).

## Ihre Liste der Sicherheitsmaßnahmen aufbauen

Sicherheitsmaßnahmen haben eine eigene Referenzliste (siehe [Sicherheitsmaßnahmen](repositories/security-measures.md)): Erfassen Sie sie einmal und hängen Sie sie dann im Bereich **Verbundene Sicherheitsmaßnahmen** des Asset-Formulars an Assets an. Diese Angaben stehen oft im DPA, den Sie mit dem Herausgeber unterzeichnet haben. Wählen Sie kurze Namen (Virenschutz, Application Firewall, Zugriffskontrollen), damit eine Maßnahme von einem Asset zum anderen wiederverwendet werden kann.

## Ihre Auftragsverarbeiter verwalten

Ein Auftragsverarbeiter ist ein [Stakeholder](repositories/stakeholders.md) Ihrer Kartierung. Erfassen Sie ihn als **Herausgeber** des Assets: Er kann dann als Auftragsverarbeiter referenziert werden, wenn das Asset in einer Verarbeitungstätigkeit genannt wird. Im Formular des Stakeholders können Sie außerdem die Unterauftragsverarbeiter des Auftragsverarbeiters erfassen, um die gesamte Unterauftragskette zu kartieren.
