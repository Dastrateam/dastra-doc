---
description: >-
  Diese Seite erklärt Ihnen, wie Sie Ihre Betroffenenanfragen in Dastra
  direkt über unsere REST-API verwalten können, ohne das JavaScript-SDK zu integrieren.
---

# API-Integration

Da Dastra nicht nativ in alle Entwicklungsplattformen integriert ist, stellen wir Ihnen eine REST-API zur Verfügung, um Ihre Betroffenenanfragen aus Ihren Anwendungen heraus zu verwalten.&#x20;

### Das JSON-Objekt der Betroffenenanfrage

Nachfolgend finden Sie das Objektmodell im JSON-Format einer Betroffenenanfrage in Dastra.

<details>

<summary>Das Objekt Betroffenenanfrage</summary>

```
{
    "customFields": {
      "13_long": "1234567891234",
      "13_html": "1234567891234"
    },
    "closedByUser": null,
    "area": {
      "order": XXX,
      "children": [],
      "permissions": [],
      "id": XXX,
      "type": "Entity",
      "parentId": null,
      "ref": null,
      "label": "Moulinsart",
      "description": null,
      "logoUrl": null,
      "address": null,
      "zipCode": null,
      "city": null,
      "countryCode": "BE",
      "immatriculationNumber": null,
      "phoneNumber": null,
      "mailAddress": null,
      "dpo": null,
      "referent": null,
      "representative": null,
      "dataProtectionAuthority": null
    },
    "creator": null,
    "operator": null,
    "operatorId": null,
    "attachments": [],
    "messages": [],
    "tags": [],
    "id": XXX,
    "title": "",
    "locale": "fr",
    "archived": false,
    "archivedDate": null,
    "subjectCategoryId": null,
    "subjectCategory": null,
    "complex": false,
    "dateClosed": null,
    "areaId": XX,
    "state": "Open",
    "description": null,
    "message": null,
    "resolutionMessage": null,
    "email": "",
    "phoneNumber": null,
    "givenName": "",
    "familyName": null,
    "dateDemand": "2023-09-18T10:31:30.6882299",
    "dateCreation": "2023-09-18T10:31:30.6882299",
    "dateUpdate": null,
    "workFlowStep": {
      "id": 22290,
      "label": "Nouveau",
      "color": "#1E8EE1",
      "order": 0,
      "itemLimit": null,
      "type": "DataSubjectRequest",
      "finalStep": false,
      "initialStep": true,
      "authorizedRole": null,
      "authorizedRoleId": null,
      "descriptionHtml": null,
      "mappedState": "Open"
    },
    "workFlowStepId": XX,
    "channel": "Widget",
    "refId": null,
    "userId": null,
    "purposes": [
      "Rectification"
    ],
    "closedReason": "None",
    "closedReasonDescription": null,
    "expiryTime": "2023-10-18T10:31:30.68823",
    "address": null,
    "zipCode": null,
    "city": null,
    "countryCode": null,
    "nbMessages": 0,
    "nbMessagesNotViewed": 0,
    "nbMessagesIncoming": 0,
    "lastMessageDate": null,
    "remainingDays": -6,
    "closingTime": null,
    "additionalDatas": {
      "givenName": null,
      "13_long": "XX",
      "13_html": "XX"
    },
    "userNotified": false,
    "dateUserNotified": null,
    "sendNotification": false,
    "emailValidationDate": "2023-09-18T10:31:53.8554799",
    "mailValidated": true,
    "referrerUrl": "",
    "demandId": "",
    "identityValidated": false,
    "dateIdentityValidated": null,
    "widgetId": 0  
  }
]
```

</details>

Um das Objektformat Ihrer mit benutzerdefinierten Feldern konfigurierten Anfrage abzurufen, können Sie einen Export einer Anfrage im JSON-Format durchführen und so das JSON-Modell erhalten.&#x20;

### Die API-Endpunkte

Hier sind die wichtigsten Endpunkte, die Ihnen für die Integration Ihrer Anwendungen mit dem Modul Betroffenenanfragen von Dastra nützlich sein werden.

## Eine neue Betroffenenanfrage in Dastra erstellen

