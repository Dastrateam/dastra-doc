---
description: >-
  Cette page vous explique comment mettre en place la configuration SCIM de
  Dastra avec Microsoft Entra ID (anciennement Azure Active Directory)
---

# SCIM

## Principe de fonctionnement

[Le SCIM](http://www.simplecloud.info/), acronyme anglais de System for Cross-domain Identity Management (comprenez « Système de gestion des identités interdomaines ») est une norme ouverte prenant en charge l'automatisation du provisioning des utilisateurs. Le protocole SCIM est un intermédiaire, il collecte les données relatives à l'identité des utilisateurs auprès des fournisseurs d'identité (Microsoft Entra ID, Google Workspace, Okta...) et les communique aux prestataires de service ayant besoin de ces informations d'identification (comme Dastra).

{% hint style="warning" %}
La fonctionnalité de SCIM est réservée aux clients avec un **plan Entreprise.**

[Consultez notre page tarif](https://www.dastra.eu/pricing)
{% endhint %}

{% hint style="info" %}
Nous vous recommandons fortement d'effectuer préalablement [la mise en place du SSO ](sso/README.md)**avec l'option Forcer pour tous les utilisateurs activée**.
{% endhint %}

## Configurer SCIM avec Microsoft Entra ID

Les utilisateurs de Dastra peuvent être ajoutés, supprimés et modifiés à l'aide de SCIM 2.0. Vous définissez des groupes dans Entra ID et Dastra synchronise ces utilisateurs automatiquement, sans intervention manuelle.

### 1. Connectez-vous au portail Microsoft Entra

Rendez-vous sur [https://entra.microsoft.com](https://entra.microsoft.com) et connectez-vous avec un compte administrateur.

### 2. Accédez à Enterprise applications

Dans le menu de gauche, cliquez sur **Entra ID** > **Enterprise applications** > **All applications**.

### 3. Cliquez sur New application

En haut de la liste des applications, cliquez sur **New application**.

### 4. Créez votre propre application

Sur la page **Browse Microsoft Entra App Gallery**, cliquez sur **+ Create your own application**.

### 5. Nommez et configurez votre application

Dans le panneau qui s'ouvre :

1. Entrez un nom pour votre application (ex. : **Dastra SCIM**)
2. Sélectionnez l'option **Integrate any other application you don't find in the gallery (Non-gallery)**
3. Cliquez sur **Create**

### 6. Accédez à la configuration du provisioning

Dans la page **Overview** de l'application nouvellement créée, cliquez sur **3. Provision User Accounts** ou sur **Provisioning** dans le menu de navigation gauche.

### 7. Récupérez l'URL SCIM et le jeton depuis Dastra

Avant de configurer Entra, récupérez vos credentials SCIM dans Dastra.

**Connectez-vous à Dastra** en tant que propriétaire de l'organisation. Allez dans **Paramètres de l'organisation** > [**Single sign on**](https://app.dastra.eu/general-settings/sso) > **SCIM**

![](../../.gitbook/assets/settings-scim-azure-app-menu-scim.png)

Cliquez sur le bouton **Configurer** pour créer une nouvelle configuration SCIM.

<figure><img src="../../.gitbook/assets/settings-scim-dastra-new-config-modal.png" alt="Modale de création d&#x27;une configuration SCIM dans Dastra"><figcaption><p>Sélectionnez l'espace de travail cible et le rôle par défaut</p></figcaption></figure>

Sélectionnez l'**espace de travail** à synchroniser (équipes et utilisateurs y seront automatiquement provisionnés) et le **rôle par défaut** attribué aux nouveaux utilisateurs. Les rôles restent modifiables localement par les administrateurs Dastra.

Cliquez sur **Enregistrer**, puis **copiez l'URL SCIM et le jeton d'authentification** affichés.

{% hint style="info" %}
Dastra permet de synchroniser **un seul espace de travail par organisation** via SCIM.
{% endhint %}

### 8. Configurez le provisioning automatique dans Entra

De retour dans Entra, sur la page de provisioning de votre application :

1. Réglez le **Provisioning Mode** sur **Automatic**
2. Dans la section **Admin Credentials**, renseignez :
   * **Tenant URL** : l'URL SCIM copiée depuis Dastra
   * **Secret Token** : le jeton d'authentification copié depuis Dastra
<figure><img src="../../.gitbook/assets/settings-scim-azure-provisioning-credentials.png" alt="Page de provisioning Entra avec le mode Automatic et les champs Tenant URL et Secret Token"><figcaption><p>Les champs Tenant URL et Secret Token dans Entra</p></figcaption></figure>

3. Cliquez sur **Test Connection** pour vérifier la connexion
4. Cliquez sur **Save**

Si vous rencontrez une erreur lors du test de connexion, vérifiez que la fonctionnalité SCIM est bien activée sur votre souscription. [Contactez le support si besoin](../../getting-started/support/request.md)

### 9. Activez le provisioning

Une fois la configuration sauvegardée, activez le provisioning en réglant le statut sur **On** et en cliquant sur **Save**.

<figure><img src="../../.gitbook/assets/settings-scim-azure-provisioning-toolbar.png" alt="Barre d&#x27;état du provisioning Entra avec le bouton On/Off"><figcaption><p>Activez le provisioning en passant le statut sur « On »</p></figcaption></figure>

### 10. Ajoutez des utilisateurs et/ou des groupes

Dans le menu de navigation de l'application, cliquez sur **Users and groups**, puis assignez les utilisateurs ou groupes Entra que vous souhaitez synchroniser avec Dastra.

<figure><img src="../../.gitbook/assets/settings-scim-azure-users-groups.png" alt="Page Users and groups de l&#x27;application Entra"><figcaption><p>Assignez les utilisateurs et groupes à synchroniser avec Dastra</p></figcaption></figure>

## Laissez vos utilisateurs se connecter

Vous devriez voir les comptes utilisateurs de votre annuaire Entra se synchroniser automatiquement dans Dastra. Si le SSO n'est pas configuré et forcé, les utilisateurs devront effectuer une réinitialisation de mot de passe pour leur première connexion. Si le SSO est actif et forcé pour tous les utilisateurs, ils seront automatiquement redirigés vers le formulaire de connexion de votre fournisseur d'identité (Microsoft Entra ID, Google Workspace, Okta…)

## Comportements et limitations de la synchronisation SCIM

### Gestion du cycle de vie des utilisateurs

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
* L’utilisateur apparaît comme **deleted user**

**Impact sur les données associées :**

* Les objets liés (ex : traitements, risques, demandes, etc.) **ne sont pas supprimés**
* Les relations (ex : propriétaire, assignation) **sont conservées**
* Seule l’identité de l’utilisateur est anonymisée

***

### Gestion des groupes (teams)

**Suppression d’un groupe dans Entra ID**

Si un groupe est supprimé dans Entra ID :

* L'équipe **correspondante est supprimée dans Dastra**
* Les **utilisateurs ne sont pas supprimés**
* Aucun impact sur leurs comptes individuels

***

### Mapping et périmètre de synchronisation

**Groupes et espaces de travail**

* SCIM permet de synchroniser **plusieurs groupes**
* Limitation actuelle :
  * Synchronisation possible vers **un seul espace de travail par organisation**
  * Le multi-workspace n’est **pas supporté**

***

**Attributs synchronisés**

Actuellement, Dastra synchronise :

* pour les utilisateurs : identifiant de connexion, prénom et nom, adresse e-mail, statut actif, langue et adresse postale (pays, ville, code postal, région) ; la liste complète figure dans [Quels attributs et claims sont pris en charge ?](#quels-attributs-et-claims-sont-pris-en-charge) ;
* pour les groupes : le **nom (`displayName`)**, l'identifiant du groupe (`externalId`) et les **membres**.

Non supporté à ce jour :

* Mapping vers des **unités organisationnelles**
* Les attributs de l'extension entreprise (organisation, service, matricule, manager…) : les fournisseurs d'identité les envoient par défaut, Dastra les accepte sans les enregistrer.

> Une évolution est possible via l’ajout d’un attribut spécifique contenant un identifiant exploitable côté Dastra.

***

### Gestion locale après synchronisation

Après synchronisation SCIM :

* Les administrateurs peuvent toujours :
  * **modifier les rôles**
  * **ajuster les permissions**
* La gestion fine des accès reste **possible localement dans Dastra**

***

### Impact sur la licence

* La synchronisation SCIM est limitée par :
  * le **nombre d’utilisateurs inclus dans votre abonnement**
* Si le quota est dépassé :
  * Le serveur SCIM retourne une **erreur `403`** de type `limitExceeded`
  * Les utilisateurs supplémentaires ne sont **pas provisionnés**

***

## Endpoints SCIM et découverte

L'API SCIM de Dastra expose les endpoints standard SCIM 2.0, tous servis sous votre URL SCIM et authentifiés par le jeton SCIM (les requêtes sans jeton valide reçoivent un `401`) :

| Endpoint | Rôle |
| --- | --- |
| `/v2/Users` | Créer, lire, mettre à jour (PATCH) et supprimer les utilisateurs |
| `/v2/Groups` | Créer, lire, mettre à jour (PATCH) et supprimer les groupes (équipes Dastra) |
| `/v2/ServiceProviderConfig` | Déclare les capacités du service SCIM |
| `/v2/ResourceTypes` | Liste les types de ressources (User, Group) |
| `/v2/Schemas` | Définition attribut par attribut de chaque schéma pris en charge |

Les mises à jour passent par `PATCH` ; le remplacement complet d'une ressource par `PUT` n'est pas pris en charge. Une création réussie (`POST`) renvoie `201` avec un en-tête `Location` et un attribut `meta.location` qui donnent l'URL de la nouvelle ressource.

Les trois **endpoints de découverte** (RFC 7644 §4) sont en lecture seule. Les fournisseurs d'identité et connecteurs SCIM (Microsoft Entra ID, Okta, connecteurs sur mesure, etc.) les interrogent pour construire automatiquement le schéma d'attributs, sans fichier de schéma manuel. `/v2/Schemas` décrit exactement les attributs que Dastra lit et écrit : c'est la liste de référence, et un attribut qui n'y figure pas est ignoré par la synchronisation. `ServiceProviderConfig` répond aussi sur les alias courants `/v2/ServiceProviderConfigs` et `/v2/ServiceProviderConfiguration`, les connecteurs divergeant sur son nom.

Capacités déclarées par `ServiceProviderConfig`, conformes au comportement réel de l'API :

* **Pris en charge** : opérations PATCH, filtrage (voir la limite ci-dessous).
* **Non pris en charge** : opérations bulk, tri, etags, changement de mot de passe.

### Filtrage

Un filtre porte sur **une seule condition**, avec l'opérateur `eq` (égal) ou `ne` (différent), sur l'un de ces attributs :

| Ressource | Attributs filtrables |
| --- | --- |
| Utilisateurs | `userName`, `externalId`, `emails.value` |
| Groupes | `displayName`, `externalId` |

Exemple : `filter=userName eq "jane.doe@entreprise.com"`. Les noms d'attributs ne tiennent pas compte de la casse.

{% hint style="info" %}
Dastra ne répond jamais à un filtre qu'il ne sait pas évaluer exactement. Un autre opérateur (`co`, `sw`, `gt`…), un autre attribut ou plusieurs conditions combinées par `and` / `or` renvoient une erreur `400` de type `invalidFilter` qui nomme le problème.
{% endhint %}

### Opérations PATCH

`PATCH` accepte les trois formes envoyées par les fournisseurs d'identité : une opération avec un `path` et une valeur simple, une opération avec un `path` et une valeur objet, et une opération sans `path` dont la valeur liste les attributs à modifier. Les opérations `add`, `replace` et `remove` sont prises en charge.

* **Utilisateurs** : les attributs listés par `/v2/Schemas` sont appliqués. Les attributs que Dastra n'enregistre pas (extension entreprise, numéros de téléphone, fonction, etc.) sont acceptés et ignorés, pour que les mappings par défaut de Microsoft Entra ID et d'Okta fonctionnent sans modification. Le `userName` et l'adresse e-mail ne peuvent pas être retirés. Passer `active` à `false` désactive l'utilisateur, comme décrit plus haut.
* **Groupes** : `displayName` et `externalId` sont modifiables. Les membres peuvent être ajoutés (`add`), remplacés en bloc (`replace`) ou retirés (`remove`), tous d'un coup ou un par un avec le chemin `members[value eq "<id utilisateur>"]`.

Un utilisateur qui n'appartient pas à votre organisation est signalé comme introuvable (`404`).

### Erreurs

Les erreurs suivent le format SCIM (RFC 7644 §3.12) : un corps JSON avec `status`, `scimType` et un message `detail` qui dit ce qui a été refusé.

| Code | Cas |
| --- | --- |
| `400` | Requête invalide : valeur absente ou mal formée (`invalidValue`), filtre non pris en charge (`invalidFilter`), chemin inconnu (`invalidPath`), attribut qui ne peut pas être retiré (`mutability`)… |
| `401` | Jeton SCIM absent ou invalide |
| `403` | Quota d'utilisateurs de votre abonnement atteint (`limitExceeded`) |
| `404` | Ressource introuvable, ou qui n'appartient pas à votre organisation |
| `409` | Un utilisateur ou un groupe avec le même identifiant existe déjà (`uniqueness`) |

***

## Foire aux questions

### Quel est le rôle du SCIM dans Dastra ?

SCIM est le canal de **provisioning automatisé** entre votre annuaire d’entreprise (Entra ID, Okta, Google Workspace, etc.) et Dastra. Son rôle est complémentaire de celui du SSO, et distinct :

|                   | SSO                          | SCIM                                                 |
| ----------------- | ---------------------------- | ---------------------------------------------------- |
| **Rôle**          | Authentification (connexion) | Gestion du cycle de vie des comptes                  |
| **Déclencheur**   | Connexion de l’utilisateur   | Action dans l’IdP (ajout, modification, suppression) |
| **Ce qu’il fait** | Vérifie l’identité           | Crée, met à jour, désactive les comptes              |
| **Protocole**     | SAML 2 / OpenID Connect      | SCIM 2.0 (HTTP REST + JSON)                          |

Grâce au SCIM, vous n’avez pas à créer manuellement les comptes dans Dastra ni à les révoquer en cas de départ : votre annuaire reste la **source de vérité** pour la gestion des identités.

{% hint style="info" %}
Le SCIM gère **qui existe** dans Dastra. Le SSO gère **comment ces personnes se connectent**. Les deux sont indépendants mais se combinent idéalement : provisionnez via SCIM, authentifiez via SSO.
{% endhint %}

***

### Quel est le fonctionnement global du provisioning et déprovisioning ?

#### Provisioning (création de compte)

Lorsqu’un utilisateur ou un groupe est assigné à l’application Dastra dans votre IdP :

1. L’IdP envoie une requête **`POST /scim/v2/Users`** à l’endpoint Dastra
2. Dastra crée le compte avec le rôle par défaut configuré dans la configuration SCIM
3. L’utilisateur est rattaché à l’espace de travail cible
4. Si le SSO est activé et forcé, l’utilisateur peut se connecter immédiatement sans mot de passe

#### Mise à jour

Toute modification du profil dans l’IdP (nom, e-mail, langue, adresse) déclenche une requête **`PATCH /scim/v2/Users/{id}`** qui met à jour le compte correspondant dans Dastra. Un changement d'appartenance à un groupe déclenche une requête **`PATCH /scim/v2/Groups/{id}`** qui ajoute ou retire les membres de l'équipe correspondante.

#### Déprovisioning (désactivation / suppression)

| Action dans l’IdP              | Requête SCIM                  | Effet dans Dastra                                    |
| ------------------------------ | ----------------------------- | ---------------------------------------------------- |
| Désactivation de l’utilisateur | `PATCH` (`active: false`)     | Profil **anonymisé**                                 |
| Suppression définitive         | `DELETE /scim/v2/Users/{id}`  | Profil **entièrement anonymisé**, données conservées |
| Suppression d’un groupe        | `DELETE /scim/v2/Groups/{id}` | Équipe supprimée, utilisateurs inchangés             |

{% hint style="warning" %}
La réactivation d’un utilisateur précédemment anonymisé crée un **nouveau compte** : l’historique de l’ancien compte n’est pas restauré.
{% endhint %}

***

### Quels attributs et claims sont pris en charge ?

#### Attributs SCIM synchronisés (provisioning)

Lors de la synchronisation, Dastra lit les attributs SCIM 2.0 suivants. `/v2/Schemas` renvoie la même liste.

**Utilisateurs**

| Attribut SCIM | Champ dans Dastra | Obligatoire |
| --- | --- | --- |
| `userName` | Identifiant de connexion, unique dans votre organisation (en général l'adresse e-mail) | Oui |
| `emails` | Adresse e-mail. Dastra conserve une seule adresse : l'entrée marquée `primary`, à défaut la première | Oui |
| `name.givenName` | Prénom | Recommandé |
| `name.familyName` | Nom | Recommandé |
| `active` | Statut actif / inactif | Oui |
| `locale` | Langue (ex. `en`, `fr-FR`) | Facultatif |
| `address` | Pays (code à deux lettres), ville, code postal, région (une seule adresse) | Facultatif |
| `externalId` | Lecture seule : renvoie toujours la même valeur que `userName`. Utilisable dans un filtre ; une valeur envoyée par le fournisseur d'identité est ignorée | Sans objet |
| `nickName` | Accepté à la création, jamais renvoyé | Facultatif |

**Groupes**

| Attribut SCIM | Champ dans Dastra | Obligatoire |
| --- | --- | --- |
| `displayName` | Nom de l'équipe (30 caractères maximum) | Oui |
| `externalId` | Identifiant du groupe dans le fournisseur d'identité | Facultatif |
| `members` | Membres de l'équipe (identifiants des utilisateurs Dastra) | Facultatif |

{% hint style="info" %}
Dastra conserve un seul identifiant de provisioning par utilisateur, le `userName`. Modifier le `userName` d'un utilisateur dans le fournisseur d'identité le met à jour dans Dastra ; lorsque le compte a été provisionné avec son adresse e-mail comme `userName`, l'adresse e-mail suit le changement.
{% endhint %}

#### Claims SSO exploités lors de la connexion

Lors de la connexion, Dastra identifie l’utilisateur via le claim e-mail transmis par l’IdP. Les deux protocoles SSO supportés utilisent la même propriété :

| Protocole      | Claim e-mail utilisé                                                 | Scope requis           |
| -------------- | -------------------------------------------------------------------- | ---------------------- |
| SAML 2         | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | Aucun                  |
| OpenID Connect | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | `openid profile email` |

{% hint style="warning" %}
L’e-mail est le **point de jonction** entre SCIM et SSO : le `userName` provisionné via SCIM doit être **identique** au claim e-mail renvoyé lors de la connexion SSO. Toute divergence empêchera le rapprochement de compte.
{% endhint %}

Pour la configuration complète des claims SSO, consultez la page [Single Sign On (SSO)](sso/README.md).
