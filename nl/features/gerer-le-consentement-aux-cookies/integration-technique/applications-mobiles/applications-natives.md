---
description: >-
  Deze pagina legt uit hoe de api voor toestemmingsbeheer werkt.
  API voor toestemmingsbeheer. Deze API kan eenvoudig worden geïntegreerd in
  toepassingen.
---

# Native toepassingen

{% swagger baseUrl="https://api.dastra.eu" path="/v1/client/cookie-widget-settings/:id?key=:key" method="get" summary="Haal widgetconfiguratie op" expanded="false" %}
{% swagger-description %}
Dit endpoint wordt gebruikt om de volledige configuratie van de widget op te halen
{% endswagger-description %}

{% swagger-parameter in="path" name="id" type="number" %}
ID van de widgetconfiguratie
{% endswagger-parameter %}

{% swagger-parameter in="query" name="culture" type="string" %}
De locale van de widgetconfiguratie (en, fr...)
{% endswagger-parameter %}

{% swagger-parameter in="query" name="key" type="string" %}
De geleverde openbare api-sleutel
{% endswagger-parameter %}

{% swagger-response status="200" description="Cake succesvol opgehaald." %}
```
{
  "translation": {
    "id": "35dddc1a-3ceb-49a8-a8d2-fc343fdb56a3",
    "lang": "nl",
    "order": 0,
    "buttonBackLabel": "Retour",
    "buttonAcceptLabel": "Alles accepteren",
    "buttonSettingsLabel": "Aanpassen",
    "buttonViewPurposeLabel": "Selecteer doeleinden",
    "buttonConfirmLabel": "Selectie opslaan",
    "buttonAcceptAllLabel": "Alles accepteren",
    "buttonLaterLabel": "Alles afwijzen",
    "buttonViewMoreLabel": "Bekijk de lijst",
    "noticeUrlButtonLabel": "Lees ons cookiebeleid",
    "startupTitle": "Wij gebruiken cookies",
    "startupDisclaimer":"Cookies stellen ons in staat inhoud en advertenties te personaliseren, functies voor sociale media aan te bieden en ons verkeer te analyseren. We delen ook informatie over het gebruik van onze site met onze sociale media-, advertentie- en analysepartners, die dit kunnen combineren met andere informatie die u aan hen hebt verstrekt of die zij hebben verzameld via uw gebruik van hun diensten."
    "innerTitle": "Dit zijn onze diensten die cookies gebruiken",
    "innerDisclaimer": "In dit configuratiescherm kunt u de cookies kiezen die u tijdens het browsen toestaat,
    "categoryNecessaryLabel": "Noodzakelijke cookies",
    "categoryNecessaryExcerpt": "Noodzakelijke cookies helpen een website bruikbaar te maken door basisfuncties mogelijk te maken, zoals paginanavigatie en toegang tot beveiligde delen van de website. Zonder deze cookies kan de website niet goed functioneren.",
    "categoryNecessaryDescription": "Noodzakelijke cookies helpen om een website bruikbaar te maken door basisfuncties zoals paginanavigatie en toegang tot beveiligde delen van de website mogelijk te maken. Zonder deze cookies kan de website niet goed functioneren.",
    "categoryPreferenceLabel": "Voorkeuren",
    "categoryPreferenceExcerpt": "Voorkeurscookies stellen een website in staat om informatie te onthouden die de manier verandert waarop de site zich gedraagt of wordt weergegeven, zoals uw voorkeurstaal of de regio waarin u zich bevindt.",
    "categoryPreferenceDescription": "Voorkeurcookies stellen een website in staat om informatie te onthouden die de manier verandert waarop de site zich gedraagt of wordt weergegeven, zoals uw voorkeurstaal of de regio waarin u zich bevindt."
    "categoryAnalyticalLabel": "Statistieken",
    "categoryAnalyticalExcerpt": "Statistische cookies helpen website-eigenaren, door anoniem informatie te verzamelen en te rapporteren, om te begrijpen hoe bezoekers omgaan met websites.",
    "categoryAnalyticalDescription": "Statistische cookies helpen website-eigenaren, door anoniem informatie te verzamelen en door te geven, om te begrijpen hoe bezoekers omgaan met websites.",
    "categoryMarketingLabel": "Marketing",
    "categoryMarketingExcerpt": "Marketingcookies worden gebruikt om bezoekers op websites te volgen. Het doel is om advertenties weer te geven die relevant en interessant zijn voor de individuele gebruiker en daardoor waardevoller voor externe uitgevers en adverteerders.",
    "categoryMarketingDescription": "Marketingcookies worden gebruikt om bezoekers van verschillende websites te volgen. Het doel is om advertenties weer te geven die relevant en interessant zijn voor de individuele gebruiker en daardoor waardevoller voor externe uitgevers en adverteerders.",
    "categoryOtherLabel": "Overige cookies",
    "categoryOtherExcerpt": "Schrijf hier een korte beschrijving",
    "categoryOtherDescription": "Schrijf hier een lange beschrijving",
    "categoryIABLabel": "IAB Reclamediensten",
    "categoryIABExcerpt": "Deze services gebruiken cookies voornamelijk om de kwaliteit van reclameboodschappen te verbeteren."
    "categoryIABDescription": "Deze services gebruiken cookies voornamelijk om de kwaliteit van reclameboodschappen te verbeteren,
    "cookieDeclaration": null,
    "buttonYes": "Yes",
    "buttonNo": "No",
    "viewProof": "Bewijs van toestemming weergeven",
    "successMessage": "Uw voorkeuren zijn opgeslagen! Bedankt! "
  },
  "groups": [
    {
      "label": "Marketing",
      "excerpt": "Marketingcookies worden gebruikt om bezoekers van verschillende websites te volgen. Het doel is om advertenties weer te geven die relevant en interessant zijn voor de individuele gebruiker en daardoor waardevoller voor externe uitgevers en adverteerders.",
      "purpose": 3,
      "services": [
        {
          "id": "e213aca4-79b7-4b93-2bad-08d897969898",
          "name": "yrdy",
          "slug": "yrdy",
          "domain": "www.dastra.eu",
          "logoUrl": "https://api.dastra.eu/v1/favicon/www.dastra.eu",
          "privacyPolicyUrl": null,
          "defaultConsent": false,
          "requiredConsent": true,
          "purpose": 3,
          "description": null,
          "cookies": [
            {
              "id": "de529978-3ae0-496d-bf25-daac9d7230c7",
              "serviceId": null,
              "name": "yrdy",
              "description": null,
              "value": null,
              "path": null,
              "domain": null,
              "expiryDays": null
            }
          ],
          "lang": "nl"
        }
      ],
      "description": "Marketingcookies worden gebruikt om bezoekers van verschillende websites te volgen. Het doel is om advertenties weer te geven die relevant en interessant zijn voor de individuele gebruiker en daardoor waardevoller voor externe uitgevers en adverteerders.",
      "requiredConsent": true,
      "defaultConsent": false
    }
  ],
  "lang": "nl",
  "versionKey": "36df80ee-235c-4485-b9e2-f28f5568f572",
  "lastVersionGeneration": "2020-12-03T14:28:55.5450603",
  "buttonLogoUrl": null,
  "enabled": true,
  "label": "www.dastra.eu",
  "displayLogo": true,
  "hideCopyright": false,
  "showFixedButton": true,
  "developerMode": true,
  "saveConsentProof": true,
  "isValid": false,
  "position": "BottomLeft",
  "timerTrigger": 0,
  "scrollTrigger": 0,
  "autoGeneratedCookieNotice": false,
  "cookieNoticeUrl": "",
  "bgColor": "#FFFFFFFF",
  "colorTitle": "#2E4058",
  "colorBtn": "#686868",
  "colorText": "#2E4058",
  "colorPrimary": "#E7630A",
  "colorSecondary": "#48ba61",
  "customCSS": "",
  "enableIAB": false,
  "tcfVersion": 1,
  "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, schreefloos",
  "dateCreation": "2020-12-03T14:20:19.3703522",
  "dateUpdate": "2021-03-15T12:32:09.848664",
  "consentCookieExpiryTime": 180,
  "consentCookieName": null,
  "id": 1,
  "tenant": null,
  "tenantId": 1
}
```
{% endswagger-response %}
{% endswagger %}

