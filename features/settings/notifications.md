---
description: Apprenez à gérer les notifications dans Dastra.
---

# Notifications

### 🧭 Vue d’ensemble

Dans Dastra, les notifications vous permettent de rester informé des activités importantes liées à vos traitements, audits, tâches ou demandes d’exercice de droits.

Il existe **deux types de notifications** :

1. **Le centre de notifications** — intégré directement dans l’application
2. **Les notifications par e-mail** — personnalisables selon vos préférences

***

### 🔔 Centre de notifications (dans l’application)

Le centre de notifications regroupe les alertes visibles via l’icône **cloche** en haut à droite de votre écran.

* Accessible à tous les utilisateurs du workspace
* Non personnalisable (commune à l’ensemble du workspace)
* Contient les notifications générales sur les activités récentes : création, modification ou suppression d’éléments

<figure><img src="../../.gitbook/assets/image (5) (5).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;Exemple : "Un nouveau traitement de données a été créé dans votre workspace."
{% endhint %}

***

### ✉️ Notifications par e-mail (personnalisables)

Chaque utilisateur peut choisir les notifications à recevoir par e-mail depuis son profil utilisateur.

#### 🔧 Comment personnaliser vos notifications

1. Cliquez sur votre **avatar** en haut à droite de Dastra
2. Sélectionnez **Centre de notifications**
3. Activez ou désactivez les catégories selon vos besoins
4. Enregistrez vos préférences

{% hint style="info" %}
Les notifications e-mail sont idéales pour être alerté des actions nécessitant une réponse rapide (audits, demandes, violations de données, etc.)
{% endhint %}

***

**🔐 Prérequis : la permission "Notification" dans le rôle**

La personnalisation des notifications par e-mail ne fonctionne que si le rôle de l'utilisateur l'y autorise.

Dans la configuration d'un rôle (**Paramètres → Rôles**), chaque module dispose d'une case **Notification**. Si cette case n'est pas cochée, les utilisateurs ayant ce rôle ne recevront aucune notification e-mail sur ce module — quelles que soient leurs préférences personnelles.

{% hint style="info" %}
Le rôle ouvre ou ferme le droit à la notification. L'utilisateur peut ensuite affiner ses préférences — mais uniquement dans la limite de ce que son rôle autorise.
{% endhint %}

### 📚 Catégories de notifications

Les notifications par e-mail sont organisées par **catégories**.\
Chaque catégorie contient plusieurs sous-types d’événements activables individuellement.

| Catégorie                               | Exemple de notification                       | Personnalisable ? |
| --------------------------------------- | --------------------------------------------- | ----------------- |
| **Traitements de données**              | Un traitement a été modifié ou supprimé       | ✅                 |
| **Demandes d’exercice de droits (DSR)** | Une nouvelle demande a été assignée           | ✅                 |
| **Violations de données**               | Une violation a été signalée ou clôturée      | ✅                 |
| **Tâches**                              | Vous avez été assigné à une tâche             | ✅                 |
| **Audits**                              | Une réponse a été validée/refusée             | ✅                 |
| **Modèles d’audit**                     | Un modèle a été mis à jour                    | ✅                 |
| **Commentaires**                        | Quelqu’un vous a mentionné (@)                | ✅                 |
| **Consentement / cookies**              | Une modification a été apportée à la bannière | ✅                 |
| **Rapports / analyses**                 | Un nouveau rapport est disponible             | ✅                 |
| **Marketing / Push**                    | Communications produit ou nouveautés Dastra   | ✅                 |

***

### ⚠️ Notifications automatiques

Certaines notifications sont considérées comme **systémiques** : elles sont envoyées automatiquement, même si vous avez désactivé la catégorie correspondante.

Ces notifications sont jugées essentielles à la collaboration :

* Invitation à un **audit**
* **Assignation** à une tâche ou à une demande
* **Mention directe** dans un commentaire (@votre-nom)
* Invitation à compléter le **registre des traitements**
* Envoi immédiat d’une **invitation planifiée** (si option activée)

***

### 💬 Bonnes pratiques

Bon à savoir

* Activez les e-mails pour les activités nécessitant une action de votre part (audits, DSR, violations).
* Consultez régulièrement la **cloche** pour le suivi global du workspace.
* Vérifiez votre **dossier “Notifications”** dans votre boîte mail si vous pensez ne plus recevoir certains messages.
* Pour un DPO : activer toutes les catégories.
* Pour un contributeur : privilégier les tâches, commentaires et audits.

***

### ❓FAQ

#### Je ne reçois plus mes notifications, que faire ?

Vérifiez vos préférences dans votre **profil utilisateur → Centre de notifications**.\
Assurez-vous également que les e-mails de Dastra ne sont pas redirigés vers le dossier “Promotions” ou “Spam”.

{% hint style="info" %}
Attention, vous ne recevez pas de notification pour des éléments qui vous concernent.&#x20;
{% endhint %}

#### Pui  s-je recevoir un résumé mensuel ?

Vous pouvez revevoir un résumé mensuel des activités de votre espace de travail. Cliquez sur la notification : **Préférences : inscription au rapport mensuel**



***

### 🔗 Voir aussi

* [Paramétrer votre profil utilisateur](../../getting-started/setup/parametrer-votre-profil-utilisateur.md)
* [Configurer les rôles et permissions](roles-et-permissions.md)
* [Suivre vos audits](../audit/)

