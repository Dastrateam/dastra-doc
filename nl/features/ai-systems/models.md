---
description: >-
  Bouw de repository van AI-modellen van uw organisatie op, importeer ze of
  genereer ze met de AI-assistent, en koppel de modellen daarna aan uw
  AI-systemen.
---

# Repository van AI-modellen

Voor elk AI-systeem dat u registreert, geeft u het AI-model of de AI-modellen op die het gebruikt. U beschrijft elk model één keer in een repository en koppelt het daarna aan de systemen die het gebruiken.

## Definitie

Een model voor kunstmatige intelligentie is een computerprogramma dat is ontworpen om specifieke taken uit te voeren met technieken voor machinaal leren en gegevensanalyse.

* Basis: een AI-model steunt op specifieke algoritmen en architecturen, zoals de neurale netwerken van deep learning, waarmee het van gegevens kan leren.
* Leren: het model wordt getraind met grote datasets om patronen en verbanden te herkennen. Zo kan het voorspellingen doen of content genereren op basis van nieuwe gegevens.
* Functie: het doel waarvoor het model wordt gebruikt, bijvoorbeeld beeldgeneratie voor het model Midjourney.
* Gebruik: deze modellen worden ingezet in uiteenlopende toepassingen, van chatbots en virtuele assistenten tot gegevensanalyse en contentcreatie.

## De repository openen

Klik op **AI-wet** in de zijbalk en daarna op **AI-modellen**.

<figure><img src="../../.gitbook/assets/ai-systems-models-1.png" alt="Lijst met AI-modellen met de knop Een nieuw AI-model creëren en het bijbehorende menu"><figcaption><p>De repository van AI-modellen</p></figcaption></figure>

De knop **Een nieuw AI-model creëren** opent het aanmaakvenster. Het menu ervan biedt ook:

* **Maak vanuit de bibliotheek**: kies een model uit de bibliotheek van Dastra;
* **Importeren**: importeer een lijst met modellen vanuit een bestand, zie hieronder;
* **Exporteren**: exporteer de lijst als CSV, Excel, JSON of Markdown.

## Een AI-model aanmaken

Klik op **Een nieuw AI-model creëren**. Het venster biedt drie opties:

* **Genereren met de IA**: de AI-assistent vult het dossier in vanuit een naam of een beschrijving, zie de volgende paragraaf;
* **Ingebouwde sjabloon**: maak het dossier aan vanuit onze bibliotheek of vanuit een andere werkruimte;
* **Gepersonaliseerd**: voer het dossier zelf in.

<figure><img src="../../.gitbook/assets/ai-systems-models-2.png" alt="Venster Een nieuw AI-model creëren met de drie opties Genereren met de IA, Ingebouwde sjabloon en Gepersonaliseerd"><figcaption><p>De drie opties om een AI-model aan te maken</p></figcaption></figure>

Voer bij **Gepersonaliseerd** de naam van het model in en vul het dossier daarna aan in het paneel **AI-model**:

| Veld | Inhoud |
| --- | --- |
| **Naam van het model** | Verplicht, maximaal 120 tekens. Voorbeeld: GPT 4, Mistral AI, MidJourney. |
| **Versie** | De exacte versie van het model, maximaal 30 tekens. Voorbeeld: gpt-4o-2024-05-13. |
| **Referentie** | Uw eigen referentie voor het model, maximaal 120 tekens. |
| **Uitgever** | De uitgever van het model, gekozen onder de stakeholders van uw werkruimte. U kunt er een aanmaken vanuit de lijst. |
| **Labels** | De labels waarmee u het model indeelt. |
| **Beschrijf het AI-model** | De beschrijving, maximaal 3.000 tekens. Beschrijf de kenmerken en de informatie waarover u beschikt. |
| **Leertype van de AI** | De methode waarmee het model is getraind, zie hieronder. |
| **Is dit model een AI voor algemeen gebruik?** | Ja of nee. Een AI-model voor algemeen gebruik (GPAI) is veelzijdig en kan worden geïntegreerd in veel downstreamsystemen. Een tooltip herinnert aan de definitie van de AI-verordening. |
| **Houdt dit model een systeemrisico in?** | Ja of nee. De vraag verschijnt alleen als het model voor algemeen gebruik is. Een tooltip herinnert aan de definitie van systeemrisico. |
| **Documentatie** | Een teksteditor voor de documentatie van het model. |

