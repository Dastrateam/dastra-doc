---
description: >-
  Een gebruiker ziet een verwerking of tabblad niet, of krijgt een 403-fout?
  Begrijp hoe rollen, teams en organisatorische eenheden bepalen wat hij of zij
  kan zien.
---

# Waarom ziet een gebruiker een verwerking niet?

Twee gebruikers met dezelfde rol zien niet noodzakelijk dezelfde items. In Dastra hangt de toegang af van **twee niveaus** die samen gelden:

1. **Hun rollen**: ze bepalen wat de gebruiker in elke module kan doen (lezen, schrijven, aanmaken, exporteren…) en in welke werkruimten.
2. **De organisatorische eenheden waartoe ze toegang hebben**: ze bepalen op welk bereik (entiteit, afdeling) de gebruiker items kan zien en bewerken.

Ontbreekt een van beide, dan verschijnt het item niet of wordt een toegangsfout (403, "Bron niet toegankelijk") getoond.

## 1. Rollen controleren

* **Eigenaars** van de organisatie hebben toegang tot alle actieve werkruimten, alle organisatorische eenheden en alle machtigingen.
* Andere gebruikers hebben alleen de machtigingen van de **rollen die aan hen zijn toegewezen**, werkruimte per werkruimte. Een rol kan aan een specifieke werkruimte of aan alle werkruimten worden toegewezen.
* Een rol zonder aangevinkte machtiging geeft geen enkele toegang.
* Een gebruiker kan meerdere rollen combineren.

Controleer onder **Instellingen > Gebruikers** (van de betreffende werkruimte) welke rollen zijn toegewezen, en onder **Configuratie > Rollen en machtigingen** of de gewenste module minstens de machtiging **Lezen** heeft. Zie [Rollen en machtigingen](../../features/settings/roles-et-permissions.md).

{% hint style="info" %}
De machtiging **Eigen items lezen/bewerken** geeft alleen toegang tot items die aan de gebruiker zijn toegewezen, niet tot alle items van de module.
{% endhint %}

## 2. Toegang tot de organisatorische eenheid controleren

Elke verwerking is gekoppeld aan een organisatorische eenheid. Heeft de gebruiker geen toegang tot die eenheid, dan ziet hij of zij de verwerkingen ervan niet, zelfs niet met de juiste rol.

De toegangsregels zijn:

* Standaard is een organisatorische eenheid **toegankelijk voor iedereen** in de werkruimte: in de machtigingen verschijnt de melding "Iedereen mag het item bekijken of bewerken".
* Zodra u **machtigingen instelt** voor een eenheid (toegestane gebruikers of teams), hebben alleen de vermelde gebruikers en de leden van de vermelde teams toegang.
* **Onderliggende** eenheden **erven** de machtigingen van de bovenliggende eenheid (aangeduid als "Geërfd"), zolang ze er geen eigen hebben. Stelt een onderliggende eenheid eigen machtigingen in, dan vervangen die die van de bovenliggende eenheid.

Om deze regels te bekijken of te wijzigen, opent u **Instellingen > Organisatorische eenheden** en kiest u in het menu van de betreffende eenheid **Machtigingen instellen voor…**. Deze actie is voorbehouden aan gebruikers met het recht voor geavanceerd beheer.

{% hint style="warning" %}
Veelvoorkomende oorzaak: een team is toegevoegd aan een bovenliggende eenheid en de gebruiker behoort niet tot dat team. Hij of zij verliest dan de toegang tot alle onderliggende eenheden die geen eigen machtigingen hebben. Controleer tot welke [teams](creer-puis-affectez-des-equipes.md) hij of zij behoort.
{% endhint %}

## Korte checklist

| Symptoom | Te controleren |
|---|---|
| Geen verwerking zichtbaar of een tabblad ontbreekt | Is in deze werkruimte een rol met de machtiging **Lezen** voor de module toegewezen? |
| Slechts enkele verwerkingen zijn zichtbaar | Toegang tot organisatorische eenheden, overerving van de bovenliggende eenheid, teamlidmaatschap |
| Een collega met dezelfde rol ziet meer items | Hij of zij behoort waarschijnlijk tot een team dat op de eenheid is toegestaan, u niet |
| De opslaan-knop is grijs | Ontbrekende machtiging **Schrijven** (of **Aanmaken** voor een nieuw item) |
| 403-fout "Bron niet toegankelijk" | Toegang tot de organisatorische eenheid van het item, of geen rol in deze werkruimte |

Als alles klopt en het item onzichtbaar blijft, neem dan contact op met de Dastra-support en vermeld de werkruimte, de gebruiker en het betreffende item.
