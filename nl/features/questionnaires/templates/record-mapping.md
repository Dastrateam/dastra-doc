---
description: >-
  Gebruik de antwoorden van een vragenlijst om een record aan te maken of een
  bestaand record bij te werken: ondersteunde objecten, variabelen, vraagtypen,
  de samenvoegknop en de foutmeldingen.
---

# Een record invullen met de antwoorden

Een vragenlijst van een aanmaaktype kan haar antwoorden omzetten in een record van Dastra: een verwerkingsactiviteit, een actief, een AI-systeem enzovoort. Is het antwoord aan een bestaand record gekoppeld, dan kunnen de antwoorden daar in plaats daarvan in worden samengevoegd. Elke vraag is via haar **naam van de variabele** aan een veld van het record gekoppeld.

Deze pagina is bedoeld voor de mensen die de sjablonen bouwen. Respondenten zien niets van de mapping.

Voor een volledig geval met een AI-systeem, zie [Vragenlijstantwoorden in een record](../../../examples/questionnaire-to-record.md).

## Welke objecten kunnen worden ingevuld

Alleen de aanmaaktypen van het veld **Type audit** dragen een gegevensmodel. De andere typen, zoals de DPIA, de beoordeling van een leverancier of de standaardvragenlijst, hebben er geen.

| Type vragenlijst | Record |
| --- | --- |
| Projectverzameling van verwerking | Verwerkingsactiviteit |
| Datalekken veroorzaken | Datalek |
| Activa maken | Actief |
| Contracten maken | Contract |
| Creatie van een AI-systeem | AI-systeem |
| Acteurscreatie | Stakeholder |

De ingebouwde sjablonen van deze typen zijn klaar voor gebruik (zie [Een vragenlijstsjabloon aanmaken](README.md)). U kunt ook uw eigen sjabloon bouwen en een van deze typen kiezen.

## Modelvalidatie en de lijst van variabelen

Het model van een type is de beschrijving van de velden van het record: hun naam, hun soort (tekst, datum, vaste lijst van waarden, lijst van items) en hun maximale lengte. De lijst van variabelen leest dit model.

Om een vraag in kaart te brengen:

1. Open het sjabloon en daarna de vraag.
2. Vink **Wilt u de naam van de variabele aanpassen (alleen voor gevorderde gebruikers)?** aan.
3. Typ bij **Naam variabele** de naam van het veld, of klik op **Selecteer een variabele om in kaart te brengen**.
4. Klik in de lijst op het veld. Het venster toont voor elk veld **Name**, **Variable's name**, **Possible values** en **Max**. Een markering **Vereist** wijst op de velden waar het record niet buiten kan.

Het kiezen van een veld vult de naam van de variabele en de maximale lengte in. Voor een veld met een vaste lijst van waarden, bijvoorbeeld het risiconiveau van een AI-systeem, maakt het ook de antwoorden van de vraag aan, één per waarde, en de naam van de variabele van elk antwoord is de waarde die Dastra verwacht. Laat deze namen van variabelen ongewijzigd.

Een naam van een variabele gebruikt letters, cijfers, koppeltekens en underscores en moet uniek zijn in het sjabloon.

{% hint style="info" %}
Een vraag waarvan de naam van de variabele met geen enkel veld van het record overeenkomt, wordt genegeerd wanneer het record wordt aangemaakt. Alleen het model van het type bepaalt welke namen geldig zijn: typ de namen precies zoals de lijst ze toont, met dezelfde hoofdletters.
{% endhint %}

<figure><img src="../../../.gitbook/assets/examples-questionnaire-1.png" alt="Venster Selecteer een variabele om in kaart te brengen met de velden van een AI-systeem"><figcaption><p>De variabelen die voor een AI-systeem worden aangeboden</p></figcaption></figure>

## Vraagtypen en velden

De lijst biedt alleen de velden aan die bij het type van de vraag passen.

| Type vraag | Aangeboden velden | Wat het record ontvangt |
| --- | --- | --- |
| Korte tekst, Lange tekst, Rich text (teksteditor) | Tekstvelden | De ingevoerde tekst |
| Datum, Datum en tijd | Datumvelden | De datum. Een ongeldige datum blijft leeg |
| Selectievakjeslijst (slechts één antwoord), Eenvoudige selector | Velden met een vaste lijst van waarden | De naam van de variabele van het gekozen antwoord, of het label ervan als het er geen heeft |
| Keuzelijst (meerdere antwoorden mogelijk), Multiple selector | Alle velden, behalve `id` | De lijst van de namen van de variabelen van de gekozen antwoorden |
| Lijst op maat | Lijstvelden | Eén item per rij. De namen van de variabelen van de subvragen zijn de eigenschappen van een item |
| Nummer, Regel, Eenvoudig aankruisvakje, Land, Tagselector | Alle velden, behalve `id` | De waarde zoals ingevoerd. Voor Tagselector de lijst van de labels |

U kiest zelf het veld voor de typen zonder filter: kies er een van dezelfde soort als het antwoord.

Het vraagtype **Bestanden** wordt niet aan een veld gekoppeld. Documenten die met de antwoorden worden verstuurd, kunnen naar het bestandsbeheer worden overgebracht wanneer het record wordt aangemaakt (zie hieronder).

## Native vragen

Een native vraag is een vraag van een ingebouwd aanmaaksjabloon die aan een veld van het record is gebonden. Het type, de naam van de variabele, de limieten en de antwoorden ervan zijn vergrendeld: alleen de beheerders van Dastra kunnen ze wijzigen, zodat de mapping correct blijft. Voeg uw eigen vragen naast de native vragen toe om andere velden in te vullen.

## Een aangepast veld invullen