<mark style="color:green;">`POST`</mark> `/v1​/ws​/{workspaceId}​/DataSubjectRequests`

#### Path Parameters

| Name                                          | Type   | Description                                                                             |
| --------------------------------------------- | ------ | --------------------------------------------------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String | Die ID des Mandanten, in dem Sie die Betroffenenanfrage erstellen möchten |

{% tabs %}
{% tab title="200: OK " %}
```json
{
  "id": 0,
  "title": "string",
  "locale": "string",
  "archived": true,
  "archivedDate": "2022-08-31T10:24:32.381Z",
  "personCategory": "Prospect",
  "complex": true,
  "dateClosed": "2022-08-31T10:24:32.381Z",
  "areaId": 0,
  "state": "Open",
  "description": "string",
  "message": "string",
  "resolutionMessage": "string",
  "email": "string",
  "phoneNumber": "string",
  "givenName": "string",
  "familyName": "string",
  "dateCreation": "2022-08-31T10:24:32.381Z",
  "dateUpdate": "2022-08-31T10:24:32.381Z",
  "workFlowStep": {
    "id": 0,
    "label": "string",
    "color": "string",
    "order": 0,
    "itemLimit": 0,
    "type": "DataSubject",
    "finalStep": true,
    "initialStep": true,
    "descriptionHtml": "string",
    "mappedState": "string"
  },
  "workFlowStepId": 0,
  "channel": "Internal",
  "refId": "string",
  "userId": "string",
  "purposes": [
    "Unknown"
  ],
  "closedReason": "None",
  "closedReasonDescription": "string",
  "expiryTime": "2022-08-31T10:24:32.381Z",
  "address": "string",
  "zipCode": "string",
  "city": "string",
  "countryCode": "st",
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "remainingDays": 0,
  "closingTime": 0,
  "additionalDatas": "string",
  "userNotified": true,
  "dateUserNotified": "2022-08-31T10:24:32.381Z",
  "sendNotification": true,
  "emailValidationDate": "2022-08-31T10:24:32.381Z",
  "mailValidated": true,
  "referrerUrl": "string",
  "demandId": "string",
  "identityValidated": true,
  "dateIdentityValidated": "2022-08-31T10:24:32.381Z",
  "widgetId": 0
}
```
{% endtab %}
{% endtabs %}

## Eine bestehende Betroffenenanfrage über ihre ID abrufen

<mark style="color:blue;">`GET`</mark> `​/v1​/ws​/{workspaceId}​/DataSubjectRequests​/{id}`

#### Path Parameters

| Name                                          | Type    | Description                                                                                                   |
| --------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String  | Die ID des Mandanten, in dem sich die abzufragende Betroffenenanfrage befindet |
| <mark style="color:red;">\*</mark>            | Integer | Die ID der Betroffenenanfrage, die Sie abfragen möchten                                           |

