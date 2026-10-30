---
description: >-
  Regroupez des champs de données en ensembles cohérents, avec les règles de
  conservation liées à leur cycle de vie, et réutilisez-les dans vos actifs et
  vos traitements.
---

# Jeux de données

Un jeu de données regroupe des champs de données, sensibles ou non, et les règles de conservation liées à leur cycle de vie. Les bulletins de paie papier ou les fiches clients d'un CRM sont des exemples de jeux de données.

Définissez un jeu de données une seule fois dans ce référentiel, puis réutilisez-le dans les actifs qui le contiennent et dans vos traitements. L'inventaire de vos données reste cohérent, et vous retrouvez, pour un actif, tout ce qu'il contient.

## Ajouter un jeu de données

Ouvrez **Inventaire** > **Référentiels** > **Jeux de données**. Vous pouvez :

* cliquer sur **Créer jeu de données** pour ouvrir l'**Assistant à la création de jeu de données**, puis choisir **Créer à partir de zéro**, **Créer avec assistant IA** (cette option dépend des fonctionnalités activées pour votre organisation) ou **Suivre le guide étape par étape**, qui vous demande de sélectionner d'abord les champs de données du jeu. **Importer de filerskeepers** apparaît lorsque l'intégration [Filerskeepers](../../integrations/filerskeepers.md) est activée ;
* cliquer sur le bouton d'IA à gauche de **Créer jeu de données** pour décrire le jeu et laisser l'assistant le rédiger ;
* cliquer sur la flèche à côté de **Créer jeu de données**, puis sur **Créer à partir de modèles** pour copier un jeu de la bibliothèque ;
* importer des jeux de données, avec leurs champs de données, depuis un fichier : flèche à côté de **Créer jeu de données**, puis **Importer**. Voir [Importer vos données (Excel, Csv)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-datasets-1.png" alt="Liste des jeux de données avec le panneau Filtres ouvert"><figcaption><p>La liste des jeux de données</p></figcaption></figure>

## Renseigner la fiche du jeu de données

| Section | Champ | Contenu |
| --- | --- | --- |
| **Informations générales** | **Nom du jeu de données** | Le nom du jeu de données, obligatoire. |
| | **Actif lié** | L'actif qui contient le jeu de données. Vous pouvez créer un actif depuis ce champ. Un jeu de données sans actif est un orphelin. |
| | **Catégories de personnes concernées** | Les [catégories de personnes concernées](subject-categories.md) auxquelles les données se rapportent. Vous pouvez créer une catégorie depuis ce champ. |
| | **Référence interne**, **Description** | Votre référence et une description libre. |
| **Détails des données** | | Les champs de données du jeu. Sélectionnez un champ dans la liste ou créez-le, puis renseignez les **Remarques** et cochez **Obligatoire** lorsque le champ est requis. Chaque champ affiche son niveau de sensibilité et sa catégorie. |
| **Durées de conservation** | **Base active**, **Archivage intermédiaire** | Pour chacun : la **Durée de conservation**, la règle (**Décrivez la règle (durée, conditions...)**) et sa **Justification**. |
| | **Sort final** | La description de la règle de purge et sa **Justification**. |
| **Origine de la collecte** | **Origine de la collecte**, **Description de l'origine de la collecte** | D'où proviennent les données. |

Les [champs personnalisés](../../general/custom-fields.md) définis pour les jeux de données et les [tags](../../general/tags.md) s'ajoutent à la fiche.

La barre d'outils de la fiche donne accès aux commentaires, aux questionnaires, aux tâches et aux systèmes d'IA liés au jeu de données, selon vos droits et les fonctionnalités activées. Elle contient aussi :

* **Eléments liés** : les [relations génériques](../relationships.md) du jeu de données ;
* **Lier à un traitement de données** : les traitements qui utilisent le jeu de données, et le lien pour en ajouter.

Le menu d'actions de la fiche propose **Dupliquer**, **Fusionner** et **Supprimer**.

## Retrouver des jeux de données dans la liste

Les filtres de la liste comprennent **Actifs**, **Types**, **Filtrer par tags**, **Cat. personnes concernées**, **Cat. données** et **Données sensibles**. Activez **Voir orphelin (sans actif)** pour lister les jeux de données qui ne sont rattachés à aucun actif, puis rattachez-les depuis le champ **Actif lié**.

Depuis une sélection, vous pouvez **Modifier les champs**, **Fusionner**, **Exporter** et **Supprimer**. **Outil de qualité de données**, dans le menu de **Créer jeu de données**, détecte les doublons. Voir [Fusion d'éléments](../../general/merge.md).

## Où les jeux de données sont utilisés

* Dans un traitement, vous ajoutez les jeux de données que le traitement manipule, et vous pouvez personnaliser leur durée de conservation pour ce traitement seulement. Voir [Données et conservation](../../ropa/activity/datasets.md).
* Dans un actif, la section **Jeux de données** liste les jeux qu'il contient. Voir [Actifs](assets.md).
* Dans les catégories de personnes concernées : la fiche d'une catégorie liste ses jeux de données. Voir [Catégories de personnes concernées](subject-categories.md).
* Dans les systèmes d'IA, par l'onglet des systèmes d'IA du jeu de données.

{% hint style="warning" %}
Supprimer un jeu de données efface ses liens avec les champs de données, les pièces jointes, les traitements et les actifs. Les conversations et le traitement des demandes d'exercice de droits liées sont supprimés définitivement. Les questionnaires et les tâches liées sont conservés.
{% endhint %}
