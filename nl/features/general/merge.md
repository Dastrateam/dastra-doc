---
description: >-
  Met het samenvoeggereedschap voegt u items samen die dubbel zijn of veel
  overeenkomsten hebben.
---

# Elementen samenvoegen

## Wat het samenvoeggereedschap doet

Met het samenvoegen van items in Dastra beheert u duplicaten en vergelijkbare items in uw compliancegegevens. U combineert meerdere identieke of vergelijkbare items tot één item, zonder zelf alle koppelingen met de bijbehorende entiteiten (verwerkingsactiviteiten, verwerkingsverantwoordelijken, registers enzovoort) te hoeven leggen.

Zo blijven uw repositories consistent en beperkt u het handmatige werk.

## Elementen waarop u het samenvoeggereedschap gebruikt

U kunt het samenvoeggereedschap gebruiken voor:

* Verwerkingsactiviteiten
* Activa
* Stakeholders
* Datasets
* Verklarende woordenlijsten voor gegevens
* Maatregelen
* Categorieën van betrokkenen
* Taken
* Compliancecontroles (toegepaste controles en referentiecontroles)
* Compliancetests (operationele tests en referentietests)

{% hint style="info" %}
Compliancecontroles en -tests voegt u samen vanuit de bibliotheek of het project van de module Conformiteit, via groepsacties. U kunt tot 30 items selecteren om samen te voegen. De details van deze bewerking staan op de pagina's [Controles](../compliance/library/controls.md) en [Tests](../compliance/library/tests.md).
{% endhint %}

## Elementen samenvoegen

1. Selecteer in de lijst de elementen die u wilt samenvoegen.

<div align="left"><figure><img src="../../.gitbook/assets/image-416-1.png" alt="Twee geselecteerde elementen in een lijst"><figcaption></figcaption></figure></div>

2. Klik op **Kies een bulkactie** en daarna op **Samenvoegen**.

![Menu met bulkacties met de optie Samenvoegen](<../../.gitbook/assets/audit-questionnaire-icone-oblig-repondue.png>)

3. Vink in het venster **Samenvoeggereedschap** in de kop van de kolom het element aan dat u wilt behouden: het wordt de **Reference version**. De andere kolommen tonen het label **Keep selected fields**: deze elementen worden verwijderd zodra de samenvoeging is bevestigd, en alleen de velden die u erin selecteert, worden overgenomen in de referentieversie.
4. Selecteer voor elk veld dat verschilt de waarde die u wilt behouden.
5. Klik op **Samenvoegen**.

<figure><img src="../../.gitbook/assets/generalites-fusion-tool-differences.png" alt="Venster Samenvoeggereedschap met de referentieversie en de velden die verschillen"><figcaption><p>Het venster Samenvoeggereedschap</p></figcaption></figure>

Om de keuze van de waarden te vergemakkelijken:

* elk veld waarvan de waarde van het ene element tot het andere verschilt, is gemarkeerd met **Different**, en een teller toont het aantal betrokken rijen;
* de tabel toont alleen de rijen die verschillen; schakel **View all fields** in om alle vergelijkbare velden weer te geven. Verborgen identieke velden behouden de waarde van de referentieversie;
* met de knop **Select all** onder de kop van een kolom behoudt u de waarden van die kolom op alle rijen die verschillen; **Undo selection** maakt dat ongedaan. Een lege waarde vervangt nooit een ingevulde waarde, en het aantal bijgewerkte rijen wordt getoond.

{% hint style="info" %}
De entiteiten (verwerkingsactiviteiten, analyses enzovoort) die aan de verwijderde elementen zijn gekoppeld, worden automatisch opnieuw aan de referentieversie gekoppeld, zodat er niets verloren gaat of losraakt in uw register. Het deel **Linked objects kept** van het venster toont hoeveel het er zijn.
{% endhint %}

Wanneer een object wordt bijgewerkt op basis van de antwoorden op een vragenlijst, opent hetzelfde venster met een kolom **Questionnaire’s responses**. Het bestaande object blijft altijd de referentieversie: het behoudt zijn identificatie, zijn geschiedenis en zijn koppelingen.

## Gegevenskwaliteitsinstrument: duplicaten automatisch opsporen

Dastra bevat een gegevenskwaliteitsinstrument dat uw repository automatisch doorzoekt op mogelijke duplicaten, zonder dat u ze eerst handmatig moet selecteren.

### Hoe de automatische opsporing werkt

Het algoritme gebruikt een verklaarbare score: voor elk paar mogelijke duplicaten analyseert het meerdere dimensies (naam, uitgever, organisatorische eenheid, URL, categorie) en kent het een betrouwbaarheidsscore toe. Met die score neemt u een weloverwogen beslissing voordat u iets samenvoegt of verwijdert.

### Ondersteunde modules

Het gegevenskwaliteitsinstrument is beschikbaar voor:

* Activa
* Maatregelen
* Stakeholders
* Datasets
* Verklarende woordenlijsten voor gegevens
* Verwerkingsactiviteiten
* Categorieën van betrokkenen

### Het instrument openen

Klik in elk van deze modules op de knop van het hoofdmenu (⋮ of **Acties**) en selecteer **Gegevenskwaliteitsinstrument**. Alle gedetecteerde duplicaten staan in een lijst met hun betrouwbaarheidsscore. U kunt elk geïdentificeerd duplicaat vervolgens samenvoegen of verwijderen.
