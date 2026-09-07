---
description: >-
  Funktionsweise von Verbindungen, Anwendungsfällen und Feld-Mappings, die für
  alle nativen Integrationen gelten
---

# Verbindungen, Anwendungsfälle und Feld-Mapping

Diese Seite beschreibt die Konzepte, die für alle nativen Integrationen gelten. Anweisungen für die einzelnen Konnektoren finden Sie auf den jeweiligen Seiten (ServiceNow, SAP LeanIX, Jira, Microsoft Teams usw.).

### Der Integrationskatalog

Öffnen Sie in Ihrem Workspace **Einstellungen > Integrationen**. Der Katalog listet alle verfügbaren Integrationen auf und kann nach Kategorie sowie nach dem jeweiligen Dastra-Objekt gefiltert werden. Zusätzlich stehen die Registerkarten **Alle / Installiert** zur Verfügung.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf eine Integration, um ihre Seite zu öffnen. Dort werden die verfügbaren **Anwendungsfälle** angezeigt (jeweils mit der Richtung des Datenflusses, z. B. _ServiceNow > Dastra_), außerdem die Beschreibung und — bei Konnektoren, die sich bei einem externen Tool authentifizieren — die Schaltfläche **Verbindungen verwalten**.

### Die Verbindungen

Eine Verbindung speichert die Informationen, die Dastra zur Authentifizierung beim externen Tool benötigt: entweder Zugangsdaten (Benutzername/Passwort oder API-Schlüssel, von Dastra verschlüsselt gespeichert) oder eine delegierte **OAuth**-Autorisierung (Dastra speichert dabei kein Passwort).

Sie können **mehrere Verbindungen zum selben Tool** erstellen — beispielsweise eine Produktionsinstanz und eine Sandbox — und für jeden Anwendungsfall auswählen, welche Verbindung verwendet werden soll.

Klicken Sie auf **Verbindungen verwalten**, um das Verbindungsfenster zu öffnen. Für jede Verbindung sehen Sie:

* ihren Status: **Verbindung funktionsfähig**, **Autorisierung ausstehend** (OAuth wurde gestartet, aber noch nicht abgeschlossen) oder **Verbindungsfehler** (mit der letzten Fehlermeldung und der Anzahl der Fehler),
* die Authentifizierungsmethode,
* die Anwendungsfälle, die diese Verbindung verwenden.

In diesem Bereich können Sie eine Verbindung **testen** (ein erfolgreicher Test setzt auch ihren Fehlerstatus zurück) oder sie **löschen**.

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Um eine Verbindung zu erstellen, klicken Sie auf **Verbindung hinzufügen**:

1. Geben Sie einen **Verbindungsnamen** ein (z. B. _Produktionsinstanz_) — optional, aber hilfreich, wenn Sie mehrere Verbindungen verwenden.
2. Wählen Sie die **Authentifizierungsmethode**, wenn der Konnektor mehrere Optionen unterstützt: **Basic (Zugangsdaten / API-Schlüssel)** oder **OAuth**.
3. Füllen Sie die vom Konnektor benötigten Felder aus (Instanz-URL, API-Token usw.).
4. Klicken Sie auf **Verbinden** — oder bei OAuth auf **Speichern und verbinden**. Sie werden anschließend zum externen Tool weitergeleitet, um Dastra zu autorisieren.

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### Einen Anwendungsfall installieren

Klicken Sie auf der Karte eines Anwendungsfalls auf **Integration hinzufügen**. Das Installationsfenster führt Sie durch maximal drei Schritte:

1. **Verbindung** — wählen Sie eine bestehende Verbindung aus oder erstellen Sie direkt über die Liste eine neue.
2. **Konfiguration** — die konnektorspezifischen Einstellungen (Synchronisierungsoptionen, Feld-Mapping usw.). Dieser Schritt wird freigeschaltet, sobald eine gültige Verbindung ausgewählt wurde.
3. **Webhook** — nur für Konnektoren, die Ereignisse von einem externen Tool empfangen (z. B. Jira). Dieser Schritt wird nach dem Speichern der Konfiguration freigeschaltet.

