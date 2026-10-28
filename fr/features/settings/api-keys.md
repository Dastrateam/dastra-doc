---
description: Cette page vous explique comment créer des clés d'APIs dans Dastra
---

# Gestion des clés d'API

### A quoi servent les clés d'API ?

* **Créer un client de l'API** de Dastra pour récupérer ou modifier les données en dehors de l'application. Ce client peut être de serveur à serveur (Client credential) ou javascript (Authorization code). Pour en savoir plus, vous pouvez [lire la documentation relative à l'authentification de l'API Dastra](../../api/authentication.md).
* **Configurer un widget d'exercice de droit** (clé publique uniquement). [Lire la documentation relative à la mise en place du widget d'exercice de droit](../requests/widget.md)
* **Configurer un widget de consentement cookies** (clé publique uniquement). [Lire la documentation de mise en place du consentement aux cookies](../cookies/README.md)
* **Connecter un outil d'IA au serveur MCP** de Dastra. [Lire la documentation du serveur MCP](../generalites/ai-assistant/serveur-mcp.md)

### Comment générer une clé d'API ?

1. [Accédez au gestionnaire](https://app.dastra.eu/general-settings/api) de clé de Dastra (Seuls les propriétaires de compte ont accès à cette partie)
2. Cliquez sur "**créer une clé d'API**"
3. Renseignez le nom de la clé et les urls de redirection et cors (si vous souhaitez utiliser l'API en javascript en OAuth2)
4. Cliquez sur "**enregistrer**"
5. Une fois votre clé d'API créée, vous pouvez la copier et la coller directement depuis le gestionnaire (clé privée ou publique)

{% hint style="info" %}
**Pour une utilisation avec le serveur MCP**, renseignez également le champ **Sélection d'un espace de travail spécifique** : une clé qui n'est liée à aucun espace de travail est refusée par le serveur MCP. Les clés éligibles portent un badge `MCP` dans la liste.
{% endhint %}

{% hint style="warning" %}
**Conservez précieusement vos clés d'APIs ! La clé privée ne doit être en aucun cas diffusée publiquement !**

**Si la sécurité de votre clé d'API est compromise**, vous pouvez la supprimer du gestionnaire et en générer une nouvelle
{% endhint %}
