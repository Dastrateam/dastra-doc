---
description: >-
  Enregistrez les entreprises et personnes avec lesquelles vous travaillez
  (sous-traitants, éditeurs, destinataires, DPO, clients), leurs sous-traitants
  ultérieurs et les actifs qu'elles éditent.
---

# Acteurs

Les acteurs sont les entreprises et les individus liés à vos traitements de données : sous-traitants, éditeurs de logiciels, fournisseurs de modèles d'IA, responsables conjoints, organismes publics, clients, etc. Contrairement aux utilisateurs, ils n'ont pas besoin de se connecter à Dastra.

Saisissez chaque acteur une seule fois dans ce référentiel. Les actifs, les traitements, les contrats et les violations de données le référencent ensuite : une modification de sa fiche s'applique partout.

## Ajouter un acteur

Ouvrez **Inventaire** > **Référentiels** > **Acteurs**. Vous pouvez :

* cliquer sur **Créer acteur**, puis choisir **A partir d'un modèle** pour partir d'un modèle de la bibliothèque, ou **A partir de zéro** pour partir d'une fiche vide ;
* cliquer sur le bouton d'IA à gauche de **Créer acteur** pour décrire l'acteur et laisser l'assistant le rédiger (cette option dépend des fonctionnalités activées pour votre organisation) ;
* cliquer sur la flèche à côté de **Créer acteur**, puis sur **Créer à partir de modèles** ;
* importer des acteurs depuis un fichier : flèche à côté de **Créer acteur**, puis **Importer**. Voir [Importer vos données (Excel, Csv)](../../general/import.md) ;
* transformer des e-mails en acteurs : flèche à côté de **Créer acteur**, puis **Transformer emails en acteurs**. Cette entrée ouvre l'intégration de réception d'emails des réglages de l'espace de travail.

<figure><img src="../../../.gitbook/assets/repositories-stakeholders-1.png" alt="Liste des acteurs avec le menu du bouton Créer acteur ouvert"><figcaption><p>La liste des acteurs</p></figcaption></figure>

## Renseigner la fiche de l'acteur

| Section | Champ | Contenu |
| --- | --- | --- |
| **Informations générales** | **Personne physique** ou **Personne morale** | La nature de l'acteur. Le champ du nom est **Nom complet** pour une personne et **Nom de l'organisation** pour une entreprise, obligatoire. |
| | **Référence interne**, **Unité organisationnelle** | Votre référence, et l'unité qui peut voir l'acteur. Sans unité, toutes les unités le voient. |
| | **Propriétaire de l'acteur** | L'utilisateur responsable de l'acteur. |
| | **Description**, **Url du site web** | Une description libre et l'adresse du site web. |
| | **Numéro d'identification d'entreprise** | Personne morale uniquement. Lorsque l'intégration SIRET est activée, vous pouvez rechercher dans la base SIRET et l'adresse est renseignée pour vous. |
| | **Adresse postale** | **Pays**, **Adresse postale**, **Ville**, **Code postal** et **Région**. |
| | **Coordonnées du contact** | **Nom du contact**, **Intitulé de poste du contact**, **Email du contact** et **Téléphone du contact**. |
| **Sous-traitants ultérieurs** | | Les sous-traitants ultérieurs de l'acteur, souvent cités dans le DPA. Sélectionnez-les dans la liste ou créez-les, puis renseignez pour chacun le **Pays de localisation des données** et une description. Vous cartographiez ainsi toute la chaîne de sous-traitance. |
| **Actifs liés** | | Les actifs édités par l'acteur. Sélectionner un actif fait de l'acteur son **Editeur** : si l'actif a déjà un autre éditeur, Dastra vous demande de confirmer le remplacement. |

Les [champs personnalisés](../../general/custom-fields.md) définis pour les acteurs s'ajoutent à la fiche, et vous pouvez joindre un logo et des [tags](../../general/tags.md).

La barre d'outils de la fiche donne accès aux documents joints, aux commentaires, aux questionnaires, aux tâches, aux contrats et aux risques liés à l'acteur, selon vos droits et les fonctionnalités activées. Elle contient aussi :

* **Eléments liés** : les [relations génériques](../relationships.md) de l'acteur ;
* **Traitements** : les traitements qui utilisent l'acteur, avec un bouton **Lier aux traitements (RT, destinataires...)** pour en ajouter ;
* **Historique d'activités** ;
* la revue régulière de l'acteur. Voir [Revue régulière (fraîcheur)](../../regular-review.md) ;
* l'étape de processus de l'acteur, lorsque des étapes sont définies.

Le menu d'actions de la fiche propose **Dupliquer**, **Fusionner**, **Exporter** et **Supprimer**.

## Retrouver des acteurs dans la liste

Outre les filtres décrits dans [Référentiels](README.md), la liste propose :

* le filtre **Référencé en tant que** : éditeur de logiciel (éditeur d'au moins un actif), fournisseur de modèle d'IA (éditeur d'au moins un modèle d'IA), ou destinataire dans un traitement (sous-traitant, responsable conjoint, organisme public, etc.) ;
* les filtres **Nature**, **Pays**, **Etapes** et **Filtrer par tags**, ainsi que l'unité organisationnelle ;
* les vues tableau et cartes ;
* les colonnes **Sous-traitants ultérieurs** et **Contrats liés**, masquées par défaut, dans **Personnaliser les colonnes**.

Depuis une sélection, les actions groupées comprennent **Lier aux traitements (RT, destinataires...)**, **Envoyer des questionnaires**, **Passer en revue**, **Fusionner** et **Exporter**.

## Où les acteurs sont utilisés

* Dans un traitement, un acteur peut être responsable de traitement, responsable conjoint, sous-traitant ou autre destinataire. Voir [Parties prenantes](../../ropa/activity/stakeholders.md) et [Destinataires](../../ropa/activity/recipients/README.md) du traitement.
* Comme **Editeur** d'un actif. Voir [Actifs](assets.md).
* Dans les contrats, les violations de données, les risques et les questionnaires.

{% hint style="warning" %}
Supprimer un acteur efface ses références dans les traitements (destinataires, responsable de traitement, partie prenante), les incidents, les unités organisationnelles et les discussions. Les tâches, les questionnaires et les fichiers joints sont conservés.
{% endhint %}
