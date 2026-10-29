---
description: >-
  Met Dastra maakt u uw eigen regelgevend kader en past u het met behulp van
  kunstmatige intelligentie aan uw behoeften aan.
---

# Een eigen kader aanmaken

## Inleiding

Met een eigen kader bouwt u een conformiteitskader dat is afgestemd op de specifieke context van de organisatie: intern beleid, sectorkader, AI-initiatief, beveiliging, kwaliteit of governance.

Een eigen kader kan:

* helemaal vanaf nul worden opgebouwd,
* of dienen als gemeenschappelijke basis voor meerdere conformiteitsprojecten.

***

## Stap 1: het kader aanmaken

{% columns %}
{% column %}
Bij het aanmaken van een eigen kader geeft de gebruiker op:

* de **Naam van het framework** (bijvoorbeeld _Custom AI_, _AI ISSP - Demo_)
* de **Taal van het framework**, die de standaardtaal van de vereisten en controles bepaalt

Na het aanmaken wordt het kader met de status concept toegevoegd aan de bibliotheek.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-448.png" alt="Venster om een kader aan te maken met de naam en de taal van het kader"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## Stap 2: weergave en beschikbare acties

Een nieuw aangemaakt kader is standaard:

* leeg
* alleen-lezen

### Acties die beschikbaar zijn zolang het kader niet is gewijzigd

* **Exporteren**: het kader ophalen in JSON- of Excel-formaat
* **Dupliceren**: een kopie van het kader maken
* **Verplaats naar de prullenbak**: het kader verwijderen

U kunt niets toevoegen of wijzigen zolang het kader zich niet in de bewerkingsmodus bevindt.

***

## Stap 3: overschakelen naar de bewerkingsmodus

{% columns %}
{% column %}
Om het kader aan te vullen (hoofdstukken, vereisten, controles enzovoort) gaat u als volgt te werk:

1. Klik op **Bewerken**.
2. Het kader schakelt over naar de bewerkingsmodus.

In de bewerkingsmodus kan de gebruiker:

* hoofdstukken aanmaken
* vereisten toevoegen
* het kader stapsgewijs structureren

{% hint style="warning" %}
De bewerkingsmodus is alleen beschikbaar voor een conceptversie. De vereisten van een gepubliceerde versie zijn vergrendeld en de knop **Bewerken** is uitgeschakeld: maak een versie van het kader aan om ze te laten evolueren (zie [Versies van een kader](versions.md)). De naam, het logo en de beschrijving blijven bewerkbaar.
{% endhint %}
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-449.png" alt="Een kader in de bewerkingsmodus"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## Vereisten aanmaken en structureren

Zodra het kader is aangemaakt en in de bewerkingsmodus staat, kan de gebruiker het kader structureren met hoofdstukken en vereisten.
Zo vertaalt u een regelgevend, normatief of intern kader naar elementen die u in Dastra kunt gebruiken.

***

### Structureren met hoofdstukken

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-450.png" alt="Hoofdstukken van een kader"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Met hoofdstukken organiseert u het kader op een leesbare en samenhangende manier.
{% endcolumn %}
{% endcolumns %}

#### Structureringsregels

Dastra staat toe:

* hoofdstukken op het hoogste niveau
* subhoofdstukken

De diepte is bewust beperkt tot maximaal twee niveaus, om:

* de leesbaarheid van het kader te waarborgen
* te complexe structuren te vermijden
* het gebruik van de vereisten in conformiteitsprojecten te vergemakkelijken

#### In te vullen velden

Bij het aanmaken van een hoofdstuk:

* **Referentie**: interne identificatiecode van het hoofdstuk
* **Naam**: functionele titel van het hoofdstuk

{% hint style="info" %}
Goede praktijk: gebruik hoofdstukken om te structureren per hoofdthema (bijvoorbeeld governance, beveiliging, operaties, gebruiksvormen).
{% endhint %}

***

### Een vereiste aanmaken

{% columns %}
{% column %}
Vereisten drukken de conformiteitsverwachtingen uit waaraan de organisatie moet voldoen.
Ze vormen de directe schakel tussen het kader en de operationele controles.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-451.png" alt="Formulier om een vereiste aan te maken"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

#### Beschikbare velden

* **Referentie** (verplicht)\
  Unieke identificatiecode van de vereiste binnen het kader
* **Naam** (verplicht)\
  Beknopte formulering van de vereiste
* **Beschrijving** (optioneel)\
  Details over de verwachte inhoud, de reikwijdte en de doelstellingen van de vereiste

***

### AI-ondersteuning voor de referentie van de vereiste

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-452.png" alt="AI-ondersteuning bij het aanmaken van een vereiste"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Bij het aanmaken van een vereiste biedt Dastra AI-ondersteuning om automatisch een referentie te genereren die past bij:

* de naam van de vereiste
* het bovenliggende hoofdstuk
* de context van het kader
{% endcolumn %}
{% endcolumns %}

Met deze functie kunt u:

* naamconventies harmoniseren
* inconsistenties of dubbels vermijden
* tijd besparen bij het aanmaken van eigen kaders

De gebruiker blijft vrij om de voorgestelde referentie te wijzigen.

***

### Vereisten organiseren en beheren

<figure><img src="../../../../.gitbook/assets/image-476.png" alt="Lijst van vereisten van een kader met samenvattende indicatoren"><figcaption></figcaption></figure>

Eenmaal aangemaakt kunnen vereisten:

* naar een ander hoofdstuk worden verplaatst
* worden verwijderd
* stapsgewijs worden aangevuld

Elke vereiste toont ook indicatoren (koppelingen met controles, risico's en tests), zodat u haar dekkingsniveau beter begrijpt.

***

### Controles aan een vereiste koppelen

{% columns %}
{% column %}
Controles zijn de operationele elementen waarmee u de conformiteit met een of meer vereisten aantoont.

Er zijn twee manieren om controles aan een vereiste te koppelen.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-453.png" alt="Opties om controles aan een vereiste te koppelen"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

#### Optie 1: bestaande controles koppelen

{% columns %}
{% column %}
De gebruiker selecteert een of meer controles die al in de bibliotheek staan en koppelt ze aan de vereiste.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-454.png" alt="Bestaande controles selecteren"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Eén controle kan aan meerdere vereisten worden gekoppeld. Dat bevordert:

* het delen van controles
* de consistentie van het kader
* een betere traceerbaarheid

***

#### Optie 2: controles aanmaken of koppelen met AI

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-455.png" alt="Voorstellen van de AI-assistent voor bestaande en nieuwe controles"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Dastra biedt een AI-assistent waarmee u:

* automatisch relevante bestaande controles identificeert
* zo nodig het aanmaken van nieuwe controles voorstelt

De AI baseert zich op:

* de inhoud van de vereiste
* de context van het kader
* de controles die al in de bibliotheek staan
{% endcolumn %}
{% endcolumns %}

Controles die via AI zijn aangemaakt, kunnen automatisch bevatten:

* hun beschrijving
* hun koppeling aan de vereiste
* de bijbehorende tests

***

### Voordelen van deze aanpak

Met deze aanpak bereikt u:

* een stapsgewijze structurering van het kader
* bewuste overlappingen tussen vereisten
* de aanmaak van transversale controles die meerdere vereisten dekken
* een stevige basis voor risicobeheer en conformiteitsprojecten
