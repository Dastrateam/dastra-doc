---
description: >-
  Deze pagina legt uit hoe u Dastra verbindt met Microsoft OneDrive & SharePoint of Google Drive om uw cloudopslag te gebruiken als het belangrijkste documentbeheersysteem van de werkruimte.
---

# Integraties met OneDrive & SharePoint / Google Drive

## Voordelen van een eigen cloudopslag

Standaard steunt het [documentbeheer](../files/README.md) van Dastra op Azure Blob Storage: de bestanden zijn versleuteld, op virussen gescand en redundant opgeslagen op een tweede server. Zie de [beveiligingsdocumentatie](../../security/general.md) voor meer informatie.

In sommige organisaties dupliceert deze opslag een bestaand cloudbestandssysteem (SharePoint, OneDrive, Google Drive). Dastra integreert standaard met deze providers om die duplicatie te vermijden:

* Microsoft OneDrive & SharePoint: een OneDrive of een SharePoint-documentbibliotheek van uw Microsoft 365-organisatie;
* Google Drive.

<figure><img src="../../.gitbook/assets/settings-files-attachment-panel.png" alt="Selector voor de bestandsbron in het documentbeheer van Dastra"><figcaption><p>Bestanden kunnen worden opgeslagen in Dastra, OneDrive & SharePoint of Google Drive</p></figcaption></figure>

## Type verbinding: OAuth van een gebruiker

{% hint style="warning" %}
Deze integratie gebruikt OAuth-authenticatie met de inloggegevens van een gebruikersaccount. Het is geen verbinding op toepassingsniveau via de Microsoft Graph API of de Google API.

In de praktijk betekent dit:

* De verbinding wordt gelegd namens de gebruiker die de integratie configureert.
* De toegang tot de bestanden hangt af van de machtigingen van dat account.
* Als het account wordt gedeactiveerd of de tokens worden ingetrokken, werkt de integratie niet meer tot ze opnieuw is verbonden.
* Het is aan te raden een speciaal serviceaccount (niet persoonlijk) te gebruiken om deze integratie te configureren.
{% endhint %}

## De integratie instellen

Open **Instellingen voor werkruimte** > **Integraties** en klik op **Microsoft OneDrive & SharePoint** of **Google Drive**.

Klik op **Integratie toevoegen**. U wordt doorgestuurd naar de aanmeldpagina van de provider, waar u toegang tot uw opslag moet autoriseren.

### De drive kiezen (alleen OneDrive & SharePoint)

Na de authenticatie toont Dastra de drives die het verbonden account kan bereiken. Kies in **Kies de rootsdrive** de drive die Dastra gebruikt:

| Optie | Beschrijving | Aanbeveling |
| --- | --- | --- |
| `<Site> / <Library>` (bijvoorbeeld `Root site / Documents`) | Een documentbibliotheek van een SharePoint-site van uw organisatie | Aanbevolen voor zakelijk gebruik: gedeelde ruimte, niet gekoppeld aan een persoonlijk account |
| Uw persoonlijke drive | De persoonlijke OneDrive van het verbonden account | Vermijd dit in productie: het geeft toegang tot alle bestanden van de persoonlijke drive |

Klik op **Verversen** als een site of bibliotheek die u net hebt aangemaakt nog niet verschijnt.

{% hint style="info" %}
Gebruikt u een persoonlijke drive, gebruik dan bij voorkeur een speciaal serviceaccount zonder persoonlijke bestanden. U kunt ook een [speciale SharePoint-site](https://learn.microsoft.com/nl-nl/sharepoint/create-site-collection) aanmaken om de bestanden van Dastra af te scheiden.
{% endhint %}

### Een hoofdmap kiezen (alleen OneDrive & SharePoint)

Standaard gebruikt Dastra de root van de drive. U kunt dat beperken tot een map van de drive:

1. Klik onder **Root folder** op **Choose a folder**.
2. Blader door de drive en klik op **Selecteer** bij de map die u wilt gebruiken. Met **Use the root of the drive** gaat u terug naar de standaardinstelling.
3. Sla de configuratie op.

Dastra slaat zijn bestanden dan op in deze map en het bladeren vanuit Dastra blijft ertoe beperkt: gebruikers kunnen er niet boven uit. Zo deelt u het gemakkelijkst één map van een SharePoint-bibliotheek met Dastra, zonder de rest van de bibliotheek bloot te stellen.

<figure><img src="../../.gitbook/assets/settings-files-onedrive-root-folder.png" alt="De drive en de hoofdmap van de integratie met OneDrive & SharePoint kiezen"><figcaption><p>De drive en de hoofdmap kiezen</p></figcaption></figure>

{% hint style="warning" %}
De hoofdmap beperkt wat Dastra toont en waar het schrijft. Ze wijzigt de machtigingen van het verbonden account in Microsoft 365 niet: dat account behoudt toegang tot alles wat het al kon openen. Wilt u de toegang ook aan Microsoft-zijde beperken, verbind de integratie dan met een serviceaccount dat alleen toegang heeft tot de gekozen bibliotheek of map.
{% endhint %}

Wordt de hoofdmap in SharePoint of OneDrive verwijderd of verplaatst, dan toont Dastra een foutmelding die u vraagt een andere map te kiezen in de instellingen van de integratie.

## Bestanden uit de cloud koppelen aan een Dastra-element

U kunt vanuit elk element (verwerkingsactiviteit, taak, stakeholder...) bestanden koppelen die in uw cloud staan:

1. Open het bestandspaneel van het element.
2. Selecteer de gegevensbron linksboven in het paneel.

![](../../.gitbook/assets/settings-files-manager-header.png)

3. Blader door uw drive via het bestandsbeheer.
4. Klik op **Voeg een bestand uit de bibliotheek toe** om het bestand te koppelen.

![](../../.gitbook/assets/settings-files-select-from-manager.png)

U kunt ook nieuwe bestanden rechtstreeks vanuit Dastra naar uw drive uploaden.

Een opslag waarvan het gebruiksscenario in de instellingen van de integratie is gedeactiveerd, wordt niet meer aangeboden als gegevensbron.

## Beperkingen

### OneDrive & SharePoint

* De verbinding gebruikt OAuth van een gebruiker, niet de Microsoft Graph API. Als het account dat de integratie heeft ingesteld wordt gedeactiveerd, wordt de verbinding verbroken.
* Dastra werkt alleen in de gekozen drive, en in de hoofdmap als er een is ingesteld.
* Kies in zakelijke omgevingen een SharePoint-documentbibliotheek in plaats van een persoonlijke drive.

### Google Drive

* Alleen bestanden die vanuit Dastra zijn aangemaakt, kunnen in Google Drive worden toegevoegd of gewijzigd. Dastra heeft geen toegangsrechten tot bestanden die rechtstreeks in Drive zijn aangemaakt. Dit is een beperking van de OAuth-connector.
* Bestanden die in Dastra zijn aangemaakt, kunt u zonder beperking delen met andere medewerkers.
