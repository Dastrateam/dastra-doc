---
description: >-
  Connectez-vous à Dastra sans mot de passe grâce aux clés d'accès (passkeys),
  basées sur les standards WebAuthn / FIDO2
---

# Clés d'accès (passkeys)

## Introduction

Une **clé d'accès** (ou _passkey_) remplace votre mot de passe par une authentification biométrique ou par code PIN de votre appareil : empreinte digitale, reconnaissance faciale ou code de déverrouillage.

Dastra s'appuie sur les standards ouverts [WebAuthn](https://fr.wikipedia.org/wiki/WebAuthn) et [FIDO2](https://fr.wikipedia.org/wiki/FIDO_Alliance). Concrètement :

* La **clé privée ne quitte jamais votre appareil** (ou votre gestionnaire de clés d'accès : iCloud Keychain, Google Password Manager, Windows Hello, 1Password, YubiKey…). Dastra ne conserve que la clé publique.
* Il n'y a **aucun secret partagé** à voler : une fuite de base de données ne permet pas de se connecter à votre compte.
* La clé d'accès est **liée au domaine de Dastra** : elle est par nature résistante au hameçonnage (_phishing_). Un site frauduleux ne peut pas vous la faire utiliser.

{% hint style="success" %}
Une connexion par clé d'accès avec vérification de l'utilisateur (biométrie ou code PIN) vaut **deux facteurs d'authentification**. Vous n'avez donc pas de code à 6 chiffres à saisir, même si votre organisation impose l'[authentification forte](mfa.md).
{% endhint %}

## Comment créer une clé d'accès ?

Deux chemins sont possibles.

### Depuis vos paramètres de sécurité

* Rendez-vous sur [https://app.dastra.eu/general-settings/account-security](https://app.dastra.eu/general-settings/account-security)
* Dans l'encart **Clés d'accès**, cliquez sur **Gérer**
* Donnez un nom à votre clé (par exemple « Mon téléphone » ou « MacBook pro »), puis cliquez sur **Ajouter une clé d'accès**
* Suivez l'invite de votre navigateur ou de votre système d'exploitation (empreinte, visage, code PIN, clé de sécurité physique…)

### Depuis l'invitation affichée après connexion

Après une connexion par mot de passe, Dastra vous propose de créer une clé d'accès si vous n'en avez pas encore. Vous pouvez :

* **Créer une clé d'accès** immédiatement ;
* choisir **Plus tard** : l'invitation ne sera plus affichée sur ce navigateur pendant 90 jours ;
* choisir **Ne plus me le demander** : l'invitation est désactivée définitivement pour votre compte (vous pourrez toujours créer une clé depuis vos paramètres de sécurité).

## Comment se connecter avec une clé d'accès ?

* Saisissez votre adresse e-mail sur la page de connexion
* Sur l'écran suivant, cliquez sur **Se connecter avec une clé d'accès**

<figure><img src="../.gitbook/assets/security-passkey-login-button.png" alt="Bouton « Se connecter avec une clé d&#x27;accès » sur la page de connexion"><figcaption><p>Le bouton « Se connecter avec une clé d'accès » s'affiche si une clé est enregistrée pour votre compte</p></figcaption></figure>

* Validez avec votre empreinte, votre visage, votre code PIN ou votre clé de sécurité

{% hint style="info" %}
Le bouton n'apparaît que si votre navigateur prend en charge WebAuthn **et** qu'au moins une clé d'accès est enregistrée sur votre compte. Votre mot de passe et la connexion par lien e-mail restent disponibles.
{% endhint %}

## Gérer ses clés d'accès

Depuis l'écran **Gérer** (paramètres de sécurité de votre compte), vous pouvez :

* **enregistrer plusieurs clés d'accès** — c'est recommandé : une par appareil (téléphone, ordinateur portable, clé de sécurité physique) vous évite de perdre l'accès si vous perdez un appareil ;
* **renommer** une clé d'accès ;
* **supprimer** une clé d'accès qui n'est plus utilisée (appareil revendu, perdu, volé).

L'encart **Clés d'accès** de vos paramètres de sécurité affiche également la date de dernière utilisation de chaque clé, ce qui permet d'identifier rapidement une clé obsolète.

{% hint style="info" %}
Si vous ne saisissez pas de nom, la clé est nommée automatiquement avec sa date de création. L'ajout et la suppression d'une clé d'accès sont journalisés et consultables dans les logs d'audit de votre organisation.
{% endhint %}

{% hint style="warning" %}
Si vous supprimez votre dernière clé d'accès alors que votre compte n'a pas de mot de passe, vous ne pourrez plus vous connecter qu'avec un code à usage unique envoyé par e-mail. Une confirmation vous est demandée dans ce cas.
{% endhint %}

## Limites

* Les clés d'accès ne sont **pas disponibles pour les utilisateurs dont l'organisation impose l'authentification unique (SSO)** : ces utilisateurs s'authentifient auprès de leur fournisseur d'identité, qui peut lui-même proposer des clés d'accès.
* Un navigateur ou un système d'exploitation trop ancien peut ne pas prendre en charge WebAuthn. Un message vous en informe le cas échéant.
