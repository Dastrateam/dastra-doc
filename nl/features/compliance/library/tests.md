---
description: Leer hoe u tests beheert in de bibliotheek van de module Conformiteit: handmatige tests, geautomatiseerde tests met connectoren, bewijs, samenvoegen en koppeling aan documenten.
---

# Tests

Een test bepaalt hoe en hoe vaak een controle wordt geëvalueerd, en op welk bewijs die evaluatie steunt.

Tests vormen de operationele schakel tussen:

* de controles (de ingevoerde maatregelen),
* het verzamelde bewijs,
* de conformiteitsresultaten die in de loop van de tijd worden waargenomen.

***

## De rol van tests in Dastra

Een test beantwoordt een eenvoudige maar essentiële vraag:

> _Wordt de controle echt toegepast en is ze doeltreffend?_

Elke test is:

* gekoppeld aan een referentiecontrole,
* uitgevoerd volgens een vastgelegde frequentie,
* gebruikt in conformiteitsprojecten om bruikbaar bewijs en resultaten te leveren.

***

## Weergave van de testbibliotheek

<figure><img src="../../../.gitbook/assets/image-492.png" alt="Weergave van de testbibliotheek met de lijst van beschikbare tests"><figcaption></figcaption></figure>

De testbibliotheek biedt een overkoepelend overzicht van alle beschikbare tests, met onder meer:

* hun type (handmatig of geautomatiseerd),
* de aanmaakdatum,
* de gekoppelde controles,
* geavanceerde filters (kader, type, vereisten, wezen-tests).

Met deze weergave kunt u:

* tests herkennen die in meerdere contexten worden hergebruikt,
* tests opsporen die nergens aan gekoppeld zijn,
* verificatiemethoden standaardiseren.

***

## Handmatige tests (standaard)

Een test is standaard handmatig.

Een handmatige test steunt op een menselijke handeling, bijvoorbeeld:

* een documentenonderzoek,
* een gesprek met de teams,
* de controle van een register,
* een eenmalige audit van een proces.

### Werking binnen een conformiteitsproject

Wanneer u een handmatige test aan een project toevoegt:

* moet het bewijs regelmatig worden bijgewerkt,
* volgens de frequentie die in de test is vastgelegd (maandelijks, driemaandelijks, jaarlijks enzovoort).

Zo blijft de conformiteit actueel en wordt ze in de loop van de tijd bijgehouden.

***

## Een test configureren

{% columns %}
{% column %}
Bij het aanmaken of bewerken van een test legt de gebruiker vast:

* de naam en de referentie van de test (met referentiegenerator),
* de **Frequentie van de test**,
* de gedetailleerde beschrijving, met onder meer:
  * het doel van de test
  * de te volgen procedure
  * het verwachte bewijs
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-493.png" alt="Formulier voor het aanmaken van een test"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Deze informatie dient als operationele leidraad wanneer u de test binnen een project uitvoert.

***

## Geautomatiseerde tests met Dastra-connectoren

Dastra biedt verschillende soorten kant-en-klare connectoren (vragenlijsten, registers, beleidsdocumenten enzovoort), en een generieke connector. Deze connectoren worden rechtstreeks gebruikt in de geautomatiseerde tests van de module Conformiteit.

<figure><img src="../../../.gitbook/assets/image-494.png" alt="Keuze van een connector voor een geautomatiseerde test"><figcaption></figcaption></figure>

Naast handmatige tests kunt u met connectoren geautomatiseerde tests configureren.

Een geautomatiseerde test gebruikt een Dastra-connector om:

* elementen van de werkruimte rechtstreeks te bevragen,
* automatisch bewijs te verzamelen,
* de conformiteit te verifiëren aan de hand van vastgelegde criteria.

### Voorbeelden van connectoren

Met connectoren kunt u onder meer:

* een register van AI-systemen verzamelen,
* controleren of documenten aanwezig en bijgewerkt zijn (bijvoorbeeld de documentatie van AI-systemen),
* registers bevragen (activa, incidenten, gegevensverwerkingen),
* vragenlijsten of beleidsdocumenten analyseren.

Voorbeeld:\
Een geautomatiseerde test kan nagaan of elk AI-systeem conforme en actuele documentatie heeft, zonder handmatige tussenkomst.

## Een aangepaste connector toevoegen

Naast de standaardconnectoren kunt u in Dastra aangepaste connectoren maken om het verzamelen van bewijs in conformiteitstests te automatiseren.

Met een aangepaste connector kunt u:

* een technische query uitvoeren (bijvoorbeeld een HTTP-verzoek),
* een interne of externe bron bevragen,
* automatisch feitelijke gegevens verzamelen,
* bewijs opleveren dat in audits bruikbaar is.

De connector wordt zo een terugkerende en traceerbare bron van bewijs.

### HTTP-verzoek

Met de connector **HTTP-verzoek** bevraagt u elke beschikbare API of elk eindpunt.

De connector is vooral geschikt om:

* tools van derden te bevragen,
* het bestaan of de status van een resource te controleren,
* technische of documentaire controles te automatiseren.

