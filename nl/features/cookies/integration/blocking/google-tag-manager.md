---
description: >-
  Dastra is standaard geïntegreerd met Google Tag Manager. Dit artikel legt uit
  hoe u met GTM tags blokkeert of deblokkeert op basis van de toestemming van de
  gebruiker.
---

# Google Tag Manager

## Inleiding

Google Tag Manager is een taggingtool die alle codefragmenten centraliseert die u in uw website wilt opnemen (Dastra kan er een van zijn).\
Deze taggingoplossing is zeer geschikt om cookietoestemming effectief te implementeren, omdat u niet telkens de hele website opnieuw hoeft te implementeren wanneer tags worden gewijzigd.

## Google Consent Mode V2

Dastra ondersteunt **Google Consent Mode V2** standaard. De vereisten, de activering voor een dienst en het standaard toestemmingsfragment worden beschreven op een aparte pagina:

{% content-ref url="google-consent-mode.md" %}
[Google Consent Mode V2](google-consent-mode.md)
{% endcontent-ref %}

## Gebeurtenissen die naar GTM worden gestuurd in de dataLayer

De volgende gebeurtenissen worden automatisch naar de dataLayer van Google gestuurd:

| Naam | Betekenis |
| --- | --- |
| `dastra:consent:{your-vendor-name}` | Deze gebeurtenis wordt gestuurd wanneer de gebruiker de cookies van deze aanbieder heeft geaccepteerd. |
| `dastra:refused:{your-vendor-name}` | Deze gebeurtenis wordt geactiveerd wanneer de gebruiker geen toestemming heeft gegeven voor de cookies van deze aanbieder. |

Met deze twee gebeurtenissen activeert u dus de tags die bij de verschillende in de widget geconfigureerde aanbieders horen.

## Voorbeeld

In dit voorbeeld activeren we de conversietag van Google Ads wanneer de bezoeker toestemming geeft voor de dienst Google Ads.

1. Maak in uw GTM-container een trigger van het type **Custom Event** met de gebeurtenisnaam `dastra:consent:google-ads`.
2. Koppel deze trigger aan uw conversietag van Google Ads.

De tag wordt dan alleen bij deze gebeurtenis geactiveerd.

## Specifiek geval: blokkeringstriggers

In sommige gevallen moet u bepaalde tags uitschakelen als er geen toestemming is gegeven. Omdat de gebeurtenis `dastra:consent:<service name>` alleen wordt uitgevoerd wanneer een pagina wordt weergegeven, volstaat dit soms niet als u op de pagina andere interactietriggers gebruikt, zoals klikken op pagina-elementen of scrolldiepte.

In dat geval moet u bepaalde instellingen configureren om **de toestemmingswaarde die in de toestemmingscookie is opgeslagen** rechtstreeks uit te lezen.

{% hint style="info" %}
Deze methode werkt alleen met cookieopslag: ze is niet geschikt als de optie **LocalStorage inschakelen voor cookies op basis van toestemming** is ingeschakeld. Hebt u in **Naam van de cookie voor de opslag van toestemming (standaard 'consent-eu')** een eigen cookienaam ingesteld, gebruik die dan in de variabele.
{% endhint %}

### 1. Een variabele DastraConsents aanmaken

#### De variabele definiëren

Meld u aan bij uw Google Tag Manager-account, ga naar "Variables" en maak een nieuwe "User-defined variable" aan.

#### "1st party cookies" selecteren

Geef uw variabele bijvoorbeeld de naam "DastraConsents". Voer in het veld voor de cookienaam de naam van de toestemmingscookie in (standaard: `consent-eu`).\
Vergeet niet de optie **"URI-decode cookie"** te selecteren.

<figure><img src="../../../../.gitbook/assets/cookies-gtm-variable-consent-cookie.png" alt="De variabele DastraConsents van het type 1st party cookie in Google Tag Manager, met de cookienaam consent-eu"><figcaption><p>De variabele die de toestemmingscookie leest</p></figcaption></figure>

#### Configureer daarna uw trigger als volgt

In dit voorbeeld wordt onze tag geactiveerd als de scrolldiepte op de pagina groter is dan 20%. We willen dat deze tag alleen wordt geactiveerd als de gebruiker de dienst Google Analytics heeft toegestaan. Zo configureert u de trigger van de tag.

<figure><img src="../../../../.gitbook/assets/cookies-gtm-trigger-scroll-depth.png" alt="Een scrolldieptetrigger met de voorwaarde op de variabele DastraConsents"><figcaption><p>De scrolldieptetrigger met een voorwaarde op de toestemming</p></figcaption></figure>

Voer in de sectie "Some Pages" de volgende formule zonder spaties in als u de tag alleen wilt activeren wanneer toestemming voor een dienst is gegeven: `DastraConsents contains "{serviceName}":true` (voorbeeld `"crisp":true`).

Wilt u de tag activeren bij een weigering, voer dan deze formule in:

`DastraConsents contains "{serviceName}":false` (voorbeeld `"google-analytics":false`)

### Meerdere triggers van hetzelfde type met een uitzondering

