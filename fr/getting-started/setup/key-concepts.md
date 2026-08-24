# Les notions importantes

Avant de commencer à utiliser Dastra, il est essentiel de bien comprendre les notions fondamentales qui structurent la plateforme.\
Elles vous permettront d’organiser efficacement vos traitements, vos équipes et vos responsabilités.

***

### 📚 Sommaire

* [Organisation](key-concepts.md#organisation)
* [Espace de travail](key-concepts.md#espace-de-travail)
* [Unité organisationnelle](key-concepts.md#unite-organisationnelle)
* [Entité](key-concepts.md#entite)
* [Département](key-concepts.md#departement)
* [Propriétaire de l’organisation](key-concepts.md#proprietaire-de-lorganisation)

***

### 🏢 Organisation

Une **organisation** regroupe les comptes et utilisateurs liés à votre abonnement Dastra.\
C’est la structure “racine” qui contient l’ensemble de vos espaces de travail, vos paramètres de facturation et vos clés API.

Vous pouvez voir le nom de votre organisation en haut à droite de l’interface, sous votre profil utilisateur.

{% hint style="info" %}
Une organisation peut contenir plusieurs **espaces de travail**, chacun dédié à un projet, une entité ou une équipe différente.\
Un utilisateur peut appartenir à plusieurs organisations.
{% endhint %}

***

### 🧰 Espace de travail

Un **espace de travail** (workspace) est l’environnement dans lequel vous collaborez avec votre équipe.\
Il regroupe les modules et données liés à vos entités : traitements, audits, risques, violations, demandes d’exercice de droits, etc.

Vous sélectionnez votre espace de travail à la connexion via les **tuiles d’accès** affichées sur votre tableau d’accueil.

{% hint style="info" %}
Pensez à nommer vos espaces de travail de manière claire (ex. “Conformité Groupe”, “Entités France”).\
Cela facilite la navigation et la gestion multi-entités.
{% endhint %}

***

### 🧩 Unité organisationnelle

Les **unités organisationnelles** vous permettent de structurer votre workspace selon votre organisation interne.\
Elles servent à regrouper les entités, départements, utilisateurs et traitements dans une logique hiérarchique.

Chaque unité peut contenir :

* des **entités** (structures juridiques),
* des **départements** (équipes internes),
* des **utilisateurs**,
* des **traitements** ou **tâches**.

{% hint style="info" %}
Les unités organisationnelles facilitent la délégation, la gouvernance et la traçabilité dans les projets de conformité.\
Elles servent souvent de référence pour les rapports ou les autorisations d’accès.
{% endhint %}

***

### 🏛️ Entité

Une **entité** correspond généralement à une **personne morale** ou un **responsable de traitement** (ex. une société, une filiale, une association).\
C’est le niveau auquel vous rattachez les traitements et les informations juridiques clés.

Chaque entité peut contenir :

* les coordonnées du **responsable du traitement**,
* le **DPO** (délégué à la protection des données),
* les **autorités de contrôle** concernées,
* et les **départements** rattachés.

Exemple :

> Entité : _Dastra France SAS_\
> Département : _Marketing_\
> DPO : _Jean Dupont_ :::

***

### 🧭 Département

Un **département** représente un service ou une division d’une entité (ex. RH, IT, Marketing, Juridique).\
Il permet d’affiner la répartition des activités au sein d’une même entité et de suivre les responsabilités par équipe.

Les départements servent notamment à :

* filtrer les traitements ou audits par périmètre,
* assigner des tâches ou demandes à un groupe ciblé,
* mieux visualiser les flux d’information internes.

{% hint style="info" %}
Les départements sont optionnels, mais fortement recommandés pour les organisations de taille moyenne à grande.\
Ils facilitent la gestion des responsabilités et le suivi opérationnel.
{% endhint %}

***

### 👑 Propriétaire de l’organisation

Le **propriétaire** (owner) est l’administrateur principal de l’organisation Dastra.\
Il dispose de l’ensemble des droits de gestion, y compris la création et la suppression d’espaces de travail, la configuration des clés API et la gestion des rôles.

Ses principales responsabilités :

* Gérer les **utilisateurs et équipes** au niveau global,
* Superviser les **espaces de travail**,
* Accéder aux **paramètres avancés** (API, sécurité, facturation),
* Supprimer un compte ou une organisation.

{% hint style="info" %}
Limitez le nombre de propriétaires pour garantir la sécurité et la cohérence de la gouvernance.\
Les autres utilisateurs peuvent se voir attribuer des rôles adaptés (Admin, Contributeur, Lecteur, etc.).
{% endhint %}

***
