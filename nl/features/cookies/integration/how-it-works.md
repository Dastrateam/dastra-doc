# Werking van de banner

## Werking van de licentie

In tegenstelling tot andere oplossingen die toestemmingsbanners per domein verkopen, gebruikt de licentie van Dastra twee criteria:

* Maximaal maandelijks verkeer: het totale aantal gebruikerssessies (of bezoeken) op uw websites gedurende één maand.
* Het aantal banners: u configureert een banner met een reeks cookies en diensten, die u kunt hergebruiken op meerdere websites of subdomeinen. De toestemmingscookie kan op meerdere subdomeinen werken (bijvoorbeeld `*.example.com`).

Het aantal domeinen en subdomeinen is dus onbeperkt per banner.

<figure><img src="../../../.gitbook/assets/cookies-widget-multi-site-architecture.png" alt="Eén Dastra-banner die op meerdere sites wordt gebruikt, met de dienstenpool van elke site"><figcaption><p>Eén banner kan meerdere sites en subdomeinen bedienen</p></figcaption></figure>

## Algemene werking

De toestemmingsbanner werkt in drie hoofdfasen:

1. Het voorstel van het toestemmingsvenster.
2. Het verzamelen van toestemming (opslag van het bewijs).
3. De daadwerkelijke uitvoering van de toestemming van de gebruiker.

{% hint style="info" %}
De Dastra-banner dekt de eerste twee stappen grotendeels automatisch. Voor de derde stap, die de cookievoorkeuren van de gebruiker toepast, moet u het toestemmingssysteem technisch integreren met de diensten van derden die cookies kunnen plaatsen. Zie de [gids voor het blokkeren van cookies](blocking/README.md).
{% endhint %}

De JavaScript-SDK van de banner moet worden aangeroepen op alle pagina's van de site die cookies gebruiken.

![Overzicht van de werking van de cookietoestemmingsbanner](../../../.gitbook/assets/cookie-consent.png)

### 1. Bezoek aan de website van de klant

De bezoeker opent de website waarop het JavaScript-codefragment is geïnstalleerd. Om de prestaties en de SEO van uw pagina's niet te beïnvloeden, wordt de SDK asynchroon geladen en één dag in de cache bewaard.

### 2. en 3. De bannerconfiguratie ophalen en in de cache bewaren

Om te werken heeft de banner een actuele configuratie nodig die van de servers van Dastra wordt opgehaald. Voor de meest recente versie doet de banner een GET-verzoek met de openbare API-sleutel, waarmee wordt gecontroleerd of de banner bij de klant hoort.

{% hint style="info" %}
Als het domein van de site niet in de banner is ingesteld, wordt het verzoek geweigerd en verschijnt de banner niet. Open de banner onder **Toestemming voor cookies** > **Banners** en voeg het adres van de site toe bij **Geautoriseerde URL's (CORS)**, in de sectie **Configuratie**.
{% endhint %}

### 4. Toestemming vragen aan de gebruiker

Als de cookie `consent-eu` ontbreekt (u kunt de naam van de cookie wijzigen), verschijnt het toestemmingsvenster. Verwijder deze cookie uit uw browser om te testen of de banner correct wordt weergegeven.

### 5. Toestemming verzamelen

Toestemmingen worden automatisch verzameld door de Dastra API via een POST-verzoek in JSON.

In de interface van de banner wordt toestemming per doeleinde gegeven, maar ze wordt per dienst opgeslagen.

Zo ziet een bewijs van toestemming eruit zoals het in onze databases is opgeslagen. Interne technische velden worden niet getoond.

```json
{
    "id": "6185fe65-0924-410d-9132-3cde838c4627",
    "sessionId": "0b93b823-ff36-4d61-8959-e9e8deee5ef8",
    "date": "2026-10-12T16:54:03.272Z",
    "dateExpiration": "2027-04-10T16:54:03.272Z",
    "type": 2,
    "widgetId": 43,
    "typeDevice": 2,
    "workSpaceId": 19,
    "consentId": "8a5e89c4-2243-4598-97c5-ba3cfb35a138",
    "countryCode": "FR",
    "referrer": "https://www.example.com/pricing",
    "consents": {
        "lang": "fr-FR",
        "versionKey": "6f65cb1d-85eb-4a64-976d-519679189f8d",
        "cookieConsents": [
            {
                "id": "584ffef3-251c-4e9a-efb8-08d7fbfbee92",
                "tenantId": 0,
                "name": "Drift",
                "slug": "drift",
                "consent": true,
                "version": "6f65cb1d-85eb-4a64-976d-519679189f8d",
                "date": "2026-10-12T16:53:59.511Z",
                "purpose": 3
            }, {
                "id": "1c3baa61-0d05-44e4-da3d-08d7eeadee05",
                "tenantId": 0,
                "name": "Google Analytics",
                "slug": "google-analytics",
                "consent": true,
                "version": "6f65cb1d-85eb-4a64-976d-519679189f8d",
                "date": "2026-10-12T16:54:00.568Z",
                "purpose": 2
            }
        ]
    }
}
```

Als antwoord geeft de API een `consentId` terug. Die wordt samen met de keuzes van de bezoeker opgeslagen in de opslag voor toestemming: standaard de cookie `consent-eu`, of `localStorage` als u die modus hebt gekozen. De levensduur is die van de instelling **Levensduur van toestemmingscookie (standaard 180 dagen)** (standaard 180 dagen, van 1 tot 365 dagen). Deze identifier is de unieke identifier van het bewijs van toestemming. Bij een geschil is dit de identifier die u in de browser van de klant moet opzoeken.

### 6. Uitvoering van de toestemming

Nadat de toestemming is verzameld, moet u de keuze van de gebruiker toepassen door de informatie over de toestemming door te geven aan alle diensten van de site.

Voor deze fase verwijzen wij naar de gids voor het blokkeren van cookies:

{% content-ref url="blocking/README.md" %}
[Cookies blokkeren](blocking/README.md)
{% endcontent-ref %}

{% hint style="info" %}
Met uitzondering van strikt noodzakelijke cookies moeten alle trackingdiensten van derden standaard worden geblokkeerd.
{% endhint %}

U kunt nu beginnen met de technische integratie van de banner:

{% content-ref url="quickstart/README.md" %}
[Snel aan de slag](quickstart/README.md)
{% endcontent-ref %}
