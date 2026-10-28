---
description: >-
  Cette page explique comment remonter les identifiants internes de
  l'organisation dans les preuves de consentement
---

# Identification des utilisateurs

## Principe de fonctionnement

Le principe est le suivant : vous envoyez l'**identifiant unique de l'utilisateur authentifié** dans votre intranet au widget dastra et celui-ci enverra cet id lors de la collecte du consentement de l'utilisateur. Il sera ainsi possible de rapprocher les preuves de consentements de la base des clients (CRM, base client, référentiel client ou autres...). Une fois dans l'espace de visualisation des preuves de consentement, l'identifiant de l'utilisateur poussé s'affichera.

## Etape 1 : Choisir l'identifiant de l'utilisateur

Pour faire ce rapprochement, choisissez un identifiant pseudonyme à transmettre au widget, par exemple l'identifiant interne du client ou son identifiant dans votre CRM. Cette variable doit être disponible dans la page web et sera transmise en clair : elle ne doit contenir aucune donnée personnelle directe (nom, prénom, adresse e-mail), même encodée en base64, un encodage réversible.


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
    userId: {your user's pseudonymous id}
}]);
</script>
```
