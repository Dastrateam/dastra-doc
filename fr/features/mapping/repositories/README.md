---
description: >-
  Le registre est lié à de nombreux référentiels : actifs, acteurs, jeux de
  données, glossaire de données, mesures de sécurité et catégories de personnes
  concernées. Dastra vous permet de les gérer de manière indépendante du
  registre pour limiter les erreurs de saisie.
---

# Référentiels

Pour réduire les erreurs de saisie, Dastra vous permet d'administrer les référentiels de manière autonome, indépendamment du registre. Les traitements du registre réutilisent ensuite les éléments de ces référentiels.

## Accéder aux référentiels

Dans le menu latéral, sous **Inventaire**, cliquez sur **Référentiels**. Le menu déroulant propose :

* **Vue d'ensemble** : le nombre d'éléments de chaque référentiel.
* **Cartographie** : la représentation graphique de vos actifs et de vos acteurs.
* **Actifs**, **Acteurs**, **Jeux de données**, **Glossaire de données**, **Mesures** et **Cat. personnes concernées** : les six référentiels.

Ce que vous pouvez faire dépend des droits de cartographie et de référentiels de votre rôle. Voir [Rôles et permissions](../../settings/roles.md).

## Les six référentiels

* [Actifs](assets.md) : les supports des données, les locaux, les éléments matériels ou immatériels.
* [Acteurs](stakeholders.md) : les entreprises et personnes liées à vos traitements, qui n'ont pas besoin de se connecter à la plateforme.
* [Jeux de données](datasets.md) : des groupes de champs de données formant des ensembles cohérents, avec leurs règles de conservation.
* [Glossaire de données](data-glossary.md) : les champs de données, niveau le plus atomique dans Dastra.
* [Mesures de sécurité](security-measures.md) : les dispositions techniques ou organisationnelles qui protègent les données. L'entrée du menu est **Mesures**.
* [Catégories de personnes concernées](subject-categories.md) : les groupes d'individus dont vous traitez les données. L'entrée du menu est **Cat. personnes concernées**.

Chaque page décrit les champs de la fiche, la création, l'import et la fusion des éléments, et les endroits où le référentiel est utilisé. La façon dont un traitement utilise ces éléments est décrite une seule fois, dans les pages du traitement : voir [Compléter un traitement](../../ropa/activity/README.md).

## Fonctions communes aux listes

Les listes des six référentiels partagent plusieurs fonctions :

* **Créer à partir de modèles** ajoute un élément depuis la bibliothèque de modèles. Pour la plupart des référentiels, un bouton d'IA à côté du bouton de création rédige un élément à partir d'une courte description, lorsque la fonctionnalité est activée pour votre organisation.
* **Importer** ajoute des éléments depuis un fichier. Voir [Importer vos données (Excel, Csv)](../../general/import.md).
* **Exporter** exporte la liste, ou seulement les lignes sélectionnées.
* **Outil de qualité de données** détecte les doublons, et **Fusionner** les regroupe. L'outil de qualité de données n'existe pas pour les catégories de personnes concernées. Voir [Fusion d'éléments](../../general/merge.md).
* Filtres, colonnes personnalisées et vues personnalisées. Voir [Filtres avancés](../../general/filters.md).
* Actions groupées sur une sélection de lignes. Voir [Listes, actions groupées et corbeille](../../general/lists.md). **Modifier les champs**, lorsqu'elle est proposée, modifie le même champ sur tous les éléments sélectionnés.
* Les vues tableau et cartes, pour les actifs et les acteurs.

Dans les référentiels, **Supprimer** demande une confirmation et supprime l'élément définitivement : la corbeille décrite dans la page des listes ne s'applique pas.

Les fiches partagent aussi les [champs personnalisés](../../general/custom-fields.md), sauf pour les catégories de personnes concernées, et, dans la barre d'outils, les [relations génériques](../relationships.md) de l'élément, lorsqu'elles sont proposées.

## Vue d'ensemble et cartographie

La **Vue d'ensemble** affiche une carte par référentiel avec son nombre d'éléments. Cliquez sur une carte pour ouvrir la liste correspondante. Le bouton **Créer un actif** crée un actif depuis cette page.

La page **Cartographie** propose quatre représentations, à choisir dans la liste déroulante en haut à gauche :

* **Cartographie des flux entre les actifs** : un graphe des actifs, de leurs éditeurs, de leurs jeux de données et de leurs étiquettes. Les [relations génériques](../relationships.md) y apparaissent comme des liens.
* **Cartographie des acteurs** : un graphe des acteurs, de leurs actifs et de leurs sous-traitants ultérieurs, que vous pouvez filtrer par **Référencé en tant que**.
* **Diagramme de répartition des données par actif** : un diagramme de Sankey, que vous pouvez filtrer par type de répartition (champs de données, traitements, propriétaires, pays, catégories de données).
* **Arbre hierarchique des actifs**.

Les boutons **Imprimer** et **Rafraîchir** sont disponibles en haut de la page.

## Générer un référentiel de données avec Dastra

{% embed url="https://youtu.be/7Ul_agu6wLc" %}

## Filtrer les référentiels

{% embed url="https://youtu.be/q3dvGcBr6ZA" %}
