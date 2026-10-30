---
description: >-
  Suivez Brightmoor Retail Group dans un projet de conformité ISO 27001 avec
  Dastra, du framework et du périmètre à la campagne de tests et aux audits.
---

# Projet ISO 27001

Brightmoor Retail Group veut obtenir la certification ISO/IEC 27001 pour sa boutique en ligne. Emma Walsh, la déléguée à la protection des données, pilote le projet et Liam O'Connor le suit. Cet exemple parcourt les six phases d'un projet de conformité avec les écrans et les libellés réels de l'application.

Dastra prépare et suit le travail. Le certificat lui-même est délivré par un organisme de certification accrédité, en dehors de Dastra.

## Le parcours en bref

| Phase | Ce que fait Brightmoor | Référence |
| --- | --- | --- |
| **Périmètre** | Définit un périmètre et crée le projet | [Périmètres](../features/compliance/scopes.md), [Projets](../features/compliance/projects/README.md) |
| **Exigences** | Ajoute le framework ISO 27001 et importe ses contrôles et ses risques | [Conception du projet](../features/compliance/projects/design.md) |
| **Implémentation** | Exclut les contrôles non applicables, assigne des propriétaires, configure les tests | [Implémentation du projet](../features/compliance/projects/implement.md) |
| **Surveillance** | Lance une campagne de tests et collecte les preuves | [Surveillance de la conformité](../features/compliance/projects/monitoring.md) |
| **Audit interne** | Audite le framework et signale les écarts | [Audits](../features/compliance/projects/audits.md) |
| **Audit final** | Consigne l'état de conformité avant la certification | [Audits](../features/compliance/projects/audits.md) |

## 1. Préparer le framework

Un framework regroupe les exigences, contrôles, tests, risques et menaces d'une norme. Brightmoor part du modèle Dastra.

1. Dans le menu, ouvrez **Conformité** > **Bibliothèque** > **Frameworks**.
2. Cliquez sur **Créer un framework**, puis choisissez **A partir d'un modèle**.
3. Recherchez ISO 27001 et sélectionnez le modèle. Vérifiez dans le détail le nombre d'exigences, de contrôles, de risques et de menaces.
4. Confirmez l'import.

Le framework est dans la bibliothèque et il est modifiable. Sa création consomme un crédit de framework du compte (voir [Import et modèles Dastra](../features/compliance/library/frameworks/import.md)).

## 2. Définir le périmètre

Le périmètre répond à une question : quelles unités organisationnelles le projet couvre-t-il ? Brightmoor certifie uniquement la boutique en ligne.

1. Ouvrez **Conformité** > **Périmètres** et créez un périmètre nommé « Boutique en ligne ».
2. Sélectionnez les unités organisationnelles « Group IT » et « E-commerce ». Un périmètre contient au moins une unité.

## 3. Créer le projet

1. Ouvrez **Conformité** > **Projets**, puis **Tous les projets**, et cliquez sur **Créer un projet**.
2. Saisissez « Certification ISO 27001 » dans **Intitulé** et choisissez le **Périmètre** « Boutique en ligne ». Cliquez sur **Suivant**.
3. Dans **Assignez des utilisateurs au projet**, ajoutez Emma Walsh avec le rôle **Responsable** et Liam O'Connor avec le rôle **Informé**. Cliquez sur **Ajouter**.

Le projet s'ouvre sur sa vue d'ensemble, dans la phase **Périmètre**. L'assistant en haut de page affiche la **Checklist** de la phase, et le bouton **Passer à la phase : …** apparaît quand toutes les étapes sont faites.

## 4. Phase Exigences : importer les contrôles

Passez le projet en phase **Exigences** et suivez la checklist.

1. Ajoutez le framework ISO 27001 au projet. Gardez la version présélectionnée dans **Version à installer**.
2. Importez tous les contrôles du framework. Les contrôles sont considérés comme implémentés par défaut, et leurs tests sont rattachés avec le statut **Preuve manquante**.
3. Ajoutez au projet les risques du framework. Ils servent de base à l'évaluation du risque initial.

Si Brightmoor ajoute plus tard un autre framework, par exemple le RGPD, Dastra détecte les contrôles communs et ne les importe qu'une seule fois (voir [Conception du projet](../features/compliance/projects/design.md#4.-mutualisation-des-controles-entre-frameworks)).

<figure><img src="../.gitbook/assets/examples-iso-1.png" alt="Vue d'ensemble du projet ISO 27001 certification avec la carte du référentiel et la checklist de l'assistant"><figcaption><p>Le projet en phase Exigences</p></figcaption></figure>

## 5. Phase Implémentation : rendre les contrôles concrets

