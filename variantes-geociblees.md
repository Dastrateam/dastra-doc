# variantes geociblées

## Présentation

Le module de consentement Dastra permet de créer des **variantes géo-ciblées** de votre bannière de cookies. Chaque variante est une version personnalisée du widget — apparence, textes, services exposés — qui s'affiche automatiquement en fonction de la **localisation géographique de l'utilisateur**, détectée via son adresse IP.

Cette fonctionnalité est particulièrement utile pour les organisations opérant dans plusieurs pays ou zones réglementaires, car les obligations en matière de consentement aux cookies varient sensiblement selon les législations locales (RGPD/ePrivacy en Europe, CCPA en Californie, LGPD au Brésil, etc.).

{% hint style="info" %}
**Pourquoi c'est important juridiquement**

La bannière conforme en France n'est pas nécessairement conforme pour un utilisateur californien (opt-out plutôt qu'opt-in) ou britannique (post-Brexit, l'ICO a ses propres lignes directrices). Les variantes géo-ciblées vous permettent d'adapter précisément votre CMP à chaque contexte légal sans multiplier les widgets.
{% endhint %}

***

## Créer une variante géo-ciblée

{% stepper %}
{% step %}
### Accéder à la configuration

Depuis le module **Cookies**, sélectionnez votre widget, puis rendez-vous dans l'onglet **Variantes**.

Cliquez sur **"Créer une variante géo-ciblée"**.
{% endstep %}

{% step %}
### Nommer la variante

Renseignez un **label** descriptif (80 caractères max). Choisissez un nom explicite pour faciliter la gestion, par exemple : `Bannière – Californie (CCPA)` ou `Bannière – Zone EEE`.
{% endstep %}

{% step %}
### Sélectionner les zones géographiques ciblées

Choisissez les **pays ou régions** pour lesquels cette variante s'appliquera. La recherche est disponible dans la liste.

Dastra propose deux raccourcis :

* **EU/EEE** : pré-sélectionne automatiquement tous les pays de l'Espace Économique Européen.
* **All adequate country** : pré-sélectionne les pays reconnus adéquats par la Commission européenne au sens de l'article 45 RGPD.

La liste est organisée par pays, avec la possibilité de cibler des **régions infra-nationales** (ex. : régions françaises, États américains). Cela permet, par exemple, de créer une variante spécifique uniquement pour la Californie au sein d'un widget plus général pour les États-Unis.

{% hint style="warning" %}
**Ordre de priorité des variantes**

Si plusieurs variantes peuvent s'appliquer à un même utilisateur (ex. un utilisateur en Île-de-France avec une variante "France" et une variante "Île-de-France"), c'est la variante **la plus spécifique** (région) qui prend la priorité sur la variante plus générale (pays).
{% endhint %}
{% endstep %}

{% step %}
### Personnaliser la variante

Une fois la variante créée, vous pouvez la configurer de manière **entièrement indépendante** du widget principal :

* **Apparence** : couleurs, disposition, boutons
* **Textes & traductions** : libellés adaptés au contexte légal local
* **Services exposés** : vous pouvez restreindre ou étendre la liste des traceurs présentés
* **Déclencheurs** : conditions d'affichage spécifiques
{% endstep %}
{% endstepper %}

***

## Cas d'usage typiques

| Situation                                     | Configuration recommandée                                                      |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| Site européen avec trafic américain           | Variante EEE (opt-in strict) + variante USA/Californie (opt-out CCPA)          |
| Site français avec une filiale allemande      | Variante France + variante Allemagne avec textes adaptés aux exigences du BfDI |
| Site global avec conformité minimale hors EEE | Widget par défaut mondial + variante EEE conforme RGPD                         |

***

## Fonctionnement technique

La détection géographique est réalisée automatiquement par le SDK Dastra à partir de **l'adresse IP** de l'utilisateur, sans nécessiter de configuration supplémentaire de votre côté.

Aucune donnée de localisation n'est stockée dans le profil de consentement de l'utilisateur : la géolocalisation sert uniquement à sélectionner la variante à afficher.

{% hint style="info" %}
Pour tester l'affichage d'une variante spécifique depuis votre navigateur, vous pouvez utiliser un VPN ou contacter le support Dastra pour activer un mode de prévisualisation par zone.
{% endhint %}

***

## Voir aussi

* [Configurer l'apparence du widget](/broken/pages/3895867aea5cca94c9192bc3bfbbd348ce81a152)
* [Textes et traductions](/broken/pages/a2948cf50302184be53cd316c9ea27cc6ebac0c8)
* [Revue régulière (fraîcheur)](/broken/pages/d06b39a1dd12a21c65281f36bbe349e5dcee5c34)
