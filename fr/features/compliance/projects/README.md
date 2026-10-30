---
description: >-
  Un projet de conformité suit l'application d'un ou plusieurs frameworks sur
  un périmètre de votre organisation, de la conception jusqu'à l'audit final.
---

# Projets

Un projet de conformité suit l'application d'un ou plusieurs frameworks sur un périmètre de votre organisation. Il regroupe les exigences, les contrôles, les tests, les risques et les audits, et avance par phases, du cadrage à l'audit final.

Cette page présente la création d'un projet, ses six phases, l'assistant de phase et la navigation. Le détail de chaque phase est décrit dans les pages suivantes :

* [Conception du projet](design.md) : frameworks, exigences, contrôles et risques à importer ;
* [Implémentation du projet](implement.md) : tests, évaluation des risques, connecteurs ;
* [Surveillance de la conformité](monitoring.md) : preuves, campagnes de tests, export de la déclaration d'applicabilité ;
* [Audits](audits.md) : audits internes et audits finaux.

Pour un parcours complet d'un projet de certification, voir l'[exemple du projet ISO 27001](../../../examples/iso-27001-project.md).

## Accéder aux projets

Dans le menu, cliquez sur **Conformité** puis sur **Projets**. Le menu latéral contient deux groupes :

* **Projets de conformité** : **Tous les projets** liste les projets de l'espace de travail ;
* **Mes tâches** : les éléments qui vous sont attribués, tous projets confondus (voir plus bas).

## Créer un projet

1. Dans **Tous les projets**, cliquez sur **Créer un projet**.
2. Saisissez l'**Intitulé** du projet (200 caractères au maximum).
3. Choisissez le **Périmètre** (obligatoire). S'il n'existe pas encore, cliquez sur **Créer un périmètre** dans la liste pour le définir sans quitter la fenêtre. Voir [Périmètres](../scopes.md).
4. Cliquez sur **Suivant**.
5. Dans **Assignez des utilisateurs au projet**, ajoutez les personnes autorisées à gérer le projet et attribuez à chacune le rôle **Responsable** ou **Informé**. Vous êtes ajouté par défaut avec le rôle **Responsable**.
6. Cliquez sur **Ajouter**.

Le projet s'ouvre sur sa vue d'ensemble, en phase **Périmètre**.

{% hint style="info" %}
Créer ou modifier un projet nécessite le droit d'écriture sur la conformité opérationnelle.
{% endhint %}

<figure><img src="../../../.gitbook/assets/compliance-projects-list-1.png" alt="Liste des projets de conformité avec le bouton Créer un projet et le menu latéral Mes tâches"><figcaption></figcaption></figure>

## Les phases d'un projet

Un projet traverse six phases. La phase en cours est mise en évidence sur la vue d'ensemble, et chaque phase affiche son objectif au survol.

| Phase | Objectif | Page |
| --- | --- | --- |
| **Périmètre** | Définir le périmètre de conformité, c'est-à-dire les unités organisationnelles concernées. Cette phase se déroule généralement à la création du projet. | [Périmètres](../scopes.md) |
| **Exigences** | Définir les frameworks à appliquer (RGPD, ISO, etc.), avec leurs exigences, contrôles et risques. Vous pouvez utiliser les modèles Dastra ou vos propres référentiels. | [Conception du projet](design.md) |
| **Implémentation** | Définir comment la conformité s'exécute : tests, évaluation des risques, propriétaires et automatisations éventuelles. | [Implémentation du projet](implement.md) |
| **Surveillance** | Collecter des preuves sur tout le projet à l'aide de campagnes de tests et s'assurer qu'un maximum de contrôles réussissent. C'est la phase de fonctionnement courant. | [Surveillance de la conformité](monitoring.md) |
| **Audit interne** | Réaliser un premier audit interne pour vérifier que tout est correctement mis en œuvre avant l'audit final. | [Audits](audits.md) |
| **Audit final** | Réaliser l'audit de certification de chaque framework mis en œuvre. | [Audits](audits.md) |

La phase **Exigences** correspond à la page [Conception du projet](design.md) : c'est le nom qu'elle porte dans l'application.

<figure><img src="../../../.gitbook/assets/compliance-projects-overview-1.png" alt="Vue d'ensemble d'un projet avec les six phases, l'assistant et la liste des frameworks"><figcaption></figcaption></figure>

### Changer de phase

