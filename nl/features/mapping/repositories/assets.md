---
description: >-
  Inventariseer de software, servers en andere dragers van uw persoonsgegevens,
  beschrijf elk actief en maak er een verwerkingsactiviteit van aan.
---

# Activa

Activa zijn de elementen die u helpen gegevens te beheren: gegevensdragers, gebouwen en materiële of immateriële uitrusting. Deze repository bevat de activa, binnen of buiten de organisatie (toepassingen, middelen, gebouwen enzovoort).

Gebruik ze om de toepassingen, software en andere items vast te leggen die als gegevensdrager dienen. Gebruikt u bijvoorbeeld klantrelatiebeheersoftware zoals een CRM, voeg die dan aan deze lijst toe. Zo houdt u uw gegevensdragers onder controle en koppelt u ze aan uw gegevenscatalogus.

{% hint style="info" %}
Activa zijn niet noodzakelijk aan verwerkers gekoppeld. Een actief kan bijvoorbeeld software zijn die op uw eigen server is geïnstalleerd, zonder dat de uitgever betrokken is bij de verwerking van persoonsgegevens.
{% endhint %}

## Een actief toevoegen

Om een actief toe te voegen, kunt u:

* vertrekken van een sjabloon: klik op de pijl naast de knop **Een app toevoegen** en daarna op **Maak vanuit de bibliotheek**;
* AI gebruiken: klik op de AI-knop links van **Een app toevoegen**, of kies **AI gegenereerd** in het aanmaakvenster (deze optie hangt af van de functies die voor uw organisatie zijn ingeschakeld);
* het actief rechtstreeks in de repository aanmaken: klik op **Een app toevoegen** en kies daarna **Gepersonaliseerd**;
* activa importeren uit een Excel-, CSV- of JSON-bestand: klik op de pijl naast de knop **Een app toevoegen** en daarna op **Importeren**. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md);
* het actief aanmaken vanuit een vragenlijst: hiervoor is een vragenlijstsjabloon van het type **Asset creation** nodig. Zie [Een vragenlijstsjabloon aanmaken](../../questionnaires/templates/README.md).

## Het formulier van het actief invullen

Het formulier van een actief groepeert de volgende informatie.

| Sectie | Veld | Inhoud |
| --- | --- | --- |
| **Algemene informatie** | **Naam van de toepassing**, **Interne referentie** | De naam van het actief en uw interne referentie. |
| | **Organisatie-eenheid** | De eenheid waartoe het actief behoort. Zie hieronder. |
| | **Type activa** | Het type actief, verplicht. |
| | **Eigenaar van het actief** | De gebruiker die verantwoordelijk is voor de implementatie van het actief. De eigenaar wordt bij voorkeur toegewezen aan de vragenlijsten en taken die aan het actief zijn gekoppeld. |
| | **Uitgever** | De organisatie die het actief publiceert, host of beheert. Ze kan als verwerker worden aangeduid wanneer het actief in een verwerkingsactiviteit wordt vermeld. Voorbeeld: de uitgever van Office 365 is Microsoft. |
| | **Beschrijving**, **URL van het privacybeleid** | Een vrije beschrijving en het adres van het privacybeleid van het actief. |
| | **Soort software**, **Status van de software**, **Type host**, **Type ontwikkeling**, **Type ondersteuning**, **Type onderhoud** | Deze zes velden verschijnen wanneer het type actief **Software** is. |
| **Gegevenslokalisatie** | **Land**, **Adres**, **Stad**, **Regio**, **Postcode** | Waar het actief zich bevindt. |
| | **Informatie over de locatie van gegevens** | Vrije tekst om te preciseren waar de gegevens worden gehost. |
| **Datasets** | | De datasets die in het actief worden bewaard. Sla het actief één keer op voordat u ze aanmaakt. |
| **Bijbehorende beveiligingsmaatregelen** | | De beveiligingsmaatregelen van het actief, vaak vermeld in de verwerkersovereenkomst. Kies korte namen zodat u ze van het ene actief naar het andere kunt hergebruiken. |

De [aangepaste velden](../../general/custom-fields.md) die voor activa zijn gedefinieerd, worden aan dit formulier toegevoegd.

De werkbalk van het formulier geeft toegang tot de bijgevoegde documenten, opmerkingen, vragenlijsten, taken, contracten, AI-systemen en risico's die aan het actief zijn gekoppeld, afhankelijk van uw rechten en de ingeschakelde functies. Ze bevat ook:

* **Gekoppelde elementen**: de [generieke relaties](../relationships.md) van het actief, met hun aantal;
* **Gerelateerde verwerkingen**: het aantal verwerkingsactiviteiten dat het actief gebruikt, en hun lijst;
* **Historisch**: de opeenvolgende wijzigingen van het formulier, die u kunt herstellen;
* de terugkerende beoordeling van het actief. Zie [Terugkerende beoordeling (frisheid)](../../regular-review.md).

## Een verwerkingsactiviteit aanmaken vanuit een actief

Met deze actie hergebruikt u de informatie van het actief om een verwerkingsactiviteit voor te bereiden, zodat u ze niet opnieuw invoert.

1. Open het actief.
2. Klik in het actiemenu van het formulier op **Creëer een verwerkingsactiviteit op basis van een actief**.
3. Zijn er verwerkingsactiviteiten voor dit actief voorgesteld, kies er dan een in de lijst, of klik op **Sla deze stap over**.
4. Voer de **Naam van de verwerking** in, kies de **Organisatie-eenheid van bestemming** en klik op **Volgende**.
5. Selecteer de datasets van het actief die in de verwerkingsactiviteit moeten worden hergebruikt en klik op **Volgende**.
6. Controleer de **Samenvatting**: label, beschrijving, datasets, beveiligingsmaatregelen, doeleinden en betrokkenen. Klik op **Creëer een verwerking**.

Om activa achteraf aan een bestaande verwerkingsactiviteit te koppelen, zie de pagina [Activa](../../ropa/activity/assets.md) van de verwerkingsactiviteit.

## Een kopie maken, samenvoegen en verwijderen

Het actiemenu van het formulier biedt **Dupliceren**, **Samenvoegen** en **Verwijderen**. In de lijst detecteert het **Gegevenskwaliteitsinstrument** dubbele activa. Zie [Elementen samenvoegen](../../general/merge.md).

## Een actief aan een organisatorische eenheid koppelen

Standaard is een actief dat in Dastra wordt aangemaakt beschikbaar voor de hele organisatie (globaal bereik). U kunt een actief aan een specifieke organisatorische eenheid koppelen om de zichtbaarheid ervan te beperken tot de gebruikers van die entiteit of afdeling.

Selecteer hiervoor bij het aanmaken of bewerken van het actief de organisatorische eenheid in het veld **Organisatie-eenheid**. Het actief is dan alleen zichtbaar voor gebruikers die toegang hebben tot die organisatorische eenheid.
