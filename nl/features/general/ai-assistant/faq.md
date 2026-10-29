---
description: >-
  Veelgestelde vragen over de Dastra AI-assistent: privacy, betrouwbaarheid,
  configuratie en naleving van de AI-verordening.
---

# Veelgestelde vragen

## Privacy en gegevens

### Worden mijn gegevens gebruikt om AI-modellen te trainen?

Nee. De modellen die Dastra gebruikt, zijn vooraf getraind en worden gehost op Microsoft Azure. Uw gegevens worden nooit gebruikt om de basismodellen te trainen, bij te stellen of te verbeteren, niet door Microsoft, OpenAI, Mistral of enige andere derde. Deze garantie is contractueel.

### Worden gegevens uit mijn werkruimte buiten mijn medeweten naar het model gestuurd?

Nee. Dastra stuurt alleen de informatie door die strikt nodig is voor de gevraagde generatie: de tekst die u invoert en, indien van toepassing, de velden van het object waaraan u werkt (verwerkingsactiviteit, AI-systeem, verzoek om rechten uit te oefenen enzovoort). Andere records in uw werkruimte, uw inloggegevens en sessiemetadata worden nooit meegestuurd. De enige uitzondering: wanneer u bij het genereren van een verwerkingsactiviteit de optie **Gebruik bestaande elementen** inschakelt, worden de labels van de bestaande beveiligingsmaatregelen, activa en gegevensvelden meegestuurd, zodat de assistent ze kan hergebruiken. Een overzicht per functie vindt u op de pagina [Werking](how-it-works.md).

### Waar worden de AI-modellen van Dastra gehost?

Voor de families OpenAI, Mistral en Open source worden de modellen gehost op de infrastructuur van Microsoft Azure in Frankrijk. Uw gegevens lopen niet via de eigen servers van OpenAI of Mistral. Dastra gebruikt uitsluitend beheerde Azure-diensten.

Configureert u een **IA-leverancier** met uw eigen API-sleutel, dan hangt de hosting af van de leverancier die u kiest.

### Worden mijn prompts na de generatie bewaard?

Azure-modellen zijn stateless: prompts en resultaten worden tussen twee aanvragen niet in het model bewaard. Ze worden ook niet vastgelegd voor commercieel hergebruik.

Uitzondering: Azure heeft een geautomatiseerd mechanisme voor het opsporen van misbruik. Als inhoud wordt gemarkeerd, kan een steekproef tijdelijk worden bewaard in een omgeving die van andere klanten is afgeschermd, met het oog op controle. Voor resources die in de EER zijn geïmplementeerd (zoals bij Dastra het geval is), bevinden eventuele menselijke beoordelaars zich eveneens in de EER. Deze bewaring blijft uitzonderlijk.

### Wie kan de AI-aanroepen in mijn organisatie zien?

Beheerders van de werkruimte hebben toegang tot de **AI invocation logs** (geschiedenis van 90 dagen) via **Organisatie-instellingen** > **Assistent IA** > **AI invocation logs**. Deze logboeken tonen de datum, de status, het type bewerking, het gebruikte model, de duur en de gebruiker die de generatie heeft gestart. De inhoud van de prompts en antwoorden wordt niet getoond.

### Valt de AI-assistent onder de verwerkersovereenkomst van Dastra?

Ja. Het gebruik van de AI-assistent valt binnen het bestaande contractuele kader tussen uw organisatie en Dastra. Microsoft Azure treedt op als subverwerker en is gebonden aan de contractuele verplichtingen van Azure op het gebied van gegevensbescherming. Raadpleeg voor meer details uw verwerkersovereenkomst met Dastra of neem contact op met ons team.

## Kwaliteit en betrouwbaarheid

### Kan ik de door AI gegenereerde resultaten vertrouwen?

Gegenereerde resultaten zijn uitgangsvoorstellen, geen definitieve antwoorden. Ze versnellen uw documentatiewerk, maar vervangen het oordeel van een deskundige niet. Alle gegenereerde inhoud moet worden gecontroleerd en gevalideerd door een bevoegde persoon voordat u ze gebruikt, met name bij complianceanalyses, informatieberichten en antwoorden op verzoeken om rechten uit te oefenen.

### Wat is een bètafunctie?

Sommige AI-functies verschijnen eerst in bèta: ze werken, maar worden nog verfijnd. De resultaten kunnen minder consistent zijn dan bij stabiele functies en vragen extra zorg.

Momenteel in bèta: de complianceanalyse van verwerkingsactiviteiten en de complianceanalyse van AI-systemen.

### Kan AI fouten maken bij juridische vragen?

Ja. De AI-assistent is geen jurist. Gegenereerde inhoud, zoals complianceanalyses, berichten en risicobeoordelingen, ondersteunt uw besluitvorming op basis van de informatie in uw werkruimte. Ze vormt geen juridisch advies en vervangt de deskundigheid van een functionaris voor gegevensbescherming (FG) of een gespecialiseerde raadsman niet.

## Configuratie en toegang

### Hoe kies ik het gebruikte AI-model?

Ga naar **Organisatie-instellingen** > **Assistent IA** om de modelfamilie te kiezen: OpenAI (standaard), Mistral, Open source of een eigen leverancier (**IA-leverancier**). Voor elke familie worden automatisch drie modelniveaus gebruikt, afhankelijk van de complexiteit van de taak (Fast, Smart, Extended context).

### Kan ik mijn eigen AI-leverancier koppelen?

