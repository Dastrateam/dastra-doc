---
description: >-
  Inventoriez les logiciels, serveurs et autres supports de vos données
  personnelles, décrivez chaque actif et créez un traitement à partir de lui.
---

# Actifs

Les actifs regroupent les éléments utiles au pilotage des données : supports des données, locaux, éléments matériels ou immatériels. Ce référentiel liste les actifs, internes ou externes à l'organisation (applications, ressources, bâtiments, etc.).

Vous y renseignez les applications, logiciels ou autres éléments qui servent de supports aux données. Par exemple, si vous utilisez un logiciel de relation client de type CRM, ajoutez-le à cette liste. Vous maîtrisez ainsi les supports de vos données et vous les reliez à votre catalogue de données.

{% hint style="info" %}
Les actifs ne sont pas nécessairement liés à des sous-traitants. Il peut s'agir, par exemple, d'un logiciel installé sur votre serveur, sans intervention de l'éditeur dans le traitement des données personnelles.
{% endhint %}

## Ajouter un actif

Pour ajouter un actif, vous pouvez :

* partir d'un modèle : cliquez sur la flèche à côté du bouton **Créer un actif**, puis sur **Créer à partir de modèles** ;
* utiliser l'IA : cliquez sur le bouton d'IA à gauche de **Créer un actif**, ou choisissez **Créer avec assistant IA** dans la fenêtre de création (cette option dépend des fonctionnalités activées pour votre organisation) ;
* créer l'actif directement dans le référentiel : cliquez sur **Créer un actif**, puis choisissez **A partir de zéro** ;
* importer des actifs depuis un fichier Excel, CSV ou JSON : cliquez sur la flèche à côté du bouton **Créer un actif**, puis sur **Importer**. Voir [Importer vos données (Excel, Csv)](../../general/import.md) ;
* créer l'actif depuis un questionnaire : cela suppose un modèle de questionnaire de type **Création d'actif**. Voir [Créer un modèle de questionnaire](../../questionnaires/templates/README.md).

## Compléter la fiche de l'actif

La fiche d'un actif regroupe les informations suivantes.

| Section | Champ | Contenu |
| --- | --- | --- |
| **Informations générales** | **Nom**, **Référence interne** | Le nom de l'actif et votre référence interne. |
| | **Unité organisationnelle** | L'unité à laquelle l'actif est rattaché. Voir plus bas. |
| | **Type d'actif** | Le type de l'actif, obligatoire. |
| | **Propriétaire de l'actif** | L'utilisateur chargé de la mise en œuvre de l'actif. Il est assigné de préférence aux questionnaires et aux tâches liés à l'actif. |
| | **Editeur** | L'organisation qui édite, héberge ou gère l'actif. Elle peut être référencée comme sous-traitant lorsque l'actif est mentionné dans un traitement. Exemple : l'éditeur d'Office 365 est Microsoft. |
| | **Description**, **Url de la politique de confidentialité** | Une description libre et l'adresse de la politique de confidentialité de l'actif. |
| | **Type de logiciel**, **Etat du logiciel**, **Type d'hôte**, **Type de développement**, **Type de support**, **Type de maintenance** | Ces six champs apparaissent lorsque le type d'actif est **Logiciel**. |
| **Localisation des données** | **Pays**, **Adresse postale**, **Ville**, **Région**, **Code postal** | Le lieu où se trouve l'actif. |
| | **Informations sur la localisation des données** | Un texte libre pour préciser où les données sont hébergées. |
| **Jeux de données** | | Les jeux de données conservés dans l'actif. Enregistrez l'actif une première fois avant de les créer. |
| **Mesures de sécurité associées** | | Les mesures de sécurité de l'actif, souvent citées dans le DPA. Préférez des libellés courts pour les réutiliser d'un actif à l'autre. |

Les [champs personnalisés](../../general/custom-fields.md) définis pour les actifs s'ajoutent à ce formulaire.

La barre d'outils de la fiche donne accès aux documents joints, aux commentaires, aux questionnaires, aux tâches, aux contrats, aux systèmes d'IA et aux risques liés à l'actif, selon vos droits et les fonctionnalités activées. Elle contient aussi :

* **Eléments liés** : les [relations génériques](../relationships.md) de l'actif, avec leur nombre ;
* **Traitements** : le nombre de traitements qui utilisent l'actif, et leur liste ;
* **Historique d'activités** : les modifications successives de la fiche, que vous pouvez restaurer ;
* la revue régulière de l'actif. Voir [Revue régulière (fraicheur)](../../regular-review.md).

## Créer un traitement à partir d'un actif

Cette action reprend les informations de l'actif pour préparer un traitement, plutôt que de les ressaisir.

1. Ouvrez l'actif.
2. Dans le menu d'actions de la fiche, cliquez sur **Créer un traitement de données à partir d'un actif**.
3. Si des traitements ont été prévus pour cet actif, choisissez-en un dans la liste, ou cliquez sur **Passer cette étape**.
4. Saisissez le **Label du nouveau traitement**, choisissez l'**Unité organisationnelle de destination**, puis cliquez sur **Suivant**.
5. Sélectionnez les jeux de données de l'actif à reprendre dans le traitement, puis cliquez sur **Suivant**.
6. Vérifiez le **Récapitulatif** : nom, description, jeux de données, mesures de sécurité, finalités et personnes concernées. Cliquez sur **Créer le traitement**.

Pour relier ensuite des actifs à un traitement existant, consultez la page [Actifs](../../ropa/activity/assets.md) du traitement.

## Dupliquer, fusionner et supprimer

Le menu d'actions de la fiche propose **Dupliquer**, **Fusionner** et **Supprimer**. Depuis la liste, **Outil de qualité de données** détecte les actifs en doublon. Voir [Fusion d'éléments](../../general/merge.md).

## Rattacher un actif à une unité organisationnelle

Par défaut, un actif créé dans Dastra est accessible à l'ensemble de l'organisation (portée globale). Vous pouvez rattacher un actif à une unité organisationnelle spécifique pour limiter sa visibilité aux utilisateurs de cette entité ou de ce département.

Pour cela, lors de la création ou de la modification de l'actif, sélectionnez l'unité organisationnelle souhaitée dans le champ **Unité organisationnelle**. L'actif n'est alors visible que pour les utilisateurs ayant accès à cette unité organisationnelle.
