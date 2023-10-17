---
description: Détails de la configuration de SAML 2
---

# SAML 2

La configuration du SSO avec SAML 2 se fait en trois étapes&#x20;

* Configuration du fournisseur d'authentification (**Identity Provider - IdP**) : Active Directory, Google Workspace...
* Configuration du fournisseur de service (**Service Provider - SP**) : Dastra
* Tests de l'authentification

Dans le cas spécifique **des serveurs ADFS**, consultez notre documentation spécifique :&#x20;

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## 1. Configuration du fournisseur d'authentification

Vous devez mettre en place une configuration SAML dans votre fournisseur d'authentification.

Pour AD FS : [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings)

Pour Azure AD : [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad)

Pour Google : [https://support.google.com/a/answer/6087519?hl=fr](https://support.google.com/a/answer/6087519?hl=fr)

Pour faire le rapprochement entre les comptes locaux (ceux hébergés dans Dastra), vous avez besoin de fournir une propriété contenant l'email de l'utilisateur (par défaut, Dastra va chercher la propriété nommée  [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Voici les informations dont vous avez besoin pour configurer le service provider :&#x20;

* **Identity Provider's Entity id** (issuer)
* **Single sign on url**
* **Le certificat au format RAW** (Encodé base64)

Pour configurer votre fournisseur d'authentification, vous allez avoir besoin des informations suivantes :

* **Issuer** : par défaut "https://www.dastra.eu"
* **SP Redirect URI** : par défaut [https://account.dastra.eu/Saml2/Acs](https://localhost:44375/Saml2/Acs)

## 2. Configuration du fournisseur de service

Dans dastra.eu, rendez-vous su[r la page d'administration du SSO](https://app.dastra.eu/general-settings/sso) et cliquez sur "ajouter un login SSO"

![](<../../../.gitbook/assets/image (116).png>)

Renseignez les champs du formulaire à l'aide des infos de la configuration de l'entité :

![](<../../../.gitbook/assets/image (117).png>)

{% hint style="danger" %}
Il est possible de forcer tous les utilisateurs du compte d'abonnement à utiliser un SSO particulier (en cochant la case "forcer les utilisateurs à utiliser ce SSO"). Il faut faire attention avant d'activer cette option. Car si le SSO dysfonctionne, vous ne pourrez plus accéder à votre compte en tant qu'administrateur. Il est préférable de gérer le SSO par utilisateur.
{% endhint %}

{% hint style="warning" %}
**Cas particuliers des utilisateurs externes**\
Seuls les comptes qui sont internes à un abonnement seront soumis au SSO. Les comptes d'utilisateurs externes (qui ont un autre abonnement supplémentaire) ne seront pas soumis au SSO.
{% endhint %}

## 3. Tester le SSO

Une fois que la configuration est terminée, vous pouvez tester l'authentification en cliquant sur le bouton tester en bas à droite. Si vous rencontrez un problème lors de la configuration du SSO, n'hésitez pas à vous rapprocher du support en vous rendant sur la page de [gestion des tickets support](https://app.dastra.eu/general-settings/support).

![](<../../../.gitbook/assets/image (121).png>)
