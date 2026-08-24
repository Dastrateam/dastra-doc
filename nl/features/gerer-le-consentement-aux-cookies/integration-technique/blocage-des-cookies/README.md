---
description: In deze handleiding wordt uitgelegd hoe u cookies kunt blokkeren.
---

# Cookies blokkeren

Er zijn verschillende methoden om cookies effectief te blokkeren: cookies verwijderen, een snippet blokkeren, gepersonaliseerd javascript of Google Tag Manager.

## Cookies verwijderen

Deze methode is het snelst te implementeren, maar ook het minst betrouwbaar. Als je in het configuratiescherm van de Dastra widget de naam van de cookies invoert die aan elke service zijn gekoppeld, worden de betreffende cookies automatisch verwijderd telkens wanneer de pagina wordt weergegeven. &#x20;

![](<../../../../.gitbook/assets/image (85).png>)

Dit kan in sommige gevallen effectief zijn, maar het riskeert de betrouwbaarheid van de gebruikte gereedschappen van derden (webanalyse gereedschappen in het bijzonder) aanzienlijk te verstoren. Het is vaak beter om een van de andere onderstaande methoden te gebruiken.

## Een codefragment in de pagina blokkeren

Met deze methode kun je een stukje trackingcode op de pagina volledig uitschakelen.

Vervang hiervoor het volgende codefragment in de html-code van je pagina:

```markup
<script >
  alert("hallo, ik ben een tracking javascript tag");
</script>
```

Van :

```markup
<script data-consent="{uw-service-slug}" type="dastra/script">
   alert("hallo, ik ben een tracking javascript tag");
</script>
```

Vervang de "{your-service-slug}" door de service-identifier die je hebt ingevoerd bij het configureren van je widget:

![](<../../....//.gitbook/assets/image (86).png>)

Als de client de cookies geaccepteerd heeft, zal de inhoud van het script automatisch uitgevoerd worden.

{% hint style="info" %}
Dit kan een aantal neveneffecten hebben, waaronder problemen met het markeren van de synthaxis in de meeste IDE's &#x20;

Het scriptfragment wordt helemaal niet uitgevoerd in het geval van een implementatiefout van een Dastra-widget.
{% endhint %}

### Blokkeren in puur javascript

In pure javascript kun je gebeurtenissen gebruiken die op het venster worden getriggerd om toestemming te verzamelen en specifiek gedrag te beheren, afhankelijk van of cookies worden geaccepteerd of geweigerd. Dit geeft je meer flexibiliteit:

```javascript
<script>
  (functie(){

      /* 
      * Trigger een aangepaste servicetag met verwachte cookies
      */
      functie customTagsTrigger () {
        /* Als de leverancier een specifieke functie biedt om de service cookie-loos te laten werken, haal die dan hierheen.
        * Anders kopieer je het standaardcodefragment dat wordt geleverd door de tagverkopers*/
      }

      /*
      * Behandel het toestemmingsgebeurtenis met globale reikwijdte
      * Als de gebruiker toestemming heeft gegeven voor de tag-cookies van de aangepaste leverancier, wordt deze gebeurtenis geactiveerd bij elke pagina waarop de cookie-toestemmingswidget is geïnstalleerd.
      */
      window.addEventListener('dastra:consent:{uw-service-slug}', functie () {
        /* De klant geeft hier toestemming voor de cookies van de aangepaste leverancier */
        customTagsTrigger();
        console.log('{uw-service-slug} geaccepteerd')
      });

      /* Vink dit aan als je de geweigerde gebeurtenis wilt afhandelen
      * Behandel geweigerde gebeurtenis met globale reikwijdte (optioneel) 
      */
        window.addEventListener('dastra:geweigerd:{uw-service-slug}', functie () {
         // De cookies van de aangepaste services worden geweigerd 
         console.log('{uw-service-slug} cookies geweigerd')
       });
      
  });
  </script>
```

### Google Tag Manager

Zie volgende pagina:

{% content-ref url="google-tag-manager.md" %}
[google-tag-manager.md](google-tag-manager.md)
{% endcontent-ref %}

### Herinnering aan levenscyclus van toestemming:&#x20;

<figure><img src="../../../../.gitbook/assets/cookies-lifecycle.drawio.png" alt=""><figcaption><p>Cookie widget levenscyclus</p></figcaption></figure>

### Javascript gebeurtenissen

Standaard verzendt de widget verschillende gebeurtenissen op het vensterelement van de pagina:&#x20;

| Naam gebeurtenis | Opmerkingen |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Triggered wanneer de service is geaccepteerd door de gebruiker (noodzakelijke cookies worden niet beïnvloed). Als de service in de standaard toestemmingsmodus staat, wordt deze gebeurtenis geactiveerd wanneer de pagina voor het eerst wordt geladen.
| dastra:refused:ß<slug du service> | Wordt geactiveerd als de service niet is geactiveerd door de gebruiker (standaard als er geen toestemming is gegeven) of als deze expliciet is geweigerd.
| dastra:consents:ready | Wordt geactiveerd als de cookie voor toestemming (consent-eu) is gelezen en gedecodeerd. |
| dastra:consents:updated | Triggers als toestemmingen zijn bijgewerkt door de gebruiker (geaccepteerd, geweigerd of ingesteld) |
| dastra:consents:any_refused | Treedt op als ten minste één cookie expliciet door de gebruiker is geweigerd via het modale venster.
| dastra:consents:all_accepted | Triggers als alle diensten door de gebruiker zijn geaccepteerd via het modale venster |