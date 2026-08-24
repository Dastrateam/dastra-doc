---
description: Met Dastra kunt u sterke gebruikersauthenticatie activeren
---

# Sterke authenticatie

## Introductie

Dastra gebruikt [TOTP](https://en.wikipedia.org/wiki/Time-based_Eén_Voor_Gebruikers_Wachtwoord_algoritme)-technologie om [multi-factor authenticatie](https://en.wikipedia.org/wiki/Multi-factor_authentication) te beheren.
Gebruikers kunnen inloggen met zowel hun gebruikelijke wachtwoord als een 6-cijferige code geleverd door een applicatie voor geheime opslag zoals Microsoft Authenticator of Google Authenticator (of anderen...).

## Hoe activeer ik sterke authenticatie?

* Ga naar https://app.dastra.eu/general-settings/two-factor
* Klik op "**sterke authenticatie inschakelen**".
* Download een applicatie voor 2-factor authenticatie
* Scan de **QR-code** met de toepassing die u hebt gekozen

![](<../.gitbook/assets/image (103).png>)

* Bewaar de herstelcode ergens;
* Log in met de 6-cijferige code die door je authenticatie applicatie is verstrekt.

![Voorbeeld authenticatie applicatie](<../.gitbook/assets/image (104).png>)

{% hint style="warning" %}
Bewaar de herstelcode veilig! Hiermee kun je je account herstellen als je je authenticatie applicatie kwijtraakt. Je account wordt permanent vergrendeld als je deze code niet kunt geven. U moet dan contact opnemen met de eigenaar van uw organisatie zodat zij de 2-factor authenticatie van uw account kunnen resetten.
{% endhint %}

## Hoe kan ik alle gebruikers dwingen om sterke authenticatie te gebruiken?

* Ga naar https://app.dastra.eu/general-settings/security
* Schakel het selectievakje in voor geforceerde activering van 2-factor authenticatie.

{% hint style="info" %}
Alle gebruikers die inloggen zullen geen toegang krijgen tot de applicatie zonder dat 2-factor authenticatie is geconfigureerd op hun account. Zorg ervoor dat uw team op de hoogte is van de best practices voor het opslaan van TOTP geheime sleutels.
{% endhint %}