---
description: >-
  Dit artikel laat zien hoe u de widget voor verzoeken van betrokkenen in een webpagina integreert.
---

# Technische integratie

## Doel

De widget voor verzoeken van betrokkenen verzamelt automatisch verzoeken van betrokkenen van uiteenlopende typen (verwijdering, wijziging, rectificatie enzovoort) vanaf een pagina van uw site.

De widget maakt deel uit van de Dastra JavaScript-SDK.

## Vereisten

Om de widget voor verzoeken van betrokkenen in te stellen hebt u een openbare API-sleutel nodig: lees [Beheer van API-sleutels](../settings/api-keys.md) of [ga rechtstreeks naar de pagina voor het beheer van API-sleutels](https://app.dastra.eu/general-settings/api).

## De widget instellen in de speciale interface

U stelt de widget eerst in via de lijst met formulieren: klik in het menu **Verzoeken** op **Collectie-widgets**.

<figure><img src="../../.gitbook/assets/requests-widget-1.png" alt="Lijst van formulieren met de knop Nieuwe widget"><figcaption><p>De lijst van formulieren</p></figcaption></figure>

Hier is een voorbeeld van een integratie van de widget (in pop-upmodus met een openingsknop):

```html
<div id="customer-subject-form-custom"></div>
<button id="customer-request-button">Open the widget</button>
<script
  src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY}"
  async
></script>
<script>
  window.dastra = window.dastra || [];
  dastra.debug = true;
  window.dastra.push(function(){
    dastra.loadCustomerSubjectForm({
      selector: '#customer-subject-form-custom',
      widgetId: {your widget id},
      onLoad: function (form) {
        document.getElementById('customer-request-button').addEventListener('click',function () {
          form.open()
        })
      }
    })
  })
</script>
```

## De taal van het formulier afdwingen

Standaard wordt de taal van de browser gebruikt. Is die taal niet beschikbaar in de vertalingen van de widget, dan wordt automatisch de standaardtaal gekozen. U kunt de taal van de widget afdwingen door de eigenschap `data-lang` toe te voegen aan de div waarin het formulier wordt weergegeven.

_In dit voorbeeld is standaard Italiaans geselecteerd (indien beschikbaar)_

```html
<div id="customer-subject-popup" data-lang="it"></div>
```

## De velden van het formulier vooraf invullen

U kunt de velden van het formulier vooraf invullen vanuit de authenticatiecontext van de gebruiker. Vooraf ingevulde velden worden voor de gebruiker alleen-lezen weergegeven (grijs).

Beschikbare standaardvelden:

```javascript
dastra.push(['set', 'dsr:refId', '{unique_user_id}'])
dastra.push(['set', 'dsr:email', '{email}'])
dastra.push(['set', 'dsr:givenName', '{first_name}'])
dastra.push(['set', 'dsr:familyName', '{last_name}'])
dastra.push(['set', 'dsr:address', '{address}'])
dastra.push(['set', 'dsr:zipCode', '{postcode}'])
dastra.push(['set', 'dsr:city', '{city}'])
dastra.push(['set', 'dsr:countryCode', '{country_code}']) // e.g. "FR"
dastra.push(['set', 'dsr:phoneNumber', '{phone}'])
dastra.push(['set', 'dsr:message', '{message}'])
```

De eigenschap `refId` is de unieke identificatie van de persoon in uw systeem (klant-ID, sessie-ID enzovoort). Ze wordt alleen-lezen weergegeven, en alleen als het veld **Persoonsreferentie** tot de actieve velden van het formulier behoort.

Aangepaste velden:

```javascript
// Pass a complete object
var payload = {
  customFieldSlug1: 'value1',
  customFieldSlug2: 'value2'
}
dastra.push(['set', 'dsr:additionalDatas', payload])

// Or field by field (@ prefix)
dastra.push(['set', 'dsr:@customFieldSlug1', 'value1'])
```

## Parameters meesturen in paginamodus

U kunt deze parameters ook in de querystring meegeven: zet `dsr_` voor de naam van de parameter.

```url
https://api.dastra.eu/v1/client/data-subject-request/page?id=<Your widget id>
&key=<your public key>
&dsr_email=test@github.org
&dsr_givenName=Dastonaute
&dsr_refId=123456
&...etc...
```

## De widget sluiten door buiten het venster te klikken

Gebruikt uw widget de opmaak **Modaal venster (pop-up)**, dan sluit het venster niet wanneer de gebruiker erbuiten klikt. Dat is bewust zo: het risico dat de ingevoerde gegevens verloren gaan, is te groot.

Wilt u toch dat de widget sluit wanneer de gebruiker buiten het venster klikt, gebruik dan de volgende code:

```javascript
window.dastra.customerSubjectReady().then((form) => {
  form.closeOnBackdrop = true
})
```

{% hint style="warning" %}
Hierdoor wordt alle tekst die de gebruiker heeft ingetypt zonder waarschuwing gewist. Bij een lang formulier kan dat gebeuren wanneer een tekstselectie verder reikt dan een lang tekstveld.
{% endhint %}

## Meerdere widgets in één pagina integreren

Standaard ondersteunt Dastra geen meerdere widgets in dezelfde pagina.

U kunt dat toch doen met twee aanroepen van `loadCustomerSubjectForm`, één per widget, met verschillende selectors en widget-ID's.

```html
<html lang="en-GB">
  <body>
    <h2>My first widget</h2>
    <div id="widget-1"></div>
    <h2>My second widget</h2>
    <div id="widget-2"></div>
    <script
      async
      src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR_PUBLIC_KEY}"
    ></script>
    <script>
      window.dastra = window.dastra || []

      // Widget 1 initialization
      window.dastra.push(function () {
        window.dastra.loadCustomerSubjectForm({
          selector: '#widget-1',
          widgetId: 991, // YOUR_WIDGET_ID_
          onLoad: function (form) {
            // Initialization
          }
        })
      })

      // Widget 2 initialization
      window.dastra.push(function () {
        window.dastra.loadCustomerSubjectForm({
          selector: '#widget-2',
          widgetId: 992, // the widget identifier for the second widget
          onLoad: function (form) {
            // Initialization
          }
        })
      })
    </script>
  </body>
</html>
```

Om in deze opzet de beginwaarden van de velden van een widget in te stellen, gebruikt u de eigenschap `form.initialData` in `onLoad`:

```javascript
window.dastra.push(function () {
  dastra.loadCustomerSubjectForm({
    selector: '#customer-subject-form-custom',
    widgetId: widgetId,
    onLoad: function (form) {
      form.initialData = {
        givenName: 'testFirstName'
      }
      document
        .getElementById('customer-request-button')
        .addEventListener('click', function () {
          form.closeOnBackdrop = true
          form.open()
        })
    }
  })
})
```
