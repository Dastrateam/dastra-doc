---
description: >-
  Apprenez comment affiner l'affichage de vos rapport dans les tableaux de
  données de tous les modules grâce aux filtres avancés
---

# Filtres avancés

{% embed url="https://www.youtube-nocookie.com/embed/uLzd1as3QBo?si=yokS5cLZcNJ__V4z" %}

## Utilisation

Les filtres avancés permettent de filtrer vos données sur presque tous les champs de vos entités.

* Allez dans un module de Dastra (par exemple, le module des exercices de droits
* Cliquez sur le bouton "Filtres" en haut à droite de la table de données.

<figure><img src="../../.gitbook/assets/filters_01_ok.png" alt=""><figcaption></figcaption></figure>

* Une petite fenêtre s'affiche, elle vous présente une liste de filtres standards les plus utilisés, en appliquant un de ces filtres, le tableau se met à jour automatiquement.

<figure><img src="../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

<p align="center"><sub><mark style="color:$info;">Combo de filtres avancés des demandes d'exercices de droits</mark></sub></p>

{% hint style="info" %}
La combinaison de ces filtres est cumuliative.

_Par exemple : si je filtre sur un ou deux tags "complexe" et "en attente" + je sélectionne une unité organisationnelle "Contoso" : cela m'affichera toutes les lignes qui contiennent les 2 tags "complexe" et "en attente" **et** qui sont dans l'unité organisationnelle "Contoso"_
{% endhint %}

* Si vous ne trouvez pas de filtres qui vous conviennent, vous pouvez cliquer sur le bouton "Ajouter un filtre". Là vous allez pouvoir éditer la combinaison de filtres qui correspondra le mieux à vos besoins

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

Par défaut, Dastra fait persister les filtres que vous sélectionnez, ce qui signifie que si vous changez de page ou que vous rafraîchissez votre navigateur, les filtres sont conservés. Ces filtres sont propre à votre navigateur et votre espace de travail (Ils sont stockés en **LocalStorage**).

## Vues personnalisées

Vous pouvez enregistrer l'état courant de vos filtres (et votre sélection de colonnes) sous forme de **vue nommée**, puis basculer entre vos vues en un seul clic depuis la barre d'outils de chaque liste.

Pour créer une vue :

1. Appliquez les filtres et la sélection de colonnes souhaités.
2. Cliquez sur le bouton **"Enregistrer"** dans la barre d'outils.
3. Donnez un nom à votre vue et confirmez.

La vue apparaît alors directement dans la barre d'outils de la section concernée — accessible en un clic, sans repasser par le panneau "Filtres".

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

Vous pouvez **partager une vue** avec les autres utilisateurs de votre espace de travail. Les vues partagées apparaissent sous la rubrique **"Vues partagées"** dans la barre d'outils.

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

Cette fonctionnalité est disponible dans toutes les sections listant des objets : demandes d'exercice de droits, registre des traitements, actifs, contrats, systèmes d'IA, violations de données…

## Problèmes connus

### Mes données ne s'affichent plus ?

Se vous rencontrez des difficultés avec les filtres : vous perdez l'affichage de vos données, nous vous recommandons de vider les données du navigateur (cookies, localstorage...). Cela réinitialisera le statut de vos filtres dans votre espace de travail.

### Certaines colonnes ne sont pas présentes dans les filtres avancées ?

Ils se peut que techniquement, il ne soit pas possible de mettre en place ces filtres pour diverses raison. Nous vous recommandons dans ce cas, soit d'exporter de manière brute les données, et effectuer le rapport dans des outils comme Excel.

Si c'est un filtre qui est essentiel à votre activité, n'hésitez pas à nous faire une demande de nouvelle fonctionnalité [via la communauté Dastra ou le système de demandes](../../getting-started/le-support/faire-une-demande-de-support.md)
