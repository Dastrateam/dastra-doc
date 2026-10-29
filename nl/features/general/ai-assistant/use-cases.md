# Gebruiksscenario's

{% hint style="warning" %}
Opmerking over de kwaliteit van gegenereerde inhoud: alle inhoud die de assistent genereert, is slechts een voorstel. Een bevoegde persoon moet die controleren en aanpassen voordat u ze gebruikt. Dastra geeft geen enkele garantie over de kwaliteit van de voorgestelde informatie.
{% endhint %}

Alle generatiefuncties gebruiken hetzelfde venster: beschrijf het te genereren item (of begin met een van de voorgestelde **Voorbeelden**), kies zo nodig de generatietaal en klik op **Genereer**. Het voorstel verschijnt op een samenvattingsscherm, zodat u het kunt nakijken voordat u het valideert.

## Verwerkingsactiviteiten

### Een verwerkingsactiviteit genereren

Genereer snel een verwerkingsactiviteit in het formaat dat Dastra verwacht, op basis van een korte beschrijving. De assistent stelt een naam voor, een of meer datasets met hun velden, een bewaartermijn, beveiligingsmaatregelen, ontvangers en een beschrijving.

1. Klik op **Maak een gegevensverwerking** en selecteer daarna **Genereren met A.I.**.
2. Voer een korte beschrijving van uw verwerkingsactiviteit in, of klik op een van de **Voorbeelden** onder het invoerveld om de aanvraag vooraf in te vullen.
3. Kies zo nodig de generatietaal en schakel de gewenste opties in:
   * **Activiteit als verwerker**: genereert het dossier voor het register van de verwerker
   * **Gebruik bestaande elementen**: geeft de assistent de labels van de bestaande beveiligingsmaatregelen, activa en gegevensvelden in uw werkruimte, zodat hij ze hergebruikt in het gegenereerde dossier in plaats van duplicaten aan te maken. De betrokken repositories staan onder de optie
4. Klik op **Genereer** en wacht enkele ogenblikken.
5. Controleer het voorstel op het samenvattingsscherm en klik op **Valideren**.

<figure><img src="../../../.gitbook/assets/register-processing-create-ai-form.png" alt="Venster voor het genereren van een verwerkingsactiviteit met AI: invoerveld, taalkeuze, voorbeelden en de optie Gebruik bestaande elementen"><figcaption><p>Een verwerkingsactiviteit genereren met de AI-assistent: voorbeelden, generatietaal en hergebruik van bestaande elementen</p></figcaption></figure>

### Een dataset genereren

1. Ga naar de pagina **Gegevenssets**.
2. Klik op **Een dataset toevoegen** en daarna op **AI gegenereerd**.
3. Voer een korte beschrijving van uw dataset in.
4. Klik op **Volgende** en wacht enkele ogenblikken.
5. Pas op het samenvattingsscherm uw correcties toe en klik op **Creëren**.

### Een informatiebericht genereren

1. Ga naar de bewerkingspagina van een verwerkingsactiviteit.
2. Klik in de sectie **Documentatie** op **Informatiebericht genereren**.
3. Kies het gewenste formaat (u kunt de instructies aanpassen door **Aangepast** te selecteren) en de **Taal van de kennisgeving**; de taal van de interface wordt standaard voorgesteld.
4. Klik op **Genereer**. Met de voorbeeldweergave kopieert u de tekst van elk tabblad, of klikt u op **Exporteren** voor een PDF-, Word-, HTML- of Markdown-bestand.
5. In het venster **Kennisgeving exportinformatie** voegt de optie **Add this file to the attachments of this data processing**, standaard ingeschakeld, het geëxporteerde bestand toe aan de bijlagen van de verwerkingsactiviteit. Elke export maakt een nieuwe bijlage aan.

<figure><img src="../../../.gitbook/assets/register-processing-notice-export-modal.png" alt="Voorbeeldweergave van het informatiebericht met de actie Exporteren"><figcaption><p>Het door AI gegenereerde informatiebericht exporteren</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/register-processing-notice-export-attachments-option.png" alt="Venster Kennisgeving exportinformatie met de optie om het bestand aan de bijlagen toe te voegen"><figcaption><p>Het geëxporteerde bericht toevoegen aan de bijlagen van de verwerkingsactiviteit</p></figcaption></figure>

### Een complianceanalyse van een verwerkingsactiviteit genereren

De assistent kan een bestaande verwerkingsactiviteit analyseren en beoordelen in hoeverre ze voldoet aan de documentatievereisten van de AVG.

{% hint style="info" %}
Bètafunctie: de resultaten kunnen minder consistent zijn dan bij een stabiele functie en vragen extra zorg. Deze analyse ondersteunt uw besluitvorming en is geen juridisch advies.
{% endhint %}

Klik nadat de analyse is gegenereerd op **Analyse afdrukken** om het resultaat als PDF te exporteren of rechtstreeks naar de printer te sturen. Dit document kunt u bij uw compliancedossier voegen.

## Vragenlijsten (DPIA, risicoanalyse enzovoort)

### Een met AI ondersteund antwoord genereren

1. Ga naar het onderdeel **Vragenlijsten** en selecteer het gewenste sjabloon (bijvoorbeeld CNIL-PIA).
2. Klik op **Plan een vragenlijst**.
3. Selecteer **AI-ondersteunde reactie**.
4. Geef de verwerkingsactiviteit op die als bron moet dienen, of voer eigen instructies in.
5. Pas zodra het antwoord is gegenereerd uw correcties rechtstreeks toe in de vragenlijst.

