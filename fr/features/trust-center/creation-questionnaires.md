---
description: >-
  Collectez des projets de traitements, d'incidents, d'actifs, de contrats, de
  systèmes d'IA ou d'acteurs depuis un Trust Center avec des modèles de
  questionnaires de création.
---

# Collecter des projets de traitements, d'incidents, d'actifs, de contrats, de systèmes d'IA ou d'acteurs

Des modèles de questionnaires sont conçus pour fonctionner avec un Trust Center. Ils fonctionnent comme les autres modèles, mais une fois la réponse validée, ses données peuvent être transformées en un objet de Dastra. Six types de modèles existent :

* **Collecte de projet de traitement** : un traitement ;
* **Création de violations de données** : une violation de données ;
* **Création d'actif** : un actif du référentiel ;
* **Création de contrat** : un contrat ;
* **Création d'un système d'IA** : un système d'IA ;
* **Création d'acteur** : un acteur.

## Ajouter un modèle

1. Dans le module Questionnaires, ouvrez la liste **Modèles de questionnaires** et cliquez sur **Créer modèle**.
2. Dans la fenêtre **Choisir le type de questionnaire**, choisissez **A partir d'un modèle**.
3. Dans la bibliothèque, filtrez par **Types** ou recherchez le modèle souhaité, puis cliquez dessus.

Le modèle est ajouté à votre espace de travail et vous êtes redirigé vers sa page de gestion. Pour le proposer aux visiteurs, ajoutez-le ensuite à votre Trust Center : voir [Questionnaires](configuration/questionnaires.md). Pour le détail de la création d'un modèle, voir [Créer un modèle de questionnaire](../questionnaires/templates/README.md).

## Contenu du modèle

Chaque modèle comprend une liste de questions qui couvrent les champs nécessaires pour créer l'objet correspondant dans Dastra.

## Transformer une réponse en objet

Les réponses données depuis le Trust Center arrivent dans le module Questionnaires, dans l'unité organisationnelle du Trust Center. Le bouton de transformation n'apparaît que lorsque la réponse est validée. Il est actif pour les approbateurs de la réponse.

Sur la page de la réponse validée, le bouton s'intitule :

* **Création d'objet** suivi du type d'objet, par exemple **Création d'objet (Traitement de données)**, tant que la réponse n'est liée à aucun objet ;
* **Fusionner les données** suivi du type d'objet, lorsque la réponse est déjà liée à un objet.

Chaque réponse est reliée au champ correspondant de l'objet. Pour la procédure complète, voir [Fusionner les réponses avec l'objet attaché](../questionnaires/monitor.md#fusionner-les-reponses-avec-lobjet-attache).

## Modifier le modèle

Chaque question est liée à un champ de l'objet à créer : modifier le modèle peut donc empêcher la transformation des réponses. Nous vous recommandons d'utiliser le modèle tel qu'il est proposé dans la bibliothèque.
