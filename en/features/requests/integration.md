---
description: >-
  This article shows you how to integrate the data subject right request widget
  into a web page
---

# Technical integration

## Purpose

The data subject right request widget automatically collects data subject right requests of various types (deletions, modifications, rectifications...) from a page of your site.

The widget is part of the Dastra JavaScript SDK.

## Prerequisites

To set up the data subject right request widget, you need a public API key: read [API key management](../settings/api-keys.md) or [go directly to the API key management page](https://app.dastra.eu/general-settings/api).

## Setting up the widget in the dedicated interface

To start with, you need to set up the widget in the list of forms: in the **Requests** menu, click **Forms**.

<figure><img src="../../.gitbook/assets/requests-widget-1.png" alt="List of forms with the Create form button"><figcaption><p>The list of forms</p></figcaption></figure>

Always copy the code from the application: the address of the script depends on the hosting region of your organization (`cdn-bleu.dastra.eu` instead of `cdn.dastra.eu` on [Bleu](../../security/bleu.md)).

Here is a simple example of how to integrate the widget (in popup mode with an open button):

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

## Forcing the language of the form

By default, the browser language is used. If the language is not available in the widget translations, the default language is selected automatically. You can force the language of the widget by adding the **data-lang** property to the div where the form is displayed.

_In this example, Italian is selected by default (if available)_

```html
<div id="customer-subject-popup" data-lang="it"></div>
```

## Prefilling the form fields

You can prefill the form fields from the authentication context of the user. Prefilled fields are displayed **read-only** (greyed out) to the user.

**Available standard fields:**

```javascript
dastra.push(['set', 'dsr:refId', '{unique_user_id}'])
dastra.push(['set', 'dsr:email', '{email}'])
dastra.push(['set', 'dsr:givenName', '{first_name}'])
dastra.push(['set', 'dsr:familyName', '{last_name}'])
dastra.push(['set', 'dsr:address', '{address}'])
dastra.push(['set', 'dsr:zipCode', '{postcode}'])
dastra.push(['set', 'dsr:city', '{city}'])
dastra.push(['set', 'dsr:countryCode', '{country_code}']) // e.g. "FR"
dastra.push(['set', 'dsr:phoneNumber', '{phone}'])
dastra.push(['set', 'dsr:message', '{message}'])
```

The `refId` property is the unique identifier of the person in your system (customer ID, session ID...). It is displayed, read-only, only if the **Reference of the requester** field is one of the active fields of the form.

**Custom fields:**

```javascript
// Pass a complete object
var payload = {
  customFieldSlug1: 'value1',
  customFieldSlug2: 'value2'
}
dastra.push(['set', 'dsr:additionalDatas', payload])

// Or field by field (@ prefix)
dastra.push(['set', 'dsr:@customFieldSlug1', 'value1'])
```

## Sending parameters using page mode

You can also pass these parameters in the query string: prefix the parameter name with `dsr_`.

```url
https://api.dastra.eu/v1/client/data-subject-request/page?id=<Your widget id>
&key=<your public key>
&dsr_email=test@github.org
&dsr_givenName=Dastonaute
&dsr_refId=123456
&...etc...
```

## Closing the widget by clicking outside the window

If your widget uses the **Modal** layout, the window does not close when the user clicks outside it. This is by design: the risk of losing the data the user has typed is too high.

If you still want the widget to close when the user clicks outside the window, use the following code:

```javascript
window.dastra.customerSubjectReady().then((form) => {
  form.closeOnBackdrop = true
})
```

{% hint style="warning" %}
This deletes all the text typed by the user, without any warning. If the form is long, this can happen when a text selection extends beyond a long text field.
{% endhint %}

## Embedding several widgets in one page

By default, Dastra does not support several widgets in the same page.

You can still do it with two calls to `loadCustomerSubjectForm`, one per widget, with distinct selectors and widget IDs.

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

To set the initial fields of a widget in this setup, use the `form.initialData` property in `onLoad`:

```javascript
window.dastra.push(function () {
  dastra.loadCustomerSubjectForm({
    selector: '#customer-subject-form-custom',
    widgetId: widgetId,
    onLoad: function (form) {
      form.initialData = {
        givenName: 'testFirstName'
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
