---
description: >-
  Het samenvoeggereedschap voegt items samen die dubbel zijn of veel op elkaar
  lijken, en het gegevenskwaliteitsinstrument spoort ze voor u op.
---

# Elementen samenvoegen

## Wat het samenvoeggereedschap doet

Met het samenvoegen van items in Dastra combineert u meerdere identieke of vergelijkbare items tot één item, zonder zelf alle koppelingen met de bijbehorende entiteiten (verwerkingsactiviteiten, verwerkingsverantwoordelijken, registers enzovoort) te hoeven leggen. Zo blijven uw repositories consistent en beperkt u het handmatige werk.

## Elementen die u kunt samenvoegen

Het samenvoeggereedschap is beschikbaar voor:

* Verwerkingsactiviteiten
* Activa
* Stakeholders
* Datasets
* Gegevensvelden (verklarende woordenlijst voor gegevens)
* Beveiligingsmaatregelen
* Categorieën van betrokkenen
* Taken
* Compliancecontroles (toegepaste controles en referentiecontroles)
* Compliancetests (operationele tests en referentietests)
* Risicoscenario's en bedreigingen van de compliancebibliotheek

{% hint style="info" %}
Controles, tests, risicoscenario's en bedreigingen voegt u samen vanuit de bibliotheek of het project van de module Conformiteit. De details van deze bewerking staan op de pagina's [Controles](../compliance/library/controls.md), [Tests](../compliance/library/tests.md), [Risico's](../compliance/library/risks.md) en [Bedreigingen](../compliance/library/threats.md).
{% endhint %}

## Elementen samenvoegen

1. Selecteer in de lijst de elementen die u wilt samenvoegen. Selecteer minder dan 30 elementen.
2. Klik op **Kies een bulkactie** en daarna op **Samenvoegen**.

<figure><img src="../../.gitbook/assets/general-merge-1.png" alt="Lijst met twee geselecteerde elementen en het menu Kies een bulkactie geopend op Samenvoegen"><figcaption><p>Twee geselecteerde elementen en de bulkactie Samenvoegen</p></figcaption></figure>

3. Kies in het venster **Samenvoeggereedschap** het element dat u wilt behouden door het in de kop van de kolom te selecteren: het wordt de **Reference version**. De andere kolommen tonen het label **Keep selected fields**: deze elementen worden verwijderd zodra de samenvoeging is bevestigd, en alleen de velden die u erin selecteert, worden overgenomen in de referentieversie.
4. Selecteer voor elk veld dat verschilt de waarde die u wilt behouden.
5. Klik op **Samenvoegen**.

<figure><img src="../../.gitbook/assets/generalites-fusion-tool-differences.png" alt="Venster Samenvoeggereedschap met de referentieversie en de velden die verschillen"><figcaption><p>Het venster Samenvoeggereedschap</p></figcaption></figure>

U kunt ook vertrekken vanuit één element: klik in het actiemenu op **Samenvoegen**, selecteer de objecten waarmee u de gegevens wilt samenvoegen en klik op **Volgende**.

Om de keuze van de waarden te vergemakkelijken:

* elk veld waarvan de waarde van het ene element tot het andere verschilt, is gemarkeerd met **Different**, en een teller toont het aantal betrokken rijen;
* de tabel toont alleen de rijen die verschillen; schakel **View all fields** in om alle vergelijkbare velden weer te geven. Verborgen identieke velden behouden de waarde van de referentieversie;
* met de knop **Select all** onder de kop van een kolom behoudt u de waarden van die kolom op alle rijen die verschillen; **Undo selection** maakt dat ongedaan. Een lege waarde vervangt nooit een ingevulde waarde.

{% hint style="info" %}
De entiteiten (verwerkingsactiviteiten, analyses, taken enzovoort) die aan de verwijderde elementen zijn gekoppeld, worden automatisch opnieuw aan de referentieversie gekoppeld, zodat er niets verloren gaat of losraakt in uw register. Het deel **Linked objects kept** van het venster toont hoeveel het er zijn.
{% endhint %}

Wanneer een object wordt bijgewerkt op basis van de antwoorden op een vragenlijst, opent hetzelfde venster met een kolom **Questionnaire’s responses**. Het bestaande object blijft altijd de referentieversie: het behoudt zijn identificatie, zijn geschiedenis en zijn koppelingen.

## Gegevenskwaliteitsinstrument

Het **Gegevenskwaliteitsinstrument** doorzoekt uw repository op items die waarschijnlijk duplicaten zijn, zonder dat u eerst iets hoeft te selecteren. Daarna stelt het voor ze samen te voegen met het samenvoeggereedschap.

### Toegang tot het instrument

Het instrument is beschikbaar in de lijsten met verwerkingsactiviteiten, stakeholders, activa, gegevensvelden, datasets en beveiligingsmaatregelen. Het wordt niet aangeboden voor categorieën van betrokkenen, die u wel vanuit de lijst kunt samenvoegen.

Klik in de lijst rechtsboven op de pijl van de knop voor aanmaken (bijvoorbeeld **Maak een gegevensverwerking**) en daarna op **Gegevenskwaliteitsinstrument**. Voor deze actie hebt u schrijftoegang tot de module nodig.

### Slimme detectie

Het tabblad **Slimme detectie** voert een gelijkenisanalyse uit (Levenshtein-afstand en Jaccard-index) en bewaart de waarschijnlijke duplicaten als suggesties. De analyse start vanzelf wanneer u het tabblad voor het eerst opent; klik op **Start de analyse** om haar opnieuw uit te voeren.

<figure><img src="../../.gitbook/assets/general-merge-2.png" alt="Tabblad Slimme detectie van het gegevenskwaliteitsinstrument met de lijst met suggesties, hun betrouwbaarheidsscore en hun acties"><figcaption><p>De suggesties voor duplicaten in het tabblad Slimme detectie</p></figcaption></figure>

Elke suggestie koppelt twee registraties (**Registratie A** en **Registratie B**). Het algoritme vergelijkt vooral het label en daarna, afhankelijk van het type element, de beschrijving, het adres, het e-mailadres, het telefoonnummer of de definitie. Het leidt daaruit een score **Vertrouwen** af van 0 % tot 100 %, die u kunt lezen voordat u iets samenvoegt. Een rood pictogram **UO verschillend** wijst op twee registraties die aan verschillende organisatorische eenheden zijn gekoppeld.

Voor elke suggestie geldt:

* **Samenvoegen** opent het samenvoeggereedschap met de twee registraties;
* **Negeren** legt de suggestie opzij: de status wordt **Genegeerd** en de analyse stelt ze niet opnieuw voor;
* **In afwachting zetten** zet een genegeerde suggestie terug bij de suggesties met de status **In afwachting**.

U kunt de lijst filteren op status (**Alle statussen**, **In afwachting**, **Genegeerd**). Het instrument verwijdert nooit zelf een duplicaat: alleen de elementen die u bij een samenvoeging niet behoudt, worden verwijderd.

### Exacte overeenkomst

Het tabblad **Exacte overeenkomst** groepeert de registraties die dezelfde waarde hebben in de kolom van uw keuze. Selecteer de kolom en klik naast een groep op **Samenvoegen** om het samenvoeggereedschap te openen.
