---
description: >-
  Avant de vous lancer dans l'implémentation technique du widget Dastra, nous
  vous recommandons de passer par une étape d'audit des cookies de vos sites
  web.
---

# Etude préliminaire

## 1. Rapprochez vous de votre webmaster ou agence web

Avant d'implémenter le widget Dastra, nous vous recommandons de vous rapprocher de la personne responsable de l'intégration des tags et autres marqueurs de votre site web, et de l'inviter dans votre espace de travail. Cette personne pourra ainsi récupérer les éléments de code générés par Dastra qui seront nécessaires à la réalisation des diverses actions techniques (mise en place de la bannière, du blocage effectif des cookies en cas de non-consentement...).

## 2. Effectuez un mini-audit des cookies de votre site ou web-app

Pour effectuer cet audit, vous pouvez vous appuyer sur le template de fichier Excel ci-dessous :

{% file src="../../../.gitbook/assets/template-audit.xlsx" %}

Ce mini audit facilitera grandement le travail d'intégration de l'équipe technique.

### Listez les services/cookies associés à votre nom de domaine

Pour vous aider, vous pouvez utiliser notre outil de scan de cookies clé en main : [https://app.dastra.eu/workspace/19/cookie-widget/integration/scan](https://app.dastra.eu/workspace/19/cookie-widget/integration/scan)\
Celui-ci vous permettra d'identifier à la volée les services installés sur votre site à partir de notre base de données de cookies.

{% content-ref url="scannez-les-cookies-deposes-sur-votre-site-web.md" %}
[scannez-les-cookies-deposes-sur-votre-site-web.md](scannez-les-cookies-deposes-sur-votre-site-web.md)
{% endcontent-ref %}

En complément, il est recommandé d'examiner avec précision l'ensemble des services installés sur votre site (examen du code source de la page, inspection des cookies...). Des outils comme [https://builtwith.com/](https://builtwith.com/) peuvent également vous venir en aide pour lister ces services.

Pour chaque domaine ou site web que vous souhaitez cartographier, nous vous recommandons de rédiger une liste exhaustive des services tiers utilisant les traceurs.

Une fois que vous avez la liste des services associés à votre site, vous allez devoir définir la stratégie de blocage à adopter.

### Définition des finalités

Chaque service identifié devra être classé dans l'une de ces catégories :&#x20;

| Type                    | Id |
| ----------------------- | -- |
| Strictement nécessaires | 0  |
| Préférences             | 1  |
| Analytique              | 2  |
| Marketing               | 3  |
| Autre                   | 4  |

### Identification du type d'intégration du service

Pour chaque service, vous allez devoir identifier la manière avec laquelle le tag js est intégré dans la page :

* Tag javascript direct dans la page
* Intégration dans le code js de la page (Développement interne)
* Intégration dans un outil de taggage (Google Tag Manager)
* Autres:  iframe, ...

### Définition de la stratégie de blocage à adopter

Pour bloquer les cookies par défaut, il existe plusieurs stratégies possibles qui dépendront de vos besoins:

* **Ne plus utiliser** : cette librairie n'est en fait pas nécessaire, vous pouvez donc la retirer complètement des sources du site ;
* **Bloquer complètement** : L'exécution de la balise est totalement bloquée tant que l'utilisateur n'a pas accepté les cookies ;
* **Blocage partiel** : Seules les fonctionnalités de traçage sont bloquées (si la librairie le permet). Certaines librairies peuvent en effet fonctionner avec un mode complètement dégradé sans aucune dégradation de performance.





