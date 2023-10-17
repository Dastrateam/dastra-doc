---
description: Dastra vous permet d'activer l'authentification forte des utilisateurs
---

# Authentification forte

## Introduction

Dastra utilise la technologie [TOTP ](https://en.wikipedia.org/wiki/Time-based\_One-time\_Password\_algorithm)pour gérer l'[authentification multi-facteurs](https://fr.wikipedia.org/wiki/Double\_authentification) des utilisateur.\
Les utilisateurs pourront ainsi se logger à la fois avec leur mot de passe habituel et un code à 6 chiffres fournie par une application de stockage de secrets telles que Microsoft Authenticator ou Google Authenticator (Ou autres...)

## Comment activer l'authentification forte ?

* Rendez-vous dans https://app.dastra.eu/general-settings/two-factor
* Cliquez sur "**activer l'authentification forte**"
* Télécharger une application d'authentification à 2 facteurs
* **Scannez le qr code** avec l'appli que vous avez choisi

![](<../.gitbook/assets/image (103).png>)

* Stocker le code de récupération quelque part.&#x20;
* Connectez vous en utilisant le code à 6 chiffres fourni par votre application d'authentification

![Exemple d'application d'authentification](<../.gitbook/assets/image (104).png>)

{% hint style="warning" %}
Conservez précieusement le code de récupération ! Celui-ci vous permettra de récupérer votre compte si vous égarez votre application d'authentification. Votre compte sera verrouillé définitivement si vous ne pouvez fournir ce code. Il faudra alors vous rapprocher de le propriétaire de votre organisation pour qu'il réinitialise l'authentification à 2 facteurs de votre compte.
{% endhint %}

## Comment forcer tous les utilisateurs à utiliser l'authentification forte ?

* Rendez-vous sur https://app.dastra.eu/general-settings/security
* Cocher la case d'activation forcée de l'authentification à 2 facteurs.

{% hint style="info" %}
L'ensemble des utilisateurs qui se connecteront ne pourrons pas accéder à l'application sans avoir configuré l'authentification à 2 facteurs sur leur compte. Veillez à ce que votre équipe soit bien avertie des bonnes pratiques de stockage des clés secrètes TOTP.
{% endhint %}



