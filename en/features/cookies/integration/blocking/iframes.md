---
description: >-
  Many websites use iframes to display videos, tweets, etc. It is therefore necessary to ask users for their consent before loading the content of the iframe.
---

# Blocking iframes (twitter/youtube...)

## Examples of services using iframes

* Video players: YouTube, Vimeo, Dailymotion, etc.
* Social media: Twitter, Facebook, etc.
* Podcast players.
* Audio players.

## Method 1: Using the SDK

The SDK blocks the iframes of the page that match a selector and displays a customizable blocking message instead:

<figure><img src="../../../../.gitbook/assets/cookies-video-consent-overlay.png" alt="A blocking message displayed in place of a YouTube video, with the I accept button"><figcaption><p>The blocking message in place of the video</p></figcaption></figure>

A click on the button of the message automatically records consent to the service and loads the iframe. If the visitor later withdraws consent to this service, the iframe is blocked again. The message offers an acceptance button only.

An example with YouTube video player iframes:

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

The `iframeBlock` options are:

| Option | Purpose |
| --- | --- |
| `selector` | CSS selector of the iframes to block. |
| `service` | Identifier (slug) of the service whose consent unblocks the iframe. |
| `body` | HTML text of the blocking message. |
| `buttonLabel` | Label of the acceptance button. |
| `buttonClass` | CSS classes of the button. |
| `footer` | HTML text displayed under the button. |

{% hint style="info" %}
You can customize the look of the message (background, fonts, etc.) with your CSS stylesheet. The blocking message is added to the page with the `.datra-blocking-iframe` class.
{% endhint %}

## Method 2: Manual implementation

You can also implement your own logic:

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
