---
description: Les causes les plus fréquentes d'une bannière de cookies qui ne s'affiche pas, et comment les corriger.
---

# Dépannage

Si la bannière de cookies ne s'affiche pas, vérifiez les points suivants dans l'ordre.

1. Vérifiez les URL autorisées. Dans le menu, cliquez sur **Consentement cookies** > **Bannières**, ouvrez la bannière, puis la section **Configuration**. L'adresse de votre site doit figurer dans **Urls autorisées (CORS)**, au format `https://monurl.com`, sans chemin. C'est la cause la plus fréquente : une origine absente de la liste est refusée.

   <figure><img src="../../.gitbook/assets/cookies-configure-6.png" alt="La section Configuration avec le champ Urls autorisées (CORS)"><figcaption><p>Le champ « Urls autorisées (CORS) »</p></figcaption></figure>
2. Vérifiez le statut de la bannière. Dans l'éditeur, l'interrupteur **Statut** doit être sur **Actif**.
3. Vérifiez la validité de votre clé d'API publique (n'utilisez pas la clé privée). Cliquez sur l'icône d'engrenage de la barre supérieure (**Réglages de l'organisation**), puis sur **Clés d'API & MCP**. Vérifiez que la clé existe et qu'elle n'est pas expirée. Voir [Gestion des clés d'API](../settings/api-keys.md).

   <figure><img src="../../.gitbook/assets/cookies-quickstart-1.png" alt="La page Clés d'API & MCP avec la liste des clés"><figcaption><p>La page « Clés d'API & MCP »</p></figcaption></figure>
4. Vérifiez que vous n'avez pas défini un déclencheur d'affichage par erreur. Dans la section **Déclencheurs**, une **Hauteur de scroll en %** trop élevée empêche d'afficher la bannière à l'arrivée sur la page.
5. Vérifiez les options qui masquent la bannière. L'option **Ne pas déclencher l'affichage la bannière (tous les cookies consenties par défaut seront déclenchés)** masque la bannière, de même que **Activer le Global Privacy Control (GPC)** pour les visiteurs dont le navigateur envoie ce signal. Un visiteur qui a déjà fait un choix ne voit plus la bannière : supprimez le cookie `consent-eu` de votre navigateur pour tester.
6. Vérifiez votre abonnement. Pour utiliser la bannière de consentement aux cookies, votre abonnement doit inclure la fonctionnalité. Si le menu **Consentement cookies** n'apparaît pas dans la navigation, la fonctionnalité n'est probablement pas incluse : contactez le propriétaire de votre organisation. Si l'abonnement a expiré, l'API refuse la configuration de la bannière. Pour plus d'informations, vous pouvez contacter le [support](mailto:support@dastra.eu).
7. Pour tout autre problème, [contactez le support](../../getting-started/support/request.md).
