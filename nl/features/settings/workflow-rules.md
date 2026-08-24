---
description: Complexe processen integreren met aangepaste workflowregels
---

# Werkstroomregels

## Hoe het werkt

Workflow Rules in Dastra zijn een set van acties (e-mail notificaties, audit scheduling, taken en veld updates) die worden uitgevoerd wanneer aan bepaalde voorwaarden wordt voldaan. Deze regels automatiseren het proces van het verzenden van e-mail notificaties, het toewijzen van taken en het bijwerken van bepaalde velden in een record wanneer een regel wordt getriggerd.

![Basisprincipe diagram](<../../.gitbook/assets/image (258) (1).png>)

## Hoe maak je een workflow regel in Dastra?

* Ga naar [de workflow regels configuratie pagina uw werkruimte](https://app.dastra.eu/workspace/0/settings/workflow-rules)
* Klik op "Nieuwe workflow regel".
* Kies een naam en het betreffende type entiteit (Behandeling, Overtredingen...)
* U bent nu in de regelontwerper

### De trigger definiëren

U kunt een workflowregel op twee gebeurtenissen triggeren:&#x20;

* Wanneer **een actie wordt ondernomen op een betrokken entiteit**: wijziging, verwijdering of creatie&#x20;
* Wanneer een specifieke datum voor de entiteit wordt bereikt**. bijvoorbeeld: stuur een notificatie 10 dagen na de publicatiedatum;

Per workflowregel kan slechts één trigger worden gedefinieerd.

Merk op dat u kunt kiezen of de workflow meerdere keren per entiteit kan worden uitgevoerd. **Het wordt sterk aanbevolen** **om workflows slechts één keer per entiteit** uit te voeren, omdat het meer dan één keer uitvoeren van een workflow gemakkelijk kan leiden tot problemen met het herhaaldelijk aanmaken van taken of dubbele meldingen.

### Voorwaarden definiëren

U kunt een of meer uitvoeringsvoorwaarden per regel configureren.

### Acties definiëren

Om een nieuwe actie toe te voegen, klik je op de knop "**Een actie toevoegen**" en kies je het model dat je wilt instellen.

Hier zijn de **verschillende soorten acties** die u kunt activeren:&#x20;

* Een e-mailbericht verzenden
* Een veld in de betreffende entiteit bijwerken
* Een tag aan de entiteit toevoegen
* Automatische auditplanning
* De eigenaar van het item definiëren (bijvoorbeeld de toegewezen persoon)
* Automatisch een taak aanmaken

Condities kunnen aan elkaar worden gekoppeld. U kunt meerdere acties per conditie toevoegen door nogmaals op "een actie toevoegen" te klikken.

{% hint style="info" %}
Voorbeeld: stuur een notificatie naar verschillende mensen wanneer een taak wordt aangemaakt. Om dit te doen, selecteer je de "taken" trigger en voeg je, afhankelijk van de voorwaarden van de taak (bijvoorbeeld het toevoegen van een tag), een "notificatie" actie toe.
{% endhint %}



### Aangepaste variabelen

Heel vaak, bijvoorbeeld in aangepaste meldingen, zal het nuttig zijn om informatie te injecteren van het object dat in de workflow wordt ingevoerd: de naam van de behandeling, de publicatiedatum, enz. zijn allemaal variabelen die u gemakkelijk in de tekst van uw meldingen kunt injecteren met behulp van het injectiesysteem voor variabelen.

Intern gebruikt Dastra een templating-engine gebaseerd op [LiquidJS](https://shopify.github.io/liquid/basics/introduction/)

**Om toegang te krijgen tot de verschillende variabelen in het triggerobject, typ "\{{",** die een lijst met voorgestelde variabelen weergeeft die je in de inhoud kunt injecteren.





## Video tutorial: workflow regels

{% embed url="https://www.youtube-nocookie.com/embed/FqPmGdk2nTI" %}


