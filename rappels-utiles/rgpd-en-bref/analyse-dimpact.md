---
description: Apprenez ce qu'est une analyse d'impact.
---

# Analyse d'impact (PIA / DPIA)

### 📖 Qu’est-ce qu’un PIA ?

L’**analyse d’impact sur la protection des données (PIA)**, prévue par l’[article 35 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article35), est un **mécanisme de conformité** qui vise à :

* **Identifier et minimiser les risques** d’atteinte aux droits et libertés des personnes,
* **Prouver la conformité** au RGPD,
* Et **intégrer la privacy dès la conception** (_Privacy by design_).

> ⚖️ Le PIA porte sur les **risques pour les personnes**, et non sur les risques pour l’organisation.

**PIA = Privacy Impact Assessment = DPIA = AIPD = EIVP**

***

### 🧩 Les trois composantes d’un PIA

Un PIA est structuré en trois grandes étapes :

1. 📝 **Description du traitement**\
   → Objectifs, contexte, acteurs, technologies, données concernées.
2. ⚖️ **Évaluation de la nécessité et de la proportionnalité**\
   → Analyse de la conformité juridique : finalités, bases légales, droits des personnes, durées, etc.
3. 🔐 **Étude des risques et des mesures de sécurité**\
   → Identification des risques pour la vie privée et détermination des mesures de maîtrise (techniques et organisationnelles).

> 📘 Le PIA est à la fois **juridique**, **technique** et **organisationnel** : il engage toute l’équipe projet.

***

### 🎯 Objectif du PIA

Le PIA permet à une organisation de :

* **Démontrer sa conformité** (principe d’accountability),
* **Anticiper les risques** et les coûts de mise en conformité,
* **Documenter les choix** et arbitrages de conception,
* **Garantir la confiance** des usagers, clients ou salariés.

***

### 🔍 Quand faut-il réaliser un PIA ?

Un PIA est **obligatoire** lorsqu’un traitement **entraîne un risque élevé** pour les droits et libertés des personnes.

#### Exemples de traitements concernés :

* Surveillance vidéo intelligente,
* Notation automatique de profils (scoring),
* Collecte massive de données de santé,
* Utilisation de biométrie ou d’IA sur données personnelles.

{% hint style="info" %}
Les traitements présentant au moins **2 des critères suivants** (EDPB) sont réputés à risque élevé :

* Évaluation ou scoring,
* Décision automatisée avec effet juridique,
* Surveillance systématique,
* Données sensibles,
* Large échelle,
* Croisement de données,
* Personnes vulnérables,
* Usage innovant (IA, IoT, big data),
* Blocage d’un droit ou d’un service,
* Transferts hors UE.
{% endhint %}

***

### 🕐 Quand le réaliser ?

Le PIA doit être mené **avant la mise en œuvre du traitement**, idéalement dès la phase de conception.\
Il constitue une application concrète du principe de **Privacy by Design**.

Il doit aussi être :

* **Mis à jour régulièrement** (tous les 3 à 5 ans),
* **Révisé en cas de modification** importante du traitement,
* **Rattaché à votre registre** dans Dastra pour un suivi continu.

![Un processus itératif](https://1301193153-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LvBxs22wUMicv9uWp6C%2F-MhI-vvGMYAjSpi9Gdmd%2F-MhI2gnfh_tui7vgUFpG%2Fimage.png?alt=media\&token=5fe8ef16-b671-435f-8202-e5ce62ee184b)

> 🔁 Le PIA est un **processus itératif** : il accompagne tout le cycle de vie du traitement.

***

### ⚙️ Comment réaliser un PIA ?

#### 1. Évaluer la nécessité et la proportionnalité du traitement

Posez-vous les bonnes questions :

* Les **finalités** sont-elles déterminées et légitimes ?
* Le **fondement juridique** est-il clair ?
* Les données sont-elles **minimisées**, exactes et à jour ?
* Les **durées de conservation** sont-elles limitées ?
* Les **personnes concernées** sont-elles correctement informées ?

#### 2. Examiner la protection des droits des personnes

* Information transparente, consentement clair, droit d’accès, d’effacement, d’opposition.
* Contrats avec les sous-traitants.
* Garanties sur les transferts internationaux.
* Mesures correctives prévues en cas de violation.

#### 3. Analyser les risques sur la vie privée

Pour chaque **événement redouté** :

* Identifier les **impacts possibles** sur les personnes (atteinte à la vie privée, réputation, discrimination…).
* Estimer la **gravité** et la **vraisemblance** du risque.
* Déterminer les **mesures de protection existantes ou prévues**.
* Évaluer le **risque résiduel** et, le cas échéant, proposer des **mesures complémentaires**.

{% hint style="success" %}
💡 Objectif final : atteindre un **niveau de risque résiduel acceptable**, documenté et justifié.
{% endhint %}

***

### 🧠 Qui doit être impliqué ?

| Acteur                        | Rôle dans le PIA                                                  |
| ----------------------------- | ----------------------------------------------------------------- |
| **Responsable du traitement** | Porte la responsabilité du PIA et pilote sa réalisation           |
| **DPO**                       | Conseille, valide la méthodologie et évalue les risques résiduels |
| **RSSI / Direction IT**       | Apporte l’expertise technique et les mesures de sécurité          |
| **Équipes métiers**           | Fournissent les détails opérationnels du traitement               |
| **Sous-traitants**            | Communiquent les informations nécessaires à l’évaluation          |
| **Personnes concernées**      | Peuvent être consultées ou représentées dans certains cas         |

> 👥 Le PIA est une démarche collaborative — il engage autant les juristes que les opérationnels.

***

### 🤖 PIA et intelligence artificielle

L’**AI Act** introduit une obligation spécifique de **documentation et d’évaluation des systèmes d’IA** à risque.\
Les organisations doivent y inclure :

* L’origine des données d’entraînement,
* Les tests de robustesse et biais,
* Les contrôles humains prévus,
* Les mesures de transparence.

Dastra permet de relier chaque **PIA** à un **système d’IA** pour assurer une **conformité croisée RGPD / AI Act**.

***

### 🧰 Bonnes pratiques Dastra

* Centralisez tous vos PIA dans **le module “Registre des traitements”**,
* Utilisez les **modèles de risques prédéfinis** (EDPB, CNIL, ISO 29134),
* Collaborez avec les équipes via **commentaires et workflows**,
* Exportez vos PIA en **PDF** pour les audits,
* Planifiez des **rappels automatiques de révision**.

{% hint style="success" %}
💡 Dastra vous guide pas à pas dans la réalisation du PIA, grâce à un modèle interactif et des bibliothèques de menaces et mesures déjà intégrées.
{% endhint %}

***

### 📘 Pour aller plus loin

{% embed url="https://www.youtube.com/watch?v=yfaJC-YESPk" %}
🎥 Webinar “Comment aborder l’étape PIA avec un outil ?”
{% endembed %}
