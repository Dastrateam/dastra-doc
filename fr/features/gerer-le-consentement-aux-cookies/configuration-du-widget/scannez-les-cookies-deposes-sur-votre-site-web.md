---
description: Apprenez à scanner les cookies déposés sur votre site web.
---

# Scannez les cookies déposés sur votre site Web

DASTRA vous permets de scanner les cookies déposés sur votre site web grâce à sa fonctionnalité de **scan des cookies,** directement intégré à son module "Widget de consentement aux cookies".

## Accédez à la fonctionalité "scan des cookies" Dastra

Vous devez tout d'abord vous connecter à votre votre espace de travail Dastra. Pour apprendre à faire cela, rendez-vous sur la page suivante:

{% content-ref url="../../../getting-started/tutoriel/" %}
[tutoriel](../../../getting-started/tutoriel/)
{% endcontent-ref %}

Ensuite, vous devez vous rendre dans le module "Cookies", et cliquer sur le bouton "Créer un widget".

![Icône du module "Cookies"](../../../.gitbook/assets/capture-web-5-5-2022-165656-app-dastra-eu.jpeg)

![Cliquer sur le bouton "Créer un widget"](../../../.gitbook/assets/capture-web-5-5-2022-165746-app-dastra-eu.jpeg)

Un nouvel écran s'affiche. Vous vous trouvez dans la section "Scan des cookies".

![](../../../.gitbook/assets/capture-web-5-5-2022-165823-app-dastra-eu.jpeg)

## Scannez les cookies déposés sur votre site web

Une fois dans la section "Scan des cookies", il vous suffit de saisir le nom de domaine de votre site internet dans l'espace réservé, et de cliquer sur "Valider".

![Section "Scan des cookies"](../../../.gitbook/assets/capture-web-5-5-2022-165912-app-dastra-eu.jpeg)

{% hint style="info" %}
Votre nom de domaine doit inclure l'intégralité du préfixe "https://www." pour être pris en compte par notre moteur.
{% endhint %}

Attendez quelques secondes, et ça y est, les cookies déposés sur votre site web sont identifiés !

![Le scan est en cours](../../../.gitbook/assets/capture-web-5-5-2022-17030-app-dastra-eu.jpeg)

![Ecran d'affichage des cookies](../../../.gitbook/assets/cookies-categories-list-overview.png)

Une fois les cookies déposés sur votre site web scannés, vous pouvez procéder à leur classification.

{% content-ref url="classifiez-les-cookies-par-categories-de-consentement.md" %}
[classifiez-les-cookies-par-categories-de-consentement.md](classifiez-les-cookies-par-categories-de-consentement.md)
{% endcontent-ref %}

***



## Traitez les cookies non classés

Le scan compare les cookies détectés au référentiel de services de Dastra. Un cookie qui ne correspond à aucun service est un cookie non classé : il n'est rattaché à aucun service, il n'est jamais affiché dans la bannière publique et les visiteurs ne peuvent donc pas y consentir.

Dans les résultats du scan, un badge d'avertissement indique le nombre de cookies non classés (par exemple « 3 cookies non classés ») à côté du résumé du scan. Ces cookies sont regroupés dans l'onglet **Cookies non classés**, à côté des onglets **Services**, **Cookies trouvés** et **Répartition des catégories de cookies**.

<figure><img src="../../../.gitbook/assets/cookies-scan-unclassified-cookies-tab.png" alt="Onglet Cookies non classés dans les résultats du scan"><figcaption><p>L'onglet « Cookies non classés » des résultats du scan, avec le badge indiquant leur nombre</p></figcaption></figure>

Sélectionnez un ou plusieurs cookies à l'aide des cases à cocher (la case de l'en-tête sélectionne toute la liste), puis choisissez l'une des actions proposées.

### Ajouter des cookies à un service existant

1. Sélectionnez les cookies, puis cliquez sur **Ajouter à un service existant**.
2. Dans le champ **Service cible**, choisissez le service auquel rattacher les cookies.
3. Validez.

