---
description: >-
  Importeer uw gegevens uit een Excel- of CSV-bestand in Dastra: importeerbare
  objecten, conflictbeheer, kolomkoppeling en resultaat.
---

# Uw gegevens importeren (Excel, CSV)

## Gegevens importeren in Dastra

Dastra importeert uw eigen gegevens uit een spreadsheetbestand. Start de import in elke lijst die dit ondersteunt via de pijl van de aanmaakknop en kies daarna **Importeren**.

<figure><img src="../../.gitbook/assets/general-import-1.png" alt="Lijst met datasets en het menu van de aanmaakknop met de optie Importeren"><figcaption><p>De optie Importeren in het menu van de aanmaakknop</p></figcaption></figure>

U kunt de volgende objecten importeren:

| Object | Waar importeren | Opmerking |
| --- | --- | --- |
| Verwerkingsactiviteiten | Data inventory > Gegevensverwerking > Register voor gegevensverwerking | Plat bestand (CSV), complexe Excel-werkmap (bèta) of JSON |
| Activa | Data inventory > Referenties > Activa | Excel of CSV, of JSON |
| Stakeholders | Data inventory > Referenties > Actoren | |
| Datasets | Data inventory > Referenties > Gegevenssets | |
| Gegevensvelden | Data inventory > Referenties > Verklarende woordenlijst voor gegevens | |
| Beveiligingsmaatregelen | Data inventory > Referenties > Maatregelen | |
| Categorieën van betrokkenen | Data inventory > Referenties > Categorie van betrokken personen | |
| AI-systemen en AI-modellen | Data inventory > AI-wet | |
| Verzoeken van betrokkenen | Operations > Verzoeken > Register van verzoeken | |
| Datalekken | Operations > Incidenten > Incidentenregister | |
| Taken | Operations > Planning > Taken | Projecten importeert u in JSON via **Projecten** |
| Contracten en beleidslijnen | Operations > Contracten en beleidslijnen > Register van contracten en beleidslijnen | |
| Risicotypen, bedreigingen, bronnen, controlepunten en gebeurtenissen | Governance > Risicobeheer | |
| Vragenlijstsjablonen | Governance > Vragenlijsten > Vraagmodellen > **Maak een sjabloon** > **Upload een sjabloon** | Excel- of JSON-bestand |
| Antwoorden op vragenlijsten | Lijst met antwoorden van een sjabloon > **Plan een audit** > **Antwoorden importeren** | |
| Kaders, controles, tests, bedreigingen en risico's van de bibliotheek | Governance > Conformiteit > Bibliotheek | Zie [Importeren en sjablonen van Dastra](../compliance/library/frameworks/import.md) voor de kaders |
| Labels | Instellingen voor werkruimte > Proces > Labels | |
| Berichtsjablonen | Instellingen voor werkruimte > Modellen | |
| Organisatorische eenheden | Instellingen voor werkruimte > Toegangsbeheer > Organisatorische eenheden | CSV-bestand |

De namen van de menugroepen Data inventory, Operations en Governance hebben geen Nederlandse waarde in de app en staan zoals ze op het scherm verschijnen.

Voor een uitgewerkt voorbeeld met een aangepast veld en de modus **Samenvoegen**, zie [Activa importeren uit een spreadsheet](../../examples/excel-import.md).

Bij elke import is het proces hetzelfde. Het verloopt in 4 stappen:

