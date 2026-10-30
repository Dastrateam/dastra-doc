---
description: >-
  Met Dastra brengt u de risico's van verwerkingsactiviteiten in kaart om snel
  het prioriteitsniveau en de te nemen acties voor een verwerkingsactiviteit te
  beoordelen.
---

# Een risico aan een verwerkingsactiviteit koppelen

## Een risico aan een verwerkingsactiviteit toevoegen

1. Open de verwerkingsactiviteit in het verwerkingsregister.
2. Klik in de rij met knoppen onder de titel op **Risico's**. De knop toont het aantal risico's dat al aan de verwerkingsactiviteit is gekoppeld.

<figure><img src="../../.gitbook/assets/risks-attach-1.png" alt="Pagina van een verwerkingsactiviteit met de knop Risico's en de teller in de rij met knoppen"><figcaption><p>De knop Risico's van een verwerkingsactiviteit</p></figcaption></figure>

3. Klik in het paneel dat opent op **Creëer een risico**.

<figure><img src="../../.gitbook/assets/risks-attach-2.png" alt="Paneel Risico's van een verwerkingsactiviteit met de matrix, de gekoppelde risico's en de knop Creëer een risico"><figcaption><p>Het paneel Risico's van een verwerkingsactiviteit</p></figcaption></figure>

U komt op de bewerkingspagina van het risico, met de verwerkingsactiviteit en de organisatorische eenheid ervan al ingevuld. Begin met het invoeren van de informatie over het risico dat u hebt geïdentificeerd, zoals beschreven in [1. Identificeren](process/identify.md).

U kunt een risico ook vanuit de module voor risicobeheer aan een verwerkingsactiviteit koppelen: open **Risicobeheer** > **Risico's**, kies het tabblad **Gegevensverwerking** en klik op **Creëer een risico**.

## De risico's van een verwerkingsactiviteit bekijken

Om de risico's van al uw verwerkingsactiviteiten te zien, opent u **Risicobeheer** > **Risico's** en kiest u het tabblad **Gegevensverwerking**. Elke rij toont het risicotype, de betreffende verwerkingsactiviteit en het initiële, het huidige en het restrisiconiveau.

<figure><img src="../../.gitbook/assets/risks-list-1.png" alt="Lijst met de risico's van het tabblad Gegevensverwerking, met initiële, huidige en restrisico's"><figcaption><p>De risico's die aan verwerkingsactiviteiten zijn gekoppeld</p></figcaption></figure>

## Beoordeling van het risiconiveau

Het risiconiveau wordt met de volgende formule berekend:

`Risiconiveau = waarschijnlijkheidswaarde x impactwaarde`

Dastra toont het in punten op het maximum van de schaal (bijvoorbeeld 16/25) en als percentage. Het percentage wordt met de volgende formule berekend:

`(impact x waarschijnlijkheid) / maximumscore van de actieve risicoschaal`

De maximumscore van de schaal is 25 bij de standaardschaal met 5 niveaus (5 x 5), 16 bij de schaal met 4 niveaus en 9 bij de schaal met 3 niveaus. Zie [De risicoschaal configureren](process/assess.md#de-risicoschaal-configureren).

Het dashboard van de werkruimte bevat een module **Risicobeheer**. Die toont de gemiddelden, als percentages, van het initiële, het huidige en het restrisico, de gemiddelde remediëring, het aantal risico's per stap (**Totaal**, **Geïdentificeerd**, **Geen antwoord**) en de verdeling van de lage, gemiddelde en hoge restrisico's. Elk gemiddelde is gebaseerd op de hierboven berekende percentages.

## Verder gaan

{% content-ref url="../tasks/README.md" %}
[Planning](../tasks/README.md)
{% endcontent-ref %}
