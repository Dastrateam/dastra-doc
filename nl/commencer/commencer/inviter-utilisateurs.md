---
description: Ontdek hoe het Dastra-uitnodigingssysteem werkt.
---

# Gebruikers uitnodigen

## Een gebruiker uitnodigen

U kunt iemand uitnodigen om samen te werken aan uw werkruimten door hem uit te nodigen voor de organisatie waartoe de werkruimte behoort &#x20;

Je kunt gebruikers uitnodigen voor je werkruimte door te klikken op de knop "instellingen" linksonder in het scherm, vervolgens op "toegangsbeheer / gebruikers" en ten slotte op "een gebruiker uitnodigen":

<figure><img src="../../.gitbook/assets/image (12) (2) (2).png" alt=""><figcaption></figcaption></figure>



Voer het e-mailadres in van de persoon die je wilt uitnodigen voor jouw Dastra ruimte. Als dit adres nog niet is gekoppeld aan de organisatie, klik er dan op om hem of haar een uitnodigingslink te sturen.


Een formulier verschijnt. Voer je achternaam, voornaam, rol en team in en klik dan op de "Stuur een uitnodiging" knop. De uitgenodigde persoon zal een e-mail ontvangen met een link die, eenmaal geklikt, deze persoon toegang geeft tot de ruimte.
\
Dat is het, de gebruiker is uitgenodigd!

### Huidige uitnodigingen bekijken

Je kunt de huidige uitnodigingen controleren in de werkruimte-instellingen in de sectie "Gebruikers".&#x20;

<figure><img src="../../.gitbook/assets/image (12) (3).png" alt=""><figcaption></figcaption></figure>

### Een uitnodigingslink opnieuw versturen

Als de uitgenodigde gebruiker niet op de uitnodigingslink heeft geklikt en de link is verlopen (na 10 dagen), kun je de uitnodigingslink opnieuw verzenden door op de knop "Uitnodiging opnieuw verzenden" te klikken.&#x20;

<figure><img src="../../.gitbook/assets/image (16) (2).png" alt=""><figcaption></figcaption></figure>

### Teams maken en toewijzen

In Dastra worden gebruikers gegroepeerd in teams, die op hun beurt worden toegewezen aan rechtspersonen of afdelingen. Op deze manier kunnen rollen en verantwoordelijkheden nauwkeurig worden beheerd.

{% hint style="info" %}
Er zijn verschillende standaardrollen in Dastra, die verschillende autorisatieniveaus vertegenwoordigen:

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **: Zij kunnen alles doen wat auteurs kunnen doen, maar ook organisatie- en ruimte-instellingen wijzigen.
*Bijdrager**: Zij kunnen ruimtes lezen en bewerken. Ze kunnen concepten en wijzigingen zien die nog niet gepubliceerd zijn. Ze kunnen wijzigingen publiceren. Ze kunnen geen organisatie- of ruimteparameters wijzigen.
* Lezer**: kan alleen gepubliceerde ruimtes in de organisatie bezoeken. Ze kunnen niet bewerken en geen wijzigingen zien die nog niet gepubliceerd zijn.
{% endhint %}

## Een grote lijst met gebruikers importeren

Je kunt het importeren van een grote lijst gebruikers in het platform aanvragen. Om dit te doen moet je de Dastra teams &#x20;

**De te volgen stappen:**&#x20;

* ga naar deze link: [https://app.dastra.eu/general-settings/users](https://app.dastra.eu/general-settings/users)
* klik op de knop "contact opnemen met het Dastra-team

<figure><img src="../../.gitbook/assets/image (1) (1) (4) (1).png" alt=""><figcaption></figcaption></figure>

* Maak een bestand per werkruimte in CSV-formaat met de volgende kolommen, gescheiden door , (komma):&#x20;

Verplicht: &#x20;

* E-mail (e-mailadres van de gebruiker)
* Voornaam (voornaam van de gebruiker)
* FamilyName (achternaam gebruiker)

Optioneel: &#x20;

* Rollen (gescheiden door |) > dit komt overeen met de rollen in Dastra
* Teams (gescheiden door |) > dit komt overeen met de teams in Dastra
* SsoConfigurationId > dit komt overeen met de SSO login identifier indien van toepassing.

Hier is een voorbeeldbestand om te downloaden en in te vullen:&#x20;

{% file src="../../.gitbook/assets/Template_import_users (1).csv" %}
Sjabloon importbestand
{% endfile %}

**Voor rolidentificaties:**&#x20;

Standaard: de basisrollen hebben de volgende identifiers:&#x20;

* Beheerder = 1
* Medewerker = 2
* Lezer = 3

Voor aangepaste rollen die u hebt gemaakt, is de identifier zichtbaar in de ontwikkelconsole van uw browser via de netwerktab &#x20;

{% hint style="info" %}
Gebruik de volgende sneltoets om de console in Chrome te openen: Cmd + Option + C (op Mac) of Ctrl + Shift + J (op Windows).

Als u de console in Firefox wilt openen, gebruikt u de volgende sneltoets: Cmd + Option + K (op Mac) of Ctrl + Shift + J (onder Windows).

Gebruik de volgende sneltoets om de console te openen Cmd + Optie + C

Als je de console wilt openen in Microsoft Edge, gebruik je de volgende sneltoets: Ctrl + Shift + I
{% endhint %}

Houd er rekening mee dat de rollen vooraf moeten worden aangemaakt.



<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption><p>Hier is de rol identifier nummer 115</p></figcaption></figure>



**Team ID's:**&#x20;

Deze kunnen worden ingesteld bij het toevoegen van een team

<figure><img src="../../.gitbook/assets/image (4) (2) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Houd er rekening mee dat teams eerst moeten worden gemaakt in de werkruimte.
{% endhint %}

Sla je bestand op in CSV UTF 8&#x20 formaat;

<figure><img src="../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

Als je bestand klaar is, vertel je ons in welke workspace je de gebruikers wilt importeren en upload je het bestand via de upload interface:&#x20;



<figure><img src="../../.gitbook/assets/image (2) (3) (1).png" alt=""><figcaption></figcaption></figure>

We zullen het verzoek ontvangen en contact met je opnemen voor een vervolg.