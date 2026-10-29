---
description: >-
  Laat een kader evolueren via opeenvolgende versies, publiceer ze, kies de
  huidige versie en werk de conformiteitsprojecten bij die het kader gebruiken.
---

# Versies van een kader

Elk kader in de bibliotheek heeft versies. Een versie heeft een automatisch toegekend nummer (_Versie 1_, _Versie 2_ enzovoort), een versieopmerking en een status (concept of gepubliceerd). Met versies laat u een kader evolueren (wijziging van de regelgeving, toegevoegde of herformuleerde vereisten, hergroepeerde hoofdstukken) zonder de conformiteitsprojecten te wijzigen die een eerdere versie gebruiken.

<figure><img src="../../../../.gitbook/assets/compliance-framework-detail-version-header.png" alt="Kop van een kader met het versienummer, het label Huidige versie en de status Gepubliceerd"><figcaption><p>Het versienummer, het label Huidige versie en de status staan onder de naam van het kader</p></figcaption></figure>

***

## Versienummer en huidige versie

Het versienummer staat onder de naam van het kader, op de kaart in de lijst van kaders en op het tabblad **Details** (kaart **Versie-informatie**, samen met de versieopmerking).

Het label **Huidige versie** geeft de versie aan die standaard wordt geïnstalleerd wanneer het kader aan een project wordt toegevoegd. Een kader heeft slechts één huidige versie.

De lijst van kaders in de bibliotheek toont de huidige versie van elk kader. De andere versies vindt u op het tabblad **Versies** van het kader.

***

## De versiegeschiedenis bekijken

Het tabblad **Versies** van een kader toont al zijn versies, van de meest recente tot de oudste. Elke rij toont:

* het versienummer en, in voorkomend geval, het label **Huidige versie**,
* de status (concept of gepubliceerd),
* de versieopmerking,
* de aanmaakdatum en de auteur van de versie.

Klik op een versie (of op **Zie** in het actiemenu) om ze te openen. Een gepubliceerde versie opent in de modus alleen-lezen.

Afhankelijk van de status biedt het actiemenu van elke versie:

* **Zie**: de versie openen,
* **Wijzig de release-opmerking**,
* **Instellen als huidige versie** (gepubliceerde versie die niet de huidige versie is),
* **Publiceren** (conceptversie),
* **Publicatie annuleren** (gepubliceerde versie),
* **Verwijderen** (conceptversie).

***

## Een versie aanmaken

1. Open het kader en daarna het tabblad **Versies**.
2. Klik op **Een nieuwe versie aanmaken**.
3. Het venster toont het automatisch toegekende nummer (**Nieuwe versie:** _Versie n_). Voer eventueel **Versieopmerkingen** in (maximaal 3.000 tekens), bijvoorbeeld _Regelgevende update 2026_.
4. Klik op **Valideren**.

De versie kopieert de structuur van het kader (hoofdstukken, vereisten en gekoppelde controles) en wordt aangemaakt als concept. Ze opent meteen: klik op **Bewerken** om de hoofdstukken en vereisten te laten evolueren (zie [Een eigen kader aanmaken](custom.md)).

Met de knop **Een nieuwe versie importeren** op het tabblad **Versies** maakt u ook een versie aan op basis van een JSON- of Excel-bestand.

U kunt de versieopmerking op elk moment wijzigen via het actiemenu van de versie (**Wijzig de release-opmerking**).

{% hint style="info" %}
De versies van een kader worden niet apart geteld in het frameworkquotum: een versie aanmaken of importeren kost geen frameworkcredit.
{% endhint %}

***

## Een versie publiceren, depubliceren of verwijderen

* **Publiceren**: via het actiemenu van de versie of met de knop **Publiceren** boven aan de kaderpagina. Een gepubliceerde versie wordt aangeboden wanneer het kader aan een project wordt toegevoegd. Meerdere gepubliceerde versies van hetzelfde kader kunnen naast elkaar bestaan.
* **Publicatie annuleren**: de versie wordt weer een concept en wordt niet meer aangeboden wanneer het kader aan een project wordt toegevoegd. De huidige versie kan niet worden gedepubliceerd: stel eerst een andere versie in als huidige versie.
* **Verwijderen**: alleen een conceptversie kan worden verwijderd. De andere versies van het kader worden niet beïnvloed.

