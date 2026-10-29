---
description: >-
  Apprenez à intégrer la bannière de cookies Dastra dans une page web avec le
  SDK JavaScript.
---

# Démarrage rapide

## Prérequis : récupérer une clé d'API publique

La bannière a besoin d'une clé d'API publique. Cliquez sur l'icône d'engrenage de la barre supérieure (**Réglages de l'organisation**), puis sur **Clés d'API & MCP** dans le menu de gauche. Voir [Gestion des clés d'API](../../../settings/api-keys.md).

<figure><img src="../../../../.gitbook/assets/cookies-quickstart-1.png" alt="La page Clés d'API & MCP avec la liste des clés"><figcaption><p>La page « Clés d'API & MCP »</p></figcaption></figure>

## Configurez votre bannière

Configurez votre bannière en suivant le guide ci-dessous :

{% content-ref url="../../banner/README.md" %}
[README.md](../../banner/README.md)
{% endcontent-ref %}

## Insérez le code d'intégration HTML

Insérez le code HTML disponible dans la section **Installation** de la bannière, carte **Javascript**, **avant la fermeture de la balise `</body>`** de votre site, sur toutes les pages. Vous pouvez utiliser Google Tag Manager pour insérer ce code dynamiquement sur chaque page.

{% hint style="info" %}
Pour que le code fonctionne, la clé d'API publique doit être configurée au préalable.
{% endhint %}

Voici le code d'intégration de la bannière :

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={your_public_key}" async></script>
```

La `div` dont l'id est `dastra-cookie-consent` est l'emplacement du rendu de la bannière. L'attribut `data-widgetid` identifie la bannière : c'est un nombre entier. `{your_public_key}` est votre clé d'API publique, disponible dans **Clés d'API & MCP**.

{% hint style="info" %}
Copiez toujours le code depuis l'application. Selon la région d'hébergement de votre organisation, l'adresse du script (`cdn-bleu.dastra.eu` plutôt que `cdn.dastra.eu`) et celle de l'API (`api-bleu.dastra.eu` plutôt que `api.dastra.eu`) changent.
{% endhint %}

Une fois le code inséré avant la balise `</body>` de votre site, la bannière s'affiche.

{% hint style="warning" %}
Pour de meilleures performances, le navigateur met la bannière en cache dans le `sessionStorage`.
{% endhint %}

## Rouvrir la bannière depuis un bouton

Retirer son consentement doit être aussi simple que le donner. Ajoutez sur votre site, par exemple dans le pied de page, un bouton qui rouvre la bannière. Le même extrait est affiché dans la section **Installation** de la bannière :

```html
<button type="button" onclick="dastra.openCookieConsent()">Check your cookie consent</button>
```

## WordPress

Si vous utilisez WordPress, la page suivante explique comment installer la bannière avec le plugin Dastra.

{% content-ref url="wordpress.md" %}
[wordpress.md](wordpress.md)
{% endcontent-ref %}

Une fois la bannière intégrée, passez à la phase de test.

{% content-ref url="../test.md" %}
[test.md](../test.md)
{% endcontent-ref %}
