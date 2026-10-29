---
description: Affichez une bannière de cookies différente selon la localisation géographique de l'utilisateur.
---

# Variantes géo-ciblées

## Présentation

Dans le module de consentement Dastra, vous pouvez créer des **variantes géo-ciblées** de votre bannière de cookies. Chaque variante est une version personnalisée de la bannière (apparence, textes, services exposés) qui s'affiche automatiquement en fonction de la **localisation géographique de l'utilisateur**, détectée à partir de son adresse IP.

Cette fonctionnalité est utile aux organisations présentes dans plusieurs pays ou zones réglementaires, car les obligations en matière de consentement aux cookies varient selon les législations locales (RGPD et ePrivacy en Europe, CCPA en Californie, LGPD au Brésil, etc.).

{% hint style="info" %}
**Pourquoi c'est important juridiquement**

La bannière conforme en France n'est pas nécessairement conforme pour un utilisateur californien (opt-out plutôt qu'opt-in) ou britannique (après le Brexit, l'ICO a ses propres lignes directrices). Les variantes géo-ciblées vous permettent d'adapter votre bannière à chaque contexte légal sans multiplier les bannières.
{% endhint %}

Les variantes dépendent de votre offre : la liste déroulante des variantes est désactivée si la fonctionnalité n'est pas incluse dans votre abonnement.

***

## Créer une variante géo-ciblée

### 1. Accéder à la configuration

1. Dans le menu, cliquez sur **Consentement cookies** > **Bannières**, puis sur votre bannière.
2. En haut à droite de l'éditeur, ouvrez la liste déroulante qui affiche **Configuration par défaut**. Elle liste les variantes existantes.
3. Cliquez sur **Créer une variante géo-ciblée**.

<figure><img src="../../../.gitbook/assets/cookies-geo-targeting-1.png" alt="La liste déroulante des variantes dans l'éditeur de bannière"><figcaption><p>La liste déroulante des variantes</p></figcaption></figure>

### 2. Nommer la variante

Renseignez un nom descriptif dans le champ **Nom de la variante** (80 caractères maximum), par exemple `Bannière - Californie (CCPA)` ou `Bannière - Zone EEE`.

### 3. Sélectionner les zones géographiques ciblées

Dans **Pays ou régions géographiques ciblées par la bannière**, choisissez les **pays ou régions** auxquels la variante s'applique. Une recherche est disponible dans la liste.

Dastra propose deux raccourcis, sous **Pré-sélection** :

* **UE/EEE** : sélectionne tous les pays de l'Espace économique européen.
* **Pays adéquats** : sélectionne les pays reconnus adéquats par la Commission européenne au sens de l'article 45 du RGPD.

La liste est organisée par pays et propose des **régions infranationales** (par exemple les régions françaises ou les États américains). Vous pouvez ainsi créer une variante propre à la Californie dans une bannière plus générale pour les États-Unis.

{% hint style="warning" %}
**Ordre de priorité des variantes**

Si plusieurs variantes peuvent s'appliquer à un même utilisateur (par exemple un utilisateur en Île-de-France avec une variante « France » et une variante « Île-de-France »), la variante **la plus spécifique** (la région) l'emporte sur la variante plus générale (le pays).
{% endhint %}

### 4. Personnaliser la variante

Une fois la variante créée, elle s'ouvre dans l'éditeur. Vous pouvez personnaliser :

* **Apparence & design** : couleurs, disposition, boutons ;
* **Textes et traductions** : textes adaptés au contexte légal local ;
* **Services** : vous pouvez restreindre ou étendre la liste des traceurs présentés ;
* **Déclencheurs** : conditions d'affichage propres à la variante.

{% hint style="info" %}
Une variante reprend de la bannière par défaut les paramètres suivants : les URL autorisées, la génération de la politique de cookies, le nom, le domaine et la durée de vie du cookie de consentement, le mode de stockage, le mode prévisualisation et la clé de version. Pour les modifier, ouvrez la **Configuration par défaut**.
{% endhint %}

### 5. Désactiver l'affichage de la bannière (facultatif)

Dans la section de la variante, l'option **Ne pas déclencher l'affichage la bannière (tous les cookies consenties par défaut seront déclenchés)** supprime l'affichage de la bannière pour les utilisateurs de la zone ciblée.

Lorsqu'elle est activée, aucune fenêtre de consentement ne s'affiche pour les visiteurs concernés. Tous les cookies sont alors déclenchés avec leur **consentement par défaut**, tel que configuré pour chaque service.

{% hint style="warning" %}
**Réservé aux zones sans obligation de consentement préalable**

Cette option convient aux pays dont la réglementation n'impose pas de recueillir activement le consentement avant le dépôt de cookies (par exemple certains pays hors EEE sans législation ePrivacy équivalente). Ne l'utilisez **jamais** pour des utilisateurs situés dans l'UE ou l'EEE, au Royaume-Uni ou dans toute autre juridiction qui impose un opt-in.
{% endhint %}

{% hint style="info" %}
Le consentement par défaut de chaque service se règle dans la section **Services** de la bannière. Vérifiez ces valeurs avant d'activer cette option.
{% endhint %}

***

## Cas d'usage typiques

| Situation                                     | Configuration recommandée                                                      |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| Site européen avec trafic américain           | Variante EEE (opt-in strict) + variante USA/Californie (opt-out CCPA)          |
| Site français avec une filiale allemande      | Variante France + variante Allemagne avec textes adaptés aux exigences du BfDI |
| Site global avec conformité minimale hors EEE | Bannière par défaut mondiale + variante EEE conforme au RGPD                   |

***

## Fonctionnement technique

Dastra détecte la localisation à partir de **l'adresse IP** du visiteur, sans configuration de votre part. La localisation sert à choisir la variante à afficher. Le cookie de consentement du visiteur ne contient pas sa localisation, mais le pays détecté et l'adresse IP sont enregistrés avec la [preuve de consentement](consent-proof.md).

{% hint style="info" %}
Pour tester l'affichage d'une variante depuis votre navigateur, utilisez un VPN situé dans la zone ciblée.
{% endhint %}