{% tabs %}
{% tab title="200: OK " %}
```json
{
  "closedByUser": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "area": {
    "order": 0,
    "children": [
      "string"
    ],
    "teams": [
      {
        "id": 0,
        "label": "string",
        "ref": "string",
        "areas": [
          0
        ],
        "users": [
          0
        ]
      }
    ],
    "id": 0,
    "type": "Entity",
    "parentId": 0,
    "ref": "string",
    "label": "string",
    "description": "string",
    "logoUrl": "string",
    "address": "string",
    "zipCode": "string",
    "city": "string",
    "countryCode": "str",
    "immatriculationNumber": "string",
    "phoneNumber": "string",
    "mailAddress": "string",
    "dpo": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:29:26.246Z",
      "dateUpdate": "2022-08-31T13:29:26.246Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "referent": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:29:26.246Z",
      "dateUpdate": "2022-08-31T13:29:26.246Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "representative": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:29:26.246Z",
      "dateUpdate": "2022-08-31T13:29:26.246Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "dataProtectionAuthority": {
      "id": 0,
      "label": "string",
      "siteURL": "string",
      "phoneNumber": "string",
      "email": "user@example.com",
      "countryCode": "str",
      "address": "string",
      "city": "string",
      "zipCode": "string"
    }
  },
  "creator": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "operator": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "operatorId": 0,
  "attachments": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "extension": "string",
      "size": 0,
      "nbDownload": 0,
      "transmitted": true,
      "fileName": "string",
      "label": "string",
      "userRequestMessageId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "userRequestId": 0,
      "dateCreation": "2022-08-31T13:29:26.246Z",
      "dateUpdate": "2022-08-31T13:29:26.246Z",
      "creator": {
        "id": 0,
        "displayName": "string",
        "familyName": "string",
        "givenName": "string",
        "email": "string",
        "color": "string",
        "avatarUrl": "string",
        "tenantId": 0
      },
      "expiration": "2022-08-31T13:29:26.246Z",
      "dateLastDownload": "2022-08-31T13:29:26.246Z",
      "dateFileRemoved": "2022-08-31T13:29:26.246Z",
      "deleted": true,
      "expired": true,
      "color": "string"
    }
  ],
  "tags": [
    {
      "id": 0,
      "label": "string",
      "type": "DataProcessing",
      "color": "string"
    }
  ],
  "id": 0,
  "title": "string",
  "locale": "string",
  "archived": true,
  "archivedDate": "2022-08-31T13:29:26.246Z",
  "personCategory": "Prospect",
  "complex": true,
  "dateClosed": "2022-08-31T13:29:26.246Z",
  "areaId": 0,
  "state": "Open",
  "description": "string",
  "message": "string",
  "resolutionMessage": "string",
  "email": "string",
  "phoneNumber": "string",
  "givenName": "string",
  "familyName": "string",
  "dateCreation": "2022-08-31T13:29:26.246Z",
  "dateUpdate": "2022-08-31T13:29:26.246Z",
  "workFlowStep": {
    "id": 0,
    "label": "string",
    "color": "string",
    "order": 0,
    "itemLimit": 0,
    "type": "DataSubject",
    "finalStep": true,
    "initialStep": true,
    "descriptionHtml": "string",
    "mappedState": "string"
  },
  "workFlowStepId": 0,
  "channel": "Internal",
  "refId": "string",
  "userId": "string",
  "purposes": [
    "Unknown"
  ],
  "closedReason": "None",
  "closedReasonDescription": "string",
  "expiryTime": "2022-08-31T13:29:26.246Z",
  "address": "string",
  "zipCode": "string",
  "city": "string",
  "countryCode": "st",
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "remainingDays": 0,
  "closingTime": 0,
  "additionalDatas": "string",
  "userNotified": true,
  "dateUserNotified": "2022-08-31T13:29:26.246Z",
  "sendNotification": true,
  "emailValidationDate": "2022-08-31T13:29:26.246Z",
  "mailValidated": true,
  "referrerUrl": "string",
  "demandId": "string",
  "identityValidated": true,
  "dateIdentityValidated": "2022-08-31T13:29:26.246Z",
  "widgetId": 0
}
```
{% endtab %}
{% endtabs %}

## Eine paginierte Liste von Betroffenenanfragen abrufen

<mark style="color:blue;">`GET`</mark> `​/v1​/ws​/{workspaceId}​/DataSubjectRequests`

Sie können optionale Suchparameter an Ihre Anfrage übergeben, um die API-Antwort zu filtern&#x20;

#### Path Parameters

| Name                                          | Type   | Description                                 |
| --------------------------------------------- | ------ | ------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String | Die Mandanten-ID, die Sie abfragen möchten |

#### Query Parameters

| Name       | Type            | Description                                                                                                                                                      |
| ---------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| overtaking | Boolean         | Anfragen suchen, deren gesetzliche Antwortfrist überschritten wurde                                                                                           |
| archived   | Boolean         | Archivierte Anfragen zurückgeben                                                                                                                                 |
| q          | String          | Textsuche im Titel der Anfrage                                                                                                                      |
| widgetId   | Integer         | Anfragen filtern, die von einem Erfassungs-Widget stammen                                                                                                              |
| states     | Array\[String]  | Anfragen nach Status filtern (Open, IdentityValidation, Processing, Active, Closed)                                                                             |
| purposes   | Array\[String]  | Anfragen nach Typ filtern (Unknown, Information, Access, Rectification, Erasure, Restriction, Opposition, Portability, AdvanceDirectives, AutomatedDecision) |
| ids        | Array\[Integer] | Eine Liste von Anfragen anhand ihrer IDs auswählen                                                                                                 |
| tags       | Array\[Integer] | Anfragen mit bestimmten Tags auswählen (ein Array von tagIds als Query-String übergeben)                                                                 |
| page       | Integer         | Die Seite, die Sie abfragen möchten                                                                                                              |
| size       | Integer         | Die Anzahl der pro Seite zurückgegebenen Elemente                                                                                                                          |
| skip       | Integer         |                                                                                                                                                                  |
| sortBy     | String          | Das Feld, nach dem die Elemente sortiert werden sollen                                                                                                                 |
| asc        | Boolean         | true für aufsteigende Sortierung                                                                                                                         |

