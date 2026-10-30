# Configuration API

Cette page présente l'API REST de Dastra : son adresse, ses limites d'utilisation, et la manière d'y manipuler les champs personnalisés et les tags. Pour obtenir une clé et appeler l'API, voir [Authentification](authentication.md).

{% embed url="https://youtu.be/Bl-T-slTyiQ" %}

## Configurer des API dans Dastra

API signifie _**application programming interface**_ ou « interface de programmation d'application » en français.

Les API connectent la plateforme Dastra à d'autres outils extérieurs.

Les possibilités sont multiples : connexion avec un logiciel CRM pour récupérer les acteurs de manière automatisée, synchronisation d'un outil de gestion des exercices des droits avec le module de Dastra, etc.

Dastra repose sur le standard **API REST** et notamment les requêtes HTTP suivantes :

| URI                                                                   | GET                                                                                               | POST                                                                                                                                                                                                                                           | PUT                                                                                                                                                                                                | PATCH                                                                                                                                                                                                                  | DELETE                                                                                   |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Ressource collection, telle que `http://api.exemple.com/collection/`  | _Récupère_ les URI des ressources membres de la ressource collection dans le corps de la réponse. | _Crée_ une ressource membre dans la ressource collection en utilisant les instructions du corps de la requête. L'URI de la ressource membre créée est _attribué automatiquement_ et retourné dans le champ d'en-tête _Location_ de la réponse. | _Remplace_ toutes les représentations des ressources membres de la ressource collection par la représentation dans le corps de la requête, ou _crée_ la ressource collection si elle n'existe pas. | _Met à jour_ toutes les représentations des ressources membres de la ressource collection en utilisant les instructions du corps de la requête, ou _crée éventuellement_ la ressource collection si elle n'existe pas. | _Supprime_ toutes les représentations des ressources membres de la ressource collection. |
| Ressource membre, telle que `http://api.exemple.com/collection/item3` | _Récupère_ une représentation de la ressource membre dans le corps de la réponse.                 | _Crée_ une ressource membre dans la ressource membre en utilisant les instructions du corps de la requête. L'URI de la ressource membre créée est _attribué automatiquement_ et retourné dans le champ d'en-tête _Location_ de la réponse.     | _Remplace_ toutes les représentations de la ressource membre, ou _crée_ la ressource membre si elle n'existe pas, par la représentation dans le corps de la requête.                               | _Met à jour_ toutes les représentations de la ressource membre, ou _crée éventuellement_ la ressource membre si elle n'existe pas, en utilisant les instructions du corps de la requête.                               | _Supprime_ toutes les représentations de la ressource membre.                            |

Source : [_Wikipédia_](https://fr.wikipedia.org/wiki/Representational_state_transfer)

## Adresse et versions

L'API de Dastra est accessible à l'adresse `https://api.dastra.eu`. Les routes sont versionnées et commencent par `/v1/`.

* Les routes d'un espace de travail contiennent son identifiant : `/v1/ws/{workspaceId}/{ressource}`, par exemple `/v1/ws/{workspaceId}/DataSubjectRequests`. Les identifiants figurent dans l'onglet **tenantId & workspaceId** de la page **Clés d'API & MCP**.
* Les routes qui concernent l'organisation entière n'ont pas d'identifiant d'espace de travail, par exemple `/v1/Workspaces`.

## Référence des endpoints

La liste des endpoints, avec leurs paramètres et leurs modèles de données, est publiée au format OpenAPI :

* l'interface Swagger : [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html) ;
* la définition OpenAPI au format JSON : [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json).

Elle ne contient que les endpoints publics de l'API. Les références sont aussi disponibles sur [dastra.readme.io](https://dastra.readme.io). Pour un exemple complet, voir [Cas d'usage de l'API](use-cases.md).

## Limitations

Les requêtes sont comptées par utilisateur, c'est-à-dire par le propriétaire de la clé d'API, selon leur type :

| Type de requête | Limite |
| --- | --- |
| Lecture (`GET`) | 500 par minute et 10 000 par période de 10 minutes |
| Écriture (`POST`, `PUT`, `PATCH`, `DELETE`) | 75 par minute et 1 000 par période de 10 minutes |
| Endpoints sensibles | 5 par période de 5 minutes |

Quelques endpoints, comme ceux de l'assistant IA, ont des limites plus strictes.

Au-delà d'une limite, l'API répond avec le code HTTP 429 et l'en-tête `Retry-After`, qui donne en secondes le délai avant de réessayer. Attendez ce délai avant de renvoyer la requête.

Pour consulter vos compteurs, appelez `GET https://api.dastra.eu/rate-limiting-state`.

Les options de sécurité, notamment le [filtrage IP](../features/settings/ip-filtering.md), ne s'appliquent pas aux appels faits avec une clé d'API.

## Exposition des champs personnalisés dans l'API Dastra

Dans Dastra, il est possible d'exposer dans l'API [des champs personnalisés](../features/general/custom-fields.md) conçus depuis votre espace de travail Dastra.

Les champs personnalisés sont propres à chaque espace de travail. Pour les prendre en compte dans l'API, définissez d'abord le **Nom de la variable (slug)** dans la définition du champ personnalisé :

<figure><img src="../.gitbook/assets/general-custom-fields-4.png" alt="La fenêtre d'ajout d'un champ personnalisé, avec le libellé et le nom de la variable (slug)"><figcaption><p>Le nom de la variable d'un champ personnalisé</p></figcaption></figure>

{% content-ref url="../features/general/custom-fields.md" %}
[custom-fields.md](../features/general/custom-fields.md)
{% endcontent-ref %}

La plupart des entités modifiables via l'API exposent une propriété `customFields` que vous pouvez modifier.

Si vous définissez les champs suivants dans votre espace de travail :

* `mon_champ_string` : un champ **Texte** ;
* `mon_champ_booleen` : un champ **Booléen** ;
* `mon_champ_numeric` : un champ **Nombre (entier)** ;
* `mon_champ_checkbox` : un champ **Case à cocher**.

vous pouvez les modifier de cette façon :

```json
{
  "label": "Google Analytics 4",
  "customFields": {
    "mon_champ_string": "Valeur de mon champ",
    "mon_champ_booleen": true,
    "mon_champ_numeric": 1,
    "mon_champ_checkbox": ["Pomme", "Banane"]
  }
}
```

Pour un champ **Case à cocher**, la valeur est la liste des libellés des réponses cochées.

## Le cas des tags

Pour associer des tags à une entité, récupérez d'abord les tags existants avec `GET /v1/ws/{workspaceId}/Tags`, puis ajoutez ceux que vous voulez à la propriété `tags` de l'entité, en reprenant leur `id`.

## Serveur MCP

Le serveur MCP (Model Context Protocol) permet à un assistant IA, un éditeur de code ou un terminal de travailler avec vos données Dastra. Il se configure dans l'onglet **MCP Server** de la page **Clés d'API & MCP** et nécessite le plan Dastra AI Pro. Voir [Le serveur MCP](../features/general/ai-assistant/mcp.md).

{% hint style="warning" %}
Les appels qui créent, modifient ou suppriment des données agissent sur vos fiches réelles. Testez d'abord sur un espace de travail dédié.
{% endhint %}

Les clés d'API se gèrent dans la page **Clés d'API & MCP**, réservée aux propriétaires de l'organisation. Voir [Gestion des clés d'API](../features/settings/api-keys.md).
