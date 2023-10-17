---
description: >-
  De nombreux sites ont recours aux iframes pour afficher des vidéos, des
  tweets... Il est donc nécessaire de demander le consentement aux utilisateurs
  avant de charger le contenu de l'iframe.
---

# Blocage des iframes (twitter/youtube...)

## Exemples de services utilisant des iframes

Lecteurs vidéos :  Youtube, Vimeo, DailyMotion...

Réseaux sociaux : Twitter, Facebook,...

Lecteurs de podcasts&#x20;

Lecteurs audios &#x20;

## Méthode 1 : En utilisant le SDK

Notre SDK vous permettra de bloquer toutes les iframes de la page en affichant  un message de blocage personnalisable :

![](<../../../../.gitbook/assets/image (184).png>)

En cliquant sur "I accept" le consentement au service spécifique sera automatiquement dispatché. Le système permet également de capturer un refus des cookies dans la CMP Dastra.

Un exemple simple avec les iframes de lecteurs de vidéo youtube :

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
Il sera possible de personnaliser l'apparence du message (fond, polices...) avec votre feuille css. Le message de blocage est intégré au DOM de la page avec une classe ".datra-blocking-iframe".&#x20;
{% endhint %}

## Méthode 2 : Implémentation manuelle&#x20;

vous pouvez également implémenter votre propre logique

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

Voilà
