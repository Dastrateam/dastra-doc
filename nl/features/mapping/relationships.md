---
description: >-
  Leer hoe u generieke relaties tussen elementen in Dastra aanmaakt.
---

# Generieke relaties

## Definitie van een generieke relatie

Een generieke relatie is een eenvoudige, benoemde koppeling tussen twee elementen in Dastra. Daarmee documenteert u verbanden tussen objecten die het platform niet automatisch afleidt, bijvoorbeeld een actief koppelen aan een stakeholder, of een datalek aan een risico.

Een relatie wordt gekenmerkt door:

* een bronobject en een doelobject,
* een relatielabel (optioneel, bijvoorbeeld "Verwerkingsverantwoordelijke" of "Beheerd door"),
* een samenvatting (optioneel, voor extra context),
* een richting, die u indien nodig kunt omkeren.

{% hint style="info" %}
Eén element kan aan meerdere andere elementen van verschillende types worden gekoppeld.
{% endhint %}

## Waar u een generieke relatie aanmaakt

U maakt een relatie aan vanuit het formulier van een:

* actief,
* stakeholder,
* dataset,
* beveiligingsmaatregel,
* datalek.

Het doelobject kan van een van deze types zijn, of een risico als de module voor risicobeheer is ingeschakeld en u er toegang toe hebt. Een risico zelf heeft geen generieke relaties.

Relaties verschijnen op de pagina **In kaart brengen** van de module **Referenties**, waar ze de knooppunten van de grafiek verbinden. Zie [Referenties](repositories/README.md).

Om verwerkingsactiviteiten aan elkaar te koppelen, zie [Relaties tussen verwerkingsactiviteiten aanmaken](../ropa/relationships.md).

## Een generieke relatie toevoegen

1. Open een element, bijvoorbeeld een actief.
2. Klik in de werkbalk op **Gekoppelde elementen**. De knop toont het aantal bestaande koppelingen.
3. Klik op **Voeg een relatie toe** en selecteer daarna het type object waaraan u wilt koppelen: stakeholder, beveiligingsmaatregel, datalek, actief, dataset of risico.
4. Doe in het venster het volgende:
   * Schakel **Omgekeerde relatie** in als de richting moet worden omgekeerd.
   * Kies **Bestaand object** om te koppelen aan een element dat al in Dastra staat, of **Maak een nieuw object** om meteen een nieuw element aan te maken.
   * Selecteer bij **Bestaand object** de doelobjecten in **Bijgevoegde object (en) selecteren**. Typ bij **Maak een nieuw object** de naam van het nieuwe object.
   * Vul desgewenst het **Relatie-label** en de **Samenvatting** in.
5. Klik op **Toevoegen** om de relatie op te slaan.

## Relaties bekijken

Zodra relaties zijn aangemaakt, verschijnen ze:

* in het paneel **Gekoppelde elementen** van elk element, met alle directe koppelingen;
* in de grafieken **In kaart brengen van stromen tussen activa** en **In kaart brengen van stakeholders** van de pagina **In kaart brengen**, waar ze als netwerk worden weergegeven.

## Verder lezen

{% content-ref url="README.md" %}
[Gegevens in kaart brengen](README.md)
{% endcontent-ref %}
