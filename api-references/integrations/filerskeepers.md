---
description: >-
  L'intégration Filerskeepers vous permettra de synchroniser les durées de
  conservation de vos jeux de données Dastra avec votre référentiel
  Filerskeepers.
---

# Filerskeepers

### Qu'est ce que c'est Filerskeepers ?

[Filerskeepers](https://www.filerskeepers.co/) est un service qui fournit des **tableaux de conservation des données** (retention schedules) prêts à l’emploi, couvrant les obligations légales du monde entier.\
Il aide les entreprises à **déterminer combien de temps conserver ou supprimer chaque type de donnée** pour rester conformes aux réglementations.

### Prérequis

* Avoir une licence payante Dastra
* Avoir un compte Filerskeepers, si vous n'en avez pas, et si vous êtes déjà client Dastra, vous pouvez en [discuter avec notre équipe commerciale](https://meetings-eu1.hubspot.com/yann-forveille/rendez-vous-avec-un-expert?message=Filerskeepers+Integration) qui vous proposera des tarifs avantageux&#x20;
* Avoir mis en place un référentiel de durées de conservation (Schedule) dans le logiciel Filerskeepers. L'intégration aura besoin de ce référentiel pour accéder aux données du catalogue.

### Installation

Le processus de mise en place est très simple :&#x20;

* **Accéder à la page de l'intégration Filerskeepers dans la marketplace** d'intégrations Dastra : [https://app.dastra.eu/workspace/0/settings/integrations/filerskeepers](https://app.dastra.eu/workspace/0/settings/integrations/filerskeepers)
* Cliquer sur le bouton **"Installer"**.
*   **Saisir vos informations de connexion** à votre compte utilisateur administrateur de Filerskeepers (e-mail + mot de passe). Ces informations d'identification nous permettrons de générer un jeton d'accès à l'API de Filerskeepers.<br>

    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
* Une fenêtre de configuration va s'afficher. Cette configuration est obligatoire afin de finaliser l'installation. Dans ce formulaire, sélectionnez le "Schedule" que vous souhaitez configurer avec Dastra.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuration

* Sélectionnez le référentiel Filerskeepers que vous souhaitez synchroniser avec Dastra
* Choisissez si vous souhaitez mettre en place la synchronisation des durées de conservation. (Les jeux de données synchronisés avec Filerskeepers seront maintenues à jour toutes les nuit à 00:00 UTC)
* Sélectionnez les personnes à notifier dans le cas de modification/création des durées de conservation dans les jeux de données. La personne recevra un email de notification contenant les informations sur les jeux de données qui ont été mis à jour.
* Cochez "Create new datasets if not exists" aura pour conséquence de créer un jeu de données pour chaque type de données déclérées dans votre compte Filerskeepers.&#x20;

{% hint style="info" %}
Attention, si vous cochez cette case, un grand nombre de jeux de données vont être créés automatiquement dans votre espace de travail.
{% endhint %}

### Sélection de la politique de durée de conservation

Le connecteur Filerskeepers a plusieurs modes de fonctionnement :&#x20;

* Affichage du sélecteur de durée de conservation depuis votre référentiel de durées de conservation. Appelées "Schedule" dans le logiciel&#x20;

Désormais, quand vous vous rendez dans un jeu de données, dans la section "politiques de conservation", un bouton de sélection de la politique de conservation s'affichera

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

En cliquant sur ce bouton, vous allez pouvoir directement sélectionner un jeu de données depuis votre référentiel Filerskeepers. **Cette durée de conservation sera automatiquement synchronisée** avec Dastra, si vous avez activé cette option dans la configuration du connection.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Sélectionnez un jeu de données, en cliquant sur  le bouton "Select"

Une fois que vous avez sélectionné la durée de conservation, la fenêtre se fermera, et les informations suivantes s'afficheront : <br>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Seul les durées conservation en base active seront synchronisées
{% endhint %}

### Comment sont synchronisées les données entre Dastra et Filerskeepers ?

Un certain nombre de champs issues de Filerskeepers seront automatiquement mappés sur votre durée de conservation :&#x20;

* **La durée de conservation** (from)
* **La description de la règle de conservation**
* **La justification légale, le lien et la juridiction concernée** seront concaténées dans le champ justification
