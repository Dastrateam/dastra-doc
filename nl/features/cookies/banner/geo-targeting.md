---
description: Toon een andere cookiebanner afhankelijk van de geografische locatie van de gebruiker.
---

# Geogerichte varianten

## Overzicht

Met de toestemmingsmodule van Dastra maakt u geogerichte varianten van uw cookiebanner. Elke variant is een aangepaste versie van de widget (uiterlijk, teksten, getoonde diensten) die automatisch wordt weergegeven op basis van de geografische locatie van de gebruiker, bepaald via het IP-adres.

Deze functie is vooral nuttig voor organisaties die in meerdere landen of regelgevingszones actief zijn, omdat de verplichtingen rond cookietoestemming sterk per rechtsgebied verschillen (AVG en e-privacyrichtlijn in Europa, CCPA in Californië, LGPD in Brazilië enzovoort).

{% hint style="info" %}
Waarom dit juridisch van belang is

Een banner die in Frankrijk conform is, is dat niet noodzakelijk voor een gebruiker in Californië (opt-out in plaats van opt-in) of in het Verenigd Koninkrijk (na de Brexit heeft de ICO eigen richtlijnen). Met geogerichte varianten past u uw toestemmingsbeheer precies aan elke juridische context aan, zonder extra widgets aan te maken.
{% endhint %}

***

## Een geogerichte variant aanmaken

### 1. De configuratie openen

Selecteer in de module **Toestemming voor cookies** uw widget. Open rechtsboven het keuzemenu dat de actieve configuratie toont (standaard **Standaardconfiguratie**) en klik op **Maak een geogerichte variant**.

### 2. De variant een naam geven

Vul een beschrijvend label in (maximaal 80 tekens) bij **Geogericht variatielabel**. Kies een duidelijke naam, zodat u de varianten later terugvindt, bijvoorbeeld: `Banner - Californië (CCPA)` of `Banner - EER`.

### 3. De geografische zones selecteren

Kies bij **Landen of geografische regio's waarop de banner zich richt** de landen of regio's waarop deze variant van toepassing is. In de lijst kunt u zoeken.

Dastra biedt twee snelkeuzes:

* **EU/EEE**: selecteert automatisch alle landen van de Europese Economische Ruimte.
* **Allemaal adequaat land**: selecteert de landen die de Europese Commissie krachtens artikel 45 van de AVG als adequaat erkent.

De lijst is per land georganiseerd en u kunt ook regio's binnen een land als doel kiezen (bijvoorbeeld Franse regio's of Amerikaanse staten). Zo maakt u bijvoorbeeld een variant die alleen voor Californië geldt, naast een algemenere widget voor de Verenigde Staten.

{% hint style="warning" %}
Voorrangsregel voor varianten

Kunnen meerdere varianten op dezelfde gebruiker van toepassing zijn (bijvoorbeeld een gebruiker in Île-de-France met een variant "Frankrijk" en een variant "Île-de-France"), dan krijgt de meest specifieke variant (regio) voorrang op de algemenere (land).
{% endhint %}

### 4. De variant aanpassen

Zodra de variant is aangemaakt, configureert u ze volledig onafhankelijk van de hoofdwidget:

* **Uiterlijk van de widget**: kleuren, indeling, knoppen
* **Teksten en vertalingen**: teksten die aan de lokale juridische context zijn aangepast
* **Diensten**: u beperkt of breidt de lijst van getoonde trackers uit
* **Triggers**: specifieke weergavevoorwaarden

### 5. De weergave van de banner uitschakelen (optioneel)

Met een optie toont u voor gebruikers in de doelzone geen banner.

Is de optie **Schakel de bannerweergave uit (alle cookies met standaardtoestemming worden geactiveerd)** ingeschakeld, dan krijgen de betrokken bezoekers geen toestemmingsvenster te zien. Alle cookies worden dan geactiveerd met hun standaardtoestemming, zoals die per dienst in de widget is ingesteld.

{% hint style="warning" %}
Alleen voor zones zonder voorafgaande toestemmingsplicht

Deze optie is bedoeld voor landen waar de lokale regelgeving geen actieve toestemming vereist voordat cookies worden geplaatst (bijvoorbeeld bepaalde landen buiten de EER zonder gelijkwaardige e-privacywetgeving). Gebruik ze nooit voor gebruikers in de EU/EER, in het Verenigd Koninkrijk of in een ander rechtsgebied dat opt-in vereist.
{% endhint %}

{% hint style="info" %}
De standaardtoestemming per dienst stelt u in bij de instellingen van de widget, in het onderdeel **Diensten**. Controleer die waarden voordat u deze optie inschakelt.
{% endhint %}

***

## Typische gebruikssituaties

| Situatie | Aanbevolen configuratie |
| --- | --- |
| Europese site met Amerikaans verkeer | EER-variant (strikte opt-in) en variant VS/Californië (CCPA, opt-out) |
| Franse site met een Duitse dochteronderneming | Variant Frankrijk en variant Duitsland met teksten die aan de eisen van de BfDI zijn aangepast |
| Wereldwijde site met minimale conformiteit buiten de EER | Standaardwidget voor de hele wereld en een variant conform de AVG voor de EER |

***

## Technische werking

De Dastra-SDK bepaalt de geografische locatie automatisch op basis van het IP-adres van de gebruiker. Aan uw kant is geen extra configuratie nodig.

In het toestemmingsprofiel van de gebruiker worden geen locatiegegevens opgeslagen: de geolocatie dient alleen om de weer te geven variant te kiezen.

{% hint style="info" %}
Om de weergave van een bepaalde variant vanuit uw browser te testen, gebruikt u een VPN of vraagt u de ondersteuning van Dastra om een voorbeeldmodus voor zones in te schakelen.
{% endhint %}
