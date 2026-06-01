---
description: Intégrez des processus complexe à l'aide des Règles de workflow personnalisées
---

# Règles de workflows

{% hint style="info" %}
**Étapes de processus vs règles de workflow**

Les [étapes de processus](etapes-de-processus.md) définissent les statuts que traversent les objets (ex. Nouveau → En cours → Fait). Les **règles de workflow** automatisent des actions lorsque ces étapes ou d'autres événements surviennent. Les deux fonctionnalités sont complémentaires.
{% endhint %}

## Le principe de fonctionnement

Les Règles de workflow dans Dastra sont un ensemble d'actions (notifications par e-mail, planification d'un audit, tâches et mises à jour de champs) qui sont exécutées lorsque certaines conditions sont réunies. Ces règles automatisent le processus d'envoi des notifications par e-mail, d'attribution des tâches et de mise à jour de certains champs d'un enregistrement lorsqu'une règle est déclenchée.

![Schéma du principe de base](<../../.gitbook/assets/image (258) (1).png>)

{% hint style="info" %}
Le nombre de règles de workflow disponibles dépend de votre plan, de **25 à 100 règles**. Une capacité supplémentaire peut être achetée si nécessaire. Contactez votre account manager pour plus de détails.
{% endhint %}

## Comment créer une règle de workflow dans Dastra ?

