---
description: >-
  Beheer de privacyconformiteit voor uw Amerikaanse gebruikers (CCPA/CPRA, GPC, DoNotTrack) met de cookietoestemmingswidget van Dastra.
---

# US Privacy: CCPA, GPC en DoNotTrack

## Regelgevend kader

Anders dan de AVG, die opt-in (voorafgaande toestemming) vereist, berust de Amerikaanse privacywetgeving vooral op een opt-out-model: trackers mogen standaard worden geplaatst, maar gebruikers moeten er bezwaar tegen kunnen maken.

De belangrijkste regelgeving:

| Wet | Staat | Model | Van kracht sinds |
| --- | --- | --- | --- |
| CCPA / CPRA | Californië | Opt-out | 2020 / 2023 |
| CPA | Colorado | Opt-out | 2023 |
| VCDPA | Virginia | Opt-out | 2023 |
| CTDPA | Connecticut | Opt-out | 2023 |

{% hint style="info" %}
GPC is verplicht in Californië

Sinds de CPRA (2023) moeten bedrijven het signaal Global Privacy Control (GPC) respecteren als een opt-outverzoek voor de verkoop en het delen van persoonsgegevens.
{% endhint %}

---

## Aanbevolen aanpak met Dastra

### 1. Een geogerichte variant voor de Verenigde Staten aanmaken

Het snelst behandelt u uw Amerikaanse gebruikers door een geogerichte variant aan te maken in het keuzemenu voor varianten rechtsboven in uw bannereditor (zie [Geogerichte varianten](geo-targeting.md)).

Configureer voor Californië (CCPA/CPRA) de variant met een opt-outmodel: niet-essentiële cookies zijn standaard actief en gebruikers kunnen zich afmelden. Overweeg ook een link "Do Not Sell or Share My Personal Information" in de voettekst van uw site, die de widget rechtstreeks opent.

Voor andere Amerikaanse staten zonder bannerverplichting schakelt u de optie **Schakel de bannerweergave uit (alle cookies met standaardtoestemming worden geactiveerd)** in, met standaardtoestemmingen volgens uw beleid.

{% content-ref url="geo-targeting.md" %}
[Geogerichte varianten](geo-targeting.md)
{% endcontent-ref %}

---

### 2. De signalen GPC en DoNotTrack respecteren

Twee browsersignalen laten een gebruiker weigeren gevolgd te worden zonder met een banner te werken:

| Signaal | Standaard | Juridisch bindend (CA) | Beschrijving |
| --- | --- | --- | --- |
| GPC (`globalPrivacyControl`) | W3C | Ja (CPRA) | Opt-outsignaal voor de verkoop of het delen van persoonsgegevens |
| DNT (`doNotTrack`) | W3C | Nee | Voorkeurssignaal "niet volgen" (juridisch niet afdwingbaar) |

#### Native activering (aanbevolen)

Dastra ondersteunt deze signalen nu native via een schakelaar in de configuratie van de widget. Schakel de optie **Activeer de Global Privacy Control (GPC)** in bij **Configuratie** van de widget.

<figure><img src="../../../.gitbook/assets/cookie-widget-gpc-toggle.png" alt="Schakelaar Activeer de Global Privacy Control (GPC) in de geavanceerde instellingen van de widget"><figcaption><p>De GPC-optie in de geavanceerde instellingen van de cookietoestemmingswidget</p></figcaption></figure>

Is deze optie ingeschakeld en heeft de bezoeker nog geen keuze gemaakt, dan weigert de widget automatisch elke cookiecategorie behalve de noodzakelijke cookies (voorkeuren, analytisch, marketing, overige en niet-geclassificeerde) zodra de browser een GPC- of DoNotTrack-signaal verstuurt, zonder extra code. De banner wordt voor deze bezoeker niet getoond.

Dezelfde schakelaar bestaat in elke **Variatie van geografische doelen**: schakel hem in op de variatie die Californië dekt.

{% hint style="info" %}
Native activering is beschikbaar vanaf de huidige versie van de Dastra-widget. Ze dekt zowel het signaal `globalPrivacyControl` als `doNotTrack`.
{% endhint %}

#### Geavanceerde optie: eigen JS-fragment

Hebt u meer controle nodig (bijvoorbeeld om een bevestigingsbericht te tonen of de opt-out op bepaalde categorieën toe te passen), gebruik dan het volgende JS-fragment naast de native schakelaar, of in plaats ervan als u de widget via de JS-API beheert:

```html
<script>
  var isOptOut =
    navigator.globalPrivacyControl === true ||
    navigator.doNotTrack === '1' ||
    window.doNotTrack === '1'

  if (isOptOut) {
    window.dastra = window.dastra || []
    window.dastra.push([
      'cookieReady',
      function (manager) {
        if (!manager.consent.hasConsented()) {
          manager.consent.setPurposeConsent('Analytical', false)
          manager.consent.setPurposeConsent('Marketing', false)
          manager.consent.dispatchEvents() // apply choices without persisting them
        }
      }
    ])
  }
</script>
```

{% hint style="info" %}
`dispatchEvents()` of `save()`: wat is het verschil?

* `dispatchEvents()` past de toestemmingskeuzes toe voor de huidige sessie, zonder iets in de opslag van de toestemming te schrijven (standaard de cookie `consent-eu`, of localStorage als die optie is ingeschakeld). Het GPC- of DNT-signaal wordt bij elke paginalading opnieuw beoordeeld. Schakelt de gebruiker GPC later uit in zijn browser, dan wordt automatisch het normale gedrag hervat. Dit is de aanbevolen aanpak om deze signalen te respecteren.
* `save()` bewaart de toestemming in die opslag, alsof de gebruiker via de widget een expliciete keuze had gemaakt. Gebruik dit alleen als u een keuze over sessies heen wilt onthouden.
{% endhint %}

