---
description: >-
  Elke organisatie is anders: maak aangepaste rollen aan en stem hun machtigingen module per module af.
---

# Rollen en machtigingen

## Algemene werking

Elke gebruiker kan aan 1 of meer rollen worden gekoppeld. De rollen zijn zelf gekoppeld aan een lijst met machtigingen (bijvoorbeeld: schrijven in het register, een vragenlijst aanmaken...). Er zijn twee manieren om de rollen van gebruikers te beheren.

* Als u eigenaar bent, klikt u op het tandwielpictogram in de bovenbalk (**Organisatie-instellingen**) en daarna op **Gebruikers**. Het directe adres is [https://app.dastra.eu/general-settings/users](https://app.dastra.eu/general-settings/users).
* Als u de rol van beheerder van de werkruimte hebt, opent u **Instellingen voor werkruimte** > **Gebruikers** om de rollen en machtigingen te beheren van de gebruikers die tot uw werkruimte behoren.

De standaardrollen (**Administrator**, **Bijdrager**, **Lezer**) worden beschreven in [Rollen en machtigingen beheren](../../getting-started/setup/roles.md). Deze pagina legt uit hoe u uw eigen rollen aanmaakt.

{% hint style="info" %}
Een rol volstaat niet altijd om een item te zien: ook de toegang tot **organisatorische eenheden** en de **teams** van de gebruiker tellen mee. Zie [Waarom ziet een gebruiker een verwerkingsactiviteit niet?](../../getting-started/setup/visibility.md)
{% endhint %}

## Uw eigen rollen aanmaken

De pagina **Rollen en machtigingen** is voorbehouden aan de eigenaren van de organisatie. Ze verschijnt wanneer uw abonnement geavanceerde personalisatie bevat. Klik om ze te openen op het tandwielpictogram in de bovenbalk (**Organisatie-instellingen**) en daarna op **Rollen en machtigingen** in het linkermenu. Het directe adres is [https://app.dastra.eu/general-settings/roles](https://app.dastra.eu/general-settings/roles).

Klik op **Nieuwe rol** om een aangepaste rol aan te maken.

<figure><img src="../../.gitbook/assets/settings-roles-1.png" alt="De lijst met rollen, met de drie standaardrollen en de knop Nieuwe rol"><figcaption><p>De lijst met rollen</p></figcaption></figure>

Vul de naam van de rol in en vink daarna de vakjes aan die bij de machtigingen van elke module passen.

<figure><img src="../../.gitbook/assets/settings-roles-2.png" alt="Het paneel voor het bewerken van een rol, met de machtigingen van de module Taken"><figcaption><p>Een rol voor taakbeheer aanmaken</p></figcaption></figure>

* **Read/Write own elements**: gebruikers kunnen alleen de items bekijken en bewerken die aan hen zijn toegewezen in de module.
* **Lezing**: gebruikers kunnen alle items van de module bekijken.
* **Schrijven**: gebruikers kunnen alle bestaande items van de module wijzigen. In modules met de machtiging **Create** geeft **Schrijven** niet het recht om nieuwe items aan te maken.
* **Create**: gebruikers kunnen nieuwe items aanmaken in de module. Deze machtiging staat los van de machtiging **Schrijven**.
* **Exporteren**: gebruikers kunnen alle items van de module exporteren.
* **Importeren**: gebruikers kunnen items in de module importeren.
* **Kennisgeving**: gebruikers ontvangen meldingen voor alle items van de module.

{% hint style="info" %}
U kunt voor dezelfde rol in een module niet tegelijk **Read/Write own elements** en de machtigingen op alle items selecteren, behalve de machtiging **Create**. Gebruikers hebben ofwel alleen toegang tot hun eigen items, ofwel tot alle items; met de machtiging **Create** kunnen ze bovendien nieuwe items aanmaken.
{% endhint %}

Zodra u uw aangepaste rol hebt aangemaakt, kunt u ze toewijzen aan elke gebruiker van een werkruimte binnen uw organisatie.

### De machtiging Create

De volgende modules bieden een machtiging **Create** die los staat van de machtiging **Schrijven**:

* Taakbeheer
* Registers van gegevensverwerkingen
* Verzoeken van betrokkenen
* Datalekken
* Gegevens in kaart brengen en repositories
* Contractbeheer
* Beheer van AI-systemen

In deze modules kunt u **Create** samen met **Lezing** of met **Read/Write own elements** aanvinken. Een rol die **Read/Write own elements** en **Create** combineert, laat de gebruiker nieuwe items aanmaken en alleen de aan hem toegewezen items bewerken. Vink voor een rol die bestaande items bewerkt zonder nieuwe aan te maken **Schrijven** aan zonder **Create** aan te vinken.

De standaardrollen **Administrator** en **Bijdrager** bevatten in deze modules de machtiging **Create**.

<figure><img src="../../.gitbook/assets/settings-roles-create-permission.png" alt="De machtiging Create aangevinkt samen met de machtiging Read/Write own elements in de module Datalekken"><figcaption><p>De machtiging Create gecombineerd met het bewerken van eigen items</p></figcaption></figure>

## Een bestaande rol klonen

Kloon een bestaande rol om een rol aan te maken op basis van een bestaande configuratie:

1. Klik in de lijst met rollen op het menu met drie puntjes op de rij van de rol die u wilt dupliceren.
2. Klik op **Klonen**.

Dastra maakt een nieuwe rol aan met alle machtigingen van de bronrol. De naam is de naam van de bronrol gevolgd door een nummer, bijvoorbeeld "Bijdrager (2)". Het bewerkingspaneel opent: geef de rol een nieuwe naam en pas de machtigingen aan.

De standaardrollen kunnen niet worden bewerkt: door ze te klonen start u vanuit hun machtigingen. Klonen is ook nuttig om varianten van een rol aan te maken, bijvoorbeeld een rol "DPO-bijdrager" die lichtjes afwijkt van de rol "Bijdrager".
