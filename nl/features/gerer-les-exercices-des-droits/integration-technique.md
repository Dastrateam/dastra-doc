---
beschrijving: >-
  Dit artikel laat zien hoe je de widget voor het uitoefenen van rechten kunt integreren in
  een webpagina
---

# Technische integratie

### Doelstellingen

Met de widget voor de uitoefening van rechten kunt u **automatisch vanaf een pagina op uw site verzoeken om de uitoefening van rechten** van verschillende typen (verwijderingen, wijzigingen, rectificaties, enz.) verzamelen.

De widget is geïntegreerd in de dastra **SDK javascript**.

### Vereisten

Om de widget voor het uitoefenen van rechten in te stellen, moet u een **openbare API-sleutel** hebben: [lees de documentatie](../settings/gestion-des-cles-dapi.md) of [ga direct naar de pagina voor het beheer van API-sleutels](https://app.dasta.eu/general-settings/api).

### De widget instellen in de speciale interface

Om te beginnen moet je de **widget** instellen in **het widgetbeheerpaneel**:&#x20;

![](<../../.gitbook/assets/image (250) (1) (1) (1).png>)

Hier is een eenvoudig voorbeeld van widget integratie (in popup mode met een open knop):

```html
<div id="customer-subject-form-custom" ></div>
<button id="customer-request-button">Open the widget</button>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY}" async></script>
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

### Hoe forceer ik de taal van het formulier?

Standaard wordt **de browsertaal** gebruikt. Als de taal niet beschikbaar is in de widgetvertalingen, wordt automatisch de standaardtaal geselecteerd. Je kunt de huidige taal van de widget afdwingen door de eigenschap **data-lang** toe te voegen aan de div waarin het formulier wordt weergegeven.

In dit voorbeeld wordt standaard de Italiaanse taal geselecteerd (indien beschikbaar)_

```html
<div id="customer-subject-popup" data-lang="it"></div>
```



### Hoe stuur ik formulierwaarden automatisch naar de widget?

```html
<script>
  dastra.push(['set','dsr:refId','{your custom userId}'])
</script>
```

U kunt de kolomnaam **refId** vervangen door de volgende eigenschapsnaam:&#x20;

* refId : de unieke identifier van de gebruiker
* familyName&#x20;
* givenName
* email
* stad
* postcode
* landcode
* adres
* telefoonnummer
* bericht
* additionalDatas**\***

\*In het specifieke geval van aangepaste velden, moet je verwijzen naar de naam additionalDatas :

```html
<script>
  var payload = {
    customFieldSlug1: 'test', 
    customFieldSlug2: 'test'.
  };
  
  // U kunt deze synthax gebruiken voor het instellen van globale aangepaste velden als een object
  dastra.push(['set','dsr:additionalDatas', payload]);
  
   // Of direct voor een enkel veld, gebruik het voorvoegsel @
   dastra.push(['set','dsr:@customFieldSlug1', 'test']);
</script>
```

Extra velden worden automatisch samengevoegd.

### Parameters verzenden met paginamodus

Het is ook mogelijk om deze parameters door te geven met querystringparameters. Zet voor de parameternaam dsr_ :&#x20;

```url
https://api.dastra.eu/v1/client/customer-subject-form?id=<uw widget id>
&key=<uw publieke sleutel>
&dsr_email=test@github.org
&dsr_givenName=Dastonaute
&dsr_refId=123456
&...etc...
```

### Sluit de widget door buiten het venster te klikken

Als je widget is geconfigureerd met een **"Popup"** weergavetype, hebben we het gedrag van het sluiten van het modale venster in het geval van een klik buiten het venster niet geïmplementeerd, omdat de risico's van het verlies van door de gebruiker ingevoerde gegevens te groot zijn.

Als je echter wilt dat de widget wordt gesloten wanneer de gebruiker buiten de widget klikt, kan dit worden geïmplementeerd met de volgende code:&#x20;

```javascript
window.dastra.customerSubjectReady().then((form) => { 
  form.closeOnBackdrop = true; 
});
```

{% hint style="warning" %}
Waarschuwing: hierdoor wordt alle door de gebruiker ingevoerde tekst verwijderd zonder waarschuwing! Als het formulier lang is, kan dit gemakkelijk gebeuren als een selectie verder gaat dan een lang tekstveld.
{% endhint %}