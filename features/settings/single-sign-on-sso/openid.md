---
description: Configuration d'une connexion SSO utilisant le protocole OpenId
---

# OpenId

## Principe de fonctionnement

Les spécification de OpenId se trouve [ici](https://openid.net/connect/)

![](<../../../.gitbook/assets/image (119).png>)



La configuration du SSO avec OpenID se fait en trois étapes&#x20;

* Configuration du fournisseur d'authentification : Active Directory, Google Workspace...
* Configuration du fournisseur de service : Dastra
* Tests de l'authentification

## 1. Configuration du fournisseur d'authentification

Vous devez mettre en place une configuration OpenId dans votre fournisseur d'authentification.

Pour active directory : [https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc](https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc)

Pour faire le rapprochement entre les comptes locaux (ceux hébergés dans Dastra), vous avez besoin de fournir une propriété contenant l'email de l'utilisateur (par défaut, Dastra va chercher la propriété nommée  [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Voici les informations dont vous avez besoin pour configurer le service provider :&#x20;

* **Authority/domain (ex: https://account.oauth.sso.com)**
* **Id du client : ClientId**&#x20;
* **Secret key**
* **Response Type, par défaut id\_token**
* **Scope : par défaut "openid profile email"**

Pour configurer votre fournisseur d'authentification, vous allez avoir besoin des informations suivantes :

* **The provided Redirect URI in this format : https://account.dastra.eu/signin-{schemeId}**

## 2. Configuration du fournisseur de service

Dans dastra.eu, rendez-vous su[r la page d'administration du SSO](https://app.dastra.eu/general-settings/sso) et cliquez sur "ajouter un login SSO"

![](<../../../.gitbook/assets/image (116).png>)

Renseignez les champs du formulaire à l'aide des infos de la configuration de l'entité :

![](<../../../.gitbook/assets/image (123).png>)

{% hint style="danger" %}
Il est possible de forcer tous les utilisateurs du compte d'abonnement à utiliser un SSO particulier (en cochant la case "forcer les utilisateurs à utiliser ce SSO"). Il faut faire attention avant d'activer cette option. Car si le SSO dysfonctionne, vous ne pourrez plus accéder à votre compte en tant qu'administrateur. Il est préférable de gérer le SSO par utilisateur.
{% endhint %}

{% hint style="warning" %}
**Cas particuliers des utilisateurs externes**\
Seuls les comptes qui sont internes à un abonnement seront soumis au SSO. Les comptes d'utilisateurs externes (qui ont un autre abonnement supplémentaire) ne seront pas soumis au SSO.
{% endhint %}

## 3. Tester le SSO avec OpenId

Une fois que la configuration est terminée, vous pouvez tester l'authentification en cliquant sur le bouton tester en bas à droite. Si vous rencontrez un problème lors de la configuration du SSO, n'hésitez pas à vous rapprocher du support en vous rendant sur la page de [gestion des tickets support](https://app.dastra.eu/general-settings/support).

![](<../../../.gitbook/assets/image (122).png>)
