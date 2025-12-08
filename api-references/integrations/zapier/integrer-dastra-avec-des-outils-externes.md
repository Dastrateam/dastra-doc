---
description: >-
  Cette page est un guide complet expliquant comment intégrer Dastra avec des
  outils externes avec des cas pratiques.
---

# Intégrer Dastra avec des Outils Externes

Les organisations cherchent souvent à intégrer **les capacités de conformité et d’orchestration de Dastra** avec des systèmes externes tels que des outils de découverte/redaction de données, des inventaires d’actifs IT, des CRM, des systèmes de gestion des fournisseurs ou des plateformes de gestion de tâches. Ces intégrations permettent de :

* automatiser les tâches répétitives de conformité,
* synchroniser les données entre systèmes,
* garantir la cohérence réglementaire (RGPD, CCPA, etc.),
* améliorer la visibilité et la collaboration.

Ce guide présente trois modèles d’intégration (du plus léger au plus robuste), fournit des exemples de workflows et décrit les **cas d’usage typiques** avec les endpoints API de Dastra.

***

### 🔹 Modèles d’intégration

#### 1. Workflows légers avec Zapier (Webhooks + APIs)

**Idéal pour :** des automatisations simples avec de faibles ou moyens volumes de données.

**Exemple de workflow :**

1. **Déclencheur dans Dastra** → un DSAR ou un événement envoie un webhook.
2. **Zapier reçoit le webhook** → appelle l’API d’un outil externe.
3. **Résultats traités** → l’outil externe renvoie les données à Zapier.
4. **Mise à jour dans Dastra** → Zapier utilise l’API REST de Dastra pour attacher les résultats (`POST /requests/{id}/attachments`) ou mettre à jour le statut.

✅ **Avantages :** rapide à mettre en place, pas de développement nécessaire.\
⚠️ **Limites :** taille des payloads et délais d’exécution limités.

***

#### 2. Workflows intermédiaires avec Zapier + Microservice

**Idéal pour :** des workflows de taille moyenne nécessitant plus de flexibilité que Zapier seul.

**Exemple de workflow :**

1. **Déclencheur dans Dastra → Zapier.**
2. **Zapier appelle un microservice** (AWS Lambda, Azure Function, GCP Cloud Run).
3. **Le microservice exécute la logique complexe** → gestion des retries, pagination, traitement de fichiers volumineux.
4. **Le microservice renvoie les résultats** → l’API REST de Dastra met à jour les données.

✅ **Avantages :** combine la simplicité de Zapier et la robustesse d’un backend personnalisé.

***

#### 3. Intégration directe via API

**Idéal pour :** des déploiements à l’échelle entreprise, avec SLA stricts, volumes importants et exigences de sécurité avancées.

**Exemple de workflow :**

1. **Dastra appelle directement l’API externe** lorsqu’un déclencheur survient.
2. **Le système externe exécute le traitement** (découverte, classification, redaction, etc.).
3. **Les résultats sont renvoyés à Dastra** via API (`PATCH /requests/{id}`, `POST /requests/{id}/attachments`).
4. **Dastra orchestre la réponse de conformité** entre plusieurs systèmes.

✅ **Avantages :** robuste, évolutif, sans limitations de Zapier.\
⚠️ **Limites :** développement nécessaire, gestion stricte de la sécurité et des quotas API.

***

### 🔹 Choisir la bonne approche

| **Scénario**                                         | **Approche recommandée** |
| ---------------------------------------------------- | ------------------------ |
| Proof of concept, petits jeux de données             | Zapier (Webhooks + APIs) |
| Workflows intermédiaires, complexité modérée         | Zapier + Microservice    |
| Déploiements à grande échelle, hautement réglementés | Intégration API directe  |

***

### 📘 Cas d’usage & Endpoints API

Voici quelques scénarios fréquents, leur objectif et les **endpoints Dastra** à utiliser ([documentation API](https://dastra.readme.io/reference/rate-limiting)) :

#### 1. Orchestration des droits des personnes (DSAR) avec des outils externes

* **But :** Déclencher des workflows de découverte/redaction lors de la réception d’un DSAR ; agréger et attacher les résultats.
* **Endpoints :**
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`.
  * `POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`.
  * `PATCH /v1/ws/{workspaceId}/DataSubjectRequests/{id}`.

***

#### 2. Intégration avec les systèmes d’inventaire des actifs IT

* **But :** Synchroniser les actifs IT avec Dastra, les lier aux traitements et les mettre à jour automatiquement.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/Assets` / `POST /v1/ws/{workspaceId}/Assets`.
  * `PATCH /v1/ws/{workspaceId}/Assets/{id}`.
  * `POST /v1/ws/{workspaceId}/Assets/import`.

***

#### 3. Intégration avec les CRM

* **But :** Synchroniser les données clients, gérer les consentements, créer des DSAR directement depuis des événements CRM.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/Actors`, `POST /v1/ws/{workspaceId}/Actors`.
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`.
  * `GenericRelationships` / `DataProcessingRelationships`.

***

#### 4. Intégration avec les systèmes de gestion des fournisseurs

* **But :** Gérer les contrats, surveiller les risques tiers, lier fournisseurs et traitements de données.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/Contracts`, `POST /v1/ws/{workspaceId}/Contracts`.
  * `GET /v1/ws/{workspaceId}/Assets` / `Actors`.
  * `GenericRelationships`.

***

#### 5. Intégration avec les catalogues de données

* **But :** Importer des métadonnées, classifier les champs, enrichir les registres de traitements.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/DataFields`.
  * `POST /v1/ws/{workspaceId}/DataProcessings`, `PATCH /v1/ws/{workspaceId}/DataProcessings/{id}`.
  * `DataProcessingRelationships`.

***

#### 6. Intégration avec les CMS (Content Management Systems)

* **But :** Automatiser l’archivage, la suppression ou l’attachement de contenus/documents dans les workflows de conformité.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/CloudStorage/{providerName}/{fileId}`.
  * `POST /v1/ws/{workspaceId}/CloudStorage/{providerName}`.
  * `DataSubjectAttachments`.

***

#### 7. Intégration avec les systèmes de gestion de tâches

* **But :** Créer et assigner des tâches de conformité (audits, revues, relances) liées aux workflows Dastra.
* **Endpoints :**
  * `GET /v1/ws/{workspaceId}/Tasks`, `POST /v1/ws/{workspaceId}/Tasks`.
  * `PATCH /v1/ws/{workspaceId}/Tasks/{id}`.
  * `Users`, `Teams`, `Workflows`.

***

### 🚀 Points clés

* **Zapier + Dastra** = intégrations rapides, sans code, pour des cas simples.
* **Modèles hybrides** (Zapier + microservices) = flexibilité et fiabilité pour des workflows intermédiaires.
* **Intégrations API directes** = robustesse et scalabilité pour les grandes organisations.
* Avec ces modèles, Dastra peut s’intégrer de manière fluide dans les écosystèmes IT, data et business.



[Contactez-nous](https://www.dastra.eu/fr/contacts/demo) pour plus d'informations.
