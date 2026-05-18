---
description: Apprenez à réaliser une analyse d'impact relative à la protection des données (AIPD/PIA) avec Dastra.
---

# Analyse d'impact (AIPD / PIA)

## Qu'est-ce qu'une AIPD / PIA ?

Une analyse d'impact relative à la protection des données (AIPD), également appelée Privacy Impact Assessment (PIA), est un processus requis par l'article 35 du RGPD lorsqu'un traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes concernées.

L'AIPD doit être réalisée avant la mise en œuvre du traitement concerné, et révisée dès lors que la nature du traitement évolue de manière significative.

## Ce traitement nécessite-t-il une AIPD ?

Dans Dastra, l'onglet **Analyse d'impact** de chaque traitement vous aide à déterminer si une AIPD est requise. Il évalue 9 critères de risque définis par le CEPD :

* Évaluation ou notation incluant le profilage et les activités de prédiction
* Prise de décision automatisée avec des effets significatifs
* Surveillance systématique
* Données personnelles sensibles
* Données traitées à grande échelle
* Combinaison, rapprochement ou croisement de données
* Données concernant des personnes vulnérables
* Usage innovant ou application de nouvelles technologies
* Traitement empêchant les personnes concernées d'exercer leurs droits

Pour chaque critère, sélectionnez "Oui", "Non" ou "Non applicable". **Deux réponses "Oui" suffisent généralement** à déclencher l'obligation de réaliser une AIPD, bien qu'un seul critère puisse être suffisant selon le contexte.

{% hint style="info" %}
La liste des traitements nécessitant une AIPD dépend des recommandations de votre autorité de contrôle nationale. Dastra propose un guide AIPD avec des recommandations par pays pour vous aider à identifier vos obligations.
{% endhint %}

Dastra affichera l'un des deux résultats suivants :

* **"Une AIPD n'est pas requise"** — le traitement ne franchit pas le seuil
* **"Vous devez réaliser une analyse d'impact relative à la protection des données (AIPD)"** — un bouton "Créer une AIPD" apparaît pour lancer l'analyse directement

## Les modèles d'AIPD dans Dastra

Plusieurs modèles de PIA/AIPD sont disponibles dans la bibliothèque Dastra, notamment :

* **PIA (CNIL) - Analyse d'impact sur la vie privée** (57 questions) : le modèle standard de la CNIL, pour un traitement unique
* **PIA (CNIL) - Analyse d'impact sur la vie privée (multi-traitements)** (57 questions) : le modèle CNIL adapté pour des analyses couvrant plusieurs traitements
* **Privacy impact assessment (PIA)** (114 questions) : un modèle PIA générique complet
* **EDPB DPIA Template 2026** (82 questions) : le modèle recommandé par le Comité européen de la protection des données
* **DPIA Template for AI Systems** (90 questions) : pour les traitements impliquant des systèmes d'IA à haut risque (RGPD + AI Act)
* **DPC DPIA Questionnaire - Irlande** (9 questions) : le modèle de l'autorité irlandaise
* **DPIA Questionnaire (ICO)** (9 questions) : le modèle de l'autorité britannique

Pour y accéder, rendez-vous dans l'onglet "Modèles de questionnaires", cliquez sur **"Créer un modèle"** → **"Questionnaires automatisés"**, puis filtrez par type "Analyse d'impact".

## Structure du questionnaire PIA (CNIL)

Le modèle PIA (CNIL) est structuré en trois grandes parties :

1. **Contexte** — décrire le traitement : informations générales, finalités, données impliquées, parties prenantes (responsable de traitement, sous-traitants, coresponsables)
2. **Principes fondamentaux** — évaluer la proportionnalité et la minimisation des données, et documenter les mesures de protection des droits des personnes
3. **Risques liés à la sécurité des données** — évaluer les risques selon quatre catégories de menaces : mesures de sécurité mises en place, accès illégitime aux données, modification non désirée des données, disparition des données

{% hint style="info" %}
Le questionnaire PIA (CNIL) propose deux modes de réponse : **Mode simplifié** pour une expérience allégée, et **Mode expert** pour une analyse plus détaillée. Vous pouvez basculer entre les deux modes à tout moment.
{% endhint %}

## Lier une AIPD à un traitement

Pour tirer pleinement parti des fonctionnalités AIPD dans Dastra, configurez votre modèle comme suit :

1. Définissez le **type de modèle** sur "Analyse d'impact" — cela active la carte de chaleur des risques dans le tableau de bord du questionnaire et intègre les données du traitement lié.
2. Dans la section **Élément évalué**, sélectionnez "Traitement de données" — cela lie chaque réponse à un traitement spécifique et met automatiquement à jour la date de la dernière AIPD lors de la validation.

{% hint style="info" %}
Une fois l'AIPD liée à un traitement, vous pouvez y accéder directement depuis l'onglet **"Analyse d'impact"** de ce traitement, et la lancer via le bouton "Créer une AIPD" lorsque le seuil est atteint.
{% endhint %}

## Importer une PIA depuis l'outil CNIL

Si vous avez déjà réalisé une PIA avec l'outil dédié de la CNIL, vous pouvez l'importer directement dans Dastra :

1. Exportez votre PIA depuis l'outil CNIL au format **.json**
2. Dans Dastra, sélectionnez le modèle PIA (CNIL) et cliquez sur **"Importer votre PIA CNIL"**
3. Une très grande partie des éléments sera automatiquement reprise dans Dastra

## Réaliser une AIPD sur plusieurs traitements

Une seule et même AIPD peut couvrir plusieurs traitements similaires en termes de nature, de portée, de contexte, de finalités et de risques. Utilisez le modèle **PIA (CNIL) - multi-traitements**, ou configurez votre modèle pour qu'il ne soit **pas lié à un traitement spécifique**. Vous pourrez alors réaliser l'AIPD, l'exporter et la rattacher à la documentation des traitements concernés.

## Pour aller plus loin

{% content-ref url="../types-de-questionnaires/tia.md" %}
[tia.md](../types-de-questionnaires/tia.md)
{% endcontent-ref %}

{% content-ref url="../types-de-questionnaires/lia.md" %}
[lia.md](../types-de-questionnaires/lia.md)
{% endcontent-ref %}
