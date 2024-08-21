---
description: >-
  Découvrez comment utiliser notre intégration native de boites emails de
  collecte
---

# Adresses emails de collecte

### Introduction

Cette intégration permet de créer automatiquement des objets dans Dastra à partir d'e-mails reçus sur des boîtes emails dédiées. Dastra s'occupe de mettre à disposition ces boites et automatise la transformation des emails entrants en objets dans l'application Dastra.

5 types d'objets peuvent être associés à ces boites emails de collecte:

* **Tâches**
* **Traitements de données**
* **Demandes d'exercices de droits**
* **Contrats**
* **Violations de données**

### Mise en place d'une boite de collecte

Pour mettre en place une boite de collecte pour l'un des objets listés ci-dessus, rendez-vous dans les réglages de votre espace de travail, onglet intégrations et sélectionnez la carte "Adresse mail de collecte"

<figure><img src="../../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>

Sélectionnez ensuite le type d'objet pour lequel vous souhaitez mettre en place l'intégration en cliquant sur "ajouter l'intégration". Il est important de noter que vous ne pouvez disposer que d'une seule boite mail de collecte par type d'objet et par espace de travail.

<figure><img src="../../.gitbook/assets/image (380).png" alt=""><figcaption></figcaption></figure>

Vous avez la possiblité de renseigner l'unité organisationnelle de destination des objets créés via cette boite de collecte lors de l'installation de l'intégration. En laissant ce champ vide, les objets seront créés dans l'unité organisationnelle defaut.

<figure><img src="../../.gitbook/assets/image (381).png" alt=""><figcaption></figcaption></figure>

En cliquant sur "Créer", Dastra finalise l'installation de l'intégration et met à votre disposition l'adresse email à utiliser.

<figure><img src="../../.gitbook/assets/image (382).png" alt=""><figcaption></figcaption></figure>

### Fonctionnalités principales

* **Création Automatique d'Objets** : Chaque e-mail reçu sur une boite email associée crée un objet correspondant dans Dastra.
* **Paramétrage de l'Unité Organisationnelle** : Vous pouvez définir une unité organisationnelle de destination lors de l'installation. Si cette unité est spécifiée, l'objet est automatiquement créé dans cette unité.
* **Gestion des Champs d'Objet** :
  * **Label** : Le sujet de l'e-mail est repris comme nom de l'objet créé.
  * **Description** : Le corps de l'e-mail est utilisé pour la description de l'objet créé.
  * **Pièces Jointes** : Les pièces jointes de l'e-mail sont ajoutées en tant que pièces jointes de l'objet, sous réserve des conditions de validation.

### La gestion des pièces jointes

Les pièces jointes de l'e-mail sont ajoutées en tant que pièces jointes de l'objet, sous réserve que:

* **Les Extensions de fichiers sont valides** : seules les pièces jointes avec une extension de fichier valide seront conservées.
* **Les images respectent une taille minimale** : pour les fichiers de type image (jpg, png, gif, etc.), une taille minimale de 5 KB est requise. Cette contrainte permet d'éviter l'inclusion d'images non pertinentes comme celles des signatures d'e-mails.

### Retrouver les objets générés depuis une boite de collecte

Les objets concernés par les boites de collecte disposent d'un champ 'source' ou 'origine de collecte' que vous pouvez afficher dans les vues tableaux en affichant la colonne source / origine de collecte.

Tous les objets générés depuis une boite de collecte sont taggés email entrant vous permettant de les identifier facilement si besoin.

### Notification de succès

En cas de création réussie d'un objet suite à la réception d'un e-mail sur la boite de collecte, une notification par e-mail est automatiquement envoyée à l'adresse qui a déclenché l'intégration. Cette notification confirme que l'objet a été créé avec succès dans Dastra, fournissant ainsi une assurance immédiate que la demande ou l'action a bien été prise en compte.

La langue de l'email de confirmation correspond à la langue par défaut de l'espace de travail dans lequel l'intégration est installée (paramètres de votre espace de travail > langue par défaut).
