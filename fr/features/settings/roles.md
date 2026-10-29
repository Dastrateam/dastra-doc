---
description: >-
  Chaque organisation est différente : créez des rôles personnalisés et ajustez
  leurs permissions module par module.
---

# Rôles et permissions

{% embed url="https://youtu.be/wNrj3Ru2wz8" %}

## Fonctionnement général

Chaque utilisateur peut être associé à 1 ou plusieurs rôles. Les rôles sont eux mêmes associés à une liste de permissions (ex : écrire dans le registre, créer un questionnaire...). Il existe deux manières d'administrer les rôles associés aux utilisateurs.

* Si vous êtes propriétaire, cliquez sur l'icône d'engrenage de la barre supérieure (**Réglages de l'organisation**), puis sur **Utilisateurs**. L'adresse directe est [https://app.dastra.eu/general-settings/users](https://app.dastra.eu/general-settings/users).
* Si vous avez le rôle d'administrateur d'espace de travail, ouvrez **Réglages espace de travail** > **Utilisateurs** pour gérer les rôles et permissions des utilisateurs appartenant à votre espace de travail.

Les rôles par défaut (**Administrateur**, **Contributeur**, **Lecteur**) sont décrits dans [Gérer les rôles et permissions](../../getting-started/setup/roles.md). Cette page explique comment créer vos propres rôles.

{% hint style="info" %}
Un rôle ne suffit pas toujours pour voir un élément : l'accès aux **unités organisationnelles** et les **équipes** de l'utilisateur comptent aussi. Voir [Pourquoi un utilisateur ne voit-il pas un traitement ?](../../getting-started/setup/visibility.md)
{% endhint %}

## Créez vos propres rôles

La page **Rôles et permissions** est réservée aux propriétaires de l'organisation. Elle apparaît lorsque l'offre souscrite inclut la personnalisation avancée. Pour l'ouvrir, cliquez sur l'icône d'engrenage de la barre supérieure (**Réglages de l'organisation**), puis sur **Rôles et permissions** dans le menu de gauche. L'adresse directe est [https://app.dastra.eu/general-settings/roles](https://app.dastra.eu/general-settings/roles).

Cliquez sur **Ajouter un rôle** pour créer un rôle personnalisé.

<figure><img src="../../.gitbook/assets/settings-roles-base-list.png" alt="La liste des rôles avec les trois rôles de base et le bouton Ajouter un rôle"><figcaption><p>La liste des rôles</p></figcaption></figure>

Saisissez le nom du rôle, puis cochez les cases associées aux permissions de chaque module.

<figure><img src="../../.gitbook/assets/settings-roles-edit-permissions.png" alt="Le panneau d'édition d'un rôle avec les permissions du module Tâches"><figcaption><p>Création d'un rôle de gestion des tâches</p></figcaption></figure>

* **Lecture/Modification de ses propres éléments :** permet aux utilisateurs de voir et modifier uniquement les éléments qui leur sont attribués dans le module.
* **Lecture :** permet aux utilisateurs de voir tous les éléments du module.
* **Ecriture :** permet aux utilisateurs de modifier tous les éléments existants du module. Dans les modules qui proposent la permission **Création**, l'écriture ne donne pas le droit de créer de nouveaux éléments.
* **Création :** permet aux utilisateurs de créer de nouveaux éléments dans le module. Cette permission est indépendante de la permission **Ecriture**.
* **Export :** permet aux utilisateurs d'exporter tous les éléments du module.
* **Import :** permet aux utilisateurs d'importer tous les éléments dans le module.
* **Notification :** les utilisateurs reçoivent des notifications pour tous les éléments du module.

{% hint style="info" %}
Il n'est pas possible de sélectionner à la fois **Lecture/Modification de ses propres éléments** et les permissions sur tous les éléments pour le même rôle dans un module, à l'exception de la permission **Création**. Les utilisateurs accèdent soit uniquement à leurs éléments, soit à tous les éléments ; la permission **Création** leur permet en plus de créer de nouveaux éléments.
{% endhint %}

Une fois votre rôle personnalisé créé, vous pouvez l'affecter à n'importe quel utilisateur de l'espace de travail au sein de votre organisation.

### Permission Création

Les modules suivants proposent une permission **Création** distincte de la permission **Ecriture** :

* Tâches et planification
* Registre et traitements de données
* Exercices des droits
* Violation de données
* Cartographie des données et référentiels
* Gestion des contrats
* Gestion des systèmes d'IA

Dans ces modules, la permission **Création** est cochable avec **Lecture** ou avec **Lecture/Modification de ses propres éléments**. Un rôle qui combine **Lecture/Modification de ses propres éléments** et **Création** permet à l'utilisateur de créer de nouveaux éléments et de modifier uniquement les éléments qui lui sont attribués. Pour qu'un rôle puisse modifier les éléments existants sans en créer, cochez **Ecriture** sans cocher **Création**.

Les rôles par défaut **Administrateur** et **Contributeur** incluent la permission **Création** dans ces modules.

<figure><img src="../../.gitbook/assets/settings-roles-create-permission.png" alt="Permission Création cochée avec la permission Lecture/Modification de ses propres éléments dans le module Violation de données"><figcaption><p>Permission Création combinée à la modification de ses propres éléments</p></figcaption></figure>

## Cloner un rôle existant

Pour créer un rôle à partir d'une configuration existante, clonez-le :

1. Dans la liste des rôles, cliquez sur le menu à trois points de la ligne du rôle à dupliquer.
2. Cliquez sur **Cloner**.

Dastra crée un nouveau rôle qui reprend toutes les permissions du rôle source. Son nom est celui du rôle source suivi d'un numéro, par exemple « Contributeur (2) ». Son panneau d'édition s'ouvre : il ne reste qu'à le renommer et à ajuster les permissions.

Les rôles de base ne sont pas modifiables : clonez-les pour partir de leurs permissions. Le clonage sert aussi à décliner des variantes d'un rôle, par exemple un rôle « Contributeur DPO » légèrement différent du rôle « Contributeur ».
