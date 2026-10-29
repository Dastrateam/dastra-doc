---
description: >-
  This page explains how to manipulate your data subject right requests directly in Dastra without integrating the javascript SDK thanks to our Rest API.
---

# API integration

As Dastra does not integrate natively with all development platforms, we provide a Rest API to manage your data subject requests from your applications.

## The data subject request object

Below is the JSON object model of a data subject request in Dastra.

<details>

<summary>The data subject request object</summary>

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

To get the object format with your own custom fields, export a request in JSON format: you obtain the JSON model of your workspace.

Request identifiers are GUIDs (for example `3fa85f64-5717-4562-b3fc-2c963f66afa6`). The workspace identifier is an integer.

## API endpoints

Here are the main endpoints you need to integrate your applications with the Dastra data subject request module.

### Create a new data subject request in Dastra

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

#### Path Parameters

| Name                                            | Type    | Description             |
| ----------------------------------------------- | ------- | ----------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace |

#### Request Body

| Name                                         | Type          | Description                                                                                                      |
| -------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| `title`<mark style="color:red;">\*</mark>    | String        | Title of the request                                                                                             |
| `message`                                    | String        | Text of the request                                                                                              |
| `locale`<mark style="color:red;">\*</mark>   | String        | Language of the requester (for example `fr`, `en`)                                                               |
| `areaId`<mark style="color:red;">\*</mark>   | Integer       | ID of the organizational unit of the request                                                                     |
| `email`                                      | String        | Email address of the requester                                                                                   |
| `dateDemand`                                 | DateTime      | Date of the request (defaults to the current date)                                                               |
| `purposes`<mark style="color:red;">\*</mark> | Array\[String] | Request types concerned (at least one). Possible values: see the `purposes` parameter of the list endpoint below |

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

### Retrieve an existing data subject request via its ID

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |
| `id`<mark style="color:red;">\*</mark>          | GUID    | The ID (GUID) of the data subject request                   |

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

### Retrieve a paginated list of data subject requests

<mark style="color:blue;">`GET`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests`

You can pass optional search parameters to filter the API response.

#### Path Parameters

| Name                                            | Type    | Description                      |
| ----------------------------------------------- | ------- | -------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace to query |

#### Query Parameters

| Name         | Type           | Description                                                                                                                                                                                                                                                                                                               |
| ------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `overtaking` | Boolean        | Search for requests whose legal response deadline has been exceeded                                                                                                                                                                                                                                                       |
| `archived`   | Boolean        | Return the requests in the recycle bin (`false` by default)                                                                                                                                                                                                                                                               |
| `q`          | String         | Text search in the title of the request                                                                                                                                                                                                                                                                                   |
| `widgetId`   | Integer        | Filter the requests that come from a collection form                                                                                                                                                                                                                                                                      |
| `areaId`     | Integer        | Filter the requests of an organizational unit                                                                                                                                                                                                                                                                             |
| `states`     | Array\[String] | Filter the requests by state (Open, IdentityValidation, Processing, Active, Closed)                                                                                                                                                                                                                                       |
| `purposes`   | Array\[String] | Filter the requests by type (Unknown, Information, Access, Rectification, Erasure, Restriction, Opposition, Portability, AdvanceDirectives, AutomatedDecision, AdministrativeAccess, DPORequest, ThirdPartyRequest, DataProtectionComplaint, DoNotSellOrShare, LimitUseSensitivePersonalInformation, WithdrawalOfConsent) |
| `ids`        | Array\[GUID]   | Select a list of requests by their IDs                                                                                                                                                                                                                                                                                    |
| `tags`       | Array\[GUID]   | Select the requests that have specific tags (pass an array of tag IDs in the query string)                                                                                                                                                                                                                                |
| `page`       | Integer        | The page to retrieve (the first page is 1)                                                                                                                                                                                                                                                                                |
| `size`       | Integer        | The number of items returned per page (20 by default)                                                                                                                                                                                                                                                                     |
| `skip`       | Integer        | The number of items to skip (replaces `page` when provided)                                                                                                                                                                                                                                                               |
| `sortBy`     | String         | The field used to order the items                                                                                                                                                                                                                                                                                         |
| `asc`        | Boolean        | `true` for ascending order                                                                                                                                                                                                                                                                                                |

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

### Update a data subject request

<mark style="color:orange;">`PUT`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |
| `id`<mark style="color:red;">\*</mark>          | GUID    | The ID (GUID) of the data subject request                   |

#### Request Body

| Name                 | Type   | Description                                                                                                                                                                     |
| -------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataSubjectRequest` | Object | The complete data subject request object (see above or our [Swagger API documentation](https://api.dastra.eu/swagger/index.html)). Its `id` field must match the ID in the URL. |

{% tabs %}
{% tab title="204: No Content" %}
The response has no content.
{% endtab %}
{% endtabs %}

### Delete a data subject request via its ID

<mark style="color:red;">`DELETE`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/{id}`

This action is irreversible: the data subject request is permanently deleted from our databases. To move it to the recycle bin without deleting it, use the archive endpoint below.

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |
| `id`<mark style="color:red;">\*</mark>          | GUID    | The ID (GUID) of the data subject request                   |

{% tabs %}
{% tab title="200: OK" %}
The response has no content.
{% endtab %}
{% endtabs %}

### Change the process step of a data subject request

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/workflow`

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |

#### Request Body

| Name                                       | Type    | Description                                                                     |
| ------------------------------------------ | ------- | ------------------------------------------------------------------------------- |
| `id`<mark style="color:red;">\*</mark>     | GUID    | The ID (GUID) of the data subject request whose process step you want to change |
| `stepId`<mark style="color:red;">\*</mark> | Integer | The ID of the process step to apply to the request                              |
| `comment`                                  | String  | Optional comment attached to the step change                                    |

### Archive a data subject request via its ID

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/archive/{id}`

This endpoint moves the data subject request to the recycle bin ("archived" state).

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |
| `id`<mark style="color:red;">\*</mark>          | GUID    | The ID (GUID) of the data subject request to archive        |

{% tabs %}
{% tab title="200: OK" %}
The response contains the data subject request (see the object described above).
{% endtab %}
{% endtabs %}

### Remove the archived status from a data subject request

<mark style="color:green;">`POST`</mark> `/v1/ws/{workspaceId}/DataSubjectRequests/restore/{id}`

This endpoint restores a request from the recycle bin.

#### Path Parameters

| Name                                            | Type    | Description                                                 |
| ----------------------------------------------- | ------- | ----------------------------------------------------------- |
| `workspaceId`<mark style="color:red;">\*</mark> | Integer | The ID of the workspace that holds the data subject request |
| `id`<mark style="color:red;">\*</mark>          | GUID    | The ID (GUID) of the data subject request to restore        |

{% tabs %}
{% tab title="200: OK" %}
The response contains the data subject request (see the object described above).
{% endtab %}
{% endtabs %}
