---
description: Leer hoe u het register van de verwerker in Dastra gebruikt.
---

# Register van de verwerker

## Inleiding

Artikel 30 van de AVG bevat specifieke verplichtingen voor het register van de verwerkingsverantwoordelijke en voor het register van de verwerker. Als uw organisatie zowel als verwerker als als verwerkingsverantwoordelijke optreedt, moet uw register de twee categorieën activiteiten duidelijk onderscheiden.

In dat geval raadt de CNIL aan twee registers bij te houden:

1. een register voor de verwerkingen van persoonsgegevens waarvoor u zelf verantwoordelijk bent,
2. een register voor de verwerkingen die u als verwerker uitvoert namens uw klanten.

De rest van deze pagina gaat alleen over het register van de verwerker.

## Het register van de verwerker

Elke verwerker moet een minder uitgebreid register bijhouden.

Dit register bevat:

* de contactgegevens van de verwerker, van zijn vertegenwoordiger (indien van toepassing) en van zijn FG
* de contactgegevens van alle verwerkingsverantwoordelijken namens wie de verwerker optreedt (meestal de klanten)
* de categorieën van verwerkte gegevens
* de ontvangers
* de doorgiften buiten de EER
* de beveiligingsmaatregelen

In Dastra wordt een verwerkingsactiviteit die als verwerker is aangemaakt, gedocumenteerd in 12 secties: **Algemeen**, **Stakeholders**, **Doeleinden**, **Activa**, **Gegevens**, **Klanten**, **Betrokken personen**, **Rechten van betrokkenen**, **Ontvangers**, **Maatregelen**, **Documentatie** en **Samenvatting**.

Vergeleken met een activiteit als verwerkingsverantwoordelijke kunt u in de sectie **Klanten** de verwerkingsverantwoordelijken opgeven namens wie u optreedt (meestal uw klanten), en er is geen sectie **Impactanalyse**.

<figure><img src="../../.gitbook/assets/ropa-processor-1.png" alt="Sectienavigatie van een verwerkingsactiviteit als verwerker"><figcaption><p>De verschillende secties van een verwerkingsactiviteit als verwerker in Dastra</p></figcaption></figure>

## De sectie Klanten

De sectie **Klanten** bevat de verwerkingsverantwoordelijken namens wie u de gegevens verwerkt, meestal uw klanten. U moet met elk van hen een contract ondertekenen waarin de clausules van artikel 28 van de AVG zijn opgenomen.

<figure><img src="../../.gitbook/assets/ropa-processor-2.png" alt="Sectie Klanten van een verwerkingsactiviteit als verwerker met de knop Voeg klant/RT toe"><figcaption><p>De sectie Klanten van een verwerkingsactiviteit als verwerker</p></figcaption></figure>

Een verwerkingsverantwoordelijke opgeven:

1. Klik op **Voeg klant/RT toe**.
2. Kies **Referentielijst van actoren (aanbevolen)** om een stakeholder uit uw repository te selecteren, of **Selecteer een afdeling of entiteit**.
3. Beschrijf eventueel uw bewerkingen bij **Beschrijf de bewerkingen die op de gegevens zijn uitgevoerd**.
4. Ontvangt de verwerkingsverantwoordelijke ook de gegevens, schakel dan **Is de klant/verwerker de ontvanger van de gegevens?** in. Kies bij **Welke gegevens zijn betrokken?** voor **Alle datasets (standaard)** of **Toegang tot bepaalde datasets** en vink de betreffende datasets aan.
5. Bevestig.

Om meerdere verwerkingsverantwoordelijken tegelijk toe te voegen, klikt u op de pijl rechts van **Voeg klant/RT toe** en kiest u **Voeg actoren in bulk toe** om meerdere stakeholders te selecteren, of **Voeg org. eenheden in bulk toe** om meerdere organisatie-eenheden te selecteren.

Met het menu aan het einde van elke rij kunt u de verwerkingsverantwoordelijke **Bewerken**, **Acteur bewerken** of **Verwijderen**. Gebruikt uw werkruimte de module Contracten, dan maakt **Genereer een VWO** de verwerkersovereenkomst van de verwerkingsverantwoordelijke aan. Om meerdere verwerkingsverantwoordelijken te verwijderen, vinkt u ze aan en klikt u op **Verwijderen**.

Om een verwerkingsverantwoordelijke alleen zijn eigen gegevens te sturen, gebruikt u de optie **Exporteren voor klant/gegevensbeheerder** van het exportvenster: het bestand sluit dan de andere verwerkingsverantwoordelijken uit (zie [Het register exporteren en importeren](export-import.md)).

***

{% hint style="info" %}
U kunt het type van een verwerkingsactiviteit wijzigen (van een activiteit als verwerkingsverantwoordelijke naar een activiteit als verwerker, en omgekeerd).\
[De werkwijze staat in de veelgestelde vragen](faq.md#hoe-wijzigt-u-het-type-van-een-verwerkingsactiviteit-van-een-activiteit-als-verwerkingsverantwoordelijke-naar-een-activiteit-als-verwerker-en-omgekeerd)

Zet u een activiteit als verwerker terug naar een activiteit als verwerkingsverantwoordelijke, dan worden de eraan gekoppelde klanten verwijderd.
{% endhint %}

## Meer informatie

{% content-ref url="controller.md" %}
[Register van de verwerkingsverantwoordelijke](controller.md)
{% endcontent-ref %}
