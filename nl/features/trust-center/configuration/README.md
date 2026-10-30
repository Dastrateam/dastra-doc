---
description: >-
  Ontdek de bewerkingspagina van een Trust Center, hoe u het publiceert en hoe u
  een conformiteitsproject weergeeft.
---

# Uw Trust Center configureren

Deze pagina presenteert de bewerkingspagina van een Trust Center, legt uit hoe u het publiceert en beschrijft hoe een conformiteitsproject wordt weergegeven. Ze is bedoeld voor de mensen die het portaal configureren.

## De bewerkingspagina

De bewerkingspagina bestaat uit onderdelen die u met een klik opent of sluit. De eerste drie zijn altijd beschikbaar:

* **Configuratie**: de naam, de organisatorische eenheid, de eigenaren, het welkomstbericht, de weer te geven functies en de snelle links. Zie [Startpagina en algemene configuratie](home.md).
* **Veiligheid**: verplichte authenticatie, goedkeuring van downloads en IP-filtering. Zie [Beveiliging](security.md).
* **Ontwerp**: het logo, de omslagafbeelding en de accentkleur. Zie [Uiterlijk en ontwerp](design.md).

De volgende onderdelen worden ontgrendeld wanneer de overeenkomstige functie is aangevinkt bij **Configuratie**:

* **Vragenlijsten**: zie [Vragenlijsten](questionnaires.md).
* **Verzoeken van betrokkenen**: zie [Verzoeken van betrokkenen](data-subject-requests.md).
* **Documenten**: zie [Bijlagen](attachments.md).
* **Conformiteit**: zie [Het conformiteitsproject weergeven](#het-conformiteitsproject-weergeven) op deze pagina.

De andere functies worden met een selectievakje ingeschakeld, zonder eigen onderdeel: het [Verwerkingsregister](ropa.md), het [Organigram](org-chart.md), de [Contacten](contacts.md) en de [AI-systemen](ai-systems.md).

<figure><img src="../../../.gitbook/assets/trust-center-configuration-1.png" alt="Actiebalk van de bewerkingspagina van een Trust Center in concept"><figcaption><p>De knoppen van de bewerkingspagina van een Trust Center in concept</p></figcaption></figure>

## Publiceren en de publicatie annuleren

Een nieuw aangemaakt Trust Center is een concept: de indicator rechtsboven op de pagina toont **Het Trust Center is in conceptmodus** en het portaal is niet online toegankelijk.

Om het te publiceren:

1. Klik rechtsboven op de bewerkingspagina op **Publiceren**. De knop is uitgeschakeld zolang een verplicht veld leeg is.
2. Bevestig de vraag "Wilt u het Trust Center opslaan en publiceren?". Alle wijzigingen worden opgeslagen.

De indicator toont dan **Het Trust Center is gepubliceerd** en het portaal wordt toegankelijk voor iedereen die over de link beschikt, binnen de regels van het onderdeel **Veiligheid**.

Om het portaal ontoegankelijk te maken, klikt u op **Publicatie annuleren**. Dit geldt onmiddellijk, zonder bevestiging. Vanuit de lijst met Trust Centers biedt het menu van elke rij ook **Inschakelen** en **Uitzetten**.

## Het conformiteitsproject weergeven

Deze functie voegt een tabblad **Conformiteit** toe aan het portaal. Het presenteert een samenvatting van een conformiteitsproject: voor elk kader van het project de actieve audit met de bijlagen ervan en de toegepaste controles. De functie vereist de functie [Conformiteit](../../compliance/README.md) in uw abonnement.

### Het te tonen project kiezen

1. Vink in het onderdeel **Configuratie** de optie **Weergave van het conformiteitsproject** aan.
2. Open het onderdeel **Conformiteit**.
3. Kies bij **Selecteer het conformiteitsproject dat u wilt weergeven** het project. Een Trust Center toont één project.
4. Sla op en publiceer daarna het Trust Center als het nog niet is gepubliceerd.

Het onderdeel **Conformiteit** wordt als fout aangemerkt zolang er geen project is geselecteerd.

<figure><img src="../../../.gitbook/assets/trust-center-configuration-2.png" alt="Onderdeel Conformiteit met de keuzelijst voor het conformiteitsproject"><figcaption><p>Het te tonen conformiteitsproject kiezen</p></figcaption></figure>

### Wat bezoekers zien

Het tabblad **Conformiteit** van het portaal toont links één kaart per kader. Alleen de kaders van het project met een [actieve audit](../../compliance/projects/audits.md) worden vermeld. Wanneer een bezoeker op een kader klikt, toont de pagina:

* **Auditdetails**: het type, de status, de naam en de begin- en einddatum van de actieve audit, gevolgd door de bijlagen ervan;
* **Controles**: de toegepaste controles van het kader die actief zijn en waarvan alle tests slagen. Elke controle toont de referentie, de titel, de beschrijving en de referenties van de vereisten waaraan ze beantwoordt.

<figure><img src="../../../.gitbook/assets/trust-center-configuration-3.png" alt="Tabblad Conformiteit van het openbare portaal met de lijst met kaders, de auditdetails en de controles"><figcaption><p>Het tabblad Conformiteit van het openbare portaal</p></figcaption></figure>

Om het portaal actueel te houden, stelt u de actieve audit van elk kader in het conformiteitsproject in en houdt u de tests van uw controles up-to-date. Zie [Audits](../../compliance/projects/audits.md).