* Allez dans [la page de configuration des règles de workflows votre espace de travail](https://app.dastra.eu/workspace/0/settings/workflow-rules)
* Cliquez sur "Nouvelle règle de workflow"
* Choisissez un nom et le type d'entité concernée (Traitement, Violations...)
* Vous arrivez dans le designer de règles

### Définition du déclencheur

Vous pouvez déclencher une règle de workflow sur deux évènements :&#x20;

* Lors d'**une action sur une entité concernée** : création, modification, changement d'étape ou mise à la corbeille (seulement pour les objets pour lesquels la corbeille existe)

<figure><img src="../../.gitbook/assets/action_fr_01 (1).png" alt=""><figcaption><p>Création d'un déclencheur par action</p></figcaption></figure>

* **Contrôle de date récurrent** — la règle est évaluée chaque jour à une heure configurée et se déclenche en fonction d'un champ date de l'objet. Configurez les paramètres suivants :
  * **Exécuter tous les jours à** — l'heure du contrôle quotidien (avec gestion du fuseau horaire, ex. 00:00 Europe/Paris).
  * **Champ date à vérifier** — le champ date à évaluer (ex. date de clôture, date de création, date de révision…).
  * **Condition sur la date** — choisissez parmi :
    * **A été dépassée** — se déclenche le jour où la date est atteinte.
    * **Modificateurs de date** — ajoutez un décalage par rapport à la date :
      * **Surviendra dans** — se déclenche N heures / jours / mois / ans *avant* la date (ex. 30 jours avant l'expiration d'un contrat).
      * **A été dépassée depuis** — se déclenche N heures / jours / mois / ans *après* la date (ex. 1 jour après la clôture).

  Le bouton **"Voir les éléments comme si c'était aujourd'hui"** permet de prévisualiser les objets qui correspondraient actuellement à la règle, utile pour tester avant activation.

<figure><img src="../../.gitbook/assets/image (513).png" alt=""><figcaption></figcaption></figure>

Un seul déclencheur (ou trigger) peut être défini par règle de workflow.

A noter que vous pouvez choisir si le workflow peut s'exécuter plus d'une fois par entité. **Il est fortement recommandé** **d'exécuter les workflows une seule fois par entité**, car l'exécution d'un workflow plusieurs fois peut conduire assez facilement à des problèmes de répétition de création de tâches ou de doublons de notifications.

### Définition de conditions

Vous pouvez configurer une ou plusieurs conditions d'exécution par règle.

Les conditions peuvent s'appliquer à l'ensemble des champs de l'objet et peuvent être assemblées au sein de groupes pour vous permettre de mettre en place l'ensemble des scénarios possibles (avec la possibilité de changer l'association "Et" ou "Ou").

<figure><img src="../../.gitbook/assets/action_fr_01 (2).png" alt=""><figcaption><p>Ici l'action sera lancée si l'étape est "validation de l'identité" ou "nouveau" ET que la date de validation de l'email est remplie</p></figcaption></figure>

### Définition des actions

Pour ajouter une nouvelle action, cliquez sur le bouton "**Ajouter un action**" et choisissez le modèle que vous souhaitez mettre en place

Voici les **différents types d'actions** que vous pouvez déclencher :&#x20;

* Envoi d'une notification par email
* Mise à jour d'un champ de l'entité concernée
* Ajout d'un tag à l'entité
* Planification automatique d'une réponse à un questionnaire
* Définition de la personne assignée
* Création automatique d'une tâche

Pour les demandes d'exercices de droit, des actions supplémentaires sont disponibles :

* Clôturer la demande
* Mise à la corbeille de la demande
* Anonymisation de la demande (uniquement possible si la demande est clôturée)

Il est possible de chaîner les conditions. Vous pouvez ajouter plusieurs actions par condition en cliquant de nouveau sur "ajouter une action".

{% hint style="info" %}
Exemple : envoyer une notification à plusieurs personnes lors de la création d'une tâche. Pour cela, sélectionner le déclencheur "taches" et selon les conditions de la tache (par exemple, l'ajout d'un tag), ajouter une action "notification"
{% endhint %}

### Variables personnalisées

\
**Exemple**

Pour afficher une variable de type chaine de caractère (la référence d'un traitement)

Très souvent, dans les notifications personnalisées par exemple, il sera intéressant d'y injecter des informations provenant de l'objet qui est entré dans le workflow : le nom du traitement, sa date de publication... sont autant de variables que vous pourrez facilement injecter dans le texte de vos notifications grâce au système d'injection de variables.

En interne, Dastra utilise un moteur de templating basé sur [LiquidJS](https://shopify.github.io/liquid/basics/introduction/)

**Pour accéder aux différentes variables de l'objet du trigger, tapez "\{{",** cela affichera une liste de propositions de variables que vous pouvez injecter dans le contenu

```
{{ref}}
```

Pour afficher toutes les valeurs d'une variable de type tableau (les tags)

```
{% for tag in tags %}

 {{ tag.label }}

{% endfor %}
```

Pour afficher uniquement la 1ere valeur d'une variable de type tableau : (1er approbateur d'un traitement)

```
{% assign accountable = accountables | first %}

{{accountable.displayName}}
```



### Exemples&#x20;

**Exemple de workflow basé sur une action**

Cet exemple permet de voir l'utilisation d'un workflow par action permettant de notifier les approbateurs d'un traitement lors d'un changement d'étape si l'étape courante est différente de "Nouveau"

<figure><img src="../../.gitbook/assets/workflow_stateChange01-fr (1).png" alt=""><figcaption></figcaption></figure>

**Exemple de workflow "complexe" basé sur une date :**

Cet exemple permet de voir l'utilisation d'un workflow par date permettant de nettoyer automatiquement les demandes de droits dont l'identité de l'utilisateur n'aurait pas été validé un mois après la création.

<figure><img src="../../.gitbook/assets/workflow_anon01-fr.png" alt=""><figcaption><p><strong>Tous les jours, fermer et anonymiser les demandes de droit dont l'identité du demandeur n'a pas été validée un mois après la création</strong></p></figcaption></figure>

### Bibliothèque de modèles de règles

La bibliothèque de modèles de règles de workflow regroupe deux sources :

* **La bibliothèque par défaut de Dastra** — des règles prêtes à l'emploi couvrant les scénarios d'automatisation les plus courants : gestion des violations de données, expiration de contrats, révision des fournisseurs, cycle de vie des demandes d'exercice de droits… Maintenue et enrichie par Dastra.
* **Les modèles personnalisés de votre organisation** — toute règle que votre équipe a enregistrée comme modèle. Ces modèles sont accessibles dans la même bibliothèque et réutilisables par tous les utilisateurs de l'espace de travail.

Les modèles peuvent être filtrés par type d'objet et par langue.

**Enregistrer une règle comme modèle**

Ouvrez une règle de workflow existante et cliquez sur **"Enregistrer comme modèle"**. Le modèle est immédiatement disponible dans la bibliothèque, réutilisable sur tout type d'entité compatible — sans reconfiguration manuelle.

Cette fonctionnalité permet d'harmoniser les règles d'automatisation à l'échelle de l'organisation et d'éviter de reconstruire des workflows identiques sur chaque objet ou entité.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (512).png" alt=""><figcaption></figcaption></figure>

***

## Tutoriel vidéo : les règles de workflow

{% embed url="https://www.youtube-nocookie.com/embed/FqPmGdk2nTI" %}
