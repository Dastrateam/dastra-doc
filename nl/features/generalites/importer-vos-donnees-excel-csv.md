# Gegevens importeren (Excel, Csv)

## Gegevens importeren in Dastra

Met Dastra is het heel eenvoudig om uw eigen gegevens in spreadsheetformaat rechtstreeks in de toepassing te importeren.

Importeren is mogelijk in de volgende modules:&#x20;

* register importeren
* actor importeren
* Activa importeren
* importeren van datasets
* importeren van velden
* invoer van beveiligingsmaatregelen
* invoer van categorieën van betrokken personen
* importeren van auditreacties
* importeren van auditmodellen (binnenkort beschikbaar)
* importeren van risicotypen
* importeren van verzoeken om rechten uit te oefenen
* importeren van datalekken
* importeren van taken

Het proces is hetzelfde voor elke import &#x20;

Er zijn 4 stappen:&#x20;

1. [Bereid het gegevensbestand voor](importer-vos-donnees-excel-csv.md#1.-preparation-du-fichier-de-donnees)
2. [Bestand uploaden](importer-vos-donnees-excel-csv.md#2.-charger-le-fichier)
3. [Controleer de gegevens voor het importeren](importer-vos-donnees-excel-csv.md#3.-verifiez-vos-donnees)
4. [Gegevens importeren](importer-vos-donnees-excel-csv.md#4.-importez-les-donnees)

### 1. Het gegevensbestand voorbereiden

Dastra ondersteunt de volgende gegevensindelingen:

* Excel** (.xlsx)
* Platte bestanden** (.csv, .txt) met scheidingsteken ; en UTF-8 codering (codering is belangrijk voor accenten)
* JSON** (alleen voor het importeren van het volledige register en de modellen voor Verwerking)

Om het menu voor het importeren van gegevens te openen, klikt u op de knop "importeren" onder elke pijl van de knop Maken.

<figure><img src="../../.gitbook/assets/image (261).png" alt=""><figcaption></figcaption></figure>

Selecteer Excel als daarom wordt gevraagd:&#x20;

<figure><img src="../../.gitbook/assets/image (83) (1).png" alt=""><figcaption></figcaption></figure>

#### Het bestandssjabloon downloaden

Download vervolgens een bestandssjabloon door op de knop "Bestandssjabloon downloaden" te klikken

<figure><img src="../../.gitbook/assets/image (264).png" alt=""><figcaption></figcaption></figure>

Het bestandssjabloon is **een CSV formaat bestand** dat je gemakkelijk kunt bewerken met een Libre Office, Wordpad, Excel of Google Sheet spreadsheet.

Het bevat alle benodigde kolommen met voorbeeldgegevens.

Voorbeeldbestand (voor het register) : &#x20;

<figure><img src="../../.gitbook/assets/image (265).png" alt=""><figcaption><p>Regel 2 bevat voorbeeldgegevens die vervangen moeten worden</p></figcaption></figure>

#### Vul de bestandssjabloon in

Vul het gedownloade bestand in met je gegevens.

Voor elk gegevensbestand kun je de verwachte waarden in de kolommen weergeven:&#x20;

<figure><img src="../../.gitbook/assets/image (262) (1).png" alt=""><figcaption><p>Verwachte waarden voor het registerimportbestand</p></figcaption></figure>

De imports bevatten verwachte waarden in het Engels. Dit is volkomen normaal. In feite is dit een technische database-import &#x20;

De waarden in het Engels komen overeen met de vervolgkeuzelijsten voor de selectieknoppen &#x20;

Bijvoorbeeld, in de import van het register komt het veld "Verwerkingsstatus" overeen met het veld "Verwerkingsstatus" in Dastra. Dit is het veld dat wordt aangegeven in de eerste stap "Algemeen".

Het veld "Verwerkingsstatus" komt overeen met de status van de Verwerking ("Concept" voor "Concept" of "Gepubliceerd" voor "Actief") &#x20;

### 2. Het bestand laden

Als uw gegevensbestand klaar is, moet u mogelijk een organisatorische eenheid opgeven. Alle geïmporteerde bestanden worden in deze organisatorische eenheid geplaatst &#x20;

{% hint style="info" %}
Dit geldt alleen voor import van objecten die aan organisatorische eenheden gekoppeld kunnen worden. Bijvoorbeeld het verwerkingsregister of datalekken. Actoren, maatregelen of datasets vallen hier niet onder.
{% endhint %}

#### Gegevens bijwerken via import

Er wordt voorgesteld om een vakje aan te vinken waarmee bestaande gegevens kunnen worden bijgewerkt &#x20;

Met deze functie kunt u de gegevens in Dastra bijwerken vanuit de gegevens in het Excel-bestand &#x20;

Het importeren maakt standaard nieuwe objecten aan. Als het object al bestaat (bijvoorbeeld een acteur), wordt er geen nieuw object gemaakt &#x20;

Het is mogelijk om een bestaand object (bijvoorbeeld een actor) te updaten &#x20;

Selecteer in dit geval het vakje "Bestaande gegevens bijwerken" en kies het overeenkomende veld. Dit veld wordt de sleutel die wordt gebruikt om de bij te werken velden te identificeren.&#x20;

<figure><img src="../../.gitbook/assets/image (263).png" alt=""><figcaption><p>Gegevens bijwerken</p></figcaption></figure>

Door op de knop "Overschrijf gegevens van overeenkomende regels" te klikken, worden de corresponderende gegevens vervangen door de gegevens van de import.

#### Het bestand verzenden

Verzend het bestand door te klikken op de knop

<figure><img src="../../.gitbook/assets/image (266).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Je kunt je bestanden ook uploaden door ze te slepen en neer te zetten in het gebied voor het uploaden van bestanden
{% endhint %}

### 3. Controleer uw gegevens

Met het volgende hulpprogramma kunt u de kolommen in uw Excel-bestand valideren en eventueel selecteren op de kolommen die worden verwacht in het importformaat.

<figure><img src="../../.gitbook/assets/image (248) (1).png" alt=""><figcaption></figcaption></figure>

Als alles er goed uitziet, kun je beginnen met het importeren van de gegevens.

### 4. de gegevens importeren

Start het importeren van de gegevens door op de knop Doorgaan te klikken. Het importproces wordt dan gestart.

<figure><img src="../../.gitbook/assets/image (252) (1) (1).png" alt=""><figcaption></figcaption></figure>



### 5. Je bent klaar!

Je hebt het einde van deze handleiding bereikt! We raden je aan om te controleren of de gegevens in de tool zijn geïmporteerd.










