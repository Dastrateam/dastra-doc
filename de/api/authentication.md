---
description: Erfahren Sie, wie Sie sich bei der Dastra-API authentifizieren.
---

# Authentifizierung

## Ihren geheimen API-Schlüssel abrufen

Die Dastra-REST-API verwendet API-Schlüssel, um jede Anfrage zu authentifizieren. Sie verwalten Ihre Schlüssel auf der Seite **API-Schlüssel & MCP**, die den Inhabern der Organisation vorbehalten ist. Siehe [API-Schlüssel verwalten](../features/settings/api-keys.md).

Sie können einen API-Schlüssel für einen bestimmten Mandanten oder für die gesamte Organisation verwenden.

Ein API-Schlüssel gewährt Zugriff auf Ihre Daten, bewahren Sie ihn daher sicher auf. Teilen Sie Ihren privaten Schlüssel nicht in öffentlichen Bereichen von Anwendungen, etwa auf GitHub oder in clientseitigem Code.

Ein abgelaufener oder unbekannter Schlüssel wird mit dem Status 401 abgelehnt.

Wenn Sie die OAuth2-Authentifizierung mit dem Ablauf „authorization\_code“ verwenden möchten, tragen Sie die Weiterleitungs-URIs und die erlaubten CORS-Ursprünge im Detailbereich des Schlüssels ein.

<figure><img src="../.gitbook/assets/settings-api-keys-1.png" alt="Das Fenster zum Erstellen eines API-Schlüssels mit Name, Mandant, Ablaufdatum und Berechtigungen"><figcaption><p>Einen API-Schlüssel erstellen</p></figcaption></figure>

## API-Schlüssel (X-API-Key)

Am einfachsten authentifizieren Sie sich mit dem HTTP-Header **X-API-Key**, der den privaten Teil Ihres API-Schlüssels enthält, wie im folgenden Beispiel:

```bash
curl -X 'GET' \
  'https://api.dastra.eu/me' \
  -H 'accept: */*' \
  -H 'X-API-Key: <your private key here>'

```

## OAuth2-Ablauf „Authorization code“

### Autorisierung

Die Autorisierungsphase wird durch Aufruf der folgenden URL durchgeführt:

```bash
https://account.dastra.eu/connect/authorize?
    response_type=code&
    client_id={YOUR_CLIENT_ID}&
    redirect_uri=https://YOUR_APP/callback&
    scope=api1+offline_access&
    state={STATE}
```

**Parameter**

| Parametername | Beschreibung |
| --- | --- |
| `response_type` | code |
| `client_id` | Der öffentliche Teil Ihres API-Schlüssels, der in Ihrem Dastra-Konto konfiguriert ist |
| `redirect_uri` | Die im Dastra-API-Schlüssel konfigurierte URL. Am Ende des Autorisierungsvorgangs werden Sie automatisch auf diese Seite weitergeleitet |
| `scope` | <p><code>api1</code> => erforderlich<br><code>offline_access</code> => um ein refresh_token zu erhalten (lange Sitzungen)</p> |
| `state` | Eine zufällige Zeichenfolge, die Ihre Anwendung erzeugt, um Cross-Site-Request-Forgery-Angriffe (CSRF) zu verhindern. Siehe [Mitigate CSRF Attacks With State Parameters](https://auth0.com/docs/protocols/oauth2/mitigate-csrf-attacks) (auf Englisch). Client-Bibliotheken übernehmen dies in der Regel automatisch |

## OAuth2-Ablauf „Client credentials“

### Authentifizierungsmethode

Die Authentifizierung der API beruht auf dem [OAuth2-Protokoll](https://oauth.net/2/) mit dem Ablauf „Client credentials“. Dieser Authentifizierungsmodus sollte nur für Server-zu-Server-Anfragen verwendet und nie auf der Clientseite eingesetzt werden (zum Beispiel in einer JavaScript-SPA).

<figure><img src="../.gitbook/assets/api-authentication-scheam.svg" alt="Diagramm des Ablaufs Client credentials: Ihr Server fordert beim Identifikationsserver von Dastra ein Token an und ruft dann die API mit diesem Token auf"><figcaption><p>Der Ablauf Client credentials</p></figcaption></figure>

### Das Token abrufen

`POST` `https://account.dastra.eu/connect/token`

Senden Sie eine Token-Anfrage mit BASIC-Headern.

**Header**

| Name | Typ | Beschreibung |
| --- | --- | --- |
| Authorization | Basic {base64("{PublicKey}:{PrivateKey}")} |  |

**Anfragetext**

| Name | Typ | Beschreibung |
| --- | --- | --- |
| grant\_type | string | client\_credentials |
| scope | string | api1 |

{% tabs %}
{% tab title="200: OK - Access Token for REST API Operations" %}
```json
{
  "access_token": "tNQoqsSePv0DnSSNVJv1aDxzSFh9H2z3YBKtuBKqWAU",
  "expires_in": 3600,
  "token_type": "Bearer",
  "scope": "api1"
}
```
{% endtab %}
{% endtabs %}

Sobald Sie ein access\_token abgerufen haben, können Sie jeden Endpunkt der REST-API aufrufen und dieses Token als „Bearer-Token“ verwenden.

Um zum Beispiel die Liste Ihrer Mandanten abzurufen:

`GET` `https://api.dastra.eu/v1/Workspaces`

Ruft die Liste der Dastra-Mandanten ab.

**Header**

| Name | Typ | Beschreibung |
| --- | --- | --- |
| Authorization | Bearer {access\_token} |  |

{% tabs %}
{% tab title="200: OK" %}
```json
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

Alle Anfragen müssen über [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure) und immer serverseitig erfolgen. Anfragen ohne Authentifizierung scheitern mit dem Fehlercode 401.

Die API-Referenz finden Sie hier: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)
