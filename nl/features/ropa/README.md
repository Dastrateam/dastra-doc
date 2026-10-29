---
description: Leer hoe u uw verwerkingsregister opstelt en beheert.
---

# Verwerkingsregister

## Inleiding

Met het verwerkingsregister brengt u uw gegevensverwerkingen in kaart en houdt u overzicht over wat u doet met de betrokken persoonsgegevens. Een volledig register bijhouden is verplicht volgens artikel 30 van de AVG. Het is daarnaast een instrument om uw gegevens beter te begrijpen en de bijbehorende waardeketen te beheersen, van het ontstaan van de gegevens tot het gebruik ervan.

Dastra biedt een register en vragenlijsten die u stap voor stap begeleiden bij het in kaart brengen van uw verwerkingsactiviteiten.

## Het Dastra-register in het kort

Het verwerkingsregister van Dastra voldoet aan alle wettelijke vereisten. Beide registers, dat van de verwerkingsverantwoordelijke en dat van de verwerker, steunen op repositories (stakeholders, activa, datasets, gegevens, risico's en beveiligingsmaatregelen). Daarmee brengt u uw verwerkingsactiviteiten in kaart en bespaart u tijd in het dagelijkse beheer.

Verwerkingsactiviteiten kunnen worden gekopieerd en sjablonen voor verwerkingsactiviteiten staan in een bibliotheek die voor alle gebruikers vrij toegankelijk is. Een workflow is ingebouwd, zoeken is standaard beschikbaar en u exporteert verwerkingsactiviteiten in verschillende indelingen (PDF, Word, HTML, Excel, CSV, JSON, Markdown) en importeert ze uit CSV-, Excel- of JSON-bestanden. U kunt ook documenten, datalekken of risico's aan uw verwerkingsactiviteiten koppelen.

<figure><img src="../../.gitbook/assets/ropa-readme-1.png" alt="Lijst van verwerkingsactiviteiten met de indicatortegels en de werkbalk"><figcaption><p>Het verwerkingsregister: bovenaan de indicatortegels, daaronder de lijst van verwerkingsactiviteiten</p></figcaption></figure>

## Register van de verwerkingsverantwoordelijke en register van de verwerker

Artikel 30 van de AVG bevat specifieke verplichtingen voor het register van de verwerkingsverantwoordelijke en voor het register van de verwerker. Als uw organisatie zowel als verwerker als als verwerkingsverantwoordelijke optreedt, moet uw register de twee categorieën activiteiten duidelijk onderscheiden.

In dat geval raadt de Franse toezichthouder CNIL aan twee registers bij te houden:

1. een register voor de verwerkingen van persoonsgegevens waarvoor u zelf verantwoordelijk bent,
2. een register voor de verwerkingen die u als verwerker uitvoert namens uw klanten.

{% content-ref url="controller.md" %}
[Register van de verwerkingsverantwoordelijke](controller.md)
{% endcontent-ref %}

{% content-ref url="processor.md" %}
[Register van de verwerker](processor.md)
{% endcontent-ref %}

## De methoden om het verwerkingsregister op te stellen

U kunt het register op twee manieren opbouwen:

* Top-down: u begint met een inventaris van de gegevensverwerkingen en verzamelt daarna per verwerkingsactiviteit de specifieke informatie (gegevens, verwerkers enzovoort).
* Bottom-up: u begint met een inventaris van de gegevens (software, datasets en velden met persoonsgegevens) en maakt daaruit de verwerkingsactiviteiten aan.

### De juiste methode kiezen

Er is geen juiste of foute methode: alles hangt af van de context van uw organisatie, de vaardigheden van het DPO-team, de bereikbaarheid van de mensen die de gegevens gebruiken, enzovoort.

Deze tabel vergelijkt de twee benaderingen:

<table><thead><tr><th width="129">Methode</th><th width="178">Doelgroep</th><th>Voordelen</th><th>Nadelen</th></tr></thead><tbody><tr><td>Top-down</td><td>Kleine organisaties of lokale overheden<br>Bedrijven met een zwakke datacultuur<br>Juridische teams met weinig affiniteit met IT</td><td>Snel op te zetten<br>Minder werk<br>Sluit goed aan op de juridische verwachtingen van de AVG</td><td>Kan lastig zijn als het team dat het register opstelt de gegevens van de organisatie niet kent<br>Veeleisender voor operationele medewerkers<br>De gegevensinventaris is veel minder waardevol, omdat ze alleen voor juridische doeleinden is gemodelleerd<br>Op lange termijn complexer te onderhouden</td></tr><tr><td>Bottom-up</td><td>Grote of middelgrote organisaties<br>Met een sterke datacultuur<br>Juridische teams met sterke affiniteit met IT</td><td>Een inventaris van de gegevens is minder abstract dan rechtstreeks verwerkingsactiviteiten aanmaken<br>Het register weerspiegelt de werkelijkheid van de organisatie<br>Het register is op lange termijn gemakkelijker te onderhouden<br>Meer medewerkers van de organisatie zijn betrokken<br>Verwerkingsactiviteiten worden meer geautomatiseerd aangemaakt</td><td>Over het geheel moeilijker en tijdrovender om in te voeren<br>Het project vraagt om goede governance</td></tr></tbody></table>

Dastra ondersteunt beide benaderingen. Voor een top-down aanpak maakt u verwerkingsactiviteiten aan [op basis van sjablonen](templates.md). Kiest u voor de bottom-up aanpak, [bouw dan eerst uw datamap](../mapping/README.md) en maak daarna een verwerkingsactiviteit rechtstreeks aan vanuit een activum (software, database).

## Uw verwerkingsregister opzetten

Wilt u weten hoe u uw verwerkingsregister ontwerpt en beheert, begin dan hier:

{% content-ref url="establish.md" %}
[Uw register opzetten](establish.md)
{% endcontent-ref %}

Wilt u weten hoe u één van uw verwerkingsactiviteiten opstelt en beheert, begin dan hier:

{% content-ref url="declare.md" %}
[Een verwerkingsactiviteit aanmaken](declare.md)
{% endcontent-ref %}

Wilt u de verschillende stappen van de vragenlijst begrijpen, lees dan:

{% content-ref url="activity/README.md" %}
[Een verwerkingsactiviteit invullen](activity/README.md)
{% endcontent-ref %}

Wilt u weten hoe u het verwerkingsregister deelt, lees dan:

{% content-ref url="share.md" %}
[Het verwerkingsregister delen](share.md)
{% endcontent-ref %}

## Acties uitvoeren op meerdere verwerkingsactiviteiten tegelijk

Vink in de weergave **Tabel** de vakjes links van de verwerkingsactiviteiten aan waarmee u wilt werken. Boven de lijst verschijnt dan de knop **Kies een bulkactie**. Afhankelijk van uw rechten en van de functies die in uw werkruimte zijn ingeschakeld, biedt die de volgende acties:

* **De werkstroomfase wijzigen**
* **Exporteren**
* **Actoren koppelen**: stakeholders of ontvangers toevoegen aan of verwijderen van alle geselecteerde verwerkingsactiviteiten
* **Velden bewerken**: de waarde van een of meer velden op alle geselecteerde verwerkingsactiviteiten wijzigen
* **Samenvoegen**: zie [Elementen samenvoegen](../general/merge.md)
* **Vragenlijsten versturen**
* **Beoordeling**
* **Delen**
* **Verplaats naar de prullenbak**

## Meer informatie

{% content-ref url="../../gdpr/concepts/ropa.md" %}
[Register van verwerkingen](../../gdpr/concepts/ropa.md)
{% endcontent-ref %}

{% content-ref url="../risks/attach-to-processing.md" %}
[Risico koppelen aan een Verwerking](../risks/attach-to-processing.md)
{% endcontent-ref %}

{% content-ref url="../tasks/README.md" %}
[Planning](../tasks/README.md)
{% endcontent-ref %}
