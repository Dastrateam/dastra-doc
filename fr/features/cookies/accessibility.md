---
description: >-
  Les résultats de l'audit d'accessibilité RGAA de la bannière de gestion des
  cookies et les points à corriger.
---

# Conformité RGAA

Cette page présente les résultats du dernier audit d'accessibilité de la bannière de gestion des cookies, réalisé selon le référentiel général d'amélioration de l'accessibilité (RGAA).

## Audit du 16 octobre 2025

* **Référentiel** : RGAA 4.1.1.
* **Type d'audit** : audit interne (visite initiale) de la bannière telle qu'elle s'affiche sur www.dastra.eu.
* **Résultat** : 47 critères conformes, 5 non conformes et 54 non applicables.

{% hint style="info" %}
La grille d'audit ne calcule aucun taux de conformité global. Cet audit ne vaut pas déclaration de conformité complète de la bannière.
{% endhint %}

## Points non conformes

| Critère | Constat | Suite donnée |
| --- | --- | --- |
| 3.2 Contraste des textes | Le texte courant, gris sur fond blanc, a un contraste de 3,98:1 pour 4,5:1 exigé. Le lien « Notre politique de cookies », orange sur fond blanc, est lui aussi concerné. | Dépend des couleurs choisies dans les paramètres de la bannière. Voir ci-dessous. |
| 3.3 Couleurs des composants d'interface | Les mots en gras reprennent la couleur du texte courant. | La grille indique « corrigé ». Le SDK de la version 3.0.0 affiche les mots en gras dans une teinte plus foncée que le texte courant. |
| 7.1 et 7.2 Affichage sans JavaScript | La bannière ne s'affiche pas sans JavaScript. | L'auditeur note que, sans JavaScript, aucun cookie n'est déposé : il n'y a alors aucun consentement à recueillir. |
| 12.6 Zones de navigation | Le lien vers la politique de cookies n'est pas dans une zone de navigation. | La grille indique « corrigé ». Le SDK de la version 3.0.0 place ce lien dans un élément `<nav>`, sur l'écran d'accueil et sur l'écran des préférences. |

L'audit recommande aussi de placer la bannière en premier dans l'ordre de tabulation (critère 10.7, conforme).

### Contrastes : vos réglages comptent

Les couleurs du texte et des liens de la bannière viennent des paramètres de chaque bannière : **Couleur principale des textes** et **Couleur primaire** dans la section **Apparence & design**. Le contraste relève donc de votre choix : Dastra ne peut pas le garantir pour chaque bannière. Vérifiez que le texte et les liens ont un contraste d'au moins 4,5:1 avec le fond. Voir [Configurez la bannière](banner/configure.md).

## Rapport de 2021

L'audit précédent date du 16 mars 2021. Il porte sur la grille RGAA 4.1, il est rédigé en français et il précède plusieurs évolutions de la bannière (Global Privacy Control, bouton « Continuer sans accepter », formes du bouton flottant). Il reste disponible à titre de référence historique.

{% file src="../../.gitbook/assets/audit-rgaa.zip" %}
Téléchargez le rapport d'audit RGAA de 2021
{% endfile %}
