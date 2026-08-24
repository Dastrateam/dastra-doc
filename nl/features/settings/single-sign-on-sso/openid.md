---
description: Een SSO-verbinding configureren met het OpenId-protocol
---

# OpenId

## Hoe het werkt

De OpenId specificatie kan [hier](https://openid.net/connect/) gevonden worden.

![](<../../../.gitbook/assets/image (119).png>)


Er zijn drie stappen voor het configureren van SSO met OpenID&#x20;

* Configureren van de authenticatie provider: Active Directory, Google Workspace, etc.
* Configuratie van de serviceprovider: Dastra
* Authenticatietests

## 1. de authenticatieprovider configureren

U moet een OpenId-configuratie instellen in uw authenticatieprovider.

Voor active directory: [https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc](https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc)

Om lokale accounts (die gehost worden in Dastra) te reconciliëren, moet je een eigenschap opgeven die het e-mailadres van de gebruiker bevat (standaard zoekt Dastra naar de eigenschap met de naam [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Hier is de informatie die u nodig hebt om de serviceprovider te configureren:&#x20;

* **Autoriteit/domein (ex: https://account.oauth.sso.com)**
* Client-ID: ClientId**&#x20;
* **Geheim sleutel**
* **Response Type, standaard id_token**
* Scope: standaard is "openid profile email"**.

Om uw authenticatieprovider te configureren, hebt u de volgende informatie nodig:

* **De opgegeven Redirect URI in dit formaat: https://account.dastra.eu/signin-{schemeId}**

## 2. De serviceprovider configureren

Ga in dastra.eu naar de [SSO administratiepagina](https://app.dastra.eu/general-settings/sso) en klik op "voeg een SSO login toe".

![](<../../../.gitbook/assets/image (116).png>)

Vul de formuliervelden in met de informatie uit de entiteitconfiguratie:

![](<../../../.gitbook/assets/image (123).png>)

{% hint style="danger" %}
Het is mogelijk om alle gebruikers van het abonnementsaccount te dwingen om een bepaalde SSO te gebruiken (door het vakje "dwingen gebruikers om deze SSO te gebruiken" aan te vinken). Wees voorzichtig voordat je deze optie activeert. Als de SSO mislukt, hebt u geen toegang meer tot uw account als beheerder. Het is beter om SSO per gebruiker te beheren.
{% endhint %}

{% hint style="warning" %}
**Speciale gevallen voor externe gebruikers**
Alleen accounts die intern zijn aan een abonnement worden onderworpen aan SSO. De accounts van externe gebruikers (die een ander aanvullend abonnement hebben) worden niet onderworpen aan SSO.
{% endhint %}

## 3. SSO testen met OpenId

Zodra de configuratie voltooid is, kunt u de authenticatie testen door op de testknop rechtsonder te klikken. Als u problemen ondervindt bij het configureren van SSO, neem dan contact op met support door de [support ticket management](https://app.dastra.eu/general-settings/support) pagina te bezoeken.

![](<../../../.gitbook/assets/image (122).png>)
