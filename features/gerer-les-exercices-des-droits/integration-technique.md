---
description: >-
  Cet article vous présente comment intégrer le widget d'exercice de droit dans
  une page web
---

# Intégration technique

### Objectifs

Le widget d'exercice de droits vous permet de **collecter automatiquement depuis une page de votre site des demandes d'exercice de droit** de différents types (suppressions, modifications, rectifications...)

Le widget est intégré au **SDK javascript** de dastra.

### Prérequis

Afin de mettre en place le widget d'exercice de droit, vous devez disposer d'**une clé publique d'API** : [lire la documentation](https://doc.dastra.eu/~/changes/OdM7a8W4pn3S8n18W72A/features/settings/gestion-des-cles-dapi) ou [accéder directement à la page de gestion des clés d'API](https://app.dastra.eu/general-settings/api)

### Mise en place du widget dans l'interface dédiée

Pour commencer, vous devez **mettre en place le widget** dans[ le panel de gestion des widgets](https://app.dasta.eu/workspace/data-subject-request/integrations) d'exercice de droits :&#x20;

![](<../../.gitbook/assets/image (250) (1) (1) (1).png>)

Voici un exemple simple d'intégration du widget (en mode popup avec un bouton d'ouverture) :

```html
<div id="customer-subject-form-custom" ></div>
<button id="customer-request-button">Open the widget</button>
<script src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR PUBLIC KEY}" async></script>
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

### Comment forcer la langue du formulaire ?

Par défaut, ce sera **la langue du navigateur** qui sera prise. Si la langue n'est pas disponible dans les traductions du widgets, la langue par défaut sera sélectionnée automatiquement. Vous pouvez forcer la langue courante du widget en ajoutant la propriété **data-lang** à la div où le formulaire s'affichera.

_Dans cet exemple, la langue italienne sera sélectionnée par défaut (si elle est disponible)_

```html
<div id="customer-subject-popup" data-lang="it"></div>
```

#### Comment envoyer automatiquement des valeurs de formulaire au widget ?

Il est possible de préremplir les champs du formulaire depuis le contexte d'authentification de l'utilisateur. Les champs préremplis s'affichent en **lecture seule** (grisés) côté utilisateur.

**Champs standards disponibles :**

```javascript
dastra.push(['set', 'dsr:refId',       '{identifiant_unique_utilisateur}']);
dastra.push(['set', 'dsr:email',        '{email}']);
dastra.push(['set', 'dsr:givenName',    '{prénom}']);
dastra.push(['set', 'dsr:familyName',   '{nom}']);
dastra.push(['set', 'dsr:address',      '{adresse}']);
dastra.push(['set', 'dsr:zipCode',      '{code_postal}']);
dastra.push(['set', 'dsr:city',         '{ville}']);
dastra.push(['set', 'dsr:countryCode',  '{code_pays}']); // ex : "FR"
dastra.push(['set', 'dsr:phoneNumber',  '{téléphone}']);
dastra.push(['set', 'dsr:message',      '{message}']);
```

**Champs personnalisés :**

```javascript
// Passer un objet complet
var payload = {
  customFieldSlug1: 'valeur1',
  customFieldSlug2: 'valeur2'
};
dastra.push(['set', 'dsr:additionalDatas', payload]);

// Ou champ par champ (préfixe @)
dastra.push(['set', 'dsr:@customFieldSlug1', 'valeur1']);
```



### Envoi des paramètres en utilisant le mode page

Il est également possible de passer ces paramètres en utilisant les paramètres querystring, il suffit de préfixer le nom du paramètre par dsr\_ :&#x20;

```url
https://api.dastra.eu/v1/client/customer-subject-form?id=<Your widget id>
&key=<your public key>
&dsr_email=test@github.org
&dsr_givenName=Dastonaute
&dsr_refId=123456
&...etc...
```

### Fermer le widget en cliquant en dehors de la fenêtre

Si votre widget est configuré avec un **type d'affichage "Popup"**, nous n'avons pas mis en place le comportement de fermeture de la modal en cas de clic en dehors de la fenêtre, car les risques de perte de données saisies par l'utilisateur sont trop importants.

Cependant, si vous souhaitez que le widget se ferme lorsque l'utilisateur clique en dehors du widget, il est possible de le mettre en place à l'aide du code suivant :&#x20;

```javascript
window.dastra.customerSubjectReady().then((form) => { 
  form.closeOnBackdrop = true; 
});
```

{% hint style="warning" %}
Attention, cela aura pour effet de supprimer l'intégralité du texte saisi par l'utilisateur sans aucun avertissement ! Si le formulaire est long, cela peut se produire facilement lors d'une sélection dépassant un champ textuel long.
{% endhint %}

### Intégrer plusieurs widgets dans une seule page

Par défaut, Dastra ne permet pas l'intégration de plusieurs widgets au sein de la même page.&#x20;

Cependant, il est possible de faire cette intégration avec la méthode suivante.&#x20;

```html
<html lang="en-GB">
<body>
  <h2>My first widget</h2>
  <div id="widget-1"></div>
  <h2>My second widget</h2>
  <div id="widget-2"></div>
  <script async src="https://cdn.dastra.eu/sdk/dastra.js?key={YOUR_PUBLIC_KEY}"></script>
  <script>
    dastra = dastra || [];
    
    // Widget 1 initialization
    dastra.push(function () {
      dastra.loadCustomerSubjectForm({
        selector: "#widget-1",
        widgetId: 991, // YOUR_WIDGET_ID_
        onLoad: function (form) {
          // Initialization
        },
      });
    });

    // Widget 2 initialization
    dastra.push(function () {
      dastra.loadCustomerSubjectForm({
        selector: "#widget-2",
        widgetId: 992, // the widget identifier for the second widget
        onLoad: function (form) {
          // Initialization
        },
      });
    });
  </script>
</body>
</html>
```

Pour intégrer les champs initiaux dans cette configuration, il faut utiliser le code suivant :&#x20;

```html
window.dastra.push(function () {
  dastra.loadCustomerSubjectForm({
    selector: "#customer-subject-form-custom",
    widgetId: widgetId,
    onLoad: function (form) {
      form.initialData = {
        givenName: "prénomTest"
      };
      document
        .getElementById("customer-request-button")
        .addEventListener("click", function () {
          form.closeOnBackdrop = true;
          form.open();
        });
    },
  });
});
```
