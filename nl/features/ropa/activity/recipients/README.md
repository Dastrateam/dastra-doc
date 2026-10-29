---
description: Geef aan wie de ontvangers van de gegevensverwerking in de activiteit zijn.
---

# Ontvangers

[Artikel 30, lid 1, onder d), van de AVG](https://gdpr-info.eu/art-30-gdpr/) bepaalt dat het register "_de categorieën van ontvangers aan wie de persoonsgegevens zijn of zullen worden verstrekt, onder meer ontvangers in derde landen of internationale organisaties_" moet vermelden.

[Artikel 4 van de AVG](https://gdpr-info.eu/art-4-gdpr/) definieert de ontvanger als "_een natuurlijke persoon of rechtspersoon, een overheidsinstantie, een dienst of een ander orgaan aan wie/waaraan de persoonsgegevens worden verstrekt, al dan niet een derde. Overheidsinstanties die mogelijk persoonsgegevens ontvangen in het kader van een bijzonder onderzoek overeenkomstig het Unierecht of het lidstatelijke recht, worden echter niet als ontvanger beschouwd; de verwerking van die gegevens door die overheidsinstanties is in overeenstemming met de gegevensbeschermingsregels die van toepassing zijn op het doel van de verwerking_".

Met andere woorden: de term ontvangers omvat alle entiteiten die toegang krijgen tot de gegevens, behalve overheidsinstanties (bevoegde derden zoals een toezichthoudende autoriteit, de gerechtelijke politie in het kader van een gerechtelijk onderzoek of de belastingdienst). Daartoe behoren de interne afdelingen van de verwerkingsverantwoordelijke (bijvoorbeeld de HR-afdeling), verwerkers, gezamenlijke verwerkingsverantwoordelijken en andere verwerkingsverantwoordelijken (bijvoorbeeld zakelijke partners).

## Een ontvanger toevoegen

1. Klik in de sectie **Ontvangers** op **Nieuwe ontvanger**.
2. Selecteer in **Categorie** het type ontvanger: **Interne ontvanger**, **Verwerker**, **Derde: externe organisatie**, **Geautoriseerde derden**, **Gezamenlijke verwerkingsverantwoordelijke** of **Persoon die betrokken is bij de verwerking**.
3. Identificeer de ontvanger:
   * **Referentielijst van actoren (aanbevolen)**: selecteer een stakeholder uit uw stakeholderlijst of maak een nieuwe aan. Met de ontvanger in de lijst kunt u de verwerkingsactiviteiten in kaart brengen die met deze stakeholder samenhangen.
   * **Selecteer een afdeling of entiteit**: selecteer een van uw organisatorische eenheden, bijvoorbeeld een interne afdeling.
   * **Vrij veld**: voer een vrije omschrijving in. Deze optie is niet beschikbaar voor verwerkers. Voor de categorie **Persoon die betrokken is bij de verwerking** is het de enige optie.
4. Beschrijf eventueel in **Beschrijf de bewerkingen die op de gegevens zijn uitgevoerd** wat de ontvanger met de gegevens doet.
5. Heeft de ontvanger toegang tot de gegevens, schakel dan **Heeft de ontvanger toegang tot de gegevens?** in en geef aan of de ontvanger **Alle datasets (standaard)** of **Toegang tot bepaalde datasets** heeft. Selecteer in het tweede geval de betreffende datasets.
6. Worden de gegevens buiten de EU doorgegeven, leg de doorgifte dan vast in hetzelfde paneel (zie [Doorgifte van gegevens buiten de EU](transfers.md)).
7. Klik op **Toevoegen**.

{% hint style="info" %}
Dastra helpt u de lijst aan te vullen:

* de gezamenlijke verwerkingsverantwoordelijken die u in de sectie **Stakeholders** hebt opgegeven, worden getoond als **Voorgestelde ontvangers**: klik op **Toevoegen** om ze toe te voegen;
* wanneer u een verwerker selecteert waarvan de volgende verwerkers in de stakeholderlijst zijn vastgelegd, kunt u die tegelijk toevoegen onder **Voeg gerelateerde subverwerkers toe**;
* wanneer de geselecteerde stakeholder of organisatorische eenheid in een ander land is gevestigd, stelt Dastra voor een doorgifte toe te voegen.
{% endhint %}

De ontvangers worden getoond met hun **Categorie** en hun **Doorgiften**. Gebruik **Reorganiseren door** om ze op naam of op categorie te sorteren. Via het menu **...** van een ontvanger kunt u, afhankelijk van de categorie, de ontvanger **Bewerken**, de bijbehorende stakeholder openen met **De gekoppelde actor bewerken**, **Voeg een volgende processor toe**, **Stuur een vragenlijst naar je subcontractant** of de ontvanger **Verwijderen**.

## Een volgende verwerker toevoegen

Een verwerker kan zelf andere verwerkers inzetten om de gegevens te verwerken. Om die vast te leggen opent u het menu **...** van een ontvanger van de categorie **Verwerker** en klikt u op **Voeg een volgende processor toe**. De volgende verwerker wordt onder zijn verwerker weergegeven.

## Een leverancier beoordelen

Klik in het menu **...** van een ontvanger die in de lijst is geregistreerd op **Stuur een vragenlijst naar je subcontractant** om deze stakeholder met een vragenlijst te beoordelen.

## Een DPA genereren

Als u de module Contracten gebruikt, kunt u rechtstreeks vanuit de verwerkingsactiviteit een verwerkersovereenkomst (DPA) genereren. In de lijst van ontvangers verschijnt een knop **DPA** bij de verwerkers van een activiteit als verwerkingsverantwoordelijke die in de lijst zijn geregistreerd. Deze knop opent de contractgeneratie met het DPA-sjabloon, al ingevuld met de verwerkingsactiviteit en de verwerker. Dezelfde actie staat in het menu **...** (**Genereer een VWO**).

Wanneer er voor een verwerker, of voor een derde van een activiteit als verwerkingsverantwoordelijke, een doorgifte is vastgelegd, genereert de knop **SCC transfer** op dezelfde manier de bijbehorende standaardcontractbepalingen.

{% content-ref url="../../../contracts/templates.md" %}
[Contractsjablonen](../../../contracts/templates.md)
{% endcontent-ref %}
