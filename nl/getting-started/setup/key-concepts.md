---
description: >-
  Definities van de concepten die Dastra structureren: organisatie, werkruimte, organisatorische eenheid, entiteit, afdeling en eigenaar.
---

# Kernbegrippen

Neem de tijd om de concepten te begrijpen die het platform structureren voordat u Dastra gebruikt. Ze helpen u uw verwerkingsactiviteiten, uw teams en uw verantwoordelijkheden te organiseren.

***

## Inhoud

* [Organisatie](key-concepts.md#organisatie)
* [Werkruimte](key-concepts.md#werkruimte)
* [Organisatorische eenheid](key-concepts.md#organisatorische-eenheid)
* [Entiteit](key-concepts.md#entiteit)
* [Afdeling](key-concepts.md#afdeling)
* [Eigenaar van de organisatie](key-concepts.md#eigenaar-van-de-organisatie)
* [Credits en quota](key-concepts.md#credits-en-quota)

***

## Organisatie

Een **organisatie** groepeert de accounts en gebruikers die aan uw Dastra-abonnement zijn gekoppeld. Het is de basisstructuur: ze bevat al uw werkruimten.

De naam van uw organisatie ziet u rechtsboven in de interface, onder de naam van uw gebruikersaccount.

{% hint style="info" %}
Een organisatie kan meerdere werkruimten bevatten, elk bestemd voor een ander project, een andere entiteit of een ander team. Een gebruiker kan tot meerdere organisaties behoren.
{% endhint %}

***

## Werkruimte

Een **werkruimte** is de omgeving waarin u met uw team samenwerkt. Ze groepeert de modules en gegevens die aan uw entiteiten zijn gekoppeld: verwerkingsactiviteiten, audits, risico's, incidenten, verzoeken van betrokkenen enzovoort. De gegevens van een werkruimte zijn nooit toegankelijk vanuit een andere werkruimte.

U kiest uw werkruimte bij het aanmelden door op de tegel ervan te klikken in de lijst met uw werkruimten.

Geef uw werkruimten duidelijke namen (bijvoorbeeld "Conformiteit van de groep" of "Franse entiteiten"). Dat maakt de navigatie gemakkelijker wanneer de organisatie er meerdere heeft.

***

## Organisatorische eenheid

**Organisatorische eenheden** structureren een werkruimte volgens uw interne organisatie. Er zijn twee types: entiteiten en afdelingen.

U koppelt verwerkingsactiviteiten, taken, verzoeken van betrokkenen, incidenten en risico's aan een organisatorische eenheid. U kunt er ook toegangsrechten voor gebruikers of teams aan koppelen.

{% hint style="info" %}
Organisatorische eenheden vormen de referentie voor rapporten en voor toegangsrechten. Zie [Organisatorische eenheden aanmaken en instellen](organizational-units.md).
{% endhint %}

***

## Entiteit

Een **entiteit** komt overeen met een rechtspersoon, dus met een verwerkingsverantwoordelijke: een bedrijf, een dochteronderneming, een vereniging. Op dit niveau koppelt u verwerkingsactiviteiten en de belangrijkste juridische informatie.

Een entiteit bevat:

* de contactgegevens van de verwerkingsverantwoordelijke,
* de functionaris voor gegevensbescherming (FG),
* de leidende toezichthoudende autoriteit,
* de afdelingen en onderliggende entiteiten die eraan zijn gekoppeld.

Voorbeeld:

> Entiteit: _Dastra France SAS_\
> Afdeling: _Marketing_\
> FG: _Jean Dupont_

***

## Afdeling

Een **afdeling** vertegenwoordigt een dienst of een divisie van een entiteit (bijvoorbeeld HR, IT, marketing, juridische zaken). Ze verfijnt de verdeling van de activiteiten binnen één entiteit.

U gebruikt afdelingen om:

* verwerkingsactiviteiten of audits te filteren op perimeter,
* taken of verzoeken toe te wijzen aan een gerichte groep,
* een team toegangsrechten te geven op een precieze perimeter.

Een afdeling kan onderliggende afdelingen hebben. Een entiteit kan ook onderliggende entiteiten hebben, bijvoorbeeld om de dochterondernemingen van een groep weer te geven.

{% hint style="info" %}
Afdelingen zijn optioneel. Ze zijn nuttig zodra de organisatie meerdere diensten heeft waarvan u de verwerkingsactiviteiten afzonderlijk wilt volgen.
{% endhint %}

***

## Eigenaar van de organisatie

De **eigenaar** is de hoofdbeheerder van de organisatie. Alleen eigenaren kunnen werkruimten aanmaken, de instellingen van de organisatie wijzigen, aangepaste rollen aanmaken en andere eigenaren toevoegen of verwijderen.

Beperk het aantal eigenaren om het bestuur overzichtelijk te houden. Andere gebruikers krijgen rollen die bij hun behoeften passen: zie [Rollen en rechten beheren](roles.md).

***

## Credits en quota

Uw abonnement bepaalt de credits, dat zijn limieten voor wat uw organisatie kan aanmaken of verbruiken. Ze worden gedeeld door alle werkruimten van de organisatie.

* **Gebruikers**: actieve gebruikers plus de gebruikers die aan een openstaande of verlopen uitnodiging zijn gekoppeld. Het verwijderen van de gebruiker van een uitnodiging maakt een plaats vrij. Zie [Gebruikers uitnodigen](users.md).
* **Entiteiten**: het aanmaken van een entiteit verbruikt één entiteitscredit. Zie [Organisatorische eenheden aanmaken en instellen](organizational-units.md).
* **Vragenlijstsjablonen**: de sjablonen van al uw werkruimten tellen mee, ook die in de prullenbak. Zie [Een vragenlijstsjabloon aanmaken](../../features/questionnaires/templates/README.md).
* **Verwerkingsactiviteiten, documentopslag, logboeken van cookietoestemming, activiteitengeschiedenis**: de pagina **Plan/abonnement wijzigen** van de organisatie-instellingen toont het krediet van uw plan voor elk ervan.
* **AI**: een maandelijks quotum aan AI-credits, beschreven in [Werking](../../features/general/ai-assistant/how-it-works.md#ai-credits-en-quota).

Wanneer een limiet is bereikt, meldt het betrokken scherm dat en biedt het een link om contact op te nemen met het Dastra-team en uw credit te verhogen.
