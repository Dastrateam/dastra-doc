---
description: >-
  Viele Websites verwenden iframes, um Videos, Tweets usw. anzuzeigen. Es ist daher
  notwendig, die Einwilligung der Nutzer einzuholen, bevor der Iframe-Inhalt geladen wird.
---

# Blockierung von iframes (Twitter/YouTube...)

## Beispiele für Dienste, die iframes verwenden

Videoplayer: YouTube, Vimeo, DailyMotion...

Soziale Netzwerke: Twitter, Facebook,...

Podcast-Player&#x20;

Audio-Player&#x20;

## Methode 1: Verwendung des SDK

Unser SDK ermöglicht es Ihnen, alle iframes auf der Seite zu blockieren und eine anpassbare Blockierungsnachricht anzuzeigen:

![](<../../../../.gitbook/assets/image-184.png>)

Durch Klicken auf „I accept" wird die Einwilligung für den spezifischen Dienst automatisch übermittelt. Das System ermöglicht auch die Erfassung einer Cookie-Ablehnung in der Dastra-CMP.

Ein einfaches Beispiel mit YouTube-Videoplayer-iframes:

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
Es ist möglich, das Erscheinungsbild der Nachricht (Hintergrund, Schriftarten...) mit Ihrem CSS-Stylesheet anzupassen. Die Blockierungsnachricht wird im DOM der Seite mit der Klasse „.datra-blocking-iframe" integriert.&#x20;
{% endhint %}

## Methode 2: Manuelle Implementierung&#x20;

Sie können auch Ihre eigene Logik implementieren

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
    divAlert.innerHTML = '<p>En cliquant sur « j'autorise » les traceurs seront déposés et vous pourrez visualiser la vidéo. Vous gardez la possibilité de retirer votre consentement à tout moment. En cliquant sur « je refuse », vous ne pourrez pas accéder à la vidéo. : </p><div class="button-container"><button type="button" onclick="SetConsent(\'youtube\', true)" href="#" class="btn btn-success" >Accept the cookies</button></div><p>Consentements fournis par <a href="https://www.dastra.eu">Dastra</a></p>';
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

Fertig
