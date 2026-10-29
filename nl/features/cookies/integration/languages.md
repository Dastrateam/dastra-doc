---
description: Deze pagina legt uit hoe u de talen van de toestemmingsbanner beheert.
---

# Taalbeheer

## Talen aan de banner toevoegen

1. Klik in het menu op **Toestemming voor cookies** > **Banners** en klik daarna op uw banner.
2. Klap de sectie **Teksten en vertalingen** uit.
3. Klik op **Taal toevoegen**, kies de taal in de lijst en klik opnieuw op **Taal toevoegen**.

<figure><img src="../../../.gitbook/assets/cookies-languages-1.png" alt="De sectie Teksten en vertalingen met de lijst van bannertalen en hun badges"><figcaption><p>De sectie "Teksten en vertalingen"</p></figcaption></figure>

De eerste taal in de lijst is de standaardtaal. Klik naast een taal op **Standaard instellen** om een andere taal te kiezen. Klik op **Bewerken** om de teksten van een taal aan te passen.

In de keuzelijst zijn de talen in de groep **Talen met vertalingen** al door Dastra vertaald: Engels (VS), Engels (VK), Frans, Duits, Spaans, Italiaans, Nederlands, Grieks, Pools en Portugees. De andere talen staan in de groep **Talen die niet zijn vertaald**: u voert de teksten zelf in.

Elke taal die u toevoegt, draagt een badge:

* **Vooraf vertaald**: de taal is een van de talen die Dastra vertaalt;
* **Behoefte aan vertaling**: sommige teksten van de taal zijn nog leeg;
* **Volledig vertaald**: alle teksten zijn ingevuld.

Een teller toont het aantal aangepaste teksten ten opzichte van het totale aantal teksten.

## Detectie van de taal van de banner

Standaard gebruikt de banner de taal die is ingesteld in het attribuut `lang` van de `<html>`-tag van de pagina. Ontbreekt dit attribuut, dan gebruikt de banner de taal van de browser.

Staat deze taal (of de hoofdtaal ervan, bijvoorbeeld `fr` voor `fr-FR`) niet in de lijst van de banner, dan verschijnt de banner in de eerste taal van de lijst.

## De taal van de banner forceren

Voeg het attribuut `data-lang` toe aan de `div` van de banner om de taal te forceren:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}" data-lang="fr"></div>
```

Laadt u de banner met de methode `loadCookieConsent`, geef dan de optie `lang` mee:

```javascript
dastra.push(['loadCookieConsent', {
    widgetId: {your_widget_id},
    selector: '#cookie-consent',
    lang: 'fr'
}]);
```
