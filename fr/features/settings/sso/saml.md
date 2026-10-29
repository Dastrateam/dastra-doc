---
description: Détails de la configuration de SAML 2
---

# SAML 2

La configuration du SSO avec SAML 2 se fait en trois étapes :

* configuration du fournisseur d'authentification (**Identity Provider - IdP**) : Active Directory, Google Workspace, etc. ;
* configuration du fournisseur de service (**Service Provider - SP**) : Dastra ;
* test de l'authentification.

Dans le cas spécifique **des serveurs ADFS**, consultez notre documentation spécifique :

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## 1. Configuration du fournisseur d'authentification

Vous devez mettre en place une configuration SAML dans votre fournisseur d'authentification.

* Pour AD FS : voir la page [ADFS](adfs.md).
* Pour Microsoft Entra ID (anciennement Azure AD) : voir la page [Active Directory (Microsoft Entra ID)](entra-id.md) et la [documentation de Microsoft](https://learn.microsoft.com/fr-fr/entra/identity/enterprise-apps/add-application-portal-setup-sso).
* Pour Google : [https://support.google.com/a/answer/6087519?hl=fr](https://support.google.com/a/answer/6087519?hl=fr)

Pour faire le rapprochement entre les comptes locaux (ceux hébergés dans Dastra), vous avez besoin de fournir une propriété contenant l'e-mail de l'utilisateur (par défaut, Dastra va chercher la propriété nommée [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)). Vous pouvez changer ce nom dans le champ **Le nom du claim contenant l'adresse email**.

Voici les informations dont vous avez besoin pour renseigner le fournisseur de service :

* **Identity Provider's Entity id** (issuer) ;
* **Single sign on url** ;
* **le certificat au format RAW** (encodé en base64).

Pour configurer votre fournisseur d'authentification, vous avez besoin des informations suivantes, affichées en haut du formulaire SAML de Dastra :

* **Issuer** : par défaut `https://www.dastra.eu` ;
* **SP Redirect URI** (ACS) : `https://account.dastra.eu/{identifiant de la connexion}/Acs`. Cette URL est propre à chaque connexion : copiez-la en haut du formulaire SAML lors de l'ajout du login SSO dans Dastra (étape 2), puis enregistrez ce login ;
* **SP start url (Sign on URL)**, si votre fournisseur demande une URL de connexion pour l'application ;
* **SAML Logout url (facultatif)**, si votre fournisseur gère la déconnexion.

## 2. Configuration du fournisseur de service

Dans Dastra, ouvrez [la page d'administration du SSO](https://app.dastra.eu/general-settings/sso) (**Configuration de l'organisation** > **Single sign on**, réservée aux propriétaires de l'organisation) et cliquez sur **Ajouter un login SSO**. Choisissez le protocole **SAML2**.

<figure><img src="../../../.gitbook/assets/settings-sso-liste-logins.png" alt="La page Single sign on avec la liste des logins SSO et le bouton Ajouter un login SSO"><figcaption></figcaption></figure>

Choisissez ensuite comment fournir la configuration de votre fournisseur d'identité :

* **Téléversez votre manifeste de configuration SAML (.xml)** : importez le fichier de métadonnées (manifeste XML) fourni par votre fournisseur. Dastra remplit les champs du formulaire à partir de ce fichier. Cliquez sur le bouton de retour pour changer de méthode.
* **Configuration manuelle** : renseignez les champs vous-même.

<figure><img src="../../../.gitbook/assets/settings-sso-saml-upload-manifest.png" alt="Choix entre l'import du manifeste SAML et la configuration manuelle"><figcaption></figcaption></figure>

En configuration manuelle, renseignez les champs du formulaire à l'aide des informations de votre fournisseur d'authentification :

<figure><img src="../../../.gitbook/assets/settings-sso-saml-config-form.png" alt="Formulaire de configuration manuelle d'un login SSO SAML dans Dastra"><figcaption></figcaption></figure>

{% hint style="danger" %}
Vous pouvez forcer tous les utilisateurs de l'organisation à utiliser un SSO particulier (option **Forcer pour tous les utilisateurs**). Soyez prudent : si le SSO dysfonctionne, vous ne pourrez plus accéder à votre compte en tant qu'administrateur. Gardez un compte local de secours, ou exemptez des utilisateurs avec le champ **Utilisateurs spécifiques exemptés de SSO (par exemple, les administrateurs de sécurité)** (voir [Single Sign On (SSO)](README.md)). Il est préférable de gérer le SSO par utilisateur.
{% endhint %}

{% hint style="warning" %}
**Cas particulier des utilisateurs externes**\
Seuls les comptes internes à un abonnement sont soumis au SSO. Les comptes d'utilisateurs externes (qui ont un autre abonnement supplémentaire) ne sont pas soumis au SSO.
{% endhint %}

## 3. Tester le SSO

Une fois la configuration terminée, testez l'authentification en cliquant sur **Tester**, à droite de la connexion dans la liste. Si vous rencontrez un problème, ouvrez un ticket depuis la [page du support](https://app.dastra.eu/general-settings/support).

<figure><img src="../../../.gitbook/assets/settings-sso-saml-provider-card.png" alt="Une connexion SSO SAML dans la liste, avec son statut et le bouton Tester"><figcaption></figcaption></figure>
