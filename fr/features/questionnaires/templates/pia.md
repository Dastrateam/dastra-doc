---
description: >-
  Apprenez à créer ou à modifier un modèle de questionnaire de type PIA : type de
  modèle, élément audité et noms de variable du plan de risques.
---

# Créer ou modifier un modèle de PIA

Dastra dispose de plusieurs modèles d'analyses d'impact relatives à la protection des données (AIPD ou PIA). Vous pouvez aussi créer le vôtre.

{% hint style="info" %}
Ne partez pas de zéro : utilisez un modèle existant pour le personnaliser. Cela vous donne une base de départ.
{% endhint %}

## Étape 1 : créer le modèle

Dans le module **Questionnaires**, cliquez sur **Créer modèle**, puis sur **A partir de zéro**.

<figure><img src="../../../.gitbook/assets/questionnaires-templates-2.png" alt="Fenêtre Choisir le type de questionnaire avec l'option A partir de zéro"><figcaption><p>L'option A partir de zéro dans la fenêtre de création</p></figcaption></figure>

## Étape 2 : configurer le modèle

Dans le panneau **Création d'un modèle de questionnaire**, choisissez les options suivantes pour profiter pleinement des fonctionnalités du PIA.

<figure><img src="../../../.gitbook/assets/questionnaires-pia-1.png" alt="Panneau de configuration avec le type Analyse d'impact (PIA) et l'objet associé Traitement de données"><figcaption><p>La configuration d'un modèle de PIA</p></figcaption></figure>

* **Type de questionnaire** : choisissez **Analyse d'impact (PIA)**.

{% hint style="info" %}
Le type PIA affiche les éléments spécifiques au PIA, en particulier la carte de chaleur dans le tableau de bord du questionnaire, et intègre les données du traitement lors de la génération du PIA. Il permet aussi de reprendre des PIA au format JSON depuis l'outil PIA de la CNIL.
{% endhint %}

* **Objet associé** : choisissez **Traitement de données**. Votre questionnaire de PIA est alors associé à un traitement, et vous retrouvez le PIA depuis ce traitement. De plus, la **Date du dernier PIA** du traitement est mise à jour automatiquement à la publication du PIA : à la finalisation du questionnaire si l'étape de validation est désactivée, sinon à sa validation.

## Étape 3 : définir les noms de variable

Les modèles de type PIA remontent deux types d'éléments :

* des analyses de risques (impact et probabilité initiaux, impact et probabilité résiduels) ;
* des tâches de remédiation.

Pour que le rapport de résultat du PIA s'affiche, nommez les variables des sections (champ **Lien (slug)**) et des questions (champ **Identifiant de la question (slug)**) selon le plan ci-dessous. Le plan reprend celui du modèle PIA (CNIL) de la bibliothèque, qui compte trois risques de sécurité. Chaque risque a deux sections : la section du risque initial et la section du risque résiduel, dont le nom commence par `pia_todo_`.

<figure><img src="../../../.gitbook/assets/questionnaires-pia-2.png" alt="Fenêtre Configurer la section avec le libellé Disparition des données et le slug pia_34"><figcaption><p>Le slug de la section Disparition des données</p></figcaption></figure>

| Section ou question | Variable | Type |
| --- | --- | --- |
| Accès illégitime à des données (risque 3.2) | `pia_32` | Section |
| Mesures existantes | `pia_324` | Sélection dynamique multiple |
| Gravité (impact) initiale | `pia_325` | Choix unique avec score |
| Vraisemblance (probabilité) initiale | `pia_326` | Choix unique avec score |
| Accès illégitime : risque résiduel | `pia_todo_32` | Section |
| Mesures envisagées (remédiation) | `pia_todo_324` | Sélection dynamique multiple |
| Précisions sur le plan d'action | `pia_todo_321` | Texte enrichi |
| Gravité (impact) résiduelle | `pia_todo_325` | Choix unique avec score |
| Vraisemblance (probabilité) résiduelle | `pia_todo_326` | Choix unique avec score |
| Modification non désirée de données (risque 3.3) | `pia_33` | Section |
| Disparition des données (risque 3.4) | `pia_34` | Section |

Pour les risques 3.3 et 3.4, reprenez la même structure en remplaçant `32` par `33` ou `34` dans tous les noms, y compris dans `pia_todo_`. Pour un risque supplémentaire, utilisez le numéro suivant (`pia_35`, `pia_todo_35`, etc.). Dans le modèle de la CNIL, les questions de gravité et de vraisemblance portent un score de 0 à 4.
