---
description: Cette page explique comment gérer les langues du widget de consentement
---

# Gestion de la langue

## Comment gérer plusieurs langues pour le widget ?

Rendez-vous sur la page de réglages du widget souhaité, puis dans l'onglet "Textes et traductions". Vous pouvez ajouter une ou plusieurs langues.

![](<../../../.gitbook/assets/Capture web\_6-5-2022\_102131\_app.dastra.eu.jpeg>)

{% hint style="warning" %}
Attention, seuls le français et l'anglais sont supportés aujourd'hui.
{% endhint %}

## Comment est détectée la langue du widget ?

Par défaut, la langue est détectée automatiquement en fonction de la langue du navigateur

## Comment forcer la langue du widget ?

Pour forcer la langue du widget, il suffit d'ajouter un attribut data-lang="" à la div du widget

```markup
<div id="cookie-consent" data-lang="fr"></div>
```

