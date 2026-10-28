---
description: Deze pagina legt uit hoe u de talen van de toestemmingswidget kunt beheren
---

# Taalbeheer

## Hoe beheer ik meerdere talen voor de widget?

Ga naar de instellingenpagina voor de gewenste widget en vervolgens naar het tabblad "Teksten en vertalingen". Je kunt een of meer talen toevoegen.

![](<../../../.gitbook/assets/Capture web\_6-5-2022\_102131\_app.dastra.eu.jpeg>)

{% hint style="warning" %}
Houd er rekening mee dat momenteel alleen Frans en Engels worden ondersteund.
{% endhint %}

## Hoe wordt de taal van de widget gedetecteerd?

Standaard gebruikt de widget de taal uit het attribuut `lang` van de `<html>`-tag van de pagina. Ontbreekt dit attribuut, dan wordt de taal van de browser gebruikt.

## Hoe forceer ik de taal van de widget?

Om de taal van de widget te forceren, voeg je het attribuut `data-lang` toe aan de div van de widget:

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}" data-lang="fr"></div>
```

Laad je de widget met de methode `loadCookieConsent`, geef dan de optie `lang` mee:

```javascript
dastra.push(['loadCookieConsent', {
    widgetId: {your_widget_id},
    selector: '#cookie-consent',
    lang: 'fr'
}]);
```
