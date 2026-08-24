---
description: >-
  Leer hoe u de Dastra cookie-widget kunt integreren in een webpagina met behulp van de javascript SDK.
---

# Snel aan de slag

## Voorwaarde: een API openbare sleutel ophalen

Om een publieke sleutel van de Dastra SDK op te halen, gaat u naar deze pagina: [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api)&#x20;

![](<../../../.gitbook/assets/image (88).png>)

## Configureer je widget

Configureer je widget door de onderstaande gids te volgen

{% content-ref url="../../configuration-du-widget/" %}
[widget-configuratie](../../configuration-du-widget/)
{% endcontent-ref %}

## De html-integratiecode invoegen

Voeg de HTML-code die beschikbaar is in de "Code" sectie van de Dastra Cookie toestemmingsmodule **voor het einde van de tag<BODY>** in op je website, op alle pagina's. Je kunt Google tag manager gebruiken om de code dynamisch te maken. U kunt Google tag manager gebruiken om deze code dynamisch op elke pagina in te voegen.

{% hint style="info" %}
Om de code correct te laten werken, moet je ervoor zorgen dat de publieke sleutel van je API vooraf correct is geconfigureerd.
{% endhint %}

De widgetintegratiecode ziet er als volgt uit

```markup
<div id="dastra-cookie-consent" data-widgetid="{your_widget_id}"></div>
<script src="https://app.dastra.eu/sdk/dastra.js?key={your_public_key}" async>
</script>
```

De div met het id "dastra-cookie-consent" wordt de renderlocatie voor je toestemmingswidget. Het "data-widgetid" attribuut wordt gebruikt om de aangeroepen widget te identificeren, wat vaak een getal is (int32). {uw_publieke_key} komt overeen met je publieke sleutel [API sleutel hier op te vragen](https://app.dastra.eu/general-settings/api)

Zodra de code is ingevoegd in de tag \<body> op je site, wordt de widget weergegeven op je site.

{% hint style="warning" %}
Voor optimale prestaties wordt de widget automatisch in de cache geplaatst door de browser in de sessionStorage
{% endhint %}

## Wordpress

Als je Wordpress gebruikt, vind je meer informatie in de onderstaande link over hoe de gegenereerde code aan het einde van de html-tag van je website kan worden ingevoegd.

{% content-ref url="wordpress.md" %}
[wordpress.md](wordpress.md)
{% endcontent-ref %}



Zodra de widget is geïntegreerd, ga je verder met de testfase.

{% content-ref url="../comment-tester-lintegration-dun-widget.md" %}
[comment-tester-lintegration-dun-widget.md](../comment-tester-lintegration-dun-widget.md)
{% endcontent-ref %}

