---
description: >-
  Créez et gérez les clés d'API de votre organisation : espace de travail,
  expiration, permissions, accès au serveur MCP.
---

# Gestion des clés d'API

Cette page explique à quoi servent les clés d'API de Dastra et comment les créer et les gérer. Seuls les propriétaires de l'organisation y ont accès.

## Usages des clés d'API

* **Créer un client de l'API** de Dastra pour récupérer ou modifier les données en dehors de l'application. Ce client peut être de serveur à serveur (Client credential) ou javascript (Authorization code). Pour en savoir plus, vous pouvez [lire la documentation relative à l'authentification de l'API Dastra](../../api/authentication.md).
* **Configurer un widget d'exercice de droit** (clé publique uniquement). [Lire la documentation relative à la mise en place du widget d'exercice de droit](../requests/widget.md)
* **Configurer un widget de consentement cookies** (clé publique uniquement). [Lire la documentation de mise en place du consentement aux cookies](../cookies/README.md)
* **Connecter un outil d'IA au serveur MCP** de Dastra. [Lire la documentation du serveur MCP](../general/ai-assistant/mcp.md)

## Où gérer les clés d'API

Cliquez sur l'icône d'engrenage de la barre supérieure (**Réglages de l'organisation**), puis sur **Clés d'API & MCP** dans le menu de gauche. L'adresse directe est [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api).

La page comporte trois onglets, dont les titres s'affichent en anglais dans toutes les langues :

* **API keys** : la liste des clés. Elle indique pour chaque clé son nom, sa dernière utilisation (**Jamais** si elle n'a pas servi) et son espace de travail. Le badge **Expirée** signale une clé dont la date d'expiration est passée, et le badge `MCP` une clé autorisée à accéder au serveur MCP.
* **MCP Server** : la connexion d'un outil d'IA au serveur MCP de Dastra. Voir [Le serveur MCP](../general/ai-assistant/mcp.md).
* **tenantId & workspaceId** : l'identifiant de l'organisation (**TENANT ID**) et celui de chaque espace de travail (**WORKSPACE ID**), avec un bouton pour les copier. Ils servent aux appels d'API qui demandent ces identifiants.

## Créer une clé d'API

1. Dans l'onglet **API keys**, cliquez sur **Créer une nouvelle clé d'API**.
2. Saisissez le **Nom** de la clé.
3. Pour limiter la clé à un espace de travail, choisissez-le dans **Sélection d'un espace de travail spécifique**. Sans choix, la clé s'applique à **Tous les espaces de travail**.
4. Choisissez l'**Expiration** : **Illimitée**, 30 jours, 180 jours, 365 jours ou **Date personnalisée**.
5. À la question **Donner toutes les permissions d'accès à cette clé d'api ?**, répondez **Oui** pour une clé sans restriction, ou **Non** pour cocher uniquement les permissions que la clé peut utiliser.
6. Cliquez sur **Créer**.

<figure><img src="../../.gitbook/assets/settings-api-keys-1.png" alt="La fenêtre de création d'une clé d'API avec le nom, l'espace de travail, l'expiration et les permissions"><figcaption><p>La création d'une clé d'API</p></figcaption></figure>

Le panneau **Détails de la clé API** s'ouvre. Il présente :

* la clé publique (`client_id`) et la clé privée (`client_secret` ou clé d'API), masquée, que vous pouvez copier depuis le panneau ;
* le bouton **Renouveller la clé privée**, qui génère une nouvelle clé privée sans supprimer la clé d'API ;
* l'espace de travail, l'accès au serveur MCP, la dernière utilisation et l'expiration de la clé ;
* les **Permissions** de la clé, que le bouton de modification permet d'ajuster ;
* les origines CORS autorisées et les URI de redirection autorisées, à renseigner si vous utilisez l'API en javascript avec OAuth2 (Authorization code).

<figure><img src="../../.gitbook/assets/settings-api-keys-2.png" alt="Le panneau Détails de la clé API avec la clé privée masquée"><figcaption><p>Les détails d'une clé d'API</p></figcaption></figure>

{% hint style="info" %}
L'expiration et l'accès au serveur MCP se choisissent à la création et ne peuvent plus être modifiés ensuite. Pour changer l'un des deux, créez une nouvelle clé.
{% endhint %}

## Utiliser une clé avec le serveur MCP

Si votre offre inclut le serveur MCP (Dastra AI Pro), la fenêtre de création propose l'option **Autoriser cette clé à accéder au serveur MCP (nécessite un espace de travail spécifique)**. Activez-la et choisissez un espace de travail : le serveur MCP refuse une clé sans cette option ou sans espace de travail. Les clés autorisées portent un badge `MCP` dans la liste. Voir [Le serveur MCP](../general/ai-assistant/mcp.md).

## Remplacer ou supprimer une clé

{% hint style="warning" %}
Conservez précieusement vos clés d'API. La clé privée ne doit en aucun cas être diffusée publiquement.

Si la sécurité de votre clé d'API est compromise, cliquez sur **Renouveller la clé privée** dans le panneau de détails, ou supprimez la clé depuis la liste (menu à trois points > **Supprimer**) et créez-en une nouvelle.
{% endhint %}
