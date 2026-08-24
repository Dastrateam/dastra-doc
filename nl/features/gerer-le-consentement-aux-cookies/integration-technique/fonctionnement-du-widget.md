# Werking van de widget

## Algemene werking :

Over het algemeen werkt de toestemmingswidget in 3 hoofdfasen:

1. Het **voorstel** van het toestemmingsvenster
2. Het **verzamelen** van toestemming (opslaan van bewijs)
3. De daadwerkelijke **uitvoering** van de toestemming van de gebruiker

{% hint style="info" %}
De Dastra-widget maakt het mogelijk om de eerste twee stappen gedeeltelijk automatisch uit te voeren. Voor de derde stap, het daadwerkelijk afdwingen van de cookievoorkeuren van de gebruiker, moet je het toestemmingssysteem technisch integreren met diensten van derden die mogelijk cookies plaatsen. Zie de [gids voor het blokkeren van cookies](blocage-des-cookies/) voor meer informatie.
{% endhint %}

De javascript SDK van de widget moet worden aangeroepen op alle pagina's van de site die cookies gebruiken.

![Globaal bewerkingsdiagram cookie-toestemming widget](https://github.com/Dastrateam/dastra-doc-nl/blob/main/.gitbook/assets/cookie-toestemming.png)

### 1. Bezoek aan de site van de klant

De gebruiker bezoekt de website waar het js codefragment is geïnstalleerd. Om de prestaties en SEO van de webpagina's niet te beïnvloeden, wordt de SDK volledig asynchroon geladen met een cachingperiode van één dag.

### 2. en 3. Verzamelen en cachen van de widgetconfiguratie

Om de widget correct te laten functioneren op de site, heeft deze een up-to-date clientconfiguratie nodig die is opgehaald van de servers van Dastra. Om de meest recente versie te hebben, zal Dastra een GET-verzoek doen naar de widget met de openbare API-sleutel om te controleren of de widget bij de klant hoort.

{% hint style="info" %}
Als de klant zijn domein niet correct heeft ingevoerd in de widget editor, zal de editor het verzoek niet autoriseren en is het onmogelijk om de widget correct weer te geven. Om dit te verhelpen, kies je widget en voeg het ontbrekende domein toe.
{% endhint %}

### 4. Toestemming vragen aan de gebruiker

Als de "consent-eu" cookie (je kunt de naam van de cookie kiezen als je dat wilt) ontbreekt, wordt het toestemmingsvenster weergegeven. Om te testen of de widget correct wordt weergegeven, kun je deze cookie uit je browser verwijderen

### 5. Verzamelen van toestemming

Toestemmingen worden automatisch verzameld door de Dastra API via een POST-verzoek in json.

Hoewel toestemming wordt uitgedrukt per doel in de widget-interface, wordt het opgeslagen per service.

Hier is hoe het bewijs van toestemming eruit ziet zoals het is opgeslagen in onze databases:

```javascript
{
    "id": "6185fe65-0924-410d-9132-3cde838c4627",
    "sessionId": "0b93b823-ff36-4d61-8959-e9e8deee5ef8",
    "date": "2020-05-19T16:54:03.272Z",
    "dateExpiration": "2020-11-19T16:54:03.272Z",
    "type": 2,
    "widgetId": 43,
    "typeDevice": 2,
    "workSpaceId": 19,
    "consentId": "8a5e89c4-2243-4598-97c5-ba3cfb35a138",
    "toestemmingen": {
        "lang": "fr-FR",
        "versionKey": null,
        "cookieConsents": [
            {
                "id": "584ffef3-251c-4e9a-efb8-08d7fbfbee92",
                "tenantId": 0,
                "name": "Drift",
                "slug": "drift",
                "consent": true,
                "version": "6f65cb1d-85eb-4a64-976d-519679189f8d",
                "date": "2020-05-19T16:53:59.511Z",
                "purpose": 3
            }, {
                "id": "1c3baa61-0d05-44e4-da3d-08d7eeadee05",
                "tenantId": 0,
                "naam": "Google Analytics (universeel)",
                "slug": "analytics",
                "consent": true,
                "version": "6f65cb1d-85eb-4a64-976d-519679189f8d",
                "date": "2020-05-19T16:54:00.568Z",
                "purpose": 2
            }
        ]
    }
}
```

Als tegenprestatie stuurt de api een string met de naam "consentId" terug, die vervolgens maximaal 180 dagen in de browser wordt opgeslagen in de localStorage. Deze string is de unieke identifier van het toestemmingsbewijs. In geval van een geschil moet deze identifier worden opgezocht in de browser van de klant.

### 6. Uitvoering van de toestemming

Nadat we de toestemming van de gebruiker hebben verzameld, is het nu nodig om de wens van de gebruiker daadwerkelijk uit te voeren door de informatie over de toestemming door te sturen naar alle diensten van de site.

Voor deze fase nodigen we u uit om de gids over het blokkeren van cookies te raadplegen:

{% content-ref url="blocage-des-cookies/" %}
[blocage-des-cookies](blocage-des-cookies/)
{% endcontent-ref %}

{% hint style="info" %}
Met uitzondering van strikt noodzakelijke cookies moeten alle trackingdiensten van derden standaard worden geblokkeerd
{% endhint %}

Gefeliciteerd, je bent klaar om te beginnen met de technische integratie van de widget:

{% content-ref url="integration-dans-les-cms/" %}
[integration-dans-les-cms](integration-dans-les-cms/)
{% endcontent-ref %}
