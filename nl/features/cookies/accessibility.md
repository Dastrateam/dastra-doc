---
description: >-
  De resultaten van de RGAA-toegankelijkheidsaudit van de cookiebanner en de
  punten die nog moeten worden aangepast.
---

# RGAA-naleving

Deze pagina toont de resultaten van de laatste toegankelijkheidsaudit van de cookiebanner, uitgevoerd op basis van het Franse algemene kader voor toegankelijkheidsverbetering (RGAA).

## Audit van 16 oktober 2025

* Kader: RGAA 4.1.1.
* Type audit: interne audit (eerste bezoek) van de banner zoals die op www.dastra.eu wordt weergegeven.
* Resultaat: 47 criteria conform, 5 niet conform en 54 niet van toepassing.

{% hint style="info" %}
Het auditraster berekent geen algemeen conformiteitspercentage. Deze audit is geen verklaring dat de banner volledig conform is.
{% endhint %}

## Niet-conforme punten

| Criterium | Bevinding | Opvolging |
| --- | --- | --- |
| 3.2 Tekstcontrast | De lopende tekst, grijs op een witte achtergrond, heeft een contrast van 3,98:1 terwijl 4,5:1 vereist is. De link "Notre politique de cookies", oranje op wit, valt hier ook onder. | Hangt af van de kleuren die in de bannerinstellingen zijn gekozen. Zie hieronder. |
| 3.3 Kleuren van interfacecomponenten | Vetgedrukte woorden hebben dezelfde kleur als de lopende tekst. | Het raster vermeldt "corrigé" (verholpen). De SDK van versie 3.0.0 toont vetgedrukte woorden in een donkerdere tint dan de lopende tekst. |
| 7.1 en 7.2 Weergave zonder JavaScript | De banner verschijnt niet zonder JavaScript. | De auditor merkt op dat zonder JavaScript geen cookie wordt geplaatst: er is dan geen toestemming om te verzamelen. |
| 12.6 Navigatiebakens | De link naar het cookiebeleid staat niet in een navigatieblok. | Het raster vermeldt "corrigé" (verholpen). De SDK van versie 3.0.0 plaatst deze link in een `<nav>`-element, op het welkomstscherm en op het voorkeurenscherm. |

De audit raadt ook aan de banner als eerste in de tabvolgorde te plaatsen (criterium 10.7, conform).

### Contrast: uw instellingen bepalen het resultaat

De kleuren van de bannertekst en de links komen uit de instellingen van elke banner: **Kleur hoofdtekst** en **Primaire kleur** in de sectie **Uiterlijk van de widget**. Het contrast is dus uw keuze: Dastra kan het niet voor elke banner garanderen. Controleer of tekst en links een contrast van ten minste 4,5:1 met de achtergrond hebben. Zie [De cookietoestemmingsbanner instellen](banner/configure.md).

## Rapport van 2021

De vorige audit dateert van 16 maart 2021. Ze betreft het RGAA 4.1-raster, is in het Frans geschreven en dateert van vóór verschillende wijzigingen aan de banner (Global Privacy Control, de knop "Doorgaan zonder te accepteren", vormen van de zwevende knop). Ze blijft beschikbaar als historische referentie.

{% file src="../../.gitbook/assets/audit-rgaa.zip" %}
Het RGAA-auditrapport van 2021 downloaden
{% endfile %}
