---
description: Gérez la conformité vie privée pour vos utilisateurs américains (CCPA/CPRA, GPC, DoNotTrack) avec le widget de consentement Dastra.
---

# Conformité US : CCPA, GPC et DoNotTrack

## Contexte réglementaire

Contrairement au RGPD qui impose un **opt-in** (consentement préalable), la législation américaine repose principalement sur un modèle **opt-out** : les traceurs peuvent être déposés par défaut, mais l'utilisateur doit pouvoir s'y opposer facilement.

Les principales réglementations à connaître :

| Loi         | État        | Modèle  | En vigueur depuis |
| ----------- | ----------- | ------- | ----------------- |
| CCPA / CPRA | Californie  | Opt-out | 2020 / 2023       |
| CPA         | Colorado    | Opt-out | 2023              |
| VCDPA       | Virginie    | Opt-out | 2023              |
| CTDPA       | Connecticut | Opt-out | 2023              |

{% hint style="info" %}
**Le GPC est obligatoire en Californie**

Depuis la CPRA (2023), les entreprises doivent honorer le signal **Global Privacy Control (GPC)** comme une demande d'opt-out de la vente et du partage de données personnelles.
{% endhint %}

***

## Approche recommandée avec Dastra

### 1. Créer une variante géo-ciblée pour les États-Unis

La façon la plus simple de gérer vos utilisateurs américains est de créer une **variante géo-ciblée** depuis l'onglet **Variantes** de votre widget.

Pour la **Californie (CCPA/CPRA)**, configurez la variante avec un modèle opt-out : les cookies non essentiels sont actifs par défaut, l'utilisateur peut se désinscrire. Pensez également à ajouter un lien **"Ne pas vendre ni partager mes données"** dans le footer de votre site, qui ouvre directement le widget.

Pour les **autres États américains** sans obligation de bannière, vous pouvez activer l'option **"Ne pas afficher de bannière"** avec les consentements par défaut configurés selon votre politique.

{% content-ref url="variantes-geo-ciblees.md" %}
[variantes-geo-ciblees.md](variantes-geo-ciblees.md)
{% endcontent-ref %}

***

### 2. Honorer les signaux GPC et DoNotTrack

Deux signaux navigateur permettent à un utilisateur d'indiquer son refus de suivi sans interagir avec une bannière :

| Signal                          | Standard | Légalement contraignant (CA) | Description                                                    |
| ------------------------------- | -------- | ---------------------------- | -------------------------------------------------------------- |
| **GPC** (`globalPrivacyControl`) | W3C      | ✅ Oui (CPRA)                | Signal opt-out de la vente/partage des données                 |
| **DNT** (`doNotTrack`)           | W3C      | ❌ Non                       | Signal de préférence "ne pas pister" (non contraignant légalement) |

Dastra ne détecte pas ces signaux nativement. Le snippet suivant les intercepte **avant la première interaction de l'utilisateur** et applique automatiquement l'opt-out sur les catégories analytique et marketing — à condition que l'utilisateur n'ait pas déjà enregistré un consentement explicite dans son navigateur.

```html
<script>
var isOptOut = navigator.globalPrivacyControl === true
            || navigator.doNotTrack === "1"
            || window.doNotTrack === "1";

if (isOptOut) {
  dastra = dastra || [];
  dastra.push(['cookieReady', function(manager) {
    if (!manager.consent.hasConsented()) {
      manager.consent.setPurposeConsent('Analytical', false);
      manager.consent.setPurposeConsent('Marketing', false);
      manager.consent.dispatchEvent(); // applique les choix sans les persister
    }
  }]);
}
</script>
```

{% hint style="info" %}
**`dispatchEvent()` vs `save()` — quelle différence ?**

- **`dispatchEvent()`** applique les choix pour la session en cours **sans rien écrire** dans le localStorage du navigateur. Le signal GPC ou DNT est re-détecté à chaque chargement de page. Si l'utilisateur désactive GPC dans son navigateur, le comportement normal reprend automatiquement. C'est l'approche recommandée pour honorer ces signaux.
- **`save()`** enregistre le consentement de façon persistante dans le localStorage, comme si l'utilisateur avait fait un choix explicite via le widget. À utiliser uniquement lorsque vous souhaitez mémoriser un choix entre les sessions.
{% endhint %}

{% hint style="info" %}
**À quoi sert `hasConsented()` ?**

Cette vérification garantit que l'opt-out automatique ne remplace pas un consentement que l'utilisateur aurait déjà exprimé explicitement via le widget. Si l'utilisateur a déjà fait un choix, ce choix est respecté.
{% endhint %}

{% hint style="warning" %}
Ce snippet doit être placé **avant** la balise de chargement du widget Dastra pour qu'il soit pris en compte dès le premier chargement de la page.
{% endhint %}

Les labels de catégories à utiliser avec `setPurposeConsent` :

| Catégorie   | Label          |
| ----------- | -------------- |
| Nécessaires | `Necessary`    |
| Préférences | `Preference`   |
| Analytique  | `Analytical`   |
| Marketing   | `Marketing`    |
| Autre       | `Other`        |
| Non classé  | `Unclassified` |

***

## Récapitulatif

| Mécanisme                  | Implémentation        | Légalement requis (CA) |
| -------------------------- | --------------------- | ---------------------- |
| Variante géo-ciblée CCPA   | Interface Dastra      | ✅ Oui                 |
| Détection GPC              | Snippet JS ci-dessus  | ✅ Oui (CPRA)          |
| Détection DNT              | Snippet JS ci-dessus  | ❌ Recommandé          |
