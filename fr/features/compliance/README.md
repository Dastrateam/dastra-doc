---
description: Gérez votre conformité aux différents frameworks dans Dastra.
---

# Conformité

Le module **Conformité** de Dastra permet de gérer la conformité réglementaire de manière structurée, traçable et auditable, en s’appuyant sur une architecture modulaire alignée avec les référentiels de conformité.

***

## Naviguer dans le module

Dans le menu, **Conformité** donne accès à quatre entrées :

* **Projets** : les projets de conformité, leurs phases, leurs audits et vos tâches. Voir [Projets](projects/README.md).
* **Bibliothèque** : les frameworks, les contrôles, les tests, les risques et les menaces réutilisables. Voir [Bibliothèque](library/README.md).
* **Périmètres** : les unités organisationnelles couvertes par un projet. Voir [Périmètres](scopes.md).
* **Statistiques** : le tableau de bord de conformité de l’espace de travail (voir plus bas).

***

## Architecture du module Compliance

Le module repose sur une chaîne logique d’objets, depuis les référentiels réglementaires jusqu’aux preuves de conformité.

<figure><img src="../../.gitbook/assets/compliance-object-chain.svg" alt="Chaîne d'objets du module : framework, exigences, contrôles, scénarios de risque, tests, preuves et audits"><figcaption></figcaption></figure>

### Frameworks (Référentiels)

Exemples : RGPD, ISO 27701, ISO 27001, AI Act.

Un framework :

* définit le cadre réglementaire ou normatif,
* contient un ensemble d’exigences applicables.

***

### Exigences (Requirements)

Les exigences représentent les obligations issues d’un framework.\
Exemples : contrôle des accès, gestion des habilitations, journalisation.

Chaque exigence :

* est rattachée à un framework,
* est évaluée lors des audits de conformité,
* est mise en œuvre via un ou plusieurs contrôles.

***

### Contrôles (Controls)

Les contrôles décrivent **comment** une exigence est appliquée concrètement.\
Exemples : revue périodique des accès, procédure d’habilitation.

Un contrôle :

* met en œuvre une exigence,
* est lié à un ou plusieurs scénarios de risque,
* est vérifié à l’aide de tests.

***

### Scénarios de risque (Risk scenarios)

Les scénarios de risque décrivent les événements redoutés. Ils s’affichent sous le nom **Risques** dans l’application.\
Exemple : accès non autorisé à des données sensibles.

Les contrôles permettent :

* de prévenir ou réduire ces risques,
* de démontrer les mesures de remédiation mises en place.

***

### Tests

Les tests servent à vérifier l’efficacité des contrôles.\
Exemples : revue récurrente des accès, délégation de validation.

Un test :

* contrôle un ou plusieurs contrôles,
* produit des résultats mesurables,
* est appuyé par des preuves.

***

### Campagnes de tests (Test campaigns)

Les campagnes permettent d’orchestrer les tests à grande échelle :

* envoi de campagnes aux équipes ou aux clients,
* collecte centralisée des réponses,
* suivi de l’avancement et des statuts.

***

### Preuves (Evidences)

Les preuves démontrent la conformité.\
Exemples : politiques, procédures, rapports de revue d’accès.

Une preuve :

* est associée à un test,
* est utilisée lors des audits,
* garantit la traçabilité des contrôles.

***

### Audits de conformité (Compliance audits)

Les audits permettent d’évaluer le niveau de conformité :

* audits internes,
* auto-évaluations,
* préparation aux audits externes.

Ils s’appuient sur :

* les exigences,
* les contrôles,
* les tests et preuves associées.

***

### Vision d’ensemble

Le module Compliance de Dastra permet ainsi de :

* structurer les exigences réglementaires,
* relier les obligations aux risques,
* prouver la conformité par des contrôles testés et documentés,
* préparer efficacement les audits et certifications.

### Principe multi-framework dans Dastra

Le module Compliance de Dastra est **nativement multi-framework**.

Cela signifie que :

* un même **framework** (RGPD, ISO, AI Act…) contient ses propres exigences,
* une **exigence** appartient à **un framework**,
* un **contrôle peut répondre à plusieurs exigences**, y compris issues de **frameworks différents**,
* les **tests et preuves** sont mutualisés et réutilisables.

Objectif : **éviter les doublons** et piloter la conformité de manière transverse.

***

### Relations clés entre les objets

* un **framework** contient plusieurs **exigences** (1 à N),
* **exigences** et **contrôles** : relation N à N,
* **contrôles** et **tests** : relation N à N,
* un **test** est appuyé par plusieurs **preuves** (1 à N),
* **contrôles** et **scénarios de risque** : relation N à N.

Un même contrôle (ex. revue des accès) peut ainsi :

* satisfaire une exigence RGPD,
* satisfaire une exigence ISO 27001,
* réduire plusieurs scénarios de risque.

Exemple : le contrôle de revue périodique des accès satisfait une exigence du RGPD et une exigence ISO 27001, est vérifié par un test appuyé par une preuve, et réduit deux risques :

<figure><img src="../../.gitbook/assets/compliance-shared-control-example.svg" alt="Exemple d'un contrôle partagé par le RGPD et ISO 27001, avec son test, sa preuve et les deux risques qu'il réduit"><figcaption></figcaption></figure>

***

## Statistiques

**Conformité** > **Statistiques** ouvre le **Tableau de bord de conformité**, qui consolide tous les projets de l’espace de travail. Filtrez-le par **Statuts** (phase du projet), **Unités organisationnelles** et **Périmètres**.

Le tableau de bord contient :

* des indicateurs globaux. Contrôles : **Total de contrôles**, **Contrôles validés**, **Non implémentés** et **Contrôles orphelins** (sans exigence associée). Tests : **Total de tests**, **Tests validés**, **Tests en échec** et **Preuves manquantes**. Audits : **Total d'audits**, **Audits terminés** et **Conformité moyenne**, avec la répartition des exigences entre **Conforme**, **Partiellement conforme**, **Non conforme** et **Non applicable** ;
* **Progression des frameworks** : pour chaque framework, le nombre de projets et l'avancement des contrôles, des tests, des exigences et des risques ;
* **Projets par statut** : la répartition des projets selon leur phase ;
* **Conformité par périmètre** : le niveau de conformité de chaque périmètre.

<figure><img src="../../.gitbook/assets/compliance-statistics-1.png" alt="Tableau de bord de conformité avec les indicateurs globaux, la progression des frameworks et la conformité par périmètre"><figcaption></figcaption></figure>