Ja, met de functie **IA-leverancier**. Elke leverancier die compatibel is met de OpenAI-API-standaard kan worden gekoppeld: OpenAI, Google (Gemini), Mistral, Microsoft Foundry of een zelfgehoste LLM. Configureer uw inloggegevens in **Organisatie-instellingen** > **Assistent IA** > **IA-leverancier**.

{% hint style="warning" %}
Bij een eigen AI-leverancier gelden de in deze documentatie beschreven Azure-garanties niet meer. De gegevens vallen onder het beleid van uw leverancier.
{% endhint %}

### Kan ik de AI-assistent voor mijn organisatie uitschakelen?

Ja. Neem contact op met ons supportteam om de functie op organisatieniveau uit te schakelen. Uitschakelen geldt globaal: u kunt niet een deel van de prompts uitschakelen en de andere actief houden.

### Is de AI-assistent beschikbaar in alle Dastra-abonnementen?

Ja, de AI-assistent is beschikbaar in alle Dastra-abonnementen. Voor sommige geavanceerde functies kunnen specifieke voorwaarden gelden. Neem contact op met ons team voor vragen over uw abonnement.

### Wat zijn AI-credits?

AI-credits zijn de meeteenheid voor het verbruik van de AI-assistent binnen uw organisatie. Elke aanroep van een AI-functie verbruikt een aantal credits, afhankelijk van het gebruikte modelniveau (Fast, Smart of Large context) en de hoeveelheid verwerkte gegevens.

Beheerders zien het huidige verbruik en het resterende saldo onder **Organisatie-instellingen** > **Assistent IA** ([directe link](https://app.dastra.eu/general-settings/ai)).

### Wat gebeurt er als mijn organisatie haar creditquotum bereikt?

Wanneer het quotum is bereikt, worden de AI-functies tijdelijk opgeschort tot de volgende vernieuwing. Uw werkruimte en gegevens blijven volledig toegankelijk, alleen de AI-generatie is uitgeschakeld.

Neem contact op met ons team om uw quotum te verhogen of een vervroegde vernieuwing aan te vragen.

### Geldt het creditsysteem ook bij een eigen AI-leverancier?

Nee. Wanneer uw organisatie een **IA-leverancier** configureert, is het creditsysteem van Dastra uitgeschakeld en worden er geen credits geteld. Het verbruik wordt rechtstreeks door uw leverancier beheerd volgens zijn eigen factureringsvoorwaarden.

## AI-verordening (EU-verordening 2024/1689)

### Valt de AI-assistent van Dastra onder de AI-verordening?

Ja. De AI-assistent van Dastra valt onder de definitie van een AI-systeem in de AI-verordening (EU 2024/1689). Afhankelijk van de gebruikte functies is hij in de eerste plaats ingedeeld als systeem met beperkt risico, wat transparantieverplichtingen (artikel 50) meebrengt wanneer de gegenereerde inhoud voor natuurlijke personen bestemd is.

### Moet ik betrokkenen informeren dat ik AI heb gebruikt om op hun verzoeken te antwoorden?

Niet op grond van een strikte verplichting van de AI-verordening, maar het wordt sterk aanbevolen als goede praktijk.

Artikel 50, lid 1, van de AI-verordening richt zich op AI-systemen die rechtstreeks met natuurlijke personen communiceren. In Dastra is dat niet het geval: een menselijke gebruiker (FG, juridisch adviseur) genereert de tekst, controleert en valideert die en stuurt haar zelf naar de betrokkene. Er is geen rechtstreekse interactie tussen het AI-systeem en de uiteindelijke ontvanger, dus de strikte verplichting van artikel 50, lid 1, is niet van toepassing.

{% hint style="info" %}
De ontwerprichtsnoeren van het AI-bureau (in 2025 gepubliceerd voor raadpleging van belanghebbenden) bevestigen deze uitleg uitdrukkelijk: "Rechtstreekse interactie sluit indirecte of bemiddelde menselijke interactie uit waarbij de persoon wordt blootgesteld aan AI-uitvoer zonder rechtstreeks met het systeem te communiceren, bijvoorbeeld wanneer klantenservicemedewerkers AI-hulpmiddelen gebruiken om met natuurlijke personen te communiceren, of wanneer de AI-uitvoer niet door het AI-systeem zelf, maar door een andere persoon aan de persoon ter beschikking wordt gesteld." (punt 3.1.1). De Dastra-situatie komt precies overeen met dit scenario.

De verplichtingen van artikel 50 gelden vanaf 2 augustus 2026. De definitieve richtsnoeren kunnen meer duidelijkheid geven.
{% endhint %}

Dat gezegd zijnde blijft het informeren van de betrokkene dat een antwoord met AI is opgesteld een goede praktijk volgens het beginsel van eerlijkheid en transparantie van de AVG (artikel 5, lid 1, onder a). Dastra voegt deze vermelding niet automatisch toe: wil uw organisatie ze opnemen, dan doet u dat zelf vóór het verzenden.

### Is Dastra aanbieder of gebruiksverantwoordelijke in de zin van de AI-verordening?

Beide, afhankelijk van het gebruik. Wanneer u de standaardmodellen gebruikt (OpenAI, Mistral, Open source via Azure), is Dastra de aanbieder van het AI-systeem en uw organisatie de gebruiksverantwoordelijke. Wanneer u uw eigen leverancier koppelt via de **IA-leverancier**, treedt Dastra uitsluitend op als compliancehulpmiddel. Uw organisatie neemt dan de rol van aanbieder en/of gebruiksverantwoordelijke op zich voor haar eigen model.
