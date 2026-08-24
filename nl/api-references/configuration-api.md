# API configureren

### API's configureren in Dastra&#x20;

API staat voor _**Application Programming Interface**_;

API's maken het mogelijk om het Dastra platform te verbinden met andere externe tools;

De mogelijkheden zijn legio: koppeling met CRM-software om stakeholders automatisch op te halen, synchronisatie van een rechtenmanagementtool met de Dastra-module, etc.

Dastra is gebaseerd op de **API-Rest** standaard en in het bijzonder op de volgende HTTP requests:&#x20;



| URI                                                                   | GET                                                                                               | POST                                                                                                                                                                                                                                           | PUT                                                                                                                                                                                                | PATCH                                                                                                                                                                                                                  | DELETE                                                                                   |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Bronnenverzameling, zoals `http://api.exemple.com/collection/`.  | Vangt_ de URI's op van de bronnen die lid zijn van de verzamelbron in de inhoud van het antwoord. | Maakt_ een lid resource in de collection resource met behulp van de instructies in de request body. De URI van de aangemaakte lid resource wordt _auto-toegewezen_ en geretourneerd in het _Location_ headerveld van het antwoord. | Vervangt_ alle representaties van de lidbronnen van de verzameling door de representatie in de verzoektekst, of _maakt_ de verzamelingbron als deze niet bestaat. | _updates_ alle representaties van de lidbronnen van de verzamelbron met behulp van de instructies in de verzoektekst, of _creëert_ de verzamelbron als deze niet bestaat. | Verwijdert alle representaties van bronnen die lid zijn van de verzamelbron. |
| Lid bron, zoals `http://api.exemple.com/collection/item3` | Haalt_ een representatie van de lidbron op in de body van het antwoord.                |Creëert_ een member resource in de member resource met behulp van de instructies in de request body. De URI van de aangemaakte member resource wordt _auto-toegewezen_ en geretourneerd in het _Location_ headerveld van het antwoord.     |Vervangt_ alle representaties van de lidbron, of _maakt_ de lidbron als deze niet bestaat, met de representatie in de verzoektekst.                               | Werkt_ alle representaties van de lidbron bij, of _maakt_ de lidbron aan als deze niet bestaat, met behulp van de instructies in de verzoektekst.                               | Verwijdert alle representaties van de lidbron.                           |

Bron : [_wikipedia_](https://en.wikipedia.org/wiki/REST);



Verschillende API's kunnen worden geconfigureerd met Dastra. De lijst met API's is hier beschikbaar: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html)

### Beperkingen&#x20;

Een http-verzoeklimiet is ingesteld op 500/min of 10000/10min.

Beveiligingsopties (met name IP-filtering) zijn niet van toepassing op API's &#x20;

### Blootstelling van aangepaste velden in de Dastra API&#x20;

In Dastra is het mogelijk om in de API [aangepaste velden](../features/generalites/champs-personnalises.md) te tonen die ontworpen zijn vanuit je Dastra-workspace.&#x20;

Aangepaste velden zijn specifiek voor elke werkruimte. Om ze mee te nemen in de Dastra API, moet je eerst de naam van hun variabele definiëren in de aangepaste velddefinitie:&#x20;

<figure><img src="../.gitbook/assets/image (276).png" alt=""><figcaption></figcaption></figure>

{% content-ref url="../features/generalites/champs-personnalises.md" %}
[champs-personnalises.md](../features/generalites/champs-personnalises.md)
{% endcontent-ref %}

De meeste entiteiten die via de API gewijzigd kunnen worden, hebben een veld met de naam "**customFields**" dat je kunt wijzigen &#x20;

Als je velden definieert met de volgende variabele namen binnen je werkruimte:&#x20;

* my\_field\_string: een "Tekst" veld
* my\_field\_booleen: een "aankruisvakje" veld
* my\_field\_numeric : een "Nummer" veld
* my\_field\_checkbox: een "Checkbox" veld

Het is mogelijk om deze informatie als volgt aan te passen

```json
{ 
  "label": "Google Analytics 4",
  ...
  "customFields": {
     "mon_champ_string": "Waarde van mijn veld",
     "mon_champ_booleen": true,
     "mon_champ_numeric": 1,
     "mon_champ_checkbox"!:["Appel", "Banaan"],
     ...a
  }
}
```

### Tags

Om tags bloot te leggen in de Dastra API, moet je ze zoeken in het tags eindpunt voordat je ze toevoegt: /v1/ws/{workspaceId}/Tags

###

{% hint style="info" %}
**TIP**: gebruik alleen API's als je weet wat je doet!
{% endhint %}



Je kunt de API beheerinterface in Dastra vinden op dit adres: [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api)





