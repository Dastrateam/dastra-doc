---
description: >-
  Veel sites gebruiken iframes om video's, tweets, enz. weer te geven.
  tweets... Het is daarom noodzakelijk om gebruikers om toestemming te vragen
  voordat de iframe-inhoud wordt geladen.
---

# Iframes blokkeren (twitter/youtube...)

## Voorbeelden van diensten die iframes gebruiken

Videospelers: Youtube, Vimeo, DailyMotion, enz.

Sociale netwerken: Twitter, Facebook, enz.

Podcast spelers &#x20;

Audiospelers &#x20;

## Methode 1: De SDK gebruiken

Met onze SDK kun je alle iframes op de pagina blokkeren door een aanpasbaar blokkeerbericht weer te geven:

![](<../../../../.gitbook/assets/image (184).png>)

Door op "Ik accepteer" te klikken wordt automatisch toestemming gegeven voor de specifieke dienst. Het systeem maakt het ook mogelijk om een weigering van cookies vast te leggen in het Dastra CMP.

Een eenvoudig voorbeeld met youtube video player iframes:

```markup
<iframe width="560" height="315" src="https://www.youtube.com/embed/aJ1qDx8lv2Y" allowfullscreen></iframe>
<script>
  // Set up youtube iframe blocking
  dastra.push(['iframeBlock', {
    selector: 'iframe[src*="youtube.com"]',
    service: 'youtube', // service slug (Check your Dastra cmp config)
    body:'<p>By clicking on "I accept" the trackers will be deposited and you will be able to view the video. You can withdraw your consent at any time :</p>',
    buttonLabel:'I accept',
    buttonClass: 'btn btn-primary'
  }])
</script>
```

{% hint style="info" %}
Het is mogelijk om het uiterlijk van het bericht (achtergrond, lettertypen...) aan te passen met je css-sheet. Het blokkeringsbericht wordt geïntegreerd in de pagina DOM met een ".datra-blocking-iframe" klasse.&#x20;
{% endhint %}

## Methode 2: Handmatige implementatie&#x20;

Je kunt ook je eigen logica implementeren

```markup
<script>
  // Select all youtube iframes 
  var iframes = document.querySelectorAll('iframe[src*="youtube.com"]');

  // Foreach iframe disable the iframe by transforming "src" attribute to "data-blocked-src"
  iframes.forEach(function(iframe){
    var iframeSrc = iframe.getAttribute('src');
    iframe.setAttribute('data-blocked-src', iframeSrc );
    iframe.setAttribute('src','about:blank');
    var divAlert = document.createElement('div');
    divAlert.classList.add('alert-iframe-cookie')
    divAlert.innerHTML = '<p>En cliquant sur « j’autorise » les traceurs seront déposés et vous pourrez visualiser la vidéo. Vous gardez la possibilité de retirer votre consentement à tout moment. En cliquant sur « je refuse », vous ne pourrez pas accéder à la vidéo. : </p><div class="button-container"><button type="button" onclick="SetConsent(\'youtube\', true)" href="#" class="btn btn-success" >Accept the cookies</button></div><p>Consentements fournis par <a href="https://www.dastra.eu">Dastra</a></p>';
    iframe.after(divAlert);
  });

  // On cookie consent, 
  window.addEventListener('dastra:consent:youtube', function() {
    // Load iframe when accepted
    document.querySelectorAll('iframe[data-blocked-src*="youtube.com"]').forEach(function(iframe){
      iframe.setAttribute('src', iframe.getAttribute('data-blocked-src'));
      iframe.removeAttribute('data-blocked-src');
    });
    
    // Delete message when accepted
    document.querySelectorAll('.alert-iframe-cookie').forEach(function(alert){
      alert.style.display = "none";
    });
  });

  function SetConsent(service, consent){
    dastra.cookieConsent.consent.setServiceConsent(service, true);
    dastra.cookieConsent.consent.save();
  };

</script>
<style>
  .alert-iframe-cookie{
    background-color:#CCC;
    padding: 20px 20px;
    color:#fff;
    text-align:center;
  }
  
  .button-container{
    margin: 10px auto; 
  }
  
</style>
```

Hier ben je