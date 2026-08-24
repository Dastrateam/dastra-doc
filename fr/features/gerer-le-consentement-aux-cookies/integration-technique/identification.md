---
description: >-
  Cette page explique comment remonter les identifiants internes de
  l'organisation dans les preuves de consentement
---

# Identification des utilisateurs

## Principe de fonctionnement

Le principe est le suivant : vous envoyez l'**identifiant unique de l'utilisateur authentifié** dans votre intranet au widget dastra et celui-ci enverra cet id lors de la collecte du consentement de l'utilisateur. Il sera ainsi possible de rapprocher les preuves de consentements de la base des clients (CRM, base client, référentiel client ou autres...). Une fois dans l'espace de visualisation des preuves de consentement, l'identifiant de l'utilisateur poussé s'affichera.

## Etape 1 : Choisir l'identifiant de l'utilisateur

Pour faire ce rapprochement, il vous faudra choisir une variable à transférer au widget. Vous pouvez utiliser l'adresse email hashée en base64 de l'utilisateur, un identifiant client interne ou de CRM. Cette variable doit être disponible dans la page web et sera passée en clair. Elle ne doit pas mentionner d'information personnelle sur l'utilisateur (nom, prénom, email en clair). &#x20;

{% hint style="info" %}
&#x20;Si vous envoyez une chaîne encodée en base64, celle-ci sera automatiquement décodée à la réception des consentements de l'utilisateur dans la base Dastra
{% endhint %}

## Etape 2 : Adapter le code d'intégration

```markup
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array's initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent',
    userId: {The userId's variable (email 64bits hash or whatever...)}
}]);
</script>
```

Vous pouvez également utiliser la méthode "set"

```markup
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array's initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent'
}]);

// Push the userId to dastra's cookies
// It must be pushed after the loadCookieConsent method
dastra.push(['set','cookie:userId',{The userId's variable (email 64bits hash or whatever...)}])
</script>
```
