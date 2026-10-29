---
description: >-
  Deze pagina legt uit hoe u uw verzoeken van betrokkenen rechtstreeks in Dastra beheert, zonder de JavaScript-SDK te integreren, dankzij onze REST-API.
---

# API-integratie

Omdat Dastra niet native met alle ontwikkelplatforms integreert, bieden wij een REST-API om uw verzoeken van betrokkenen vanuit uw toepassingen te beheren.

## Het object verzoek van een betrokkene

Hieronder staat het JSON-objectmodel van een verzoek van een betrokkene in Dastra.

<details>

<summary>Het object verzoek van een betrokkene</summary>

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

Om het objectformaat met uw eigen aangepaste velden te krijgen, exporteert u een verzoek in JSON-indeling: zo verkrijgt u het JSON-model van uw werkruimte.

De identificatoren van verzoeken zijn GUID's (bijvoorbeeld `3fa85f64-5717-4562-b3fc-2c963f66afa6`). De identificator van de werkruimte is een geheel getal.

## API-endpoints

Dit zijn de belangrijkste endpoints waarmee u uw toepassingen integreert met de module voor verzoeken van betrokkenen van Dastra.

### Een nieuw verzoek van een betrokkene aanmaken in Dastra

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte |

#### Aanvraagtekst

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `title`<mark style="color:red;">\*</mark> | String | Titel van het verzoek |
| `message` | String | Tekst van het verzoek |
| `locale`<mark style="color:red;">\*</mark> | String | Taal van de aanvrager (bijvoorbeeld `fr`, `en`) |
| `areaId`<mark style="color:red;">\*</mark> | Geheel getal | ID van de organisatorische eenheid van het verzoek |
| `email` | String | E-mailadres van de aanvrager |
| `dateDemand` | DateTime | Datum van het verzoek (standaard de huidige datum) |
| `purposes`<mark style="color:red;">\*</mark> | Array\[String] | Betrokken soorten verzoeken (minstens één). Mogelijke waarden: zie de parameter `purposes` van het lijst-endpoint hieronder |

{% tabs %}
{% tab title="201: Aangemaakt" %}
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

### Een bestaand verzoek van een betrokkene ophalen via zijn ID

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het verzoek van de betrokkene |

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

### Een gepagineerde lijst van verzoeken van betrokkenen ophalen

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

U kunt optionele zoekparameters meegeven om het API-antwoord te filteren.

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die u bevraagt |

#### Queryparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `overtaking` | Boolean | Zoek verzoeken waarvan de wettelijke antwoordtermijn is overschreden |
| `archived` | Boolean | Geef de verzoeken in de prullenbak terug (standaard `false`) |
| `q` | String | Tekstzoekopdracht in de titel van het verzoek |
| `widgetId` | Geheel getal | Filter de verzoeken die afkomstig zijn van een verzamelformulier |
| `areaId` | Geheel getal | Filter de verzoeken van een organisatorische eenheid |
| `states` | Array\[String] | Filter de verzoeken op status (Open, IdentityValidation, Processing, Active, Closed) |
| `purposes` | Array\[String] | Filter de verzoeken op type (Unknown, Information, Access, Rectification, Erasure, Restriction, Opposition, Portability, AdvanceDirectives, AutomatedDecision, AdministrativeAccess, DPORequest, ThirdPartyRequest, DataProtectionComplaint, DoNotSellOrShare, LimitUseSensitivePersonalInformation, WithdrawalOfConsent) |
| `ids` | Array\[GUID] | Selecteer een lijst van verzoeken op basis van hun ID's |
| `tags` | Array\[GUID] | Selecteer de verzoeken met specifieke labels (geef een array van label-ID's mee in de querystring) |
| `page` | Geheel getal | De op te halen pagina (de eerste pagina is 1) |
| `size` | Geheel getal | Het aantal items per pagina (standaard 20) |
| `skip` | Geheel getal | Het aantal over te slaan items (vervangt `page` wanneer het wordt meegegeven) |
| `sortBy` | String | Het veld waarop de items worden gesorteerd |
| `asc` | Boolean | `true` voor oplopende volgorde |

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

### Een verzoek van een betrokkene bijwerken

<mark style="color:orange;">`PUT`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het verzoek van de betrokkene |

#### Aanvraagtekst

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `dataSubjectRequest` | Object | Het volledige object van het verzoek van de betrokkene (zie hierboven of onze [Swagger-API-documentatie](https://api.dastra.eu/swagger/index.html)). Het veld `id` moet overeenkomen met de ID in de URL. |

{% tabs %}
{% tab title="204: Geen inhoud" %}
Het antwoord heeft geen inhoud.
{% endtab %}
{% endtabs %}

### Een verzoek van een betrokkene verwijderen via zijn ID

<mark style="color:red;">`DELETE`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

Deze actie is onomkeerbaar: het verzoek van de betrokkene wordt definitief uit onze databases verwijderd. Gebruik het archiveer-endpoint hieronder om het naar de prullenbak te verplaatsen zonder het te verwijderen.

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het verzoek van de betrokkene |

{% tabs %}
{% tab title="200: OK" %}
Het antwoord heeft geen inhoud.
{% endtab %}
{% endtabs %}

### De processtap van een verzoek van een betrokkene wijzigen

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/workflow`

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |

#### Aanvraagtekst

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het verzoek van de betrokkene waarvan u de processtap wilt wijzigen |
| `stepId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de processtap die op het verzoek wordt toegepast |
| `comment` | String | Optionele opmerking bij de stapwijziging |

### Een verzoek van een betrokkene archiveren via zijn ID

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/archive/{id}`

Dit endpoint verplaatst het verzoek van de betrokkene naar de prullenbak (status "gearchiveerd").

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het te archiveren verzoek van de betrokkene |

{% tabs %}
{% tab title="200: OK" %}
Het antwoord bevat het verzoek van de betrokkene (zie het hierboven beschreven object).
{% endtab %}
{% endtabs %}

### De status gearchiveerd van een verzoek van een betrokkene opheffen

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/restore/{id}`

Dit endpoint herstelt een verzoek uit de prullenbak.

#### Padparameters

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `workspaceId`<mark style="color:red;">\*</mark> | Geheel getal | De ID van de werkruimte die het verzoek van de betrokkene bevat |
| `id`<mark style="color:red;">\*</mark> | GUID | De ID (GUID) van het te herstellen verzoek van de betrokkene |

{% tabs %}
{% tab title="200: OK" %}
Het antwoord bevat het verzoek van de betrokkene (zie het hierboven beschreven object).
{% endtab %}
{% endtabs %}