Hebt u veel verschillende triggers voor dezelfde tag, dan kunt u op deze manier ook een uitzondering maken.\
Voorbeeld van een tag met meerdere triggers:

<figure><img src="../../../../.gitbook/assets/cookies-gtm-tag-google-ads-conversion.png" alt="Een conversietag van Google Ads met meerdere triggers"><figcaption><p>Een tag met meerdere triggers</p></figcaption></figure>

In dit geval willen we een uitzondering toevoegen: als de tag van Google Ads (google-ads) niet is geaccepteerd, willen we niet dat de tag wordt geactiveerd.

Klik op "Add Exception".

{% hint style="info" %}
Uitzonderingen werken alleen goed als ze van hetzelfde type zijn. Zijn uw triggers van het type "Page view", dan moet de uitzondering ook van het type "Page view" zijn.
{% endhint %}

Maak een trigger van hetzelfde type met een naam als "Pages viewed with Google Ads service explicitly refused".

{% hint style="info" %}
Wilt u de standaardtag ook uitschakelen als de gebruiker niet op het toestemmingsvenster heeft geklikt (en dus geen cookies met voorkeuren heeft), gebruik dan een trigger met een ontkenning zoals:

`DastraConsents Does not contain "google-ads":true`
{% endhint %}

<figure><img src="../../../../.gitbook/assets/cookies-gtm-trigger-google-ads-refused.png" alt="Een uitzonderingstrigger voor paginaweergaven waarbij de dienst Google Ads uitdrukkelijk is geweigerd"><figcaption><p>De uitzonderingstrigger</p></figcaption></figure>

Klik op "Save". U zou nu dit moeten hebben:

<figure><img src="../../../../.gitbook/assets/cookies-gtm-tag-ads-triggering.png" alt="De conversietag van Google Ads met zijn triggers en de uitzondering"><figcaption><p>De tag met zijn triggers en uitzondering</p></figcaption></figure>

Sla uw wijzigingen op: de tags zijn dan uitgeschakeld op de betreffende pagina's als er geen toestemming is gegeven.

### Specifiek geval: de pagina vernieuwen als de toestemmingsconfiguratie wijzigt

{% hint style="warning" %}
De gebeurtenissen `dastra:consents:*` en `dastra:consent:<slug>` worden ook bij elke paginalading afgevuurd, wanneer de widget de reeds opgeslagen keuzes toepast. Een `location.reload()` die rechtstreeks aan deze gebeurtenissen is gekoppeld, laadt de pagina in een lus opnieuw. Registreer de listener daarom altijd binnen `dastra:consents:ready`, zoals in de onderstaande voorbeelden: alleen de keuzes van de bezoeker veroorzaken dan het herladen.
{% endhint %}

#### Weigering van cookies na acceptatie

In sommige gevallen worden bepaalde tags niet goed opgeschoond nadat cookies zijn geweigerd. Dat gebeurt vooral wanneer een gebruiker eerst cookies accepteert, daarna opnieuw op de widget klikt en zijn toestemming intrekt. Meestal geeft dit geen probleem, omdat de tags toch niet meerdere keren op de pagina worden uitgevoerd en het dus niet meer nodig is de in de pagina ingevoegde scripttags te verwijderen.

In sommige situaties kunnen de tags echter nog actief zijn.

Om dit soort problemen te voorkomen, kunt u een vernieuwing van de pagina afdwingen. Daarmee worden alle tags of JavaScript-SDK's die de diensten hebben geladen volledig opnieuw ingesteld.

Voeg de volgende code in (indien mogelijk onder de initialisatietag van de Dastra-widget):

```markup
<script>
// If any service is refused explicitely in the modal
// Consent events also fire on every page load: listen only once the widget is ready
window.addEventListener('dastra:consents:ready', function(){
    window.addEventListener('dastra:consents:any_refused', function(){
        // Refresh the current page
        location.reload();
    })
})
</script>
```

#### Toestemmingsupdate

Om de pagina opnieuw te laden wanneer een toestemming op welke manier dan ook verandert, gebruikt u de gebeurtenis `updated` met de volgende code:

```markup
<script>
// Consent events also fire on every page load: listen only once the widget is ready
window.addEventListener('dastra:consents:ready', function(){
    window.addEventListener('dastra:consents:updated', function(){
        // Refresh the current page
        location.reload();
    })
})
</script>
```

#### Volledige acceptatie van de trackers

Om de pagina opnieuw te laden wanneer alle trackers zijn geaccepteerd (knop "alles accepteren"):

```markup
<script>
// Consent events also fire on every page load: listen only once the widget is ready
window.addEventListener('dastra:consents:ready', function(){
    window.addEventListener('dastra:consents:all_accepted', function(){
        // Refresh the current page
        location.reload();
    })
})
</script>
```

#### Acceptatie van een specifieke dienst

Om de pagina opnieuw te laden wanneer een specifieke dienst wordt geaccepteerd:

```markup
<script>
// Consent events also fire on every page load: listen only once the widget is ready
window.addEventListener('dastra:consents:ready', function(){
    window.addEventListener('dastra:consent:<service-slug>', function(){
        // Refresh the current page
        location.reload();
    })
})
</script>
```
