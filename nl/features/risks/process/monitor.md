---
description: >-
  Leer hoe u risico's opvolgt in Dastra.
---

# 4. Opvolgen

Zodra het risico is aangepakt, moet u ervoor zorgen dat het in de tijd wordt gevolgd en dat elke verandering wordt opgemerkt. Op de risicopagina toont de monitoringstap het label **Monitoring** wanneer het type respons **Reductie en beheersing** is; bij een andere optie draagt de stap de naam van die optie.

## De controlepunten opvolgen

Met de optie **Reductie en beheersing** toont het onderdeel twee indicatoren: de **Veerkracht** als percentage en de **Scoren** in punten op het maximum. De controlepunten zijn gegroepeerd naar invloed: die welke de ernst verminderen en die welke de waarschijnlijkheid verminderen, elk met hun percentage.

<figure><img src="../../../.gitbook/assets/risks-monitor-1.png" alt="Monitoringstap van een risico: voltooiing, score en controlepunten gegroepeerd per ernst en waarschijnlijkheid"><figcaption><p>De controlepunten van een risico en de remediëring ervan</p></figcaption></figure>

1. Klik op **Controlepunten toewijzen** om de controlepunten van het risicotype te kiezen.
2. Klik op het betrokken controlepunt op **Nieuw audit**.
3. Kies het antwoord, vul de **Datum van implementatie** in en voeg indien nodig een beschrijving en bestanden toe in **Bewijs van implementatie bestanden**.
4. Klik op **Verstuur het antwoord**.

Elke respons wordt bewaard: de knop **Historisch** van het controlepunt toont ze allemaal, en de meest recente is de huidige respons. Als het controlepunt op terugkerende basis wordt geëvalueerd, waarschuwt Dastra u wanneer het gekozen aantal dagen is verstreken.

## Effect op het huidige risico

Na elke nieuwe respons berekent Dastra opnieuw het remediëringspercentage en daarna het huidige risico: {Huidig risico} = {Initieel risico} - ({Initieel risico} - {Restrisico}) \* {Remediëringspercentage}. Hoe dichter de remediëring bij 100% komt, hoe dichter het huidige risico bij het restrisico komt. De berekening wordt toegelicht in de [woordenlijst](../glossary.md).

## Veranderingen in de tijd volgen

De eerste pagina van de module, onder het menu **Rapportage**, en het dashboard van de werkruimte volgen hoe de risico's evolueren: gemiddeld initieel, huidig en resterend risico, gemiddelde remediëring en aantal risico's per stap. De heat map toont het initiële, het resterende of het huidige risico. De laatste pagina van het menu, **Rapportage**, geeft per object de minimale, gemiddelde en maximale scores.

<figure><img src="../../../.gitbook/assets/risks-monitor-2.png" alt="Risico-overzicht met de indicatoren en de heat map van het huidige risico"><figcaption><p>Het risicodashboard volgt de veranderingen in de tijd</p></figcaption></figure>

## Een risico archiveren

Wanneer een risico is verdwenen, klikt u op **Het risico wegnemen**. Het risico gaat naar de stap **Terugtrekking**: u kunt het nog lezen, maar niet meer wijzigen. Om het opnieuw onder monitoring te plaatsen, klikt u op **Annuleren** in het onderdeel Terugtrekking. Alleen de eigenaar van het risico kan een risico archiveren of de archivering annuleren.
