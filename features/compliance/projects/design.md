---
description: >-
  La phase de conception constitue le point de départ de votre projet de
  conformité.
---

# Conception du projet

Elle permet de définir le **cadre organisationnel**, de sélectionner les **référentiels applicables** et d’initialiser automatiquement les contrôles, tests et risques associés.

Cette étape pose les fondations du projet et conditionne la qualité du suivi dans les phases suivantes.

***

<figure><img src="../../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>

### 1. Création du projet et définition du périmètre

Lors de la création du projet, un **périmètre organisationnel** doit être sélectionné.\
Le périmètre (scope) regroupe une ou plusieurs unités organisationnelles et détermine **le champ d’application du projet de conformité**.

{% columns %}
{% column %}
Une fois le projet créé, le périmètre est affiché dans l’en-tête du projet et utilisé tout au long du cycle de conformité.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image (490).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

### 2. Affectation des utilisateurs au projet

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image (491).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
La phase de conception permet également de **désigner les utilisateurs autorisés à gérer le projet**.

* Chaque utilisateur peut se voir attribuer un rôle (ex. : responsable).
* Ces utilisateurs seront habilités à piloter les contrôles, les tests et les audits du projet.
{% endcolumn %}
{% endcolumns %}

***

<figure><img src="../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

### 3. Ajout des frameworks de conformité

Un projet de conformité repose sur un ou plusieurs **frameworks** (standards, référentiels internes ou personnalisés).

L’ajout d’un framework permet d’importer :

* les **exigences**,
* les **contrôles**,
* les **tests**,
* et les **risques** associés.

<figure><img src="../../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

Il est possible d’ajouter plusieurs frameworks successivement au même projet.

***

### 4. Mutualisation des contrôles entre frameworks

Lorsque plusieurs frameworks sont ajoutés au projet, Dastra détecte automatiquement les **contrôles communs**.

* Un contrôle partagé entre plusieurs frameworks **n’est importé qu’une seule fois**.
* Sa mise en œuvre couvre simultanément l’ensemble des exigences associées.
* Cela permet d’augmenter la couverture de conformité sans multiplier les actions.

<figure><img src="../../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>

***

### 5. Sélection des contrôles à importer

Lors de l’ajout d’un framework, plusieurs options sont proposées :

* importer **l’ensemble des contrôles** du framework,
* importer **uniquement certains contrôles**,
* ou **ne pas importer de contrôles** afin de les implémenter manuellement.

<figure><img src="../../../.gitbook/assets/image (437).png" alt=""><figcaption></figcaption></figure>

Cette flexibilité permet d’adapter le projet à la maturité de l’organisation.

***

### 6. Initialisation des contrôles et des tests



{% columns %}
{% column %}
Une fois les frameworks importés :

* Les **contrôles sélectionnés** sont automatiquement ajoutés au projet.
* Ils sont considérés comme **implémentés par défaut**.
* Les **tests associés** sont également rattachés aux contrôles.

À ce stade :

* les tests sont positionnés dans l’état **« preuve manquante »**,
* aucune preuve n’est encore collectée.
{% endcolumn %}

{% column %}
<p align="center"></p>

<p align="center"></p>

<p align="center"><img src="../../../.gitbook/assets/image (438).png" alt=""></p>
{% endcolumn %}
{% endcolumns %}



***

### 7. Préparation de l’analyse des risques

Les **risques issus des frameworks** peuvent être sélectionnés lors de l’import.

Ils constituent :

* la base de l’**évaluation du risque initial**,
* le point de référence pour le calcul du **risque résiduel** après application des contrôles.

<figure><img src="../../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

***

### Résultat de la phase Conception

À l’issue de la phase de conception, le projet dispose :

* d’un périmètre clairement défini,
* de responsables identifiés,
* de frameworks applicables importés,
* de contrôles mutualisés et prêts à être suivis,
* de tests initialisés,
* et d’une base de risques structurée.

Le projet est alors prêt à entrer dans la phase suivante : **Implémentation**.
