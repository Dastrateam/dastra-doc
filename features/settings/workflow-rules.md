---
description: Intégrez des processus complexe à l'aide des Règles de workflow personnalisées
---

# Règles de worfkows

## Le principe de fonctionnement

Les Règles de workflow dans Dastra sont un ensemble d'actions (notifications par e-mail, planification d'un audit, tâches et mises à jour de champs) qui sont exécutées lorsque certaines conditions sont réunies. Ces règles automatisent le processus d'envoi des notifications par e-mail, d'attribution des tâches et de mise à jour de certains champs d'un enregistrement lorsqu'une règle est déclenchée.

![Schéma du principe de base](<../../.gitbook/assets/image (258) (1).png>)

## Comment créer une règle de workflow dans Dastra ?

* Allez dans [la page de configuration des règles de workflows votre espace de travail](https://app.dastra.eu/workspace/0/settings/workflow-rules)
* Cliquez sur "Nouvelle règle de workflow"
* Choisissez un nom et le type d'entité concernée (Traitement, Violations...)
* Vous arrivez dans le designer de règles

### Définition du déclencheur

Vous pouvez déclencher une règle de workflow sur deux évènements :&#x20;

* Lors d'**une action sur une entité concernée** : modification, suppression ou création&#x20;
* **Lorsqu'une date précise de l'entité est atteinte**. par exemple : envoyer une notification 10 jours après la date de publication.&#x20;

Un seul trigger peut être défini par règle de workflow.

A noter que vous pouvez choisir si le workflow peut s'exécuter plus d'une fois par entité. **Il est fortement recommandé** **d'exécuter les workflows une seule fois par entité**, car l'exécution d'un workflow plusieurs fois peut conduire assez facilement à des problèmes de répétition de création de tâches ou de doublons de notifications.

### Définition de conditions

Vous pouvez configurer une ou plusieurs conditions d'éxécution par règle.

### Définition des actions

Pour ajouter une nouvelle action, cliquez sur le bouton "**Ajouter un action**" et choisissez le modèle que vous souhaitez mettre en place

Voici les **différents types d'actions** que vous pouvez déclencher :&#x20;

* Envoi d'une notification par email
* Mise à jour d'un champ de l'entité concernée
* Ajout d'un tag à l'entité
* Planification automatique de l'audit
* Définition du propriétaire de l'élément (la personne assignée par exemple)
* Création automatique d'une tâche

Il est possible de chaîner les conditions. Vous pouvez ajouter plusieurs actions par condition en cliquant de nouveau sur "ajouter une action".

{% hint style="info" %}
Exemple : envoyer une notification à plusieurs personnes lors de la création d'une tâche. Pour cela, sélectionner le déclencheur "taches" et selon les conditions de la tache (par exemple, l'ajout d'un tag), ajouter une action "notification"
{% endhint %}



### Variables personnalisées

Très souvent, dans les notifications personnalisées par exemple, il sera intéressant d'y injecter des informations provenant de l'objet qui est entré dans le workflow : le nom du traitement, sa date de publication... sont autant de variables que vous pourrez facilement injecter dans le texte de vos notifications grâce au système d'injection de variables.

En interne, Dastra utilise un moteur de templating basé sur [LiquidJS](https://shopify.github.io/liquid/basics/introduction/)

**Pour accéder aux différentes variables de l'objet du trigger, tapez "\{{",** cela affichera une liste de propositions de variables que vous pouvez injecter dans le contenu





## Tutoriel vidéo : les règles de workflow

{% embed url="https://www.youtube-nocookie.com/embed/FqPmGdk2nTI" %}



