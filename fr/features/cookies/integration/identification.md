---
description: >-
  Cette page explique comment remonter les identifiants internes de
  l'organisation dans les preuves de consentement.
---

# Identification des utilisateurs

## Principe de fonctionnement

Vous envoyez l'**identifiant unique de l'utilisateur authentifié** de votre intranet à la bannière Dastra, qui transmet cet identifiant lors de la collecte du consentement. Vous pouvez ainsi rapprocher les preuves de consentement de votre base clients (CRM, référentiel client, etc.). L'identifiant transmis s'affiche dans l'espace de consultation des preuves de consentement.

## Étape 1 : choisir l'identifiant de l'utilisateur

Pour faire ce rapprochement, choisissez un identifiant pseudonyme à transmettre à la bannière, par exemple l'identifiant interne du client ou son identifiant dans votre CRM. Cette variable doit être disponible dans la page web et est transmise en clair : elle ne doit contenir aucune donnée personnelle directe (nom, prénom, adresse e-mail), même encodée en base64, un encodage réversible.

## Étape 2 : adapter le code d'intégration

```html
<div id="cookie-consent"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY HERE}" async></script>
<script>

// Dastra's array initialization
window.dastra = window.dastra || [];

// Load the cookie consent in page
dastra.push(['loadCookieConsent', {
    widgetId: {Paste your widgetId here (digit)},
    selector: '#cookie-consent',
    userId: '{your user pseudonymous id}'
}]);
</script>
```

{% hint style="info" %}
Selon la région d'hébergement de votre organisation, l'adresse du script change (`cdn-bleu.dastra.eu` au lieu de `cdn.dastra.eu`). Reprenez l'adresse du code copié depuis la section **Installation** de la bannière.
{% endhint %}