{% tabs %}
{% tab title="200: OK Ein Objekt mit den zurückgegebenen Betroffenenanfragen (Eigenschaft items), der Seite, der Anfragegröße und der Gesamtanzahl der Elemente" %}
```json
{
  "items": [
    {
      "closedByUser": {
        "id": 0,
        "displayName": "string",
        "familyName": "string",
        "givenName": "string",
        "email": "string",
        "color": "string",
        "avatarUrl": "string",
        "tenantId": 0
      },
      "area": {
        "order": 0,
        "children": [
          "string"
        ],
        "teams": [
          {
            "id": 0,
            "label": "string",
            "ref": "string",
            "areas": [
              0
            ],
            "users": [
              0
            ]
          }
        ],
        "id": 0,
        "type": "Entity",
        "parentId": 0,
        "ref": "string",
        "label": "string",
        "description": "string",
        "logoUrl": "string",
        "address": "string",
        "zipCode": "string",
        "city": "string",
        "countryCode": "str",
        "immatriculationNumber": "string",
        "phoneNumber": "string",
        "mailAddress": "string",
        "dpo": {
          "id": 0,
          "displayName": "string",
          "dateCreation": "2022-08-31T10:30:53.839Z",
          "dateUpdate": "2022-08-31T10:30:53.839Z",
          "logoUrl": "string",
          "actorType": "Physical",
          "vendorType": "B2B",
          "accessLevel": "None",
          "givenName": "string",
          "familyName": "string",
          "companyName": "string",
          "description": "string",
          "countryCode": "st",
          "readonly": true,
          "email": "string",
          "phoneNumber": "string",
          "contactName": "string",
          "contactPosition": "string",
          "immatriculationNumber": "string",
          "websiteUrl": "string",
          "address": "string",
          "zipCode": "string",
          "city": "string"
        },
        "referent": {
          "id": 0,
          "displayName": "string",
          "dateCreation": "2022-08-31T10:30:53.839Z",
          "dateUpdate": "2022-08-31T10:30:53.839Z",
          "logoUrl": "string",
          "actorType": "Physical",
          "vendorType": "B2B",
          "accessLevel": "None",
          "givenName": "string",
          "familyName": "string",
          "companyName": "string",
          "description": "string",
          "countryCode": "st",
          "readonly": true,
          "email": "string",
          "phoneNumber": "string",
          "contactName": "string",
          "contactPosition": "string",
          "immatriculationNumber": "string",
          "websiteUrl": "string",
          "address": "string",
          "zipCode": "string",
          "city": "string"
        },
        "representative": {
          "id": 0,
          "displayName": "string",
          "dateCreation": "2022-08-31T10:30:53.839Z",
          "dateUpdate": "2022-08-31T10:30:53.839Z",
          "logoUrl": "string",
          "actorType": "Physical",
          "vendorType": "B2B",
          "accessLevel": "None",
          "givenName": "string",
          "familyName": "string",
          "companyName": "string",
          "description": "string",
          "countryCode": "st",
          "readonly": true,
          "email": "string",
          "phoneNumber": "string",
          "contactName": "string",
          "contactPosition": "string",
          "immatriculationNumber": "string",
          "websiteUrl": "string",
          "address": "string",
          "zipCode": "string",
          "city": "string"
        },
        "dataProtectionAuthority": {
          "id": 0,
          "label": "string",
          "siteURL": "string",
          "phoneNumber": "string",
          "email": "user@example.com",
          "countryCode": "str",
          "address": "string",
          "city": "string",
          "zipCode": "string"
        }
      },
      "creator": {
        "id": 0,
        "displayName": "string",
        "familyName": "string",
        "givenName": "string",
        "email": "string",
        "color": "string",
        "avatarUrl": "string",
        "tenantId": 0
      },
      "operator": {
        "id": 0,
        "displayName": "string",
        "familyName": "string",
        "givenName": "string",
        "email": "string",
        "color": "string",
        "avatarUrl": "string",
        "tenantId": 0
      },
      "operatorId": 0,
      "attachments": [
        {
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "extension": "string",
          "size": 0,
          "nbDownload": 0,
          "transmitted": true,
          "fileName": "string",
          "label": "string",
          "userRequestMessageId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "userRequestId": 0,
          "dateCreation": "2022-08-31T10:30:53.839Z",
          "dateUpdate": "2022-08-31T10:30:53.839Z",
          "creator": {
            "id": 0,
            "displayName": "string",
            "familyName": "string",
            "givenName": "string",
            "email": "string",
            "color": "string",
            "avatarUrl": "string",
            "tenantId": 0
          },
          "expiration": "2022-08-31T10:30:53.839Z",
          "dateLastDownload": "2022-08-31T10:30:53.839Z",
          "dateFileRemoved": "2022-08-31T10:30:53.839Z",
          "deleted": true,
          "expired": true,
          "color": "string"
        }
      ],
      "tags": [
        {
          "id": 0,
          "label": "string",
          "type": "DataProcessing",
          "color": "string"
        }
      ],
      "id": 0,
      "title": "string",
      "locale": "string",
      "archived": true,
      "archivedDate": "2022-08-31T10:30:53.840Z",
      "personCategory": "Prospect",
      "complex": true,
      "dateClosed": "2022-08-31T10:30:53.840Z",
      "areaId": 0,
      "state": "Open",
      "description": "string",
      "message": "string",
      "resolutionMessage": "string",
      "email": "string",
      "phoneNumber": "string",
      "givenName": "string",
      "familyName": "string",
      "dateCreation": "2022-08-31T10:30:53.840Z",
      "dateUpdate": "2022-08-31T10:30:53.840Z",
      "workFlowStep": {
        "id": 0,
        "label": "string",
        "color": "string",
        "order": 0,
        "itemLimit": 0,
        "type": "DataSubject",
        "finalStep": true,
        "initialStep": true,
        "descriptionHtml": "string",
        "mappedState": "string"
      },
      "workFlowStepId": 0,
      "channel": "Internal",
      "refId": "string",
      "userId": "string",
      "purposes": [
        "Unknown"
      ],
      "closedReason": "None",
      "closedReasonDescription": "string",
      "expiryTime": "2022-08-31T10:30:53.840Z",
      "address": "string",
      "zipCode": "string",
      "city": "string",
      "countryCode": "st",
      "nbMessages": 0,
      "nbMessagesNotViewed": 0,
      "remainingDays": 0,
      "closingTime": 0,
      "additionalDatas": "string",
      "userNotified": true,
      "dateUserNotified": "2022-08-31T10:30:53.840Z",
      "sendNotification": true,
      "emailValidationDate": "2022-08-31T10:30:53.840Z",
      "mailValidated": true,
      "referrerUrl": "string",
      "demandId": "string",
      "identityValidated": true,
      "dateIdentityValidated": "2022-08-31T10:30:53.840Z",
      "widgetId": 0
    }
  ],
  "total": 0,
  "size": 0,
  "page": 0
}
```
{% endtab %}
{% endtabs %}

