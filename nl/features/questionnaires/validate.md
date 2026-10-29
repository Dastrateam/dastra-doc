---
description: >-
  Begrijp het validatieproces van vragenlijsten in Dastra: goedkeuringen door
  de goedkeurders, definitieve validatie, verzoeken om revisie en annulering.
---

# Een vragenlijst valideren

Validatie is de beoordelingsfase die volgt op het afronden van een vragenlijst door de respondenten. De aangewezen goedkeurders controleren elk antwoord, vragen waar nodig correcties en keuren de vragenlijst daarna goed en publiceren ze.

## Levenscyclus van een antwoord

1. **Wachten op antwoorden** en **Begonnen**: de respondenten vullen het formulier in.
2. **Wachten op validatie**: zodra alle verplichte respondenten op **Finaliseren** hebben geklikt, gaat het antwoord naar deze status en worden de goedkeurders op de hoogte gebracht.
3. **Geldig**: nadat alle vereiste goedkeurders hebben goedgekeurd en de definitieve validatie is uitgevoerd.

Vanuit de status **Wachten op validatie** zijn er drie mogelijke uitkomsten: valideren, een revisie vragen (het antwoord terugsturen naar de respondenten) of de vragenlijst annuleren.

{% hint style="info" %}
Zijn er geen knoppen beschikbaar, controleer dan of het antwoord echt de status **Wachten op validatie** heeft. In elke andere status zijn alle validatieacties geblokkeerd.
{% endhint %}

## Aanwijzing van de goedkeurders

De goedkeurders worden bepaald bij het plannen van de vragenlijst (zie [Een audit of PIA plannen](schedule.md)), in het onderdeel **Eigenaren**:

* **Vereiste goedkeurders**: ze moeten allemaal de vragenlijst goedkeuren voordat ze kan worden gevalideerd. Minstens één vereiste goedkeurder is verplicht.
* **Optionele goedkeurders**: schakel **Voeg optionele goedkeurders toe** in om goedkeurders te betrekken van wie de goedkeuring wordt bijgehouden maar niet blokkerend is.

Alleen deze gebruikers kunnen het antwoord goedkeuren, valideren, een revisie vragen of annuleren.

{% hint style="success" %}
U kunt deze fase volledig uitschakelen bij het plannen van de vragenlijst, met de optie **Geen validatiestap**. Het antwoord wordt dan rechtstreeks gepubliceerd zodra de respondenten het hebben afgerond.
{% endhint %}

## Het beoordelingsscherm

Klik in het antwoord op **Controleer en valideer de audit**. Het beoordelingsscherm volgt de structuur van de vragenlijst: links de navigatie tussen secties, in het midden de vragen en antwoorden, rechts de validatieacties.

### Elk antwoord kwalificeren

Aan elke vraag kunt u een beoordelingsstatus geven:

* **Geen status**: de vraag is niet gekwalificeerd (standaard, niet blokkerend)
* **Gevalideerd**: het antwoord is aanvaard
* **Behoefte aan herziening**: het antwoord moet worden aangevuld of gecorrigeerd
* **Niet gevalideerd**: het antwoord is geweigerd

Met een selector boven aan elke sectie past u dezelfde status in één keer toe op alle weergegeven vragen.

Bij elke vraag kunt u ook:

* een annotatie toevoegen: een interne discussie met respondenten en andere goedkeurders
* een taak toevoegen met **Voeg een taak toe**: de taak komt rechtstreeks in het actieplan
* de verantwoording van het antwoord aanvullen en een bestand bijvoegen met **Voeg een justificatie toe**
* een risico kwalificeren met **Bepaal risico** wanneer de vraag aan een risico is gekoppeld

{% hint style="warning" %}
Is minstens één vraag gemarkeerd als **Behoefte aan herziening** of **Niet gevalideerd**, dan zijn goedkeuring en validatie geblokkeerd: gebruik **Vraag revisie aan** om de vragenlijst terug te sturen naar de respondenten.
{% endhint %}