## De HTTP-connector configureren

<figure><img src="../../../.gitbook/assets/compliance-test-http-connector-form.png" alt="Venster voor het aanmaken van de HTTP-connector met de velden URL, HTTP-methode, Auth, Headers, URL-parameters en Body"><figcaption><p>De configuratie-interface van de HTTP-connector met de tabbladen Auth, Headers, URL-parameters en Body</p></figcaption></figure>

De configuratie-interface van de HTTP-connector is opnieuw ontworpen, zodat u verzoeken rechtstreeks vanuit Dastra kunt opbouwen en testen.

Met de configuratie-interface bouwt u een verzoek op zonder de JSON-syntaxis te kennen:

* Keuze van de authenticatiemethode: kies rechtstreeks tussen **API-sleutel**, **Autorisatietoken (Bearer)** of **Basisauthenticatie (Basic)**, zonder headers handmatig in JSON-indeling in te voeren.
* Afgeschermde inloggegevens: gevoelige velden (token, wachtwoord) zijn standaard afgeschermd. Met een oogpictogram maakt u ze tijdelijk zichtbaar. Deze waarden verschijnen nooit leesbaar in de logs.
* Editors voor sleutel/waarde-paren (zoals in Postman): configureer eigen headers en URL-parameters als sleutel/waarde-paren, zonder JSON te schrijven.
* Alleen-lezen voorbeeld: een voorbeeld toont de headers die bij de uitvoering echt worden verzonden, waarbij gevoelige waarden afgeschermd blijven.

### Verzoekbouwer

Met een visuele editor configureert u elk onderdeel van het verzoek:

| Veld | Beschrijving |
| --- | --- |
| URL | Het te bevragen eindpunt (verplicht). Ondersteunt variabelen tussen accolades `{{variabele}}`. |
| HTTP-methode | GET, POST, PUT, PATCH, DELETE. |
| **Headers** | Voeg headers toe als sleutel/waarde-paren: verwerking van authenticatie met token, API-sleutel of eigen header. |
| **Aanvraagtekst** | JSON-payload of vrije tekst (voor de methoden POST/PUT/PATCH). |
| Variabelen | Declareer herbruikbare variabelen in de URL en in de aanvraagtekst, die bij de uitvoering worden ingevuld. |

### Het verzoek testen

Met een testknop (**Test request**) voert u het verzoek rechtstreeks vanuit de configuratie-interface uit en toont u het ruwe antwoord. Dat vergemakkelijkt het opsporen van fouten voordat u de connector aan een conformiteitstest koppelt.

### Het antwoord analyseren

Leg de succescriteria vast: verwachte HTTP-code, aanwezigheid van een veld in het JSON-antwoord, doelwaarde van een attribuut. Het resultaat van de analyse wordt als bewijs opgeslagen in het conformiteitsproject.

## Voordelen van geautomatiseerde tests

Met geautomatiseerde tests kunt u:

* continu bewijs verzamelen,
* de operationele werklast verlagen,
* de betrouwbaarheid van de controles verbeteren,
* afwijkingen sneller opsporen.

Ze zijn vooral geschikt voor terugkerende of gestructureerde controles.

***

## Bewijs bijvoegen vanuit Bestandsbeheer

Wanneer u bewijs aan een test toevoegt, kunt u een bestand rechtstreeks selecteren in het **Bestandsbeheer** van Dastra, zonder het opnieuw te hoeven uploaden. Klik in het venster **Bewijs toevoegen** op **Bestandsverkenner**.

<figure><img src="../../../.gitbook/assets/compliance-test-evidence-file-explorer.png" alt="Venster Bewijs toevoegen met de knop Bestandsverkenner"><figcaption><p>Met de knop Bestandsverkenner selecteert u bewijs dat al in het Bestandsbeheer van Dastra staat</p></figcaption></figure>

***

## IA-analyse van bewijs

Dastra kan het bewijs dat aan een test is gekoppeld automatisch analyseren en aangeven of het overeenkomt met wat de procedure verwachtte. Deze functie is een hulpmiddel voor de auditor: ze vervangt het menselijke oordeel nooit en accepteert of weigert geen bewijs namens de klant.

### Werking

Wanneer u bewijs aan een testprocedure toevoegt, ontvangt de AI twee elementen:

1. De procedurebeschrijving: wat de test als bewijs verwacht
2. De inhoud van het aangeleverde bewijs, geanalyseerd naargelang het type (zie hieronder)

De AI vergelijkt beide en geeft vier gegevens terug, die in de bewijstabel verschijnen als een gekleurde badge met een tooltip:

| Gegeven | Beschrijving |
| --- | --- |
| Waardering | **Correct**, **Waarschijnlijk correct**, **Niet conform** of **Onbekend** |
| Vertrouwensscore | Van 0 tot 100 %: geeft aan hoe zeker de AI is van haar oordeel |
| Beschrijving | Korte samenvatting van het geanalyseerde document |
| Rechtvaardiging | Uitleg van het oordeel ten opzichte van de criteria van de procedure |

