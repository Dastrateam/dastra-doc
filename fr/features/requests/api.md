---
description: >-
  Cette page vous explique comment manipuler directement vos demandes d'exercice de droits dans Dastra sans intégrer le SDK javascript grâce à notre API Rest.
---

# Intégration de l'API

Dastra ne s'intégrant pas nativement à toutes les plateformes de développement, nous mettons à votre disposition une API Rest pour gérer vos demandes d'exercice de droits depuis vos applications.

## L'objet demande d'exercice de droits

Vous trouverez ci-dessous le modèle objet au format JSON d'une demande d'exercice de droits dans Dastra.

<details>

<summary>L'objet demande d'exercice de droits</summary>

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Access to my personal data",
  "locale": "en",
  "state": "Open",
  "channel": "Widget",
  "externalSource": "None",
  "externalId": null,
  "refId": null,
  "userId": null,
  "widgetId": 29,
  "widget": {
    "label": "Privacy requests",
    "id": 29,
    "tenantId": 20
  },
  "purposes": [
    "Access"
  ],
  "complex": false,
  "description": null,
  "message": "I would like to receive a copy of my personal data.",
  "resolutionMessage": null,
  "givenName": "Jane",
  "familyName": "Doe",
  "email": "jane.doe@example.com",
  "phoneNumber": null,
  "address": null,
  "zipCode": null,
  "city": null,
  "countryCode": "GB",
  "subjectCategoryId": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
  "subjectCategory": {
    "id": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
    "label": "Customers",
    "ref": null,
    "dateCreation": "2026-03-02T08:00:00Z",
    "dateUpdate": null,
    "creatorUserId": 4128,
    "creatorUser": null,
    "description": null,
    "minorConcerned": false,
    "workflowStepId": null,
    "workflowStep": null,
    "dataRetentionRules": []
  },
  "areaId": 120,
  "area": {
    "type": "Entity",
    "id": 120,
    "label": "Brightmoor UK"
  },
  "areaOwnerId": null,
  "operatorId": 4128,
  "operator": {
    "id": 4128,
    "displayName": "Emma Walsh",
    "familyName": "Walsh",
    "givenName": "Emma",
    "email": "emma.walsh@example.com",
    "active": true,
    "color": "#1E8EE1",
    "avatarUrl": null,
    "tenantId": 20
  },
  "creator": null,
  "updatedBy": null,
  "closedByUser": null,
  "workflowStepId": 22290,
  "workflowStep": {
    "type": "DataSubjectRequest",
    "id": 22290,
    "label": "New",
    "color": "#1E8EE1",
    "order": 0,
    "itemLimit": null,
    "finalStep": false,
    "initialStep": true,
    "authorizedRole": null,
    "authorizedRoleId": null,
    "descriptionHtml": null,
    "mappedState": "Open"
  },
  "dateDemand": "2026-10-12T09:15:42.381Z",
  "dateCreation": "2026-10-12T09:15:42.381Z",
  "dateUpdate": null,
  "expiryTime": "2026-11-11T09:15:42.381Z",
  "remainingDays": 13,
  "forecastedExpiryDate": "2026-11-11T09:15:42.381Z",
  "isOverdue": false,
  "suspensionDate": null,
  "suspensionJustification": null,
  "suspensionTime": 0,
  "suspensionRealTime": 0,
  "nbSuspensions": 0,
  "dateClosed": null,
  "closedReason": "None",
  "closedReasonDescription": null,
  "closedReasonInternalDescription": null,
  "closingTime": null,
  "overdueTime": null,
  "archived": false,
  "archivedDate": null,
  "anonymizationDate": null,
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "nbMessagesIncoming": 0,
  "nbMessagesWithErrors": 0,
  "lastMessageDate": null,
  "userNotified": false,
  "dateUserNotified": null,
  "sendNotification": false,
  "emailValidationDate": "2026-10-12T09:16:10.554Z",
  "mailValidated": true,
  "identityValidated": false,
  "dateIdentityValidated": null,
  "referrerUrl": "https://www.example.com/privacy",
  "demandId": "k7Xq2mP9",
  "dataProcessedCount": 0,
  "dataToProcessCount": 3,
  "dataProcessedByAssetOwnersAt": null,
  "customFields": {
    "13_long": "1234567891234",
    "13_html": "<p>Example</p>"
  },
  "attachments": [],
  "messages": [],
  "tags": []
}
```

</details>

Pour obtenir le format de l'objet avec vos champs personnalisés, exportez une demande au format JSON : vous récupérez ainsi le modèle JSON de votre espace de travail.

Les identifiants des demandes sont des GUID (par exemple `3fa85f64-5717-4562-b3fc-2c963f66afa6`). L'identifiant de l'espace de travail est un entier.

## Les endpoints de l'API

Voici les principaux endpoints qui vous seront utiles pour intégrer vos applications avec le module Exercices des droits de Dastra.

### Créer une nouvelle demande d'exercice de droits dans Dastra

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

#### Paramètres d'URL

| Nom                                             | Type    | Description                          |
| ----------------------------------------------- | ------- | ------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail |

#### Corps de la requête

| Nom                                          | Type          | Description                                                                                                       |
| -------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------- |
| `title`<mark style="color:red;">\*</mark>    | String        | Titre de la demande                                                                                               |
| `message`                                    | String        | Texte de la demande                                                                                               |
| `locale`<mark style="color:red;">\*</mark>   | String        | Langue du demandeur (par exemple `fr`, `en`)                                                                      |
| `areaId`<mark style="color:red;">\*</mark>   | Integer       | Identifiant de l'unité organisationnelle de la demande                                                            |
| `email`                                      | String        | Adresse e-mail du demandeur                                                                                       |
| `dateDemand`                                 | DateTime      | Date de la demande (par défaut, la date du jour)                                                                  |
| `purposes`<mark style="color:red;">\*</mark> | Array\[String] | Types de demande concernés (au moins un). Valeurs possibles : voir le paramètre `purposes` de la liste ci-dessous |

{% tabs %}
{% tab title="201: Created" %}
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Access to my personal data",
  "locale": "en",
  "state": "Open",
  "channel": "Widget",
  "externalSource": "None",
  "externalId": null,
  "refId": null,
  "userId": null,
  "widgetId": 29,
  "purposes": [
    "Access"
  ],
  "complex": false,
  "description": null,
  "message": "I would like to receive a copy of my personal data.",
  "resolutionMessage": null,
  "givenName": "Jane",
  "familyName": "Doe",
  "email": "jane.doe@example.com",
  "phoneNumber": null,
  "address": null,
  "zipCode": null,
  "city": null,
  "countryCode": "GB",
  "subjectCategoryId": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
  "subjectCategory": {
    "id": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
    "label": "Customers",
    "ref": null,
    "dateCreation": "2026-03-02T08:00:00Z",
    "dateUpdate": null,
    "creatorUserId": 4128,
    "creatorUser": null,
    "description": null,
    "minorConcerned": false,
    "workflowStepId": null,
    "workflowStep": null,
    "dataRetentionRules": []
  },
  "areaId": 120,
  "workflowStepId": 22290,
  "workflowStep": {
    "type": "DataSubjectRequest",
    "id": 22290,
    "label": "New",
    "color": "#1E8EE1",
    "order": 0,
    "itemLimit": null,
    "finalStep": false,
    "initialStep": true,
    "authorizedRole": null,
    "authorizedRoleId": null,
    "descriptionHtml": null,
    "mappedState": "Open"
  },
  "dateDemand": "2026-10-12T09:15:42.381Z",
  "dateCreation": "2026-10-12T09:15:42.381Z",
  "dateUpdate": null,
  "expiryTime": "2026-11-11T09:15:42.381Z",
  "isOverdue": false,
  "suspensionDate": null,
  "suspensionJustification": null,
  "dateClosed": null,
  "closedReason": "None",
  "closedReasonDescription": null,
  "closedReasonInternalDescription": null,
  "archived": false,
  "archivedDate": null,
  "anonymizationDate": null,
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "nbMessagesIncoming": 0,
  "nbMessagesWithErrors": 0,
  "lastMessageDate": null,
  "userNotified": false,
  "dateUserNotified": null,
  "sendNotification": false,
  "emailValidationDate": "2026-10-12T09:16:10.554Z",
  "mailValidated": true,
  "identityValidated": false,
  "dateIdentityValidated": null,
  "referrerUrl": "https://www.example.com/privacy",
  "demandId": "k7Xq2mP9"
}
```
{% endtab %}
{% endtabs %}