<figure><img src="../../.gitbook/assets/ai-systems-models-3.png" alt="Paneel AI-model met de velden naam, versie, uitgever, leertype en de vragen over algemeen gebruik en systeemrisico"><figcaption><p>Het dossier van een AI-model</p></figcaption></figure>

Het leertype beschrijft hoe het model is getraind om zijn taken uit te voeren. Het bepaalt hoe het model de opgedane kennis generaliseert. Dastra biedt er vier aan, elk met zijn definitie in de lijst:

* Begeleid leren: leren met gelabelde gegevens om voorspellingen te doen;
* Leren zonder toezicht: leren zonder gelabelde gegevens om patronen te vinden;
* Versterking leren: leren door beloningen en straffen om acties te optimaliseren;
* Transfert leren: kennis uit het ene gebied gebruiken om het leren in een ander gebied te verbeteren.

### Het dossier genereren met de AI-assistent

De optie **Genereren met de IA** van het aanmaakvenster genereert het dossier van een AI-model vanuit een eenvoudige naam of beschrijving. Ze is beschikbaar als uw abonnement de bijbehorende AI-functies bevat. De assistent zoekt op het web om de relevante informatie op te zoeken en in te vullen.

1. Klik op **Een nieuw AI-model creëren** en daarna op **Genereren met de IA**.
2. Voer de naam van het model of een korte beschrijving in, bijvoorbeeld "GPT-4o by OpenAI".
3. Controleer en vul het gegenereerde dossier aan voordat u het bevestigt.

De gegenereerde content is een suggestie. Controleer en vul de informatie aan voordat u bevestigt, want door AI gegenereerde content kan fouten bevatten.

<figure><img src="../../.gitbook/assets/ai-systems-create-generate-form.png" alt="Venster om een AI-model te genereren met invoerveld, taalkeuze en voorbeelden"><figcaption><p>Beschrijf het AI-model dat u wilt genereren (naam, uitgever enzovoort): het web wordt gebruikt om de informatie aan te vullen</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/ai-system-generate-result.png" alt="Door de assistent gegenereerd dossier van een AI-model, te controleren vóór bevestiging"><figcaption><p>Het gegenereerde dossier moet vóór bevestiging worden gecontroleerd</p></figcaption></figure>

### Modellen importeren en exporteren

Om meerdere modellen te importeren, opent u het menu van de knop **Een nieuw AI-model creëren** en klikt u op **Importeren**. De procedure is dezelfde als in de andere modules: zie [Uw gegevens importeren (Excel, CSV)](../general/import.md). Het bestand kan de volgende kolommen bevatten:

| Kolom | Beschrijving |
| --- | --- |
| `Label` | Naam van het model, verplicht. |
| `Ref` | Uw referentie voor het model. |
| `Description` | Beschrijving van het model. |
| `VersionName` | Versie van het model. |
| `LearningType` | `SupervisedLearning`, `UnSupervisedLearning`, `ReinforcedLearning` of `TransferLearning`. |
| `IsGeneralPurposeAi` | `true` als het model voor algemeen gebruik is, anders `false`. |
| `SystemicRisk` | `true` als het model een systeemrisico inhoudt, anders `false`. |
| `DocumentationHtml` | Documentatie van het model, als HTML. |

De actie **Exporteren** levert een CSV-, Excel-, JSON- of Markdownbestand van de lijst.

## Een model koppelen aan een AI-systeem

Open het dossier van het betreffende AI-systeem. De stap **AI-modellen** is de derde, na **Algemeen** en **Verantwoordelijkheid**.

1. Kies in de selector **Selecteer AI-modellen** een of meer modellen uit uw repository. U kunt er ook een aanmaken vanuit de selector.
2. Vul voor elk model de **Gebruiksbeschrijving** in. Dat veld legt uit hoe het model in dit AI-systeem wordt gebruikt.
3. Sla het dossier op.

Een waarschuwingspictogram markeert de modellen die een systeemrisico inhouden.

<figure><img src="../../.gitbook/assets/ai-systems-models-4.png" alt="Stap AI-modellen van een AI-systeem met één geselecteerd model en de gebruiksbeschrijving ervan"><figcaption><p>Een model koppelen aan een AI-systeem</p></figcaption></figure>
