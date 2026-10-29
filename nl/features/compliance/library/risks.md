---
description: >-
  De risicobibliotheek helpt bij het identificeren, kwalificeren en opvolgen van
  de risico's die verbonden zijn aan de vereisten en controles van de
  conformiteitskaders.
---

# Risico's

In Dastra is een risico een gevreesde gebeurtenis die een negatief effect kan hebben op de organisatie, in verband met het gebruik, de ontwikkeling of de werking van systemen (bijvoorbeeld AI-systemen).

Risico's zijn een belangrijk stuurelement: ze meten de blootstelling van de organisatie en beoordelen de werkelijke doeltreffendheid van de bestaande controles.

***

## Risico's en controles: een centrale relatie

Het is essentieel te begrijpen dat risico's nooit los staan van de rest.

In Dastra geldt:

* een risico wordt gedekt door een of meer controles,
* een controle draagt bij aan het verminderen van een of meer risico's.

Controles vormen dus de maatregelen om risico's te beperken.\
Ze verminderen:

* de waarschijnlijkheid dat het risico zich voordoet,
* en/of de impact ervan op de organisatie.

Door deze relatie gaat u van een declaratieve aanpak naar operationeel risicobeheer, op basis van concrete en controleerbare acties.

***

## Weergave van de risicobibliotheek

<figure><img src="../../../.gitbook/assets/image-497.png" alt="Weergave van de risicobibliotheek met de lijst van risico's"><figcaption></figcaption></figure>

De risicobibliotheek geeft een globaal overzicht van de geïdentificeerde risico's, met onder meer:

* hun referentie en beschrijving,
* de gekoppelde labels (vertrouwelijkheid, prestaties, robuustheid enzovoort),
* het initiële niveau van impact en waarschijnlijkheid,
* filters voor een overkoepelende analyse.

Met deze weergave kunt u:

* de belangrijkste risico's identificeren,
* nagaan of ze door controles worden gedekt,
* de conformiteitsinspanningen prioriteren.

***

## Een risico aanmaken en beschrijven

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image-498.png" alt="Venster voor het bewerken van een risico met de naam, de referentie, de beschrijving en de beoordeling"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Bij het aanmaken of bewerken van een risico geeft de gebruiker op:

* de naam en de referentie van het risico,
* een beschrijving waarmee het risicoscenario wordt gekwalificeerd,
* labels om de categorisering te vergemakkelijken.
{% endcolumn %}
{% endcolumns %}

***

## Risicobeoordeling

Voor elk risico voert u twee beoordelingen in, het initiële risico en het restrisico. Daarnaast berekent Dastra een derde niveau, het huidige risico:

### Initieel risico

Het initiële risico is het risiconiveau vóór de invoering van de controles.

Het wordt beoordeeld aan de hand van:

* een waarschijnlijkheid,
* een impact.

Deze twee dimensies worden geplaatst op een gestandaardiseerd risicoraster.

***

### Restrisico

Het restrisico is het risiconiveau na toepassing van de gekoppelde controles.

Door het initiële risico en het restrisico te vergelijken kunt u:

* de doeltreffendheid van de controles meten,
* de vermindering van het risico visualiseren,
* de gekozen remediëring rechtvaardigen.

In dit stadium is het risicoraster vast en voor alle risico's gelijk, zodat de beoordeling homogeen en vergelijkbaar blijft.

***

### Huidig risico

In een project toont Dastra ook het huidige risico. Het geeft het risiconiveau op een bepaald moment weer, op basis van de werkelijke voortgang van de remediëringsacties en de controles. Het ontwikkelt zich dus tussen het initiële risico en het restrisico.

De drie niveaus ziet u naast elkaar in de weergave **Cartography** van het tabblad **Risico's** van een project (zie [Projectimplementatie](../projects/implement.md)).

***

## Controles koppelen

{% columns %}
{% column %}
Een risico moet aan een of meer controles worden gekoppeld: de maatregelen die zijn ingevoerd om het te beperken.

Dankzij de koppeling kunt u:

* duidelijk zien welke hefbomen het risico verminderen,
* de invloed van de controles op het restrisico opvolgen,
* de traceerbaarheid tussen conformiteit en risicobeheer waarborgen.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-499.png" alt="Zoeken naar controles om aan een risico te koppelen"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## Bedreigingen koppelen

Risico's kunt u ook koppelen aan bedreigingen: de gebeurtenissen of oorzaken die het risico kunnen doen ontstaan.

Voorbeeld:

* Bedreiging: gebrek aan monitoring van AI-logs
* Risico: informatielek via AI-vragen

Dit onderscheid maakt een fijnere en meer gestructureerde analyse van risicoscenario's mogelijk.

***

## Risico's samenvoegen

Net als bij controles en tests kan de risicobibliotheek duplicaten bevatten. Selecteer ten minste twee risico's en klik vervolgens op **Samenvoegen** in de bulkacties, of op **Samenvoegen** in het bewerkingsvenster van een risico. De wizard is dezelfde als voor controles: kies de **Reference version** en de velden die u wilt overnemen (zie [Controles](controls.md)). Het samenvoegen kan niet ongedaan worden gemaakt.

***

## Waarom risico's in de bibliotheek opnemen

Door risico's in de bibliotheek te centraliseren hebt u:

* een overkoepelend overzicht van de risico's in alle kaders,
* een consistentere beoordeling,
* een rechtstreeks verband tussen risico's, controles en vereisten,
* een doeltreffendere sturing van conformiteit en beveiliging.
