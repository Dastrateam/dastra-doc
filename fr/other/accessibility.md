---
description: >-
  Politique d’accessibilité numérique de Dastra, standards de référence
  appliqués et démarche d’amélioration continue.
---

# Accessibilité

## Engagement

Dastra s’engage à rendre ses services numériques accessibles à tous, conformément aux standards internationaux et aux exigences réglementaires applicables.

L’accessibilité est intégrée dans notre démarche globale de conformité et d’amélioration continue.

## Référentiels et normes applicables

Notre démarche d’accessibilité repose sur les standards suivants :

* **WCAG 2.1 (niveaux A et AA)** publiées par le W3C
* **EN 301 549**, norme européenne définissant les exigences d’accessibilité des produits et services numériques
* **RGAA**, déclinaison opérationnelle française des WCAG dans le cadre réglementaire national

Les WCAG définissent 50 critères de succès aux niveaux A et AA.

Le RGAA propose un cadre méthodologique structuré permettant de vérifier la conformité des contenus HTML (HTML4, XHTML1, HTML5), CSS et JavaScript à travers un ensemble de critères de contrôle et de tests techniques.

La méthode RGAA comprend 106 critères incluant plusieurs tests par critère, certains reposant sur des techniques d’implémentation spécifiques pour limiter les marges d’interprétation.

Certains tests, notamment pour les composants d’interface dynamiques développés en JavaScript, nécessitent une vérification avec des technologies d’assistance (lecteurs d’écran, navigation clavier) dans un environnement de référence associant navigateur et système d’exploitation.

Les applications mobiles natives, logiciels et autres environnements spécifiques sont évalués directement au regard des exigences pertinentes de la norme EN 301 549.

## Audit d’accessibilité

Un premier audit RGAA 4.1.1 a été réalisé en interne le 16 octobre 2025 sur trois pages accessibles au grand public :

* La bannière de gestion des cookies, telle qu’elle s’affiche sur www.dastra.eu
* La page publique du formulaire de demande d’exercice de droits
* Le Privacy Hub

Les interfaces internes, qui demandent une authentification, ne font pas partie de ce périmètre initial. L’audit ne produit pas de taux de conformité global : seules ces trois pages ont été évaluées.

| Page | Critères conformes | Critères non conformes | Critères non applicables |
| --- | --- | --- | --- |
| Bannière de cookies | 47 | 5 | 54 |
| Formulaire de demande d’exercice de droits | 43 | 11 | 52 |
| Privacy Hub | 56 | 3 | 47 |

Les critères 7.1 et 7.2 (affichage sans JavaScript) sont relevés sur les trois pages. L’audit les juge non applicables pour la bannière, qui ne dépose aucun cookie sans JavaScript, et pour le formulaire.

## Plan d’amélioration

Les corrections se font au fil des cycles de développement. Elles concernent à ce jour :

* Le critère 3.3 (couleurs dans les composants d’interface)
* Le critère 12.6 (zones de navigation)
* Le critère 9.3 (balisage des listes) et les critères 11.5 et 11.6 (groupes de champs avec légende) du formulaire de demande

Les travaux restants portent sur :

* La navigation au clavier du formulaire de demande d’exercice de droits (critères 7.3 et 7.4)
* L’étiquette du sélecteur de langue du formulaire (critère 11.1)

L’audit recommande en outre des textes alternatifs plus précis (critère 1.1), des messages d’erreur plus explicites (critère 11.11) et, pour la bannière de cookies, de la placer en premier dans l’ordre de tabulation (critère 10.7).

### Contraste des couleurs

Le critère 3.2 (contraste du texte) dépend des couleurs que chaque client choisit dans ses réglages de design. Le contraste reste donc de la responsabilité du client : vérifiez que les couleurs retenues respectent un rapport de contraste d’au moins 4,5:1 pour le texte courant.

## État de conformité

Dernière mise à jour : 30 octobre 2026.

* L’audit RGAA initial est réalisé, sur trois pages.
* Les corrections listées ci-dessus sont livrées ; les travaux restants sont à traiter.
* La déclaration d’accessibilité détaillée n’est pas encore publiée. Elle le sera une fois les principales corrections déployées.

## Signaler un problème d’accessibilité

Si vous rencontrez une difficulté d’accès à un contenu ou à une fonctionnalité, vous pouvez nous contacter à :

contact@dastra.eu

Nous nous engageons à vous répondre dans les meilleurs délais.
