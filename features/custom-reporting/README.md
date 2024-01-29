---
description: Cette page explique le fonctionnement des rapports personnalisés de Dastra
---

# Rapports personnalisés

Cette fonctionnalité puissante vous permet de créer des rapports sur mesure, adaptés à vos besoins spécifiques. Que vous soyez un utilisateur débutant ou avancé, cette fonctionnalité conviviale vous offre une flexibilité maximale pour extraire les informations importantes des données de Dastra.

### Démarrage rapide

1. Cliquez sur le menu à gauche "Rapports personnalisés"\
   &#x20;![](<../../.gitbook/assets/image (292).png>)
2. Les rapports sont organisés dans un système de catégorie. Avant de créer votre premier rapport, vous devez **créer une première catégorie**
3. **Cliquez sur créer un rapport** et choisissez une des deux options : créer nouveau rapport ou créer à partir d'un modèle

## Glossaire

* **Métrique** : une métrique est une valeur mesurable permettant de regrouper (agréger) les éléments _Exemple: Le nombre de traitement, la moyenne de durée de traitement d'une tâche..._
* **Dimension** : par opposition à la métrique, la dimension ne permet pas d'agréger les données. Il s'agit d'une propriété (= une colonne) toute simple d'un élément. \
  _Exemple: le nom du traitement, le statut du traitement, la référence, ..._

## Construction du rapport

### Principes de base

1. **Sélection des Données :** Choisissez les données que vous souhaitez inclure dans votre rapport. Notre interface conviviale vous permet de parcourir facilement vos ensembles de données et de sélectionner les variables (métriques et dimensions) pertinentes des différentes tables de Dastra.
2. **Filtres Avancés :** Affinez vos résultats en utilisant des filtres avancés. Créez des critères spécifiques pour extraire uniquement les données pertinentes à votre analyse.
3. **Personnalisation Graphique :** Donnez vie à vos rapports en personnalisant les graphiques et les tableaux. Modifiez les styles de graphiques qui répondent le mieux à vos besoins.
4. **Exportation Multiple :** Exportez vos rapports dans divers formats tels que PDF, Excel, ou CSV. Partagez facilement vos résultats avec vos collègues, clients ou partenaires. Intégrez vos données simplement à des outils comme PowerBI.

### Sélection des données

#### Sélection des tables de données

Sélectionnez les différentes tables de données que vous souhaitez requêter : les traitements, les étapes du traitement, finalité, tags... Vous pouvez requêter **jusque 6 tables différentes dans chaque rapport**.

<figure><img src="../../.gitbook/assets/image (293).png" alt=""><figcaption></figcaption></figure>

Cliquez sur "Suivant" quand vous avez choisi les tables

{% hint style="info" %}
Attention, une fois les tables sélectionnées, vous ne pourrez plus revenir en arrière pour remodifier les tables concernées.
{% endhint %}

#### Construction du rapport à partir des métriques et dimensions

Construisez votre rapport en sélectionnant les métriques et dimensions que vous souhaitez afficher.

<figure><img src="../../.gitbook/assets/image (291).png" alt=""><figcaption></figcaption></figure>

Cliquez sur le bouton "Enregistrer" en bas à droite de la page

{% hint style="info" %}
Automatiquement les données seront agrégées par dimension afin de calculer les métriques sélectionnées.&#x20;
{% endhint %}

Exemple : Vous sélectionnez la variable "Nb Traitements de données" et "Statut", vous obtenez un rapport regroupé sous cette forme &#x20;

| Statut    | Nb Traitements de données |
| --------- | ------------------------- |
| Brouillon | 12                        |
| Actif     | 560                       |



## Affichage et visualisation graphique du rapport personnalisé

Une fois le rapport créé, vous serez redirigé sur la page suivante :&#x20;

<figure><img src="../../.gitbook/assets/image (290).png" alt=""><figcaption><p>Capture du résultat des rapports personnalisés</p></figcaption></figure>



Pour ajouter un graphique, cliquez sur "**Ajouter un graphique**".

Vous pouvez alors définir plusieurs catégories de graphique.\
![](<../../.gitbook/assets/image (289).png>)



