---
description: Apprenez à tester l'intégration d'une bannière de consentement.
---

# Tester l'intégration d'une bannière

## Activez le mode prévisualisation

Dans la section **Configuration** de la bannière, ouvrez le bloc des paramètres avancés et activez **Mode prévisualisation**.

<figure><img src="../../../.gitbook/assets/cookies-test-1.png" alt="L'interrupteur Mode prévisualisation dans la section Configuration"><figcaption><p>L'interrupteur « Mode prévisualisation »</p></figcaption></figure>

Le mode prévisualisation désactive le cache de la configuration de la bannière : vous voyez vos modifications en direct. Il désactive aussi la collecte des statistiques.

{% hint style="warning" %}
Ne laissez pas le mode prévisualisation actif en production : il dégrade les performances de la bannière.
{% endhint %}

Les adresses `localhost` avec un port, par exemple `http://localhost:3000`, sont toujours acceptées, avec ou sans mode prévisualisation.

## Prévisualisez la bannière sur votre site

Cliquez sur **Prévisualiser** en haut de l'éditeur. Le bouton est désactivé tant qu'aucune adresse n'est renseignée dans **Urls autorisées (CORS)**. Choisissez le site, saisissez si besoin le chemin d'une page et la langue, puis cliquez sur **Lancement de l'aperçu**. Le code de la bannière doit déjà être installé sur le site ciblé.

## Utilisez la clé d'API suivante

```
dastra00-0testing1-key
```

{% hint style="info" %}
Cette clé affiche un exemple de bannière de consentement. Vous ne pouvez pas en modifier la configuration. Elle sert à effectuer des tests d'intégration, par exemple dans un jsFiddle.
{% endhint %}
