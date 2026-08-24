---
description: >-
  Leer hoe u de gegevenscategorieën en de bijbehorende opslagregels kunt invoeren die specifiek zijn voor een Verwerking.
---

# Gegevens en bewaring

{% embed url="https://www.youtube.com/watch?v=BJSynYF0aDw&list=PL-EvtNdEiDxEUikz6mrcMlKZ54r3RpBLZ&index=6" %}

[**Artikel 30 van de AVG**](https://eur-lex.europa.eu/legal-content/NL/TXT/PDF/?uri=CELEX:32016R0679) vereist ook dat de categorieën van gegevensverwerking worden ingevoerd.

Hiervoor moeten de categorieën van gegevensverwerking worden gedefinieerd. Deze kunnen worden omschreven als routinematig of gevoelig. Er wordt onderscheid gemaakt tussen gegevens die een groter risico vormen voor personen, zoals gegevens met betrekking tot persoonlijke gezondheid, politieke opvattingen of vakbondsactiviteiten. Gegevens met betrekking tot overtredingen of andere maatregelen om een straf ten uitvoer te leggen zijn ook bijzonder beschermd&x20;

Ook het registratienummer (NIR) of socialezekerheidsnummer kan worden beschouwd als gevoelige gegevens.&#x20;

Het verzamelen van gevoelige gegevens is principieel verboden. Alleen de uitzonderingen in [**artikel 9 van de AVG**](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504) staan toe dat ze worden verzameld.

## Datasets

De dataset groepeert de gegevens voor een specifiek element, bijvoorbeeld een tabel in een database of een papieren verzamelformulier.

### Verschillende toepassingen voor datasets

Datasets kunnen op verschillende manieren gebruikt worden:

* **Geval 1**: door **een dataset te koppelen aan één Activa**. In dit geval komt de dataset overeen met de Activa-gegevens en is niet generiek.
* **Geval 2**: door **een dataset te associëren met gegevensverwerking**. Deze dataset kan specifiek zijn voor de gegevensverwerking en wordt niet hergebruikt in een andere gegevensverwerking.
* **Geval 3**: door **generieke gegevensreeksen te koppelen aan de gegevensverwerking**. In dit geval kan de dataset in meerdere gegevensverwerkingen worden hergebruikt.

Om generieke datasets te gebruiken, raden we de volgende procedure aan:

* Open de verwerkingspagina voor de datasets.
* Open een nieuw tabblad op de datasetpagina in de kaart.
* Selecteer de dataset in het venster voor gegevensverwerking.
* Als de dataset gewijzigd moet worden, maak dan een nieuwe aan: ga naar het andere tabblad en dupliceer de generieke dataset door de vereiste velden te verwijderen of toe te voegen.
* Voor meer duidelijkheid raden we je aan om een tag te gebruiken voor deze datasets (zo kun je ze gemakkelijk onderscheiden in de dataset selector). Bijvoorbeeld: een "generieke" tag en een tag voor de toegevoegde of verwijderde gegevens.

#### Datasets zonder velden gebruiken

Het is ook mogelijk om nog generieker te blijven door niet de gegevens te specificeren die bij de dataset horen, maar door de dataset een gegevenscategorie te noemen (wat bijvoorbeeld ook geldig is in de zin van de AVG).

Afhankelijk van het type verwerking kun je verschillende benaderingen kiezen, afhankelijk van hoe gevoelig ze zijn in termen van de rechten en vrijheden van betrokkenen.

### Koppel de bron van de gegevens aan de dataset

In elke dataset kunt u de oorsprong van de gegevens aangeven. Dit kan direct, indirect of beide zijn &#x20;

Met een veld waarin u de oorsprong van de verzameling kunt beschrijven, kunt u de nodige nauwkeurigheid bieden.

<figure><img src="../../../.gitbook/assets/image (10) (2).png" alt=""><figcaption><p>Bron van gegevens</p></figcaption></figure>

### Activa koppelen aan de dataset

Datasets hebben een natuurlijke roeping om te worden toegevoegd aan [Activa](applications.md).&#x20;

U kunt een Activa aan uw dataset koppelen wanneer deze wordt gemaakt.&#x20;

<figure><img src="../../../.gitbook/assets/image (2) (1) (3).png" alt=""><figcaption><p>activakiezer</p></figcaption></figure>

Een dataset kan maar aan één asset worden gekoppeld. Bij het definiëren van de datasets voor een activa zijn ze namelijk uniek &#x20;

Als u bijvoorbeeld boekhoudsoftware als een activum beschouwt, kunnen er verschillende datasets aan dit activum worden gekoppeld, zoals "factureringsgegevens", met gegevens over de module voor het bijhouden van facturen, of "klantgegevens", met gegevens over klantenrekeningen.

### Een categorie van betrokkenen koppelen

Voor elke gegevensset kunt u een of meer categorieën van gegevenssubjecten&#x20 koppelen;

Dit geeft u een beter inzicht in de gegevens die aan de betrokkenen zijn gekoppeld. Het vereenvoudigt ook het mappingproces.&#x20;

<figure><img src="../../../.gitbook/assets/image (3) (1) (3) (2).png" alt=""><figcaption><p>Selector voor gegevensonderwerpcategorie</p></figcaption></figure>

{% hint style="info" %}
Het aangeven van de betrokkenen is handig voor het beheren van [verzoeken tot uitoefening van rechten](../../gerer-les-exercices-des-droits/). U kunt de gegevens waarop het verzoek betrekking heeft gemakkelijk vinden door snel de betreffende gegevensreeksen te identificeren.
{% endhint %}

### Gegevensvelden koppelen

Elke gegevensset moet worden aangevuld met gegevensvelden. Deze velden zijn de gegevens zelf &#x20;

De velden die in de selector worden weergegeven, zijn de velden die beschikbaar zijn in de gegevenswoordenlijst &#x20;

<figure><img src="../../../.gitbook/assets/image (8) (1) (3).png" alt=""><figcaption><p>Gegevensveld selector</p></figcaption></figure>

Als een gegeven nog niet aanwezig is, kun je het direct vanuit deze selector maken om het aan de dataset toe te voegen &#x20;

Velden kunnen worden gecategoriseerd volgens vooraf gedefinieerde categorieën. Dit zijn onder andere de categorieën die worden aanbevolen door de CNIL.

<figure><img src="../../../.gitbook/assets/image (9) (2).png" alt=""><figcaption><p>Selector categorie persoonsgegevens</p></figcaption></figure>

In dit veld kun je ook de aanwezigheid van gevoelige gegevens aangeven. Bijvoorbeeld gezondheidsgegevens of een ander type gevoelige gegevens&#x20;

In dit geval wordt u gevraagd om het verzamelen van deze gegevens te rechtvaardigen en in het bijzonder de rechtsgrondslag hiervoor.

&#x20;

<figure><img src="../../../.gitbook/assets/image (4) (3) (2).png" alt=""><figcaption><p>Gevoelige gegevens</p></figcaption></figure>

{% hint style="info" %}
Deze informatie wordt door de toepassing geanalyseerd om een intelligent criterium te activeren [van PIA](analyse-dimpact.md).&#x20;
{% endhint %}

### Een gegevensbewaringsregel koppelen

In elke dataset kun je een dataretentieregel koppelen.&#x20;

<figure><img src="../../../.gitbook/assets/image (6) (2).png" alt=""><figcaption><p>Retentie tijden</p></figcaption></figure>

Bewaartermijnen worden als standaard beschouwd omdat ze op het niveau van de Verwerking kunnen worden aangepast (zie hieronder).

Je kunt een bewaarperiode toevoegen voor een actieve database, een tussentijds archief of een zuiveringsregel.

De actieve basis is de huidige verwerkingsbasis. Tussenarchivering is een beperktere vorm van opslag. Met het veld "purge" kun je de voorwaarden beschrijven voor het verwijderen van gegevens of het verzenden voor definitieve archivering.

## Gegevensbehoud

Beperkte gegevensbewaring is een van de algemene beginselen van de wet op persoonsgegevens en is vastgelegd in [**artikel 5 1. e) van de AVG**](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504). Hierin staat dat "gegevens in een vorm die het mogelijk maakt de betrokkenen te identificeren, niet langer mogen worden bewaard dan noodzakelijk is voor de verwezenlijking van de doeleinden waarvoor zij worden verwerkt".

