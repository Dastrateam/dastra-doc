---
description: >-
  Verbinden Sie Claude, ChatGPT, Copilot, Cursor oder Ihr Terminal über den
  MCP-Server mit Ihren Dastra-Daten
---

# Der MCP-Server

Der MCP-Server (**Model Context Protocol**) ermöglicht es Ihrem KI-Assistenten, Ihrem Code-Editor oder Ihrem Terminal, mit Ihren Dastra-Daten zu arbeiten: Einträge suchen, Entitäten erstellen, Felder aktualisieren und mehr.

Anders gesagt: Statt in Dastra zu arbeiten, bitten Sie das Tool, das Sie ohnehin nutzen (Claude, ChatGPT, Microsoft Copilot, Le Chat, Cursor und andere), dies für Sie zu tun.

Alles konfigurieren Sie unter **Organisationseinstellungen** > **API-Schlüssel & MCP** > **MCP Server** ([direkter Zugriff](https://app.dastra.eu/general-settings/api)).

<figure><img src="../../../.gitbook/assets/mcp-panneau.png" alt="Tab MCP Server in den Organisationseinstellungen"><figcaption><p>Organisationseinstellungen &#x3E; API-Schlüssel &#x26; MCP &#x3E; MCP Server</p></figcaption></figure>

***

## Bevor Sie beginnen

{% hint style="warning" %}
**Drei Voraussetzungen müssen erfüllt sein:**

* Der MCP-Server gehört zum Tarif **Dastra AI Pro**. Ist er in Ihrem Abonnement nicht enthalten, bleibt der Tab sichtbar, aber die Verbindung wird abgelehnt.
* Nur ein **Kontoinhaber** kann ein KI-Tool verbinden.
* **Jede Verbindung ist auf einen einzigen Mandanten beschränkt**: den, der bei der Freigabe der Anmeldung gewählt wird, oder den, an den der API-Schlüssel gebunden ist. Um an zwei Mandanten zu arbeiten, legen Sie zwei Verbindungen an.
{% endhint %}

## Server-URL

Richten Sie Ihren Client auf die im Bereich angezeigte URL aus:

```
https://api.dastra.eu/mcp
```

Der Transport ist **HTTP** (Streaming). Sie müssen lokal nichts installieren: Es handelt sich nicht um einen `stdio`-Server.

{% hint style="info" %}
Wenn Ihre Organisation auf der souveränen Infrastruktur gehostet wird, lautet die URL `https://api-bleu.dastra.eu/mcp`. Verwenden Sie immer die URL aus Ihrem eigenen Bereich, statt sie von dieser Seite zu kopieren.
{% endhint %}

***

## Eine Verbindungsmethode wählen

Zwei Methoden funktionieren, und der Bereich zeigt für jedes Tool beide nebeneinander.

### Anmeldung im Browser (empfohlen)

Ihr Tool registriert sich selbst bei Dastra und öffnet ein Browserfenster, in dem Sie sich anmelden und den **Mandanten wählen**, auf den es zugreifen darf.

Diese Methode sollten Sie bevorzugen: Sie müssen keinen Schlüssel erstellen, kopieren oder aufbewahren, und Sie können den Zugriff jederzeit widerrufen.

### API-Schlüssel

Reserviert für Automatisierungen und Umgebungen ohne Browser. Sie fügen der Konfiguration des Konnektors einen HTTP-Header hinzu:

| Name des Headers | Wert |
| --- | --- |
| `X-API-Key` | Der private Schlüssel Ihres API-Schlüssels |

{% hint style="danger" %}
**Der API-Schlüssel muss an einen Mandanten gebunden sein**, sonst wird die MCP-Verbindung abgelehnt. Füllen Sie beim Erstellen des Schlüssels im Tab **API keys** das Feld **Auswahl eines bestimmten Mandanten** aus. Geeignete Schlüssel tragen in der Liste das Badge `MCP`.
{% endhint %}

<figure><img src="../../../.gitbook/assets/mcp-cle-api-workspace.png" alt="Erstellung eines API-Schlüssels mit der Auswahl des Mandanten"><figcaption><p>Das Feld „Auswahl eines bestimmten Mandanten“ macht einen Schlüssel für MCP nutzbar</p></figcaption></figure>

Das allgemeine Vorgehen zum Erstellen eines Schlüssels ist unter [API-Schlüssel verwalten](../../settings/api-keys.md) beschrieben.

***

## Ihr Tool verbinden

Der Bereich **Einen KI-Assistenten verbinden** hat für jedes Tool einen eigenen Tab mit den genauen Schritten und den zu kopierenden Werten. Hier das Wesentliche.

{% tabs %}
{% tab title="Claude" %}
Konnektoren werden in Ihrem Claude-Konto eingerichtet, die Schritte sind also auf claude.ai und in der Desktop-App dieselben.

1. Öffnen Sie im Profilmenü **Settings** und wechseln Sie dann zum Tab **Connectors**.
2. Klicken Sie auf **Add custom connector**.
3. Fügen Sie die Server-URL ein und fügen Sie dann den Konnektor hinzu.
4. Klicken Sie auf **Connect** und melden Sie sich im sich öffnenden Fenster bei Dastra an.

Um zu prüfen, ob es funktioniert hat, starten Sie eine neue Unterhaltung und öffnen Sie das Tool-Menü im Nachrichtenfeld: Die Dastra-Tools sollten aufgelistet sein.

Bei einer Verbindung mit API-Schlüssel gehen Sie genauso vor, öffnen dann die **erweiterten Einstellungen** des Konnektors und fügen den Header `X-API-Key` hinzu.
{% endtab %}

{% tab title="Claude Code" %}
Registrieren Sie den Server mit dem folgenden Befehl, starten Sie dann Claude Code und geben Sie `/mcp` ein, um die Verbindung abzuschließen:

```bash
claude mcp add --transport http dastra https://api.dastra.eu/mcp
```

Mit einem API-Schlüssel ist keine interaktive Anmeldung nötig:

```bash
claude mcp add --transport http dastra https://api.dastra.eu/mcp \
  --header "X-API-Key: YOUR_API_KEY"
```
{% endtab %}

{% tab title="Cursor" %}
Fügen Sie den Server in `~/.cursor/mcp.json` hinzu:

```json
{
  "mcpServers": {
    "dastra": {
      "url": "https://api.dastra.eu/mcp"
    }
  }
}
```
{% endtab %}

{% tab title="VS Code" %}
Fügen Sie den Server in `.vscode/mcp.json` hinzu:

```json
{
  "servers": {
    "dastra": {
      "type": "http",
      "url": "https://api.dastra.eu/mcp"
    }
  }
}
```
{% endtab %}

{% tab title="Andere Tools" %}
**ChatGPT** und **Microsoft Copilot** haben jeweils einen eigenen Einrichtungsassistenten: Folgen Sie den Schritten des passenden Tabs im Dastra-Bereich. Copilot Studio verwendet die OAuth-2.0-Option **Dynamic discovery**, die genau dem Anmeldemodus über den Browser von Dastra entspricht.

**Mistral (Le Chat)** unterstützt nur die **Anmeldung im Browser**: Dieses Tool sendet keinen `X-API-Key`-Header, die Methode mit API-Schlüssel funktioniert daher nicht.

Für jeden anderen MCP-kompatiblen Client verwenden Sie den Tab **Other**: Er nennt die Server-URL und den zu setzenden Header.
{% endtab %}
{% endtabs %}

***

## Was Ihr Tool tun kann

Nach der Verbindung stehen Ihrem Tool etwa dreißig Dastra-Tools zur Verfügung.

### Lese-Tools

| Tool | Was es tut |
| --- | --- |
| Den Mandanten durchsuchen | Breite Suche über alle Eintragstypen, der übliche Ausgangspunkt |
| Einträge durchsuchen | Listet und filtert die Einträge eines bestimmten Typs |
| Einen Eintrag lesen | Ruft einen Eintrag nach Typ und Kennung ab |
| Die Struktur eines Eintrags prüfen | Beschreibt die Felder und Spalten eines Eintragstyps |
| Bearbeitbare Felder prüfen | Gibt an, welche Felder aktualisiert werden können und in welchem Format |
| Kommentare lesen | Listet die Kommentare eines Eintrags auf |
| Dateien lesen | Listet die Dateien des Mandanten oder eines Eintrags auf |
| Eine Datei lesen | Extrahiert den Text einer PDF-, DOCX-, XLSX-, HTML-, TXT-, CSV-, JSON- oder Markdown-Datei |
| Einen Fragebogen lesen | Ruft eine Audit-Vorlage oder einen geplanten Fragebogen mit seinen Fragen ab |
| Organisationseinheiten lesen | Liefert die Hierarchie der Entitäten und Abteilungen |
| Nutzer auflisten | Listet die Mitglieder des Mandanten auf |
| Tags auflisten | Listet Tags auf, optional nach Typ gefiltert |
| Workflow-Schritte auflisten | Listet die für einen Eintragstyp konfigurierten Schritte auf |
| Rechtsvorschriften prüfen | Fragt das von Dastra indexierte Regelwerk ab (DSGVO, NIS2, DORA, ISO 27001 und weitere), mit zitierten Quellen |
| Kategorien von Rechtsvorschriften auflisten | Liefert die Kategorien, die für die Suche in Rechtsvorschriften genutzt werden können |
| Die Dokumentation durchsuchen | Durchsucht die Dastra-Dokumentation |
| Im Web suchen | Öffentliche Websuche, als letzter Ausweg |
| Den Eintrag analysieren | Erstellt eine Compliance-Analyse mit Bewertung von A bis F und Verbesserungsvorschlägen |
| Links zu Einträgen | Erzeugt anklickbare URLs der Dastra-Webanwendung für Einträge |

### Bearbeitungstools

| Tool | Was es tut |
| --- | --- |
| Einen Eintrag erstellen | Erstellt einen leeren Eintrag |
| Einen Eintrag entwerfen | Erzeugt aus einer Beschreibung einen vollständigen Eintrag und importiert ihn |
| Einträge aktualisieren | Aktualisiert bis zu 50 Einträge auf einmal |
| Den Workflow-Status ändern | Verschiebt einen Eintrag in eine andere Phase |
| Einen Kommentar hinzufügen | Kommentiert einen Eintrag, einschließlich Erwähnungen |
| Einen Maßnahmenplan erstellen | Erstellt bis zu 10 Aufgaben, die mit einem Eintrag verknüpft sind |
| Einen Tag erstellen | Erstellt einen Tag für einen Eintragstyp |
| Ein Dokument schreiben | Erstellt oder aktualisiert ein Markdown-Dokument im Dateimanager |
| Eine Datei verknüpfen | Hängt eine vorhandene Datei an einen Eintrag an |
| Einen Fragebogen planen | Erstellt aus einer Vorlage einen Fragebogen und weist ihn zu |
| Einen Fragebogen aktualisieren | Füllt die Antworten eines geplanten Fragebogens aus |

{% hint style="info" %}
Der MCP-Server stellt **nur Tools** bereit. Er veröffentlicht weder *Resources* noch *Prompts* im Sinne des Protokolls: Ein Client, der `resources/list` oder `prompts/list` abfragt, erhält eine leere Liste.
{% endhint %}

***

## Sicherheit

**Ihr Tool hat nie mehr Rechte als Sie.** Der MCP-Server hat kein Dienstkonto: Er leitet Ihren eigenen Schlüssel oder Ihr eigenes Token an die Dastra-API weiter. Jeder Lese- und Schreibzugriff unterliegt daher den üblichen Berechtigungen des Nutzers oder des API-Schlüssels.

Einige Punkte, die Sie kennen sollten:

* **Geltungsbereich**: Eine Verbindung sieht nur einen Mandanten in einer Organisation.
* **Nachvollziehbarkeit**: Schreibzugriffe über MCP werden als von einem KI-Agenten stammend gekennzeichnet. Das Datum der letzten Verwendung jedes Schlüssels sehen Sie in der Liste der API-Schlüssel.
* **Widerruf**: Eine im Browser freigegebene Verbindung wird zu einem gewöhnlichen API-Schlüssel, der im Tab **API keys** sichtbar ist und widerrufen werden kann. Löschen Sie den Schlüssel, ist der Zugriff sofort gesperrt.
* **Ratenbegrenzung**: Aufrufe sind auf 60 Anfragen pro Minute am MCP-Server und auf 120 Anfragen pro Minute über alle Nutzungen hinweg begrenzt. Darüber hinaus antwortet der Server mit einem Fehler `429` und nennt die Wartezeit.

{% hint style="warning" %}
Ein für MCP verwendeter API-Schlüssel gewährt Lese- **und Schreibzugriff** auf einen ganzen Mandanten. Behandeln Sie ihn wie ein Passwort: Veröffentlichen Sie ihn nie und widerrufen Sie ihn bei der geringsten Unsicherheit.
{% endhint %}

***

## Fehlerbehebung

| Symptom | Wahrscheinliche Ursache |
| --- | --- |
| Die Verbindung wird mit einer Meldung zum Abonnement abgelehnt | Der MCP-Server ist in Ihrem Tarif nicht enthalten: Er erfordert Dastra AI Pro |
| „API key must be bound to a specific workspace“ | Der Schlüssel wurde ohne Mandant erstellt: Erstellen Sie einen neuen und füllen Sie dieses Feld aus |
| In Ihrem Client erscheint kein Dastra-Tool | Die Verbindung wurde nicht abgeschlossen. Öffnen Sie in Claude den Konnektor und klicken Sie auf **Connect**, geben Sie in Claude Code `/mcp` ein |
| Le Chat lehnt den API-Schlüssel ab | Das ist erwartet: Le Chat unterstützt nur die Anmeldung im Browser |
| Sie müssen sich ständig neu anmelden | Der langlebige Zugriff wurde nicht gewährt: Entfernen Sie den Konnektor und verbinden Sie ihn erneut |
| Fehler `429` | Sie haben die Ratenbegrenzung überschritten: Versuchen Sie es nach der genannten Wartezeit erneut |

***

{% content-ref url="agents/README.md" %}
[Dastra-KI-Agenten](agents/README.md)
{% endcontent-ref %}
