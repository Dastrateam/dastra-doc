---
description: Pour s'authentifier sur l'API Dastra vous devez utiliser
---

# Authentification

### Obtention de la clé secrète d'API

L'API Rest Dastra utilise les clés d'API pour authentifier chaque requête. Vous pouvez gérer vos clés dans l['interface de configuration de votre organisation](https://app.dastra.eu/general-settings/api).&#x20;

Vous pouvez utiliser une clé d'API pour un espace de travail spécifique ou l'organisation complète.

Votre clé d'API permet de faire beaucoup de chose, c'est pourquoi, vous devez la conserver précieusement. Ne partagez pas votre clé secrète dans les parties publiques d'applications comme GitHub, le code client...etc...

Si vous souhaitez utiliser l'authentification OAuth2 en mode "authorization\_code", il sera nécessaire de bien configurer le ou les urls de redirection ainsi que les origines CORs autorisées.

![](<../.gitbook/assets/image (249) (1) (1) (1).png>)

## Clé d'api (X-API-Key)&#x20;

Pour vous authentifier, la manière la plus simple est d'utiliser une entête HTTP **X-API-Key** contenant la clé privée de votre clé d'API, comme dans l'exemple ci-dessous :

```bash
curl -X 'GET' \
  'https://api.dastra.eu/me' \
  -H 'accept: */*' \
  -H 'X-API-Key: <your private key here>'
```

## OAuth2 "Authorization code" flow

### Authorization

la phase d'autorisation s'effectue en appelant l'url suivante :

```
https://account.dastra.eu/connect/authorize?
    response_type=code&
    client_id={YOUR_CLIENT_ID}&
    redirect_uri=https://YOUR_APP/callback&
    scope=api1+offline_access&
    state={STATE}
```

**Paramètres**

<table><thead><tr><th width="272.5595168190588">Parameter Name</th><th width="470.9578998488362">Description</th></tr></thead><tbody><tr><td><code>response_type</code></td><td>code</td></tr><tr><td><code>client_id</code></td><td>La clé publique de votre clé d'api configuré dans votre compte Dastra</td></tr><tr><td><code>redirect_uri</code></td><td>L'url configuré dans la clé d'API de Dastra. Vous serez automatiquement redirigé sur cette page à l'issue du processus d'authorisation</td></tr><tr><td><code>scope</code></td><td><p>api1 => obligatoire</p><p>offline_access <em>=></em> pour récupérer un refresh_token (sessions longues)</p></td></tr><tr><td><code>state</code></td><td>Une clé aléatoire généré par votre application qui permet d'éviter les attaques de type cross-site request forgery (CSRF) , lire <a href="https://auth0.com/docs/protocols/oauth2/mitigate-csrf-attacks">Mitigate CSRF Attacks With State Parameters</a>. Les librairies cliente gèrent ça rapidement</td></tr></tbody></table>



## OAuth2 "Client credential" flow

### Méthode d'authentification

L'authentification de l'API s'effectue grâce à l'aide du [protocole OAuth2](https://oauth.net/2/) utilisant le flow "Client credential". Ce mode d'authentification doit être utilisé uniquement pour des requêtes de serveur à serveur et ne doit en aucun cas être utilisé côté navigateur (SPA en javascript par exemple).

![](<../.gitbook/assets/API authentication scheam.svg>)

### Récupération du token

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

Une fois que vous avez récupéré un access\_token, vous pouvez ensuite appeler n'importe quel endpoint de l'API Rest à l'aide de ce jeton d'accès en le passant en "Bearer token".&#x20;

Par exemple, pour récupérer la liste de vos espaces de travail :

<mark style="color:blue;">`GET`</mark> `https://api.dastra.eu/v1/workspaces`

Récupérer la liste des espaces de travail de Dastra

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



Toutes les requêtes doivent s'effectuer en [HTTPS](http://en.wikipedia.org/wiki/HTTP\_Secure) et toujours côté serveur. Les requêtes sans authentification échoueront avec le code d'erreur 401

Consultez les références de l'API ici : [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)\
