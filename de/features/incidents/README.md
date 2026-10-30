---
description: >-
  Führen Sie das Verzeichnis der Vorfälle und Datenschutzverletzungen Ihrer
  Organisation, verfolgen Sie die Meldefristen und sehen Sie die Statistiken ein.
---

# Datenschutzvorfälle

Das Modul **Vorfälle** von Dastra dokumentiert Sicherheitsvorfälle, die personenbezogene Daten betreffen, verfolgt die Meldungen an die Aufsichtsbehörde und an die betroffenen Personen und führt ein Verzeichnis jedes Vorfalls. Es richtet sich an Datenschutzbeauftragte, Sicherheitsteams und Rechtsabteilungen.

Was eine Verletzung des Schutzes personenbezogener Daten ist und welche Pflichten Sie haben, lesen Sie auf der Seite [Meldung von Datenschutzverletzungen](../../gdpr/concepts/breaches.md).

## Warum ein Verzeichnis der Verletzungen führen

Artikel 33 Absatz 5 DSGVO verpflichtet jede Organisation, alle Verletzungen des Schutzes personenbezogener Daten zu dokumentieren: die Fakten, ihre Auswirkungen und die ergriffenen Maßnahmen. Das gilt auch, wenn die Verletzung der Aufsichtsbehörde nicht gemeldet wird.

Das Verzeichnis hilft Ihnen außerdem, Meldefristen einzuhalten und Präventionsmaßnahmen zu erkennen. Weitere Informationen finden Sie auf der [dafür vorgesehenen Seite der Dastra-Website](https://www.dastra.eu/en/product-features/data-breach).

## Das Verzeichnis der Vorfälle öffnen

Öffnen Sie im linken Menü **Betrieb** > **Vorfälle** > **Verzeichnis der Vorfälle**.

<figure><img src="../../.gitbook/assets/incidents-readme-1.png" alt="Linkes Menü mit der Gruppe Betrieb und dem aufgeklappten Eintrag Vorfälle"><figcaption><p>Das Modul Vorfälle im linken Menü</p></figcaption></figure>

Das Modul erscheint nur, wenn die Funktion für Ihre Organisation aktiviert ist und Ihre Rolle Zugriff auf Vorfälle gibt.

## Das Verzeichnis lesen

Das Verzeichnis listet die Vorfälle des Mandanten auf, einen pro Zeile.

<figure><img src="../../.gitbook/assets/incidents-readme-2.png" alt="Verzeichnis der Vorfälle mit der Kennzahlenleiste über der Tabelle"><figcaption><p>Das Verzeichnis der Vorfälle</p></figcaption></figure>

### Kennzahlenleiste

Über der Tabelle zählt eine Kennzahlenleiste die Vorfälle:

* **Gesamt**, **In Bearbeitung** (Status Aktiv) und **Geschlossen**;
* **Ohne Risikoanalyse** und **Mit sensiblen Daten**;
* **Einschließlich eines KI-Systems**, wenn das Modul KI-Systeme aktiviert ist.

Klicken Sie auf eine Kennzahl, um die Tabelle auf die Vorfälle zu filtern, die sie zählt.

### Spalten und Filter

Sie wählen die Spalten der Tabelle selbst. Die Spalte **Authority control notification** zeigt bei jedem Vorfall, dessen Meldung verpflichtend ist, die Anzahl der verbleibenden Stunden (grünes Badge) oder der überschrittenen Stunden (rotes Badge), danach **Sie haben die Aufsichtsbehörde informiert**, sobald die Meldung erfasst ist. Ist keine Meldung nötig, zeigt die Zelle **Keine Benachrichtigung der Behörde erforderlich**.

Zu den Filtern gehören die Organisationseinheit, Tags, **Arten von Vorfällen**, **Status** (Neu, Aktiv, Geschlossen), **Rolle** (Auftragsverarbeiter oder Verantwortlicher), die **Schritte** des Workflows und die **Person, die für den Vorfall verantwortlich ist**. Aktivieren Sie **Mit Benachrichtigungsfunktion**, um nur die Vorfälle zu behalten, die gemeldet wurden, oder **Verknüpft mit einem KI-System** für die Vorfälle, an denen ein KI-System beteiligt ist. Zu erweiterten Filtern und benutzerdefinierten Ansichten siehe [Erweiterte Filter](../general/filters.md).

### Aktionen für Vorfälle

* Klicken Sie auf eine Zeile, um den Vorfall zu öffnen.
* Das Menü am Ende einer Zeile bietet **Bearbeiten**, **Felder bearbeiten** und **In den Papierkorb verschieben**.
* Aktivieren Sie mehrere Zeilen, um auf die Auswahl zu wirken: **Prozessschritt umschalten**, **Felder bearbeiten**, **Exportieren**, **Teilen** oder **In den Papierkorb verschieben**.
* Die Schaltfläche **Einen Vorfall hinzufügen** erstellt einen Vorfall. Ihr Pfeil öffnet ein Menü mit **Importieren**, **Exportieren**, **Teilen** und **Bitte lesen Sie die Dokumentation**.

### Papierkorb

**In den Papierkorb verschieben** entfernt den Vorfall aus dem Verzeichnis, ohne ihn zu löschen. Aktivieren Sie **Papierkorb anzeigen**, um die Vorfälle im Papierkorb anzuzeigen, und wählen Sie dann **Wiederherstellen**, um sie wieder in das Verzeichnis aufzunehmen, oder **Löschen**, um sie zu löschen.

{% hint style="warning" %}
**Löschen** löscht den Vorfall endgültig. Artikel 33 Absatz 5 DSGVO verlangt weiterhin, dass Sie jede Verletzung belegen können: Löschen Sie nicht die Spur einer Verletzung, die Sie dokumentieren müssen.
{% endhint %}

## Die Statistiken ansehen

Öffnen Sie **Betrieb** > **Vorfälle** > **Statistiken**, um einen Überblick über das Verzeichnis zu erhalten. Die Schaltfläche **Drucken** erzeugt eine druckbare Version der Seite.

<figure><img src="../../.gitbook/assets/incidents-readme-3.png" alt="Die Seite Statistiken der Vorfälle mit den Kennzahlen und den Diagrammen"><figcaption><p>Die Seite Statistiken der Vorfälle</p></figcaption></figure>

Die Seite zeigt:

* die Kennzahlen **Gesamtzahl der Vorfälle**, **Mit dokumentierter Post-Mortem-Analyse**, **Mit Risikoanalyse**, **Ohne Risikoanalyse**, **Mit sensiblen Daten** und **Einschließlich eines KI-Systems**;
* die Diagramme **Aufteilung nach Workflow-Schritten**, **Aufteilung nach Tags**, **Aufteilung nach Rollen** und **Vorfälle nach Organisationseinheiten**.

## Weiterführende Informationen

{% content-ref url="document-breach.md" %}
[Einen neuen Datenschutzvorfall dokumentieren](document-breach.md)
{% endcontent-ref %}

{% content-ref url="as-processor.md" %}
[Datenschutzvorfälle als Auftragsverarbeiter](as-processor.md)
{% endcontent-ref %}

{% content-ref url="export.md" %}
[Ihre Datenschutzvorfälle exportieren](export.md)
{% endcontent-ref %}
