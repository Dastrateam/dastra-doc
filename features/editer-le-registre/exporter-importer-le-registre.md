---
description: Apprenez à exporter et importer un registre existant complet dans Dastra.
---

# Exporter / importer le registre

## L'export de registre

Pour exporter l'ensemble du registre, il vous suffit de vous rendre dans le module "Registre", de cliquer sur la flèche en haut à droite à côté de la création d'un traitement, puis de sélectionner "exporter le registre".

![Menu déroulant du registre comportant la fonctionnalité d'export](<../../.gitbook/assets/Capture web\_3-5-2022\_164438\_app.dastra.eu.jpeg>)

Choisissez ensuite le format d'export ainsi que le type d'export désiré (complet ou format article 30), et cliquez sur "Télécharger le fichier". Ca y est, votre registre est exporté !



### Format article 30/CNIL

Le format dit article 30 correspond à ce qui est exigé par le RGPD. L'export prendra en compte les champs obligatoires au sens du RGPD. En effet, le RGPD oblige à la création du registre des activités de traitement. Les informations contenues sont :&#x20;

* Nom du traitement
* Finalités (sans les bases légales)
* Données et conservation
* Destinataires et transferts éventuels
* Mesures de sécurité



### Format complet

Le format complet est le format natif de Dastra. Vous exportez l'ensemble des champs composant la fiche de traitement.&#x20;



{% hint style="info" %}
Il est également possible de n'exporter qu'un ou plusieurs traitements du registre, au lieu du registre entier. Pour cela, sélectionnez les traitements concernés manuellement en cochant les cases à gauche du registre, puis "Choisir une action groupée" et "Exporter".
{% endhint %}

## L'import de registre

Pour éviter de remplir chaque traitement à la main et prendre en compte tous les formats possibles de registre, Dastra a conçu une méthodologie se reposant sur le principe de la **ségrégation du registre en domaines de données**. Ainsi, 7 étapes sont conseillées pour importer l’ensemble d’un registre existant dans Dastra.

{% hint style="info" %}
Ces étapes, non obligatoires, sont néanmoins fortement conseillées notamment lorsque le registre de traitement contient de nombreux traitements.
{% endhint %}

N'hésitez pas à consulter également notre bibliothèque de modèles de traitements de données : [https://www.dastra.eu/fr/data-processing/referentials](https://www.dastra.eu/fr/data-processing/referentials)

## Etape 1 : Import des labels de traitement

Pour importer vos labels de traitements existants, il faut cliquer sur l'onglet "importer vos données" dans la section Registre, onglet Registre:

![](<../../.gitbook/assets/image (10) (1) (1).png>)

Ensuite, téléchargez un échantillon de notre fichier tel que présenté à l'écran.

![](<../../.gitbook/assets/image (11) (1) (1).png>)



Remplissez le fichier  téléchargé avec vos labels de traitements en respectant l'ordre suivant :

| Colonne          | Description                           | Valeurs possibles                                   |
| ---------------- | ------------------------------------- | --------------------------------------------------- |
| Ref              | Référence interne (string)            |                                                     |
| Processing state | Etat du traitement (processing state) | "Study", "BeingDeployed", "InProduction", "Stopped" |
| Label            | Nom (string)                          |                                                     |
| Description      | Description (String)                  |                                                     |

Ci-dessous un exemple de fichier respectant le format demandé disponible à l'import et pouvant être importé en "glisser-déposer" dans Dastra :

{% file src="../../.gitbook/assets/sample-DataProcessing (18).csv" %}

Importez-le directement dans notre interface par glisser-déposer, puis cliquez sur Continuez.&#x20;

Ca y est, vos labels de traitements sont importés !

## Etape 2 : import du référentiel des actifs

Pour importer vos applications/actifs existantes, il faut cliquer sur l'onglet "importer" dans le module Référentiels, onglet Actifs :

![](<../../.gitbook/assets/image (92).png>)

Ensuite, téléchargez un échantillon de notre fichier tel que présenté à l'écran. Remplissez le fichier  téléchargé avec vos applications en respectant l'ordre suivant :

| Colonne                    | Description                             | Valeurs possibles                       |
| -------------------------- | --------------------------------------- | --------------------------------------- |
| Description                | Description (string)                    |                                         |
| Label                      | Nom (string)                            |                                         |
| ApplicationState           | Application state (applicationstate)    | "InProduction""InDevelopment""Stopped"  |
| ApplicationType            | Application type (applicationtype)      | "Software""WebApp""Saas""Module""Other" |
| HostingType                | Hosting type (hostingtype)              | "InHouse""OutSourced"                   |
| SupportType                | Support type (supporttype)              | "InHouse""OutSourced"                   |
| DevelopmentType            | Development type (developmenttype)      | "InHouse""OutSourced"                   |
| HostName                   | Host name (string)                      |                                         |
| PrivacyByDesignImplemented | Privacy by design implemented (boolean) | "true""false"                           |

Ci-dessous un exemple de fichier respectant le format demandé disponible à l'import et pouvant être importé en "glisser-déposer" dans Dastra :

{% file src="../../.gitbook/assets/sample-applications - EXAMPLE.xlsx" %}

Importez-le directement dans notre interface par glisser-déposer, puis cliquez sur Continuez.&#x20;

Ca y est, vos applications sont importées !

## Etape 3 : import du référentiel des acteurs

Recommencez la procédure similaire aux précédentes depuis le module Référentiels, onglet Acteurs. Ci-dessous un exemple:

{% file src="../../.gitbook/assets/sample-Asset.csv" %}

Votre référentiel des acteurs référence l'ensemble des parties prenantes à un traitement. Personnes morales telles que les sous-traitants, les clients ou les responsables conjoints ou les personnes physiques telles que les interlocuteurs des traitements.&#x20;

Ce référentiel sert d'annuaire interne dans l'espace de travail. Pour chaque acteur, vous pourrez définir un type le caractérisant. Par exemple, si vous souhaitez ajouter votre référentiel de sous-traitants, vous ajoutez tous les acteurs et chaque sous-traitant devra être associé à un traitement.&#x20;

## Etape 4 : import du référentiel des mesures de sécurité

Recommencez la procédure similaire aux précédentes depuis le module Référentiels, onglet Mesures.

## Etape 5 : import du glossaire de données&#x20;

Recommencez la procédure similaire aux précédentes depuis le module Référentiels, onglet Glossaire de données.

## Etape 6 : import du référentiel des jeux de données&#x20;

Recommencez la procédure similaire aux précédentes depuis  la section Registre, onglet Règles de conservation.

## Etape 7 : Construction des liaisons&#x20;

Maintenant que les référentiels ont tous été importés, éditez chacun des traitements et remplissez les informations sur la bases des informations importées en suivant le guide ci-dessous:

{% content-ref url="remplir-le-questionnaire/" %}
[remplir-le-questionnaire](remplir-le-questionnaire/)
{% endcontent-ref %}

Ca y est, les liaisons sont construites !

