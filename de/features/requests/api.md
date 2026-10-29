---
description: >-
  Diese Seite erklärt, wie Sie Ihre Betroffenenanfragen über unsere REST-API direkt in Dastra verwalten, ohne das JavaScript-SDK zu integrieren.
---

# API-Integration

Da Dastra nicht nativ in alle Entwicklungsplattformen integriert ist, stellen wir eine REST-API bereit, mit der Sie Ihre Betroffenenanfragen aus Ihren Anwendungen heraus verwalten können.

## Das Objekt der Betroffenenanfrage

Nachfolgend sehen Sie das JSON-Objektmodell einer Betroffenenanfrage in Dastra.

<details>

<summary>Das Objekt der Betroffenenanfrage</summary>

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

Um das Objektformat mit Ihren eigenen benutzerdefinierten Feldern zu erhalten, exportieren Sie eine Anfrage im JSON-Format: Sie erhalten so das JSON-Modell Ihres Mandanten.

Die Kennungen der Anfragen sind GUIDs (zum Beispiel `3fa85f64-5717-4562-b3fc-2c963f66afa6`). Die Kennung des Mandanten ist eine ganze Zahl.

## API-Endpunkte

Hier finden Sie die wichtigsten Endpunkte, mit denen Sie Ihre Anwendungen in das Dastra-Modul für Betroffenenanfragen integrieren.

### Eine neue Betroffenenanfrage in Dastra erstellen

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

#### Pfadparameter

| Name                                            | Typ     | Beschreibung         |
| ----------------------------------------------- | ------- | -------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten |

#### Request-Body

| Name                                         | Typ            | Beschreibung                                                                                                                 |
| -------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `title`<mark style="color:red;">\*</mark>    | String         | Titel der Anfrage                                                                                                            |
| `message`                                    | String         | Text der Anfrage                                                                                                             |
| `locale`<mark style="color:red;">\*</mark>   | String         | Sprache des Antragstellers (zum Beispiel `fr`, `en`)                                                                         |
| `areaId`<mark style="color:red;">\*</mark>   | Integer        | ID der Organisationseinheit der Anfrage                                                                                      |
| `email`                                      | String         | E-Mail-Adresse des Antragstellers                                                                                            |
| `dateDemand`                                 | DateTime       | Datum der Anfrage (standardmäßig das aktuelle Datum)                                                                         |
| `purposes`<mark style="color:red;">\*</mark> | Array\[String] | Betroffene Anfragetypen (mindestens einer). Mögliche Werte: siehe den Parameter `purposes` des Listen-Endpunkts weiter unten |

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

### Eine bestehende Betroffenenanfrage über ihre ID abrufen

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                             |
| ----------------------------------------------- | ------- | -------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält |
| `id`<mark style="color:red;">\*</mark>          | GUID    | Die ID (GUID) der Betroffenenanfrage                     |

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

### Eine paginierte Liste von Betroffenenanfragen abrufen

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

Sie können optionale Suchparameter übergeben, um die Antwort der API zu filtern.

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                       |
| ----------------------------------------------- | ------- | ---------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des abzufragenden Mandanten |

#### Query-Parameter

| Name         | Typ            | Beschreibung                                                                                                                                                                                                                                                                                                                |
| ------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `overtaking` | Boolean        | Sucht Anfragen, deren gesetzliche Antwortfrist überschritten ist                                                                                                                                                                                                                                                            |
| `archived`   | Boolean        | Gibt die Anfragen im Papierkorb zurück (standardmäßig `false`)                                                                                                                                                                                                                                                              |
| `q`          | String         | Textsuche im Titel der Anfrage                                                                                                                                                                                                                                                                                              |
| `widgetId`   | Integer        | Filtert die Anfragen, die aus einem Erfassungsformular stammen                                                                                                                                                                                                                                                              |
| `areaId`     | Integer        | Filtert die Anfragen einer Organisationseinheit                                                                                                                                                                                                                                                                             |
| `states`     | Array\[String] | Filtert die Anfragen nach Status (Open, IdentityValidation, Processing, Active, Closed)                                                                                                                                                                                                                                     |
| `purposes`   | Array\[String] | Filtert die Anfragen nach Typ (Unknown, Information, Access, Rectification, Erasure, Restriction, Opposition, Portability, AdvanceDirectives, AutomatedDecision, AdministrativeAccess, DPORequest, ThirdPartyRequest, DataProtectionComplaint, DoNotSellOrShare, LimitUseSensitivePersonalInformation, WithdrawalOfConsent) |
| `ids`        | Array\[GUID]   | Wählt eine Liste von Anfragen anhand ihrer IDs aus                                                                                                                                                                                                                                                                          |
| `tags`       | Array\[GUID]   | Wählt die Anfragen mit bestimmten Tags aus (übergeben Sie ein Array von Tag-IDs im Query-String)                                                                                                                                                                                                                            |
| `page`       | Integer        | Die abzurufende Seite (die erste Seite ist 1)                                                                                                                                                                                                                                                                               |
| `size`       | Integer        | Die Anzahl der Elemente pro Seite (standardmäßig 20)                                                                                                                                                                                                                                                                        |
| `skip`       | Integer        | Die Anzahl der zu überspringenden Elemente (ersetzt `page`, wenn angegeben)                                                                                                                                                                                                                                                 |
| `sortBy`     | String         | Das Feld, nach dem die Elemente sortiert werden                                                                                                                                                                                                                                                                             |
| `asc`        | Boolean        | `true` für aufsteigende Sortierung                                                                                                                                                                                                                                                                                          |

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