1. [Het gegevensbestand voorbereiden](import.md#1.-het-gegevensbestand-voorbereiden)
2. [Het bestand laden](import.md#2.-het-bestand-laden)
3. [Uw gegevens controleren](import.md#3.-uw-gegevens-controleren)
4. [De gegevens importeren](import.md#4.-de-gegevens-importeren)

### 1. Het gegevensbestand voorbereiden

Dastra ondersteunt de volgende gegevensindelingen:

* Excel (.xlsx)
* Platte bestanden (.csv, .txt) met het scheidingsteken ; en UTF-8-codering (de codering is nodig om accenten te behouden)
* JSON, voor het volledige register, de activa, de projecten, de vragenlijstsjablonen en de conformiteitskaders

Bij sommige lijsten kiest u de indeling voordat de importwizard opent. Voor het verwerkingsregister opent de optie voor CSV-bestanden (in de app **Excel** genoemd) de hieronder beschreven wizard.

#### Het bestandssjabloon downloaden

Klik in de importwizard op **Het bestandssjabloon downloaden**. Het sjabloon is een CSV-bestand dat u kunt bewerken met Excel, LibreOffice of Google Sheets. Het bevat alle kolommen van de import met één rij voorbeeldgegevens, die u door uw eigen gegevens vervangt.

#### Het bestandssjabloon invullen

Vul het gedownloade bestand met uw gegevens. De knop **Zie kolomindeling** toont voor elke import de verwachte kolommen, hun regels en hun mogelijke waarden.

<figure><img src="../../.gitbook/assets/general-import-3.png" alt="Venster met de kolomindeling voor de import, met het type, de regels en de mogelijke waarden van elke kolom"><figcaption><p>De kolomindeling die de import verwacht</p></figcaption></figure>

De mogelijke waarden staan in het Engels: het gaat om een technische import in de database. Ze komen overeen met de keuzelijsten van de toepassing.

Bij de import van het register zijn bijvoorbeeld:

* de kolom `State` de status van de verwerkingsactiviteit: `Draft` voor **Concept** en `Active` voor **Gepubliceerd**. Als de cel leeg is, wordt de verwerkingsactiviteit aangemaakt met de status **Gepubliceerd**;
* de kolom `ProcessingState` het veld **Status gegevensverwerking** van de stap **Algemeen**: `Study` voor **Om te bestuderen**, `BeingDeployed` voor **Wordt geïmplementeerd**, `InProduction` voor **In productie** en `Stopped` voor **Gestopt**.

Een waarde die bij geen enkele mogelijke keuze past, blokkeert de import niet: ze wordt vervangen door de standaardwaarde van de kolom. Controleer uw waarden voordat u het bestand verstuurt.

### Datasets: import van gekoppelde velden

De export van datasets bevat een kolom **Velden voor persoonlijke gegevens** met de gekoppelde gegevensvelden. Elk veld wordt geschreven als `label#gevoeligheidsclassificatie#categorie persoonsgegevens` en de velden worden gescheiden door `|`. Voor de import geldt dezelfde indeling.

Tijdens de import geldt voor elke nieuwe dataset:

* een veld waarvan het label al in de werkruimte bestaat, wordt ongewijzigd gekoppeld: de classificatie en de categorie in het bestand wijzigen het niet;
* een veld waarvan het label niet bestaat, wordt automatisch aangemaakt.

{% hint style="info" %}
Gekoppelde velden worden alleen gelezen voor datasets die door de import zijn aangemaakt. In de modus **Samenvoegen** worden de velden van een bestaande dataset niet gewijzigd.
{% endhint %}

Om datasets te importeren opent u **Data inventory** > **Referenties** > **Gegevenssets**, klikt u op de pijl van de knop **Nieuwe dataset** en kiest u **Importeren**.

### 2. Het bestand laden

Bij sommige objecten vraagt de importwizard eerst om een organisatorische eenheid: alle geïmporteerde items worden eraan gekoppeld. Dit geldt voor verwerkingsactiviteiten, verzoeken, datalekken, taken, contracten en AI-systemen.

<figure><img src="../../.gitbook/assets/general-import-2.png" alt="Stap Het bestand verzenden van de importwizard met conflictbeheer op Samenvoegen, het matchingveld en de zone om bestanden neer te zetten"><figcaption><p>De stap Het bestand verzenden, met het conflictbeheer</p></figcaption></figure>

#### Conflictbeheer

Voor objecten met een matchingsleutel (bijvoorbeeld het label of de referentie) bepaalt de groep **Conflictbeheer** wat er gebeurt wanneer een rij van het bestand overeenkomt met een bestaand item. Er zijn drie modi:

* **Geen: maak een registratie voor elke regel bestand** (standaard): elke rij maakt een nieuw item aan, ook als er al een identiek item bestaat;
* **Samenvoegen: Overschrijven van gegevens van overeenkomende rijen (gevaarlijk!)**: rijen die overeenkomen met een bestaand item werken dat bij, en de andere rijen maken nieuwe items aan;
* **Behoud: wijzig de gegevens die aan een voorwaarde voldoen niet**: rijen die overeenkomen met een bestaand item worden overgeslagen en dat item blijft ongewijzigd, en de andere rijen maken nieuwe items aan.

Kies bij **Samenvoegen** of **Behoud** het veld dat u wilt gebruiken voor het matchen van gegevens (**Kies het veld dat u wilt gebruiken voor het matchen van gegevens**). Een rij komt overeen met een item wanneer de waarde van dit veld in het bestand en in de werkruimte strikt identiek is, hoofdletters en kleine letters inbegrepen.

{% hint style="warning" %}
De modus **Samenvoegen** vervangt de opgeslagen waarden door die van het bestand. Een lege cel laat de bestaande waarde ongewijzigd, behalve in kolommen met een verplichte keuze (bijvoorbeeld het type of de status van een activum): die krijgen dan hun standaardwaarde, dus vul ze altijd in. Controleer uw bestand voordat u de import start, want de bewerking kan niet ongedaan worden gemaakt.
{% endhint %}

Objecten zonder matchingsleutel, zoals labels, berichtsjablonen, verzoeken of risicotypen, tonen deze groep niet. Bij datalekken wordt de groep wel getoond, maar elke rij maakt altijd een item aan. Bij imports in de conformiteitsbibliotheek worden rijen overgeslagen waarvan de referentie al bestaat, ongeacht de modus.

{% hint style="info" %}
Voor activa werkt de modus **Samenvoegen** ook **aangepaste velden** bij, ongeacht hun type. Net als bij de standaardkolommen laat een lege cel de opgeslagen waarde ongewijzigd, en een lijst met meerdere antwoorden vervangt de bestaande lijst volledig. Als een waarde wordt geweigerd, stopt de import zonder iets te wijzigen en geeft hij de betrokken rij aan.
{% endhint %}

#### Het bestand versturen

Klik op de zone **Verstuur/verplaats hier bestanden** om uw bestand te kiezen, of zet het rechtstreeks in de zone neer. Dastra leest de eerste rijen om de kolomkoppeling voor te bereiden.

### 3. Uw gegevens controleren

De stap **Correspondentie** koppelt de kolommen van uw bestand aan de kolommen die de import verwacht. Dastra koppelt ze automatisch wanneer de kop gelijk is aan de naam of het label van de kolom. De tabbladen **Alle kolommen**, **Geen overeenkomst** en **Correspondentie (geïmporteerd bestand)** filteren de lijst, en de kolom **Bestandsgegevens** toont een voorbeeld van uw gegevens.

<figure><img src="../../.gitbook/assets/general-import-4.png" alt="Stap Correspondentie met de Dastra-kolommen, de gekoppelde kolom van het bestand en een voorbeeld van de gegevens"><figcaption><p>De stap Correspondentie</p></figcaption></figure>

De knop **Ga verder** blijft uitgeschakeld zolang een verplichte kolom geen overeenkomst heeft.

### 4. De gegevens importeren

Klik op **Ga verder** om de import te starten. Het scherm **Resultaat** toont het aantal verwerkte rijen en het aantal aangemaakte, bijgewerkte en overgeslagen objecten. Klik op **Tonen** om de lijst te openen.

<figure><img src="../../.gitbook/assets/general-import-5.png" alt="Resultaatscherm van de import met het aantal verwerkte rijen en aangemaakte, bijgewerkte en overgeslagen objecten"><figcaption><p>Het resultaat van de import</p></figcaption></figure>

Als een rij de validatie niet doorstaat (bijvoorbeeld een leeg verplicht veld of een te lange waarde), wordt de hele import gestopt en wordt niets opgeslagen. Het bericht geeft het nummer van de betrokken rij, waarbij de kop van het bestand als rij 1 telt. Corrigeer het bestand en start de import opnieuw.

Controleer daarna of de gegevens correct in de toepassing zijn geïmporteerd.