### Récupérer une demande d'exercice de droits existante via son identifiant

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |
| `id`<mark style="color:red;">\*</mark>          | GUID    | L'identifiant (GUID) de la demande d'exercice de droits                                    |

{% tabs %}
{% tab title="200: OK" %}
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Access to my personal data",
  "locale": "en",
  "state": "Open",
  "channel": "Widget",
  "externalSource": "None",
  "externalId": null,
  "refId": null,
  "userId": null,
  "widgetId": 29,
  "widget": {
    "label": "Privacy requests",
    "id": 29,
    "tenantId": 20
  },
  "purposes": [
    "Access"
  ],
  "complex": false,
  "description": null,
  "message": "I would like to receive a copy of my personal data.",
  "resolutionMessage": null,
  "givenName": "Jane",
  "familyName": "Doe",
  "email": "jane.doe@example.com",
  "phoneNumber": null,
  "address": null,
  "zipCode": null,
  "city": null,
  "countryCode": "GB",
  "subjectCategoryId": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
  "subjectCategory": {
    "id": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
    "label": "Customers",
    "ref": null,
    "dateCreation": "2026-03-02T08:00:00Z",
    "dateUpdate": null,
    "creatorUserId": 4128,
    "creatorUser": null,
    "description": null,
    "minorConcerned": false,
    "workflowStepId": null,
    "workflowStep": null,
    "dataRetentionRules": []
  },
  "areaId": 120,
  "area": {
    "type": "Entity",
    "id": 120,
    "label": "Brightmoor UK"
  },
  "areaOwnerId": null,
  "operatorId": 4128,
  "operator": {
    "id": 4128,
    "displayName": "Emma Walsh",
    "familyName": "Walsh",
    "givenName": "Emma",
    "email": "emma.walsh@example.com",
    "active": true,
    "color": "#1E8EE1",
    "avatarUrl": null,
    "tenantId": 20
  },
  "creator": null,
  "updatedBy": null,
  "closedByUser": null,
  "workflowStepId": 22290,
  "workflowStep": {
    "type": "DataSubjectRequest",
    "id": 22290,
    "label": "New",
    "color": "#1E8EE1",
    "order": 0,
    "itemLimit": null,
    "finalStep": false,
    "initialStep": true,
    "authorizedRole": null,
    "authorizedRoleId": null,
    "descriptionHtml": null,
    "mappedState": "Open"
  },
  "dateDemand": "2026-10-12T09:15:42.381Z",
  "dateCreation": "2026-10-12T09:15:42.381Z",
  "dateUpdate": null,
  "expiryTime": "2026-11-11T09:15:42.381Z",
  "remainingDays": 13,
  "forecastedExpiryDate": "2026-11-11T09:15:42.381Z",
  "isOverdue": false,
  "suspensionDate": null,
  "suspensionJustification": null,
  "suspensionTime": 0,
  "suspensionRealTime": 0,
  "nbSuspensions": 0,
  "dateClosed": null,
  "closedReason": "None",
  "closedReasonDescription": null,
  "closedReasonInternalDescription": null,
  "closingTime": null,
  "overdueTime": null,
  "archived": false,
  "archivedDate": null,
  "anonymizationDate": null,
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "nbMessagesIncoming": 0,
  "nbMessagesWithErrors": 0,
  "lastMessageDate": null,
  "userNotified": false,
  "dateUserNotified": null,
  "sendNotification": false,
  "emailValidationDate": "2026-10-12T09:16:10.554Z",
  "mailValidated": true,
  "identityValidated": false,
  "dateIdentityValidated": null,
  "referrerUrl": "https://www.example.com/privacy",
  "demandId": "k7Xq2mP9",
  "dataProcessedCount": 0,
  "dataToProcessCount": 3,
  "dataProcessedByAssetOwnersAt": null,
  "customFields": {
    "13_long": "1234567891234",
    "13_html": "<p>Example</p>"
  },
  "attachments": [],
  "messages": [],
  "tags": []
}
```
{% endtab %}
{% endtabs %}

### Récupérer une liste paginée de demandes d'exercice de droits

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

Vous pouvez passer des paramètres de recherche optionnels pour filtrer la réponse de l'API.

#### Paramètres d'URL

| Nom                                             | Type    | Description                                       |
| ----------------------------------------------- | ------- | ------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail à interroger |

#### Paramètres de requête

| Nom          | Type           | Description                                                                                                                                                                                                                                                                                                                 |
| ------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `overtaking` | Boolean        | Rechercher les demandes dont le délai légal de réponse est dépassé                                                                                                                                                                                                                                                          |
| `archived`   | Boolean        | Retourner les demandes de la corbeille (`false` par défaut)                                                                                                                                                                                                                                                                 |
| `q`          | String         | Recherche texte dans le titre de la demande                                                                                                                                                                                                                                                                                 |
| `widgetId`   | Integer        | Filtrer les demandes issues d'un formulaire de collecte                                                                                                                                                                                                                                                                     |
| `areaId`     | Integer        | Filtrer les demandes d'une unité organisationnelle                                                                                                                                                                                                                                                                          |
| `states`     | Array\[String] | Filtrer les demandes par état (Open, IdentityValidation, Processing, Active, Closed)                                                                                                                                                                                                                                        |
| `purposes`   | Array\[String] | Filtrer les demandes par type (Unknown, Information, Access, Rectification, Erasure, Restriction, Opposition, Portability, AdvanceDirectives, AutomatedDecision, AdministrativeAccess, DPORequest, ThirdPartyRequest, DataProtectionComplaint, DoNotSellOrShare, LimitUseSensitivePersonalInformation, WithdrawalOfConsent) |
| `ids`        | Array\[GUID]   | Sélectionner une liste de demandes par leurs identifiants                                                                                                                                                                                                                                                                   |
| `tags`       | Array\[GUID]   | Sélectionner les demandes ayant des tags spécifiques (passer un tableau d'identifiants de tags en query string)                                                                                                                                                                                                             |
| `page`       | Integer        | La page à récupérer (la première page est 1)                                                                                                                                                                                                                                                                                |
| `size`       | Integer        | Le nombre d'éléments retournés par page (20 par défaut)                                                                                                                                                                                                                                                                     |
| `skip`       | Integer        | Le nombre d'éléments à ignorer (remplace `page` s'il est fourni)                                                                                                                                                                                                                                                            |
| `sortBy`     | String         | Le champ utilisé pour ordonner les éléments                                                                                                                                                                                                                                                                                 |
| `asc`        | Boolean        | `true` pour un tri ascendant                                                                                                                                                                                                                                                                                                |

{% tabs %}
{% tab title="200: OK" %}
```json
{
  "items": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "title": "Access to my personal data",
      "locale": "en",
      "state": "Open",
      "channel": "Widget",
      "externalSource": "None",
      "externalId": null,
      "refId": null,
      "userId": null,
      "widgetId": 29,
      "widget": {
        "label": "Privacy requests",
        "id": 29,
        "tenantId": 20
      },
      "purposes": [
        "Access"
      ],
      "complex": false,
      "description": null,
      "message": "I would like to receive a copy of my personal data.",
      "resolutionMessage": null,
      "givenName": "Jane",
      "familyName": "Doe",
      "email": "jane.doe@example.com",
      "phoneNumber": null,
      "address": null,
      "zipCode": null,
      "city": null,
      "countryCode": "GB",
      "subjectCategoryId": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
      "subjectCategory": {
        "id": "0c5f4a52-6d1e-4c1b-9a47-3c3b9f6f1a10",
        "label": "Customers",
        "ref": null,
        "dateCreation": "2026-03-02T08:00:00Z",
        "dateUpdate": null,
        "creatorUserId": 4128,
        "creatorUser": null,
        "description": null,
        "minorConcerned": false,
        "workflowStepId": null,
        "workflowStep": null,
        "dataRetentionRules": []
      },
      "areaId": 120,
      "area": {
        "type": "Entity",
        "id": 120,
        "label": "Brightmoor UK"
      },
      "areaOwnerId": null,
      "operatorId": 4128,
      "operator": {
        "id": 4128,
        "displayName": "Emma Walsh",
        "familyName": "Walsh",
        "givenName": "Emma",
        "email": "emma.walsh@example.com",
        "active": true,
        "color": "#1E8EE1",
        "avatarUrl": null,
        "tenantId": 20
      },
      "creator": null,
      "updatedBy": null,
      "closedByUser": null,
      "workflowStepId": 22290,
      "workflowStep": {
        "type": "DataSubjectRequest",
        "id": 22290,
        "label": "New",
        "color": "#1E8EE1",
        "order": 0,
        "itemLimit": null,
        "finalStep": false,
        "initialStep": true,
        "authorizedRole": null,
        "authorizedRoleId": null,
        "descriptionHtml": null,
        "mappedState": "Open"
      },
      "dateDemand": "2026-10-12T09:15:42.381Z",
      "dateCreation": "2026-10-12T09:15:42.381Z",
      "dateUpdate": null,
      "expiryTime": "2026-11-11T09:15:42.381Z",
      "remainingDays": 13,
      "forecastedExpiryDate": "2026-11-11T09:15:42.381Z",
      "isOverdue": false,
      "suspensionDate": null,
      "suspensionJustification": null,
      "suspensionTime": 0,
      "suspensionRealTime": 0,
      "nbSuspensions": 0,
      "dateClosed": null,
      "closedReason": "None",
      "closedReasonDescription": null,
      "closedReasonInternalDescription": null,
      "closingTime": null,
      "overdueTime": null,
      "archived": false,
      "archivedDate": null,
      "anonymizationDate": null,
      "nbMessages": 0,
      "nbMessagesNotViewed": 0,
      "nbMessagesIncoming": 0,
      "nbMessagesWithErrors": 0,
      "lastMessageDate": null,
      "userNotified": false,
      "dateUserNotified": null,
      "sendNotification": false,
      "emailValidationDate": "2026-10-12T09:16:10.554Z",
      "mailValidated": true,
      "identityValidated": false,
      "dateIdentityValidated": null,
      "referrerUrl": "https://www.example.com/privacy",
      "demandId": "k7Xq2mP9",
      "dataProcessedCount": 0,
      "dataToProcessCount": 3,
      "dataProcessedByAssetOwnersAt": null,
      "customFields": {
        "13_long": "1234567891234",
        "13_html": "<p>Example</p>"
      },
      "attachments": [],
      "messages": [],
      "tags": []
    }
  ],
  "total": 1,
  "size": 20,
  "page": 1
}
```
{% endtab %}
{% endtabs %}

### Mettre à jour une demande d'exercice de droits

<mark style="color:orange;">`PUT`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |
| `id`<mark style="color:red;">\*</mark>          | GUID    | L'identifiant (GUID) de la demande d'exercice de droits                                    |

#### Corps de la requête

| Nom                  | Type   | Description                                                                                                                                                                                                      |
| -------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataSubjectRequest` | Object | L'objet complet de la demande d'exercice de droits (voir plus haut ou notre [documentation d'API Swagger](https://api.dastra.eu/swagger/index.html)). Son champ `id` doit correspondre à l'identifiant de l'URL. |

{% tabs %}
{% tab title="204: No Content" %}
La réponse n'a pas de contenu.
{% endtab %}
{% endtabs %}

### Supprimer une demande d'exercice de droits via son identifiant

<mark style="color:red;">`DELETE`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

Attention, cette action est irréversible : la demande d'exercice de droits est supprimée définitivement de nos bases de données. Pour la déplacer dans la corbeille sans la supprimer, utilisez l'endpoint d'archivage ci-dessous.

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |
| `id`<mark style="color:red;">\*</mark>          | GUID    | L'identifiant (GUID) de la demande d'exercice de droits                                    |

{% tabs %}
{% tab title="200: OK" %}
La réponse n'a pas de contenu.
{% endtab %}
{% endtabs %}

### Changer l'étape de processus de la demande d'exercice de droits

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/workflow`

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |

#### Corps de la requête

| Nom                                        | Type    | Description                                                                                               |
| ------------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------- |
| `id`<mark style="color:red;">\*</mark>     | GUID    | L'identifiant (GUID) de la demande d'exercice de droits dont vous souhaitez modifier l'étape de processus |
| `stepId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'étape de processus à appliquer à la demande                                            |
| `comment`                                  | String  | Commentaire optionnel associé au changement d'étape                                                       |

### Archiver une demande d'exercice de droits via son identifiant

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/archive/{id}`

Cet endpoint déplace la demande d'exercice de droits dans la corbeille (état « archivée »).

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |
| `id`<mark style="color:red;">\*</mark>          | GUID    | L'identifiant (GUID) de la demande d'exercice de droits à archiver                         |

{% tabs %}
{% tab title="200: OK" %}
La réponse contient la demande d'exercice de droits (voir l'objet décrit plus haut).
{% endtab %}
{% endtabs %}

### Retirer le statut archivé d'une demande d'exercice de droits

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/restore/{id}`

Cet endpoint restaure une demande depuis la corbeille.

#### Paramètres d'URL

| Nom                                             | Type    | Description                                                                                |
| ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | L'identifiant de l'espace de travail dans lequel se trouve la demande d'exercice de droits |
| `id`<mark style="color:red;">\*</mark>          | GUID    | L'identifiant (GUID) de la demande d'exercice de droits à restaurer                        |

{% tabs %}
{% tab title="200: OK" %}
La réponse contient la demande d'exercice de droits (voir l'objet décrit plus haut).
{% endtab %}
{% endtabs %}
