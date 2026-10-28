---
description: Faites l'inventaire des données transférées hors de l'UE.
---

# Transferts de données hors UE

Le transfert peut être défini comme toute communication, copie ou déplacement de données personnelles ayant vocation à être traitées dans un pays tiers à l’Union européenne.

Les transferts de données hors de l’Union européenne sont par principe interdits.

Les [**articles 44 à 49 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre5) prévoient des exceptions à cette interdiction. Ils prévoient l’utilisation d’outils qui encadrent le transfert :

* une décision d’adéquation de la Commission européenne concernant certains pays assurant un niveau de protection adéquat ;
* des clauses contractuelles types (CCT) de la Commission européenne ;
* des règles internes d’entreprise (BCR) ;
* des clauses contractuelles spécifiques (considérées comme conformes aux modèles de clauses de la Commission européenne) ;
* des clauses contractuelles types adoptées par une autorité de contrôle et approuvées par la Commission européenne ;
* un code de conduite approuvé (comportant l’engagement contraignant et exécutoire pris par les destinataires hors UE d’appliquer les garanties appropriées) ;
* un mécanisme de certification approuvé (comportant l’engagement contraignant et exécutoire pris par les destinataires hors UE d’appliquer les garanties appropriées) ;
* un arrangement administratif ou un texte juridiquement contraignant et exécutoire pris pour permettre la coopération entre autorités publiques (Memorandum of Understanding dit MoU, convention internationale, etc.).

Des dérogations sont prévues à l’[**article 49 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre5). Si une dérogation justifie le transfert, il faut indiquer la nature de celle-ci et, le cas échéant, détailler l’évaluation des circonstances du transfert et les garanties appropriées.

## Déclarer un transfert dans Dastra

Les transferts se déclarent sur chaque destinataire, dans la section **Destinataires** du traitement.

1. Ouvrez le destinataire, ou créez-en un avec **Créer un destinataire**.
2. En bas du panneau du destinataire, cliquez sur **Ajouter un transfert de données**.
3. Remplissez le panneau **Éditer un transfert de données** :
   * **Description du transfert de données** (facultatif) ;
   * **Pays** : le pays vers lequel les données sont transférées ;
   * **Mécanisme de transfert de données** (obligatoire) : l'outil qui encadre le transfert ;
   * **Description du mécanisme de transfert de données** (facultatif), par exemple pour détailler une dérogation.
4. Cliquez sur **Ajouter** dans le panneau du transfert, puis sur **Ajouter** (ou **Modifier** pour un destinataire existant) dans le panneau du destinataire.

La liste **Mécanisme de transfert de données** propose les options suivantes :

* **Non renseigné**
* **Transfert encadré par le RGPD**
* **Clauses contractuelles type de l'UE**
* **Règles internes d'entreprise**
* **Décision d’adéquation**
* **Dérogation (article 49)**
* **Clauses contractuelles type adoptées par une autorité de contrôle**
* **Code de conduite approuvé**
* **Mécanisme de certification approuvé**
* **Clauses contractuelles autorisées par une autorité de contrôle**
* **Arrangement administratif autorisé par une autorité de contrôle**
* **Accord international**
* **Autre**

Les transferts d'un destinataire sont listés dans son panneau avec leur **Pays**, leur description et leur **Mécanisme de transfert de données**. Ils sont résumés dans la colonne **Transferts** de la liste des destinataires.

{% hint style="info" %}
Lorsque l'acteur ou l'unité organisationnelle que vous sélectionnez comme destinataire se trouve dans un autre pays, Dastra propose d'ajouter un transfert vers ce pays. Cliquez sur **Ajouter** dans la suggestion.
{% endhint %}

## Aller plus loin

* Si vous utilisez les [questionnaires](../../../questionnaires/README.md), Dastra propose de créer une analyse d'impact des transferts (TIA) dès qu'un transfert est déclaré : **Créer un questionnaire d'impact de transfert (TIA)**.
* Si vous utilisez le module Contrats, le bouton **CCT transfert** d'un destinataire génère les clauses contractuelles types de ses transferts (voir [Destinataires](README.md#generer-un-dpa)).
* Un transfert vers un pays qui n'offre pas un niveau de protection adéquat augmente l'indicateur **Sensibilité** du traitement.
* Tous les transferts de vos traitements sont visibles sur la [carte des transferts](../../visualization/transfers-map.md).
