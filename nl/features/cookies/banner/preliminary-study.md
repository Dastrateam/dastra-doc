---
description: >-
  Voordat u begint met de technische implementatie van de Dastra-banner, raden we u aan een cookieaudit van uw websites uit te voeren.
---

# Vooronderzoek

## 1. Neem contact op met uw webmaster of webbureau

Voordat u de Dastra-banner implementeert, raden we u aan contact op te nemen met de persoon die verantwoordelijk is voor het integreren van tags en andere markeringen op uw website, en die persoon uit te nodigen in uw werkruimte. Die persoon kan dan de door Dastra gegenereerde code-elementen ophalen die nodig zijn voor de verschillende technische acties (de banner instellen, cookies daadwerkelijk blokkeren bij het ontbreken van toestemming enzovoort).

## 2. Voer een mini-audit uit van de cookies van uw website of webapplicatie

Voor deze audit kunt u het onderstaande Excel-sjabloon gebruiken:

{% file src="../../../.gitbook/assets/template-audit.xlsx" %}

Deze mini-audit bereidt het integratiewerk van het technische team voor.

### De diensten en cookies van uw domeinnaam opsommen

Als hulpmiddel kunt u de scantool voor cookies van Dastra gebruiken: klik in het menu op **Toestemming voor cookies** > **Banners** > **Creëer een widget** en kies daarna **Analyse van de website**. De tool herkent de diensten die op uw site zijn geïnstalleerd op basis van de cookiedatabase van Dastra.

{% content-ref url="scan.md" %}
[De op uw website geplaatste cookies scannen](scan.md)
{% endcontent-ref %}

Daarnaast raden we aan alle diensten die op uw site zijn geïnstalleerd nauwkeurig te onderzoeken (de broncode van de pagina nakijken, cookies inspecteren enzovoort). Hulpmiddelen zoals [https://builtwith.com/](https://builtwith.com/) kunnen u ook helpen deze diensten op te sommen.

Stel voor elk domein of elke website die u in kaart wilt brengen een volledige lijst op van de diensten van derden die trackers gebruiken.

Zodra u de lijst hebt van de diensten die aan uw site zijn gekoppeld, bepaalt u de blokkeerstrategie die u hanteert.

### Doeleinden bepalen

Elke geïdentificeerde dienst wordt in een van deze categorieën ingedeeld:

| Type                | Id |
| ------------------- | -- |
| Strikt noodzakelijk | 0  |
| Voorkeuren          | 1  |
| Analytisch          | 2  |
| Marketing           | 3  |
| Andere              | 4  |

### Het type integratie van de dienst bepalen

Bepaal voor elke dienst hoe de JavaScript-tag in de pagina is geïntegreerd:

* een directe JavaScript-tag in de pagina;
* integratie in de JavaScript-code van de pagina (interne ontwikkeling);
* integratie in een tagbeheertool (Google Tag Manager);
* andere: iframe enzovoort.

### De te hanteren blokkeerstrategie bepalen

Om cookies standaard te blokkeren zijn er verschillende strategieën mogelijk, afhankelijk van uw behoeften:

* **Niet meer gebruiken**: deze bibliotheek is eigenlijk niet nodig, dus u kunt haar volledig uit de bronnen van de site verwijderen;
* **Volledig blokkeren**: de uitvoering van de tag wordt volledig geblokkeerd zolang de gebruiker de cookies niet heeft geaccepteerd;
* **Gedeeltelijk blokkeren**: alleen de trackingfuncties worden geblokkeerd (als de bibliotheek dat toelaat). Sommige bibliotheken kunnen namelijk in een volledig gereduceerde modus werken zonder prestatieverlies.

{% content-ref url="scan.md" %}
[De op uw website geplaatste cookies scannen](scan.md)
{% endcontent-ref %}