{% hint style="info" %}
Wat doet `hasConsented()`?

Deze controle zorgt dat de automatische opt-out een keuze die de gebruiker al expliciet via de widget heeft gemaakt, niet overschrijft. Heeft de gebruiker al een voorkeur uitgedrukt, dan wordt die gerespecteerd.
{% endhint %}

{% hint style="warning" %}
Plaats dit fragment vóór de laadtag van de Dastra-widget, zodat het al bij de allereerste paginalading wordt meegenomen.
{% endhint %}

Categorielabels voor `setPurposeConsent`:

| Categorie | Label |
| --- | --- |
| Noodzakelijk | `Necessary` |
| Voorkeuren | `Preference` |
| Analytisch | `Analytical` |
| Marketing | `Marketing` |
| Andere | `Other` |
| Niet geclassificeerd | `Unclassified` |

### 3. Een bevestigingsbericht "Opt-Out Request Honored" tonen

Wordt een GPC- of DNT-signaal gedetecteerd, dan raadt regelgeving zoals de CPRA aan de gebruiker te informeren dat zijn opt-outverzoek is gehonoreerd.

Bij native activering toont de widget dit bericht gedurende 6 seconden in plaats van de banner. De standaardtekst is: "Globale privacycontrole gedetecteerd: analytische en marketingcookies zijn uitgeschakeld." Om die te wijzigen opent u op de banner **Teksten en vertalingen**, onderdeel **Startpagina**, en past u het veld **Bericht weergegeven wanneer de browser een signaal voor globale privacycontrole of niet volgen verzendt** aan.

De widget stuurt ook de gebeurtenis `dastra:gpc:applied` naar `window`, waarnaar u kunt luisteren voor uw eigen verwerking.

Gebruikt u geen native activering, of wilt u een andere weergave, dan zijn er twee aanpakken met een JS-fragment.

#### Optie A: tijdelijke melding

Een bericht dat enkele seconden verschijnt en daarna vanzelf verdwijnt. Het vraagt weinig implementatie, maar de gebruiker kan het missen als hij op dat moment niet naar de pagina kijkt.

```html
<script>
var isOptOut = navigator.globalPrivacyControl === true
            || navigator.doNotTrack === "1"
            || window.doNotTrack === "1";

if (isOptOut) {
  window.dastra = window.dastra || [];
  window.dastra.push(['cookieReady', function(manager) {
    if (!manager.consent.hasConsented()) {
      manager.consent.setPurposeConsent('Analytical', false);
      manager.consent.setPurposeConsent('Marketing', false);
      manager.consent.dispatchEvents();

      var notice = document.createElement('div');
      notice.setAttribute('role', 'status');
      notice.style.cssText = 'position:fixed;bottom:16px;left:16px;background:#222;color:#fff;padding:12px 18px;border-radius:6px;font-size:14px;z-index:9999;max-width:320px;';
      notice.textContent = 'Opt-Out Request Honored: analytics and marketing cookies have been disabled.';
      document.body.appendChild(notice);
      setTimeout(function() { notice.remove(); }, 6000);
    }
  }]);
}
</script>
```

#### Optie B: permanente balk

Een vaste balk onderaan de pagina, zichtbaar zolang GPC in de browser actief is. Dit is beter voor de conformiteit: de melding is permanent en blijft ook na de eerste lading zichtbaar. Met een knop Dismiss kan de gebruiker de balk sluiten.

```html
<script>
var isOptOut = navigator.globalPrivacyControl === true
            || navigator.doNotTrack === "1"
            || window.doNotTrack === "1";

if (isOptOut) {
  window.dastra = window.dastra || [];
  window.dastra.push(['cookieReady', function(manager) {
    if (!manager.consent.hasConsented()) {
      manager.consent.setPurposeConsent('Analytical', false);
      manager.consent.setPurposeConsent('Marketing', false);
      manager.consent.dispatchEvents();

      var bar = document.createElement('div');
      bar.setAttribute('role', 'status');
      bar.setAttribute('aria-live', 'polite');
      bar.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:#1a1a1a;color:#fff;font-size:13px;padding:10px 20px;display:flex;align-items:center;justify-content:space-between;z-index:9999;border-top:1px solid #333';
      bar.innerHTML = '<span>🔒 Opt-Out Request Honored, analytics and marketing cookies are disabled.</span>'
        + '<button onclick="this.parentNode.remove()" style="background:none;border:1px solid #555;color:#fff;padding:4px 12px;border-radius:4px;cursor:pointer;font-size:12px;margin-left:16px">Dismiss</button>';
      document.body.appendChild(bar);
    }
  }]);
}
</script>
```

{% hint style="info" %}
Pas de tekst van het bericht aan uw redactionele stijl en aan de taal van uw gebruikers aan. Bij meertalige sites bepaalt u de tekst voorwaardelijk op basis van de taal van de pagina.
{% endhint %}

***

## Samenvatting

| Mechanisme | Implementatie | Wettelijk verplicht (CA) |
| --- | --- | --- |
| Geogerichte CCPA-variant | Dastra-interface | Ja |
| GPC-detectie | Native schakelaar (widgetconfiguratie), aanbevolen | Ja (CPRA) |
| DNT-detectie | Native schakelaar (widgetconfiguratie), aanbevolen | Nee, aanbevolen |
| Bevestigingsbericht | Native (bewerkbare tekst) of JS-fragment | Nee, aanbevolen |
