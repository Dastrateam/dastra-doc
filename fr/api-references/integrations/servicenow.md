---
description: Intégration ServiceNow pour synchroniser les actifs (assets) dans Dastra
---

# ServiceNow

### Qu'est ce que c'est ServiceNow ?

L’intégration [ServiceNow](https://www.servicenow.com/) permet de **synchroniser automatiquement les applications métiers** issus du CMDB de ServiceNow directement dans Dastra.

Elle permet :

* d’éviter la double saisie ;
* de centraliser les actifs techniques utilisés dans toute l’organisation;
* d’utiliser ces actifs dans vos **registres de traitement**, **jeux de données**, **analyses d’impact**, **analyses de risques**, **audits**, etc.
* de garantir que les informations issues de ServiceNow restent **à jour** dans Dastra.

### Prérequis

* **Avoir une licence payante Dastra** incluant l’accès au module Intégrations / connecteurs.
* **Avoir une instance ServiceNow** (ex. `https://votre-instance.service-now.com`) qui permet l’**appel API REST** depuis l’extérieur, et selon la méthode d’authentification :
  * **OAuth 2.0 (recommandé)** — la possibilité d’enregistrer une application OAuth dans votre instance,
  * **Basic** — un compte de service disposant des droits de lecture sur `cmdb_ci_business_app`.

### Installation

Le processus de mise en place suit le parcours commun des intégrations (voir [Connexions, cas d'usage et mapping des champs](connexions-et-mapping-des-champs.md)) :

1. Accédez à la page de l’intégration **ServiceNow** dans la marketplace d’intégrations Dastra.\
   Exemple :\
   `https://app.dastra.eu/workspace/0/settings/integrations/servicenow`
2. Sur le cas d’usage d’import des actifs, cliquez sur **Ajouter l'intégration**.
3. Ajoutez une connexion et choisissez la **Méthode d'authentification** (voir ci-dessous).
4. Complétez l’étape de **Configuration**. Elle est **obligatoire** pour finaliser l’installation.

<!-- 📸 Capture à refaire : la modale de connexion ServiceNow avec le sélecteur Méthode d'authentification (Basic / OAuth) -->

<figure><img src="../../.gitbook/assets/setupservicenowaccount.png" alt=""><figcaption></figcaption></figure>

### Méthodes d'authentification

**OAuth 2.0 (recommandé)** — Dastra ne stocke jamais de mot de passe ; ServiceNow émet des jetons à durée de vie courte que Dastra renouvelle automatiquement.

1. Dans ServiceNow, créez une app OAuth pour Dastra : **All > Application Registry** (sur les versions récentes : *Inbound integrations > Authorization code grant*), type *OAuth API endpoint for external clients*.
2. Renseignez l’URL de redirection : `https://api.dastra.eu/v1/integrationaccounts/callback/servicenow`
3. Vérifiez que la restriction de scope de l’app est **Broadly scoped** (ou déclarez le scope `useraccount`) : une app *securely scoped* sans scopes refusera l’échange de jetons.
4. Dans Dastra, créez la connexion avec la méthode **OAuth**, saisissez l’**URL de l'instance**, le **Client ID OAuth** et le **Client secret OAuth**, puis cliquez sur **Enregistrer et se connecter** et autorisez Dastra dans ServiceNow.

**Authentification Basic** — identifiant/mot de passe d’un compte ServiceNow, stockés chiffrés par Dastra.

{% hint style="warning" %}
Les instances ServiceNow récentes restreignent l’authentification Basic sur l’API REST au niveau du compte. Si vous utilisez Basic, créez un **compte de service dédié avec « Web service access only » coché** — jamais un compte nominatif ni un compte admin. Symptôme de la restriction : une réponse `401 User is not authenticated` malgré des identifiants valides.
{% endhint %}

### Configuration

* Sélectionnez les **utilisateurs à notifier en cas d'erreur** (obligatoire). Ils recevront un email de notification en cas d’échec de synchronisation, contenant les informations sur les actifs qui ont été mis à jour.
* **Créer l'enregistrement Dastra s'il n'existe pas** — activé, un actif est créé s’il n’existe pas dans Dastra, en se basant sur la référence externe.
* **Dédoublonner les éléments synchronisés** — fait correspondre les applications entrantes aux actifs existants via un **Champ de correspondance** (**Label** ou **Référence**) pour les mettre à jour au lieu de créer des doublons.
* **Mapping des champs** — choisissez quel champ ServiceNow (de `cmdb_ci_business_app`) alimente chaque champ Dastra. Les listes de choix sont lues en direct depuis le dictionnaire de données de votre instance : leurs valeurs peuvent donc être transcodées en valeurs Dastra. Voir [Connexions, cas d'usage et mapping des champs](connexions-et-mapping-des-champs.md).

{% hint style="info" %}
Attention : si vous activez l’option de création, un grand nombre d’actifs seront automatiquement créés dans votre espace de travail. Veillez à bien renseigner les références externes.
{% endhint %}

<!-- 📸 Capture à refaire : le panneau de configuration ServiceNow avec les options et l'éditeur de mapping des champs -->

### Comment sont synchronisées les données entre Dastra et ServiceNow ?

La synchronisation s’exécute automatiquement **une fois par jour**, et peut être déclenchée à tout moment avec **Lancer la synchronisation** sur la carte du cas d’usage. Lors de chaque synchronisation, les champs issus de ServiceNow sont mappés dans votre référentiel d’actifs Dastra. Par défaut, les informations suivantes sont récupérées et mises à jour :

* **Label** de l’actif
* **Description** (Short Description ServiceNow)
* **Type d’application**
* **État / statut d’installation**
* **Type d’actif** (systématiquement importé comme _Software_)
* **Zone / domaine** associé (AreaId)
* **Tags** associés
* **Identifiant externe** ServiceNow (`sys_id`)
* **Source externe** (`ServiceNow`)
* **Date de dernière synchronisation**
* **Propriétaire** de l’actif

Chacun de ces comportements par défaut peut être remplacé champ par champ dans l’éditeur de **Mapping des champs**. Toutes ces données permettent de maintenir un lien fiable et à jour entre votre CMDB ServiceNow et votre référentiel Dastra.

#### Gestion des actifs supprimés côté ServiceNow

Lorsque Dastra détecte qu’un actif précédemment synchronisé **n’existe plus dans ServiceNow**, il **n’est pas supprimé automatiquement** dans Dastra.\
À la place, Dastra ajoute **un tag automatique** (`To-delete-servicenow`) sur l’actif indiquant qu’il est _supprimé dans ServiceNow_. Si l’application réapparaît plus tard dans ServiceNow, le tag est retiré automatiquement.

Ce comportement permet :

* de conserver l’historique dans Dastra,
* d’éviter les suppressions involontaires,
* de faciliter la revue manuelle des actifs obsolètes.

Lorsque le dédoublonnage trouve **plusieurs** actifs correspondant à une même application entrante, les candidats sont marqués `To-merge-servicenow` pour une décision de fusion manuelle.
