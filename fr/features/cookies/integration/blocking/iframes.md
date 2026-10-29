---
description: >-
  De nombreux sites ont recours aux iframes pour afficher des vidéos, des tweets, etc. Il faut donc demander le consentement des utilisateurs avant de charger le contenu de l'iframe.
---

# Blocage des iframes (twitter/youtube...)

## Exemples de services qui utilisent des iframes

* Lecteurs vidéo : YouTube, Vimeo, Dailymotion, etc.
* Réseaux sociaux : Twitter, Facebook, etc.
* Lecteurs de podcasts.
* Lecteurs audio.

## Méthode 1 : utiliser le SDK

Le SDK bloque les iframes de la page ciblées par un sélecteur et affiche à la place un message de blocage personnalisable :

<figure><img src="../../../../.gitbook/assets/cookies-video-consent-overlay.png" alt="Un message de blocage affiché à la place d'une vidéo YouTube, avec le bouton I accept"><figcaption><p>Le message de blocage à la place de la vidéo</p></figcaption></figure>

Un clic sur le bouton du message enregistre automatiquement le consentement au service concerné et charge l'iframe. Si le visiteur retire ensuite son consentement à ce service, l'iframe est bloquée de nouveau. Le message ne propose qu'un bouton d'acceptation.

Exemple avec une iframe de lecteur vidéo YouTube :

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/aJ1qDx8lv2Y" allowfullscreen></iframe>
<script>
  // Set up youtube iframe blocking
  dastra.push(['iframeBlock', {
    selector: 'iframe[src*="youtube.com"]',
    service: 'youtube', // service slug (check your banner configuration)
    body: '<p>By clicking on "I accept" the trackers will be deposited and you will be able to view the video. You can withdraw your consent at any time :</p>',
    buttonLabel: 'I accept',
    buttonClass: 'btn btn-primary',
    footer: '<p>Consents provided by <a href="https://www.dastra.eu">Dastra</a></p>'
  }])
</script>
```

Les options de `iframeBlock` sont :

| Option | Rôle |
| --- | --- |
| `selector` | Sélecteur CSS des iframes à bloquer. |
| `service` | Identifiant (slug) du service dont le consentement débloque l'iframe. |
| `body` | Texte HTML du message de blocage. |
| `buttonLabel` | Libellé du bouton d'acceptation. |
| `buttonClass` | Classes CSS du bouton. |
| `footer` | Texte HTML affiché sous le bouton. |

{% hint style="info" %}
Vous pouvez adapter l'apparence du message (fond, polices, etc.) avec votre feuille de style CSS. Le message de blocage est intégré à la page avec la classe `.datra-blocking-iframe`.
{% endhint %}

## Méthode 2 : implémentation manuelle

Vous pouvez aussi implémenter votre propre logique :

```html
<script>
  // Select all youtube iframes
  var iframes = document.querySelectorAll('iframe[src*="youtube.com"]');

  // For each iframe, disable it by moving the "src" attribute to "data-blocked-src"
  iframes.forEach(function (iframe) {
    var iframeSrc = iframe.getAttribute('src');
    iframe.setAttribute('data-blocked-src', iframeSrc);
    iframe.setAttribute('src', 'about:blank');
    var divAlert = document.createElement('div');
    divAlert.classList.add('alert-iframe-cookie');
    divAlert.innerHTML = '<p>En cliquant sur « J’accepte », les traceurs seront déposés et vous pourrez visualiser la vidéo. Vous pouvez retirer votre consentement à tout moment.</p><div class="button-container"><button type="button" onclick="SetConsent(\'youtube\', true)" class="btn btn-success">J’accepte</button></div><p>Consentements fournis par <a href="https://www.dastra.eu">Dastra</a></p>';
    iframe.after(divAlert);
  });

  // On consent, load the iframes and hide the message
  window.addEventListener('dastra:consent:youtube', function () {
    document.querySelectorAll('iframe[data-blocked-src*="youtube.com"]').forEach(function (iframe) {
      iframe.setAttribute('src', iframe.getAttribute('data-blocked-src'));
      iframe.removeAttribute('data-blocked-src');
    });

    document.querySelectorAll('.alert-iframe-cookie').forEach(function (alert) {
      alert.style.display = 'none';
    });
  });

  function SetConsent(service, consent) {
    dastra.cookieConsent.consent.setServiceConsent(service, consent);
    dastra.cookieConsent.consent.save();
  }
</script>
<style>
  .alert-iframe-cookie {
    background-color: #ccc;
    padding: 20px;
    color: #333;
    text-align: center;
  }

  .button-container {
    margin: 10px auto;
  }
</style>
```
