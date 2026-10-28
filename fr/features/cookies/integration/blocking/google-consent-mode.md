---
description: >-
  Dastra supporte nativement le Google Consent Mode V2. Cette page décrit les
  prérequis et les étapes pour l'activer sur les services de votre widget
  cookies.
---

# Google Consent Mode V2

Dastra supporte nativement le **Google Consent Mode V2**. Cette intégration permet d'envoyer un signal `consent_update` à Google Tag Manager (GTM) dès qu'un utilisateur exprime son consentement, afin que les tags Google respectent ce choix avant de déclencher le tracking.

## Prérequis

* Le snippet de consentement par défaut (voir étape 2) doit être inséré dans le `<head>` de votre site, **avant** le chargement de Google Tag Manager.
* Dans Google Tag Manager, configurez une balise **« Google Tag »** déclenchée sur toutes les pages.
* L'intégration fonctionne avec **Google Ads** (sans personnalisation) et **Google Analytics**.
* Si vous utilisez des balises de conversion ou de remarketing Google Ads, assurez-vous qu'elles ne se déclenchent qu'après consentement, à l'aide d'un évènement personnalisé du type `dastra:consent:{slug-du-service}` (exemple : `dastra:consent:googleleads`).

## Étape 1 — Activer le Consent Mode V2 sur le service

Depuis l'intégration du widget cookies, éditez le service concerné (ex. Google Analytics, Google Ads) et activez l'interrupteur **« Consent mode V2 »**. Une fois activée, la bannière Dastra enverra automatiquement le signal `consent_update` à GTM lors de chaque interaction de l'utilisateur avec le bandeau.

Sélectionnez ensuite les **types de consentement** à piloter pour ce service (tous cochés par défaut) :

* `ad_storage`
* `analytics_storage`
* `ad_user_data`
* `ad_personalization`

<figure><img src="../../../../.gitbook/assets/cookies-service-consent-mode-v2.png" alt=""><figcaption><p>Activation du Consent Mode V2 sur un service du widget cookies</p></figcaption></figure>

Le snippet de consentement par défaut à insérer dans votre site est affiché directement dans l'interface : utilisez le bouton **Copier** pour le récupérer, puis suivez l'étape 2.

## Étape 2 — Placer le code de consentement par défaut avant GTM

Pour que les tags Google attendent le signal de consentement avant de se déclencher, insérez le snippet suivant **avant** le code d'initialisation de GTM dans votre page :

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments) }
  gtag('consent', 'default', {
    ad_storage: 'denied',
    analytics_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    wait_for_update: 500
  });
</script>
```

Ce snippet indique aux tags Google qu'ils doivent attendre au maximum 500 ms le signal `consent_update` avant d'exécuter le tracking. Si l'utilisateur accepte les services concernés, la bannière Dastra déclenche automatiquement ce signal et les tags peuvent alors s'exécuter.

{% hint style="warning" %}
Ce snippet doit impérativement être placé **avant** l'initialisation de GTM. S'il est chargé après, les tags Google peuvent se déclencher sans attendre le consentement.
{% endhint %}

## Installation : en dur ou via GTM ?

Le script Dastra CMP peut être intégré directement dans le code de la page (en dur) ou via GTM. Les deux méthodes sont valides. L'installation en dur est cependant recommandée car elle garantit que le snippet de consentement par défaut (ci-dessus) s'exécute bien avant GTM, ce qui est une condition nécessaire au bon fonctionnement du Consent Mode V2.

## Ajout de nouveaux services et réinitialisation du consentement

Dastra ne re-propose pas automatiquement le bandeau aux visiteurs ayant déjà exprimé un consentement lorsque de nouveaux services sont ajoutés à la configuration. Si vous ajoutez un nouvel outil (ex. un nouvel outil analytics) et souhaitez obtenir le consentement des visiteurs existants pour ce service, vous devez **réinitialiser les consentements** depuis l'interface Dastra. Un bouton dédié dans la configuration du widget permet de forcer l'affichage du bandeau à tous les visiteurs lors de leur prochaine visite, y compris ceux ayant déjà effectué un choix.

## Pour aller plus loin

Pour le déclenchement de tags en fonction des consentements (évènements du dataLayer, blocking triggers...), consultez la page dédiée à Google Tag Manager :

{% content-ref url="google-tag-manager.md" %}
[google-tag-manager.md](google-tag-manager.md)
{% endcontent-ref %}
