---
description: >-
  Dit hoofdstuk leert u hoe u de toestemmingen van onze cookiebanner
  programmatisch beheert.
---

# Toestemming programmatisch beheren

## Opslaglocatie van toestemmingen

Standaard worden toestemmingen 180 dagen lang opgeslagen in een browsercookie met de naam `consent-eu`, als geserialiseerde JSON. In de configuratie van de banner kunt u:

* de naam van deze cookie wijzigen (**Naam van de cookie voor de opslag van toestemming (standaard 'consent-eu')**);
* de levensduur (**Levensduur van toestemmingscookie (standaard 180 dagen)**) en het domein (**Cookie domein (standaard het subdomein van de pagina)**) ervan wijzigen;
* toestemmingen in plaats daarvan opslaan in localStorage (**LocalStorage inschakelen voor cookies op basis van toestemming**). De sleutel is dan `dastra-consents`, of de naam die u voor de cookie hebt gekozen.

{% hint style="info" %}
De verspreiding van toestemmingen hangt van deze gegevens af: wijzig ze niet rechtstreeks. Gebruik de Dastra JavaScript-SDK.
{% endhint %}

### Toegang tot de toestemmingsservice

De toestemmingsservice van Dastra is bereikbaar op deze manier:

```javascript
<script>
  window.dastra = window.dastra || [];
  window.dastra.push(['cookieReady',function(manager)
  {console.log(manager.consent)}]);
</script>
```

### Lijst van de beschikbare methoden in de toestemmingsmanager

In `manager.consent` hebt u de volgende methoden:

- getAllConsents(): alle toestemmingen ophalen
- hasConsented(): geeft `true` terug als de gebruiker al een expliciete toestemming heeft vastgelegd
- getPurposeConsent(purposeLabel:string): de toestemming voor een cookiecategorie ophalen
- setPurposeConsent(purposeLabel:string, consent:bool): de toestemming voor een categorie instellen
- getServiceConsent(serviceShortName:string): de toestemming voor een bepaalde dienst ophalen
- setServiceConsent(serviceShortName:string, consent:bool): de toestemming voor een bepaalde dienst instellen
- save(): de toestemmingen opslaan en de gebeurtenissen verzenden
- dispatchEvents(): de huidige toestemmingen toepassen (gebeurtenissen, Google Consent Mode, scripts) zonder ze op te slaan

Gebruik `manager.open()` en `manager.close()` om de banner te openen of te sluiten. Gebruik buiten de callback `cookieReady` `dastra.push(['openCookieConsent'])` en `dastra.push(['closeCookieConsent'])`.

### De lijst met toestemmingen van de gebruiker ophalen (getAllConsents)

Zodra u toegang hebt tot de toestemmingsmanager, kunt u de toestemmingen van de huidige gebruiker ophalen:

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager){
    // Get the complete consent services list
    var consents = manager.consent.getAllConsents()
}]);
</script>
```

{% hint style="warning" %}
Gebruik het volledige pad om `getAllConsents()` buiten de callback `cookieReady` aan te roepen (bijvoorbeeld vanuit uw eigen code nadat de banner is geladen):

```javascript
var consents = window.dastra.cookieConsent.consent.getAllConsents();
```

De oude syntaxis op het hoogste niveau, `dastra.getAllConsents()`, wordt niet meer ondersteund.
{% endhint %}

De bovenstaande methode geeft een lijst terug met alle toestemmingen van de gebruiker:

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

Cookiecategorieën worden geïdentificeerd door de volgende tekstlabels:

| Categorie | Label |
| --- | --- |
| Noodzakelijk | `Necessary` |
| Voorkeuren | `Preference` |
| Analytisch | `Analytical` |
| Marketing | `Marketing` |
| Overig | `Other` |
| Niet geclassificeerd | `Unclassified` |

{% hint style="warning" %}
Gebruik altijd de tekstlabels (bijvoorbeeld `'Analytical'`): numerieke waarden worden door de API niet ondersteund.
{% endhint %}

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady',function(manager){
    let consents = manager.consent.getPurposeConsent('Analytical');
    manager.consent.setPurposeConsent('Analytical', false);

    // persist consent
    manager.consent.save();
}]);
</script>
```

### Toestemmingen per dienst beheren

Om toestemmingen per dienst te beheren, hebt u de vereenvoudigde naam van de dienst nodig.

{% hint style="info" %}
U vindt de vereenvoudigde naam (slug) van de dienst in de interface voor dienstenbeheer van uw banner: bij het bewerken van een dienst verschijnt hij onder de naam van de cookie.
{% endhint %}

![Plaats van de vereenvoudigde naam van de cookie](../../../.gitbook/assets/cookies-service-cookie-name-field.png)

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady',function(manager){
    let cookieService = 'google-analytics';
    let consents = manager.consent.getServiceConsent(cookieService);
    manager.consent.setServiceConsent(cookieService, false);

    // persist consent in cookies
    manager.consent.save();
}]);
</script>
```

### Voorbeeld van gebruik

Het volgende voorbeeld toont hoe u programmatisch een volledige opt-out toepast, bijvoorbeeld wanneer de gebruiker klikt op een knop "Alles weigeren" die u zelf hebt gebouwd, of wanneer u een privacysignaal van de browser respecteert.

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager) {

  // Only act if the user hasn't already made an explicit choice
  if (!manager.consent.hasConsented()) {

    // Opt out of all non-essential categories
    manager.consent.setPurposeConsent('Preference',   false);
    manager.consent.setPurposeConsent('Analytical',   false);
    manager.consent.setPurposeConsent('Marketing',    false);
    manager.consent.setPurposeConsent('Other',        false);
    manager.consent.setPurposeConsent('Unclassified', false);

    // Persist the choice in the browser
    manager.consent.save();
  }

}]);
</script>
```

U kunt ook selectief opt-in toepassen, bijvoorbeeld om alleen analytische cookies te accepteren:

```javascript
<script>
window.dastra = window.dastra || [];
window.dastra.push(['cookieReady', function(manager) {

  manager.consent.setPurposeConsent('Analytical', true);
  manager.consent.setPurposeConsent('Marketing',  false);
  manager.consent.save();

}]);
</script>
```

### Reageren op wijzigingen van toestemming (de gebeurtenis `dastra:consents:updated`)

Telkens wanneer een gebruiker zijn toestemmingskeuzes wijzigt, via de banner of programmatisch met `save()`, verzendt Dastra een gebeurtenis `dastra:consents:updated` op `window`. U kunt zich erop abonneren om uw eigen logica uit te voeren: scripts van derden laden, de interface bijwerken, een analytische gebeurtenis verzenden enzovoort.

```javascript
window.addEventListener('dastra:consents:updated', function(event) {
  // event.detail contains the updated consents
  console.log('Consents updated', event.detail);

  // Example: reload Google Analytics if the user just accepted analytics
  if (window.dastra.cookieConsent.consent.getPurposeConsent('Analytical')) {
    // load or re-enable your analytics scripts here
  }
});
```

{% hint style="info" %}
Deze gebeurtenis wordt bij elke aanroep van `save()` of `dispatchEvents()` verzonden, en ook bij elke paginalading, wanneer de banner de opgeslagen keuzes toepast. Registreer de listener in `dastra:consents:ready` om alleen te reageren op wijzigingen van de bezoeker (zie [Google Tag Manager](blocking/google-tag-manager.md)).
{% endhint %}
