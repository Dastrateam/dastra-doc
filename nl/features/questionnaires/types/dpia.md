---
description: Leer hoe u met Dastra een Privacy Impact Assessment (PIA) of gegevensbeschermingseffectbeoordeling (DPIA) uitvoert.
---

# Effectbeoordeling (PIA / DPIA)

## Over de PIA en de DPIA

Een gegevensbeschermingseffectbeoordeling (DPIA, Data Protection Impact Assessment), ook Privacy Impact Assessment (PIA) genoemd, is een proces dat artikel 35 van de AVG voorschrijft wanneer een verwerking waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van personen.

Een DPIA moet worden uitgevoerd voordat een verwerkingsactiviteit met zulke risico's begint, en worden herzien telkens wanneer de aard van de verwerking aanzienlijk verandert.

## Bepalen of een DPIA nodig is

In Dastra helpt de sectie **Impactanalyse** van elke verwerkingsactiviteit te bepalen of een DPIA vereist is. Ze beoordeelt 9 risicocriteria van het EDPB:

* Evaluatie of scoring, inclusief profilering en voorspellende activiteiten
* Geautomatiseerde besluitvorming met significante gevolgen
* Systematische monitoring
* Gevoelige persoonsgegevens
* Op grote schaal verwerkte gegevens
* Combineren, koppelen of kruisverwijzen van gegevens
* Gegevens over kwetsbare personen
* Innovatief gebruik of toepassing van nieuwe technologieën
* Verwerking die betrokkenen belet hun rechten uit te oefenen

Kies voor elk criterium **Ja**, **Neen** of **Niet van toepassing**. Twee antwoorden **Ja** volstaan doorgaans om een DPIA verplicht te maken, maar afhankelijk van de context kan één criterium volstaan.

Klik naast de titel **Evaluatie van de 9 criteria van de AIPD (CEPD)** op **Genereer de evaluatie** om tijd te winnen: de AI-assistent stelt voor elk criterium een antwoord voor, met een motivering, op basis van de informatie die al in de verwerkingsactiviteit is ingevoerd. U beoordeelt het voorstel voordat u het op het formulier toepast, en elk antwoord blijft bewerkbaar. De gedetailleerde procedure staat op de pagina [Impactanalyse](../../ropa/activity/impact-analysis.md).

{% hint style="info" %}
De lijst van verwerkingsactiviteiten waarvoor een DPIA vereist is, hangt af van de aanbevelingen van uw nationale toezichthoudende autoriteit. Dastra biedt een DPIA-gids met aanbevelingen per land om uw verplichtingen vast te stellen.
{% endhint %}

Dastra toont een van deze twee resultaten:

* **DPIA is niet verplicht**: de verwerking haalt de drempel niet
* **Een DPIA is vereist**: er verschijnt een knop **Maak een DPIA** om de beoordeling rechtstreeks te starten

## PIA- en DPIA-sjablonen in Dastra

In de bibliotheek van Dastra staan verschillende PIA- en DPIA-sjablonen, waaronder:

* **PIA (CNIL) - Privacy Impact Analysis** (57 vragen): het standaard PIA-model van de Franse toezichthouder CNIL, voor één verwerkingsactiviteit
* **PIA (CNIL) - Privacy Impact Analysis (multi-processing)** (57 vragen): het CNIL-model, aangepast voor beoordelingen die meerdere verwerkingsactiviteiten omvatten
* **Privacy impact assessment (PIA)** (114 vragen): een uitgebreid generiek PIA-sjabloon
* **EDPB DPIA Template 2026** (82 vragen): het sjabloon dat het Europees Comité voor gegevensbescherming aanbeveelt
* **DPIA Template for AI Systems** (90 vragen): voor verwerkingsactiviteiten met AI-systemen met een hoog risico (AVG en AI-verordening)
* **DPC DPIA Questionnaire - Ireland** (9 vragen): het sjabloon van de Ierse toezichthouder
* **DPIA Questionnaire (ICO)** (9 vragen): het sjabloon van de Britse toezichthouder
* **US PIA (cross-state)** (86 vragen): voor verwerkingsactiviteiten in de Verenigde Staten

Ga voor deze sjablonen naar het tabblad **Vraagmodellen**, klik op **Maak een sjabloon** en daarna op **Geautomatiseerde audit**, en filter op het type **Gegegevensefffectbeoordeling (Data Protection Impact Assessement)**.

## Structuur van de PIA-vragenlijst (CNIL)

Het PIA-sjabloon (CNIL) is opgebouwd uit drie hoofdonderdelen:

1. Context: beschrijf de verwerkingsactiviteit: algemene informatie, doeleinde, betrokken gegevens, stakeholders (verwerkingsverantwoordelijke, verwerkers, gezamenlijke verwerkingsverantwoordelijken)
2. Basisbeginselen: beoordeel de evenredigheid en de noodzaak van de gegevens en leg de maatregelen vast die de rechten van personen beschermen
3. Risico's voor de gegevensbeveiliging: beoordeel de risico's in vier categorieën van bedreigingen: genomen beveiligingsmaatregelen, onrechtmatige toegang tot gegevens, ongewenste wijziging van gegevens en verdwijnen van gegevens

