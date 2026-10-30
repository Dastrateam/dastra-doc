---
description: >-
  Erfahren Sie, wie Sie die personenbezogenen Daten Ihrer Organisation in Dastra
  kartieren
---

# Datenkartierung

## Alles beginnt mit einer Datenkartierung

Bevor Sie Ihre Verarbeitungstätigkeiten erstellen, kartieren Sie die Daten Ihrer Organisation so genau wie möglich. In der Anwendung heißt dieses Modul **Metadaten**. Die Kartierung verknüpft vier Arten von Elementen: den Herausgeber eines Assets, das Asset selbst, die darauf angewandten Sicherheitsmaßnahmen und die Datenkategorien, die es enthält und die aus Datenfeldern bestehen.

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

Klicken Sie dann auf die Referenzliste, die Sie öffnen möchten. Einzelheiten zu jeder Referenzliste finden Sie unter [Metadaten](repositories/README.md).

## Ihre Liste der Sicherheitsmaßnahmen aufbauen

Sicherheitsmaßnahmen haben eine eigene Referenzliste: Erfassen Sie sie einmal und hängen Sie sie dann im Bereich **Verbundene Sicherheitsmaßnahmen** des Asset-Formulars an Assets an. Diese Angaben stehen oft im DPA, den Sie mit dem Herausgeber unterzeichnet haben. Wählen Sie kurze Namen (Virenschutz, Application Firewall, Zugriffskontrollen), damit eine Maßnahme von einem Asset zum anderen wiederverwendet werden kann.

## Ihre Auftragsverarbeiter verwalten

Ein Auftragsverarbeiter ist ein Stakeholder Ihrer Kartierung. Erfassen Sie ihn als **Herausgeber** des Assets: Er kann dann als Auftragsverarbeiter referenziert werden, wenn das Asset in einer Verarbeitungstätigkeit genannt wird. Im Formular des Stakeholders können Sie außerdem die Unterauftragsverarbeiter des Auftragsverarbeiters erfassen, um die gesamte Unterauftragskette zu kartieren.
