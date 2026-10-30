---
description: >-
  Het verwerkingsregister steunt op repositories: activa, stakeholders,
  datasets, gegevensvelden, beveiligingsmaatregelen en categorieën van
  betrokkenen. Met Dastra beheert u ze los van het register om invoerfouten te
  beperken.
---

# Referenties

Om invoerfouten te beperken, kunt u in Dastra repositories onafhankelijk van het verwerkingsregister beheren. De verwerkingsactiviteiten van het register hergebruiken daarna de elementen van die repositories.

## De repositories openen

Klik in het zijmenu onder **Data inventory** op **Referenties**. Het menu biedt:

* **Rapportage**: het aantal elementen in elke repository.
* **In kaart brengen**: een grafische weergave van uw activa en stakeholders.
* **Activa**, **Actoren**, **Datasets**, **Verklarende woordenlijst voor gegevens**, **Maatregelen** en **Categorie van betrokken personen**: de zes repositories.

Wat u kunt doen, hangt af van de rechten voor gegevensmapping en repositories van uw rol. Zie [Rollen en machtigingen](../../settings/roles.md).

## De zes repositories

* [Activa](assets.md): gegevensdragers, gebouwen en materiële of immateriële uitrusting.
* [Actoren](stakeholders.md): de bedrijven en personen die aan uw verwerking zijn gekoppeld en zich niet bij het platform hoeven aan te melden.
* [Datasets](datasets.md): groepen gegevensvelden die samenhangende sets vormen, met hun bewaarregels.
* [Verklarende woordenlijst voor gegevens](data-glossary.md): de gegevensvelden, het meest atomaire niveau in Dastra.
* [Beveiligingsmaatregelen](security-measures.md): de technische of organisatorische voorzieningen die de gegevens beschermen. Het menu-item is **Maatregelen**.
* [Categorieën van betrokkenen](subject-categories.md): de groepen personen van wie u gegevens verwerkt. Het menu-item is **Categorie van betrokken personen**.

Elke pagina beschrijft de velden van het formulier, hoe u elementen aanmaakt, importeert en samenvoegt, en waar de repository wordt gebruikt. Hoe een verwerkingsactiviteit deze elementen gebruikt, wordt één keer beschreven, op de pagina's van de activiteit: zie [Een verwerkingsactiviteit invullen](../../ropa/activity/README.md).

## Functies die de lijsten delen

De lijsten van de zes repositories delen verschillende functies:

* **Maak vanuit de bibliotheek** voegt een element toe uit de sjablonenbibliotheek. Bij de meeste repositories stelt een AI-knop naast de knop om aan te maken een element op basis van een korte beschrijving op, wanneer de functie voor uw organisatie is ingeschakeld.
* **Importeren** voegt elementen toe uit een bestand. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md).
* **Exporteren** exporteert de lijst, of alleen de geselecteerde regels.
* Het **Gegevenskwaliteitsinstrument** detecteert duplicaten en **Samenvoegen** combineert ze. Het gegevenskwaliteitsinstrument bestaat niet voor categorieën van betrokkenen. Zie [Elementen samenvoegen](../../general/merge.md).
* Filters, aangepaste kolommen en aangepaste weergaven. Zie [Geavanceerde filters](../../general/filters.md).
* Bulkacties op een selectie van regels. Zie [Lijsten, bulkacties en prullenbak](../../general/lists.md). **Velden bewerken**, waar het wordt aangeboden, wijzigt hetzelfde veld op alle geselecteerde elementen.
* De tabel- en kaartweergave, voor activa en stakeholders.

In de repositories vraagt **Verwijderen** om bevestiging en verwijdert het element definitief: de prullenbak die op de pagina over lijsten wordt beschreven, geldt hier niet.

De formulieren delen ook de [aangepaste velden](../../general/custom-fields.md), behalve voor categorieën van betrokkenen, en, in de werkbalk, de [generieke relaties](../relationships.md) van het element, waar die worden aangeboden.

## Rapportage en grafieken

De pagina **Rapportage** toont één kaart per repository met het aantal elementen. Klik op een kaart om de bijbehorende lijst te openen. Met de knop **Een app toevoegen** maakt u vanaf deze pagina een actief aan.

De pagina **In kaart brengen** biedt vier weergaven, die u kiest in de keuzelijst linksboven:

* **In kaart brengen van stromen tussen activa**: een grafiek van activa, hun uitgevers, hun datasets en hun labels. [Generieke relaties](../relationships.md) verschijnen als koppelingen.
* **In kaart brengen van stakeholders**: een grafiek van stakeholders, hun activa en hun sub-verwerkers, die u kunt filteren op **Verantwoordelijkheid**.
* **Uitsplitsing van gegevens per actief**: een Sankey-diagram van de verdeling van gegevens per actief, dat u kunt filteren op type (gegevensvelden, verwerkingsactiviteiten, eigenaars, landen, gegevenscategorieën).
* **Hiërarchische structuur van activa**.

De knoppen **Afdrukken** en **Verversen** staan boven aan de pagina.