Praktisch gezien betekent dit dat wanneer gegevensverwerking plaatsvindt, we moeten nadenken over wat er met de gegevens gebeurt nadat het doel is bereikt. De gegevens moeten ofwel permanent worden vernietigd, anoniem worden gemaakt of worden verwerkt voor een nieuw, compatibel doel&#x20;

De bewaartermijn hangt af van het doel van de gegevensverwerking en de aard van de gegevens. Bewaartermijnen kunnen worden gedefinieerd op basis van het type gegevens. Voor salarisadministratie worden gegevens met betrekking tot de loonstrook bijvoorbeeld 1 maand bewaard in de actieve database en 5 jaar in het tussenliggende archief, terwijl gegevens met betrekking tot de betalingsopdracht worden bewaard gedurende de tijd die nodig is om de loonstrook uit te geven in de actieve database en 10 jaar na sluiting in het tussenliggende archief&#x20;

De bewaartermijn kan worden uitgedrukt in een waarde of, indien dit niet mogelijk is, in de criteria die worden gebruikt om de bewaartermijn te definiëren (bijvoorbeeld tot uitschrijving). Het wordt aanbevolen, met name door de CNIL in haar **aanbeveling van 11 oktober 2005 over elektronische archivering in de privésector**, om procedures in te stellen voor het beheer van bewaartermijnen op het niveau van gegevenscategorieën en, in het bijzonder, voor het beheer van het wissen of vernietigen van gegevens.

#### Bewaarregels aanpassen voor een dataset

De gegevensvelden in een generieke dataset kunnen niet per Verwerking verschillen. De bewaarperiode kan echter wel verschillen. Het is zelfs mogelijk om de bewaartermijn voor een dataset aan te passen aan de Verwerking. Op deze manier wordt er geen rekening meer gehouden met de bewaarperiode van de gegevensset &#x20;

Om dit te doen, moet je de dataset toevoegen aan de Verwerking. In de lijst met datasets moet je klikken op de knoppen "actieve basis/...".

<figure><img src="../../../.gitbook/assets/image (4) (1) (5).png" alt=""><figcaption><p>"Base activa"</p></figcaption></figure> knop.

Je ziet nu het aanpassingsvenster verschijnen.&#x20;

<figure><img src="../../../.gitbook/assets/image (11).png" alt=""><figcaption><p>Duur aanpassen venster</p></figcaption></figure>

Wanneer de bewaartermijn op het niveau van de Verwerking wordt aangepast, verschijnt er een klein pennetjeslogo op de betreffende knop:&#x20;

Het uiteindelijke doel kan zijn om het gebruik van generieke gegevensreeksen te beperken en over te gaan op nauwkeuriger kartering via gegevensverwerking (geval 2) of via Activa (geval 1).

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (2) (4).png" alt=""><figcaption><p>Aangepaste duur op Verwerking</p></figcaption></figure>



####

##

\