{% hint style="warning" %}
De vereisten van een gepubliceerde versie zijn vergrendeld: de knop **Bewerken** is uitgeschakeld. Maak een versie aan om de hoofdstukken of vereisten te wijzigen. De naam, het logo en de beschrijving van het kader (tabblad **Details**) blijven bewerkbaar op een gepubliceerde versie.
{% endhint %}

***

## De huidige versie instellen

Open op het tabblad **Versies** het actiemenu van een gepubliceerde versie en klik op **Instellen als huidige versie**.

Deze versie wordt de versie die standaard wordt aangeboden en geïnstalleerd wanneer het kader aan een project wordt toegevoegd. Projecten die een andere versie gebruiken, blijven ongewijzigd.

***

## Bijwerken vanuit het bronreferentiekader

Als een kader is aangemaakt op basis van een sjabloon en er een nieuwere versie van dat bronreferentiekader beschikbaar is:

* toont de kaderkaart in de lijst het label **Beschikbare update**,
* toont de kaderpagina de banner **Een nieuwere versie van de bronnent repository is beschikbaar**, gevolgd door de link **bijwerken**.

Klik op **bijwerken** om het venster **Bijwerken vanuit de bronnent repository** te openen. Het toont een voorbeeld van de wijzigingen in controles, tests, risicoscenario's en bedreigingen. Items die uit het bronreferentiekader zijn verwijderd, zijn gemarkeerd met het label **Afwezig van de bron**.

Klik op **Valideren**: op basis van de bron wordt een gepubliceerde versie van het kader aangemaakt, die de huidige versie wordt. Eerdere versies en de projecten die ze gebruiken, worden niet beïnvloed.

***

## Versies en conformiteitsprojecten

### De te installeren versie kiezen

Wanneer een kader aan een project wordt toegevoegd (**Een framework aan het project toevoegen**), worden alleen gepubliceerde versies aangeboden. Bestaan er meerdere gepubliceerde versies, dan verschijnt naast de naam van het kader een keuzelijst (**Te installeren versie**), met de huidige versie vooraf geselecteerd. Het project wordt vervolgens gekoppeld aan de geïnstalleerde versie.

### Een project herkennen dat moet worden bijgewerkt

In het projectoverzicht toont de kaart van elk kader het nummer van de gebruikte versie. Het label **Beschikbare update** geeft aan dat het project een versie gebruikt die niet meer de huidige versie van het kader is.

<figure><img src="../../../../.gitbook/assets/compliance-project-overview-framework-update-available.png" alt="Kaderkaart in een project met het versienummer en het label Beschikbare update"><figcaption><p>Het label Beschikbare update markeert een project dat aan een eerdere versie van het kader is gekoppeld</p></figcaption></figure>

### Een project naar een andere versie verplaatsen

1. Open in het projectoverzicht het actiemenu van de kaderkaart en klik op **Werk de versie van het framework bij**.
2. Kies de **Doelversie** uit de andere gepubliceerde versies. De versieopmerking en een voorbeeld van de items die aan het project worden toegevoegd, worden getoond.
3. Klik op **Valideren**.

Tijdens de migratie:

* worden de items van de doelversie aan het project toegevoegd,
* worden de labels, beschrijvingen en tags van de bestaande controles, tests, risicoscenario's en bedreigingen vernieuwd op basis van de doelversie,
* blijven resultaten en bewijs behouden,
* worden controles die de doelversie niet bevat, losgekoppeld van de vereisten, maar blijven ze in het project (een bericht toont het aantal voordat u bevestigt).

{% hint style="warning" %}
De migratie gebeurt altijd handmatig: een project wordt nooit automatisch naar de huidige versie verplaatst. Ze is niet mogelijk zolang er een audit loopt in het project.
{% endhint %}
