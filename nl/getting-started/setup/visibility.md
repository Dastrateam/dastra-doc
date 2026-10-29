---
description: >-
  Ziet een gebruiker een verwerkingsactiviteit of een tabblad niet, of krijgt
  die een 403-fout? Begrijp hoe rollen, teams en organisatorische eenheden
  bepalen wat iemand ziet.
---

# Waarom ziet een gebruiker een verwerkingsactiviteit niet?

Twee gebruikers met dezelfde rol zien niet noodzakelijk dezelfde items. In Dastra hangt toegang af van twee niveaus die samen gelden:

1. Hun rollen: die bepalen wat de gebruiker in elke module kan doen (lezen, schrijven, aanmaken, exporteren...) en in welke werkruimten.
2. De organisatorische eenheden waartoe ze toegang hebben: die bepalen op welk bereik (entiteit, afdeling) de gebruiker items kan bekijken en bewerken.

Ontbreekt een van beide, dan verschijnt het item niet of wordt een toegangsfout (403, "Resource inaccessible") weergegeven.

## 1. Rollen controleren

* Eigenaars van de organisatie hebben toegang tot alle actieve werkruimten, alle organisatorische eenheden en alle machtigingen.
* Andere gebruikers hebben alleen de machtigingen van de rollen die aan hen zijn toegewezen, werkruimte per werkruimte. Een rol kan aan een specifieke werkruimte of aan alle werkruimten worden toegewezen.
* Een rol waarbij geen enkele machtiging is aangevinkt, geeft nergens toegang toe.
* Een gebruiker kan meerdere rollen hebben.

Controleer bij **Instellingen voor werkruimte** > **Gebruikers** (van de betreffende werkruimte) welke rollen zijn toegewezen en controleer daarna bij **Instelling van de organisatie** > **Rollen en machtigingen** of de module minstens de machtiging **Lezing** heeft. Zie [Rollen en machtigingen](../../features/settings/roles.md).

{% hint style="info" %}
De machtiging **Read/Edit your own items** geeft alleen toegang tot items die aan de gebruiker zijn toegewezen, niet tot alle items van de module.
{% endhint %}

## 2. Toegang tot de organisatorische eenheid controleren

Elke verwerkingsactiviteit is gekoppeld aan een organisatorische eenheid. Heeft de gebruiker geen toegang tot die eenheid, dan ziet die de verwerkingsactiviteiten ervan niet, ook niet met de juiste rol.

De regels zijn:

* Standaard is een organisatorische eenheid toegankelijk voor iedereen in de werkruimte: in de machtigingen ervan verschijnt het bericht "Iedereen mag de het element weergeven of wijzigen".
* Zodra u machtigingen instelt op een eenheid (toegestane gebruikers of teams), hebben alleen de vermelde gebruikers en de leden van vermelde teams er toegang toe.
* Onderliggende eenheden erven de machtigingen van hun bovenliggende eenheid (weergegeven als "Geërfd") zolang ze er zelf geen hebben. Stelt een onderliggende eenheid eigen machtigingen in, dan vervangen die die van de bovenliggende eenheid.

Om deze regels te bekijken of te wijzigen, opent u **Instellingen voor werkruimte** > **Organisatorische eenheden** en kiest u in het menu van de betreffende eenheid **Machtigingen instellen voor**. Deze actie is beperkt tot gebruikers met het recht voor geavanceerd beheer.

{% hint style="warning" %}
Een vaak voorkomende oorzaak: er is een team toegevoegd aan een bovenliggende eenheid en de gebruiker behoort niet tot dat team. Die verliest dan de toegang tot alle onderliggende eenheden die geen eigen machtigingen hebben. Controleer tot welke [teams](teams.md) de gebruiker behoort.
{% endhint %}

## Controlelijst

| Symptoom | Wat u controleert |
|---|---|
| Geen verwerkingsactiviteit zichtbaar, of een tabblad ontbreekt | Is in deze werkruimte een rol met de machtiging **Lezing** van de module toegewezen? |
| Slechts enkele verwerkingsactiviteiten zijn zichtbaar | Toegang tot de organisatorische eenheid, overerving van de bovenliggende eenheid, lidmaatschap van teams |
| Een collega met dezelfde rol ziet meer items | Die behoort waarschijnlijk tot een team dat op de eenheid is toegestaan, en u niet |
| De knop Opslaan is grijs | Ontbrekende machtiging **Schrijven** (of **Create** voor een nieuw item) |
| Fout 403 "Resource inaccessible" | Toegang tot de organisatorische eenheid van het item, of geen rol in deze werkruimte |

Is alles correct en blijft het item onzichtbaar, neem dan contact op met de ondersteuning van Dastra, met vermelding van de werkruimte, de gebruiker en het betreffende item.
