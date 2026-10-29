# Vragenlijsten opvolgen

## Dashboard met antwoorden

Selecteer op het tabblad **Alle audits** een sjabloon om het dashboard met antwoorden te openen. Dat dashboard biedt vier weergaven:

* **Reacties**: lijst van alle antwoorden met hun status (in afwachting van validatie, gevalideerd, niet gevalideerd, geannuleerd, deadline overschreden), hun score en het gekoppelde object
* **Gedetailleerd bord**: vergelijking naast elkaar van alle antwoorden per categorie en score, nuttig voor benchmarking tussen entiteiten of verwerkingsactiviteiten
* **Statistieken**: geaggregeerde statistieken over alle antwoorden voor dat sjabloon
* **Details**: configuratie en metagegevens van de vragenlijst

<figure><img src="../../.gitbook/assets/questionnaire-state-badges.png" alt="Statusbadges van de antwoorden op een vragenlijst"><figcaption><p>De statussen van de antwoorden, waaronder Geannuleerd (rode badge)</p></figcaption></figure>

## Rapportage per antwoord

Een antwoord openen geeft toegang tot een gedetailleerde rapportageweergave:

* **Status**: verloop van **Wachten op antwoorden** naar **Begonnen**, **Wachten op validatie** en **Geldig**
* **Score**: totale score op het maximale aantal punten
* **Voltooiingspercentage**: aantal beantwoorde vragen op het totaal
* **Reactietijd**: hoe lang het invullen van de vragenlijst duurde
* **Aandachtspunten**: antwoorden die op basis van de configuratie van het sjabloon automatisch zijn gemarkeerd omdat ze aandacht vragen
* **Resultaten van de analyse**: automatische analyseblokken op basis van de antwoorden (nalevingsniveau, risicobeoordeling enzovoort)
* **Scores per categorie**: weergegeven als radardiagram of staafdiagram

Antwoorden op meerkeuzevragen worden beknopt weergegeven:

* alleen de opties die de respondent heeft geselecteerd, worden getoond;
* de link **Alle opties weergeven** onder elke vraag toont de niet-geselecteerde opties van die vraag, en de link **Opties verbergen** keert terug naar de beknopte weergave;
* een onbeantwoorde vraag wordt aangeduid met een koppelteken (-), zonder lijst van opties.

<figure><img src="../../.gitbook/assets/audit-questionnaire-response-condensed-view.png" alt="Antwoorden op een vragenlijst in beknopte weergave"><figcaption><p>Alleen de geselecteerde opties worden getoond; de andere opties blijven per vraag beschikbaar</p></figcaption></figure>

## AI-analyse (bèta)

Start vanuit de rapportageweergave van een antwoord de **Analyse IA** om te krijgen:

* een algemene nalevings- of risicoscore
* een schriftelijke samenvatting van de belangrijkste bevindingen
* een uitsplitsing per criterium (volledigheid, wettelijke basis, beveiligingsmaatregelen enzovoort)
* voorgestelde taken om de vastgestelde tekortkomingen aan te pakken

{% hint style="warning" %}
De AI-analyse is een bètafunctie. Interpreteer de resultaten voorzichtig en laat ze nalezen door een gekwalificeerde professional.
{% endhint %}

## Een antwoord valideren

Klik na het nalezen van het antwoord op **Controleer en valideer de audit** om het de status **Geldig** te geven. Deze actie is beschikbaar voor de verantwoordelijken van de vragenlijst.

{% hint style="info" %}
Kunt u een antwoord niet valideren, controleer dan of de respondent op de knop **Finaliseren** heeft geklikt. Zonder die stap blijft het antwoord in de status **Wachten op validatie**.
{% endhint %}

## Een vragenlijst annuleren

Bij een antwoord dat **wacht op validatie** kan de verantwoordelijke de vragenlijst annuleren, zonder terug te gaan naar de lijst met vragenlijsten. De actie **Annuleer de vragenlijst** staat in de validatiestap, naast **Valideer de vragenlijst** en **Vraag revisie aan**.

