---
description: >-
  Découvrez ce que la confidentialité par conception et la confidentialité par
  défaut signifient et comment les appliquer dans Dastra.
---

# Confidentialité dès la conception et par défaut

### 🌍 Introduction

Les principes de **confidentialité dès la conception** (_privacy by design_) et **confidentialité par défaut** (_privacy by default_) sont au cœur du **RGPD**, posés par [l’article 25](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article25).\
Ils visent à garantir que la **protection des données personnelles** est intégrée **dès la conception d’un projet**, et que **les paramètres par défaut** respectent le niveau de confidentialité le plus élevé possible.

> 🎯 Objectif : prévenir les risques avant qu’ils ne surviennent et démontrer la conformité à chaque étape du cycle de vie des données.

***

### 🧩 Définitions essentielles

#### 🧠 Privacy by Design — "Confidentialité dès la conception"

Le responsable de traitement anticipe la protection des données **dès la conception** d’un produit, d’un service ou d’un traitement.\
➡️ On agit **en amont**, avant toute collecte ou mise en production.

#### 🛡️ Privacy by Default — "Confidentialité par défaut"

Les réglages par défaut doivent garantir le **plus haut niveau de protection possible** : seules les données **strictement nécessaires** sont traitées, et les options de partage ou de visibilité doivent être **désactivées par défaut**.

#### ⚖️ Minimisation

Ne traiter que les données **adéquates, pertinentes et limitées** à la finalité visée.

#### 🔐 Intégrité et sécurité

Restreindre les accès, assurer la **confidentialité, intégrité et disponibilité** des données, et tracer toute action.

#### ⏳ Limitation de la conservation

Planifier **dès la conception** la suppression, l’anonymisation ou l’archivage des données au terme de leur durée utile.

***

### 🧭 Mise en œuvre du Privacy by Design

La démarche doit être **continue** et intégrée au **cycle de vie du traitement** :

#### Étapes clés :

1. **Identifier le projet**
   * Tout nouveau traitement, outil ou changement de processus.
   * Alerter le DPO dès la phase d’étude.
2. **Évaluer les impacts**
   * Cartographier les données et finalités.
   * Identifier les risques pour les droits et libertés.
   * Lancer une **analyse d’impact (PIA/DPIA)** si nécessaire.
3. **Concevoir des mesures adaptées**
   * Minimisation, cloisonnement, chiffrement, pseudonymisation, journalisation.
   * Définir les durées de conservation, les rôles et habilitations.
   * Prévoir les mécanismes d’exercice des droits.
4. **Documenter la conformité**
   * Mentionner les mesures dans le **registre de traitement**.
   * Archiver les preuves dans la **piste d’audit**.
   * Justifier les arbitrages (proportionnalité, choix technologiques, etc.).
5. **Contrôler et améliorer**
   * Auditer régulièrement les traitements.
   * Mettre à jour les registres et plans d’action.

***

### 🧱 Mesures typiques à intégrer

| Objectif                 | Mesure technique ou organisationnelle                        |
| ------------------------ | ------------------------------------------------------------ |
| Minimiser les données    | Collecte sélective, masquage, suppression automatique        |
| Sécuriser les flux       | Chiffrement, TLS, authentification forte, gestion des accès  |
| Préserver les droits     | Portail de gestion des droits (DSR), procédures d’opposition |
| Garantir la transparence | Mentions d’information, logs d’accès, documentation claire   |
| Assurer la traçabilité   | Journalisation des traitements, audits réguliers             |
| Maîtriser la durée       | Purge, anonymisation, archivage intermédiaire sécurisé       |

***

### 🧠 Lien avec l’Accountability (responsabilité démontrée)

Le **Privacy by Design** découle directement du [principe d’accountability (article 5 RGPD)](https://www.cnil.fr/fr/definition/accountability).\
Le responsable de traitement doit pouvoir **prouver à tout moment** la conformité de ses traitements.

> 💬 Cela signifie : _“Ne pas seulement être conforme, mais être capable de le démontrer.”_

***

### ⚙️ Privacy by Design dans Dastra

Dastra facilite la mise en œuvre concrète du **privacy by design** et du **privacy by default** à travers ses modules intégrés :

#### 🔍 1. Identifier les risques

Créez des **audits ciblés** ou des **modèles d’analyse** pour chaque nouveau projet.

***

#### 🧮 2. Évaluer et documenter les risques

Réalisez des **analyses d’impact (PIA)** ou **évaluations de risques** pour chaque traitement.

***

#### 📋 3. Planifier les actions de conformité

Attribuez des **tâches de remédiation**, suivez leur avancement et automatisez les relances.

***

#### 🗂️ 4. Documenter dans le registre

Intégrez les mesures de sécurité et de gouvernance dans vos **fiches de traitement**, avec preuve et journalisation.

***

### 🤖 Extension : Privacy by Design et IA responsable

Le **Privacy by Design** s’applique aussi à la **gouvernance des systèmes d’IA** (AI Act).\
Dastra permet de relier vos **modèles d’IA** à leurs **traitements de données**, d’évaluer la conformité et de documenter les **mesures de maîtrise du risque**.

***

### 📘 Pour aller plus loin

***

{% hint style="success" %}
💡 **Bon réflexe :** Anticipez la conformité dès la phase de conception : impliquer le DPO, documenter les choix, évaluer les risques et intégrer des garanties par défaut.\
Dastra vous aide à structurer cette démarche et à la démontrer facilement.
{% endhint %}
