# Wie funktioniert es?

### Modelle und Hosting

Dastra verwendet vortrainierte generative KI-Modelle, die in vier Familien zur Auswahl stehen:

| Familie                                | Konfigurierte Modelle                                                                | Hosting                     |
| -------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------- |
| **OpenAI** _(standardmäßig empfohlen)_ | Fast: gpt-4o-nano · Smart: gpt-5-mini · Large context: gpt-4.1-mini                  | Azure, Frankreich / EWR     |
| **Mistral**                            | Fast: mistral-small-2503 · Smart: Mistral-Large-3 · Large context: Mistral-Large-3   | Azure, Frankreich / EWR     |
| **Open Source**                        | Fast: Ministral-3B · Smart: DeepSeek-V3.2 · Large context: Llama-4-Maverick-17B-128K | Azure, Frankreich / EWR     |
| **Custom AI Provider**                 | Ihr eigener Anbieter per API-Schlüssel _(siehe unten)_                               | Je nach Ihrer Konfiguration |

Für die ersten drei Familien werden die Modelle auf der Microsoft Azure-Infrastruktur in Frankreich gehostet. Sie werden nicht direkt von OpenAI oder Mistral betrieben: Dastra nutzt die verwalteten Azure-Dienste, was bedeutet, dass **Ihre Daten nicht an die eigene Infrastruktur von OpenAI oder Mistral übertragen werden**.

Für jede Familie werden drei Modellstufen je nach Komplexität der Aufgabe verwendet:

* **Fast** (einfache Aktionen): Generierung von Beschreibungen, Tag-Vorschläge
* **Smart** (Aktionen, die mehr Überlegung erfordern): Generierung strukturierter Elemente in Dastra
* **Erweiterter Kontext** (Aktionen, die ein großes Datenvolumen verarbeiten): Beantwortung eines Fragebogens, Compliance-Analyse

Sie können die verwendete Modellfamilie in den **Einstellungen Ihrer Organisation > KI-Assistent** konfigurieren.

***

### Custom AI Provider

Dastra ermöglicht es Ihnen, Ihren eigenen KI-Anbieter über einen API-Schlüssel zu verbinden, sofern dieser mit dem OpenAI-API-Standard kompatibel ist. Unterstützte Anbieter umfassen insbesondere OpenAI, Google (Gemini), Mistral, Microsoft Foundry sowie jedes selbst gehostete kompatible LLM.

Um einen benutzerdefinierten Anbieter zu konfigurieren, gehen Sie zu **Einstellungen > KI-Assistent > Custom AI Provider** und geben Sie Ihre Anmeldedaten ein und ordnen Sie sie den drei Modellstufen zu (Fast, Smart, Erweiterter Kontext).

{% hint style="warning" %}
Wenn Sie einen Custom AI Provider verwenden, unterliegen die an das Modell übermittelten Daten der Datenschutzrichtlinie **Ihres Anbieters** und nicht den auf dieser Seite beschriebenen Azure-Garantien. Überprüfen Sie die Bedingungen Ihres Anbieters, bevor Sie diese Option aktivieren, insbesondere wenn Ihre Prompts personenbezogene Daten enthalten können.
{% endhint %}

***

### Was Dastra an das Modell sendet

Dastra übermittelt nur die für die angeforderte Generierung erforderlichen Informationen: den vom Nutzer eingegebenen Text und gegebenenfalls die strukturierten Felder des betreffenden Objekts (Verarbeitung, KI-System, Betroffenenanfrage usw.).

Die genauen Details der pro Funktion übermittelten Daten sind im Abschnitt "Welche Daten werden übermittelt?" verfügbar.

***

### Was Dastra nicht tut

Die folgenden Punkte sind vertraglich durch Microsoft Azure für alle Modelle der Familien OpenAI, Mistral und Open Source garantiert:

* Ihre Prompts und Ergebnisse **sind nicht verfügbar** für andere Azure-Kunden
* Ihre Daten **werden nicht übertragen** an OpenAI, Mistral oder Dritte
* Ihre Daten **werden nicht verwendet**, um die Basismodelle zu trainieren oder zu verbessern
* Die Modelle sind **zustandslos (stateless)**: Kein Prompt wird zwischen zwei Anfragen im Modell gespeichert

