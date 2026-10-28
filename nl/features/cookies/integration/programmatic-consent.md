---
description: >-
  Dit hoofdstuk leert je hoe je de toestemmingen van onze
  widget programmatisch te beheren.
---

# Toestemmingen programmatisch beheren

## Waar worden de toestemmingen opgeslagen?

Standaard worden de toestemmingen 180 dagen lang opgeslagen in een browsercookie met de naam `consent-eu`, als geserialiseerde JSON. In de configuratie van de banner kun je:

* de naam van deze cookie wijzigen;
* de levensduur en het domein ervan wijzigen;
* de toestemmingen in plaats daarvan in de localStorage opslaan. De sleutel is dan `dastra-consents`, of de naam die voor de cookie is gekozen.

{% hint style="info" %}
De verspreiding van de toestemmingen hangt af van deze gegevens: wijzig ze niet rechtstreeks. Gebruik de JavaScript-SDK van Dastra.
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

* getAllConsents(): Alle toestemmingen ophalen.
* getPurposeConsent(purposeLabel:string): vraagt toestemming op voor een categorie cookies
* setPurposeConsent(purposeLabel:string, consent:bool): stelt de toestemming voor een categorie in
* getServiceConsent(serviceShortName:string): hiermee wordt de toestemming voor een bepaalde dienst opgehaald.
* setServiceConsent(serviceShortName:string, consent:bool): stelt de toestemming voor een bepaald item in.
* save(): slaat de toestemmingen op en activeert de events
* dispatchEvents(): past de huidige toestemmingen toe (events, Google Consent Mode, scripts) zonder ze op te slaan

Gebruik `manager.open()` en `manager.close()` om de widget te openen of te sluiten. Buiten de callback `cookieReady` gebruik je `dastra.push(['openCookieConsent'])` en `dastra.push(['closeCookieConsent'])`.

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
    "id": "000000-0000000-000000",
    "name": "Google Analytics",
    "slug": "google-analytics",
    "consent": true,
    "version": "1",
    "date": "2026-10-28T10:00:00.000Z",
    "purpose": "Analytical"
  },
  ...
]
```

### Toestemmingen per categorie opvragen (getPurposeConsent/setPurposeConsent)

Cookiecategorieën worden aangeduid met de volgende labels:

| Categorie    | Label          |
| ------------ | -------------- |
| Noodzakelijk | `Necessary`    |
| Voorkeuren   | `Preference`   |
| Analytisch   | `Analytical`   |
| Marketing    | `Marketing`    |
| Andere       | `Other`        |
| Niet geclassificeerd | `Unclassified` |

{% hint style="warning" %}
Gebruik de **labels als tekenreeks** (bijv. `'Analytical'`) en niet de numerieke waarden: die worden niet ondersteund.
{% endhint %}

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager){
    let consent = manager.consent.getPurposeConsent('Analytical');
    manager.consent.setPurposeConsent('Analytical', false);

    // persist consent in cookies
    manager.consent.save();
}]);
</script>
```

### Toestemmingen per service manipuleren

Om toestemmingen per service te manipuleren, heb je de vereenvoudigde servicenaam nodig die beschikbaar is in de servicebeheerinterface van je widget.

{% hint style="info" %}
**Hoe vind ik de vereenvoudigde servicenaam?**\
Ga naar de servicebeheerinterface en bewerk een service. De vereenvoudigde naam (slug) van de service verschijnt onder de naam van de cookie.
{% endhint %}

![Locatie van vereenvoudigde cookienaam](<../../../.gitbook/assets/image (67).png>)

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager){
    let cookieService = 'google-analytics';
    let consent = manager.consent.getServiceConsent(cookieService);
    manager.consent.setServiceConsent(cookieService, false);

    // persist consent in cookies
    manager.consent.save();
}]);
</script>
```