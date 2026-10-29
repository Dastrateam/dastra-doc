---
description: >-
  Un utilisateur ne voit pas un traitement, un onglet ou obtient une erreur 403
  ? Comprenez comment les rôles, les équipes et les unités organisationnelles
  déterminent ce qu'il peut voir.
---

# Pourquoi un utilisateur ne voit-il pas un traitement ?

Deux utilisateurs ayant le même rôle ne voient pas forcément les mêmes éléments. Dans Dastra, l'accès dépend de **deux niveaux** qui se cumulent :

1. **Ses rôles** : ils déterminent ce que l'utilisateur peut faire dans chaque module (lecture, écriture, création, export…) et dans quels espaces de travail.
2. **Les unités organisationnelles auxquelles il a accès** : elles déterminent sur quel périmètre (entité, département) il peut voir et modifier les éléments.

Si l'un des deux manque, l'élément n'apparaît pas, ou un message d'erreur d'accès (403, « Ressource inaccessible ») s'affiche.

## 1. Vérifier les rôles

* Les **propriétaires** de l'organisation ont accès à tous les espaces de travail actifs, à toutes les unités organisationnelles et à toutes les permissions.
* Les autres utilisateurs n'ont que les permissions des **rôles qui leur sont attribués**, espace de travail par espace de travail. Un rôle peut être attribué à un espace précis ou à tous les espaces.
* Un rôle sans aucune permission cochée ne donne accès à rien.
* Un utilisateur peut cumuler plusieurs rôles.

Vérifiez dans **Réglages espace de travail** > **Utilisateurs** (de l'espace de travail concerné) quels rôles sont attribués, puis dans **Configuration de l'organisation** > **Rôles et permissions** que le module voulu a bien au minimum la permission **Lecture**. Voir [Rôles et permissions](../../features/settings/roles.md).

{% hint style="info" %}
La permission **Lecture/Modification de ses propres éléments** ne donne accès qu'aux éléments qui sont attribués à l'utilisateur, pas à tous les éléments du module.
{% endhint %}

## 2. Vérifier l'accès à l'unité organisationnelle

Chaque traitement est rattaché à une unité organisationnelle. Si l'utilisateur n'a pas accès à cette unité, il ne voit pas ses traitements, même avec le bon rôle.

Les règles d'accès sont les suivantes :

* Par défaut, une unité organisationnelle est **accessible à tous** les utilisateurs de l'espace de travail : le message « Tout le monde est autorisé à afficher ou modifier l'élément » s'affiche dans ses permissions.
* Dès qu'on **définit des permissions** sur une unité (utilisateurs ou équipes autorisés), seuls les utilisateurs et les membres des équipes listés y ont accès.
* Les unités **filles héritent** des permissions de l'unité parente (indiquées « Hérité »), tant qu'elles n'ont pas les leurs. Si une unité fille définit ses propres permissions, elles remplacent celles du parent.

Pour consulter ou modifier ces règles, ouvrez **Réglages espace de travail** > **Unités organisationnelles**, puis, dans le menu de l'unité concernée, choisissez **Définir les permissions pour…**. Cette action est réservée aux utilisateurs disposant du droit de gestion avancée.

{% hint style="warning" %}
Cause fréquente : une équipe a été ajoutée sur une unité parente, et l'utilisateur n'appartient pas à cette équipe. Il perd alors l'accès à toutes les unités filles qui n'ont pas leurs propres permissions. Vérifiez à quelles [équipes](teams.md) il appartient.
{% endhint %}

## Check-list rapide

| Symptôme | À vérifier |
|---|---|
| Aucun traitement visible, ou un onglet manque | Un rôle avec la permission **Lecture** du module est-il attribué dans cet espace de travail ? |
| Seuls certains traitements sont visibles | Accès aux unités organisationnelles, héritage depuis l'unité parente, appartenance aux équipes |
| Un collègue avec le même rôle voit plus d'éléments | Il appartient probablement à une équipe autorisée sur l'unité, pas vous |
| Le bouton d'enregistrement est grisé | Permission **Écriture** (ou **Création** pour un nouvel élément) manquante |
| Erreur 403 « Ressource inaccessible » | Accès à l'unité organisationnelle de l'élément, ou rôle absent dans cet espace |

Si tout est correct et que l'élément reste invisible, contactez le support Dastra en indiquant l'espace de travail, l'utilisateur et l'élément concernés.
