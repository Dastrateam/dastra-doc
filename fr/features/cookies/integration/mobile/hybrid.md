---
description: Intégrer la bannière de cookies Dastra dans une application hybride.
---

# Applications hybrides

Une application hybride affiche des pages web dans une WebView. Le SDK fonctionne alors comme sur un site internet.

1. Insérez le code de la bannière, copié depuis la section **Installation**, dans les pages chargées par la WebView. Voir [Démarrage rapide](../quickstart/README.md).
2. Ajoutez l'adresse de ces pages dans **Urls autorisées (CORS)**, section **Configuration** de la bannière. Sans cela, la bannière ne s'affiche pas.
3. Pour rapprocher une preuve de consentement d'un utilisateur de l'application, transmettez son identifiant pseudonyme. Voir [Identification des utilisateurs](../identification.md).
4. Pour lire ou modifier le consentement depuis votre code, utilisez l'API JavaScript du SDK. Voir [Gérer le consentement programmatiquement](../programmatic-consent.md).
5. Ajoutez dans l'application un moyen de rouvrir la bannière, avec `dastra.openCookieConsent()`.

Il reste à configurer manuellement les traceurs de l'application. Voir [Blocage des cookies](../blocking/README.md).
