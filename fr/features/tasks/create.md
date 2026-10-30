---
description: >-
  Créez une tâche du plan d'action, assignez-la, modifiez-la, mettez-la à la
  corbeille ou supprimez-la.
---

# Créer ou modifier une tâche

Dans Dastra, une tâche est un travail à réaliser. Elle a une personne assignée, une échéance et une étape de suivi. Cette page explique comment créer, assigner, modifier et supprimer une tâche.

## Créer une tâche

{% embed url="https://youtu.be/ARvp9PGVnAE" %}

Une tâche se crée de trois façons :

* depuis la page **Tâches** du module Planification ;
* depuis la fiche d'un autre élément de l'application ;
* à partir d'un e-mail reçu sur une adresse de collecte.

### Depuis le module Planification

1. Dans le menu latéral, cliquez sur **Planification**, puis sur **Tâches**.
2. Cliquez sur **Créer tâche**. Le panneau **Créer tâche** s'ouvre à droite de l'écran.

<figure><img src="../../.gitbook/assets/tasks-create-1.png" alt="La barre d'outils de la page Tâches avec le bouton Créer tâche et son menu déroulant ouvert"><figcaption><p>Le bouton Créer tâche et les actions de son menu</p></figcaption></figure>

3. Renseignez l'**Intitulé de la tâche** (120 caractères au maximum) et l'**Unité organisationnelle**, deux champs obligatoires. Complétez les autres champs selon vos besoins.
4. Cliquez sur **Enregistrer**. Pour créer plusieurs tâches de suite, cliquez sur **Enregistrer et créer un nouveau**.

<figure><img src="../../.gitbook/assets/tasks-create-2.png" alt="Le panneau Créer tâche avec l'intitulé, l'unité organisationnelle, la personne assignée, les dates et les éléments associés"><figcaption><p>Le panneau de création d'une tâche</p></figcaption></figure>

Le panneau contient notamment :

* **Unité organisationnelle** : préremplie avec l'unité sélectionnée dans l'espace de travail, ou à défaut la première unité disponible ;
* **Projet**, **Itération** et **Tags** pour classer la tâche ;
* **Assignée à**, **Date de début** et **Date d'échéance** ;
* **Priorité** et **Référence interne**, dans la partie dépliable du panneau ;
* les champs personnalisés que vous avez ajoutés aux tâches.

### Lier une tâche à des éléments

Une tâche peut être liée à un ou plusieurs éléments de l'application. Dans le panneau, cliquez sur **Associer un élément**, choisissez le type d'élément, puis un ou plusieurs éléments de ce type. Les éléments liés sont listés sous **Eléments associés**.

Les types disponibles sont :

* **Traitement de données** ;
* **Demande** ;
* **Violation de données** ;
* **Soumission de questionnaire** ;
* **Acteur** ;
* **Actif** ;
* **Jeu de données** ;
* **Evaluation de risque** ;
* **Point de contrôle** ;
* **Mesure de sécurité** ;
* **Système d'IA** ;
* **Contrat** ;
* **Données** ;
* **Catégorie de personne concernée** ;
* **Projet de conformité** ;
* **Audit de conformité**.

Vous retrouvez ensuite la tâche dans la fiche de chacun de ces éléments (voir ci-dessous). Le filtre **Associée à** de la page **Tâches** liste les tâches liées à un type d'élément donné.

### Depuis la fiche d'un autre élément

Les fiches des traitements, des demandes d'exercice de droits, des violations de données, des acteurs, des actifs, des jeux de données, des mesures de sécurité, des contrats, des systèmes d'IA, des points de contrôle et des évaluations de risque ont un bouton de tâches : une icône de liste avec coche et le nombre de tâches liées.

1. Ouvrez la fiche de l'élément.
2. Cliquez sur le bouton de tâches. Le panneau **Tâches attachées** liste les tâches liées à cet élément, avec des filtres par étape et par tag.
3. Cliquez sur **Créer tâche**. La tâche est liée à l'élément et reprend son unité organisationnelle.

<figure><img src="../../.gitbook/assets/tasks-create-3.png" alt="La fiche d'un traitement avec le panneau Tâches attachées ouvert"><figcaption><p>Le panneau Tâches attachées sur la fiche d'un traitement</p></figcaption></figure>

Le bouton **Afficher dans la planification** du panneau ouvre la page **Tâches** avec les tâches de l'élément.

{% hint style="info" %}
Un plan d'action peut aussi être généré à partir d'un questionnaire validé. Voir [Piloter les questionnaires](../questionnaires/monitor.md).
{% endhint %}

### À partir d'un e-mail

