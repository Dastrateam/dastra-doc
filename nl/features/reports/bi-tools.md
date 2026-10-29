---
description: Leer hoe u Dastra koppelt aan uw favoriete hulpmiddel voor gegevensanalyse.
---

# Integratie met hulpmiddelen voor gegevensanalyse (BI)

{% hint style="info" %}
Om deze functie te gebruiken, moet uw abonnement het Enterprise-plan omvatten.
{% endhint %}

Met Dastra importeert u [aangepaste rapporten](README.md) in uw favoriete BI-hulpmiddel (Power BI, Google Looker, Tableau Software enzovoort). Zo benut u de mogelijkheden van BI-hulpmiddelen om gegevens diepgaand te analyseren, terwijl de rapporten automatisch worden ververst.

## Instellen in Dastra

Ga naar de module voor aangepaste rapporten, open een rapport en klik op de knop **Connect BI Tools**.

Er opent een venster. Klik op **Create connect link**.

Kopieer de gegenereerde link.

{% hint style="warning" %}
Geef de gegenereerde link aan niemand door. Ze geeft toegang tot de ruwe gegevens van het rapport.
{% endhint %}

## Power BI

1. Open Power BI Desktop:
   * Start Power BI Desktop op uw computer.
2. Maak verbinding met de gegevensbron Web:
   * Ga in Power BI Desktop naar het tabblad Home.
   * Klik op Get Data en selecteer **Web**.
3. Voer de URL van de JSON-link in:
   * Voer in het venster Get Data Web dat verschijnt de URL van uw JSON-bestand of API in (als u een JSON-deellink hebt).
   * Controleer of de URL verwijst naar een JSON-bestand of een API die JSON-gegevens teruggeeft.
   * Klik op OK.
4. Authenticatie (indien vereist):
   * Als de URL authenticatie vereist (bijvoorbeeld omdat hij met een wachtwoord of API-sleutel is beveiligd), vraagt Power BI u zich aan te melden.
   * Selecteer het juiste authenticatietype (bijvoorbeeld Anonymous, OAuth2, API Key) en vul zo nodig uw inloggegevens in.
5. Toegang tot de JSON-gegevens:
   * Power BI maakt verbinding met de URL en haalt het JSON-bestand op.
   * Na een geslaagde verbinding verschijnt een voorbeeldvenster met de JSON-gegevens. U verkent de gegevens als geneste lijsten, objecten of tabellen.

{% hint style="info" %}
* Prestaties: is uw JSON-bestand groot of bevat het diepe hiërarchieën, dan heeft Power BI mogelijk wat tijd nodig om de gegevens te laden en te transformeren.
* Gegevens verversen: worden de JSON-gegevens regelmatig bijgewerkt (bijvoorbeeld door een API), dan stelt u in Power BI Service een gegevensverversing in om de nieuwste gegevens automatisch op te halen.
{% endhint %}

## Google Looker <a href="#google-looker" id="google-looker"></a>

Google Looker maakt verbinding met Google BigQuery, een datawarehouse van Google Cloud dat JSON-bestanden kan opslaan en verwerken.

### 1. Google BigQuery als gegevensbron gebruiken

1. Upload het JSON-bestand naar Google Cloud Storage:
   * Is uw JSON-bestand bereikbaar via een deellink, upload het bestand dan eerst naar **Google Cloud Storage**.
   * Maak het openbaar of stel de juiste machtigingen in.
2. Laad de JSON-gegevens in BigQuery:
   * Open de console van Google Cloud Platform (Google Cloud Console).
   * Ga naar **BigQuery** en selecteer of maak een project.
   * Selecteer in **BigQuery** uw dataset en klik op **Create Table**.
   * Selecteer **Google Cloud Storage** als bron en voer de URL van uw JSON-bestand in bij het veld **URL**.
   * Stel het gegevensformaat in op **JSON** en controleer of **BigQuery** de structuur van uw bestand correct kan interpreteren.
3. Verbind BigQuery met Looker:
   * Zodra het JSON-bestand in BigQuery is geladen, verbindt u Looker met BigQuery.
   * Ga in Looker naar Admin > Connections en voeg BigQuery toe als gegevensbron.
   * Zodra de verbinding tot stand is gebracht, bevraagt en visualiseert u de BigQuery-gegevens rechtstreeks in Looker.

### 2. ETL-hulpmiddelen gebruiken om JSON in Looker te integreren

Wilt u de integratie van JSON-gegevens uit een API of extern bestand in Looker automatiseren, dan gebruikt u ETL-hulpmiddelen (Extract, Transform, Load) zoals Fivetran, Stitch of Airflow. Deze hulpmiddelen extraheren de JSON-gegevens, transformeren ze en laden ze in een datawarehouse dat compatibel is met Looker.

Voorbeeld met Fivetran:

1. Verbind een REST-API of JSON-bron met Fivetran.
2. Transformeer de gegevens zodat ze aan de eisen van uw datawarehouse voldoen.
3. Laad de gegevens in het datawarehouse (bijvoorbeeld BigQuery).
4. Verbind Looker met dit datawarehouse om de gegevens te bevragen en te visualiseren.

## Tableau Software <a href="#tableau-software" id="tableau-software"></a>

### 1. Tableau Desktop openen

* Start Tableau Desktop op uw computer.

### 2. Verbinden met een webgegevensbron

* Ga in Tableau Desktop naar het menu File en selecteer New Data Source.
* Klik in het venster voor de keuze van de gegevensbron op Web Data Connector. Met deze optie verbindt u met gegevens uit verschillende webbronnen, waaronder JSON-bestanden via een API of URL.

### 3. De JSON-URL invoeren

* Voer in het venster dat verschijnt de URL van het JSON-bestand of de API in.

### 4. Authenticatie (indien vereist)

* Vereist de JSON-URL een vorm van authenticatie (bijvoorbeeld een API-sleutel, een OAuth-token of inloggegevens), dan vraagt Tableau om inloggegevens.
* Selecteer het juiste authenticatietype (bijvoorbeeld API Key of OAuth) en vul de benodigde gegevens in.

### 5. JSON-gegevens analyseren in Tableau

* Tableau maakt verbinding met de URL, downloadt het JSON-bestand en probeert het om te zetten naar een begrijpelijke tabelvorm (een tabel of gestructureerde gegevensweergave).
* Tableau herkent de structuur van JSON-gegevens automatisch. Is het bestand erg complex of diep genest, dan moet u soms in de gegevenseditor aanpassingen doen om de gegevens af te vlakken of in een geschikt formaat om te zetten.

{% hint style="info" %}
* Beperkingen van JSON-bestanden: is uw JSON-bestand groot of sterk genest, dan kan Tableau het mogelijk niet goed verwerken. Soms moet u het eerst transformeren of vereenvoudigen voordat u het integreert.
* Authenticatie en beveiliging: vereist uw JSON-link een API-sleutel, beheer dan de autorisaties en inloggegevens zorgvuldig. Sommige API's beperken het aantal verzoeken of vereisen specifieke autorisaties.
* Gegevens verversen: veranderen de JSON-gegevens regelmatig (bijvoorbeeld via een API met realtime-updates), dan stelt u Tableau in om de gegevens met vaste tussenpozen automatisch te verversen, zodat uw rapporten up-to-date blijven.
{% endhint %}
