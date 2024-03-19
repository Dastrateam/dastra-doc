---
description: >-
  Découvrez comment mettre en place le consent mode V2 de Google vous permettant
  d'utiliser Google Analytics ou Google Ads en mode dégradé sans collecte du
  consentement.
---

# Consent mode V2 (Google)

{% hint style="info" %}
Il s'agit d'une fonctionnalité encore en beta
{% endhint %}

### Principe de fonctionnement

Le "[Consent Mode V2](https://support.google.com/google-ads/answer/10000067?hl=fr)" de Google est une fonctionnalité qui permet aux éditeurs de sites web de mieux contrôler la collecte de données des utilisateurs en fonction de leur consentement aux cookies et autres outils de suivi.&#x20;

Il fonctionne en ajustant les paramètres des tags publicitaires et analytiques pour limiter la collecte de données lorsque le consentement de l'utilisateur n'a pas été obtenu. Cela permet aux éditeurs de respecter les réglementations telles que le RGPD tout en maintenant une certaine capacité à collecter des données pour des activités essentielles.&#x20;

Le Consent Mode V2 utilise des signaux de consentement pour personnaliser l'expérience publicitaire et analytique, ce qui permet une meilleure gestion des préférences de confidentialité des utilisateurs. En résumé, il offre un moyen plus granulaire pour les éditeurs de gérer la collecte de données en fonction du consentement des utilisateurs, tout en maintenant une certaine fonctionnalité publicitaire et analytique.

### Mise en place facile

1. **Créer une bannière de consentement aux cookies**
2. Intégrer le widget **en cochant la case "Activer le consent mode V2".** Il est recommandé d'utiliser les outils de taggage de type Google Tag Manager
3. Ajouter un service du type Google Ads ou Google Analytics et cocher la case "Activer le consent mode V2"

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption><p>Exemple ici</p></figcaption></figure>

Cocher les différents types d'autorisations que vous octroyez si le consentement est donné pour le service en question.

Lorsque le consentement sera donné, automatiquement, Dastra fera le nécessaire pour transmettre à google tag manager les informations de consentement.

Si le service est consenti par défaut, cela activera automatiquement le tag pour tous les utilisateurs

### Comment mettre à jour mon script pour qu'il supporte le "consent mode V2" ?

Insérez le script suivant dans la balise \<head> de votre site web

```html
<script>
    window.dastra = window.dastra || [];
    window.dastra.consentModeV2Enabled = true;
</script>
```