Een aangepast veld wordt ingevuld door een naam van een variabele die bestaat uit `custom_` gevolgd door de technische naam van het veld.

1. Klik in de zijbalk op **Instellingen voor werkruimte**, daarna op **Aangepaste velden** en kies de module van het record.
2. Klik op het veld. De technische naam is de **Naam van de variabele (slug)**, bijvoorbeeld `business_owner`. Die is na het aanmaken alleen-lezen.
3. Stel in de vraag de naam van de variabele in op `custom_business_owner`.

Aangepaste velden staan niet in de lijst **Selecteer een variabele om in kaart te brengen**: typ de hele naam. Zie [Aangepaste velden](../../general/custom-fields.md) voor de opties van het veld.

Kies een vraagtype dat bij het type van het veld past:

| Type aangepast veld | Type vraag |
| --- | --- |
| Tekst, Tekstzone, Opgemaakte tekst | Korte tekst, Lange tekst, Rich text (teksteditor) |
| Aantal (geheel getal), Aantal (decimaal) | Nummer |
| Datum, Datum en tijd | Datum, Datum en tijd |
| Radio, Eenvoudige selector | Selectievakjeslijst (slechts één antwoord), Eenvoudige selector |
| Selectievakje, Meervoudige selector | Keuzelijst (meerdere antwoorden mogelijk), Multiple selector |
| Booleaans | Eenvoudig aankruisvakje |

Twee regels gelden wanneer het record wordt aangemaakt:

* een technische naam die met geen enkel aangepast veld van de werkruimte voor dit type record overeenkomt, wordt zonder fout weggelaten: het antwoord wordt niet opgeslagen. Controleer de spelling en het voorvoegsel `custom_`;
* een waarde die het veld niet accepteert, stopt het aanmaken met een melding die het veld noemt, bijvoorbeeld wanneer het veld verplicht is en het antwoord leeg is, of wanneer een lijst te weinig of te veel items heeft.

## Het record aanmaken of samenvoegen

De knop verschijnt in het antwoord van de vragenlijst wanneer:

* het antwoord is gepubliceerd, dat wil zeggen gevalideerd en niet gearchiveerd;
* het sjabloon van een aanmaaktype is.

Ze is alleen ingeschakeld voor de eigenaar van het antwoord.

* Zonder gekoppeld record heet de knop **Aanmaak verzoek**, gevolgd door het type record. Ze opent een voorbeeld van het record dat uit de antwoorden is opgebouwd. Kies de **Organisatie-eenheid** (niet gevraagd voor activa en stakeholders), behoud of wis de optie om de bestanden naar het bestandsbeheer over te brengen en klik op **Creëren**. Het record wordt aangemaakt en aan het antwoord gekoppeld.
* Met een gekoppeld record heet de knop **Gegevens samenvoegen**. Koppel het record wanneer u de vragenlijst plant, bij **Auditobject** (zie [Een audit of PIA plannen](../schedule.md#de-vragenlijst-koppelen-aan-andere-objecten-in-dastra)), nadat u **Gerelateerd aan** op het sjabloon op het type van het record hebt ingesteld. Het voorbeeld opent op dezelfde manier en de knop heet **Bestaande maken en samenvoegen**.

Met **Bestaande maken en samenvoegen** bouwt Dastra een tijdelijk record op uit de antwoorden, met het label gevolgd door "(From Questionnaire)", en opent het samenvoegvenster met het bestaande en het tijdelijke record. U kiest veld per veld de waarden die u behoudt. De bestanden worden overgebracht zodra u het samenvoegen bevestigt. Verlaat u het venster zonder samen te voegen, dan wordt het tijdelijke record verwijderd en verandert er niets.

Er wordt niets automatisch samengevoegd: de antwoorden werken nooit zelf een record bij. Het samenvoegen is altijd een actie van een persoon.

<figure><img src="../../../.gitbook/assets/examples-questionnaire-2.png" alt="Pagina van de samenvoegaanvraag met het voorbeeld van het AI-systeem en de knop Bestaande maken en samenvoegen"><figcaption><p>De samenvoegaanvraag van een antwoord</p></figcaption></figure>

## Foutmeldingen

| Melding of symptoom | Oorzaak | Oplossing |
| --- | --- | --- |
| This audit template type has no model validation configured | Het sjabloontype is niet een van de zes aanmaaktypen en heeft dus geen model. De melding verschijnt wanneer u op **Selecteer een variabele om in kaart te brengen** klikt | Wijzig het **Type audit** naar een aanmaaktype, of typ de namen van de variabelen met de hand als het sjabloon alleen antwoorden verzamelt |
| De lijst **Selecteer een variabele om in kaart te brengen** is leeg | Geen enkel veld van het record past bij het vraagtype, bijvoorbeeld een vraag van het type Datum op een record zonder datum | Wijzig het vraagtype, of kies een type zonder filter |
| You need at least a slug name | De naam van de variabele is leeg | Vul **Naam variabele** in |
| The variable name {slug} is present in another question | Twee vragen gebruiken dezelfde naam van een variabele | Geef elke vraag een eigen naam |
| De knop **Aanmaak verzoek** of **Gegevens samenvoegen** ontbreekt | Het antwoord is niet gepubliceerd, is gearchiveerd of het sjabloon is niet van een aanmaaktype | Valideer het antwoord, herstel het, of controleer het type |
| De knop is grijs | U bent niet de eigenaar van het antwoord | Vraag het aan de eigenaar |
| Een veld is leeg in het nieuwe record | De naam van de variabele komt niet met het veld overeen, of het aangepaste veld bestaat niet | Vergelijk ze met de lijst en met de technische naam |
| Het aanmaken stopt met een melding die een veld noemt | De waarde is niet geldig voor het veld | Corrigeer het antwoord en probeer opnieuw |
