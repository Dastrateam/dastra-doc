# Veelgestelde vragen

## Waarom verschijnt het menu Risicobeheer niet?

De module moet voor uw werkruimte zijn geactiveerd en uw rol moet leestoegang tot risico's bevatten. Voor het aanmaken of bewerken van een risico is schrijftoegang nodig. Neem contact op met de beheerder van uw werkruimte.

## Waarom kan ik een risico niet naar de volgende stap brengen?

Alleen de eigenaar van een risico kan de status ervan wijzigen: de beoordeling valideren, de respons valideren, het risico archiveren of terugkeren naar een eerdere stap. De naam van de eigenaar staat in de sectie **Identificatie** van het risico. Om het risico aan iemand anders over te dragen, wijzigt u de **Risico-eigenaar** in die sectie.

## Wat is het verschil tussen initieel, rest- en huidig risico?

Het initiële risico is het risico vóór enige beheersmaatregel. Het restrisico is het risico dat u nastreeft zodra de maatregelen zijn ingevoerd. Het huidige risico ligt daartussen, afhankelijk van het remediëringspercentage van uw controlepunten. De formules staan in de [woordenlijst](glossary.md).

## Waarom verandert mijn huidige risico niet ondanks mijn controlepunten?

Controleer het volgende:

* het responstype is **Reductie en beheersing**: de andere opties berekenen geen remediëringspercentage;
* het risico heeft een initieel niveau en een restniveau;
* er zijn controlepunten aan het risicotype toegewezen en ze hebben een respons gekregen. Een controlepunt zonder respons telt voor nul punten;
* de responsen zijn niet allemaal **Niet van toepassing**: die responsen worden van de berekening uitgesloten.

## Wat gebeurt er als ik de risicoschaal wijzig?

Als u een andere schaal activeert, veranderen de statistieken van alle risico's in de werkruimte. Dastra vraagt om een bevestiging voordat het dat doet. Kies uw schaal voordat u uw eerste risico's invoert. Zie [De risicoschaal configureren](process/assess.md#de-risicoschaal-configureren).

## Hoe beoordeel ik hetzelfde risico op meerdere verwerkingsactiviteiten of activa?

Gebruik **Creatie van risico's in bulk**: selecteer het risicotype en alle betrokken objecten, en Dastra maakt één risico per object aan. Zie [Risicobeheer](README.md).