Les phases ne sont pas verrouillées : vous pouvez passer à n'importe laquelle, en avant comme en arrière.

1. Sur la vue d'ensemble, cliquez sur la phase souhaitée.
2. Confirmez dans la fenêtre **Souhaitez-vous passer le projet à cette étape ?**

Certaines fonctionnalités sont activées ou désactivées selon la phase, et tout votre travail est conservé. Lorsque vous agissez en dehors de la phase recommandée, Dastra affiche un avertissement sans vous bloquer :

* modifier les preuves hors de la phase **Surveillance** ;
* lancer une campagne de tests hors de la phase **Surveillance** ;
* créer un audit hors d'une phase d'audit, ou un audit de certification hors de la phase **Audit final**.

### Suivre la checklist de l'assistant

En haut de la vue d'ensemble, l'assistant rappelle l'**Objectif de phase** et propose une **Checklist** propre à la phase en cours. Chaque étape a un bouton d'action qui mène à l'écran concerné.

| Phase | Étapes de la checklist |
| --- | --- |
| **Périmètre** | Définir le périmètre du projet |
| **Exigences** | Ajouter au moins un framework ; ajouter des contrôles au projet ; ajouter des risques au projet |
| **Implémentation** | Configurer au moins un contrôle ; configurer les tests automatisés ; évaluer tous les risques ; attribuer des propriétaires aux tests |
| **Surveillance** | Valider au moins un test ; s'assurer qu'au moins 80 % des tests réussissent |
| **Audit interne** | Configurer votre premier audit de conformité ; finaliser au moins un audit interne |
| **Audit final** | Lancer un audit final par framework ; finaliser l'un de vos audits finaux ou de certification |

Lorsque toutes les étapes sont terminées, le bouton **Passer à la phase : …** apparaît pour passer à la phase suivante, après la même confirmation.

Pour masquer l'assistant, cliquez sur sa croix (**Masquer l'assistant**). Le bouton **Assistant d'affichage** le fait réapparaître.

## Naviguer dans un projet

Le menu latéral d'un projet rappelle le périmètre, le titre (modifiable en cliquant dessus) et les utilisateurs du projet, puis donne accès aux onglets suivants :

| Groupe | Onglets |
| --- | --- |
| **Projet** | **Vue d'ensemble**, **Exigences**, **Audits** |
| **Contrôles & tests** | **Contrôles**, **Tests**, **Campagnes de test** |
| **Risques** | **Risques**, **Menaces** |

Les boutons de tâches et de commentaires du menu permettent de suivre le projet avec les autres utilisateurs. Le menu **⋯** propose :

* **Paramètres** : modifier le titre, la description et le périmètre ;
* **Historique** : consulter les modifications du projet ;
* **Exporter** : exporter le projet aux formats PDF, DOCX, JSON, HTML ou Markdown ;
* **Déplacer dans la corbeille** : archiver le projet. Un projet archivé est en lecture seule : **Restaurer** le rend de nouveau modifiable et **Supprimer** l'efface définitivement.

## Suivre vos tâches

Le groupe **Mes tâches** du menu latéral réunit, tous projets confondus, ce qui vous est attribué. C'est l'espace de travail quotidien des propriétaires de tests et des auditeurs. Un utilisateur qui n'a pas accès à la liste des projets arrive directement sur **Mes tests** en ouvrant **Conformité**.

| Vue | Contenu |
| --- | --- |
| **Mes tests** | Les tests dont vous êtes propriétaire, avec leurs statistiques. Filtrez par campagne de tests pour ouvrir une campagne et ajouter vos preuves. |
| **Mes contrôles** | Les contrôles dont vous êtes propriétaire. |
| **Mes risques** | Les risques dont vous êtes propriétaire. |
| **Mes audits** | Les audits pour lesquels vous êtes désigné auditeur. Cliquez sur un audit pour l'évaluer. |
| **Mes campagnes de tests** | Les campagnes de tests, filtrables par statut et par framework. |

Voir aussi [Validation des tests](monitoring.md#validation-des-tests).

## Afficher un projet dans le Trust Center

Le Trust Center peut afficher une synthèse de tous les frameworks d'un projet de conformité, avec les informations du dernier audit et les pièces jointes associées. L'option s'active dans la configuration du Trust Center : voir [Paramétrer votre Trust center](../../trust-center/configuration/README.md).