### Ondersteunde soorten bewijs

De analyse past zich automatisch aan het type aangeleverd bewijs aan:

| Soort bewijs | Analysemethode |
| --- | --- |
| Schermafdruk of afbeelding | Visuele analyse van de inhoud |
| Document (PDF, Word, tekst) | Lezen en extraheren van de tekstinhoud |
| URL of webpagina | Ophalen van de pagina via de opgegeven URL |
| Geen bewijs bijgevoegd | Resultaat automatisch ingesteld op **Onbekend** |

{% hint style="info" %}
Een tooltip bij het analyseresultaat legt uit welke methode de AI voor het betrokken bewijs heeft gebruikt (OCR, lezen van het label, vergelijking met de testprocedure enzovoort). De tooltip bevat ook een link naar deze documentatie, voor meer informatie over de werking van de analyse.
{% endhint %}

### Activering en instellingen

De functie is optioneel en standaard uitgeschakeld. Om ze te activeren gaat u naar **Configuratie** > **Conformiteit** en schakelt u de optie **Automatische IA-analyse van bewijsstukken** in.

{% hint style="info" %}
Zolang de functie niet is geactiveerd, worden er geen bewijsgegevens naar het AI-model verzonden.
{% endhint %}

Het AI-model dat voor de analyse van bewijs wordt gebruikt, kunt u naar keuze van uw organisatie configureren via de instellingen van de AI-assistent (modelfamilie of aangepaste AI-provider).

### Wat de analyse niet doet

* Ze accepteert of weigert bewijs niet automatisch: de eindbeslissing blijft altijd bij de auditor.
* Ze wijzigt de status van de test niet.
* Ze is niet bindend: een lage vertrouwensscore (**Onbekend** of **Waarschijnlijk correct**) geeft alleen aan dat een menselijke controle aanbevolen is.

***

## Tests samenvoegen

Net als bij controles kan de testbibliotheek overbodige tests verzamelen, vooral na het importeren van meerdere kaders. Met de functie voor het samenvoegen van tests voegt u deze dubbele tests samen tot één referentietest.

### Werking van het samenvoegen

Selecteer in de testbibliotheek de tests die u wilt samenvoegen en klik op **Samenvoegen**. Kies de doeltest die u wilt behouden: de koppelingen van de brontests (gekoppelde controles, uitvoeringsresultaten, frequentie) worden overgenomen door de doeltest, waarna de brontests worden verwijderd.

{% hint style="warning" %}
Het samenvoegen is onomkeerbaar. Controleer de koppelingen van elke brontest voordat u bevestigt.
{% endhint %}

### Typische gebruiksscenario's

* Ontdubbeling: twee kaderimports hebben een dubbele test "Verificatie van het privacybeleid" aangemaakt. Het samenvoegen voegt ze samen.
* Rationalisatie: meerdere sterk op elkaar lijkende handmatige tests kunt u groeperen tot één completere test.
* Opruimen vóór een audit: minder wezen-tests verbetert de leesbaarheid van het dashboard.

***

## Een test aan een document koppelen

Een conformiteitstest kunt u koppelen aan een of meer documenten uit het Bestandsbeheer van Dastra: contracten, beleidsdocumenten, documentair bewijs, verwerkersovereenkomsten voor subverwerking. Dankzij deze koppeling vindt u gemakkelijk de tests die bij elk document horen, en omgekeerd.

### Vanuit de weergave van een document

Wanneer een test aan een document is gekoppeld, verschijnt in de bewerkingsweergave van het betrokken document of contract een paneel **Tests**, met de referentie, de naam en de status van elke gekoppelde test.

<figure><img src="../../../.gitbook/assets/compliance-test-linked-document.png" alt="Weergave van een contract met het paneel Tests, dat de gekoppelde conformiteitstests toont"><figcaption><p>Een gekoppelde test verschijnt in het paneel Tests rechts van het document (hier: G-T2 Lawful Basis Spot Check, status Done en resultaat Pass)</p></figcaption></figure>

### Vanuit Bestandsbeheer

In Bestandsbeheer toont het detailblad van een document in de zijkolom alle Dastra-entiteiten waaraan het is gekoppeld: verwerkingsactiviteiten, contracten en conformiteitstests.

<figure><img src="../../../.gitbook/assets/file-manager-document-with-test.png" alt="Documentblad in Bestandsbeheer met de sectie Tests in de zijkolom"><figcaption><p>Bestandsbeheer toont de tests die bij elk document horen in de detailkolom</p></figcaption></figure>

Dankzij deze tweerichtingstraceerbaarheid controleert u gemakkelijk welke tests op welk document steunen en vindt u al het documentaire bewijs vanuit Bestandsbeheer.

***

## Een combinatie van benaderingen

In Dastra kunt u combineren:

* handmatige tests voor controles die analyse of menselijk oordeel vereisen,
* geautomatiseerde tests voor objectieve en repetitieve verificaties.

Deze combinatie zorgt voor een evenwicht tussen striktheid, efficiëntie en pragmatisme.
