---
description: >-
  Dastra werkt samen met al uw hulpmiddelen.
---

# Integraties

## Integraties

Dastra koppelt aan de hulpmiddelen die uw teams al gebruiken: u importeert uw applicatie-inventaris uit uw ITAM of CMDB, synchroniseert verzoeken van betrokkenen met uw ticketingtool, plaatst meldingen in uw samenwerkingskanalen, stuurt uw beveiligingsauditlogs door naar uw SIEM of voegt bestanden toe vanuit uw clouddrives. Native connectoren dekken de meest gebruikte tools, Zapier dekt de rest.

De integratiestore vindt u onder **Instellingen voor werkruimte** > **Integraties** in uw werkruimte. Ze toont alle beschikbare integraties, te filteren op categorie en op het Dastra-object waarop ze betrekking hebben, met de tabbladen **Alles** en **Geïnstalleerd**.

### Hoe native integraties werken

Elke native integratie is opgebouwd uit drie begrippen:

* Gebruiksscenario's: elke integratie biedt een of meer gebruiksscenario's (bijvoorbeeld applicaties importeren als activa of verzoeken van betrokkenen synchroniseren). U installeert, activeert, configureert en verwijdert elk gebruiksscenario afzonderlijk.
* Verbindingen: een verbinding legt vast hoe Dastra zich bij de externe tool authenticeert, met inloggegevens die Dastra versleuteld opslaat of met een gedelegeerde OAuth-autorisatie. U kunt meerdere verbindingen met dezelfde tool aanmaken (bijvoorbeeld een productie-instantie en een sandbox) en kiezen welke verbinding elk gebruiksscenario gebruikt. Verbindingen tonen hun status en u kunt ze op elk moment testen.
* Veldmapping: bij importgebruiksscenario's kiest u voor elk Dastra-veld het externe veld dat het vult, met standaardwaarden, transcodering van waarden voor gesloten lijsten (statussen, levenscyclusfasen enzovoort) en suggesties van de AI-assistent.

Importconnectoren synchroniseren één keer per dag en op aanvraag met **Synchronisatie starten**. Elke uitvoering wordt vastgelegd in de integratielogs, met het aantal aangemaakte, bijgewerkte, gemarkeerde en foutieve items.

<figure><img src="../../.gitbook/assets/integrations-catalog.png" alt="De integratiestore met de lijst van beschikbare integraties"><figcaption><p>De integratiestore</p></figcaption></figure>

