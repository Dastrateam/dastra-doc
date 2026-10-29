---
description: Beheer uw conformiteit met de verschillende kaders in Dastra.
---

# Conformiteit

De module **Conformiteit** van Dastra beheert de naleving van regelgeving op een gestructureerde, traceerbare en controleerbare manier, met een modulaire opbouw op basis van conformiteitskaders.

***

## Architectuur van de module Conformiteit

De module berust op een logische keten van objecten, van regelgevende kaders tot bewijs van conformiteit.

<figure><img src="../../.gitbook/assets/mermaid-diagram-2026-01-28-160744.png" alt="Schema van de keten van objecten in de module Conformiteit: kaders, vereisten, controles, risicoscenario's, tests, testcampagnes, bewijs en audits"><figcaption><p>De keten van objecten in de module Conformiteit</p></figcaption></figure>

### Kaders

Voorbeelden: AVG, ISO 27701, ISO 27001, AI-verordening.

Een kader:

* definieert het regelgevende of normatieve referentiekader,
* bevat een reeks toepasselijke vereisten.

***

### Vereisten

Vereisten zijn de verplichtingen die uit een kader voortvloeien.\
Voorbeelden: toegangsbeheer, beheer van autorisaties, logging.

Elke vereiste:

* is gekoppeld aan een kader,
* wordt beoordeeld tijdens conformiteitsaudits,
* wordt uitgevoerd met een of meer controles.

***

### Controles

Controles beschrijven hoe een vereiste concreet wordt toegepast.\
Voorbeelden: periodieke toegangsreview, autorisatieprocedure.

Een controle:

* geeft invulling aan een vereiste,
* is gekoppeld aan een of meer risicoscenario's,
* wordt geverifieerd met tests.

***

### Risicoscenario's

Risicoscenario's beschrijven de gevreesde gebeurtenissen.\
Voorbeeld: onbevoegde toegang tot gevoelige gegevens.

Met controles kunt u:

* deze risico's voorkomen of beperken,
* de genomen herstelmaatregelen aantonen.

***

### Tests

Met tests verifieert u de doeltreffendheid van controles.\
Voorbeelden: terugkerende toegangsreview, validatie van delegatie.

Een test:

* controleert een of meer controles,
* levert meetbare resultaten op,
* wordt onderbouwd met bewijs.

***

### Testcampagnes

Met campagnes organiseert u tests op grote schaal:

* campagnes versturen naar teams of klanten,
* antwoorden centraal verzamelen,
* de voortgang en de statussen opvolgen.

***

### Bewijs

Bewijs toont conformiteit aan.\
Voorbeelden: beleid, procedures, rapporten van toegangsreviews.

Een stuk bewijs:

* is gekoppeld aan een test,
* wordt gebruikt tijdens audits,
* waarborgt de traceerbaarheid van controles.

***

### Conformiteitsaudits

Met audits beoordeelt u het niveau van conformiteit:

* interne audits,
* zelfbeoordelingen,
* voorbereiding op externe audits.

Ze berusten op:

* vereisten,
* controles,
* de bijbehorende tests en het bewijs.

***

## Overzicht

Met de module Conformiteit van Dastra:

* structureert u regelgevende vereisten,
* koppelt u verplichtingen aan risico's,
* toont u conformiteit aan met geteste en gedocumenteerde controles,
* bereidt u audits en certificeringen doeltreffend voor.

## Het multikaderprincipe in Dastra

De module Conformiteit van Dastra is van nature multikader.

Dat betekent dat:

* een kader (AVG, ISO, AI-verordening enzovoort) zijn eigen vereisten bevat,
* een vereiste tot één kader behoort,
* een controle meerdere vereisten kan dekken, ook vereisten uit verschillende kaders,
* tests en bewijs worden gedeeld en hergebruikt.

Het doel is dubbel werk te vermijden en conformiteit transversaal te sturen.

***

## Belangrijkste verbanden tussen objecten

* Kader → vereisten: 1 → N
* Vereisten ↔ controles: N ↔ N
* Controles ↔ tests: N ↔ N
* Tests → bewijs: 1 → N
* Controles → risicoscenario's: N ↔ N

Eén controle (bijvoorbeeld een toegangsreview) kan dus:

* voldoen aan een vereiste van de AVG,
* voldoen aan een vereiste van ISO 27001,
* meerdere risicoscenario's beperken.
