---
beschrijving: Dastra geeft u oneindig veel mogelijkheden om uw formulieren aan te passen
---

# Aangepaste velden

{% hint style="warning" %}
Deze functie is nog in bèta. Er kunnen nog enkele instabiliteiten zijn.
{% endhint %}

{% embed url="https://www.youtube-nocookie.com/embed/mDyJD-mnnL0" %}
Hoe aangepaste velden gebruiken in Dastra
{% endembed %}

## Wanneer moeten aangepaste velden gebruikt worden?

Het is mogelijk dat bepaalde informatie die specifiek is voor uw sector niet aanwezig is in de standaardvelden van het Verwerkingsregister, de uitoefening van rechten, taken, enz.

Met Dastra kunt u aangepaste formuliervelden maken die u eenvoudig kunt toevoegen om de ingevoerde gegevens te verrijken.

Hier is een voorbeeld van een veldconfiguratie voor de acteur:

<figure><img src="../../.gitbook/assets/image (2) (1) (3) (1) (1).png" alt=""><figcaption><p>Veldconfiguratie</p></figcaption></figure>

En hier is het resultaat in het formulier:

<figure><img src="../../.gitbook/assets/image (4) (1) (3).png" alt=""><figcaption></figcaption></figure>

## Betrokken functies

{% hint style="info" %}
Let op! Niet alle functies worden beïnvloed door aangepaste velden
{% endhint %}

Je kunt de volgende formulieren aanpassen:

* [Verwerking](../editer-le-registre.md/)
* [Rechten van betrokkenen](../gerer-les-exercices-des-droits.md)
* [Taken](../planifier/gerer-vos-taches.md)
* [Activa](../editer-le-registre/remplir-le-questionnaire/applications.md)
* [Actoren](../cartography/referentials.md)
* Metingen
* Gegevenssets
* Gegevensvelden
* [Inbreuken](../../rappels-utiles/rgpd-en-bref/violations-de-donnees.md)
* [Risicobeoordelingen](../la-gestion-des-risques/risques.md)

{% hint style="danger" %}
#### Beperkingen op het aantal velden

Het aantal aangepaste velden is beperkt, afhankelijk van het abonnement dat u gebruikt. Raadpleeg de prijspagina van de applicatie (https://www.dastra.eu/en/pricing) voor meer informatie over dit onderwerp.
{% endhint %}

## Beschikbare veldtypes

Dastra biedt verschillende soorten aangepaste velden

* Eenvoudige tekst
* Lange tekst
* Rijke tekst
* Geheel getal
* Decimaal getal
* Datum en tijd
* Datum en tijd
* Aankruisvakje (meerdere antwoorden) (**niet filtreerbaar**)
* Aankruisvakje (één antwoord)
* Eenvoudige selector
* Meervoudige selector
* Aankruisvakje (Ja/Nee)

## Aangepaste velden gebruiken

Je kunt :

* Aangepaste veldgegevens weergeven en wijzigen in de formulieren van elke module.
* Aangepaste velden kunnen worden weergegeven in alle weergavetabellen van de toepassing. Klik op de knop Instellingen tabelkolommen om ze weer te geven.
* Aangepaste velden zijn **aanwezig in alle Excel** data-exports. Voor meer informatie over exports, [raadpleeg de pagina over exports](../editer-le-registre/export-import-le-registre.md)
* Aangepaste velden kunnen optioneel worden opgenomen in HTML-, Word- en PDF-exports (door het vakje "Exporteerbaar in rapporten" aan te vinken bij het veld in kwestie).
* Met uitzondering van meervoudige antwoordvelden\*\*, kunnen alle aangepaste velden gefilterd worden met behulp van het \[geavanceerde filters] systeem (geavanceerde-filters.md).
* Aangepaste velden kunnen massaal worden bijgewerkt in gegevenstabellen.
* Aangepaste velden kunnen worden geïmporteerd via platte bestanden \[met behulp van het importsysteem] (import-uw-gegevens-excel-csv.md)
* Aangepaste velden zijn **toegankelijk en aanpasbaar via alle API's**. Gebruik hiervoor de variabelenaam die aan elke kolom is toegewezen. [Zie de sectie over het wijzigen van aangepaste velden via API](custom-fields.md#manipulate-custom-fields-in-api).

## Aangepaste velden instellen

* Ga naar uw **Workspace**.
* Klik links op het menu **Workspace-instellingen**.
* Klik op het **Aangepaste velden** menu
* Kies de module waarin je een aangepast veld wilt toevoegen.
* Velden moeten in groepen worden gemaakt. Deze groepen kunnen op een bepaalde manier in het formulier worden geplaatst Klik op "**Een veldgroep toevoegen**".

<figure><img src="../../.gitbook/assets/image (3) (1) (3) (1).png" alt=""><figcaption></figcaption></figure>

* **Vul de naam en locatie** in de gewenste vorm in

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (2) (2).png" alt=""><figcaption></figcaption></figure>

Voor sommige elementen kun je de gewenste locatie in het formulier definiëren!

* Zodra de groep is gemaakt, kun je de veldtypen\*\* die je wilt instellen \*\*slepen en neerzetten!

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (2) (3).png" alt=""><figcaption></figcaption></figure>

Vul alle informatie in!

* Klik op Opslaan en dat is het! Je eerste persoonlijke gegevensveld is klaar!
* Je kunt slepen en neerzetten om de volgorde van de velden aan te passen.

## Omgaan met aangepaste velden in API's

Met Dastra kun je via de [API Rest](../../api-references/configuration-api.md) alle waarden van entiteiten met aangepaste velden ophalen, wijzigen en aanmaken.

Een "**customFields**" eigenschap zal beschikbaar zijn in alle entiteiten die u ophaalt in get in Dastra.c

```json
 {
   "id": 1234,
   "label": "Test asset",
   etc...
   "customFields": {
     "dpo_name": "jean-marc le dpo",
     "dpo_email": "dpo@github.com",
     "dpo_habilitations": ["Expert", "Consulting", "Data Mapping"],
     "has_large_dataset":false,
     etc...
   }
 }
```

Als je deze eigenschap wilt wijzigen, post (POST) of wijzig (PUT) je gewoon het element en werk je de elementen in de verzameling bij.

Om de namen van aangepaste variabelen te verzamelen, moet je naar de configuratiepagina voor aangepaste velden gaan.

{% hint style="info" %}
Houd er rekening mee dat alle **aangepaste velden worden gevalideerd door de server**. Als een colonen niet aanwezig is in de configuratie, wordt het automatisch verwijderd.

Als een veld ongeldig is (bijvoorbeeld als het niet is ingevuld hoewel het is gemarkeerd als verplicht), zal dit een uitzondering opleveren met code 400
{% endhint %}

## Beperkingen

Je kunt **niet filteren op aangepaste velden van het meervoudige type (selectievakje (Meervoudig) en selector (Meervoudig))**. Dit is een bekende beperking waar we aan werken
