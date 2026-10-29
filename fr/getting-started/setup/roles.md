---
description: Découvrez comment gérer les rôles et permissions dans Dastra.
---

# Gérer les rôles et permissions

{% embed url="https://youtu.be/wNrj3Ru2wz8" %}

Au moment d'inviter un utilisateur, Dastra propose, par défaut, **cinq rôles** :

* **Administrateur** : les administrateurs ont les droits des contributeurs et peuvent administrer les réglages d'espaces de travail. Les administrateurs sont les seuls à pouvoir passer un traitement en statut « publié », à créer des unités organisationnelles et à inviter de nouveaux utilisateurs dans l'espace de travail.
* **Contributeur** : les contributeurs peuvent lire et éditer le contenu des espaces de travail. Ils peuvent créer des éléments et modifier les brouillons qui ne sont pas encore publiés. Ils ne peuvent pas modifier les paramètres des espaces de travail.
* **Lecteur** : les lecteurs peuvent uniquement visualiser le contenu de l'espace de travail. Ils ne peuvent pas éditer le contenu ni modifier les paramètres de l'espace de travail.
* **Auditeur** : rôle du module de conformité. Il donne accès en lecture aux fichiers et pièces jointes, et vous laisse modifier ses propres éléments d'audit de conformité.
* **Testeur de conformité** : rôle du module de conformité. Il donne accès en lecture et en écriture aux fichiers et pièces jointes, et vous laisse modifier ses propres éléments opérationnels de conformité.

{% hint style="info" %}
Seuls les **propriétaires** peuvent modifier les paramètres du compte d'organisation et créer des espaces de travail.
{% endhint %}

## Attribuer un rôle à un utilisateur

Dans Dastra, un utilisateur peut cumuler plusieurs rôles. Vous pouvez les attribuer depuis deux endroits.

### Dans l'espace de travail courant

1. Dans le menu de gauche, cliquez sur **Réglages espace de travail**, puis sur **Utilisateurs**.
2. Ouvrez le menu de la ligne de l'utilisateur, puis cliquez sur **Assigner rôles**. Le nombre entre parenthèses est le nombre de rôles déjà attribués à l'utilisateur.
3. Sélectionnez le ou les rôles à lui attribuer.

### Dans plusieurs espaces de travail à la fois

Seuls les propriétaires de l'organisation peuvent utiliser cette méthode.

1. Cliquez sur l'icône de votre profil en haut à droite de l'écran, puis sur **Configuration de l'organisation**, puis sur **Utilisateurs**.
2. Ouvrez le menu de la ligne de l'utilisateur, puis cliquez sur **Rôles & espaces de travail**.
3. Cliquez sur **Assigner**, sélectionnez le rôle, puis choisissez la portée : **Tous les espaces de travail de l'organisation** ou **Espaces de travail spécifiques**.

<figure><img src="../../.gitbook/assets/getting-started-roles-1.png" alt="Fenêtre d'attribution de rôle avec la liste des rôles et le choix des espaces de travail"><figcaption><p>L'attribution d'un rôle à tous les espaces de travail ou à une sélection</p></figcaption></figure>

Il est aussi possible de créer des rôles sur mesure, potentiellement mieux adaptés à votre organisation.

## Créer un rôle personnalisé

{% embed url="https://youtu.be/zdUm7SQ3mLY" %}

Pour créer un rôle personnalisé, vous devez être propriétaire de l'organisation.

1. Cliquez sur l'icône de votre profil en haut à droite de l'écran, puis sur **Configuration de l'organisation**.
2. Dans le panneau de configuration, cliquez sur **Rôles et permissions**.

<figure><img src="../../.gitbook/assets/getting-started-roles-2.png" alt="Menu du profil avec l'entrée Configuration de l'organisation"><figcaption><p>Le menu du profil</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/getting-started-roles-3.png" alt="Panneau de configuration de l'organisation avec le bouton Rôles et permissions"><figcaption><p>Le panneau de configuration de l'organisation</p></figcaption></figure>

La liste des rôles et permissions s'affiche.

<figure><img src="../../.gitbook/assets/getting-started-roles-4.png" alt="Liste des rôles de base et des rôles personnalisés"><figcaption><p>La liste des rôles, avec des exemples de rôles personnalisés</p></figcaption></figure>

{% hint style="info" %}
Seuls les propriétaires de l'organisation ont accès à l'écran de gestion des rôles et permissions.
{% endhint %}

3. Cliquez sur **Ajouter un rôle** et donnez-lui un nom.
4. Cochez les permissions liées à chaque fonctionnalité (**Lecture**, **Écriture**, **Création**, **Import**, **Export**, etc.). Dans les modules qui la proposent, la permission **Création** autorise la création de nouveaux éléments, indépendamment de la permission **Écriture** qui autorise leur modification (voir [Rôles et permissions](../../features/settings/roles.md)).
5. Cliquez sur **Enregistrer** en bas de l'écran.

Pour repartir d'un rôle existant, cliquez sur **Cloner** en face de ce rôle. **Voir permissions** affiche les permissions d'un rôle sans le modifier.

{% hint style="info" %}
Pour être effectif, le nouveau rôle doit être attribué à un ou plusieurs utilisateurs, depuis la page **Utilisateurs** décrite plus haut.
{% endhint %}

Vous pouvez maintenant suivre le tutoriel ou commencer à explorer les fonctionnalités de Dastra par vous-même.

{% content-ref url="../tutorial/README.md" %}
[README.md](../tutorial/README.md)
{% endcontent-ref %}
