---
description: >-
  Beheer de lijst van gegevensvelden, het meest atomaire niveau van de
  gegevensmapping, met hun categorie en gevoeligheidsniveau.
---

# Verklarende woordenlijst voor gegevens

Een gegevensveld is een stukje informatie, zoals een naam, een e-mailadres of een dossiernummer in de gezondheidszorg. Het is het meest atomaire niveau van de mapping: [datasets](datasets.md) bestaan uit gegevensvelden.

Vermeld elk veld één keer in deze woordenlijst, zodat elke dataset dezelfde gegevens op dezelfde manier beschrijft.

## Een gegevensveld toevoegen

Open **Data inventory** > **Referenties** > **Verklarende woordenlijst voor gegevens**. U kunt:

* op **Gegevens toevoegen** klikken om een leeg formulier te openen;
* op de pijl naast **Gegevens toevoegen** klikken en daarna op **Maak vanuit de bibliotheek** om velden uit de bibliotheek te kopiëren;
* velden importeren uit een bestand: pijl naast **Gegevens toevoegen** en daarna **Importeren**. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md).

U kunt een veld ook rechtstreeks aanmaken in de sectie **Velden voor persoonlijke gegevens** van een dataset.

## Het formulier van het gegevensveld invullen

| Veld | Inhoud |
| --- | --- |
| **Naam** | De naam van het veld, verplicht. |
| **Interne referentie** | Uw referentie. |
| **Categorie persoonlijke gegevens** | De categorie van persoonsgegevens waartoe het veld behoort. |
| **Niveau van verwerking** | **Standaard** (naam, voornaam, telefoonnummer), **Zeer persoonlijke gegevens** (financiële gegevens, locatie, communicatie) of **Gevoelige gegevens** (raciale of etnische afkomst, politieke opvattingen, religie, gezondheid, seksuele geaardheid). |
| **Wettelijke basis voor inzameling**, **Rechtvaardiging voor het verzamelen van gevoelige gegevens** | Alleen weergegeven voor het niveau **Gevoelige gegevens**: de wettelijke basis die in de lijst is gekozen, en uw rechtvaardiging. |
| **Beschrijving van de gegevens**, **Technische beschrijving** | Een vrije beschrijving en de technische definitie van het veld. |
| **Gegevenstype** | Het generieke type van de gegevens. |

De [aangepaste velden](../../general/custom-fields.md) die voor gegevensvelden zijn gedefinieerd, worden aan het formulier toegevoegd. De werkbalk geeft toegang tot de opmerkingen en taken die aan het veld zijn gekoppeld, tot de activiteitengeschiedenis en, wanneer werkstroomstappen zijn gedefinieerd, tot de werkstroomstap. De knop met het databasepictogram toont de datasets die het veld bevatten.

Het actiemenu van het formulier biedt **Samenvoegen** en **Verwijderen**.

## Gegevensvelden in de lijst vinden

De filters zijn **Categorie persoonlijke gegevens** en **Gegevenstype**. De kolom **Datasets**, standaard verborgen in **Kolommen aanpassen**, kunt u filteren met **Is leeg** of **Is niet leeg**: gebruik ze om de velden te vinden die tot geen enkele dataset behoren.

Bij een selectie kunt u **De werkstroomfase wijzigen**, **Velden bewerken**, **Samenvoegen**, **Exporteren** en **Verwijderen**. Het **Gegevenskwaliteitsinstrument**, in het menu van **Gegevens toevoegen**, detecteert duplicaten. Zie [Elementen samenvoegen](../../general/merge.md).

## Waar gegevensvelden worden gebruikt

Gegevensvelden komen via datasets in uw verwerkingsactiviteiten terecht. Zie [Gegevens en retentie](../../ropa/activity/datasets.md), waar u ook de velden van een dataset aan een verwerkingsactiviteit kunt toevoegen.

{% hint style="warning" %}
Het verwijderen van een gegevensveld verwijdert alle verwijzingen ernaar in datasets definitief. De gekoppelde gesprekken worden verwijderd.
{% endhint %}