Tous les cookies sélectionnés sont ajoutés au service en une seule fois. Un cookie déjà présent dans le service (même nom et même domaine) n'est pas ajouté une seconde fois.

### Créer un service à partir d'une sélection

1. Sélectionnez les cookies, puis cliquez sur **Créer un nouveau service**.
2. Le formulaire du service s'ouvre, pré-rempli à partir du domaine le plus fréquent parmi les cookies sélectionnés (nom, domaine et logo du service) et contenant les cookies sélectionnés.
3. Vérifiez les informations proposées, en particulier la finalité du service, puis enregistrez.

Seuls les cookies conservés dans le service quittent la liste des cookies non classés.

### Supprimer des cookies

Sélectionnez les cookies, cliquez sur **Supprimer**, puis confirmez. Les cookies sont retirés de la liste des cookies non classés.

### Retirer un cookie d'un service

Dans l'onglet **Services** des résultats du scan, dépliez la liste des cookies d'un service, puis cliquez sur l'icône de corbeille en regard du cookie (info-bulle « Retirer de ce service »). Le cookie est détaché du service et rejoint l'onglet **Cookies non classés**.

Après chaque action, les compteurs des onglets, le badge et le graphique de répartition se mettent à jour immédiatement.

### Traiter les cookies non classés depuis l'éditeur de bannière

Il n'est pas nécessaire de traiter tous les cookies avant de créer la bannière : les cookies non traités restent attachés à la bannière et peuvent être traités plus tard. Dans l'éditeur de la bannière, le titre de la section **Services** indique le nombre de cookies non classés, et l'onglet **Cookies non classés** de cette section propose les mêmes actions : **Supprimer**, **Ajouter à un service existant** et **Créer un nouveau service**.

Lorsque tous les cookies sont rattachés à un service, l'onglet affiche le message « Tous les cookies sont classés ».

### Relancer le scan d'une bannière existante

Dans l'onglet **Services** de l'éditeur de la bannière, cliquez sur **Scan des cookies** pour relancer le scan du site. Dans les résultats, une coche verte (info-bulle « Déjà dans votre configuration ») signale les services déjà déclarés dans la bannière. Les cookies détectés qui correspondent aux cookies d'un service déjà déclaré, y compris un service personnalisé, sont rattachés à ce service et ne figurent pas parmi les cookies non classés.

{% hint style="warning" %}
Les cookies non classés ne sont jamais affichés dans la bannière publique. Rattachez chaque cookie réellement déposé par votre site à un service pour que les visiteurs puissent y consentir.
{% endhint %}

***

## Limitations et bonnes pratiques

### Cookies déposés après consentement (services opt-in)

Par défaut, un scanner de cookies navigue sur votre site sans donner de consentement. Les cookies déposés uniquement après opt-in (analytique, marketing, etc.) ne sont donc pas déclenchés et ne peuvent pas être détectés.

**Exception : si le SDK Dastra est déjà intégré sur votre site**, le scanner est capable de contourner la bannière de consentement et de collecter l'ensemble des cookies réellement déposés, y compris ceux des services opt-in. Dans ce cas, le scan produit un résultat complet sans intervention manuelle.

Si le SDK Dastra n'est pas encore en place sur le site scanné, les services opt-in devront être **ajoutés manuellement** via la bibliothèque de services.

### Services ajoutés manuellement — cookies en excès

Lorsque vous ajoutez un service depuis la bibliothèque Dastra (ex. Google Analytics, Meta Pixel), Dastra importe la liste complète des cookies que ce service _peut_ déposer dans toutes ses configurations possibles. Votre implémentation n'en utilise probablement qu'une partie.

Il est recommandé de **supprimer les cookies que votre implémentation spécifique ne dépose pas réellement**. Déclarer des cookies non utilisés est trompeur pour les visiteurs et peut poser problème lors d'un audit de conformité.

Pour identifier les cookies à conserver, croisez les résultats du scan automatique (qui détecte ce qui est effectivement déposé) avec la liste importée depuis la bibliothèque, et supprimez les entrées qui n'apparaissent pas dans le scan.