{% hint style="info" %}
Als een AI-analyse is uitgevoerd op het antwoord op een vragenlijst of op een PIA, verschijnt in de kop van het analysepaneel een knop **Analyse afdrukken** zodra er een resultaat beschikbaar is. Het gestructureerde document bevat de algemene score (A tot F), de algemene beoordeling, de beoordeelde criteria met hun score en motivering, en de voorgestelde taken gerangschikt naar prioriteit, zonder schermafbeeldingen.
{% endhint %}

### Een vragenlijstsjabloon genereren

1. Ga naar het onderdeel **Vragenlijsten** en klik om een vragenlijstsjabloon aan te maken.
2. Selecteer **Creëren met AI**.
3. Geef een beschrijving van de vragenlijst (300 woorden) en een type op.
4. Pas het aantal secties en vragen aan.
5. Klik op **Genereer**.

## Verzoeken om rechten uit te oefenen

### Een antwoord op een verzoek genereren

Genereer antwoorden in meerdere talen, met aanpassingsopties (lengte, formele of informele toon enzovoort).

1. Open een verzoek om rechten uit te oefenen dat in behandeling is.
2. Vul de informatie in tot de stap **Antwoord op verzoek**.
3. Klik op **Genereer met AI**. De assistent genereert een antwoord op basis van de volgende informatie:
   * Voor- en achternaam van de aanvrager
   * Bericht van het verzoek
   * Te gebruiken taal
   * Naam van de werkruimte
   * Doeleinden van de betrokken verwerkingsactiviteit
   * Naam van de behandelaar van het verzoek
   * Datum van het verzoek en aantal resterende dagen
   * Status en ID van het verzoek
4. Pas de voorgestelde tekst aan of gebruik de herformuleringsopties (inkorten, verlengen, toon wijzigen).
5. Klik op **Validate this message**, voeg eventuele bijlagen toe en klik op **Verzenden**.

{% hint style="info" %}
Voor deze functie geldt een limiet op het aantal aanroepen per minuut.
{% endhint %}

{% hint style="info" %}
AI-verordening, artikel 50: wanneer de AI-assistent een antwoord genereert, geldt de strikte verplichting van artikel 50, lid 1 (de persoon informeren dat hij met een AI-systeem communiceert) niet, omdat er geen rechtstreekse interactie is tussen het AI-systeem en de betrokkene: een menselijke gebruiker controleert, valideert en verstuurt het antwoord. Het blijft wel aanbevolen de betrokkene te informeren als goede praktijk volgens de AVG (artikel 5, lid 1, onder a, eerlijkheid). Zie de [veelgestelde vragen](faq.md#moet-ik-betrokkenen-informeren-dat-ik-ai-heb-gebruikt-om-op-hun-verzoeken-te-antwoorden) voor de volledige analyse.
{% endhint %}

## Activa en actoren

### Een activum genereren

Genereer snel een activum (software, hulpmiddel enzovoort) in het formaat dat Dastra verwacht. De assistent stelt een naam voor, links naar het privacybeleid van de actor en maakt een actor aan als uitgever.

1. Klik op **Creëer een asset** en daarna op **AI gegenereerd**.
2. Voer een beschrijving of de URL van een privacybeleid in.
3. Controleer en vul de voorgestelde informatie aan voordat u valideert.

## Datalekken

### Een postmortem genereren

Vanuit een bestaand datalekdossier genereert de assistent een gestructureerd postmortemdocument met een beschrijving van het incident, de getroffen gegevens en de genomen maatregelen.

U vindt deze functie op de bewerkingspagina van een datalekdossier, in de sectie voor documentatie.

## Contracten

### Contractmetadata extraheren

Importeer een contractdocument (PDF of URL) en laat de assistent automatisch de metadata ervan extraheren: partijen, onderwerp, looptijd, belangrijke bepalingen enzovoort.

U vindt deze functie in de module **Contracten en beleidslijnen**, bij het aanmaken of bewerken van een contract.

## Aangepaste documenten en rapporten

### Een aangepast document genereren

Voer uw eigen instructies in en geef eventueel bronmateriaal op. De assistent genereert een gestructureerd document volgens uw specificaties.

### Een aangepast rapport genereren

Beschrijf in de module **Aangepaste rapportage** in natuurlijke taal het gewenste rapport. De assistent maakt een eerste versie die u daarna verfijnt.

## AI-systemen

### De beschrijving van een AI-systeem genereren

1. Ga naar de module **AI-systemen**.
2. Maak een AI-systeem aan of open het.
3. Klik in het beschrijvingsveld op **Generate with AI assistant**.
4. Voer een vrije beschrijving in of geef een URL op.

### Een informatiebericht voor een AI-systeem genereren

Klik in het dossier van een AI-systeem op **Genereer uw informatiebericht** om automatisch het informatiedocument voor gebruikers of betrokkenen te maken.

### Een risicoanalyse voor een AI-systeem genereren

De assistent analyseert de ingevulde velden van het dossier van het AI-systeem en beoordeelt de bijbehorende risico's.

{% hint style="info" %}
Bètafunctie: met extra zorg te behandelen en door een deskundige te valideren voordat u een beslissing neemt.
{% endhint %}

Klik nadat de analyse is gegenereerd op **Analyse afdrukken** om het resultaat als PDF te exporteren. Dit document kunt u bij uw nalevingsdossier voor de AI-verordening voegen.

<figure><img src="../../../.gitbook/assets/generalites-ai-assistant-cas-dusage-analysis-print.png" alt="Analysepaneel van de AI met de knoppen Analyse afdrukken en Analyse opnieuw starten"><figcaption><p>De knop Analyse afdrukken exporteert het resultaat van de analyse als PDF</p></figcaption></figure>

## Kaders en controles

### Controles, vereisten en tests voorstellen

Vanuit een kader in de module Conformiteit kan de assistent relevante controles, vereisten of tests voorstellen op basis van de context van het betrokken object (naam, beschrijving, gekoppeld kader).
