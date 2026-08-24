---
description: SAML 2 configuratiedetails
---

# SAML 2

Er zijn drie stappen voor het configureren van SSO met SAML 2&#x20;

* Configureren van de authenticatie provider (**Identity Provider - IdP**) : Active Directory, Google Workspace...
* Configuratie van de dienstverlener (**Service Provider - SP**): Dastra
* Authenticatietests

In het specifieke geval **van ADFS-servers**, raadpleeg onze specifieke documentatie:&#x20;

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## 1. authenticatie provider configuratie

U moet een SAML-configuratie instellen in uw authenticatieprovider.

Voor AD FS: [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings)

Voor Azure AD: [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad)

Voor Google: [https://support.google.com/a/answer/6087519?hl=fr](https://support.google.com/a/answer/6087519?hl=fr)

Om lokale accounts (die gehost worden in Dastra) te reconciliëren, moet je een eigenschap opgeven die het e-mailadres van de gebruiker bevat (standaard zoekt Dastra naar de eigenschap met de naam [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Hier is de informatie die u nodig hebt om de serviceprovider te configureren:&#x20;

* **Identity Provider's Entity id** (uitgever)
* **Single sign on url** (uitgever)
* Het certificaat in **RAW-formaat** (base64-gecodeerd)

Om je authenticatie provider te configureren, heb je de volgende informatie nodig:

* **Issuer**: standaard "https://www.dastra.eu".
* **SP Redirect URI**: standaard [https://account.dastra.eu/Saml2/Acs](https://localhost:44375/Saml2/Acs)

## 2. Configuratie serviceprovider

Ga in dastra.eu naar de SSO-administratiepagina (https://app.dastra.eu/general-settings/sso) en klik op "add an SSO login".

![](<../../..gitbook/assets/image (116).png>)

Vul de formuliervelden in met de informatie uit de entiteitconfiguratie:

![](<../../../.gitbook/assets/image (117).png>)

{% hint style="danger" %}
Het is mogelijk om alle gebruikers van het abonnementenaccount te dwingen om een bepaalde SSO te gebruiken (door het vakje "Force users to use this SSO" aan te vinken). Wees voorzichtig voordat je deze optie activeert. Als de SSO mislukt, hebt u geen toegang meer tot uw account als beheerder. Het is beter om SSO per gebruiker te beheren.
{% endhint %}

{% hint style="warning" %}
**Speciale gevallen voor externe gebruikers**

Alleen accounts die intern zijn aan een abonnement worden onderworpen aan SSO. De accounts van externe gebruikers (die een ander aanvullend abonnement hebben) worden niet onderworpen aan SSO.
{% endhint %}

## 3. SSO testen

Zodra de configuratie is voltooid, kunt u de verificatie testen door op de testknop rechtsonder te klikken. Als u problemen ondervindt bij het configureren van SSO, neem dan contact op met support via de pagina [support ticket management](https://app.dastra.eu/general-settings/support).

![](<../../../.gitbook/assets/image (121).png>)
