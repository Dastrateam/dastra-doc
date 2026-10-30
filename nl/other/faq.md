---
description: >-
  De FAQ van elke Dastra-module op één plek, en antwoorden op algemene vragen:
  logo's, een bestaand register importeren, een verwerkingsactiviteit
  verwijderen, items die niet te vinden zijn en de lokale opslag van de browser.
---

# FAQ

Deze pagina is het toegangspunt tot de vragen die in de documentatie worden beantwoord. Ze bundelt de FAQ van elke module en beantwoordt daarna de algemene vragen die op de lijst volgen.

## FAQ van de modules

* [FAQ Aan de slag](../getting-started/setup/faq.md): teams en organisatorische eenheden als stakeholders, organisatorische eenheden exporteren en importeren, de FG wijzigen en de eigenaars van de organisatie beheren.
* [FAQ Algemene functies](../features/general/faq.md): datasets importeren.
* [FAQ AI-assistent](../features/general/ai-assistant/faq.md): privacy en gegevens, kwaliteit en betrouwbaarheid, configuratie en toegang en de AI-verordening.
* [FAQ Verwerkingsregister](../features/ropa/faq.md): wijzigingsgeschiedenis, verwijdering, datasets in alleen-lezenmodus, bulkwijzigingen van stakeholders, dupliceren naar een andere werkruimte, wijziging van type en foutmeldingen.
* [FAQ Vragenlijsten](../features/questionnaires/faq.md): DPIA op meerdere verwerkingsactiviteiten, e-mailsjablonen, externe respondenten, voorgestelde taken, sjablonen publiceren, foutmeldingen en limieten.
* [FAQ Risico's](../features/risks/faq.md): het ontbrekende menu, een risico naar de volgende stap verplaatsen, initieel, rest- en huidig risico en de risicoschaal wijzigen.
* [FAQ Taken](../features/tasks/faq.md): taken aan een project koppelen, een taak verwijderen, de werklast registreren en opvolgen.
* [FAQ Verzoeken](../features/requests/faq.md): sluitingsmails, de beveiligde ruimte van de aanvrager en de verificatie van het e-mailadres, de lengte van berichten en cookies op de verzamelpagina.
* [FAQ Zapier](../features/integrations/zapier/faq.md): contractuele status van Zapier, wie het contract ondertekent en documentatie over betrouwbaarheid.

Voor problemen in plaats van vragen, zie [Bekende problemen](known-problems.md) en de [bekende problemen van SSO](../features/settings/sso/known-problems.md).


## Hoe wijzigt u het logo van de organisatie in Dastra?

De organisatie heeft geen logo. De afbeelding rechtsboven in het scherm, naast uw naam en de naam van de organisatie, is de afbeelding van uw gebruikersaccount. Om die te wijzigen, opent u rechtsboven uw profielmenu, klikt u op **Gebruikersprofiel** en uploadt u een nieuwe afbeelding.

Zie de volgende vraag om het logo aan te passen dat in exports wordt gebruikt.

## Hoe wijzigt u het logo van de werkruimte in Dastra?

Open de instellingen van de werkruimte en daarna de sectie **Design & merk**. U kunt een vierkant logo en een rechthoekig logo uploaden en de **Merk kleur** en de **Secundaire kleur** kiezen. Met deze elementen past u de exports van Dastra aan uw merk aan.

Deze sectie is voorbehouden aan de eigenaars van de organisatie.

## Hoe importeert u uw verwerkingsregister in het CNIL-formaat?

U kunt een bestaand verwerkingsregister in het CNIL-formaat in Dastra importeren. De import verloopt in meerdere stappen:

1. Importeer de namen van de verwerkingsactiviteiten.
2. Importeer de datasets.
3. Importeer de stakeholders.
4. Importeer de beveiligingsmaatregelen.
5. Maak in de verwerkingsactiviteiten de koppelingen tussen deze objecten.

Voor het importeren van verwerkingsactiviteiten, zie [Het register exporteren en importeren](../features/ropa/export-import.md). Voor hulp bij het importeren van uw register [neemt u contact op met support](../getting-started/support/request.md).

## Hoe verwijdert u een verwerkingsactiviteit?

Verwijderen verloopt in twee stappen, om verwijderingen per ongeluk te voorkomen. Verplaats de verwerkingsactiviteit eerst naar de prullenbak met **Verplaats naar de prullenbak**. Geef daarna de prullenbak weer met **Bekijk prullenbak** in de filters en kies **Verwijderen** om ze definitief te verwijderen, of **Herstellen** om ze terug te zetten in het register.

De volledige werkwijze staat in de [FAQ van het register](../features/ropa/faq.md#hoe-verwijdert-u-een-verwerkingsactiviteit).

## Ik kan sommige items niet vinden, wat kan ik doen?

Als u een item niet vindt waartoe u toegang zou moeten hebben, kan het om een van de volgende redenen verborgen zijn:

1. Een filter is actief en beperkt de weergave. Het aantal actieve filters staat tussen haakjes op de knop, bijvoorbeeld "(1)". Klik op **Filters wissen**.

   <figure><img src="../.gitbook/assets/other-faq-1.png" alt="Lijst van het register met een actief filter en de knop Filters wissen (1)"><figcaption><p>Een actief filter beperkt de lijst</p></figcaption></figure>
2. Het item is gekoppeld aan een organisatorische eenheid waartoe u geen toegang hebt of waarvoor u niet over de nodige rechten beschikt. Neem contact op met uw werkruimtebeheerder.
3. Het item staat in de prullenbak en verschijnt daarom niet meer in de standaardlijst. Klik op **Filters** en vink **Bekijk prullenbak** aan.

   <figure><img src="../.gitbook/assets/ropa-faq-3.png" alt="Filterpaneel van het register met de optie Bekijk prullenbak"><figcaption><p>De prullenbak weergeven</p></figcaption></figure>
4. In uw browser zijn onjuiste instellingen opgeslagen. Open Dastra in een privévenster om dit te controleren. Verdwijnt het probleem, wis dan de lokale opslag van uw browser met de werkwijze in de volgende vraag.

## Hoe wist u de lokale opslag van de browser?

De lokale opslag (localStorage) bevat gegevens die de browser bewaart zodat Dastra werkt en uw instellingen onthoudt, zoals uw filters. Hebt u een weergaveprobleem, dan kan support u vragen om die te wissen.

U kunt ook de knop **Voorkeursgegevens opnieuw instellen** in uw gebruikersprofiel gebruiken, die wordt beschreven in [Bekende problemen](known-problems.md).

### Google Chrome

1. Open het browsermenu en kies **More tools** > **Developer tools** (F12).
2. Open het tabblad **Application** en kies daarna **Storage** > **Local storage**.
3. Klik met de rechtermuisknop op het adres van Dastra en kies **Clear**.
4. Vernieuw de pagina (F5).

### Mozilla Firefox

1. Open het browsermenu en kies **More tools** > **Web Developer** > **Developer Tools** (F12).
2. Open het tabblad **Storage** en kies daarna **Local Storage**.
3. Klik met de rechtermuisknop op het adres van Dastra en kies **Delete All**.
4. Vernieuw de pagina (F5).
