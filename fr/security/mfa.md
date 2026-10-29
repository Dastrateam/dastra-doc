---
description: >-
  Activez l'authentification forte (code à 6 chiffres) pour votre compte, ou
  rendez-la obligatoire pour les utilisateurs de votre organisation.
---

# Authentification forte

Dastra utilise la technologie [TOTP](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm) pour gérer l'[authentification multifacteur](https://fr.wikipedia.org/wiki/Double_authentification) des utilisateurs. Ils se connectent avec leur mot de passe habituel et un code à 6 chiffres fourni par une application d'authentification, telle que Microsoft Authenticator ou Google Authenticator.

Cette page explique comment activer l'authentification forte sur votre compte, puis comment la rendre obligatoire pour les utilisateurs de votre organisation.

## Activer l'authentification forte sur votre compte

1. Ouvrez le menu de votre profil en haut à droite, cliquez sur **Profil utilisateur**, puis sur **Sécurité du compte** dans le menu de gauche. Vous pouvez aussi ouvrir directement [https://app.dastra.eu/general-settings/account-security](https://app.dastra.eu/general-settings/account-security).
2. Dans la carte **Protéger votre compte avec l'authentification à deux facteurs**, cliquez sur **Activer l'authentification forte**.

<figure><img src="../.gitbook/assets/security-mfa-1.png" alt="Page Sécurité du compte : carte d'authentification à deux facteurs avec le bouton Activer l'authentification forte"><figcaption><p>La carte d'authentification à deux facteurs dans Sécurité du compte</p></figcaption></figure>

3. Sur l'écran **Configuration de l'authentification forte**, installez une application d'authentification sur votre téléphone, si ce n'est pas déjà fait.
4. Scannez le QR code avec l'application. Si elle ne peut pas le scanner, saisissez le code affiché sous le texte.

<figure><img src="../.gitbook/assets/security-mfa-2.png" alt="Écran Configuration de l'authentification forte avec le QR code à scanner"><figcaption><p>L'écran de configuration : le QR code à scanner avec votre application</p></figcaption></figure>

5. Cliquez sur **Continuer**. Dastra affiche alors votre code de restauration : conservez-le dans un endroit sûr.
6. À chaque connexion, saisissez votre mot de passe, puis le **code à 6 chiffres** fourni par votre application.

<figure><img src="../.gitbook/assets/security-mfa-3.png" alt="Exemple d'application d'authentification affichant des codes à 6 chiffres"><figcaption><p>Exemple d'application d'authentification</p></figcaption></figure>

{% hint style="warning" %}
Conservez précieusement le code de restauration. Si vous perdez votre application d'authentification, vous pouvez l'utiliser pour réinitialiser l'authentification forte : sur l'écran de saisie du code, cliquez sur **Impossible de vous connecter ?**. Sans ce code, votre compte reste verrouillé : rapprochez-vous alors du propriétaire de votre organisation pour qu'il réinitialise l'authentification forte de votre compte.
{% endhint %}

## Rendre l'authentification forte obligatoire

Les propriétaires de l'organisation peuvent obliger tous les utilisateurs internes, c'est-à-dire ceux que l'organisation gère, à utiliser l'authentification forte. Cette option fait partie des réglages de sécurité de l'organisation, réservés au plan Enterprise.

1. Ouvrez le menu de votre profil, cliquez sur **Configuration de l'organisation**, puis sur **Sécurité** dans le menu de gauche. Vous pouvez aussi ouvrir directement [https://app.dastra.eu/general-settings/security](https://app.dastra.eu/general-settings/security).
2. Dans la carte **Forcer les utilisateurs à utiliser l'authentification forte (A deux facteurs)**, activez l'interrupteur : il passe à **Actif**.

<figure><img src="../.gitbook/assets/security-mfa-4.png" alt="Réglages de sécurité de l'organisation : carte pour forcer l'authentification forte"><figcaption><p>La carte pour rendre l'authentification forte obligatoire</p></figcaption></figure>

{% hint style="info" %}
À leur prochaine connexion, les utilisateurs concernés ne peuvent pas accéder à l'application tant qu'ils n'ont pas configuré l'authentification forte. Prévenez votre équipe et rappelez les bonnes pratiques de conservation du code de restauration. Une connexion par [passkey](passkey.md) avec vérification de l'utilisateur vaut déjà deux facteurs : elle ne demande pas de code à 6 chiffres.
{% endhint %}