## De vragenlijst goedkeuren

Elke goedkeurder geeft afzonderlijk goedkeuring, met de knop **Het vragenformulier goedkeuren**:

* U kunt opmerkingen voor de beoordeling schrijven: ze worden bewaard en opgenomen in de export van het rapport.
* Er wordt een e-mailnotificatie gestuurd naar de goedkeurders die nog niet hebben goedgekeurd.

Het paneel **Vereiste goedkeuringen (n/totaal)** geeft de stand van elke goedkeurder weer (**Goedgekeurd**, met de datum, of **In afwachting van goedkeuring**), plus waar relevant een apart blok **Optionele goedkeuringen**. De opmerkingen van elke goedkeurder kunt u er raadplegen.

Twee extra acties:

* **Herroep mijn goedkeuring**: trekt uw goedkeuring in zolang de vragenlijst niet is gevalideerd.
* Bent u de laatste vereiste goedkeurder die goedkeurt, dan biedt Dastra meteen aan om door te gaan naar validatie en publicatie.

## Valideren en publiceren

De knop **Valideer de vragenlijst** wordt pas actief wanneer alle vereiste goedkeurders hebben goedgekeurd en geen enkele vraag is gemarkeerd voor correctie. Het validatievenster toont:

* het aantal gevalideerde vragen op het totaal;
* de stand van de goedkeuringen;
* voor een PIA of DPIA die aan een verwerkingsactiviteit is gekoppeld, het bericht "De datum van de laatste PIA van de bijbehorende verwerking zal worden bijgewerkt.": het veld **Datum laatste DPIA** van de verwerkingsactiviteit wordt bij de validatie automatisch bijgewerkt;
* de optie om een melding naar de stakeholders te sturen.

Het antwoord krijgt dan de status **Geldig** met de publicatiedatum en u wordt doorgestuurd naar het rapport. Daarna kunt u [het rapport exporteren](export.md), een actieplan genereren of de antwoorden samenvoegen met het gekoppelde object (zie [Vragenlijsten opvolgen](monitor.md)).

Na de validatie ontvangt elke respondent, intern of extern, een e-mail met de vragenlijst, de werkruimte en de validatiedatum, met een link naar het eindscherm. Op dat scherm downloadt de respondent met de actie **Export to PDF** de eigen vragen en antwoorden, zonder Dastra-account. De export is pas beschikbaar zodra de vragenlijst is gevalideerd, en elke respondent kan alleen de beantwoorde vragenlijst exporteren. Wilt u valideren zonder te informeren, schakel dan de notificatieoptie in het validatievenster uit.

## Een revisie vragen

De actie **Vraag revisie aan** stuurt de vragenlijst terug naar de respondenten:

* het antwoord keert terug naar **Aan de gang** en er wordt een nieuwe deadline berekend op basis van de termijn van het sjabloon (standaard 30 dagen);
* elke reeds gegeven goedkeuring wordt gereset;
* een correctieronde wordt vastgelegd in de geschiedenis van het antwoord;
* elke respondent krijgt een melding, samen met uw bericht voor de beoordeling. U kunt dat bericht vrij schrijven of vooraf invullen met een e-mailsjabloon.

Wanneer de respondenten opnieuw afronden, begint de validatiecyclus opnieuw.

## De vragenlijst annuleren

De actie **Annuleer de vragenlijst** beëindigt de cyclus zonder publicatie. Met een optionele opmerking kunt u de reden toelichten: ze wordt bewaard in de geschiedenis en is zichtbaar voor de respondenten. De goedkeuringen worden gereset en het antwoord krijgt de status **Geannuleerd**: het kan niet meer worden bewerkt en wordt niet opgenomen in de resultaten.

## Vragenlijsten opvolgen die op validatie wachten

Vragenlijsten die op uw goedkeuring wachten, staan gegroepeerd onder **Wachten op mijn validatie** in uw vragenlijsten en zijn gemarkeerd met de badge **Wachten op validatie** in de lijsten en de rapportageweergaven.
