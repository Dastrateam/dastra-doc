---
description: >-
  Deze pagina legt uit hoe u de SSO van Dastra instelt met Microsoft Entra ID
  (Active Directory) via het SAML 2-protocol.
---

# Active Directory (Microsoft Entra ID)

## De toepassing configureren in Microsoft Entra ID

* Ga naar het Microsoft Entra-beheercentrum: [https://entra.microsoft.com](https://entra.microsoft.com)
* Klik in de linkernavigatie op **Entra ID** > **Enterprise apps**.
* Klik op **New application** en daarna op **Create your own application**.
* Voer de naam van de toepassing in, bijvoorbeeld "Dastra".
* Selecteer **Integrate any other application you don't find in the gallery (Non-gallery)** en maak de toepassing aan.
* Klik in het gedeelte **Manage** op **Single sign-on** en selecteer **SAML**.
* U komt op deze pagina:

<figure><img src="../../../.gitbook/assets/ad1.png" alt="De SAML-configuratiepagina van een enterprise-toepassing in Microsoft Entra ID"><figcaption></figcaption></figure>

## De SSO-client configureren in Dastra

### Stap 1: een SAML-SSO-login maken in Dastra

* Ga naar de [SSO-configuratiepagina van Dastra](https://app.dastra.eu/general-settings/sso) (**Organisatie-instellingen** > **Eenmalig inloggen**).
* Klik op **Voeg een SSO-login toe**.
* Selecteer bij **SSO-protocol** de optie **SAML2** en daarna **Handmatige configuratie**.
* Voer bij **Titel van de SSO-verbinding** een naam voor de verbinding in, bijvoorbeeld "Active Directory".

### Stap 2: de SSO-login configureren in Microsoft Entra ID

* Ga terug naar de SAML-configuratiepagina van Microsoft Entra ID.
* Klik op **Edit** in het gedeelte **Basic SAML Configuration**.
* Voer de verbindingsgegevens in die bovenaan het SAML-formulier van Dastra staan: **Identifier (Entity ID)** en **Reply URL (Assertion Consumer Service URL)**:

<figure><img src="../../../.gitbook/assets/ad2.png" alt="Het gedeelte Basic SAML Configuration met de identifier en de reply-URL"><figcaption></figcaption></figure>

* Klik op **Save**.
* Ga direct naar het gedeelte **SAML Certificates** om het certificaat in Base64-formaat te downloaden:

<figure><img src="../../../.gitbook/assets/ad3.png" alt="Het gedeelte SAML Certificates met de downloadlink voor het Base64-certificaat"><figcaption></figcaption></figure>

* Open het CER-bestand met een teksteditor (bijvoorbeeld Kladblok) en kopieer de inhoud (Ctrl + C):

<figure><img src="../../../.gitbook/assets/ad4.png" alt="De inhoud van het certificaat geopend in een teksteditor"><figcaption></figcaption></figure>

### Stap 3: het certificaat toevoegen aan de Dastra-client

* Ga terug naar het scherm voor het maken van de SAML-verbinding in Dastra.
* Plak de tekst van het certificaat (Ctrl + V) in het veld **Identity Provider Certificaat (RAW)**.

### Stap 4: de URL's van de identiteitsprovider configureren in Dastra

* Kopieer in het gedeelte **Set up** van de Entra ID-toepassing de drie waarden **Login URL**, **Microsoft Entra Identifier** en **Logout URL**:

<figure><img src="../../../.gitbook/assets/ad5.png" alt="Het gedeelte Set up van de toepassing met de drie te kopiëren URL's"><figcaption></figcaption></figure>

* Plak ze in Dastra volgens deze koppeling:
  * **Login URL**: **Identity Provider SSO url**
  * **Microsoft Entra Identifier**: **Entiteits-ID van de identiteitsprovider (uitgever)**
  * **Logout URL**: **Uitlog-URL van identiteitsprovider**
* Uw SSO-configuratieformulier in Dastra moet er zo uitzien:

<figure><img src="../../../.gitbook/assets/settings-sso-entra-dastra-idp-configuration.png" alt="Het SAML-formulier van Dastra, ingevuld met de waarden van Microsoft Entra ID"><figcaption></figcaption></figure>

* U kunt de optie **Gebruiker aangemaakt als de gebruiker nog nooit is uitgenodigd voor Dastra** inschakelen, in de sectie **Automatisch gebruikers aanmaken**. In dat geval worden accounts uit uw directory die nog niet in Dastra bestaan, aangemaakt bij hun eerste login:

<figure><img src="../../../.gitbook/assets/settings-sso-entra-auto-create-user-option.png" alt="De optie voor automatische gebruikersaanmaak in het SSO-formulier"><figcaption></figcaption></figure>

* Sla uw wijzigingen op in Dastra.

{% hint style="info" %}
Zorg ervoor dat er een gebruiker aan de nieuwe toepassing is toegewezen voordat u de verbinding test.
{% endhint %}

### Uw SSO-verbinding testen

Klik in Microsoft Entra ID op de knop **Test** in het gedeelte **Test single sign-on** van de toepassing. Als alles werkt, wordt u doorgestuurd naar Dastra.

{% hint style="info" %}
Als u de automatische gebruikersaanmaak niet hebt ingeschakeld, weigert Dastra de toegang totdat het lokale account via een uitnodiging is aangemaakt.
{% endhint %}

### Meer informatie

{% content-ref url="known-problems.md" %}
[Bekende problemen](known-problems.md)
{% endcontent-ref %}

{% content-ref url="saml.md" %}
[SAML 2](saml.md)
{% endcontent-ref %}