{% hint style="info" %}
De PIA-vragenlijst (CNIL) kent twee antwoordmodi. Het verschil tussen beide betreft uitsluitend de zichtbaarheid van extra velden per vraag: in de **Uitgebreide modus** worden de velden **Reden voor respons**, **Bijlagen** en **Annotaties** bij elke vraag getoond. In de **Vereenvoudigde modus** zijn deze velden verborgen. U kunt op elk moment van modus wisselen.
{% endhint %}

## Een PIA koppelen aan een verwerkingsactiviteit

Configureer uw PIA-sjabloon als volgt om het meeste uit de PIA-functionaliteit van Dastra te halen:

1. Stel het **Type audit** van het sjabloon in op het type voor effectanalyses. Daarmee schakelt u de risicoheatmap in het dashboard van de vragenlijst in en integreert u de gegevens van de gekoppelde verwerkingsactiviteit.
2. Selecteer in het onderdeel **Geauditeerd element** de optie Verwerking. Zo koppelt u elk PIA-antwoord aan een specifieke verwerkingsactiviteit en wordt het veld **Datum laatste DPIA** van de verwerkingsactiviteit automatisch bijgewerkt wanneer de DPIA wordt gepubliceerd (zie "De datum van de laatste DPIA bijwerken" hieronder).

{% hint style="info" %}
Zodra een PIA aan een verwerkingsactiviteit is gekoppeld, opent u ze rechtstreeks via de sectie **Impactanalyse** van die verwerkingsactiviteit en start u ze met de knop **Maak een DPIA** wanneer de drempel is bereikt.
{% endhint %}

### De datum van de laatste DPIA bijwerken

Wanneer een DPIA die aan een verwerkingsactiviteit is gekoppeld, wordt gepubliceerd, kopieert Dastra de publicatiedatum naar het veld **Datum laatste DPIA** in de stap **Impactanalyse** van de verwerkingsactiviteit. Deze update geldt ongeacht de herkomst van de DPIA (gestart vanuit de verwerkingsactiviteit of gepland vanuit de module Vragenlijsten), op voorwaarde dat het sjabloontype een effectanalyse is en het geauditeerde element een verwerkingsactiviteit.

De publicatie vindt plaats:

* wanneer de laatste verplichte respondent de vragenlijst afrondt, als de validatiestap is uitgeschakeld;
* wanneer de goedkeurders de vragenlijst valideren, in alle andere gevallen.

Een informatiebericht meldt dit op het moment van publicatie:

* in het venster **De audit afronden**: "De datum van de laatste PIA van de bijbehorende verwerking zal worden bijgewerkt.", of "De datum van de laatste PIA van de bijbehorende verwerking zal worden bijgewerkt bij de validatie van dit vragenformulier." wanneer een validatie wordt verwacht;
* in het validatievenster van de vragenlijst: "De datum van de laatste PIA van de bijbehorende verwerking zal worden bijgewerkt."

Vereist de verwerkingsactiviteit een DPIA, dan toont de stap **Impactanalyse** daarna het bericht **Er is een DPIA uitgevoerd**.

{% hint style="info" %}
De publicatiedatum overschrijft elke waarde die al in het veld **Datum laatste DPIA** is ingevoerd.
{% endhint %}

## Een PIA importeren uit de CNIL-tool

Hebt u al een PIA uitgevoerd met de CNIL-tool, dan importeert u die rechtstreeks in Dastra:

1. Exporteer uw PIA uit de CNIL-tool in **.json-indeling**
2. Selecteer in Dastra het PIA-sjabloon (CNIL) en klik op **Importeer PIA vanuit de PIA-tool (CNIL)**
3. Een groot deel van de elementen wordt automatisch in Dastra geïmporteerd

## Een DPIA uitvoeren voor meerdere verwerkingsactiviteiten

Eén DPIA kan meerdere verwerkingsactiviteiten omvatten die vergelijkbaar zijn qua aard, reikwijdte, context, doeleinden en risico's. Gebruik het sjabloon **PIA (CNIL) - Privacy Impact Analysis (multi-processing)**, of configureer uw sjabloon zo dat het niet aan een specifieke verwerkingsactiviteit is gekoppeld. U voert de DPIA dan uit, exporteert ze en voegt ze toe aan de documentatie van de betrokken verwerkingsactiviteiten.

## Verder lezen

{% content-ref url="tia.md" %}
[Transfer Impact Assessment (TIA)](tia.md)
{% endcontent-ref %}

{% content-ref url="lia.md" %}
[Beoordeling van het gerechtvaardigd belang (LIA)](lia.md)
{% endcontent-ref %}
