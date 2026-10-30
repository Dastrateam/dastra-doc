---
description: >-
  Voeg de velden die specifiek zijn voor uw activiteit toe aan uw formulieren
  met aangepaste velden: veldtypen, opties, gebruik en API.
---

# Aangepaste velden

## Wanneer u aangepaste velden gebruikt

Sommige informatie die specifiek is voor uw sector, zit niet in de standaardvelden van het verwerkingsregister, de verzoeken van betrokkenen, de taken enzovoort. Met aangepaste velden maakt u uw eigen formuliervelden aan om de gegevens die u invoert aan te vullen.

Dit is een voorbeeld van de configuratie van velden voor een stakeholder:

<figure><img src="../../.gitbook/assets/general-custom-fields-1.png" alt="Pagina Aangepaste velden van de stakeholder met een veldgroep en de bijbehorende velden"><figcaption><p>Veldconfiguratie van een stakeholder</p></figcaption></figure>

En dit is het resultaat in het formulier:

<figure><img src="../../.gitbook/assets/general-custom-fields-2.png" alt="Formulier van een stakeholder met de groep aangepaste velden"><figcaption><p>De aangepaste velden in het formulier van een stakeholder</p></figcaption></figure>

## Betrokken functies

Aangepaste velden zijn niet in elke module beschikbaar. U kunt de volgende formulieren aanpassen:

* [Verwerkingsactiviteiten](../ropa/README.md)
* [Verzoeken van betrokkenen](../requests/README.md)
* [Taken](../tasks/README.md)
* [Activa](../ropa/activity/assets.md)
* [Stakeholders](../ropa/activity/stakeholders.md)
* [Beveiligingsmaatregelen](../ropa/activity/security.md)
* [Datasets](../ropa/activity/datasets.md)
* Gegevensvelden
* [Datalekken](../incidents/README.md)
* [Risicobeoordelingen](../risks/attach-to-processing.md)
* [AI-systemen](../ai-systems/README.md)
* [Contracten en beleidslijnen](../contracts/README.md)
* [Controlepunten](../risks/process/monitor.md)

