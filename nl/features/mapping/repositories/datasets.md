---
description: >-
  Groepeer gegevensvelden in samenhangende sets, met de bewaarregels die voor
  hun levenscyclus gelden, en hergebruik ze in uw activa en verwerkingsactiviteiten.
---

# Datasets

Een dataset groepeert gegevensvelden, gevoelig of niet, met de bewaarregels die voor hun levenscyclus gelden. Loonstroken op papier of de klantendossiers van een CRM zijn voorbeelden van datasets.

Definieer een dataset één keer in deze repository en hergebruik hem daarna in de activa die hem bevatten en in uw verwerkingsactiviteiten. Zo blijft de inventaris van uw gegevens consistent en vindt u voor één actief alles wat het bevat.

## Een dataset toevoegen

Open **Data inventory** > **Referenties** > **Datasets**. U kunt:

* op **Nieuwe dataset** klikken om de **Wizard voor het maken van gegevenssets** te openen en daarna **Lege gegevensset**, **AI gegenereerd** (deze optie hangt af van de functies die voor uw organisatie zijn ingeschakeld) of **Stap voor stap handleiding** te kiezen, die u eerst de gegevensvelden van de dataset laat selecteren. **Importeren van Filerskeepers** verschijnt wanneer de integratie [Filerskeepers](../../integrations/filerskeepers.md) is ingeschakeld;
* op de AI-knop links van **Nieuwe dataset** klikken om de dataset te beschrijven en de assistent een concept te laten opstellen;
* op de pijl naast **Nieuwe dataset** klikken en daarna op **Maak vanuit de bibliotheek** om een dataset uit de bibliotheek te kopiëren;
* datasets, met hun gegevensvelden, importeren uit een bestand: pijl naast **Nieuwe dataset** en daarna **Importeren**. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-datasets-1.png" alt="Lijst van datasets met het paneel Filters geopend"><figcaption><p>De lijst van datasets</p></figcaption></figure>

## Het formulier van de dataset invullen

| Sectie | Veld | Inhoud |
| --- | --- | --- |
| **Algemene informatie** | **Naam van de gegevensset** | De naam van de dataset, verplicht. |
| | **Gerelateerde activa** | Het actief dat de dataset bevat. U kunt vanuit dit veld een actief aanmaken. Een dataset zonder actief is een wees. |
| | **Categorieën betrokken personen** | De [categorieën van betrokkenen](subject-categories.md) waarop de gegevens betrekking hebben. U kunt vanuit dit veld een categorie aanmaken. |
| | **Interne referentie**, **Samenvatting** | Uw referentie en een vrije beschrijving. |
| **Velden voor persoonlijke gegevens** | | De gegevensvelden van de dataset. Selecteer een veld in de lijst of maak er een aan, vul daarna de **Opmerkingen** in en vink **Vereist** aan wanneer het veld verplicht is. Elk veld toont zijn gevoeligheidsniveau en zijn categorie. |
| **Standaard bewaartijden** | **Actieve basis**, **Tussentijdse archivering** | Voor elk: de **Bewaartermijn**, de regel (**Beschrijf de regel (duur, voorwaarden...)**) en de **Justificatie** ervan. |
| | **Definitief verwijderen** | De beschrijving van het opschoningsbeleid en de **Justificatie** ervan. |
| **Herkomst van de collectie** | **Herkomst van de collectie**, **Beschrijving van de bron van de verzameling** | Waar de gegevens vandaan komen. |

De [aangepaste velden](../../general/custom-fields.md) die voor datasets zijn gedefinieerd en de [labels](../../general/tags.md) worden aan het formulier toegevoegd.

De werkbalk van het formulier geeft toegang tot de opmerkingen, vragenlijsten, taken en AI-systemen die aan de dataset zijn gekoppeld, afhankelijk van uw rechten en de ingeschakelde functies. Ze bevat ook:

* **Gekoppelde elementen**: de [generieke relaties](../relationships.md) van de dataset;
* **Link naar een verwerkingsactiviteit**: de verwerkingsactiviteiten die de dataset gebruiken, en de link om er meer toe te voegen.

Het actiemenu van het formulier biedt **Dupliceren**, **Samenvoegen** en **Verwijderen**.

## Datasets in de lijst vinden

De filters van de lijst omvatten **Activa**, **Soorten**, **Filteren op tags**, **Categorie van betrokken personen**, **Cat. gegevens** en **Gevoelige gegevens**. Schakel **Zie weeskind (zonder actief)** in om de datasets te tonen die aan geen enkel actief zijn gekoppeld en koppel ze daarna via het veld **Gerelateerde activa**.

Bij een selectie kunt u **Velden bewerken**, **Samenvoegen**, **Exporteren** en **Verwijderen**. Het **Gegevenskwaliteitsinstrument**, in het menu van **Nieuwe dataset**, detecteert duplicaten. Zie [Elementen samenvoegen](../../general/merge.md).

## Waar datasets worden gebruikt

* In een verwerkingsactiviteit voegt u de datasets toe die de verwerking behandelt, en kunt u hun bewaartermijn alleen voor deze activiteit aanpassen. Zie [Gegevens en retentie](../../ropa/activity/datasets.md).
* In een actief toont de sectie **Datasets** de datasets die het bevat. Zie [Activa](assets.md).
* In categorieën van betrokkenen: het formulier van een categorie toont de datasets ervan. Zie [Categorieën van betrokkenen](subject-categories.md).
* In AI-systemen, via het tabblad **AI-systemen** van de dataset.

{% hint style="warning" %}
Het verwijderen van een dataset verwijdert de koppelingen ervan met gegevensvelden, bijlagen, verwerkingsactiviteiten en activa. De gesprekken en de verwerking van gerelateerde verzoeken om rechten uit te oefenen worden definitief verwijderd. Vragenlijsten en gerelateerde taken blijven bewaard.
{% endhint %}