### Eine Betroffenenanfrage aktualisieren

<mark style="color:orange;">`PUT`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                             |
| ----------------------------------------------- | ------- | -------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält |
| `id`<mark style="color:red;">\*</mark>          | GUID    | Die ID (GUID) der Betroffenenanfrage                     |

#### Request-Body

| Name                 | Typ    | Beschreibung                                                                                                                                                                                            |
| -------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataSubjectRequest` | Object | Das vollständige Objekt der Betroffenenanfrage (siehe oben oder unsere [Swagger-API-Dokumentation](https://api.dastra.eu/swagger/index.html)). Das Feld `id` muss mit der ID in der URL übereinstimmen. |

{% tabs %}
{% tab title="204: No Content" %}
Die Antwort enthält keinen Inhalt.
{% endtab %}
{% endtabs %}

### Eine Betroffenenanfrage über ihre ID löschen

<mark style="color:red;">`DELETE`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

Diese Aktion ist unwiderruflich: Die Betroffenenanfrage wird endgültig aus unseren Datenbanken gelöscht. Um sie in den Papierkorb zu verschieben, ohne sie zu löschen, verwenden Sie den Endpunkt zum Archivieren weiter unten.

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                             |
| ----------------------------------------------- | ------- | -------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält |
| `id`<mark style="color:red;">\*</mark>          | GUID    | Die ID (GUID) der Betroffenenanfrage                     |

{% tabs %}
{% tab title="200: OK" %}
Die Antwort enthält keinen Inhalt.
{% endtab %}
{% endtabs %}

### Den Prozessschritt einer Betroffenenanfrage ändern

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/workflow`

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                             |
| ----------------------------------------------- | ------- | -------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält |

#### Request-Body

| Name                                       | Typ     | Beschreibung                                                                  |
| ------------------------------------------ | ------- | ----------------------------------------------------------------------------- |
| `id`<mark style="color:red;">\*</mark>     | GUID    | Die ID (GUID) der Betroffenenanfrage, deren Prozessschritt Sie ändern möchten |
| `stepId`<mark style="color:red;">\*</mark> | Integer | Die ID des Prozessschritts, der auf die Anfrage angewendet werden soll        |
| `comment`                                  | String  | Optionaler Kommentar zum Schrittwechsel                                       |

### Eine Betroffenenanfrage über ihre ID archivieren

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/archive/{id}`

Dieser Endpunkt verschiebt die Betroffenenanfrage in den Papierkorb (Status „archiviert“).

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                             |
| ----------------------------------------------- | ------- | -------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält |
| `id`<mark style="color:red;">\*</mark>          | GUID    | Die ID (GUID) der zu archivierenden Betroffenenanfrage   |

{% tabs %}
{% tab title="200: OK" %}
Die Antwort enthält die Betroffenenanfrage (siehe das oben beschriebene Objekt).
{% endtab %}
{% endtabs %}

### Den Archivierungsstatus einer Betroffenenanfrage aufheben

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/restore/{id}`

Dieser Endpunkt stellt eine Anfrage aus dem Papierkorb wieder her.

#### Pfadparameter

| Name                                            | Typ     | Beschreibung                                               |
| ----------------------------------------------- | ------- | ---------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | Die ID des Mandanten, der die Betroffenenanfrage enthält   |
| `id`<mark style="color:red;">\*</mark>          | GUID    | Die ID (GUID) der wiederherzustellenden Betroffenenanfrage |

{% tabs %}
{% tab title="200: OK" %}
Die Antwort enthält die Betroffenenanfrage (siehe das oben beschriebene Objekt).
{% endtab %}
{% endtabs %}