{% hint style="warning" %}
Het aantal velden is beperkt. Het aantal aangepaste velden hangt af van het abonnement van uw organisatie. Op de configuratiepagina staat een quota-indicator. Zie voor meer informatie de [pagina met de tarieven](https://www.dastra.eu/en/pricing).
{% endhint %}

## Beschikbare veldtypen

Dastra biedt de volgende veldtypen:

| Type | Gebruik |
| --- | --- |
| Tekst | Eén regel tekst |
| Tekstzone | Tekst op meerdere regels |
| Opgemaakte tekst | Tekst met opmaak |
| Aantal (geheel getal) | Een getal zonder decimalen |
| Aantal (decimaal) | Een getal met decimalen |
| Datum | Een datum |
| Datum en tijd | Een datum en een tijdstip |
| Selectievakje | Meerdere antwoorden mogelijk uit een lijst met keuzes |
| Radio | Eén enkel antwoord uit een lijst met keuzes |
| Eenvoudige selector | Eén waarde gekozen in een keuzelijst |
| Meervoudige selector | Meerdere waarden gekozen in een keuzelijst |
| Booleaans | Een antwoord Ja of Nee |

## Aangepaste velden gebruiken

Eenmaal aangemaakt werken aangepaste velden zoals de standaardvelden:

* Ze worden weergegeven en bewerkt in de formulieren van elke module.
* Ze kunnen in alle tabellen van de toepassing worden weergegeven: klik op de knop **Kolommen aanpassen** van de tabel. Standaard zijn ze verborgen.
* Ze zijn aanwezig in alle Excel-exports van gegevens. Zie voor meer informatie over exports [de pagina over exports](../ropa/export-import.md).
* Ze zijn aanwezig in PDF- en Word-rapporten wanneer bij het veld **Inbegrepen in PDF- of Word-rapporten?** is aangevinkt (standaard aangevinkt).
* Ze kunnen worden gefilterd met de [geavanceerde filters](filters.md). Velden van het type **Selectievakje** en **Meervoudige selector** kunnen echter niet worden gebruikt om een lijst te sorteren.
* Ze kunnen in gegevenstabellen in bulk worden bijgewerkt.
* Ze kunnen met het [importsysteem](import.md) uit platte bestanden worden geïmporteerd.
* Ze zijn toegankelijk en bewerkbaar via alle API's, met de variabelenaam die aan het veld is toegekend. Zie [Aangepaste velden in API's gebruiken](custom-fields.md#aangepaste-velden-in-apis-gebruiken).

## Aangepaste velden instellen

1. Klik in de zijbalk op **Instellingen voor werkruimte** en daarna op **Aangepaste velden**.
2. Kies in de lijst links de module waaraan u een aangepast veld wilt toevoegen.
3. Velden worden in groepen aangemaakt. Klik op **Een veldtype maken**.
4. Vul het label van de groep in (het veld **Tekst**) en de **Locatie in het formulier**. Bij sommige modules, zoals de verwerkingsactiviteit, kiest u de stap van het formulier waarin de groep wordt weergegeven.

<figure><img src="../../.gitbook/assets/general-custom-fields-3.png" alt="Venster voor het aanmaken van een groep velden met het label en de positie in het formulier"><figcaption><p>Een veldgroep aanmaken</p></figcaption></figure>

5. Sleep nadat de groep is aangemaakt een veldtype uit de lijst **Aangepaste velden** naar de groep. Het veldvenster opent.
6. Vul de opties van het veld in (zie hieronder) en sla op.

<figure><img src="../../.gitbook/assets/general-custom-fields-4.png" alt="Venster voor het aanmaken van een aangepast veld met de bijbehorende opties"><figcaption><p>De opties van een aangepast veld</p></figcaption></figure>

U herschikt velden, of verplaatst ze van de ene groep naar de andere, door te slepen. Een groep kan pas worden verwijderd als ze geen velden meer bevat. Een verwijderd veld gaat naar de prullenbak: schakel **Bekijk prullenbak** in om het te herstellen.

### Veldopties

| Optie | Beschrijving |
| --- | --- |
| **Tekst** (label van het aangepaste veld) | De naam van het veld zoals die in formulieren staat. Verplicht. |
| **Naam van de variabele (slug)** | De technische naam van het veld, gebruikt door API's en imports. Ze wordt voorgesteld op basis van het label, in kleine letters met underscores (bijvoorbeeld `business_owner` voor "Business owner"), en kan niet meer worden gewijzigd zodra het veld is aangemaakt. Ze wordt alleen in dit venster getoond: open het veld in de lijst om ze te lezen. Om het veld vanuit een vragenlijst in te vullen, schrijft u `custom_` gevolgd door deze naam (zie [Een record invullen met de antwoorden](../questionnaires/templates/record-mapping.md)). |
| **Tooltip-tekst** | Een hulptekst naast het veld. |
| **Verplicht veld** | Maakt de invoer verplicht. |
| **Inbegrepen in PDF- of Word-rapporten?** | Voegt het veld toe aan de gegenereerde rapporten. Standaard aangevinkt. |
| **Validatieregel** | Voor tekstvelden: controleert of de invoer een syntaxis volgt (e-mail, URL) of een **Aangepaste reguliere expressie (Javascript-formaat)**. |
| **Minimale grootte** en **Maximale grootte** | Lengte van de invoer voor tekstvelden. |
| **Minimumwaarde** en **Maximale waarde** | Grenzen voor numerieke velden. |
| **Antwoordkeuze** | Voor types met een lijst met keuzes: één rij per keuze, met een kleur. Met **Voeg een mogelijke keuze toe** voegt u een rij toe; als u tekst plakt met één optie per regel, wordt er per regel een antwoord aangemaakt. |

Het label en de variabelenaam van een veld moeten binnen een module uniek zijn.

## Aangepaste velden in API's gebruiken

Met Dastra haalt u via de [REST API](../../api/configuration.md) alle waarden op van entiteiten die aangepaste velden bevatten, en wijzigt of maakt u ze aan.

Een eigenschap `customFields` is aanwezig in elke entiteit die u met een `GET` ophaalt:

```json
 {
   "id": 1234,
   "label": "Test asset",
   etc...
   "customFields": {
     "dpo_name":"jean-marc le dpo",
     "dpo_email":"dpo@github.com",
     "dpo_habilitations": ["Expert","Consulting","Data Mapping"],
     "has_large_dataset":false,
     etc...
   }
 }
```

Om deze eigenschap te wijzigen, verstuurt u het element met `POST` of `PUT` en werkt u de elementen van de verzameling bij. De te gebruiken variabelenamen staan op de configuratiepagina voor aangepaste velden.

{% hint style="info" %}
Alle aangepaste velden worden door de server gevalideerd. Als een kolom niet in de configuratie voorkomt, wordt ze automatisch verwijderd.

Als een veld niet geldig is (bijvoorbeeld als het leeg is terwijl het als verplicht is aangemerkt), geeft de API een fout met de code 400.
{% endhint %}
