---
description: >-
  Cette page vous explique comment mettre en place la configuration SCIM de
  Dastra avec un annuaire d'entreprise du type Azure Active Directory (Cloud)
---

# SCIM

### Principe de fonctionnement

[Le SCIM](http://www.simplecloud.info/), acronyme anglais de System for Cross-domain Identity Management (comprenez « Système de gestion des identités interdomaines ») est une norme ouverte prenant en charge l'automatisation du provisioning des utilisateurs. Le protocole SCIM est un intermédiaire, il collecte les données relatives à l'identité des utilisateurs auprès des fournisseurs d'identité (Azure AD, Google Workspace, Okta...) et les communique aux prestataires de service ayant besoin de ces informations d'identification (comme Dastra).



{% hint style="warning" %}
La fonctionnalité de SCIM est réservée aux clients avec un **plan Entreprise.**

[Consultez notre page tarif](https://www.dastra.eu/pricing)
{% endhint %}

{% hint style="info" %}
Nous vous recommandons fortement d'effectuer préalablement [la mise en place du SSO ](single-sign-on-sso/)**avec l'option "Forcer pour tous les utilisateurs" activée**.&#x20;
{% endhint %}

### Comment configurer SCIM avec Azure Active Directory ?

Les utilisateurs de Dastra peuvent être ajoutés, supprimés et modifiés à l'aide de SCIM 2.0.&#x20;

Vous définissez des groupes dans votre Azure Directory et Dastra peut synchroniser ces utilisateurs. C'est un moyen idéal de gagner du temps et d'éviter les tracas liés à la gestion des comptes d'utilisateurs. Il s'agit également d'une mise en œuvre idéale de la sécurité.

#### 1. Connectez vous à Azure et cliquez sur Azure Active Directory

<figure><img src="https://www.reftab.com/img/faq/01-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 2. Allez dans "Entreprise applications"

<figure><img src="https://www.reftab.com/img/faq/02-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 3. Cliquez sur "New application,"

<figure><img src="https://www.reftab.com/img/faq/03-azure.png" alt="03-Azure-SCIM"><figcaption></figcaption></figure>

#### 4. Cliquez sur "Create your own application"

<figure><img src="https://www.reftab.com/img/faq/04-azure.png" alt="04-Azure-SCIM"><figcaption></figcaption></figure>

#### 5. Nommez votre application

<figure><img src="../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

#### 6. Dans l'application nouvellement créée, cliquez sur le bouton "Provision User Accounts"

<figure><img src="https://www.reftab.com/img/faq/06-azure.png" alt="06-Azure-SCIM"><figcaption></figcaption></figure>

#### 7. Cliquez sur "Get Started"

<figure><img src="https://www.reftab.com/img/faq/07-azure.png" alt="07-Azure-SCIM"><figcaption></figcaption></figure>

#### 8. Réglez le mode de provisionnement sur automatique. Remplissez l'URL du locataire et le jeton secret à partir des informations contenues dans votre compte Dastra.

**Connectez vous à Dastra** en tant qu'administrateur. **Allez dans la configuration de l'organisation** > **cliquez sur Sécurité / SCIM**

![](<../../.gitbook/assets/image (14) (1).png>)



Cliquez sur le bouton **configurer**

<figure><img src="../../.gitbook/assets/image (18) (2).png" alt=""><figcaption></figcaption></figure>

Configurez votre SCIM. Sélectionnez l'espace de travail que vous souhaitez synchroniser (les équipes et utilisateurs seront automatiquement provisionés dans cet espace).

Choisissez ensuite le rôle par défaut que vous souhaitez donner aux nouveaux utilisateurs. A noter que les rôles seront managés en local par l'administrateur du compte Dastra.

Cliquez sur **Enregistrer**

**Copiez le jeton d'authentification et l'Url SCIM**

{% hint style="info" %}
Aujourd'hui, Dastra vous permet de synchroniser en SCIM (équipes + utilisateurs) **un seul espace de travail par organisation**.&#x20;
{% endhint %}

<figure><img src="../../.gitbook/assets/image (12) (2).png" alt=""><figcaption></figcaption></figure>

Cliquez sur "**Tester la connection**" et "**Enregistrer**". Si vous rencontrez une erreur lors du test de connexion, cela peut provenir d'une absence de fonctionnalité activé au niveau de votre souscription. [Contactez alors le support](../../getting-started/le-support/faire-une-demande-de-support.md)

#### 9. Activez le provisioning de l'application

<figure><img src="../../.gitbook/assets/image (10) (2).png" alt=""><figcaption></figcaption></figure>

#### 10. Ajoutez des utilisateurs et/ou des groupes à l'application créée&#x20;

<figure><img src="../../.gitbook/assets/image (9) (3).png" alt=""><figcaption></figcaption></figure>



### Laissez vos utilisateurs se connecter

Vous devriez voir les comptes utilisateurs de votre AD se synchroniser automatiquement dans Dastra. Si ils se connectent à Dastra via [la page de connexion](https://app.dastra.eu/login), ils devraient pouvoir se connecter avec leur e-mail. Si le SSO n'est pas configuré et forcé pour tous les utilisateurs, les utilisateurs devront faire une réinitialisation de mot de passe pour se connecter. Si le SSO est actif et qu'il est forcé pour tous les utilisateurs, ceux-ci seront automatiquement redirigés vers le formulaire de connexion de votre fournisseur d'identité (Azure AD, Google Workspace, Okta...)



### Comportements et limitations de la synchronisation SCIM

#### Gestion du cycle de vie des utilisateurs

**Désactivation dans Entra ID**

Lorsqu’un utilisateur est désactivé dans Entra ID :

* Son profil est **anonymisé dans Dastra**
* S’il est réactivé par la suite :
  * **Un nouveau compte utilisateur est créé**
  * L’ancien compte anonymisé n’est pas restauré

***

**Suppression complète dans Entra ID**

Lorsqu’un utilisateur est supprimé définitivement dans Entra ID :

* Son profil est **entièrement anonymisé dans Dastra**
* Toutes les actions réalisées sont **conservées**
* L’utilisateur apparaît comme **"deleted user"**

**Impact sur les données associées :**

* Les objets liés (ex : traitements, risques, demandes, etc.) **ne sont pas supprimés**
* Les relations (ex : propriétaire, assignation) **sont conservées**
* Seule l’identité de l’utilisateur est anonymisée

***

#### Gestion des groupes (teams)

**Suppression d’un groupe dans Entra ID**

Si un groupe est supprimé dans Entra ID :

* L'équipe **correspondante est supprimée dans Dastra**
* Les **utilisateurs ne sont pas supprimés**
* Aucun impact sur leurs comptes individuels

***

#### Mapping et périmètre de synchronisation

**Groupes et workspaces**

* SCIM permet de synchroniser **plusieurs groupes**
* Limitation actuelle :
  * Synchronisation possible vers **un seul workspace par organisation**
  * Le multi-workspace n’est **pas supporté**

***

**Attributs synchronisés**

Actuellement, Dastra synchronise :

* Le **nom des groupes (`displayName`)**

Non supporté à ce jour :

* Mapping vers des **unités organisationnelles**
* Synchronisation d’attributs comme :
  * organisation
  * pays

> Une évolution est possible via l’ajout d’un attribut spécifique contenant un identifiant exploitable côté Dastra.

***

#### Gestion locale après synchronisation

Après synchronisation SCIM :

* Les administrateurs peuvent toujours :
  * **modifier les rôles**
  * **ajuster les permissions**
* La gestion fine des accès reste **possible localement dans Dastra**

***

#### Impact sur la licence

* La synchronisation SCIM est limitée par :
  * le **nombre d’utilisateurs inclus dans votre abonnement**
* Si le quota est dépassé :
  * Le serveur SCIM retourne une **erreur**
  * Les utilisateurs supplémentaires ne sont **pas provisionnés**
