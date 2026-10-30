# Liste des endpoints d'API

Cette page explique où consulter la liste à jour des endpoints de l'API Dastra et comment la lire.

## Consulter la référence

La liste des endpoints est générée à partir de l'API elle-même et publiée au format OpenAPI :

* l'interface Swagger : [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html). Elle affiche pour chaque endpoint ses paramètres, ses modèles de données et ses codes de réponse, et vous pouvez y tester un appel après avoir renseigné votre clé avec le bouton **Authorize** ;
* la définition OpenAPI au format JSON : [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json), pour générer un client dans votre langage ;
* la référence d'API : [https://dastra.readme.io](https://dastra.readme.io).

Seuls les endpoints publics de l'API y figurent. Le module Conformité (référentiels, contrôles, tests, audits) a sa propre référence, dont les routes commencent par `/v1/compliance/ws/{workspaceId}/` : [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

## Lire un chemin

Un chemin commence par la version de l'API, puis, pour un espace de travail, par son identifiant :

| Chemin | Usage |
| --- | --- |
| `/v1/ws/{workspaceId}/Actors` | Les acteurs d'un espace de travail |
| `/v1/ws/{workspaceId}/DataSubjectRequests` | Les demandes d'exercice de droits d'un espace de travail |
| `/v1/ws/{workspaceId}/Tags` | Les tags d'un espace de travail |
| `/v1/Workspaces` | Les espaces de travail de l'organisation |

La méthode HTTP indique l'action : `GET` lit, `POST` crée, `PUT` ou `PATCH` modifie et `DELETE` supprime. Selon la ressource, des routes complémentaires existent, comme `/batch-delete` pour supprimer plusieurs éléments ou `/export/{format}` pour exporter une liste.

Pour vérifier qu'une clé d'API fonctionne, appelez `GET https://api.dastra.eu/me`.

Pour l'authentification, voir [Authentification](authentication.md). Pour les limites de requêtes, les champs personnalisés et les tags, voir [Configuration API](configuration.md). Pour des exemples d'appels, voir [Cas d'usage de l'API](use-cases.md).
