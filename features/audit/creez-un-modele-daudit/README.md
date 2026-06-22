---
description: Apprenez à créer et modifier un modèle de questionnaire avec Dastra.
---

# Créer ou modifier un modèle de questionnaire

## Introduction

La création ou la modification d'un modèle de questionnaire dans Dastra est un jeu d'enfant. Pour ce faire, accédez à la fonctionnalité "Questionnaires".

## Créer ou modifier un modèle de questionnaire

{% embed url="https://youtu.be/bESwC6iMcI8" %}

Pour créer un modèle de questionnaire, cliquez sur le bouton "Créer un modèle" dans l'onglet "Questionnaires". Ensuite vous pouvez sélectionner un des types de modèles disponibles dans Dastra : questionnaire automatisé, personnalisé ou importé depuis un fichier.

<figure><img src="../../../.gitbook/assets/audit-template-list-toolbar.png" alt=""><figcaption></figcaption></figure>

Vous arrivez sur l'interface de sélection des types de modèles :

![Choix des types de modèles](<../../../.gitbook/assets/audit-create-type-picker.png>)

* En cliquant sur l'onglet "**Questionnaire automatisé**", vous choisirez un modèle de questionnaire prédéfini existant en piochant dans la bibliothèque de Dastra.
* En cliquant sur "**Questionnaire personnalisé**", vous pouvez construire votre propre modèle de questionnaire.

{% hint style="info" %}
Contrairement aux questionnaires automatisés, les questionnaires personnalisés sont entièrement personnalisables. En fonction des réponses sélectionnées par les répondants, vous serez en mesure de générer automatiquement un plan d'actions ou de cartographier les risques associés au modèle.
{% endhint %}

## Les modèles de questionnaires automatisés

Dastra propose de nombreux modèles de questionnaires automatisés permettant de documenter la conformité et de piloter les processus. Ces modèles incluent notamment des AIPD/PIA, des TIA, des LIA, des questionnaires sous-traitants, et bien d'autres.

![Bouton de sélection de bibliothèque](<../../../.gitbook/assets/capture-web-6-5-2022-103438-app-dastra-eu.jpeg>)

Une fois le modèle sélectionné, vous accédez à l'écran de planification où vous pouvez :

* soit **modifier le modèle** en cliquant sur le bouton "Modifier le modèle"
* soit planifier un questionnaire en cliquant sur le bouton "Planifier un questionnaire"

{% hint style="info" %}
Certains types de questionnaires (AIPD, TIA, LIA) peuvent également être lancés directement depuis un traitement — par exemple depuis les onglets "Analyse d'impact", "Destinataires" ou "Finalités". Consultez les pages dédiées ci-dessous pour plus de détails.
{% endhint %}

## Les modèles de questionnaires personnalisés

Dans Dastra, il vous est possible de créer votre propre modèle de questionnaire personnalisé. Pour cela, cliquez sur l'option "Questionnaire personnalisé". Vous accéderez ainsi à l'interface d'édition de modèle de questionnaire.

Construisez le modèle de questionnaire que vous souhaitez et cliquez sur "Enregistrer et continuer".

![Exemple de modèle de questionnaire personnalisable.](<../../../.gitbook/assets/capture-web-6-5-2022-103818-app-dastra-eu.jpeg>)

### Éléments évalués

Vous pouvez lier des questionnaires à des éléments dans Dastra. En choisissant le type d'élément évalué, vous forcez toutes les réponses basées sur ce modèle à être liées à un objet du type choisi. Par exemple, vous pouvez choisir que ce modèle de questionnaire sera toujours lié à un traitement.

<figure><img src="../../../.gitbook/assets/audit-create-audited-element-dropdown.png" alt=""><figcaption></figcaption></figure>

Vous pouvez choisir de ne pas lier un questionnaire à un objet particulier. Dans ce cas, la réponse sera toujours liée à une unité organisationnelle. Cela peut être le cas pour des questionnaires de conformité globaux par exemple.

### Les types de modèles

Lors de la création d'un modèle personnalisé, vous devrez choisir un type de modèle.

<figure><img src="../../../.gitbook/assets/audit-create-type-dropdown.png" alt=""><figcaption></figcaption></figure>

Ces types permettent une certaine personnalisation des modèles de questionnaires.

* **Questionnaire standard** : il s'agit d'un questionnaire classique
* **Questionnaire de conformité** : à l'heure actuelle, il s'agit d'un questionnaire classique
* **Analyse d'impact** : ce modèle permet d'afficher une matrice des risques (avec la configuration requise) et d'être appelé lors de l'étape AIPD d'un traitement
* **Questionnaire de sous-traitant** : ce modèle est appelé lors de l'étape destinataires sous-traitants d'un traitement
* **Analyse d'impact sur le transfert (TIA)** : questionnaire permettant l'analyse des risques relatifs à un transfert de données hors UE
* **Analyse de la base légale (LIA)** : questionnaire de la base légale des intérêts légitimes pour s'assurer que les intérêts n'outrepassent pas les droits et libertés des personnes
* **Questionnaire de formation** : questionnaire permettant de réaliser des quiz de formation. Ce type de questionnaire permet de sélectionner une bonne réponse parmi les réponses et d'afficher les bonnes réponses en fin de questionnaire.

## Charger un modèle de questionnaire que vous possédez

Il est enfin possible d'importer un de vos modèles de questionnaires, au format json. Pour cela, à la création du questionnaire, sélectionnez l'option "Charger un modèle".

## Les blocs d'analyse

{% embed url="https://youtu.be/Ot4OmgTKtrg" %}

## Pour aller plus loin

{% content-ref url="../planifier-un-audit.md" %}
[planifier-un-audit.md](../planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="../rapport-daudit.md" %}
[rapport-daudit.md](../rapport-daudit.md)
{% endcontent-ref %}

{% content-ref url="../pia-aipd.md" %}
[pia-aipd.md](../pia-aipd.md)
{% endcontent-ref %}

{% content-ref url="../tia.md" %}
[tia.md](../tia.md)
{% endcontent-ref %}

{% content-ref url="../lia.md" %}
[lia.md](../lia.md)
{% endcontent-ref %}