## Eine Betroffenenanfrage aktualisieren

<mark style="color:orange;">`PUT`</mark> `/v1/ws/{workspaceId}​/DataSubjectRequests​/{id}`

#### Path Parameters

| Name                                          | Type    | Description                                                                                                    |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String  | Die ID des Mandanten, in dem sich die zu aktualisierende Betroffenenanfrage befindet |
| id<mark style="color:red;">\*</mark>          | Integer | Die ID der bestehenden Betroffenenanfrage, die Sie aktualisieren möchten                                 |

#### Request Body

| Name               | Type   | Description                                                                                                                                                 |
| ------------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dataSubjectRequest | Object | Senden Sie das vollständige Objekt der Betroffenenanfrage (siehe oben oder unsere [Swagger-API-Dokumentation](https://api.dastra.eu/swagger/index.html)) |

{% tabs %}
{% tab title="200: OK Success" %}
```json
{
  "closedByUser": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "area": {
    "order": 0,
    "children": [
      "string"
    ],
    "teams": [
      {
        "id": 0,
        "label": "string",
        "ref": "string",
        "areas": [
          0
        ],
        "users": [
          0
        ]
      }
    ],
    "id": 0,
    "type": "Entity",
    "parentId": 0,
    "ref": "string",
    "label": "string",
    "description": "string",
    "logoUrl": "string",
    "address": "string",
    "zipCode": "string",
    "city": "string",
    "countryCode": "str",
    "immatriculationNumber": "string",
    "phoneNumber": "string",
    "mailAddress": "string",
    "dpo": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:44:54.781Z",
      "dateUpdate": "2022-08-31T13:44:54.781Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "referent": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:44:54.781Z",
      "dateUpdate": "2022-08-31T13:44:54.781Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "representative": {
      "id": 0,
      "displayName": "string",
      "dateCreation": "2022-08-31T13:44:54.781Z",
      "dateUpdate": "2022-08-31T13:44:54.781Z",
      "logoUrl": "string",
      "actorType": "Physical",
      "vendorType": "B2B",
      "accessLevel": "None",
      "givenName": "string",
      "familyName": "string",
      "companyName": "string",
      "description": "string",
      "countryCode": "st",
      "readonly": true,
      "email": "string",
      "phoneNumber": "string",
      "contactName": "string",
      "contactPosition": "string",
      "immatriculationNumber": "string",
      "websiteUrl": "string",
      "address": "string",
      "zipCode": "string",
      "city": "string"
    },
    "dataProtectionAuthority": {
      "id": 0,
      "label": "string",
      "siteURL": "string",
      "phoneNumber": "string",
      "email": "user@example.com",
      "countryCode": "str",
      "address": "string",
      "city": "string",
      "zipCode": "string"
    }
  },
  "creator": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "operator": {
    "id": 0,
    "displayName": "string",
    "familyName": "string",
    "givenName": "string",
    "email": "string",
    "color": "string",
    "avatarUrl": "string",
    "tenantId": 0
  },
  "operatorId": 0,
  "attachments": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "extension": "string",
      "size": 0,
      "nbDownload": 0,
      "transmitted": true,
      "fileName": "string",
      "label": "string",
      "userRequestMessageId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "userRequestId": 0,
      "dateCreation": "2022-08-31T13:44:54.781Z",
      "dateUpdate": "2022-08-31T13:44:54.781Z",
      "creator": {
        "id": 0,
        "displayName": "string",
        "familyName": "string",
        "givenName": "string",
        "email": "string",
        "color": "string",
        "avatarUrl": "string",
        "tenantId": 0
      },
      "expiration": "2022-08-31T13:44:54.781Z",
      "dateLastDownload": "2022-08-31T13:44:54.781Z",
      "dateFileRemoved": "2022-08-31T13:44:54.781Z",
      "deleted": true,
      "expired": true,
      "color": "string"
    }
  ],
  "tags": [
    {
      "id": 0,
      "label": "string",
      "type": "DataProcessing",
      "color": "string"
    }
  ],
  "id": 0,
  "title": "string",
  "locale": "string",
  "archived": true,
  "archivedDate": "2022-08-31T13:44:54.781Z",
  "personCategory": "Prospect",
  "complex": true,
  "dateClosed": "2022-08-31T13:44:54.781Z",
  "areaId": 0,
  "state": "Open",
  "description": "string",
  "message": "string",
  "resolutionMessage": "string",
  "email": "string",
  "phoneNumber": "string",
  "givenName": "string",
  "familyName": "string",
  "dateCreation": "2022-08-31T13:44:54.781Z",
  "dateUpdate": "2022-08-31T13:44:54.781Z",
  "workFlowStep": {
    "id": 0,
    "label": "string",
    "color": "string",
    "order": 0,
    "itemLimit": 0,
    "type": "DataSubject",
    "finalStep": true,
    "initialStep": true,
    "descriptionHtml": "string",
    "mappedState": "string"
  },
  "workFlowStepId": 0,
  "channel": "Internal",
  "refId": "string",
  "userId": "string",
  "purposes": [
    "Unknown"
  ],
  "closedReason": "None",
  "closedReasonDescription": "string",
  "expiryTime": "2022-08-31T13:44:54.781Z",
  "address": "string",
  "zipCode": "string",
  "city": "string",
  "countryCode": "st",
  "nbMessages": 0,
  "nbMessagesNotViewed": 0,
  "remainingDays": 0,
  "closingTime": 0,
  "additionalDatas": "string",
  "userNotified": true,
  "dateUserNotified": "2022-08-31T13:44:54.781Z",
  "sendNotification": true,
  "emailValidationDate": "2022-08-31T13:44:54.781Z",
  "mailValidated": true,
  "referrerUrl": "string",
  "demandId": "string",
  "identityValidated": true,
  "dateIdentityValidated": "2022-08-31T13:44:54.781Z",
  "widgetId": 0
}
```
{% endtab %}
{% endtabs %}

## Eine Betroffenenanfrage über ihre ID löschen

<mark style="color:red;">`DELETE`</mark> `​/v1​/ws​/{workspaceId}​/DataSubjectRequests​/{id}`

Achtung, diese Aktion ist unwiderruflich. Die Betroffenenanfrage wird endgültig aus unseren Datenbanken gelöscht.

#### Path Parameters

| Name                                          | Type    | Description                                                                                                    |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String  | Die ID des Mandanten, in dem sich die zu löschende Betroffenenanfrage befindet |
| id<mark style="color:red;">\*</mark>          | Integer | Die ID der bestehenden Betroffenenanfrage, die Sie löschen möchten                                 |

{% tabs %}
{% tab title="200: OK Success" %}
```javascript
{
    // Response
}
```
{% endtab %}
{% endtabs %}

## Den Prozessschritt der Betroffenenanfrage ändern

<mark style="color:green;">`POST`</mark> `/v1​/ws​/{workspaceId}​/DataSubjectRequests​/workflow`

#### Path Parameters

| Name                                          | Type   | Description                                                                                                    |
| --------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------- |
| workspaceId<mark style="color:red;">\*</mark> | String | Die ID des Mandanten, in dem sich die Betroffenenanfrage befindet |

#### Request Body

| Name   | Type    | Description                                                                                 |
| ------ | ------- | ------------------------------------------------------------------------------------------- |
| id     | Integer | Die ID der Betroffenenanfrage, deren Prozessschritt Sie ändern möchten   |
| stepId | Integer | Die ID des Prozessschritts, den Sie auf die Betroffenenanfrage anwenden möchten |

## Eine Betroffenenanfrage über ihre ID archivieren

<mark style="color:green;">`POST`</mark> `/v1​/ws​/{workspaceId}​/DataSubjectRequests​/archive​/{id}`

Dieser Endpunkt wendet den Status "Archived" auf die Betroffenenanfrage an.

#### Path Parameters

| Name        | Type    | Description                                                                                                    |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| workspaceId | String  | Die ID des Mandanten, in dem sich die zu archivierende Betroffenenanfrage befindet |
| id          | Integer | Die ID der Betroffenenanfrage, die Sie archivieren möchten                                            |

{% tabs %}
{% tab title="200: OK Success" %}
```javascript
{
    // Response
}
```
{% endtab %}
{% endtabs %}

## Den Archivierungsstatus einer Betroffenenanfrage aufheben

<mark style="color:green;">`POST`</mark> `​/v1​/ws​/{workspaceId}​/DataSubjectRequests​/restore​/{id}`

#### Path Parameters

| Name        | Type     | Description                                                                                                    |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| workspaceId | String   | Die ID des Mandanten, in dem sich die wiederherzustellende Betroffenenanfrage befindet |
| id          | Integrer | Die ID der Betroffenenanfrage, die Sie wiederherstellen möchten                                           |
