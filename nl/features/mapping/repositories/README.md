---
description: >-
  Het verwerkingsregister steunt op repositories: activa, stakeholders,
  datasets en beveiligingsmaatregelen. Met Dastra beheert u ze los van het
  register om invoerfouten te beperken.
---

# Referenties

Om invoerfouten te beperken, kunt u in Dastra een of meer repositories onafhankelijk van het verwerkingsregister beheren. De verwerkingsactiviteiten van het register hergebruiken daarna de elementen van die repositories.

## De repositories openen

Klik in het zijmenu onder **Data inventory** op **Referenties**. Het menu biedt:

* **Rapportage**: het aantal elementen in elke repository.
* **In kaart brengen**: een grafische weergave van uw activa en stakeholders.
* **Activa**, **Actoren**, **Datasets**, **Verklarende woordenlijst voor gegevens**, **Maatregelen** en **Categorie van betrokken personen**: de zes repositories.

## Repositories die Dastra aanbiedt

* **Activa**: activa zijn de elementen die u helpen gegevens te beheren, zoals gegevensdragers, gebouwen en materiële of immateriële uitrusting. Zie [Activa](assets.md).
* **Actoren**: stakeholders verschillen van gebruikers doordat ze zich niet bij het platform hoeven aan te melden.
* **Datasets**: datasets zijn groepen gegevens die samenhangende geheel vormen, met hun bewaarregels.
* **Verklarende woordenlijst voor gegevens**: gegevensvelden zijn de stukjes informatie. Ze vormen het meest atomaire niveau in Dastra.
* **Maatregelen**: beveiligingsmaatregelen zijn de technische of organisatorische voorzieningen die zijn getroffen om de gegevens te beschermen.
* **Categorie van betrokken personen**: categorieën van betrokkenen groeperen categorieën van personen.

## Functies die de lijsten delen

De lijsten van de zes repositories delen verschillende functies:

* **Maak vanuit de bibliotheek** voegt een element toe uit de sjablonenbibliotheek.
* **Importeren** voegt elementen toe uit een bestand. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md).
* **Exporteren** exporteert de lijst.
* Het **Gegevenskwaliteitsinstrument** detecteert duplicaten en **Samenvoegen** combineert ze. Het gegevenskwaliteitsinstrument bestaat niet voor categorieën van betrokkenen. Zie [Elementen samenvoegen](../../general/merge.md).

## Rapportage en grafieken

De pagina **Rapportage** toont één kaart per repository met het aantal elementen. Klik op een kaart om de bijbehorende lijst te openen. Met de knop **Een app toevoegen** maakt u vanaf deze pagina een actief aan.

De pagina **In kaart brengen** biedt vier weergaven, die u kiest in de keuzelijst linksboven:

* **In kaart brengen van stromen tussen activa**: een grafiek van activa, hun uitgevers, hun datasets en hun labels. [Generieke relaties](../relationships.md) verschijnen als koppelingen.
* **In kaart brengen van stakeholders**: een grafiek van stakeholders, hun activa en hun sub-verwerkers, die u kunt filteren op **Verantwoordelijkheid**.
* **Uitsplitsing van gegevens per actief**: een Sankey-diagram van de verdeling van gegevens per actief, dat u kunt filteren op type (gegevensvelden, verwerkingsactiviteiten, eigenaars, landen, gegevenscategorieën).
* **Hiërarchische structuur van activa**.

De knoppen **Afdrukken** en **Verversen** staan boven aan de pagina.

## Wat specifiek is voor elke repository

### Actoren

Een stakeholder kan aan een organisatorische eenheid worden gekoppeld, waardoor de zichtbaarheid beperkt blijft tot de gebruikers van die eenheid. Met de knop **Nieuwe actor** begint u vanuit een sjabloon (**Ingebouwde sjabloon**) of vanaf nul (**Gepersonaliseerd**).

In het formulier kunt u in de sectie **Sub-verwerkers** de sub-verwerkers van de organisatie opslaan, die vaak in de verwerkersovereenkomst worden genoemd, en zo de hele keten van onderaanneming in kaart brengen.

In de lijst vindt u met het filter **Verantwoordelijkheid** stakeholders volgens de manier waarop u ze gebruikt: softwareuitgever (uitgever van ten minste één actief), aanbieder van een AI-model (uitgever van ten minste één AI-model) of ontvanger in een verwerkingsactiviteit (verwerker, gezamenlijke verwerkingsverantwoordelijke, openbare instantie enzovoort).

### Datasets

Een dataset groepeert gegevensvelden, gevoelig of niet, met de bewaarregels die van toepassing zijn op hun levenscyclus: bijvoorbeeld loonstroken op papier of klantendossiers in een CRM. Vul de **Herkomst van de collectie**, de **Actieve basis** en de **Tussentijdse archivering** in en voeg daarna de gegevens toe bij **Velden voor persoonlijke gegevens**.

Het filter **Zie weeskind (zonder actief)** toont de datasets die niet aan een actief zijn gekoppeld. U kunt ze koppelen via het veld **Gerelateerde activa**.

### Verklarende woordenlijst voor gegevens

Elk gegevensveld heeft een **Niveau van verwerking**:

* **Standaard**, bijvoorbeeld naam, voornaam of telefoonnummer.
* **Zeer persoonlijke gegevens**, bijvoorbeeld financiële gegevens, locatie of communicatie.
* **Gevoelige gegevens**, bijvoorbeeld raciale of etnische afkomst, politieke opvattingen, religie, gezondheid of seksuele geaardheid.

Het niveau **Gevoelige gegevens** toont het veld **Wettelijke basis voor inzameling**. De kolom **Datasets**, standaard verborgen, kunt u filteren met **Is leeg** of **Is niet leeg**: gebruik ze om de gegevensvelden te vinden die tot geen enkele dataset behoren.

### Maatregelen

Een maatregel heeft een naam, een **Type** en eventueel het adres van de documentatie ervan, bijvoorbeeld op de website van de CNIL. Het filter **Bekijk de wezen** toont de maatregelen die noch aan een actief, noch aan een verwerkingsactiviteit zijn gekoppeld.

### Categorieën van betrokkenen

Een categorie heeft een naam en de optie **Betrokken kwetsbare personen**. Vink die aan wanneer de categorie mensen in een onevenwichtige situatie groepeert, zoals minderjarigen, werknemers of ouderen.
