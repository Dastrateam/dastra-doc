---
description: Leer hoe u generieke relaties tussen elementen in Dastra aanmaakt.
---

# Generieke relaties

## Over generieke relaties

Een generieke relatie is een eenvoudige, benoemde koppeling tussen twee elementen in Dastra. Daarmee documenteert u verbanden tussen objecten die het platform niet automatisch afleidt, bijvoorbeeld een activum koppelen aan een stakeholder, of een risico aan een datalek.

Een relatie wordt gekenmerkt door:

* een bronobject en een doelobject,
* een relatielabel (optioneel, bijvoorbeeld "Verwerkingsverantwoordelijke", "Beheerd door"),
* een samenvatting (optioneel, voor extra context),
* een richting, die u indien nodig kunt omkeren.

{% hint style="info" %}
Eén element kan aan meerdere andere elementen van verschillende types worden gekoppeld.
{% endhint %}

## Beschikbaarheid van generieke relaties

U kunt generieke relaties aanmaken vanuit de volgende elementen:

* Activa
* Stakeholders
* Beveiligingsmaatregelen
* Datalekken
* Datasets
* Risico's

Ze worden vooral gebruikt in de module Activa en in de repositories (cartografie), waar de volledige relatiegrafiek wordt weergegeven.

## Een generieke relatie toevoegen

1. Open een element (bijvoorbeeld een activum).
2. Klik op het pictogram **Gekoppelde elementen** in de werkbalk bovenaan. Het toont het huidige aantal gekoppelde elementen.
3. Klik op **Voeg een relatie toe** en selecteer het type object waaraan u wilt koppelen (stakeholder, beveiligingsmaatregel, datalek, activum, dataset of risico).
4. Doe in het venster het volgende:
   * Schakel **Omgekeerde relatie** in als de richting moet worden omgekeerd.
   * Kies **Bestaand object** om te koppelen aan een element dat al in Dastra staat, of **Maak een nieuw object** om meteen een nieuw element aan te maken.
   * Selecteer het doelobject in de keuzelijst.
   * Voeg desgewenst een **Relatie-label** en een samenvatting toe.
5. Klik op **Toevoegen** om de relatie op te slaan.

## Relaties visualiseren

Zodra relaties zijn aangemaakt, verschijnen ze in:

* Het paneel **Gekoppelde elementen** van elk element, met alle directe koppelingen.
* De knooppuntgrafiek in de cartografieweergave, waar alle relaties als een verbonden netwerk worden getoond.

## Verder lezen

{% content-ref url="README.md" %}
[Gegevens in kaart brengen](README.md)
{% endcontent-ref %}
