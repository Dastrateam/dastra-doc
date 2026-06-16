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

![Icône du module "Cookies"](<../../../.gitbook/assets/capture-web-5-5-2022-165656-app-dastra-eu.jpeg>)

![Cliquer sur le bouton "Créer un widget"](<../../../.gitbook/assets/capture-web-5-5-2022-165746-app-dastra-eu.jpeg>)

Un nouvel écran s'affiche. Vous vous trouvez dans la section "Scan des cookies".

![](<../../../.gitbook/assets/capture-web-5-5-2022-165823-app-dastra-eu.jpeg>)

## Scannez les cookies déposés sur votre site web&#x20;

Une fois dans la section "Scan des cookies", il vous suffit de saisir le nom de domaine de votre site internet dans l'espace réservé, et de cliquer sur "Valider".

![Section "Scan des cookies"](<../../../.gitbook/assets/capture-web-5-5-2022-165912-app-dastra-eu.jpeg>)

{% hint style="info" %}
Votre nom de domaine doit inclure l'intégralité du préfixe "https://www." pour être pris en compte par notre moteur.
{% endhint %}

&#x20;Attendez quelques secondes, et ça y est, les cookies déposés sur votre site web sont identifiés !

![Le scan est en cours](<../../../.gitbook/assets/capture-web-5-5-2022-17030-app-dastra-eu.jpeg>)

![Ecran d'affichage des cookies](<../../../.gitbook/assets/image-51.png>)

Une fois les cookies déposés sur votre site web scannés, vous pouvez procéder à leur classification.

{% content-ref url="classifiez-les-cookies-par-categories-de-consentement.md" %}
[classifiez-les-cookies-par-categories-de-consentement.md](classifiez-les-cookies-par-categories-de-consentement.md)
{% endcontent-ref %}

***

## Limitations et bonnes pratiques

### Cookies déposés après consentement (services opt-in)

Par défaut, un scanner de cookies navigue sur votre site sans donner de consentement. Les cookies déposés uniquement après opt-in (analytique, marketing, etc.) ne sont donc pas déclenchés et ne peuvent pas être détectés.

**Exception : si le SDK Dastra est déjà intégré sur votre site**, le scanner est capable de contourner la bannière de consentement et de collecter l'ensemble des cookies réellement déposés, y compris ceux des services opt-in. Dans ce cas, le scan produit un résultat complet sans intervention manuelle.

Si le SDK Dastra n'est pas encore en place sur le site scanné, les services opt-in devront être **ajoutés manuellement** via la bibliothèque de services.

### Services ajoutés manuellement — cookies en excès

Lorsque vous ajoutez un service depuis la bibliothèque Dastra (ex. Google Analytics, Meta Pixel), Dastra importe la liste complète des cookies que ce service *peut* déposer dans toutes ses configurations possibles. Votre implémentation n'en utilise probablement qu'une partie.

Il est recommandé de **supprimer les cookies que votre implémentation spécifique ne dépose pas réellement**. Déclarer des cookies non utilisés est trompeur pour les visiteurs et peut poser problème lors d'un audit de conformité.

Pour identifier les cookies à conserver, croisez les résultats du scan automatique (qui détecte ce qui est effectivement déposé) avec la liste importée depuis la bibliothèque, et supprimez les entrées qui n'apparaissent pas dans le scan.







