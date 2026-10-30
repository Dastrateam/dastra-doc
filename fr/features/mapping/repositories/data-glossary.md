---
description: >-
  Tenez à jour la liste des champs de données, niveau le plus atomique de la
  cartographie, avec leur catégorie et leur niveau de sensibilité.
---

# Glossaire de données

Un champ de données est une information, comme un nom, une adresse e-mail ou un numéro de dossier médical. C'est le niveau le plus atomique de la cartographie : les [jeux de données](datasets.md) sont composés de champs de données.

Listez chaque champ une seule fois dans ce glossaire, pour que tous les jeux de données décrivent la même donnée de la même façon.

## Ajouter un champ de données

Ouvrez **Inventaire** > **Référentiels** > **Glossaire de données**. Vous pouvez :

* cliquer sur **Créer une donnée** pour ouvrir une fiche vide ;
* cliquer sur la flèche à côté de **Créer une donnée**, puis sur **Créer à partir de modèles** pour copier des champs de la bibliothèque ;
* importer des champs depuis un fichier : flèche à côté de **Créer une donnée**, puis **Importer**. Voir [Importer vos données (Excel, Csv)](../../general/import.md).

Vous pouvez aussi créer un champ directement depuis la section **Détails des données** d'un jeu de données.

## Renseigner la fiche du champ de données

| Champ | Contenu |
| --- | --- |
| **Nom** | Le nom du champ, obligatoire. |
| **Référence interne** | Votre référence. |
| **Catégorie de données personnelles** | La catégorie de données personnelles à laquelle le champ appartient. |
| **Niveau de sensibilité** | **Standard** (nom, prénom, numéro de téléphone), **Données hautement personnelles** (données financières, localisation, communications) ou **Données sensibles** (origine raciale ou ethnique, opinions politiques, religion, santé, orientation sexuelle). |
| **Base légale de collecte**, **Justification de la collecte de données sensibles** | Affichés pour le niveau **Données sensibles** uniquement : la base légale choisie dans la liste, et votre justification. |
| **Description de la donnée**, **Description technique** | Une description libre, et la définition technique du champ. |
| **Type de donnée** | Le type générique de la donnée. |

Les [champs personnalisés](../../general/custom-fields.md) définis pour les champs de données s'ajoutent à la fiche. La barre d'outils donne accès aux commentaires et aux tâches liés au champ, à l'historique d'activités et, lorsque des étapes de processus sont définies, à l'étape de processus. Le bouton à l'icône de base de données liste les jeux de données qui contiennent le champ.

Le menu d'actions de la fiche propose **Fusionner** et **Supprimer**.

## Retrouver des champs dans la liste

Les filtres sont **Catégorie de données personnelles** et **Type de données**. La colonne **Jeux de données**, masquée par défaut dans **Personnaliser les colonnes**, se filtre avec **Est vide** ou **N'est pas vide** : utilisez-la pour retrouver les champs qui n'appartiennent à aucun jeu de données.

Depuis une sélection, vous pouvez **Basculer l'étape de processus**, **Modifier les champs**, **Fusionner**, **Exporter** et **Supprimer**. **Outil de qualité de données**, dans le menu de **Créer une donnée**, détecte les doublons. Voir [Fusion d'éléments](../../general/merge.md).

## Où les champs de données sont utilisés

Les champs de données arrivent dans vos traitements par les jeux de données. Voir [Données et conservation](../../ropa/activity/datasets.md), où vous ajoutez aussi les champs d'un jeu de données à un traitement.

{% hint style="warning" %}
Supprimer un champ de données efface définitivement toutes ses références aux jeux de données. Les conversations liées sont supprimées.
{% endhint %}
