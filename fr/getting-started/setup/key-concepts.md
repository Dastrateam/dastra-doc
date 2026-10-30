---
description: >-
  Définitions des notions qui structurent Dastra : organisation, espace de travail, unité organisationnelle, entité, département et propriétaire.
---

# Les notions importantes

Avant de commencer à utiliser Dastra, prenez le temps de comprendre les notions qui structurent la plateforme. Elles vous permettront d'organiser vos traitements, vos équipes et vos responsabilités.

***

## Sommaire

* [Organisation](key-concepts.md#organisation)
* [Espace de travail](key-concepts.md#espace-de-travail)
* [Unité organisationnelle](key-concepts.md#unite-organisationnelle)
* [Entité](key-concepts.md#entite)
* [Département](key-concepts.md#departement)
* [Propriétaire de l'organisation](key-concepts.md#proprietaire-de-lorganisation)
* [Crédits et quotas](key-concepts.md#credits-et-quotas)

***

## Organisation

Une **organisation** regroupe les comptes et utilisateurs liés à votre abonnement Dastra. C'est la structure racine : elle contient l'ensemble de vos espaces de travail.

Vous voyez le nom de votre organisation en haut à droite de l'interface, sous le nom de votre compte utilisateur.

{% hint style="info" %}
Une organisation peut contenir plusieurs espaces de travail, chacun dédié à un projet, à une entité ou à une équipe différente. Un utilisateur peut appartenir à plusieurs organisations.
{% endhint %}

***

## Espace de travail

Un **espace de travail** est l'environnement dans lequel vous collaborez avec votre équipe. Il regroupe les modules et les données liés à vos entités : traitements, audits, risques, incidents, demandes d'exercice de droits, etc. Les données d'un espace de travail ne sont jamais accessibles depuis un autre espace.

Vous choisissez votre espace de travail à la connexion, en cliquant sur sa tuile dans la liste de vos espaces.

Donnez à vos espaces de travail des noms explicites (par exemple « Conformité Groupe » ou « Entités France »). Cela facilite la navigation quand l'organisation en compte plusieurs.

***

## Unité organisationnelle

Les **unités organisationnelles** structurent un espace de travail selon votre organisation interne. Elles sont de deux types : les entités et les départements.

On rattache à une unité organisationnelle des traitements, des tâches, des demandes d'exercice de droits, des incidents et des risques. On peut aussi lui associer des droits d'accès pour des utilisateurs ou des équipes.

{% hint style="info" %}
Les unités organisationnelles servent de référence pour les rapports et pour les autorisations d'accès. Voir [Créer et paramétrer les unités organisationnelles](organizational-units.md).
{% endhint %}

***

## Entité

Une **entité** correspond à une personne morale, donc à un **responsable du traitement** : une société, une filiale, une association. C'est le niveau auquel vous rattachez les traitements et les informations juridiques clés.

Une entité porte :

* les coordonnées du responsable du traitement,
* le **DPO** (délégué à la protection des données),
* l'**autorité de contrôle chef de file**,
* les départements et les entités enfants qui lui sont rattachés.

Exemple :

> Entité : _Dastra France SAS_\
> Département : _Marketing_\
> DPO : _Jean Dupont_

***

## Département

Un **département** représente un service ou une division d'une entité (par exemple RH, informatique, marketing, juridique). Il affine la répartition des activités au sein d'une même entité.

Les départements servent notamment à :

* filtrer les traitements ou les audits par périmètre,
* assigner des tâches ou des demandes à un groupe ciblé,
* donner des droits d'accès à une équipe sur un périmètre précis.

Un département peut avoir des départements enfants. Une entité peut aussi avoir des entités enfants, par exemple pour représenter les filiales d'un groupe.

{% hint style="info" %}
Les départements sont optionnels. Ils sont utiles dès que l'organisation compte plusieurs services dont vous voulez suivre les traitements séparément.
{% endhint %}

***

## Propriétaire de l'organisation

Le **propriétaire** (owner) est l'administrateur principal de l'organisation. Seuls les propriétaires peuvent créer des espaces de travail, modifier les paramètres de l'organisation, créer des rôles personnalisés et ajouter ou retirer d'autres propriétaires.

Limitez le nombre de propriétaires pour garder une gouvernance claire. Les autres utilisateurs reçoivent des rôles adaptés à leurs besoins : voir [Gérer les rôles et permissions](roles.md).

***

## Crédits et quotas

Votre abonnement définit des crédits, c'est-à-dire des limites sur ce que votre organisation peut créer ou consommer. Ils sont partagés par tous les espaces de travail de l'organisation.

* **Utilisateurs** : les utilisateurs actifs, plus ceux liés à une invitation en attente ou expirée. Supprimer l'utilisateur d'une invitation libère un emplacement. Consultez [Inviter des utilisateurs](users.md).
* **Entités** : la création d'une entité consomme un crédit d'entité. Consultez [Créer et paramétrer les unités organisationnelles](organizational-units.md).
* **Modèles de questionnaires** : les modèles de tous vos espaces de travail comptent, y compris ceux de la corbeille. Consultez [Créer un modèle de questionnaire](../../features/questionnaires/templates/README.md).
* **Traitements, stockage des documents, consentements cookies, historique d'activité** : la page **Abonnement** des paramètres de l'organisation indique le crédit de votre offre pour chacun d'eux.
* **IA** : un quota mensuel de crédits IA, décrit dans [Comment ça marche ?](../../features/general/ai-assistant/how-it-works.md#credits-et-quotas-ia).

Lorsqu'une limite est atteinte, l'écran concerné l'indique et propose un lien pour contacter l'équipe Dastra et augmenter votre crédit.
