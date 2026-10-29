---
description: >-
  Cette page vous explique comment mettre en place le SSO de Dastra avec
  Microsoft Entra ID (Active Directory) en utilisant le protocole SAML 2
---

# Active Directory (Microsoft Entra ID)

Découvrez dans le guide vidéo comment configurer le SSO Active Directory (Microsoft Entra ID) pas à pas :

{% embed url="https://www.youtube.com/embed/SUC_J489wjI?si=VPoD5nAxG_i1-AEp" %}

## Configuration de l'application dans Microsoft Entra ID

* Rendez-vous dans le centre d'administration Microsoft Entra : [https://entra.microsoft.com](https://entra.microsoft.com)
* Dans la navigation à gauche, cliquez sur **Entra ID** > **Enterprise apps**
* Cliquez sur **New application**, puis sur **Create your own application**
* Renseignez le nom de l'application, par exemple « Dastra »
* Sélectionnez **Integrate any other application you don't find in the gallery (Non-gallery)**, puis créez l'application
* Dans la section **Manage**, cliquez sur **Single sign-on** et sélectionnez **SAML**
* Vous arrivez sur cette page :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-saml-configuration.png" alt="La page de configuration SAML d'une application d'entreprise Microsoft Entra ID"><figcaption></figcaption></figure>

## Configuration du client SSO dans Dastra

### Étape 1 : créez un login SSO SAML dans Dastra

* Allez sur la [page de configuration du SSO de Dastra](https://app.dastra.eu/general-settings/sso) (**Configuration de l'organisation** > **Single sign on**)
* Cliquez sur **Ajouter un login SSO**
* Sélectionnez **SAML2** dans **Choisir le protocole SSO**, puis **Configuration manuelle**
* Saisissez un intitulé de connexion dans **Intitulé de la connexion SSO**, par exemple « Active Directory »

### Étape 2 : configurez le login SSO dans Microsoft Entra ID

* Retournez sur la page de configuration SAML de Microsoft Entra ID
* Cliquez sur **Edit** dans la section **Basic SAML Configuration**
* Saisissez les informations de connexion, affichées en haut du formulaire SAML de Dastra : **Identifier (Entity ID)** et **Reply URL (Assertion Consumer Service URL)** :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-saml-basic-config.png" alt="La section Basic SAML Configuration avec l'identifiant et l'URL de réponse"><figcaption></figcaption></figure>

* Cliquez sur **Save**
* Allez directement à la section **SAML Certificates** pour **télécharger le certificat au format Base64** :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-saml-certificate-download.png" alt="La section SAML Certificates avec le lien de téléchargement du certificat Base64"><figcaption></figcaption></figure>

* Ouvrez le fichier CER avec un éditeur de texte (par exemple le Bloc-notes) et copiez le contenu (Ctrl + C) :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-certificate-content.png" alt="Le contenu du certificat ouvert dans un éditeur de texte"><figcaption></figcaption></figure>

### Étape 3 : ajoutez le certificat au client Dastra

* Retournez dans l'écran de création de la connexion SAML dans Dastra
* Collez le texte du certificat (Ctrl + V) dans le champ **Identity Provider Certificate (RAW)**

### Étape 4 : configurez les URL du fournisseur d'identité dans Dastra

* Dans la section **Set up** de l'application Entra ID, copiez les trois valeurs **Login URL**, **Microsoft Entra Identifier** et **Logout URL** :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-app-urls.png" alt="La section Set up de l'application avec les trois URL à copier"><figcaption></figcaption></figure>

* Collez-les dans Dastra en respectant la correspondance suivante :
  * **Login URL** : **Fournisseur d'identité (Identity Provider) single sign on url**
  * **Microsoft Entra Identifier** : **Identity Provider's Entity id (issuer)**
  * **Logout URL** : **Identity Provider Signout url**
* Le formulaire de configuration du SSO dans Dastra doit ressembler à ceci :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-dastra-idp-configuration.png" alt="Le formulaire SAML de Dastra rempli avec les valeurs de Microsoft Entra ID"><figcaption></figcaption></figure>

* Vous pouvez activer l'option **Utilisateur créé si l'utilisateur n'a jamais été invité dans Dastra**, dans la section **Création automatique des utilisateurs**. Dans ce cas, les comptes de votre annuaire qui n'existent pas encore dans Dastra sont créés au moment de la première connexion :

<figure><img src="../../../.gitbook/assets/settings-sso-entra-auto-create-user-option.png" alt="L'option de création automatique des utilisateurs dans le formulaire SSO"><figcaption></figcaption></figure>

* Enregistrez vos changements dans Dastra

{% hint style="info" %}
Avant de lancer le test de la connexion, assurez-vous qu'un utilisateur est bien assigné à la nouvelle application.
{% endhint %}

### Testez votre connexion SSO

Dans Microsoft Entra ID, cliquez sur le bouton **Test** de la section **Test single sign-on** de l'application. Si tout fonctionne, vous êtes redirigé vers Dastra.

{% hint style="info" %}
Si vous n'avez pas activé la création automatique des utilisateurs, l'accès est refusé côté Dastra tant que le compte local n'a pas été créé par une invitation.
{% endhint %}

### Pour aller plus loin

{% content-ref url="known-problems.md" %}
[Problèmes connus](known-problems.md)
{% endcontent-ref %}

{% content-ref url="saml.md" %}
[SAML 2](saml.md)
{% endcontent-ref %}
