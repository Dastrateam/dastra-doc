---
description: Zur Authentifizierung bei der Dastra-API müssen Sie Folgendes verwenden
---

# Authentifizierung

### Erhalt des geheimen API-Schlüssels

Die Dastra REST-API verwendet API-Schlüssel zur Authentifizierung jeder Anfrage. Sie können Ihre Schlüssel in der [Konfigurationsoberfläche Ihrer Organisation](https://app.dastra.eu/general-settings/api) verwalten.

Sie können einen API-Schlüssel für einen bestimmten Mandanten oder die gesamte Organisation verwenden.

Ihr API-Schlüssel ermöglicht viele Aktionen, daher sollten Sie ihn sorgfältig aufbewahren. Teilen Sie Ihren geheimen Schlüssel nicht in öffentlichen Bereichen von Anwendungen wie GitHub, clientseitigem Code usw.

Wenn Sie die OAuth2-Authentifizierung im Modus "authorization\_code" verwenden möchten, müssen die Weiterleitungs-URL(s) sowie die autorisierten CORS-Ursprünge korrekt konfiguriert werden.

![](<../.gitbook/assets/Einen neuen API-Schlüssel erstellen (1).png>)

## API-Schlüssel (X-API-Key)

Zur Authentifizierung ist die einfachste Methode die Verwendung eines HTTP-Headers **X-API-Key**, der den privaten Schlüssel Ihres API-Schlüssels enthält, wie im folgenden Beispiel:

```bash
curl -X 'GET' \
  'https://api.dastra.eu/me' \
  -H 'accept: */*' \
  -H 'X-API-Key: <your private key here>'
```

## OAuth2 "Authorization code" Flow

### Authorization

Die Autorisierungsphase erfolgt durch Aufruf der folgenden URL:

```
https://account.dastra.eu/connect/authorize?
    response_type=code&
    client_id={YOUR_CLIENT_ID}&
    redirect_uri=https://YOUR_APP/callback&
    scope=api1+offline_access&
    state={STATE}
```

**Parameter**

<table><thead><tr><th width="272.5595168190588">Parameter Name</th><th width="470.9578998488362">Description</th></tr></thead><tbody><tr><td><code>response_type</code></td><td>code</td></tr><tr><td><code>client_id</code></td><td>Der öffentliche Schlüssel Ihres in Ihrem Dastra-Konto konfigurierten API-Schlüssels</td></tr><tr><td><code>redirect_uri</code></td><td>Die im Dastra-API-Schlüssel konfigurierte URL. Sie werden nach Abschluss des Autorisierungsprozesses automatisch auf diese Seite weitergeleitet</td></tr><tr><td><code>scope</code></td><td><p>api1 => erforderlich</p><p>offline_access <em>=></em> um ein refresh_token zu erhalten (lange Sitzungen)</p></td></tr><tr><td><code>state</code></td><td>Ein von Ihrer Anwendung generierter zufälliger Schlüssel, der Cross-Site-Request-Forgery-Angriffe (CSRF) verhindert, siehe <a href="https://auth0.com/docs/protocols/oauth2/mitigate-csrf-attacks">Mitigate CSRF Attacks With State Parameters</a>. Client-Bibliotheken handhaben dies schnell</td></tr></tbody></table>

## OAuth2 "Client credential" Flow

### Authentifizierungsmethode

Die API-Authentifizierung erfolgt mithilfe des [OAuth2-Protokolls](https://oauth.net/2/) unter Verwendung des "Client credential"-Flows. Dieser Authentifizierungsmodus darf ausschließlich für Server-zu-Server-Anfragen verwendet werden und darf keinesfalls browserseitig eingesetzt werden (z. B. SPA in JavaScript).

![](../.gitbook/assets/api-authentication-scheam.svg)

### Token abrufen

<mark style="color:green;">`POST`</mark> `https://account.dastra.eu/connect/token`

Perform a token request using BASIC Headers

#### Headers

| Name                               | Type          | Description                                |
| ---------------------------------- | ------------- | ------------------------------------------ |
| <mark style="color:red;">\*</mark> | Authorization | Basic {base64("{PublicKey}:{PrivateKey}")} |

#### Request Body

| Name                               | Type        | Description         |
| ---------------------------------- | ----------- | ------------------- |
| <mark style="color:red;">\*</mark> | grant\_type | client\_credentials |
| <mark style="color:red;">\*</mark> | scope       | api1                |

{% tabs %}
{% tab title="200: OK The access_token necessary to perform operations on the REST API" %}
```javascript
{
  "access_token":"tNQoqsSePv0DnSSNVJv1aDxzSFh9H2z3YBKtuBKqWAU",
  "expires_in":3600,
  "token_type":"Bearer",
  "scope":"api1"
}
```
{% endtab %}
{% endtabs %}

Sobald Sie ein access\_token erhalten haben, können Sie anschließend jeden Endpunkt der REST-API mit diesem Zugriffstoken aufrufen, indem Sie es als "Bearer Token" übergeben.

Zum Beispiel, um die Liste Ihrer Mandanten abzurufen:

<mark style="color:blue;">`GET`</mark> `https://api.dastra.eu/v1/workspaces`

Liste der Dastra-Mandanten abrufen

#### Headers

| Name                               | Type          | Description            |
| ---------------------------------- | ------------- | ---------------------- |
| <mark style="color:red;">\*</mark> | Authorization | Bearer {access\_token} |

{% tabs %}
{% tab title="200: OK " %}
```javascript
{
  "items": [
    {
      "id": 1,
      "tenantId": 1,
      "label": "My data company",
      "logoUrl": null,
      "state": "Active",
      "permissions": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 1
    },
    {
      "id": 2,
      "tenantId": 1,
      "label": "My test workspace",
      "logoUrl": null,
      "state": "Active",
      "permissions": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 1
    },
    {
      "id": 3,
      "tenantId": 1,
      "label": "My experimentation workspace",
      "logoUrl": null,
      "state": "Active",
      "permissions": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 0
    }
  ],
  "total": 3
}
```
{% endtab %}
{% endtabs %}

Alle Anfragen müssen über [HTTPS](https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol_Secure) und immer serverseitig erfolgen. Anfragen ohne Authentifizierung schlagen mit dem Fehlercode 401 fehl.

Die API-Referenz finden Sie hier: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)<br>
