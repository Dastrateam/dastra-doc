---
description: Apprenez à créer et modifier un modèle d'audit ou un PIA avec Dastra.
---

# Créer ou modifier un modèle d'audit ou un PIA

## Introduction

La création ou la modification d'un modèle d'audit ou d'un PIA dans Dastra est un jeu d'enfant. Pour ce faire, accédez à la fonctionnalité "Audit".



## Créer ou modifier un modèle d'audit / PIA

Pour créer un modèle d'audit ou de PIA, cliquez sur le bouton "Créer un modèle" dans l'onglet "Audit". Ensuite vous pouvez sélectionner un des 3 types de modèles d'audit existant dans Dastra : audit automatisé, combiné ou personnalisé.

<figure><img src="../../.gitbook/assets/image (16) (3).png" alt=""><figcaption></figcaption></figure>

Vous arrivez sur l'interface de sélection des types de modèles :&#x20;

![Choix des types de modèles](<../../.gitbook/assets/image (138).png>)

* En cliquant sur l'onglet "**Audit automatisé**", vous choisirez un modèle d'audit prédéfini existant en piochant dans la bibliothèque d'audits de Dastra.
* En cliquant sur "**Audit combiné**", vous rassemblez plusieurs audits dans un seul.
* En cliquant sur "**Audit personnalisé**", vous pouvez construire votre propre modèle d'audit.

{% hint style="info" %}
Contrairement aux audits automatisés, les audits personnalisés sont entièrement personnalisables. En fonction des réponses sélectionnées par les répondants, vous serez en mesure de générer automatiquement un plan d'actions ou de cartographier les risques associés au modèle.&#x20;
{% endhint %}

## Créer une modèle d'AIPD

Les modèles de AIPD sont inclus dans les modèles d'audits automatisés et sont librement accessibles depuis la bibliothèque Dastra.  Pour créer ou modifier un modèle PIA, cliquez sur "Audit automatisé", puis sélectionner "PIA (CNIL) - analyse d'impact sur la vie privée" avant de cliquer sur "enregistrer".

{% hint style="info" %}
Dans Dastra, les PIA sont un **modèle parmi d'autres d'audit automatisé.**
{% endhint %}

![Bouton de sélection de bibliothèque](<../../.gitbook/assets/Capture web\_6-5-2022\_103438\_app.dastra.eu.jpeg>)

![Modèle PIA](<../../.gitbook/assets/Capture web\_6-5-2022\_10342\_app.dastra.eu.jpeg>)

Une fois le modèle sélectionné, vous accédez à l'écran de planification où vous pouvez réaliser l'une des 2 actions ci-dessous :

* soit **modifier le modèle** en cliquant sur le bouton "Modifier le modèle"
* soit planifier un audit en cliquant sur le bouton "Planifier un audit"&#x20;

{% hint style="info" %}
Pour les PIA, une option complémentaire est possible, le cas échéant :  **importer votre PIA provenant de l'outil de la CNIL**. Pour faire cela, cliquer sur le bouton "Importer votre PIA CNIL".&#x20;

En effet, il est possible d'importer un PIA réalisé par l'outil de la CNIL. Il faut extraire le PIA de la CNIL au format .json pour l'importer dans Dastra.&#x20;

Une très grande partie des éléments sera reprise dans le PIA de Dastra.
{% endhint %}

![Les boutons ](<../../.gitbook/assets/image (216).png>)

## Les modèles d'audit automatisés

Dastra propose de nombreux modèles d'audits automatisés permettant de documenter la conformité et de piloter les processus.&#x20;

Par exemple, des modèles de tests de balance des intérêts (LIA ou legitimate interest assessment) ou de transferts hors UE (TIA) sont présents dans l'application.&#x20;

## Les modèles d'audits personnalisés

Dans Dastra, il vous est possible de créer votre propre modèle d'audit personnalisé. Pour cela, cliquer sur l'option "Audit personnalisé". Vous accéderez ainsi à l'interface d'édition de modèle d'audit.&#x20;

Construisez le modèle d'audit que vous souhaitez et cliquer sur "Enregistrer et continuer".

![Exemple de modèle d'audit personnalisable.](<../../.gitbook/assets/Capture web\_6-5-2022\_103818\_app.dastra.eu.jpeg>)

### Elements audités

Vous pouvez lier des audits à des éléments dans Dastra. En choisissant le type d'élément audité, vous forcez toutes les réponses d'audit basées sur ce modèle à être liées à un objet du type choisi. Par exemple, vous pouvez choisir que ce modèle d'audit sera toujours lié à un traitement.&#x20;

<figure><img src="../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

Vous pouvez choisir de ne pas lier d'audit à un objet particulier. Dans ce cas, la réponse sera toujours liée à une unité organisationnelle. Cela peut être le cas pour des audits de conformité globaux par exemple.&#x20;

### Les types de modèles&#x20;

Lors de la création d'un modèle personnalisé, vous devrez choisir un type de modèle.

<figure><img src="../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

Ces types permettent une certaine personnalisation des modèles d'audit.

* **Audit standard** : il s'agit d'un questionnaire classique
* **Audit de conformité** : à l'heure actuelle, il s'agit d'un questionnaire classique
* **Analyse d'impact** : ce modèle d'audit permet d'afficher une matrice des risques (avec la configuration requise) et d'être appelé lors de l'étape PIA d'un traitement
* **Audit de sous-traitant** : ce modèle d'audit est appelé lors de l'étape destinataires sous-traitants d'un traitement
* **Audit d'impact sur le transfert (TIA)** : audit permettant l'analyse des risques relatifs à un transfert de données hors UE
* **Audit de base légale du registre (LIA)** : audit de la base légale des intérêts légitimes pour s'assurer que les intérêts n'outrepassent pas les droits et libertés des personnes
* **Questionnaire de formation** : questionnaire permettant de réaliser des quizz de formation. Ce type de questionnaire permet de sélectionner une bonne réponse parmi les réponses et d'afficher les bonnes réponses en fin de questionnaire.

## Les modèles d'audit combiné

Dans Dastra, vous pouvez combiner plusieurs modèles d'audits existants pour n'en former plus qu'un. Pour faire cela, sélectionnez l'option "Audit combiné" et suivez les étapes.

## Charger un modèle d'audit que vous possédez

Il est enfin possible d'importer un de vos modèle d'audit, au format json. Pour cela, à la création de l'audit, sélectionnez l'option "Charger un modèle".&#x20;

## Pour aller plus loin

{% content-ref url="planifier-un-audit.md" %}
[planifier-un-audit.md](planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="planifier-un-audit.md" %}
[planifier-un-audit.md](planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="rapport-daudit.md" %}
[rapport-daudit.md](rapport-daudit.md)
{% endcontent-ref %}
