---
description: >-
  Tenez à jour les catégories de personnes concernées, signalez les personnes
  vulnérables, et consultez ou importez les jeux de données liés à chaque
  catégorie.
---

# Catégories de personnes concernées

Une catégorie de personnes concernées regroupe les personnes dont vous traitez les données : salariés, clients, candidats, mineurs, etc. Dans le menu, le référentiel s'appelle **Cat. personnes concernées**.

Créez chaque catégorie une seule fois ici, puis sélectionnez-la dans vos jeux de données, vos traitements, vos violations de données et vos demandes : vos rapports comptent ainsi les mêmes populations partout.

## Ajouter une catégorie

Ouvrez **Inventaire** > **Référentiels** > **Cat. personnes concernées**. Vous pouvez :

* cliquer sur **Ajouter catégorie de personnes** pour ouvrir une fiche vide ;
* cliquer sur la flèche à côté de ce bouton, puis sur **Créer à partir de modèles** pour copier des catégories de la bibliothèque ;
* importer des catégories depuis un fichier : flèche à côté du bouton, puis **Importer**. Voir [Importer vos données (Excel, Csv)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-subject-categories-1.png" alt="Liste des catégories de personnes concernées avec la colonne Jeux de données affichée"><figcaption><p>La liste des catégories, avec la colonne Jeux de données</p></figcaption></figure>

## Renseigner la fiche de la catégorie

| Champ | Contenu |
| --- | --- |
| **Libellé** | Le nom de la catégorie, obligatoire. |
| **Description** | Une description libre. |
| **Personnes vulnérables concernées** | À cocher lorsque la catégorie regroupe des personnes en situation de déséquilibre, comme des mineurs, des salariés ou des personnes âgées. |

La barre d'outils de la fiche donne accès aux tâches et aux systèmes d'IA liés à la catégorie, selon vos droits et les fonctionnalités activées. Elle contient aussi les traitements qui utilisent la catégorie, les jeux de données de la catégorie (voir ci-dessous), l'historique d'activités et, lorsque des étapes de processus sont définies, l'étape de processus.

Le menu d'actions de la fiche propose **Fusionner** et **Supprimer**. L'**Outil de qualité de données** n'existe pas pour les catégories.

## Jeux de données d'une catégorie

Un jeu de données peut se rapporter à plusieurs catégories, et une catégorie à plusieurs jeux de données. Ce lien vous aide à retrouver, pour une population donnée, les données que vous détenez, par exemple lorsque vous traitez une [demande d'exercice de droits](../../requests/README.md).

* Pour voir les jeux de données d'une catégorie, ouvrez sa fiche : le bouton qui affiche le nombre de jeux de données les liste. Cliquez sur un jeu pour l'ouvrir. Dans la liste des catégories, affichez la colonne **Jeux de données** dans **Personnaliser les colonnes** : vous pouvez aussi filtrer la liste par jeu de données.
* Pour lier ou délier un jeu de données, ouvrez le jeu de données, puis ajoutez ou retirez la catégorie dans son champ **Catégories de personnes concernées**. Voir [Jeux de données](datasets.md). La liste des jeux de données se filtre aussi par **Cat. personnes concernées**.
* Pour importer les liens, utilisez la colonne **Jeux de données** du fichier d'import des catégories : elle contient les noms ou les identifiants des jeux de données, séparés par une barre verticale (`|`). Seuls les jeux de données qui existent déjà dans l'espace de travail sont liés : Dastra ne crée pas les autres.
* Pour exporter les liens, la colonne **Jeux de données** est incluse dans l'export de la liste.

## Retrouver des catégories dans la liste

Depuis une sélection, vous pouvez **Basculer l'étape de processus**, **Fusionner** et **Supprimer**.

## Où les catégories sont utilisées

* Dans un traitement, la section **Personnes concernées** liste les catégories visées, avec leur volume. Voir [Personnes concernées](../../ropa/activity/data-subjects.md).
* Dans les jeux de données, par le champ **Catégories de personnes concernées**. Voir [Jeux de données](datasets.md).

{% hint style="warning" %}
Supprimer une catégorie efface toutes ses références dans les traitements, les violations de données, les demandes d'exercice de droits et les jeux de données.
{% endhint %}
