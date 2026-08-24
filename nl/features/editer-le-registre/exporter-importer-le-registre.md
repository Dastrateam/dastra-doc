---
description: Leer hoe je een compleet bestaand register kunt exporteren en importeren in Dastra.
---

# Register exporteren / importeren

## Register exporteren

Om het hele register te exporteren, ga je naar de module "Register", klik je op het pijltje rechtsboven naast het aanmaken van een Verwerking en selecteer je "register exporteren".

Kies dan het export formaat en het type export dat je wilt (volledig of artikel 30 formaat), en klik op "Download het bestand". Dat is het, je register is geëxporteerd!



### Artikel 30/CNIL-formaat

Het zogenaamde artikel 30-formaat komt overeen met wat de AVG vereist. De export houdt rekening met de verplichte velden zoals gedefinieerd door de AVG. De AVG vereist de creatie van een register van de verwerkingsactiviteiten. De informatie die het bevat is:&#x20;

* Naam van de Verwerking
* Doeleinden (zonder rechtsgrondslag)
* Gegevens en opslag
* Ontvangers en mogelijke doorgiften
* Beveiligingsmaatregelen



### Volledig formaat

Het volledige formaat is het native formaat van Dastra. U exporteert alle velden waaruit het formulier voor de Verwerking bestaat &#x20;



{% hint style="info" %}
Het is ook mogelijk om alleen één of meer Verwerkingen uit het register te exporteren, in plaats van het hele register. Selecteer hiervoor handmatig de betreffende Verwerkingen door de vakjes links van het register aan te vinken, vervolgens "Kies een gegroepeerde actie" en "Exporteren".
{% endhint %}

## Register importeren

Om te voorkomen dat elke Verwerking handmatig moet worden ingevuld en om rekening te houden met alle mogelijke registerformaten, heeft Dastra een methodologie ontworpen die gebaseerd is op het principe **van het opsplitsen van het register in gegevensdomeinen**. Er zijn 7 aanbevolen stappen voor het importeren van een bestaand register in Dastra.

{% hint style="info" %}
Deze stappen zijn niet verplicht, maar worden toch sterk aanbevolen, vooral als het register van de Verwerking een groot aantal processen bevat.
{% endhint %}

U kunt ook onze bibliotheek met modellen voor gegevensverwerking raadplegen: [https://www.dastra.eu/en/data-processing/referentials](https://www.dastra.eu/en/data-processing/referentials)

## Stap 1: Verwerkingslabels importeren

Om uw bestaande gegevensverwerkingslabels te importeren, klikt u op het tabblad "Uw gegevens importeren" in de sectie Register:

![](<../../.gitbook/assets/image (10) (1) (1).png>)

Download vervolgens een voorbeeld van ons bestand zoals op het scherm te zien is.

![](<../../.gitbook/assets/image (11) (1) (1).png>)



Vul het gedownloade bestand in met je labels voor de Verwerking in de volgende volgorde:

| Colonne          | Beschrijving                          | Mogelijke waarden                                 |
| ---------------- | ------------------------------------- | --------------------------------------------------- |
| Ref              | Interne referentie (string)            |                                                     |
| Verwerkingstoestand | Verwerkingstoestand (string) | "Studie", "Wordt geïmplementeerd", "In productie", "Gestopt" |
| Label            | Naam(string)                          |                                                     |
| Beschrijving      | Beschrijving (string)                  |      


Hieronder staat een voorbeeld van een bestand in het vereiste formaat dat beschikbaar is voor import en in Dastra kan worden geïmporteerd met drag & drop:

{% file src="../../.gitbook/assets/sample-DataProcessing (18).csv" %}

Importeer het direct in onze interface met drag & drop, klik dan op Doorgaan &#x20;

Dat is het, uw labels voor de Verwerking zijn geïmporteerd!

## Stap 2: Activa importeren

Om uw bestaande Activa te importeren, klikt u op het tabblad "importeren" in de module Repositories, tabblad Activa:

![](<../../.gitbook/assets/image (92).png>)

Upload vervolgens een voorbeeld van ons bestand zoals op het scherm te zien is. Vul het gedownloade bestand in met uw toepassingen in de volgende volgorde:

| Kolom | Beschrijving | Mogelijke waarden |
| -------------------------- | --------------------------------------- | --------------------------------------- |
| Beschrijving (tekenreeks)
| Label Naam (string)
| ApplicationState | Toestand van de toepassing (applicationstate) | "In productie""In ontwikkeling""Gestopt" |
| ApplicationType | Type toepassing (toepassingstype) | "Software""WebApp""Saas""Module""Overige" |
| HostingType | Type hosting (hostingtype) | "InHouse""OutSourced" |
| SupportType | Type ondersteuning (supporttype) | "InHouse""OutSourced" |
| DevelopmentType | Type ontwikkeling (developmenttype) | "InHouse""OutSourced" |
| HostName | Hostnaam (string) |
| PrivacyByDesignImplemented | Privacy by design geïmplementeerd (booleaans) | "true""false" |

Hieronder staat een voorbeeld van een bestand in het vereiste formaat dat beschikbaar is voor import en in Dastra kan worden geïmporteerd met drag & drop:

{% file src="../../.gitbook/assets/sample-applications - EXAMPLE.xlsx" %}

Importeer het direct in onze interface met drag & drop, klik dan op Doorgaan &#x20;

Dat is het, je applicaties zijn geïmporteerd!

## Stap 3: Importeer de speler-repository

Herhaal de procedure vergelijkbaar met de vorige vanuit de module Repositories, tab Actors. Hieronder staat een voorbeeld:

{% file src="../../.gitbook/assets/sample-Asset.csv" %}

Je stakeholder repository verwijst naar alle partijen die betrokken zijn bij een Verwerking. Juridische entiteiten zoals onderaannemers, klanten of gezamenlijke verwerkingsverantwoordelijken, of natuurlijke personen zoals verwerkingsverantwoordelijken&#x20;

Dit archief dient als een interne map in de werkruimte. Je kunt voor elke Actor een type definiëren. Als u bijvoorbeeld uw archief van onderaannemers wilt toevoegen, voegt u alle actoren toe en moet elke onderaannemer aan een proces worden gekoppeld&#x20;

## Stap 4: Importeer de beveiligingsmaatregelen opslagplaats

Herhaal de procedure vergelijkbaar met de vorige vanuit de module Repositories, tabblad Measures.

## Stap 5: Importeer de data glossary &#x20;

Herhaal de procedure zoals eerder beschreven in de module Repositories, tabblad Data glossary.

## Stap 6: Importeer de gegevensverzameling&#x20;

Herhaal de procedure zoals hierboven beschreven vanuit de sectie Register, tabblad Bewaarregels.

## Stap 7: Bouw koppelingen&#x20;

Nu alle repositories zijn geïmporteerd, bewerk je elk van de Verwerkingen en vul je de informatie in op basis van de geïmporteerde informatie volgens de onderstaande gids:

{% content-ref url="remplir-le-questionnaire/" %}
[de vragenlijst invullen](remplir-le-questionnaire/)
{% endcontent-ref %}

Dat is het, de links zijn gemaakt!
