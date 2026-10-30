---
description: >-
  Importieren Sie Ihre Daten aus einer Excel- oder CSV-Datei in Dastra:
  importierbare Objekte, Konfliktmanagement, Spaltenzuordnung und Ergebnis.
---

# Daten importieren (Excel, CSV)

## Daten in Dastra importieren

Dastra importiert Ihre eigenen Daten aus einer Tabellendatei. Starten Sie den Import in jeder Liste, die ihn unterstützt, über den Pfeil der Schaltfläche zum Erstellen und dann über **Importieren**.

<figure><img src="../../.gitbook/assets/general-import-1.png" alt="Liste der Datensätze mit geöffnetem Menü der Schaltfläche zum Erstellen und dem Eintrag Importieren"><figcaption><p>Der Eintrag Importieren im Menü der Schaltfläche zum Erstellen</p></figcaption></figure>

Die folgenden Objekte können importiert werden:

| Objekt | Ort des Imports | Hinweis |
| --- | --- | --- |
| Verarbeitungstätigkeiten | Dateninventar > Verarbeitungsverzeichnis > Verarbeitungstätigkeiten | Flache Datei (CSV), komplexe Excel-Arbeitsmappe (Beta) oder JSON |
| Assets | Dateninventar > Metadaten > Assets | Excel oder CSV, oder JSON |
| Stakeholder | Dateninventar > Metadaten > Stakeholder | |
| Datensätze | Dateninventar > Metadaten > Datenkategorien | |
| Datenfelder | Dateninventar > Metadaten > Datenglossar | |
| Sicherheitsmaßnahmen | Dateninventar > Metadaten > Maßnahmen | |
| Kategorien betroffener Personen | Dateninventar > Metadaten > Betroffenenkategorie | |
| KI-Systeme und KI-Modelle | Dateninventar > KI-Governance | |
| Betroffenenanfragen | Betrieb > Anfragen > Anfragen | |
| Datenschutzvorfälle | Betrieb > Vorfälle > Verzeichnis der Vorfälle | |
| Aufgaben | Betrieb > Aufgaben > Aufgaben | Projekte werden als JSON über **Projekte** importiert |
| Verträge und Richtlinien | Betrieb > Verträge und Richtlinien > Verzeichnis der Verträge und Richtlinien | |
| Risikotypen, Bedrohungen, Quellen, Kontrollpunkte und Ereignisse | Governance > Risikomanagement | |
| Fragebogenvorlagen | Governance > Fragebögen > Vorlagen > **Vorlage erstellen** > **Eine Datei senden** | Excel-Datei oder JSON-Datei |
| Fragebogenantworten | Antwortliste einer Vorlage > **Fragebogen planen** > **Antworten importieren** | |
| Frameworks, Kontrollen, Tests, Bedrohungen und Risiken der Bibliothek | Governance > Compliance > Bibliothek | Zu den Frameworks siehe [Dastra-Import und Vorlagen](../compliance/library/frameworks/import.md) |
| Tags | Mandanteneinstellungen > Prozess > Tags | |
| Nachrichtenvorlagen | Mandanteneinstellungen > Vorlagen | |
| Organisationseinheiten | Mandanteneinstellungen > Zugriffsverwaltung > Organisationseinheiten | CSV-Datei |

Ein durchgängiges Beispiel mit einem benutzerdefinierten Feld und dem Modus **Zusammenführen** finden Sie unter [Assets aus einer Tabelle importieren](../../examples/excel-import.md).

Bei jedem Import ist der Ablauf derselbe. Er erfolgt in 4 Schritten:

