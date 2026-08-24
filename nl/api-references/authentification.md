---
description: Om u te authenticeren bij de Dastra API moet u gebruik maken van
---

# Authenticatie

### API geheime sleutel ophalen

De Dastra API Rest gebruikt API-sleutels om elk verzoek te authenticeren. U kunt uw sleutels beheren in de[ configuratie-interface van uw organisatie](https://app.dastra.eu/general-settings/api). &#x20;

U kunt een API-sleutel gebruiken voor een specifieke werkruimte of voor de hele organisatie.

Met uw API-sleutel kunt u veel dingen doen en daarom moet u deze veilig bewaren. Deel je geheime sleutel niet in de openbare delen van applicaties zoals GitHub, client code, etc.

Als je OAuth2 authenticatie in de "authorization\_code" modus wilt gebruiken, dan moet je de omleiding url('s) en de geauthoriseerde COR's origins configureren.

![](<../.gitbook/assets/image (249) (1) (1) (1).png>)

## OAuth2 "Autorisatie code" stroom

### Autorisatie

de autorisatie fase wordt uitgevoerd door de volgende url aan te roepen:

```
https://account.dastra.eu/connect/authorize?
    response_type=code&
    client_id={YOUR_CLIENT_ID}&
    redirect_uri=https://YOUR_APP/callback&
    scope=api1+offline_access&
    state={STATE}
```

**Parameters**

<table><thead><tr><th width="272.5595168190588">Parameter Name</th><th width="470.9578998488362">Beschrijving</th></tr></thead><tbody><tr><td><code>response_type</code></td><td>code</td></tr><tr><td><code>client_id</code></td><td>De openbare sleutel van uw api-sleutel die is geconfigureerd in uw Dastra-account</td></tr><tr><td><code>redirect_uri</code></td><td>De url die is geconfigureerd in de Dastra API-sleutel. U wordt automatisch doorgestuurd naar deze pagina aan het einde van het autorisatieproces</td></tr><tr><td><code>scope</code></td><td><p>api1 => mandatory</p><p>offline_access <em>=></em> om een refresh_token op te halen (lange sessies)</p></td></tr><tr><td><code>state</code></td><td>Een willekeurige sleutel die wordt gegenereerd door uw applicatie om cross- site request forgery (CSRF)-aanvallen voorkomt, lees <a href="https://auth0.com/docs/protocols/oauth2/mitigate-csrf-attacks">Mitigate CSRF Attacks With State Parameters</a>. Clientbibliotheken kunnen dit snel afhandelen</td></tr></tbody></table>


## OAuth2 "Client credential" stroom

### Authenticatiemethode

De API wordt geauthenticeerd met behulp van het [OAuth2 protocol] (https://oauth.net/2/) met behulp van de "Client credential" stroom. Deze authenticatiemethode mag alleen worden gebruikt voor server-naar-serververzoeken en mag nooit aan de browserzijde worden gebruikt (SPA in javascript bijvoorbeeld).

![](<../.gitbook/assets/API authenticatie scheam.svg>)

### Het token herstellen

{% swagger method="post" path="/connect/token" baseUrl="https://account.dastra.eu" summary=" %}
{% swagger-beschrijving %}
Voer een tokenverzoek uit met BASIC-headers
{% endswagger-description %}

{% swagger-parameter in="body" type="scope" required="true" %}
api1
{% endswagger-parameter %}

{% swagger-parameter in="body" required="true" type="grant_type" %}
client_credentials
{% endswagger-parameter %}

{% swagger-parameter in="header" type="Authorization" required="true" %}
Basic {base64("{PublicKey}:{PrivateKey}")}
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Het toegangs_token dat nodig is om bewerkingen op de REST API uit te voeren" %}

```javascript
{
  "access_token":"tNQoqsSePv0DnSSNVJv1aDxzSFh9H2z3YBKtuBKqWAU",
  "verloopt_in":3600,
  "token_type":"Bearer",
  "scope": "api1"
}
```
{% endswagger-response %}
{% endswagger %}

Als je eenmaal een toegangstoken hebt opgehaald, kun je elk Rest API endpoint aanroepen met dit toegangstoken door het als een "Bearer token" &#x20 door te geven;

Bijvoorbeeld, om de lijst van je workspaces op te halen :

{% swagger method="get" path="" baseUrl="https://api.dastra.eu/v1/workspaces" summary="" %}
{% swagger-description %}
Verkrijg de lijst van Dastra workspaces
{% endswagger-description %}

{% swagger-parameter in="header" type="Authorization" required="true" %}
Bearer {access_token}
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="" %}
```javascript
{
  "items": [
    {
      "id": 1,
      "huurderId": 1,
      "label": "Mijn gegevens bedrijf",
      "logoUrl": null,
      "status": "Activa",
      "permissies": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 1
    },
    {
      "id": 2,
      "tenantId": 1,
      "label": "Mijn testwerkruimte",
      "logoUrl": null,
      "status": "Activa",
      "permissies": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 1
    },
    {
      "id": 3,
      "tenantId": 1,
      "label": "Mijn experimenteerwerkruimte",
      "logoUrl": null,
      "status": "Activa",
      "permissies": null,
      "dataSubjectArchivedRetentionDays": null,
      "nbEntities": 0
    }
  ],
  "total": 3
}
```
{% endswagger-response %}
{% endswagger %}



Alle verzoeken moeten worden gedaan via [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure) en altijd aan de serverkant. Verzoeken zonder authenticatie zullen mislukken met foutcode 401.

Zie de API referenties hier: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)^.