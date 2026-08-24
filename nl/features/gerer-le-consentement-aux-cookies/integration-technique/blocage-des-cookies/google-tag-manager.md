---
description: >-
  Dastra is geïntegreerd met Google Tag Manager. Dit artikel
  legt uit hoe u het blokkeren of deblokkeren van tags kunt integreren op basis van de toestemming van de gebruiker toestemming van de gebruiker met behulp van GTM.
---

# Google Tag Manager

## Introductie

Google Tag Manager is een krachtige taggingtool die alle codeknipsels centraliseert die u in uw site wilt integreren (Dastra kan ook worden opgenomen!).
Deze tagging-oplossing is zeer effectief voor het implementeren van effectieve cookietoestemming, omdat u niet de hele website opnieuw hoeft te implementeren telkens wanneer u tags wijzigt.

## Gebeurtenissen verzonden naar GTM in de DataLayer

De volgende gebeurtenissen worden automatisch verzonden naar de Google Data Layer:


| Naam                               | Betekenis                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| dastra:consent:{your-vendor-name} | Deze gebeurtenis wordt verzonden wanneer de gebruiker cookies van deze verkoper heeft geaccepteerd.           |
| dastra:refused:{your-vendor-name} | Deze gebeurtenis wordt verstuurd wanneer de gebruiker geen toestemming heeft gegeven voor de cookies van deze verkoper |

Je kunt daarom de tags die overeenkomen met de verschillende verkopers die in de widget zijn geconfigureerd activeren met deze twee gebeurtenissen

## Voorbeeld

In dit voorbeeld gaan we de Google Optimize tag activeren na toestemming van de gebruiker.

Maak in je GTM container een trigger aan op een data layer event met de naam "dastra:consent:google-optimize".

De Google Optimize tag wordt dan alleen getriggerd op deze gebeurtenis. Zo ziet het eruit in de GTM-interface:

![](<../../../../.gitbook/assets/image (169).png>)

## Specifiek geval van blokkerende triggers

In sommige gevallen moet je bepaalde tags uitschakelen als er geen toestemming is gegeven. Omdat de "dastra:consent:\<service naam>" gebeurtenis alleen wordt uitgevoerd wanneer een pagina wordt weergegeven, kan dit in sommige gevallen niet voldoende zijn als je verschillende triggers voor pagina-interactie gebruikt, zoals klikken op pagina-elementen, scrollhoogtes, enz.

In dit geval moet je bepaalde instellingen maken om **de toestemmingswaarde die is opgeslagen in de toestemmingscookie** direct uit te lezen.

### 1. Maak een variabele "DastraConsents" aan.

#### Definieer de variabele

**Log in** bij je Google Tag Manager-account en ga naar "Variabelen". Maak vervolgens een nieuwe "Door gebruiker gedefinieerde variabele" aan.

#### Selecteer "1st party cookies

Geef uw tag bijvoorbeeld de naam "DastraConsents". Voer in het veld Cookienaam de naam van de cookie voor toestemming in (standaard: **consent-eu**).
Vergeet niet **de optie "URI-decode cookie"** te selecteren.

<figure><img src="../../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

#### Configureer je trigger dan als volgt:&#x20;

In dit geval wordt onze tag geactiveerd als de scrolldiepte op de pagina > 20% is. We willen dat deze tag alleen wordt geactiveerd als de google analytics-service is geautoriseerd door de gebruiker. Zo configureer je de tag-trigger.

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Als je in de sectie "Sommige pagina's" de tag alleen wilt activeren als het gebruik van een service is overeengekomen, voer dan de formule **DastraConsents bevat "{serviceName}":true** (bijvoorbeeld "crisp":true) zonder spaties in.

Als u de tag wilt activeren in het geval van een weigering, voert u de formule in :

**DastraConsents contains "{serviceName}":false** (bijvoorbeeld "google-analytics":false)

#### Meerdere triggers van hetzelfde type met één uitzondering

Als je een aantal verschillende triggers hebt voor dezelfde tag, kun je op deze manier ook een uitzondering maken.
Voorbeeld van een tag met meerdere triggers:&#x20;

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

In dit geval willen we een uitzondering toevoegen, als de google ads tag (google-ads) niet wordt geaccepteerd, willen we niet dat de tag wordt geactiveerd.

Klik op "Uitzondering toevoegen

{% hint style="info" %}
Merk op dat uitzonderingen alleen goed werken als ze van hetzelfde type zijn. Als je triggers van het type "Paginaweergave" zijn, moet de uitzondering ook van het type paginaweergave zijn
{% endhint %}

Maak een trigger van hetzelfde type met de naam "Pagina's bekeken met de Google Ads-service expliciet geweigerd", bijvoorbeeld &#x20;

{% hint style="info" %}
Als je de tag ook niet standaard wilt activeren, zelfs als de gebruiker niet op het toestemmingsmodal heeft geklikt (en dus geen cookies heeft om voorkeuren op te slaan). In dit geval kun je een trigger gebruiken met een negatie van het type :&#x20;

**DastraConsents Bevat geen "google-ads":true**
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

Klik op "Opslaan". Dit zou je nu moeten hebben:

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Sla je wijzigingen op en je zou moeten zien dat je tags zijn uitgeschakeld op de pagina's in kwestie als er geen toestemming is gegeven.

### Specifiek geval: vernieuw de pagina als de toestemmingsconfiguratie is gewijzigd.

#### Weigering van cookies na acceptatie:

In sommige gevallen worden bepaalde tags niet correct opgeschoond na weigering van cookies. Dit gebeurt met name wanneer een gebruiker besluit cookies te accepteren en vervolgens opnieuw op de widget klikt en besluit zijn toestemming in te trekken. In de meeste gevallen vormt dit geen probleem, omdat de markers toch niet meerdere keren in de pagina worden uitgevoerd en het dus niet meer nodig is om de scripttags die in de pagina zijn ingevoegd te verwijderen &#x20;

In bepaalde situaties is het mogelijk dat de tags nog Activa zijn.

Om dit soort problemen te voorkomen, is het mogelijk om een paginaverversing te forceren, waardoor alle javascript-tags of sdk die door de services zijn geladen, volledig worden gereset.

Voeg eenvoudig de volgende code in (indien mogelijk onder de Dastra widget initialisatie tag)

```html
<script>
// If any service is refused explicitely in the modal
window.addEventListener('dastra:consents:any_refused', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### Toestemming bijwerken :

Gebruik de functie _updated_ met de volgende code om de pagina opnieuw te laden wanneer een toestemming op een of andere manier wordt gewijzigd:&#x20;

```markup
<script>
window.addEventListener('dastra:consents:updated', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### Volledige acceptatie van trackers :

Om de pagina opnieuw te laden wanneer trackers volledig zijn geaccepteerd ("accepteer alle" knop):&#x20;

```markup
<script>
window.addEventListener('dastra:consents:all_accepted', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### &#x20;Een specifieke service accepteren :

De pagina herladen wanneer een specifieke service wordt geaccepteerd:&#x20;

```markup
<script>
window.addEventListener('dastra:consent:<slug du service>', function(){
    // Refresh the current page
    location.reload();
})
</script>
```