{% swagger baseUrl="https://api.dastra.eu" path="/v1/client/collect/:id?key=:key" method="post" summary="Toestemming registratie" %}
{% swagger-description %}
Deze methode wordt gebruikt om toestemming voor cookies te verzamelen
{% endswagger-description %}

{% swagger-parameter in="path" name="id" type="string" %}
ID van de widgetconfiguratie
{% endswagger-parameter %}

{% swagger-parameter in="query" name="key" type="string" %}
De openbare api-sleutel
{% endswagger-parameter %}

{% swagger-parameter in="body" name="consents" type="object" %}
&#x20;De lijst van gebruikers toestemmingen
\
`{`\
cookieConsents":`
`[`\
&#x20; `{`\
&#x20; `"toestemming":true, // True als toegestaan, false als geweigerd``.
&#x20; `"id":"e213aca4-79b7-4b93-2bad-08d897969898", // Cookies id`.
&#x20; `"date":"2021-03-15T14:00:04.133Z",`\
&#x20; `"name":"yrdy",`
&#x20; `"slug":"yrdy",`
&#x20; `"purpose":3``
&#x20; `}`\
`],`\
`"lang":"nl-NL",`
`"consentId":"6f47576e-5a0c-4219-8efe-331e72bab73a",`\
`"date":1615809009744`\
`}`\
\
\
\
\
\
\
\
\
\
&#x20;
{% endswagger-parameter %}

{% swagger-parameter in="body" name="type" type="string" %}
CookieEventType Bezoek,Afsluiten,Toestemmingen
{% swagger-parameter %}

{% swagger-parameter in="body" name="consentId" type="string" %}
De huidige toestemmings-id (indien eerder verzameld)
{% endswagger-parameter %}

{% swagger-parameter in="body" name="userId" type="string" %}
Aangepaste gebruikers-id (
{% endswagger-parameter %}

{% swagger-response status="200" description="Geef de id van de verzamelde toestemming terug" %}
```
140f213b-de17-4572-99a7-5075ccbcbbec
```
{% endswagger-response %}
{% endswagger %}