De details leest u in [Verbindingen, gebruiksscenario's en veldmapping](connections.md).

### Beschikbare integraties

| Integratie | Wat ze doet | Documentatie |
| --- | --- | --- |
| ServiceNow | Importeert de bedrijfsapplicaties uit uw CMDB als activa en houdt ze dagelijks gesynchroniseerd | [ServiceNow](servicenow.md) |
| SAP LeanIX | Importeert uw Application-factsheets als activa en houdt ze dagelijks gesynchroniseerd | [SAP LeanIX](sap-leanix.md) |
| Jira | Maakt verzoeken van betrokkenen aan en volgt ze vanuit uw Jira-project, en stuurt uw taken als gesynchroniseerde issues naar Jira (status, toegewezen persoon, gemapte velden) | [Jira](jira.md) |
| Filerskeepers | Koppelt uw bewaartermijnen uit Filerskeepers aan Dastra | [Filerskeepers](filerskeepers.md) |
| Microsoft Teams | Plaatst de meldingen van uw workflowregels als kaarten in een Teams-kanaal | [Microsoft Teams](microsoft-teams.md) |
| HTTP / Custom API | Roept vanuit uw workflowregels elke externe API aan met een aangepast HTTP-verzoek: methode, URL, headers en een JSON- of XML-body op basis van het record | [HTTP / Custom API](custom-http.md) |
| Slack | Waarschuwt gebruikers op Slack wanneer ze in een opmerking worden genoemd | [Slack](#slack) |
| Docusign | Stuurt uw contracten voor elektronische ondertekening naar uw verwerkers | [Docusign-integratie](../contracts/docusign.md) |
| OneDrive & SharePoint / Google Drive | Voegt bestanden uit uw OneDrive, SharePoint-bibliotheken of Google Drive toe aan uw actoren, beveiligingsmaatregelen, verwerkingsactiviteiten, taken, incidenten enzovoort | [Integratie met OneDrive/Google Drive](../settings/cloud-storage.md) |
| Office 365 / Gmail | Verstuurt Dastra-e-mails vanuit uw eigen mailbox | [SMTP-configuratie](../settings/smtp/README.md) |
| Inkomende e-mail | Zet de e-mails die naar een speciaal verzameladres worden gestuurd om in taken, verzoeken, datalekken, contracten of verwerkingsactiviteiten | [Gegevens verzamelen via inkomende e-mail](../settings/mailboxes.md) |
| SIRENE (INSEE) | Vult de gegevens van uw stakeholders aan vanuit het Franse bedrijvenregister | [SIRENE (INSEE)](#sirene-insee) |
| AI-leverancier | Koppelt elke OpenAI-compatibele AI-leverancier aan de Dastra-assistent | [Eigen AI-leverancier](../general/ai-assistant/how-it-works.md) |
| MCP-server | Laat uw AI-tools (Claude, Le Chat, VS Code enzovoort) de gegevens van Dastra lezen en bijwerken | [De MCP-server](../general/ai-assistant/mcp.md) |
| Single sign-on (SSO) | Laat uw gebruikers inloggen met uw eigen identiteitsprovider | [Single Sign On (SSO)](../settings/sso/README.md) |
| SIEM-streaming | Streamt uw beveiligingsauditgebeurtenissen in realtime naar uw SIEM | [SIEM-streaming](../settings/siem.md) |
| Zapier | Koppelt Dastra via geautomatiseerde workflows aan duizenden applicaties | [Zapier](zapier/README.md) |

Sommige integraties gelden voor uw hele organisatie in plaats van voor een werkruimte: single sign-on, SIEM-streaming, Office 365 / Gmail en de AI-leverancier. Hun tegel in de store brengt u naar de bijbehorende organisatie-instellingen, waar een accounteigenaar ze configureert.

### Zapier: alles wat u nog meer wilt koppelen

Zapier is een online automatiseringstool die uw applicaties en diensten zonder code met elkaar verbindt. Een Zap is een geautomatiseerde workflow met een trigger en een of meer acties: wanneer de triggergebeurtenis zich voordoet, worden de acties uitgevoerd.

Aan de kant van Dastra kan Zapier op twee triggers reageren (een nieuw verzoek van een betrokkene is aangemaakt, een nieuwe taak is aangemaakt) en zes acties uitvoeren: een taak aanmaken, een actor aanmaken, een verzoek van een betrokkene aanmaken, een actor koppelen aan een bestaande verwerkingsactiviteit, een actor zoeken en een actor zoeken of aanmaken. U kunt dus vertrekken van een Dastra-gebeurtenis om in een externe applicatie te handelen, of vertrekken van een externe gebeurtenis om in Dastra te handelen.

Vooraf geconfigureerde sjablonen (Salesforce, Zoho, Trello, Google Sheets, Excel, Outlook, Azure DevOps enzovoort) staan op de [Dastra-pagina van de Zapier-catalogus](https://zapier.com/apps/dastra/integrations). Met de Zap-editor bouwt u ook zelf een workflow vanaf nul. Zie de pagina [Zapier](zapier/README.md) en de bijbehorende [FAQ](zapier/faq.md).

#### Slack

De Slack-integratie doet één ding: wanneer een gebruiker in een opmerking wordt genoemd met de syntaxis @gebruikersnaam, stuurt de Dastra-bot hem of haar een direct bericht op Slack. Het bericht toont wie de gebruiker heeft genoemd, de tekst van de opmerking en het type van het gekoppelde object, met een knop **Bekijk in Dastra**.

1. Open **Instellingen voor werkruimte** > **Integraties** en selecteer **Slack**.
2. Klik bij het gebruiksscenario voor vermeldingen op **Integratie toevoegen**.
3. Kies in de stap **Verbinding** de optie **Voeg een verbinding toe** en klik daarna op **Opslaan en inloggen**. Dastra stuurt u door naar Slack om de applicatie in uw Slack-werkruimte te autoriseren.

De verbinding volstaat: dit gebruiksscenario heeft geen configuratiestap. Dastra vraagt Slack om de machtigingen om berichten te sturen en om gebruikers en hun e-mailadres te lezen.

{% hint style="info" %}
Dastra zoekt de Slack-gebruiker op via zijn of haar e-mailadres. Een gebruiker van wie het e-mailadres in Dastra met geen enkel account van uw Slack-werkruimte overeenkomt, ontvangt geen bericht.
{% endhint %}

#### SIRENE (INSEE)

De SIRENE (INSEE)-integratie bevraagt het Franse bedrijvenregister om de gegevens van een stakeholder aan te vullen. Ze wordt door Dastra beheerd: u hoeft geen inloggegevens in te voeren en ze geldt alleen voor bedrijven die in Frankrijk zijn geregistreerd.

1. Open **Instellingen voor werkruimte** > **Integraties** en selecteer **Sirene / Insee**.
2. Klik op **Integratie toevoegen**. De integratie wordt meteen geactiveerd.

In het formulier van een stakeholder van het type **Bedrijf** verschijnt daarna een zoekknop naast het veld **Naam van de organisatie** (**Zoeken in de SIRET-database**). Voer de bedrijfsnaam in, start de zoekopdracht en klik daarna op **Selecteer** naast het juiste bedrijf. Dastra vult de naam, het registratienummer (SIREN) en het postadres in.

### Beveiliging en gegevensbescherming

* Inloggegevens en tokens van integraties worden versleuteld opgeslagen, nooit teruggegeven door de API en gewist wanneer u een integratie verwijdert of een werkruimte wist.
* OAuth-stromen valideren hun callbacks strikt en de inkomende webhook-endpoints zijn in snelheid beperkt.
* Integraties zijn beperkt tot één werkruimte: gegevens van de ene werkruimte zijn nooit zichtbaar vanuit een andere.
* Records die een integratie aanmaakt (activa, verzoeken enzovoort) behoren tot uw werkruimte en blijven behouden wanneer u de integratie verwijdert.

### Andere behoeften

Past geen enkele integratie bij uw behoefte, dan kunt u met de [Dastra REST API](../../api/configuration.md) uw eigen scripts en connectoren bouwen. Via de support dient u ook een connectoraanvraag in bij het Dastra-team.