1. Excluez les contrôles non applicables. Brightmoor héberge tout dans le cloud : les contrôles sur son propre centre de données sont hors périmètre. Dans l'onglet **Contrôles**, réglez **Statut du contrôle** sur **Exclu** et renseignez **Expliquez pourquoi ce contrôle doit être exclu**. La justification est reprise dans la déclaration d'applicabilité et dans les audits.
2. Assignez les propriétaires. Dans l'onglet **Exigences**, cliquez sur le bouton utilisateurs d'une exigence. Dans **Assigner un propriétaire à tous les contrôles et tests**, sélectionnez le propriétaire et cliquez sur **Valider**. Sophie Becker prend les exigences de contrôle d'accès, Noah Martin celles d'exploitation.
3. Configurez les tests. Pour chaque test, définissez la procédure, la fréquence et le propriétaire. Un test est manuel, ou automatisé par un connecteur (voir [Tests](../features/compliance/library/tests.md)).
4. Évaluez les risques. Dans l'onglet **Risques**, définissez l'évaluation initiale et l'évaluation résiduelle de chaque risque, et choisissez son traitement. La vue **Cartographie** affiche côte à côte les matrices du risque initial, courant et résiduel.

La checklist de la phase se lit **Configurer au moins un contrôle**, **Configurer les tests automatisés**, **Évaluer tous les risques** et **Attribuer des propriétaires aux tests**.

## 6. Phase Surveillance : collecter les preuves

Passez le projet en phase **Surveillance**. Une preuve ajoutée dans une autre phase déclenche un avertissement.

1. Ouvrez l'onglet **Campagnes de test** et cliquez sur **Créer une campagne de tests**.
2. Saisissez le **Libellé de la campagne**, « Première collecte de preuves », et sélectionnez tous les tests en attente de preuves.
3. Vérifiez que chaque test a un propriétaire. Si ce n'est pas le cas, Dastra vous avertit : utilisez **Voir tests sans propriétaires**.
4. Lancez la campagne et cliquez sur **Envoyer les invitations** pour prévenir les propriétaires, avec un message si besoin.

Chaque propriétaire ouvre **Mes tests**, lit la **Procédure de test**, ajoute la preuve avec **Ajouter preuve** et clique sur **Valider test**. Un même fichier peut servir de preuve à plusieurs tests.

Brightmoor suit les indicateurs **État des tests** et **Fraîcheur des tests** de la vue d'ensemble. La checklist demande au moins 80 % de tests réussis avant la phase suivante.

La norme ISO/IEC 27001 exige une déclaration d'applicabilité. Sur la carte du framework, ouvrez le menu **⋯** et cliquez sur **Exporter la déclaration d’applicabilité**. Le fichier XLSX liste chaque contrôle avec son applicabilité, sa justification et son statut d'implémentation.

## 7. Audit interne

Passez le projet en phase **Audit interne**. La norme ISO/IEC 27001 exige des audits internes à intervalles planifiés.

1. Dans l'onglet **Audits**, cliquez sur **Créer un nouvel audit** et sélectionnez le framework ISO 27001.
2. Saisissez le **Nom**, « Audit interne ISO 27001 », choisissez Sophie Becker dans **Auditeurs**, réglez **Phase de l'audit** sur **Pré-audit** et renseignez **Date de début** et **Échéance**.
3. Gardez **Définir comme audit actif** activé, puis cliquez sur **Valider**.
4. Cliquez sur **Compléter l'audit** et évaluez chaque exigence : **Conforme**, **Partiellement conforme**, **Non conforme** ou **Non applicable**, avec un **Commentaire**.
5. Quand la preuve d'un test est insuffisante, cliquez sur **Signaler erreur**, choisissez la **Sévérité** et décrivez le problème. Dans l'onglet **Tests en erreur**, cochez les tests signalés et cliquez sur **Invalider les tests**, puis sur **Relancer une campagne de tests** pour que les propriétaires complètent leurs preuves.
6. Quand toutes les exigences sont évaluées, cliquez sur **Finaliser l'audit** et rédigez l'**Appréciation finale de l'audit**.

<figure><img src="../.gitbook/assets/examples-iso-2.png" alt="Tableau de bord de l'audit interne ISO 27001 avec sa progression et l'onglet des problèmes de test"><figcaption><p>Le tableau de bord de l'audit interne</p></figcaption></figure>

## 8. Audit final

Passez le projet en phase **Audit final** et créez un nouvel audit avec la phase d'audit **Audit final**. Évaluez de nouveau les exigences sur les preuves améliorées, puis finalisez l'audit.

Le pourcentage de conformité par framework s'affiche sur la vue d'ensemble du projet et dans **Conformité** > **Statistiques**. Brightmoor exporte l'audit pour transmettre les preuves à l'organisme de certification, et peut afficher le projet dans son Trust Center (voir [Paramétrer votre Trust Center](../features/trust-center/configuration/README.md)).
