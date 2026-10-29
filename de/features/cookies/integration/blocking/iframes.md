---
description: >-
  Viele Websites nutzen Iframes, um Videos, Tweets usw. anzuzeigen. Deshalb müssen Sie die Nutzer um ihre Einwilligung bitten, bevor der Inhalt des Iframes geladen wird.
---

# Iframe-Blockierung (Twitter/YouTube...)

## Beispiele für Dienste, die Iframes nutzen

* Videoplayer: YouTube, Vimeo, Dailymotion usw.
* Soziale Netzwerke: Twitter, Facebook usw.
* Podcast-Player.
* Audioplayer.

## Methode 1: Das SDK verwenden

Das SDK blockiert die Iframes der Seite, die einem Selektor entsprechen, und zeigt stattdessen eine anpassbare Blockierungsmeldung an:

<figure><img src="../../../../.gitbook/assets/cookies-video-consent-overlay.png" alt="Eine Blockierungsmeldung anstelle eines YouTube-Videos, mit der Schaltfläche I accept"><figcaption><p>Die Blockierungsmeldung anstelle des Videos</p></figcaption></figure>

Ein Klick auf die Schaltfläche der Meldung erfasst automatisch die Einwilligung in den Dienst und lädt das Iframe. Zieht der Besucher seine Einwilligung in diesen Dienst später zurück, wird das Iframe erneut blockiert. Die Meldung bietet nur eine Schaltfläche zum Akzeptieren.

Ein Beispiel mit Iframes des YouTube-Videoplayers:

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

Die Optionen von `iframeBlock` sind:

| Option | Zweck |
| --- | --- |
| `selector` | CSS-Selektor der zu blockierenden Iframes. |
| `service` | Kennung (Slug) des Dienstes, dessen Einwilligung das Iframe freigibt. |
| `body` | HTML-Text der Blockierungsmeldung. |
| `buttonLabel` | Beschriftung der Schaltfläche zum Akzeptieren. |
| `buttonClass` | CSS-Klassen der Schaltfläche. |
| `footer` | HTML-Text unterhalb der Schaltfläche. |

{% hint style="info" %}
Sie können das Aussehen der Meldung (Hintergrund, Schriftarten usw.) mit Ihrem CSS-Stylesheet anpassen. Die Blockierungsmeldung wird der Seite mit der Klasse `.datra-blocking-iframe` hinzugefügt.
{% endhint %}

## Methode 2: Manuelle Umsetzung

Sie können auch Ihre eigene Logik umsetzen:

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
    divAlert.innerHTML = '<p>By clicking on "I accept" the trackers will be deposited and you will be able to view the video. You can withdraw your consent at any time.</p><div class="button-container"><button type="button" onclick="SetConsent(\'youtube\', true)" class="btn btn-success">I accept</button></div><p>Consents provided by <a href="https://www.dastra.eu">Dastra</a></p>';
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
