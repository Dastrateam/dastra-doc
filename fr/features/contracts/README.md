---
description: >-
  Déclarez, faites signer et suivez vos contrats, politiques et autres documents
  juridiques directement dans Dastra.
---

# Contrats et politiques

Le module **Contrats et politiques** de Dastra sert à déclarer, modifier, faire signer et versionner vos documents juridiques et organisationnels : contrats, politiques, notices et procédures. Chaque document est relié aux actifs, aux acteurs et aux utilisateurs concernés, pour que vos engagements restent cohérents avec votre registre et vos référentiels.

## Accéder au module

Votre souscription doit inclure la fonctionnalité contrats. Si elle est active dans votre plan, ouvrez **Opérations** > **Contrats et politiques** dans le menu latéral. Le module propose trois entrées :

* **Registre des contrats et politiques** : la liste de vos documents.
* **Statistiques** : les indicateurs et graphiques du module (voir [Statistiques](README.md#statistiques)).
* **Modèles de documents** : les modèles qui servent à générer des documents (voir [Modèles de contrats dynamiques](templates.md)). Cette entrée n'est pas affichée aux utilisateurs dont le rôle est `User`.

<figure><img src="../../.gitbook/assets/contracts-readme-1.png" alt="Le menu latéral avec le groupe Opérations ouvert sur Contrats et politiques et ses trois entrées"><figcaption><p>Le module Contrats et politiques dans le menu latéral</p></figcaption></figure>

## Types de document

Chaque document a un type : **Contrat**, **Politique**, **Notice**, **Procédure** ou **Autre**. Vous choisissez le type à la création (voir [Créer un document](declare.md)). Pour le modifier ensuite, cliquez sur le badge du type, à côté du titre du document.

Dans le registre, le filtre **Types** limite la liste à un ou plusieurs types.

## Le registre des documents

Le registre liste vos documents dans un tableau dont vous choisissez les colonnes, par exemple la version, le nombre de signatures, le nombre de pièces jointes et l'échéance. Filtrez le registre par unité organisationnelle, étape, statut des signatures, type, statut, tag ou utilisateur.

Le bouton **Créer un document** ouvre l'assistant de création (voir [Créer un document](declare.md)). La flèche à sa droite déroule les autres actions du module :

* **Importer** : importer plusieurs documents depuis un fichier.
* **Exporter** : exporter la liste.
* **Configurer revue régulière** : définir la périodicité de revue des documents (voir [Revue régulière des documents](review.md)).
* **Transformer emails en documents** : créer des documents à partir des e-mails reçus sur une adresse de collecte.
* **Lire la documentation** : ouvrir cette documentation.

<figure><img src="../../.gitbook/assets/contracts-readme-2.png" alt="Le registre des contrats et politiques avec le menu du bouton Créer un document déroulé"><figcaption><p>Le registre et les actions du bouton Créer un document</p></figcaption></figure>

## Importer et exporter

**Importer** ouvre l'assistant d'import des documents. Il est réservé aux utilisateurs qui disposent du droit d'import sur les contrats. Le fonctionnement de l'assistant est décrit dans [Importer vos données (Excel, Csv)](../general/import.md).

**Exporter** ouvre une fenêtre où vous choisissez le format : CSV, XLSX, JSON, PDF, HTML, DOCX ou Markdown. Depuis le registre, l'export porte sur la liste. Depuis un document, le menu du bouton **Enregistrer** propose **Exporter** pour ce seul document, avec l'option **Inclure les documents** pour y joindre ses pièces jointes.

## Créer des documents depuis vos e-mails

L'entrée **Transformer emails en documents** mène à l'intégration des adresses e-mail de collecte. Une fois l'adresse créée pour les contrats, chaque e-mail reçu crée un document : l'objet devient le nom, le corps devient la description et les pièces jointes valides sont rattachées au document. L'installation, qui demande le droit de gérer les intégrations, est décrite dans [Adresses emails de collecte](../settings/mailboxes.md).

## Statistiques

L'entrée **Statistiques** affiche une vue d'ensemble de vos documents. Les indicateurs du haut donnent le nombre de documents **En retard**, le **Total**, les **Brouillons** et les **Publiés**. Un clic sur un indicateur ouvre la liste correspondante.

Les graphiques montrent :

* **Nouveaux documents** : l'évolution du nombre de documents de l'espace de travail et le nombre de documents créés à chaque date.
* **Signataires** : le nombre de documents par signataire.
* **Etapes** : le nombre de documents par étape de processus.
* **Tags** : le nombre de documents par tag.
* **Documents par unités organisationnelles** : le nombre de documents de chaque unité organisationnelle, pour chaque étape.

Le bouton **Filtres** restreint les indicateurs et les graphiques, et **Imprimer** produit une version imprimable. L'indicateur **En retard** s'appuie sur la date de fin des documents : renseignez-la dans l'onglet **Détails** (voir [Détails et pièces jointes](documents.md)).

<figure><img src="../../.gitbook/assets/contracts-readme-3.png" alt="La page Statistiques avec les quatre indicateurs et les graphiques"><figcaption><p>La page Statistiques du module</p></figcaption></figure>