Nach der Installation bietet die Karte des Anwendungsfalls folgende Optionen:

* einen Schalter **Aktivieren**,
* den Eintrag **Konfiguration**, um die Einstellungen erneut zu öffnen,
* **Synchronisierung starten** (nur bei Import-Konnektoren), um eine sofortige Synchronisierung auszulösen,
* **Protokolle anzeigen**, um vergangene Ausführungen einzusehen,
* **Deinstallieren**.

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Durch die Deinstallation eines Anwendungsfalls werden die zugehörigen Zugangsdaten gelöscht. Assets, Anfragen und andere von der Integration erstellte Datensätze bleiben erhalten — sie gehören zu Ihrem Workspace.

### Das Feld-Mapping

Import-Anwendungsfälle enthalten einen Abschnitt **Feld-Mapping**: Wählen Sie für jedes Dastra-Feld das Feld des externen Tools aus, das bei der Synchronisierung als Quelle dient. Ein Feld ohne zugewiesene Quelle behält sein **Standardverhalten** bei.

* Pflichtfelder in Dastra sind mit einem roten Sternchen gekennzeichnet. Die Konfiguration kann nicht gespeichert werden, solange ein Pflichtfeld weder eine Quelle noch einen Standardwert hat.
* Mit **Feld zuordnen** können Sie für jedes weitere Dastra-Feld eine zusätzliche Zeile hinzufügen, einschließlich Ihrer benutzerdefinierten Felder.
* Die Liste der Quellfelder wird, wenn möglich, live aus dem externen Tool abgerufen. Dadurch werden auch Ihre benutzerdefinierten Attribute auf der Quellseite angezeigt.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

### **Erweiterte Optionen**

Für jede Zeile steht ein Bereich **Erweitert** mit zwei Optionen zur Verfügung:

* **Standardwert** — wird verwendet, wenn kein Quellfeld vorhanden ist, oder als Fallback für Quellwerte, die nicht transkodiert wurden. Bei Datumsfeldern können Sie **Heute** oder ein relatives Datum auswählen (z. B. _in 30 Tagen_), das zum Zeitpunkt der Erstellung des Datensatzes aufgelöst wird.
* **Wertetranscodierung** — für geschlossene Listen (Status, Lebenszyklusphasen usw.): Ordnen Sie jedem Quellwert einen Dastra-Wert zu. Nicht zugeordnete Werte übernehmen den Standardwert.

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

Bei Datumsfeldern kann der Standardwert dynamisch sein — er wird zum Zeitpunkt der Erstellung des Datensatzes aufgelöst:

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

<sub>Ein relativer Standardwert für das Datum (hier: in 30 Tagen) für die Fälligkeit der Anfrage</sub>

#### **KI-Vorschläge**

Wenn der KI-Assistent für Ihr Konto aktiviert ist, schlägt die Schaltfläche **Von KI vorschlagen lassen** ein vollständiges Mapping vor. Zusätzlich verfügt jede Zeile über eine eigene Schaltfläche für Vorschläge. Bereits zugeordnete Felder werden dabei niemals überschrieben, und alle Vorschläge werden Ihnen vor dem Speichern zur Überprüfung angezeigt.

### Synchronisierung und Protokolle

* Import-Konnektoren (ServiceNow, SAP LeanIX, Filerskeepers) synchronisieren **täglich**. Sie können außerdem jederzeit über **Synchronisierung starten** eine Synchronisierung manuell auslösen.
* **Protokolle anzeigen** zeigt jede Ausführung mit ihrem Ergebnis und den zugehörigen Zählern: erstellte, aktualisierte, markierte und fehlerhafte Elemente sowie gegebenenfalls die Details zum jeweiligen Fehler.

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