Dastra peut transformer chaque e-mail reçu sur une adresse de collecte en tâche, avec ses pièces jointes. Pour installer l'adresse, cliquez sur la flèche du bouton **Créer tâche**, puis sur **Transformer emails en tâches**. La page d'installation s'ouvre dans **Réglages espace de travail** > **Intégrations**. Voir [Adresses emails de collecte](../settings/mailboxes.md). Cette entrée demande le droit de gérer les intégrations.

### Créer des sous-tâches

Une tâche peut contenir une liste de sous-tâches. Enregistrez d'abord la tâche : le bouton **Ajouter une sous-tâche** reste inactif tant qu'elle n'existe pas. Modifiez ensuite la tâche et cliquez sur **Ajouter une sous-tâche**.

<figure><img src="../../.gitbook/assets/tasks-create-4.png" alt="Une tâche ouverte avec sa liste de sous-tâches et le bouton Ajouter une sous-tâche"><figcaption><p>Les sous-tâches d'une tâche</p></figcaption></figure>

Quand toutes les sous-tâches sont terminées, Dastra propose de fermer la tâche principale.

## Assigner une tâche

Deux champs désignent les personnes concernées :

* **Assignée à** : la personne qui exécute la tâche. Par défaut, c'est vous quand vous créez la tâche ;
* **Propriétaire** : la personne responsable de la tâche. Elle est notifiée en cas de changement d'étape.

Le champ **Propriétaire** se trouve dans la partie dépliable du panneau. Chaque utilisateur reçoit les notifications selon ses préférences : voir [Notifications](../settings/notifications.md). Pour relancer une personne, mentionnez-la dans la discussion de la tâche (voir les [Questions fréquentes](faq.md)).

## Modifier une tâche

Pour modifier une tâche, cliquez dessus : le panneau **Modifier une tâche** s'ouvre. Dans la vue **Tableau**, vous pouvez aussi cliquer sur les trois points à droite de la ligne, puis sur **Modifier**.

<figure><img src="../../.gitbook/assets/tasks-create-5.png" alt="La vue Tableau avec le menu des trois points d'une tâche ouvert"><figcaption><p>Le menu d'une tâche dans la vue Tableau</p></figcaption></figure>

Ce menu propose aussi **Copier le lien**, **Dupliquer**, **Fusionner** et **Déplacer dans la corbeille**. **Dupliquer** crée une copie de la tâche et de ses sous-tâches : l'intitulé de la copie se termine par « - copy ».

{% hint style="info" %}
Pour changer l'étape d'une tâche, glissez-déposez-la dans la vue **Colonnes**. Les étapes par défaut sont **Nouveau**, **Besoins d'infos**, **En cours** et **Fait**. Pour les modifier, cliquez sur la flèche du bouton **Créer tâche**, puis sur **Configurer les colonnes** : voir [Personnaliser le workflow des tâches](workflow.md).
{% endhint %}

### Envoyer une tâche vers Jira

Quand l'intégration Jira est active pour les tâches, le menu d'actions de la tâche propose **Envoyer vers Jira**. Voir [Jira](../integrations/jira.md).

## Mettre à la corbeille ou supprimer une tâche

Une tâche mise à la corbeille n'est pas supprimée : elle porte la mention **Dans la corbeille** et disparaît des listes. Vous pouvez la restaurer à tout moment.

1. Dans le menu des trois points de la tâche, ou dans le menu d'actions du panneau, cliquez sur **Déplacer dans la corbeille**, puis confirmez.
2. Pour retrouver les tâches de la corbeille, ouvrez **Filtres** et cochez **Voir la corbeille**.

<figure><img src="../../.gitbook/assets/tasks-create-6.png" alt="Le panneau Filtres avec la case Voir la corbeille cochée"><figcaption><p>Le filtre Voir la corbeille</p></figcaption></figure>

3. Dans le menu de la tâche, cliquez sur **Restaurer** pour la remettre dans la liste, ou sur **Supprimer**, puis confirmez, pour la supprimer.

<figure><img src="../../.gitbook/assets/tasks-create-7.png" alt="Le menu d'une tâche de la corbeille avec les actions Restaurer et Supprimer"><figcaption><p>Les actions d'une tâche de la corbeille</p></figcaption></figure>

{% hint style="danger" %}
La suppression d'une tâche est définitive. Ses sous-tâches sont supprimées avec elle.
{% endhint %}

Pour supprimer des tâches sans passer par la corbeille, voir les [Questions fréquentes](faq.md).

## Aller plus loin

{% content-ref url="projects.md" %}
[Créer ou modifier un projet ou une itération](projects.md)
{% endcontent-ref %}
