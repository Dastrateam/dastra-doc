---
description: >-
  Voordat u begint met de technische implementatie van de Dastra widget, raden we u aan om de cookies op uw websites te controleren.
  raden we u aan de cookies op uw websites te controleren.
  sites.
---

# Vooronderzoek

## 1. neem contact op met uw webmaster of webbureau

Voordat u de Dastra widget implementeert, raden wij u aan contact op te nemen met de persoon die verantwoordelijk is voor het integreren van tags en andere markers op uw website en deze uit te nodigen voor uw werkruimte. Deze persoon kan dan de door Dastra gegenereerde code-elementen ophalen die nodig zijn om de verschillende technische acties uit te voeren (het instellen van de banner, het effectief blokkeren van cookies in geval van non-consent, etc.).

## 2. Voer een mini-audit uit van de cookies op uw site of web-app

Om deze audit uit te voeren, kunt u het onderstaande Excel-bestandssjabloon gebruiken:

{% file src="../../..gitbook/assets/template-audit.xlsx" %}

Deze mini-audit zal het integratiewerk van het technische team enorm vergemakkelijken.

### Maak een lijst van de services/cookies die aan uw domeinnaam zijn gekoppeld

Om u te helpen, kunt u onze kant-en-klare cookie-scantool gebruiken: [https://app.dastra.eu/workspace/19/cookie-widget/integration/scan](https://app.dastra.eu/workspace/19/cookie-widget/integration/scan)\.
Hiermee kunt u ter plekke de services identificeren die op uw site zijn geïnstalleerd vanuit onze cookie-database.

{% content-ref url="scannez-les-cookies-deposes-sur-votre-site-web.md" %}
[scan-de-cookies-gedeponeerd-op-uw-website](scannez-les-cookies-deposes-sur-votre-site-web.md)
{% endcontent-ref %}

Daarnaast is het raadzaam om een gedetailleerd onderzoek uit te voeren naar alle services die op uw site zijn geïnstalleerd (onderzoek van de broncode van de pagina, inspectie van cookies, enz.) Tools zoals [https://builtwith.com/](https://builtwith.com/) kunnen u ook helpen bij het inventariseren van deze services.

Voor elk domein of elke website die u in kaart wilt brengen, raden we u aan een volledige lijst op te stellen van diensten van derden die cookies gebruiken.

Zodra u een lijst hebt van de diensten die met uw site verbonden zijn, moet u de te volgen blokkeringsstrategie bepalen.

### Definitie van doeleinden

Elke geïdentificeerde dienst moet in een van deze categorieën worden ingedeeld:&#x20;

| Type | Id |
| ----------------------- | -- |
| Strikt noodzakelijk | 0 |
| Voorkeuren 1
| Analytisch 2
| Marketing | | 3 |
| Overige 4

### Het type service-integratie identificeren

Voor elke service moet u bepalen op welke manier de javascript-tag in de pagina is geïntegreerd:

* Directe javascript tag in de pagina
* Integratie in de js-code van de pagina (interne ontwikkeling)
* Integratie in een tagging tool (Google Tag Manager)
* Andere: iframe, enz.

### De te gebruiken blokkeringsstrategie bepalen

Er zijn verschillende strategieën mogelijk om cookies standaard te blokkeren, afhankelijk van uw behoeften:

* **Niet langer gebruiken**: deze bibliotheek is in feite overbodig, dus u kunt hem volledig verwijderen uit de bronnen van de site;
* **Volledig blokkeren** : De uitvoering van de tag wordt volledig geblokkeerd totdat de gebruiker cookies accepteert;
* **Gedeeltelijk blokkeren**: Alleen de trackingfuncties worden geblokkeerd (als de bibliotheek dit toestaat). Sommige bibliotheken kunnen in een volledig gedegradeerde modus werken zonder prestatieverlies.



