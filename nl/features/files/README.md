---
description: >-
  Centraliseer in het bestandsbeheer van Dastra de documenten die uw naleving
  aantonen: documenten aanmaken, mappen, toegangsrechten en cloudopslag.
---

# Bestandsbeheer

Dastra integreert standaard een bestandsbeheer, in het Frans ook GED (elektronisch documentbeheer) genoemd. Het centraliseert en deelt de toegang tot alle documenten die bij uw werk in Dastra horen. U vindt de module onder **Resources** > **Bestandsbeheer** in het linkermenu.

Hier kunt u alle documentatie opslaan die helpt uw naleving van de AVG aan te tonen.

{% hint style="info" %}
**Focus op AVG-documentatie**

De documentatieplicht vloeit voort uit het verantwoordingsbeginsel van artikel 24 van de AVG.

In de praktijk gaat dit verder dan het verwerkingsregister en omvat het (niet-limitatieve lijst):

* Interne procedures voor het aanmaken van nieuwe verwerkingen van persoonsgegevens
* DPIA-methodologie en uitgevoerde beoordelingen
* Schriftelijk gegevensbeschermingsbeleid
* Procedures voor het in kaart brengen en inventariseren van gegevens
* Opleidingsregisters van het personeel dat betrokken is bij gegevensverwerking
* Procedures voor het beheer van de rechten van betrokkenen
* Interne mechanismen voor klachtenbehandeling
* Procedures voor het beheer en de melding van datalekken
* Verslagen en bevindingen van interne of externe audits
* Contractdocumentatie voor verwerkers en gezamenlijke verwerkingsverantwoordelijken
{% endhint %}

## Geaccepteerde bestandsformaten

Veel formaten worden ondersteund:

* PDF
* Word (.docx)
* Excel (.xlsx)
* Afbeeldingen (JPG, PNG enzovoort)
* Archieven (.zip)
* En meer

Wordt een formaat niet geaccepteerd, plaats het bestand dan in een `.zip`-archief en upload dat.

## Een document aanmaken

U kunt rechtstreeks in Dastra een document schrijven, bijvoorbeeld om aantekeningen te maken. Klik in het bestandsbeheer op **Schrijf een document**.

<figure><img src="../../.gitbook/assets/files-1.png" alt="De werkbalk van het bestandsbeheer met de knop Schrijf een document"><figcaption><p>De knop Schrijf een document</p></figcaption></figure>

Voer het label van het document in en daarna de inhoud ervan in de Markdown-editor. Het document wordt opgeslagen in Markdown-formaat (.md).

<figure><img src="../../.gitbook/assets/files-2.png" alt="De documenteditor met de knop Genereer met AI"><figcaption><p>De documenteditor</p></figcaption></figure>

### Een document genereren met AI

De AI-assistent kan een **document genereren** op basis van een beschrijving en, indien nodig, bestanden of een websiteadres als context.

Om dit te gebruiken, klikt u op **Schrijf een document** en daarna in de editor op **Genereer met AI**. Beschrijf kort het document dat u nodig hebt (type, doel, verwachte inhoud) en voeg eventueel bestanden toe om de context te verrijken. De gegenereerde tekst verschijnt in de editor: controleer ze, bewerk ze en sla ze op. De knop is alleen actief als de AI-assistent in uw abonnement beschikbaar is.

{% hint style="info" %}
Deze functie is handig om een eerste versie op te stellen van een gegevensbeschermingsbeleid, een interne procedure of een ander nalevingsdocument.
{% endhint %}

## Een map aanmaken

Organiseer uw documenten in mappen zodat u ze kunt terugvinden. Klik op **Maak een map**, geef ze een naam en kies de locatie ervan: submappen worden ondersteund.

<figure><img src="../../.gitbook/assets/files-3.png" alt="Het venster voor het aanmaken van een map"><figcaption><p>Het venster voor het aanmaken van een map</p></figcaption></figure>

## Toegangsrechten beheren

U kunt de toegang tot mappen en bestanden beperken. Rechten gelden voor mappen en bestanden. Ze worden geconfigureerd door de beheerder van de werkruimte of door een gebruiker die bestanden mag beheren.

{% hint style="info" %}
Standaard worden er geen beperkingen toegepast op de mappenstructuur. De machtigingen die aan de rollen van de gebruiker zijn gekoppeld, blijven wel van toepassing.
{% endhint %}

Klik op de rij van een map of een bestand op de knop **Element toegangsrechten** en voeg daarna de teams en gebruikers toe met het gewenste machtigingsniveau.

<figure><img src="../../.gitbook/assets/files-4.png" alt="Het venster om de toegangsrechten van een map te beheren"><figcaption><p>Het venster voor de toegangsrechten</p></figcaption></figure>

Deze machtigingen gelden voor alle onderliggende elementen, dat wil zeggen alles wat de map bevat, submappen inbegrepen.

{% hint style="info" %}
Een map zonder gedefinieerde machtigingen is toegankelijk voor alle gebruikers.

Zijn er machtigingen gedefinieerd of geërfd op een element, dan is het verborgen voor gebruikers die niet over de vereiste autorisaties beschikken.
{% endhint %}

## Bestanden uit andere modules

De bestanden die aan verwerkingsactiviteiten, activa, stakeholders en contracten zijn gekoppeld, kunnen in het bestandsbeheer worden opgeslagen, in een speciale map. Ze zijn dan zichtbaar voor alle gebruikers die bestanden mogen bekijken: u moet de toegang tot de mappen beheren.

Om dit standaardgedrag te kiezen, klikt u op **Instellingen voor werkruimte** > **Algemeen** en schakelt u daarna in de kaart **Bestandsbeheer** de optie **Upload standaard bestanden in GED** in. Schakelt u de optie uit, dan blijven bestanden aan hun item gekoppeld en verschijnen ze niet in het bestandsbeheer, wat het beheer van de toegang eenvoudiger kan maken.

<figure><img src="../../.gitbook/assets/files-5.png" alt="De kaart Bestandsbeheer in de algemene instellingen van de werkruimte"><figcaption><p>De optie om bestanden standaard te uploaden</p></figcaption></figure>

Gebruikers die bestanden mogen beheren, hebben drie extra opdrachten:

* **Bekijk bestanden die niet in bestandsbeheer staan**, in het menu **Filters** van het bestandsbeheer, toont de bestanden die er niet in zijn opgeslagen.
* **Ga naar gemeenschappelijk bestandsbeheer** verplaatst een bestand naar het bestandsbeheer, in de map van uw keuze.
* **Verwijderen uit algemeen bestandsbeheer** haalt het bestand uit het bestandsbeheer: het bestand blijft bewaard, maar andere gebruikers kunnen het niet meer vinden.

## Cloudopslag

Standaard slaat Dastra bestanden op in Azure Blob Storage: ze zijn versleuteld, op virussen gescand en redundant. U kunt ook uw eigen opslag koppelen, Microsoft OneDrive & SharePoint of Google Drive, om te vermijden dat bestanden tussen systemen worden gedupliceerd.

{% content-ref url="../settings/cloud-storage.md" %}
[Integraties met OneDrive & SharePoint / Google Drive](../settings/cloud-storage.md)
{% endcontent-ref %}

## Documentsjablonen

Dastra biedt kant-en-klare documentsjablonen om u te helpen uw nalevingsdocumentatie op te bouwen.

{% content-ref url="templates.md" %}
[Documentsjablonen](templates.md)
{% endcontent-ref %}
