---
description: (Sortie Q1 2026)
---

# Mappage des Fact Sheets de SAP LeanIX vers Dastra

### **Aperçu**

Le connecteur LeanIX → Dastra fournit une synchronisation automatisée et planifiée qui transfère des informations sélectionnées provenant des **Fact Sheets SAP LeanIX de type Application** vers les **Assets Dastra**.\
Dastra agit comme **système de destination**, recevant les métadonnées des applications LeanIX via l’API **LeanIX Pathfinder** :

```
GET /services/pathfinder/v1/factSheets (type = Application)
```

À chaque cycle de synchronisation, le connecteur analyse les applications LeanIX reçues et exécute l’une des actions suivantes dans Dastra :

* **Mettre à jour un Asset existant** si un Fact Sheet LeanIX correspondant existe déjà dans Dastra
* **Créer un nouvel Asset** si aucun Asset existant ne correspond
* **Marquer un Asset existant** si le Fact Sheet LeanIX associé a été supprimé

Cela garantit une **mise en cohérence continue** entre l’inventaire applicatif LeanIX et le catalogue d’assets de Dastra.

***

### **Vue d’architecture**

Ci-dessous une représentation conceptuelle de la synchronisation de bout en bout :

```
SAP LeanIX (Pathfinder API)
     |
     | GET /services/pathfinder/v1/factSheets (Application)
     v
 Fact Sheets (Applications)
     |
     |  Synchronisation nocturne
     v
 Dastra (Assets)
```

Lors de l’import, certains champs issus des Fact Sheets LeanIX sont directement mappés vers les propriétés des Assets Dastra.



<figure><img src="../../.gitbook/assets/image Dastra SAP LeanIX.png" alt=""><figcaption></figcaption></figure>

***

## **Processus de synchronisation**

### **1. Extraction depuis LeanIX**

Le connecteur récupère l’ensemble des Fact Sheets LeanIX de type **Application** via l’API Pathfinder.

Chaque Fact Sheet contient des identifiants, des champs descriptifs, des tags et des attributs relationnels.\
Seuls certains attributs sont importés dans Dastra.

***

### **2. Correspondance des Assets dans Dastra**

Chaque application entrante est comparée aux assets existants dans Dastra en utilisant **l’identifiant du Fact Sheet LeanIX** (`ref`).

Règles de correspondance :

* Si un Asset existe avec le même `ref` → **l’Asset est mis à jour**
* Si aucun Asset ne correspond → **un nouvel Asset est créé**

***

### **3. Gestion du cycle de vie**

Si un Asset Dastra existe mais que l’application LeanIX associée n’apparaît plus dans la réponse API :

* Dastra **ne supprime pas** l’Asset
* À la place, Dastra applique un tag spécifique :

```
leanix-todelete
```

Cela permet une gestion contrôlée du cycle de vie au lieu d’une suppression automatique.

***

### **4. Planification**

La synchronisation s’exécute **une fois par nuit** par défaut.\
Des déclencheurs supplémentaires peuvent être ajoutés selon la configuration du système.

***

## **Mappage des champs (LeanIX → Dastra)**

Le tableau suivant liste tous les champs importés depuis LeanIX et leur cible dans Dastra :

| Champ LeanIX    | Champ Dastra Asset | Description                                              |
| --------------- | ------------------ | -------------------------------------------------------- |
| displayName     | name               | Nom de l’application LeanIX                              |
| description     | description        | Description textuelle de l’application                   |
| tags\[]         | tags               | Tags LeanIX copiés dans Dastra                           |
| user (si mappé) | user               | Utilisateur lié dans Dastra, uniquement s’il existe déjà |
| id              | ref                | Identifiant unique du Fact Sheet LeanIX                  |
| (N/A)           | type               | Toujours défini à « Software » pour les assets importés  |

***

## **Comportement des tags**

### **Tags hérités**

Tous les tags issus de LeanIX sont transférés vers Dastra lors de la création ou de la mise à jour des assets.

### **Tag de suppression**

Si une application LeanIX disparaît du portefeuille, Dastra ajoute :

```
leanix-todelete
```

Ce tag reste présent jusqu’à traitement manuel, permettant aux administrateurs de :

* Archiver l’Asset
* Le retirer
* Ou supprimer le tag si l’application réapparaît

***

## **Gestion des erreurs et diagnostics**

Le connecteur journalise les événements liés à la synchronisation des données, incluant :

* Le nombre d’applications récupérées
* Les assets créés ou mis à jour
* Les assets marqués pour suppression
* Les codes de réponse de l’API
* Les incohérences de mapping ou attributs requis manquants

Les administrateurs peuvent consulter ces journaux dans Dastra (interface de logs prévue prochainement) ou via des outils externes selon la configuration.

***

## **Avantages**

#### **Alignement automatisé de l’inventaire**

Assure la cohérence du catalogue d’assets Dastra avec LeanIX sans intervention manuelle.

#### **Cycle de vie contrôlé des assets**

Le marquage au lieu de la suppression évite les pertes de données tout en préservant la traçabilité.

#### **Propagation cohérente des tags**

Les stratégies de tagging LeanIX sont reflétées dans Dastra, soutenant la classification, les workflows et le reporting.

#### **Modèle d’Asset logiciel standardisé**

Toutes les applications importées utilisent un type d’Asset uniforme (« Software »), facilitant la gouvernance et le traitement.

***

## **Améliorations futures**&#x20;

Extensions potentielles à l’étude :

* Synchronisation bi-directionnelle
* Configuration personnalisable du mapping de champs
* Support d’autres types de Fact Sheets (IT Component, Business Capability, etc.)
* Déclencheurs de synchronisation en temps réel au lieu du traitement nocturne
