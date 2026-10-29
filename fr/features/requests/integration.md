---
description: >-
  Cet article vous présente comment intégrer le widget d'exercice de droit dans
  une page web
---

# Intégration technique

## Objectifs

Le widget d'exercice de droits collecte automatiquement, depuis une page de votre site, des demandes d'exercice de droit de différents types (suppressions, modifications, rectifications...)

Le widget est intégré au **SDK javascript** de Dastra.

## Prérequis

Pour mettre en place le widget d'exercice de droit, vous devez disposer d'**une clé publique d'API** : lisez la page [Gestion des clés d'API](../settings/api-keys.md) ou [accédez directement à la page de gestion des clés d'API](https://app.dastra.eu/general-settings/api).

## Mise en place du widget dans l'interface dédiée

Pour commencer, vous devez mettre en place le widget dans la liste des formulaires de collecte : dans le menu **Demandes**, cliquez sur **Formulaires de collecte**.

<figure><img src="../../.gitbook/assets/requests-widget-1.png" alt="Liste des formulaires de collecte avec le bouton Créer un formulaire"><figcaption><p>La liste des formulaires de collecte</p></figcaption></figure>

Voici un exemple simple d'intégration du widget (en mode popup avec un bouton d'ouverture) :

```html
<div id="customer-subject-form-custom"></div>
<button id="customer-request-button">Open the widget</button>
<script
  src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY}"
  async
></script>
<script>
  window.dastra = window.dastra || [];
  dastra.debug = true;
  window.dastra.push(function(){
    dastra.loadCustomerSubjectForm({
      selector: '#customer-subject-form-custom',
      widgetId: {your widget id},
      onLoad: function (form) {
        document.getElementById('customer-request-button').addEventListener('click',function () {
          form.open()
        })
      }
    })
  })
</script>
```

## Forcer la langue du formulaire

Par défaut, ce sera **la langue du navigateur** qui sera prise. Si la langue n'est pas disponible dans les traductions du widgets, la langue par défaut sera sélectionnée automatiquement. Vous pouvez forcer la langue courante du widget en ajoutant la propriété **data-lang** à la div où le formulaire s'affichera.

_Dans cet exemple, la langue italienne sera sélectionnée par défaut (si elle est disponible)_

```html
<div id="customer-subject-popup" data-lang="it"></div>
```

## Préremplir les champs du formulaire

Il est possible de préremplir les champs du formulaire depuis le contexte d'authentification de l'utilisateur. Les champs préremplis s'affichent en **lecture seule** (grisés) côté utilisateur.

**Champs standards disponibles :**

```javascript
dastra.push(['set', 'dsr:refId', '{identifiant_unique_utilisateur}'])
dastra.push(['set', 'dsr:email', '{email}'])
dastra.push(['set', 'dsr:givenName', '{prénom}'])
dastra.push(['set', 'dsr:familyName', '{nom}'])
dastra.push(['set', 'dsr:address', '{adresse}'])
dastra.push(['set', 'dsr:zipCode', '{code_postal}'])
dastra.push(['set', 'dsr:city', '{ville}'])
dastra.push(['set', 'dsr:countryCode', '{code_pays}']) // ex : "FR"
dastra.push(['set', 'dsr:phoneNumber', '{téléphone}'])
dastra.push(['set', 'dsr:message', '{message}'])
```

La propriété `refId` est l'identifiant unique de la personne dans votre système (identifiant client, identifiant de session...). Elle s'affiche, en lecture seule, uniquement si le champ **Référence de la demande** fait partie des champs actifs du formulaire.

**Champs personnalisés :**

```javascript
// Passer un objet complet
var payload = {
  customFieldSlug1: 'valeur1',
  customFieldSlug2: 'valeur2'
}
dastra.push(['set', 'dsr:additionalDatas', payload])

// Ou champ par champ (préfixe @)
dastra.push(['set', 'dsr:@customFieldSlug1', 'valeur1'])
```

## Envoi des paramètres en utilisant le mode page

Il est également possible de passer ces paramètres en utilisant les paramètres querystring : préfixez le nom du paramètre par `dsr_`.

```url
https://api.dastra.eu/v1/client/data-subject-request/page?id=<Your widget id>
&key=<your public key>
&dsr_email=test@github.org
&dsr_givenName=Dastonaute
&dsr_refId=123456
&...etc...
```

## Fermer le widget en cliquant en dehors de la fenêtre

Si votre widget est configuré avec le type d'affichage **Fenêtre modale (popup)**, la fenêtre ne se ferme pas lorsque l'utilisateur clique en dehors. Ce comportement est voulu : le risque de perdre les données saisies est trop important.

Si vous souhaitez malgré tout que le widget se ferme lorsque l'utilisateur clique en dehors de la fenêtre, utilisez le code suivant :

```javascript
window.dastra.customerSubjectReady().then((form) => {
  form.closeOnBackdrop = true
})
```

{% hint style="warning" %}
Cela supprime l'intégralité du texte saisi par l'utilisateur, sans aucun avertissement. Si le formulaire est long, cela peut arriver lors d'une sélection de texte qui dépasse d'un champ long.
{% endhint %}

## Intégrer plusieurs widgets dans une seule page

Par défaut, Dastra ne permet pas l'intégration de plusieurs widgets au sein de la même page.

Il est cependant possible de le faire avec deux appels à `loadCustomerSubjectForm`, un par widget, avec des sélecteurs et des identifiants de widget distincts.

```html
<html lang="en-GB">
  <body>
    <h2>My first widget</h2>
    <div id="widget-1"></div>
    <h2>My second widget</h2>
    <div id="widget-2"></div>
    <script
      async
      src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR_PUBLIC_KEY}"
    ></script>
    <script>
      window.dastra = window.dastra || []

      // Widget 1 initialization
      window.dastra.push(function () {
        window.dastra.loadCustomerSubjectForm({
          selector: '#widget-1',
          widgetId: 991, // YOUR_WIDGET_ID_
          onLoad: function (form) {
            // Initialization
          }
        })
      })

      // Widget 2 initialization
      window.dastra.push(function () {
        window.dastra.loadCustomerSubjectForm({
          selector: '#widget-2',
          widgetId: 992, // the widget identifier for the second widget
          onLoad: function (form) {
            // Initialization
          }
        })
      })
    </script>
  </body>
</html>
```

Pour définir les champs initiaux d'un widget dans cette configuration, utilisez la propriété `form.initialData` dans `onLoad` :

```javascript
window.dastra.push(function () {
  dastra.loadCustomerSubjectForm({
    selector: '#customer-subject-form-custom',
    widgetId: widgetId,
    onLoad: function (form) {
      form.initialData = {
        givenName: 'prénomTest'
      }
      document
        .getElementById('customer-request-button')
        .addEventListener('click', function () {
          form.closeOnBackdrop = true
          form.open()
        })
    }
  })
})
```
