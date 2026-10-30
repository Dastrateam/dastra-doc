---
description: >-
  Maak aangepaste rapporten op basis van Dastra-gegevens: tabellen, metrieken,
  dimensies, filters, grafieken, exports en delen.
---

# Aangepaste rapportage

Met aangepaste rapporten haalt u de informatie die u nodig hebt uit de Dastra-gegevens, in de vorm die u kiest: tabel, grafiek of export.

## Snel aan de slag

1. Klik in het linkermenu onder **Resources** op **Rapportages**.
2. Rapporten zijn in categorieën ingedeeld. Voordat u uw eerste rapport aanmaakt, moet u **een eerste categorie aanmaken** met **Create Category**.
3. Klik op **Create Report** om een leeg rapport op te bouwen, of open de pijl van de knop en kies **Maak vanuit de bibliotheek**.

Is AI-analyse inbegrepen in uw abonnement, dan genereert de AI-knop naast **Create Report** (**Genereer een op maat gemaakt rapport met de IA**) een rapport op basis van een korte beschrijving, bijvoorbeeld "Aantal verwerkingen per werkstroomstap met een grafiek".

## Woordenlijst

* **Metriek**: een meetbare waarde waarmee u elementen groepeert (aggregeert). _Voorbeeld: het aantal verwerkingsactiviteiten, de gemiddelde verwerkingstijd van een taak enzovoort._
* **Dimensie**: anders dan een metriek aggregeert een dimensie geen gegevens. Het is een eenvoudige eigenschap (een kolom) van een item. _Voorbeeld: de naam van de verwerkingsactiviteit, de status, de referentie enzovoort._

## Een rapport opbouwen

Een rapport wordt in vier stappen opgebouwd:

1. **Gegevensselectie**: kies de tabellen die u wilt bevragen en daarna de relevante metrieken en dimensies.
2. **Filters**: verfijn uw resultaten met criteria om alleen de gegevens te behouden die voor uw analyse relevant zijn.
3. **Grafiek**: toon het rapport als grafiek of als tabel.
4. **Export en delen**: exporteer het rapport als PDF, Word, HTML, Excel, CSV, JSON of Markdown, deel het, of koppel het aan een BI-tool zoals Power BI.

### Tabellen selecteren

Kies eerst de roottabel in de lijst **Select the Root Table**: dat is de hoofdtabel van het rapport, bijvoorbeeld verwerkingsactiviteiten. Klik daarna op **Add Table** om tabellen toe te voegen die aan de roottabel zijn gekoppeld (verwerkingsstappen, doeleinde, labels enzovoort). U kunt in elk rapport maximaal 7 tabellen bevragen, de roottabel inbegrepen.

<figure><img src="../../.gitbook/assets/reports-1.png" alt="De selectie van de roottabel en de gekoppelde tabellen"><figcaption><p>De selectie van de roottabel en de gekoppelde tabellen</p></figcaption></figure>

Klik op **Volgende** wanneer u de tabellen hebt gekozen.

{% hint style="info" %}
U kunt vanuit de rapportbouwer terugkeren naar de tabelselectie, met de knop **Bewerken** van de kaart **Selected Tables**, om meer tabellen toe te voegen. De tabellen die het rapport al gebruikt, zijn vergrendeld.
{% endhint %}

### Opbouwen met metrieken en dimensies

Bouw uw rapport op door de gewenste metrieken en dimensies uit het linkerpaneel naar het gebied **Drop Metrics and Dimensions Here** te slepen of te selecteren. Een melding waarschuwt u wanneer u het maximale aantal metrieken en dimensies voor een rapport hebt bereikt.

<figure><img src="../../.gitbook/assets/reports-2.png" alt="De editor voor metrieken en dimensies"><figcaption><p>De editor voor metrieken en dimensies</p></figcaption></figure>

De kaart **Filters** beperkt de gegevens en **Sort By** bepaalt de volgorde van de rijen (vink **Ascending order** aan voor een oplopende sortering). **Refresh Data** werkt het voorbeeld bij.

Klik op **Opslaan en doorgaan** om het rapport te openen, of op **Opslaan** om in de editor te blijven.

{% hint style="info" %}
De gegevens worden automatisch per dimensie geaggregeerd om de geselecteerde metrieken te berekenen.
{% endhint %}

Voorbeeld: selecteert u de metriek **Number of Data processing** en de dimensie **Status**, dan krijgt u een rapport dat als volgt is gegroepeerd:

