# TCF 1.1/2.0

{% hint style="danger" %}
**Voorlopig is deze functionaliteit nog in de experimentele fase. Elke implementatie van TCF zal niet effectief zijn**&#x20;
{% endhint %}

Het [consent management platform (CMP) framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) wordt momenteel ondersteund door de Dastra-widget. Om de opt-in voor IAB-verkopers te activeren, ga je naar het gedeelte "services" van de widgetconfiguratie en activeer je het betreffende vakje.

Zodra het vakje is aangevinkt, kun je de veranderingen zien in de interface van de widget:

![](<../../../.gitbook/assets/image (69).png>)

Automatisch, wanneer de IAB optin wordt uitgevoerd, wordt de cookie met de gecodeerde informatie over de toestemming van de gebruiker voor IAB-verkopers automatisch aangemaakt in de browser:

![](<../../../.gitbook/assets/image (71).png>)

{% hint style="info" %}
Deze cookie heeft een standaard levensduur van 180 dagen en heet "eupubconsent".
{% endhint %}

### De toestemmingsstring van IAB vastleggen

Wanneer de gebruiker toestemming geeft, is het mogelijk om de toestemmingsstring direct vast te leggen met de volgende event listener:

```javascript
document.addEventListener('dastra:consentstring',function(consentString){
    console.log(consentString); // BOybBVKOybbNhABABBENCoAAAAAq6AAA
});
```