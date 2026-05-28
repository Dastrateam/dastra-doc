---
description: >-
  La phase d’implémentation marque le passage du cadre théorique à l’exécution
  opérationnelle de la conformité.
---

# Implémentation du projet

Elle consiste à **configurer concrètement les contrôles**, à définir les modalités de vérification et à préparer la collecte des preuves.

À ce stade, le projet dispose déjà :

* de ses frameworks,
* de ses contrôles,
* de ses tests et risques initialisés lors de la conception.

***

### 🎯 Objectif de la phase

L’objectif de la phase d’implémentation est de :

* définir **comment les contrôles sont vérifiés**,
* configurer les **tests (manuels ou automatisés)**,
* associer les **risques aux contrôles**,
* préparer la **collecte des preuves de conformité**.

***

### 1. Comprendre le statut des tests en phase d’implémentation

Par défaut, tous les tests du projet sont dans l’état **« Preuve manquante »**.

Cela signifie que :

* le contrôle existe,
* le test est défini,
* mais **aucune preuve n’est encore fournie ou collectée**.

👉 Tant que le projet n’est pas en phase de **surveillance**, la modification ou la validation des preuves n’est pas recommandée.

<figure><img src="../../../.gitbook/assets/image (458).png" alt=""><figcaption></figcaption></figure>

***

### 2. Configurer les tests de conformité

Chaque contrôle peut être vérifié à l’aide d’un ou plusieurs **tests**.

{% columns %}
{% column %}
Un test permet de définir :

* une **procédure de vérification**,
* une **fréquence d’exécution** (ex. mensuelle, trimestrielle, annuelle),
* un **responsable du test**.

Les tests peuvent être :

* **manuels**, nécessitant une action humaine et une preuve,
* ou **automatisés**, via un connecteur Dastra ou personnalisé.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image (459).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

### 3. Associer et évaluer les risques

Les contrôles peuvent être liés à un ou plusieurs **risques** afin de mesurer leur impact sur la réduction du risque.

Pour chaque risque, vous pouvez :

* définir une **évaluation initiale** (probabilité × impact),
* définir une **évaluation résiduelle**, après application des contrôles,
* choisir le **traitement du risque** (réduction, acceptation, etc.).

Cette approche permet de visualiser concrètement l’effet des contrôles sur la posture de risque.

<figure><img src="../../../.gitbook/assets/image (461).png" alt=""><figcaption></figcaption></figure>

***

### 4. Lier menaces, risques et contrôles

Les **menaces** représentent les scénarios concrets pouvant déclencher un risque\
(ex. : injection de données malveillantes, absence de supervision, exfiltration d’informations).

Une menace peut être :

* liée à un ou plusieurs **risques**,
* indirectement couverte par les **contrôles** mis en place.

Ce chaînage permet une traçabilité complète :\
**Menace → Risque → Contrôle → Test → Preuve**

***

### 5. Installer un connecteur pour automatiser les preuves

Pour certains tests, il est possible d’installer un **connecteur Dastra** afin d’automatiser la collecte des preuves.

Les connecteurs permettent par exemple de :

* vérifier la présence d’une politique ou d’un contrat,
* interroger un registre (systèmes d’IA, incidents, traitements),
* automatiser des contrôles récurrents sans action manuelle.

Chaque connecteur est configuré avec :

* une **fréquence d’exécution**,
* des **paramètres de collecte** adaptés au test.

<figure><img src="../../../.gitbook/assets/image (462).png" alt=""><figcaption></figcaption></figure>

***

### 6. Résultat de la phase d’implémentation

À la fin de la phase d’implémentation :

* les **contrôles sont configurés**,
* les **tests sont prêts à être exécutés**,
* les **risques sont évalués et liés**,
* les **connecteurs éventuels sont installés**.

Le projet est alors prêt à entrer dans la phase suivante : **Surveillance**, durant laquelle :

* les tests sont exécutés périodiquement,
* les preuves sont collectées,
* et la conformité est mesurée dans le temps.