| Status | Number of Data processing |
| ------ | ------------------------- |
| Draft  | 12                        |
| Active | 560                       |

### Link naar het dossier

Voor tabellen van objecten die een dossier hebben (verwerkingsactiviteiten, verzoeken van betrokkenen, datalekken, activa, stakeholders, audits, beveiligingsmaatregelen, contracten, AI-systemen en taken) voegt de dimensie **Record url** aan elke rij een klikbare link **Details** toe. Die link opent het dossier van het object in de juiste module, in een nieuw tabblad en voor de huidige werkruimte. De kolom wordt ook in exports opgenomen, als URL.

<figure><img src="../../.gitbook/assets/custom-report-record-url-dimension.png" alt="De dimensie Record url in de opbouw van het rapport"><figcaption><p>De dimensie Record url aan het rapport toevoegen</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/custom-report-details-link.png" alt="Klikbare link Details in een aangepast rapport"><figcaption><p>Elke rij toont een link Details die het dossier van het object opent</p></figcaption></figure>

## Het rapport weergeven en een grafiek toevoegen

Zodra het rapport is opgeslagen, komt u op de pagina ervan. De gegevenstabel wordt weergegeven met een filter op organisatorische eenheid, **Filters wissen** en de beschrijving van het rapport, die u ter plaatse kunt bewerken.

<figure><img src="../../.gitbook/assets/reports-3.png" alt="Een aangepast rapport met de gegevenstabel"><figcaption><p>De pagina van een aangepast rapport</p></figcaption></figure>

Om een grafiek toe te voegen, klikt u op **Add Chart** en stelt u daarna de opties in:

* **Chart Type**: **Column Chart**, **Bar Chart**, **Pie Chart** of **Heatmap**.
* **Displayed Metric**: de waarde die de grafiek meet.
* **Dimension #1** en **Dimension #2**: de assen van de grafiek.
* **Data Stacking**: **Default**, **Stacking in Column** (gestapelde waarden) of **Stacking by Percentage** (gestapeld tot 100%).
* **Sort By** en **Ascending order**: de weergavevolgorde.

Het voorbeeld wordt bijgewerkt terwijl u uw keuzes maakt. Om de grafiek later te wijzigen of te verwijderen, gebruikt u **Edit Chart** of **Remove Chart** boven de grafiek.

<figure><img src="../../.gitbook/assets/reports-4.png" alt="Het venster Add Chart met de opties ervan"><figcaption><p>Het venster Add Chart</p></figcaption></figure>

## Afdrukken, exporteren en delen

Vanaf de pagina van een rapport:

* **Exporteren** downloadt het rapport als CSV, Excel, JSON, PDF, Word, HTML of Markdown.
* Het menu van de knop **Bewerken** biedt **Afdrukken**, **Exporteren**, **Delen** (voorbehouden aan gebruikers met de machtiging **Geavanceerde configuratie**) en **Verplaats naar de prullenbak**.
* **Connect BI Tools** koppelt het rapport aan een hulpmiddel voor gegevensanalyse: zie [Integratie met hulpmiddelen voor gegevensanalyse (BI)](bi-tools.md).

## Prullenbak

Een verwijderd rapport of een verwijderde categorie komt eerst in de prullenbak terecht: u kunt het terugzetten zolang het niet definitief is verwijderd.

* **Een item naar de prullenbak verplaatsen**: klik in het actiemenu van een rapport op **Verplaats naar de prullenbak** en bevestig. Het actiemenu van een categorie, in het linkerpaneel, biedt dezelfde actie: de categorie en al haar rapporten gaan naar de prullenbak.
* **De prullenbak bekijken**: schakel de optie **Bekijk prullenbak** in boven de lijst met rapporten, of in het menu van het paneel met categorieën.
* **Terugzetten**: in de prullenbak zet **Herstellen** het item terug in de actieve lijst. Het terugzetten van een categorie zet ook de rapporten terug die samen met de categorie naar de prullenbak zijn verplaatst. Zet u een rapport terug waarvan de categorie in de prullenbak staat, dan wordt ook die categorie teruggezet.
* **Definitief verwijderen**: in de prullenbak wist **Verwijderen** het item na bevestiging. Het verwijderen van een categorie verwijdert ook al haar rapporten. Deze actie kan niet ongedaan worden gemaakt.

{% hint style="info" %}
Acties in de prullenbak vereisen het recht om aangepaste rapporten te bewerken.
{% endhint %}
