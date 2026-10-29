---
description: Cette page explique comment gérer les langues de la bannière de consentement.
---

# Gestion de la langue

## Ajoutez des langues à la bannière

1. Dans le menu, cliquez sur **Consentement cookies** > **Bannières**, puis sur votre bannière.
2. Dépliez la section **Textes et traductions**.
3. Cliquez sur **Ajouter la langue**, choisissez la langue dans la liste, puis cliquez sur **Ajouter la langue**.

<figure><img src="../../../.gitbook/assets/cookies-languages-1.png" alt="La section Textes et traductions avec la liste des langues de la bannière et leurs badges"><figcaption><p>La section « Textes et traductions »</p></figcaption></figure>

La première langue de la liste est la langue par défaut. Pour en choisir une autre, cliquez sur **Définir par défaut** en regard de la langue. Cliquez sur **Modifier** pour adapter les textes d'une langue.

Dans la liste de choix, les langues du groupe **Langues avec traductions** sont déjà traduites par Dastra : anglais (États-Unis), anglais (Royaume-Uni), français, allemand, espagnol, italien, néerlandais, grec, polonais et portugais. Les autres langues sont dans le groupe **Langues pas traduites** : vous saisissez vous-même les textes.

Chaque langue ajoutée porte un badge :

* **Pré-traduit** : la langue fait partie de celles que Dastra traduit ;
* **Besoin de traduction** : certains textes de la langue sont encore vides ;
* **Entièrement traduit** : tous les textes sont renseignés.

Un compteur indique le nombre de textes personnalisés sur le nombre total de textes.

## Comment est détectée la langue de la bannière ?

Par défaut, la bannière utilise la langue indiquée par l'attribut `lang` de la balise `<html>` de la page. Si cet attribut est absent, elle utilise la langue du navigateur.

Si cette langue (ou sa langue principale, par exemple `fr` pour `fr-FR`) ne figure pas dans la liste de la bannière, la bannière s'affiche dans la première langue de la liste.

## Comment forcer la langue de la bannière ?

Pour forcer la langue, ajoutez l'attribut `data-lang` à la `div` de la bannière :

```html
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}" data-lang="fr"></div>
```

Si vous chargez la bannière avec la méthode `loadCookieConsent`, passez plutôt l'option `lang` :

```javascript
dastra.push(['loadCookieConsent', {
    widgetId: {your_widget_id},
    selector: '#cookie-consent',
    lang: 'fr'
}]);
```
