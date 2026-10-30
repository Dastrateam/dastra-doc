---
description: 'SAP LeanIX-Integration: Anwendungen als Assets mit Dastra synchronisieren'
---

# SAP LeanIX

### Was ist SAP LeanIX?

[SAP LeanIX](https://www.leanix.net/) ist eine Plattform für Enterprise Architecture Management. Unternehmen nutzen sie, um ihre Anwendungslandschaft in Form von _Fact Sheets_ zu erfassen und zu verwalten.

### Was macht die Integration?

Die Integration **importiert Ihre SAP LeanIX Application Fact Sheets in das Asset-Verzeichnis von Dastra und hält sie synchron**:

* Jede LeanIX-Anwendung wird zu einem **Asset** in Ihrem Mandanten oder aktualisiert ein bereits vorhandenes Asset.
* Die Synchronisierung erfolgt **täglich** und kann jederzeit manuell ausgelöst werden.
* Bestehende Assets werden aktualisiert und nicht dupliziert: Die Zuordnung erfolgt anhand der ID des LeanIX Fact Sheets und optional anhand eines von Ihnen gewählten Feldes (siehe Deduplizierung weiter unten).
* Die Integration löscht niemals Assets — Anwendungen, die nicht mehr in LeanIX vorhanden sind, werden lediglich mit einem Tag gekennzeichnet.

### Voraussetzungen

* Die **URL Ihrer SAP LeanIX-Instanz**, z. B. `https://ihr-unternehmen.leanix.net`.
* Ein **API-Token** eines LeanIX-_Technical Users_, der von Ihrem LeanIX-Administrator erstellt wurde.

{% hint style="warning" %}
Verwenden Sie die Root-URL Ihrer LeanIX-Instanz ohne Workspace-Pfad (z. B. `https://ihr-unternehmen.leanix.net` und nicht `https://ihr-unternehmen.leanix.net/MeinWorkspace`).
{% endhint %}

### Installation

1. Öffnen Sie **Mandanteneinstellungen** > **Integrationen** und wählen Sie **SAP LeanIX** aus.
2. Klicken Sie beim Anwendungsfall für den Import von Anwendungen auf **Integration hinzufügen**.
3. Fügen Sie eine Verbindung hinzu: Geben Sie einen **Verbindungsnamen**, die **Instanz-URL** und das **API-Token** ein und klicken Sie anschließend auf **Verbinden**. Dastra validiert das Token bei Ihrer Instanz.

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### Konfiguration

Im Konfigurationsschritt legen Sie fest, wie Anwendungen importiert werden:

* **Bei Fehlern zu benachrichtigende Benutzer (erforderlich)**: Diese Benutzer erhalten eine E-Mail, wenn eine Synchronisierung fehlschlägt.
* **Dastra-Eintrag erstellen, falls nicht vorhanden**: Ist diese Option deaktiviert, werden nur bereits vorhandene Assets aktualisiert.
* **Synchronisierte Elemente deduplizieren**: Eingehende Anwendungen werden anhand eines **Abgleichfelds** (Bezeichnung oder Referenz) bestehenden Assets zugeordnet und aktualisiert, anstatt Duplikate zu erzeugen.
* **Feldzuordnung (Mapping)**: Legen Sie fest, welches LeanIX-Feld welches Dastra-Feld befüllt (siehe [Verbindungen, Anwendungsfälle und Feld-Mapping](connections.md)).

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

#### Besonderheiten des Mappings

* Die Liste der Quellfelder wird direkt aus Ihrem **LeanIX-Datenmodell** übernommen. Auch Ihre benutzerdefinierten Attribute stehen zur Verfügung, einschließlich ihrer möglichen Werte für die Transkodierung (Wertemapping).
*   Das Standard-Mapping funktioniert ohne zusätzliche Konfiguration:

    * **Display name** → **Bezeichnung**
    * **Description** → **Beschreibung**
    * **Lifecycle** → **Anwendungsstatus**

    Dabei ist bereits eine Standard-Transkodierung hinterlegt:

    * **plan** / **phase-in** → _In Entwicklung_
    * **active** → _In Produktion_
    * **phase-out** / **end-of-life** → _Außer Betrieb_

    Diese Zuordnung kann im Bereich **Erweitert** angepasst werden.
* Sie können jedes beliebige LeanIX-Feld (beispielsweise eine interne Anwendungskennung) auf das Feld **Referenz** des Assets abbilden. Dadurch wird die Kennung in Dastra durchsuchbar und kann gleichzeitig als **Abgleichfeld** für die Deduplizierung verwendet werden.

### Wie werden die Daten synchronisiert?

Die Synchronisierung wird automatisch **einmal täglich** ausgeführt.

Sie können sie außerdem jederzeit manuell starten, indem Sie auf der Karte des Anwendungsfalls **Synchronisierung starten** auswählen. Über **Protokolle anzeigen** können Sie die Synchronisierungsläufe nachverfolgen, einschließlich:

* Anzahl der erstellten Elemente
* Anzahl der aktualisierten Elemente
* Anzahl der markierten Elemente
* Details zu aufgetretenen Fehlern

#### Gelöschte Anwendungen in SAP LeanIX

Wenn ein zuvor importiertes Asset in LeanIX nicht mehr vorhanden ist, wird es von Dastra **nicht gelöscht**. Stattdessen wird das Tag **To-delete-sap-leanix** hinzugefügt, damit Sie das Asset prüfen und über das weitere Vorgehen entscheiden können.

Erscheint das entsprechende Fact Sheet später erneut in LeanIX, wird dieses Tag automatisch entfernt.

#### Erkannte Duplikate

Wenn die Deduplizierung mehrere bestehende Assets findet, die derselben eingehenden Anwendung entsprechen könnten, werden diese Kandidaten mit dem Tag **To-merge-sap-leanix** versehen. Die Entscheidung über eine Zusammenführung erfolgt anschließend manuell.

#### Deinstallation der Integration

{% hint style="info" %}
Die importierten Assets bleiben Bestandteil Ihres Mandanten. Bei einer Deinstallation der Integration werden sie **nicht entfernt** und bleiben einschließlich ihrer Tags unverändert erhalten.
{% endhint %}
