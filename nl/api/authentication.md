---
description: >-
  Leer hoe u zich authenticeert bij de Dastra API.
---

# Authenticatie

## Uw geheime API-sleutel ophalen

De Dastra REST API gebruikt API-sleutels om elk verzoek te authenticeren. U beheert uw sleutels op de pagina **API-sleutels**, die is voorbehouden aan de eigenaars van de organisatie. Zie [API-sleutelbeheer](../features/settings/api-keys.md).

U kunt een API-sleutel gebruiken voor een specifieke werkruimte of voor de hele organisatie.

Een API-sleutel geeft toegang tot uw gegevens, dus bewaar hem veilig. Deel uw privésleutel niet in openbare delen van toepassingen, zoals GitHub of code aan de clientzijde.

Een verlopen of onbekende sleutel wordt geweigerd met status 401.

Wilt u OAuth2-authenticatie gebruiken met de "authorization\_code"-flow, vul dan de redirect-URI's en de toegestane CORS-oorsprongen in het detailpaneel van de sleutel in.

<figure><img src="../.gitbook/assets/settings-api-keys-1.png" alt="Het venster voor het aanmaken van een API-sleutel met de naam, de werkruimte, de vervaldatum en de machtigingen"><figcaption><p>Een API-sleutel aanmaken</p></figcaption></figure>

## API-sleutel (X-API-Key)

De eenvoudigste manier om u te authenticeren is de HTTP-header **X-API-Key** met het privégedeelte van uw API-sleutel, zoals in het voorbeeld hieronder:

```bash
curl -X 'GET' \
  'https://api.dastra.eu/me' \
  -H 'accept: */*' \
  -H 'X-API-Key: <your private key here>'

```

## OAuth2-flow "Authorization code"

### Autorisatie

De autorisatiefase wordt uitgevoerd door de volgende URL aan te roepen:

```bash
https://account.dastra.eu/connect/authorize?
    response_type=code&
    client_id={YOUR_CLIENT_ID}&
    redirect_uri=https://YOUR_APP/callback&
    scope=api1+offline_access&
    state={STATE}
```

**Parameters**

| Parameternaam   | Beschrijving |
| --------------- | ------------ |
| `response_type` | code |
| `client_id`     | De publieke sleutel van uw API-sleutel die in uw Dastra-account is geconfigureerd |
| `redirect_uri`  | De URL die in de Dastra-API-sleutel is geconfigureerd. U wordt aan het einde van het autorisatieproces automatisch naar deze pagina doorgestuurd |
| `scope`         | <p><code>api1</code> => verplicht<br><code>offline_access</code> => om een refresh_token te verkrijgen (lange sessies)</p> |
| `state`         | Een willekeurige tekenreeks die uw toepassing genereert om aanvallen van het type cross-site request forgery (CSRF) te voorkomen. Zie [Mitigate CSRF Attacks With State Parameters](https://auth0.com/docs/protocols/oauth2/mitigate-csrf-attacks). Clientbibliotheken doen dit meestal automatisch |

## OAuth2-flow "Client credentials"

### Authenticatiemethode

De API-authenticatie is gebaseerd op het [OAuth2-protocol](https://oauth.net/2/) met de flow "Client credentials". Deze authenticatiemodus mag alleen worden gebruikt voor server-naar-serververzoeken en nooit aan de clientzijde (bijvoorbeeld in een JavaScript-SPA).

<figure><img src="../.gitbook/assets/api-authentication-scheam.svg" alt="Diagram van de flow Client credentials: uw server vraagt een token aan bij de identificatieserver van Dastra en roept daarna de API aan met dat token"><figcaption><p>De flow Client credentials</p></figcaption></figure>

### Het token ophalen

`POST` `https://account.dastra.eu/connect/token`

Voer een tokenverzoek uit met BASIC-headers.

**Headers**

| Naam          | Type                                       | Beschrijving |
| ------------- | ------------------------------------------ | ------------ |
| Authorization | Basic {base64("{PublicKey}:{PrivateKey}")} |              |

**Request body**

| Naam        | Type   | Beschrijving        |
| ----------- | ------ | ------------------- |
| grant\_type | string | client\_credentials |
| scope       | string | api1                |

{% tabs %}
{% tab title="200: OK - toegangstoken voor REST API-bewerkingen" %}
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



Zodra u een access\_token hebt opgehaald, kunt u elk REST API-endpoint aanroepen met dit token als "Bearer token".

Om bijvoorbeeld de lijst van uw werkruimten op te halen:

`GET` `https://api.dastra.eu/v1/Workspaces`

Haal de lijst van Dastra-werkruimten op.

**Headers**

| Naam          | Type                   | Beschrijving |
| ------------- | ---------------------- | ------------ |
| Authorization | Bearer {access\_token} |              |

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

Alle verzoeken moeten via [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure) en altijd vanaf de serverzijde worden gedaan. Verzoeken zonder authenticatie mislukken met foutcode 401.

Zie de API-referentie hier: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)
