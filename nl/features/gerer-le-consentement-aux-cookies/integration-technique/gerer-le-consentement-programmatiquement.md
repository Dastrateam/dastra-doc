---
description: >-
  Dit hoofdstuk leert je hoe je de toestemmingen van onze
  widget programmatisch te beheren.
---

# Toestemmingen programmatisch beheren

## Waar worden de toestemmingen opgeslagen?

Het volledige bewijs van de toestemming van de gebruiker wordt opgeslagen in de localStorage van de browser (de opslagsleutel heet dastra-consents) in json-formaat. De propagatie van toestemmingen hangt hiervan af, daarom wordt het niet aangeraden om de gegevens in deze sleutel direct te wijzigen.

{% hint style="info" %}
&#x20;Het wordt niet aanbevolen om de gegevens in de localStorage rechtstreeks te wijzigen. Gebruik bij voorkeur de dastra Javascript SDK.
{% endhint %}

### Toegang tot de toestemmingsservice

De toestemmingsservice van dastra kan als volgt worden geopend

```Javascript
<script>
dastra = dastra || []
dastra.push(['cookieReady',function(manager){
    console.log(manager.consent)
});
</script>
```

### Lijst van beschikbare methoden in de toestemmingsmanager

In manager.consent zijn de volgende methoden beschikbaar:

* open(): opent de toestemmingswidget.
* close(): Sluit de toestemmingswidget.
* getAllConsents(): Alle toestemmingen ophalen.
* getPurposeConsent(purposeId:number): vraagt toestemming op voor een categorie cookies
* setPurposeConsent(purposeId:number, consent:bool): stelt de toestemming voor een categorie in
* getServiceConsent(serviceShortName:string): hiermee wordt de toestemming voor een bepaalde dienst opgehaald.
* setServiceConsent(serviceShortName:string, consent:bool): stelt de toestemming voor een bepaald item in.

### De lijst met gebruikerstoestemmingen ophalen (getAllConsents)

Als je eenmaal toegang hebt tot de toestemmingsmanager, is het heel eenvoudig om de toestemmingen van de huidige gebruiker op te vragen:

```Javascript
<script>
dastra = dastra || []
dastra.push(['cookieReady', functie(manager){
    // De volledige lijst met toestemmingsservices ophalen
    var consents = manager.consent.getAllConsents()
});
</script>
```

De bovenstaande methode retourneert een lijst met alle toestemmingen van de gebruiker

```javascript
[
  {
    "id":"000000-0000000-000000",
    "name": "Service name",
    "purpose": 1,
    "logoUrl": "https://logo-url/img.jpg",
    "privacyPolicyUrl":"",
    "description": "Short description",
    "defaultConsent": true,
    "requiredConsent":true
  },
  ...
]
```

### Toestemmingen per categorie opvragen (getPurposeConsent/setPurposeConsent)

Cookiecategorieën worden vertegenwoordigd door de volgende id's:

| Type        | Id |
| ----------- | -- |
| Noodzakelijk | 0  |
| Voorkeuren | 1  |
| Analytisch | 2  |
| Marketing   | 3  |
| Andere     | 4  |

```Javascript
<script>
dastra = dastra || []
dastra.push(['cookieReady',function(manager){
    // De volledige lijst met toestemmingsservices ophalen
    laat cookiePurpose = 2; // 2 = Analytisch
    laat toestemmingen = manager.consent.getPurposeConsent(cookiePurpose);
    manager.consent.setPurposeConsent(cookiePurpose, false)
});
</script>
```

### Toestemmingen per service manipuleren

Om toestemmingen per service te manipuleren, heb je de vereenvoudigde servicenaam nodig die beschikbaar is in de servicebeheerinterface van je widget.

{% hint style="info" %}
**Hoe vind ik de vereenvoudigde servicenaam?
Ga naar de servicebeheerinterface en bewerk een service. De vereenvoudigde naam (slug) van de service verschijnt onder de naam van de cookie.
{% endhint %}

![Locatie van vereenvoudigde cookienaam](<../../..gitbook/assets/image (67).png>)

```javascript
<script> 
dastra = dastra || []
dastra.push(['cookieReady',function(manager){
    // De volledige lijst met toestemmingsservices ophalen
    laat cookiePurpose = 'google-analytics'; // 2 = Analytic
    laat toestemmingen = manager.consent.getServiceConsent(cookiePurpose );
    manager.consent.setServicePurpose(cookiePurpose, false)
});
</script>
```