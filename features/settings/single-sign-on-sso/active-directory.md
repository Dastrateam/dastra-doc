---
description: >-
  Cette page vous explique comment mettre en place le SSO de Dastra avec
  l'Active Directory de Microsoft en utilisant le protocole Saml2P
---

# Active Directory

## **Configuration de l'application dans le portail azure**

* Rendez-vous dans le portail Microsoft Azure : [https://portal.azure.com](https://portal.azure.com)
* Cliquez sur **Active Directory**
* Dans la navigation à gauche, cliquez sur Entreprise Applications
* Cliquez sur le bouton **New application**
* Cliquez ensuite sur **Create your own application**
* Renseigner le nom de l'application, vous pouvez mettre tout simplement "Dastra"
* Sélectionnez la case "**Integrate any other application you don't find in the gallery (Non-gallery)**"
* Votre application est créée !
* Cliquez sur **Single-Sign-On** et sélectionnez **SAML**
* **Vous arrivez sur cette page**

![](<../../../.gitbook/assets/image (8).png>)



## **Configuration du client SSO dans Dastra**

**Etape 1 : Créez un login SSO OpenId dans Dastra.**

* Allez sur la [page de configuration du SSO de Dastra](https://app.dastra.eu/general-settings/sso)
* Cliquez sur "Ajouter un login SSO"
* Sélectionnez **SAML** en type de "**Protocole du SSO**"
* Saisissez un label de connexion. Par exemple "Active Directory"

**Etape 2 : Configurez le login SSO dans Active Directory**

* Retournez sur la page de configuration SAML de l'Active Directory
* **Cliquez sur le bouton "Edit"** de la première partie.
* Saisissez les informations de connexion (**Entity ID et Url ACS**) de la manière suivante :

![](<../../../.gitbook/assets/image (3) (1) (1).png>)

* Cliquez sur **Enregistrer**
* Allez directement dans la partie 3 afin de **télécharger le certificat au format base64**
* ![](<../../../.gitbook/assets/image (5) (1).png>)
* **Ouvrez le fichier CER avec votre éditeur de texte préféré** (par exemple le bloc note) et copiez le contenu (CTRL + C)
* ![](<../../../.gitbook/assets/image (4) (1).png>)

**Etape 3 : Ajouter le certificat au client Dastra**

* Retournez dans l'écran de création de connexion SAML dans Dastra
* **Collez le texte du certificat** dans le champ "Identity Provider Certificate (RAW)" (CTRL + V)

**Etape 4 : Configurez les url de l'IdP dans Dastra**

* Copiez les 3 liens Entity Id, SSO Url et Logout Url depuis l'étape 4 de Active Directory
* ![](<../../../.gitbook/assets/image (7) (1) (1).png>)
* Copiez les urls en respectant le schéma suivant :\
  **Login URL => Single sign on url** \
  **Azure AD Identifier => Identity provider's Entity Id** \
  **Logout Url => Identity provider Signout url**
* Votre formulaire de configuration du SSO dans Dastra devrait ressembler à ceci :
* ![](<../../../.gitbook/assets/image (2) (1) (1).png>)
* Vous pouvez cocher la case "Utilisateur créé si l'utilisateur n'a jamais été invité dans Dastra" . Si vous activez cette option, les comptes de votre organisation AD qui ne sont pas présents dans Dastra seront provisionnés à la volée au moment du login si ils n'existent pas localement dans Dastra.

![](<../../../.gitbook/assets/image (6).png>)

* **Enregistrez vos changements** dans Dastra

{% hint style="info" %}
Avant de lancer le test de la connexion assurez vous qu'un utilisateur est bien assigné à la nouvelle application.
{% endhint %}

### Testez votre connexion SSO

Cliquez ensuite sur le bouton "Test" au pied du formulaire dans l'active directory. Si tout fonctionne correctement vous devriez être redirigé vers l'application Dastra.&#x20;

{% hint style="info" %}
Si vous n'avez pas activé **le provisionnement automatique** des comptes, l'accès sera refusé du côté de Dastra si le compte local n'a pas été créé via une invitation
{% endhint %}

### Pour aller plus loin

{% content-ref url="problemes-connus.md" %}
[problemes-connus.md](problemes-connus.md)
{% endcontent-ref %}

{% content-ref url="saml-2.md" %}
[saml-2.md](saml-2.md)
{% endcontent-ref %}