***

### Missbrauchsüberwachung und menschliche Überprüfung

Microsoft Azure unterhält einen automatisierten Mechanismus zur Erkennung potenziell missbräuchlicher Inhalte. In den seltenen Fällen, in denen ein Inhalt gemeldet wird, kann eine Stichprobe von Prompts vorübergehend in einem kundenspezifisch isolierten Speicherbereich zur Überprüfung aufbewahrt werden. Für Ressourcen, die im EWR bereitgestellt werden (was bei Dastra der Fall ist), befinden sich auch die menschlichen Prüfer im EWR.

Diese Aufbewahrung ist außergewöhnlich und betrifft nicht die normale Nutzung der Plattform. Weitere Einzelheiten finden Sie in der [Microsoft-Dokumentation zu Daten, Datenschutz und Sicherheit für Modelle, die von Azure in Microsoft Foundry verkauft werden](https://learn.microsoft.com/de-de/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal).

***

### KI-Aufrufprotokolle

Dastra speichert einen Verlauf der Aufrufe an den KI-Assistenten für die **letzten 90 Tage**, zugänglich über **Einstellungen > KI-Assistent > Ausführungsprotokolle des KI-Assistenten (90 Tage)**. Für jeden Aufruf werden folgende Informationen aufgezeichnet:

| Feld          | Beschreibung                                          |
| ------------- | ----------------------------------------------------- |
| **Datum**     | Zeitstempel des Aufrufs                               |
| **Status**    | Erfolg oder Fehler der Generierung                    |
| **Operation** | Art des verwendeten Prompts                           |
| **Modell**    | Name des verwendeten Modells                          |
| **Dauer**     | Verarbeitungszeit der Anfrage                         |
| **Nutzer**    | Workspace-Mitglied, das die Generierung ausgelöst hat |

### Welche Daten werden an das Modell übermittelt?

{% hint style="info" %}
Dastra übermittelt **keine Daten Ihres Workspace** an das KI-Modell, ohne dass Sie die Ursache dafür sind. Nur die unten aufgeführten Informationen werden je nach verwendeter Funktion in die an das Modell gesendete Anfrage aufgenommen.
{% endhint %}

| Funktion                                              | An das Modell übermittelte Daten                                                                                                                                                     | Potenziell personenbezogene Daten                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Verarbeitung generieren**                           | Vom Nutzer eingegebener Freitext                                                                                                                                                     | Nein — es sei denn, der Nutzer erwähnt Personen in seiner Beschreibung |
| **Asset generieren**                                  | Freitext + URL der bereitgestellten Datenschutzrichtlinie                                                                                                                            | Nein                                                                   |
| **Stakeholder generieren**                            | Freitext + URL oder bereitgestellter Anhang                                                                                                                                          | Nein                                                                   |
| **Datensatz generieren**                              | Vom Nutzer eingegebener Freitext                                                                                                                                                     | Nein                                                                   |
| **Sicherheitsmaßnahme generieren**                    | Vom Nutzer eingegebener Freitext                                                                                                                                                     | Nein                                                                   |
| **Datenschutzerklärung generieren**                   | Strukturierte Felder der Verarbeitung (Zwecke, Rechtsgrundlage, Fristen, Empfänger, Rechte)                                                                                          | Potenziell — wenn die Felder namentliche Verweise enthalten            |
| **Beschreibung generieren**                           | Vom Nutzer eingegebener Freitext                                                                                                                                                     | Nein                                                                   |
| **Tags vorschlagen**                                  | Textinhalt des Objekts (Name, Beschreibung)                                                                                                                                          | Nein                                                                   |
| **Fragebogenvorlage generieren**                      | Vom Nutzer eingegebener Freitext                                                                                                                                                     | Nein                                                                   |
| **Fragebogen beantworten (DSFA, Risikoanalyse...)**   | Strukturierte Felder der zugehörigen Verarbeitung + eventuelle benutzerdefinierte Anweisungen                                                                                        | Potenziell — je nach Inhalt der Verarbeitung                           |
| **Antwort auf eine Betroffenenanfrage generieren**    | Vor- und Nachname des Antragstellers, Nachricht der Anfrage, Sprache, Name des Workspace, Zwecke, Name des Bearbeiters, Datum und verbleibende Frist, Status und Kennung der Anfrage | **Ja** — Name, Vorname und Inhalt der Anfrage                          |
| **Post-Mortem eines Datenschutzvorfalls generieren**  | Strukturierte Felder des Vorfalls (Beschreibung, betroffene Daten, ergriffene Maßnahmen)                                                                                             | Potenziell — je nach Inhalt des Datenschutzvorfalls                    |
| **Metadaten eines Vertrags extrahieren**              | Textinhalt des übermittelten Dokuments (Anhang oder URL)                                                                                                                             | Potenziell — je nach Vertragsinhalt                                    |
| **Benutzerdefiniertes Dokument generieren**           | Vom Nutzer eingegebene Anweisungen + eventueller Quellinhalt                                                                                                                         | Potenziell — je nach gegebenen Anweisungen                             |
| **Benutzerdefinierten Bericht generieren**            | Vom Nutzer eingegebene Anweisungen                                                                                                                                                   | Nein — es sei denn, der Nutzer fügt Daten in seine Anweisungen ein     |
| **Risikoanalyse (KI-System)**                         | Strukturierte Felder des KI-Systems (Beschreibung, Zwecke, verarbeitete Daten, Interessengruppen)                                                                                    | Potenziell — je nach Inhalt des KI-Systems                             |
| **Beschreibung eines KI-Systems generieren**          | Freitext + URL oder bereitgestellter Anhang                                                                                                                                          | Nein                                                                   |
| **KI-System-Hinweis generieren**                      | Strukturierte Felder des betreffenden KI-Systems                                                                                                                                     | Potenziell                                                             |
| **Vorschläge für Kontrollen / Anforderungen / Tests** | Kontext des betreffenden Objekts (Name, Beschreibung, Referenzrahmen)                                                                                                                | Nein                                                                   |

{% hint style="warning" %}
**Bewährte Praxis**: Vermeiden Sie es, personenbezogene Daten direkt in Freitextfelder (Beschreibungen, benutzerdefinierte Anweisungen) einzugeben. Verwenden Sie nach Möglichkeit Kennungen oder allgemeine Begriffe.
{% endhint %}

#### Daten, die niemals übermittelt werden

Die folgenden Elemente sind **niemals** Teil der an das KI-Modell gesendeten Anfragen:

* Kennungen und Passwörter der Dastra-Nutzer
* Daten anderer Datensätze Ihres Workspace (nur das Objekt, an dem Sie arbeiten, ist betroffen)
* Sitzungsmetadaten (Name des angemeldeten Nutzers, IP-Adresse usw.)
* Anhänge, die nicht explizit in der betreffenden Funktion bereitgestellt wurden

#### Aufbewahrungsdauer der Anfragen

Die von Dastra verwendeten Azure-Modelle sind **zustandslos (stateless)**: Die Prompts und Ergebnisse werden nicht im Modell gespeichert und nicht zum erneuten Training oder zur Verbesserung der Basismodelle verwendet.

{% hint style="info" %}
**Ausnahme — Missbrauchserkennung**: Microsoft Azure unterhält einen automatisierten Mechanismus zur Überwachung potenziell missbräuchlicher Inhalte. Wenn ein Prompt gemeldet wird, kann eine Stichprobe vorübergehend in einem kundenspezifisch isolierten Speicherbereich zur Überprüfung aufbewahrt werden. Für Ressourcen, die im EWR bereitgestellt werden (was bei Dastra der Fall ist), befinden sich die menschlichen Prüfer ebenfalls im EWR. Diese Aufbewahrung ist außergewöhnlich und betrifft nicht die normale Nutzung der Plattform.
{% endhint %}

Weitere Informationen finden Sie in der [Microsoft-Dokumentation zu Daten, Datenschutz und Sicherheit für Modelle, die von Azure in Microsoft Foundry verkauft werden](https://learn.microsoft.com/de-de/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal).