1. [Die Datendatei vorbereiten](import.md#1.-die-datendatei-vorbereiten)
2. [Die Datei laden](import.md#2.-die-datei-laden)
3. [Ihre Daten überprüfen](import.md#3.-ihre-daten-uberprufen)
4. [Die Daten importieren](import.md#4.-die-daten-importieren)

### 1. Die Datendatei vorbereiten

Dastra unterstützt die folgenden Datenformate:

* **Excel** (.xlsx)
* **Flache Dateien** (.csv, .txt) mit dem Trennzeichen ; und der Kodierung UTF-8 (die Kodierung ist wichtig, damit Umlaute und Akzente erhalten bleiben)
* **JSON**, für das vollständige Verzeichnis, Assets, Projekte, Fragebogenvorlagen und Compliance-Frameworks

Bei einigen Listen müssen Sie das Format wählen, bevor sich der Import-Assistent öffnet. Beim Verarbeitungsverzeichnis öffnet **Flache Datei** den unten beschriebenen Assistenten.

#### Die Dateivorlage herunterladen

Klicken Sie im Import-Assistenten auf **Laden Sie die Dateivorlage herunter**. Die Vorlage ist eine **CSV-Datei**, die Sie mit Excel, LibreOffice oder Google Sheets bearbeiten können. Sie enthält alle Spalten des Imports mit einer Zeile Beispieldaten, die Sie durch Ihre Daten ersetzen.

#### Die Dateivorlage ausfüllen

Füllen Sie die heruntergeladene Datei mit Ihren Daten aus. Bei jedem Import zeigt die Schaltfläche **Spaltenformat anzeigen** die erwarteten Spalten, ihre Regeln und ihre möglichen Werte an.

<figure><img src="../../.gitbook/assets/general-import-3.png" alt="Fenster Spaltenformat für den Import mit Typ, Regeln und möglichen Werten jeder Spalte"><figcaption><p>Das vom Import erwartete Spaltenformat</p></figcaption></figure>

Die möglichen Werte werden auf Englisch angegeben: Es handelt sich um einen technischen Import in die Datenbank. Sie entsprechen den Auswahllisten der Anwendung.

Beim Import des Verzeichnisses zum Beispiel:

* Die Spalte `State` ist der Status der Verarbeitungstätigkeit: `Draft` für **Entwurf** und `Active` für **Veröffentlicht**. Ist die Zelle leer, wird die Verarbeitungstätigkeit mit dem Status **Veröffentlicht** erstellt.
* Die Spalte `ProcessingState` ist das Feld **Status der Datenverarbeitung** im Schritt **Allgemeines**: `Study` für **Zu prüfen**, `BeingDeployed` für **Derzeit in der Einführung**, `InProduction` für **In Produktion** und `Stopped` für **Beschluss** (englisch „Stopped“).

Ein Wert, der keiner der möglichen Auswahlen entspricht, blockiert den Import nicht: Er wird durch den Standardwert der Spalte ersetzt. Prüfen Sie Ihre Werte, bevor Sie die Datei senden.

### Datensätze: Import der zugehörigen Felder

Der Export der Datensätze enthält eine Spalte **Personal data fields**, die die zugehörigen Datenfelder auflistet. Jedes Feld wird als `label#sensitivity classification#personal data category` geschrieben, und die Felder werden durch `|` getrennt. Dasselbe Format wird für den Import verwendet.

Beim Import gilt für jeden **neuen** Datensatz:

* Ein Feld, dessen Label im Mandanten bereits existiert, wird unverändert verknüpft: Die Klassifizierung und die Kategorie in der Datei ändern es nicht.
* Ein Feld, dessen Label nicht existiert, wird automatisch erstellt.

{% hint style="info" %}
Zugehörige Felder werden nur für Datensätze gelesen, die durch den Import erstellt werden. Im Modus **Fusion** werden die Felder eines bestehenden Datensatzes nicht verändert.
{% endhint %}

Um Datensätze zu importieren, öffnen Sie **Dateninventar** > **Metadaten** > **Datenkategorien**, klicken Sie auf den Pfeil der Schaltfläche **Datensatz erstellen** und dann auf **Importieren**.

### 2. Die Datei laden

Im Import-Assistenten fragen einige Objekte zuerst nach einer Organisationseinheit: Alle importierten Elemente werden ihr zugeordnet. Das gilt für Verarbeitungstätigkeiten, Anfragen, Datenschutzvorfälle, Aufgaben, Verträge und KI-Systeme.

<figure><img src="../../.gitbook/assets/general-import-2.png" alt="Schritt Versenden der Datei des Import-Assistenten mit dem Konfliktmanagement im Modus Fusion, dem Zuordnungsfeld und der Ablagezone"><figcaption><p>Der Schritt Versenden der Datei, mit dem Konfliktmanagement</p></figcaption></figure>

#### Konfliktmanagement

Bei Objekten mit einem Zuordnungsschlüssel (zum Beispiel dem Label oder der Referenz) legt die Gruppe **Konfliktmanagement** fest, was geschieht, wenn eine Zeile der Datei mit einem bestehenden Datensatz übereinstimmt. Die drei Modi sind:

* **Keine** (Standard): Jede Zeile erstellt einen neuen Datensatz, auch wenn bereits ein identischer Datensatz existiert.
* **Fusion**: Zeilen, die mit einem bestehenden Datensatz übereinstimmen, aktualisieren ihn, die übrigen Zeilen erstellen neue Datensätze.
* **Aufbewahrung**: Zeilen, die mit einem bestehenden Datensatz übereinstimmen, werden übersprungen, und dieser Datensatz bleibt unverändert; die übrigen Zeilen erstellen neue Datensätze.

Wählen Sie bei **Fusion** oder **Aufbewahrung** das **Feld, das für die Datenübereinstimmung verwendet werden soll**. Eine Zeile stimmt mit einem Datensatz überein, wenn der Wert dieses Feldes in der Datei und im Mandanten streng identisch ist (einschließlich Groß- und Kleinschreibung).

{% hint style="warning" %}
Der Modus **Fusion** ersetzt die gespeicherten Werte durch die der Datei. Eine leere Zelle lässt den bestehenden Wert unverändert, außer in Spalten mit einer Pflichtauswahl (zum Beispiel dem Typ oder dem Status eines Assets), die dann ihren Standardwert annehmen: Füllen Sie sie immer aus. Prüfen Sie Ihre Datei vor dem Start des Imports, denn der Vorgang kann nicht rückgängig gemacht werden.
{% endhint %}

Objekte ohne Zuordnungsschlüssel, wie Tags, Nachrichtenvorlagen, Anfragen oder Risikotypen, zeigen diese Gruppe nicht an. Bei Datenschutzvorfällen wird die Gruppe angezeigt, aber jede Zeile erstellt immer einen Datensatz. Importe der Compliance-Bibliothek überspringen die Zeilen, deren Referenz bereits existiert, unabhängig vom Modus.

{% hint style="info" %}
Bei **Assets** aktualisiert der Modus **Fusion** auch die **benutzerdefinierten Felder**, unabhängig von ihrem Typ. Wie bei den nativen Spalten lässt eine leere Zelle den gespeicherten Wert unverändert, und eine Liste mit Mehrfachantwort ersetzt die bestehende Liste vollständig. Wird ein Wert abgelehnt, bricht der Import ab, ohne etwas zu ändern, und nennt die betroffene Zeile.
{% endhint %}

#### Die Datei senden

Klicken Sie auf die Zone **Bitte senden/verschieben Sie die Dateien hierher**, um Ihre Datei auszuwählen, oder legen Sie sie direkt in der Zone ab. Dastra liest die ersten Zeilen, um die Spaltenzuordnung vorzubereiten.

### 3. Ihre Daten überprüfen

Der Schritt **Entsprechungen** ordnet die Spalten Ihrer Datei den vom Import erwarteten Spalten zu. Dastra ordnet sie automatisch zu, wenn die Kopfzeile mit dem Namen oder dem Label der Spalte identisch ist. Die Tabs **Alle Spalten**, **Keine Übereinstimmung** und **Korrespondenz (importierte Datei)** filtern die Liste, und die Spalte **Daten aus der Datei** zeigt eine Auswahl Ihrer Daten.

<figure><img src="../../.gitbook/assets/general-import-4.png" alt="Schritt Entsprechungen mit den Dastra-Spalten, der zugeordneten Spalte der Datei und einer Datenauswahl"><figcaption><p>Der Schritt Entsprechungen</p></figcaption></figure>

Die Schaltfläche **Weiter** bleibt deaktiviert, solange eine Pflichtspalte keine Zuordnung hat.

### 4. Die Daten importieren

Klicken Sie auf **Weiter**, um den Import zu starten. Der Bildschirm **Ergebnis** zeigt die Anzahl der verarbeiteten Zeilen, der erstellten, der aktualisierten und der übersprungenen Objekte. Klicken Sie auf **Anzeigen**, um die Liste zu öffnen.

<figure><img src="../../.gitbook/assets/general-import-5.png" alt="Bildschirm Ergebnis des Imports mit der Anzahl der verarbeiteten Zeilen sowie der erstellten, aktualisierten und übersprungenen Objekte"><figcaption><p>Das Ergebnis des Imports</p></figcaption></figure>

Schlägt die Prüfung einer Zeile fehl (zum Beispiel wegen eines leeren Pflichtfeldes oder eines zu langen Wertes), wird der gesamte Import abgebrochen, und es wird nichts gespeichert. Die Meldung nennt die Nummer der betroffenen Zeile, wobei die Kopfzeile der Datei als Zeile 1 zählt. Korrigieren Sie die Datei und starten Sie den Import erneut.

Prüfen Sie anschließend, ob die Daten korrekt in das Tool importiert wurden.