<figure><img src="../../.gitbook/assets/questionnaire-cancel-button.png" alt="Validatieacties van een antwoord: Valideer de vragenlijst, Vraag revisie aan, Annuleer de vragenlijst"><figcaption><p>De actie Annuleer de vragenlijst staat in de validatiestap</p></figcaption></figure>

Annuleren vraagt om een bevestiging en accepteert een optionele opmerking. De opgegeven reden wordt bewaard in de geschiedenis en blijft zichtbaar voor de respondent.

Een geannuleerd antwoord krijgt de status **Geannuleerd**, getoond als rode badge in de lijst, de filters, de rapportageweergave en de exports. De respondent kan het niet meer bewerken en het wordt niet opgenomen in de resultaten.

## Antwoorden samenvoegen in het gekoppelde object

Na het invullen van een vragenlijst die aan een Dastra-object is gekoppeld (verwerkingsactiviteit, activum, actor enzovoort), kunt u de verzamelde antwoorden rechtstreeks samenvoegen met de velden van dat object.

Daarmee worden de overeenkomstige velden van het doelobject bijgewerkt op basis van de gegevens die in het formulier zijn ingevoerd, zonder extra handmatige invoer.

Open om de samenvoeging te starten het voltooide antwoord en klik op **Gegevens samenvoegen**, gevolgd door het type object tussen haakjes. Een bevestigingsvenster toont de velden die in het doelobject worden bijgewerkt.

<figure><img src="../../.gitbook/assets/questionnaire-merge-processing-button.png" alt="Rapportageweergave van een antwoord met de knop Gegevens samenvoegen voor een verwerkingsactiviteit"><figcaption><p>De knop Gegevens samenvoegen brengt de antwoorden op de vragenlijst terug in het gekoppelde Dastra-object</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/questionnaire-merge-processing-dialog.png" alt="Bevestiging van de samenvoeging met de details van de doelverwerkingsactiviteit"><figcaption><p>De samenvoeging bevestigen en de verwerkingsactiviteit aanmaken op basis van de verzamelde antwoorden</p></figcaption></figure>

Deze functie is vooral nuttig bij externe gegevensverzameling via Trust Centers, waar derden (leveranciers, subverwerkers) informatie invullen die daarna in uw interne registers moet worden doorgevoerd.

## Een vragenlijstsjabloon met AI vertalen

Met de AI-assistent vertaalt Dastra automatisch alle secties en vragen van een vragenlijstsjabloon naar een andere taal.

Open om de vertaling te starten een vragenlijstsjabloon en klik op **Vertaal de vragenlijst**.

<figure><img src="../../.gitbook/assets/questionnaire-translate-button.png" alt="Knop Vertaal de vragenlijst in de sjabloneditor"><figcaption><p>De knop Vertaal de vragenlijst is beschikbaar in de sjabloneditor</p></figcaption></figure>

Kies de doeltaal en de opslagmodus:

* **Nieuwe versie**: vervangt de huidige versie van het sjabloon door de vertaling
* **Nieuwe onafhankelijke sjabloon**: maakt een afzonderlijk sjabloon aan zonder koppeling met het origineel

<figure><img src="../../.gitbook/assets/questionnaire-translate-dialog.png" alt="Venster voor de AI-vertaling met doeltaal en opslagmodus"><figcaption><p>De doeltaal en de opslagmodus van de vertaling selecteren</p></figcaption></figure>

## Een actieplan genereren

Klik in de rapportageweergave van een antwoord op **Genereer een actieplan** om automatisch taken aan te maken op basis van de gegeven antwoorden. De taken worden voorgesteld volgens de configuratie van het sjabloon en rechtstreeks toegevoegd aan de module voor taakbeheer van Dastra.
