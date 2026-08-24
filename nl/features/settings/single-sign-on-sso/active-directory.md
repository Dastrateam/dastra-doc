---
description: >-
  Deze pagina legt uit hoe u Dastra SSO instelt met de Microsoft
  Microsoft Active Directory met behulp van het Saml2P protocol
---

# Active Directory

## De applicatie configureren in de azure portal*** * Ga naar de Microsoft Azure portal.

* Ga naar het Microsoft Azure-portaal: [https://portal.azure.com](https://portal.azure.com)
* Klik op **Active Directory**.
* Klik in de linkernavigatie op Enterprise Applications
* Klik op de knop **Nieuwe toepassing**.
* Klik vervolgens op **Eigen toepassing maken**.
* Voer de naam van de applicatie in, u kunt gewoon "Dastra" invoeren.
* Selecteer het vakje "**Integreer elke andere applicatie die u niet in de galerij vindt (Non-gallery)**".
* Uw toepassing is gemaakt!
* Klik op **Single-Sign-On** en selecteer **SAML**.
* U bevindt zich nu op deze pagina**!

![](<../../../.gitbook/assets/image (8).png>)

## **De SSO-client configureren in Dastra**

**Stap 1: Maak een OpenId SSO login in Dastra***.

* Ga naar de [Dastra SSO-configuratiepagina](https://app.dastra.eu/general-settings/sso)
* Klik op "Een SSO login toevoegen".
* Selecteer **SAML** als het type "**SSO Protocol**".
* Voer een aanmeldingslabel in. Bijvoorbeeld "Active Directory".

**Stap 2: Configureer de SSO login in Active Directory** * Keer terug naar de configuratiepagina.

* Ga terug naar de SAML Active Directory configuratiepagina.
* Klik op de knop "Bewerken"** in het eerste deel.
* Voer de verbindingsgegevens (**Entity ID en ACS Url**) als volgt in:

![](<../../../.gitbook/assets/image (3) (1) (1) (1).png>)

* Klik op **Opslaan**.
* Ga direct naar deel 3 om **het certificaat in base64 formaat** te downloaden.
* ![](<../../../.gitbook/assets/image (5) (1).png>)
* Open het CER bestand met je favoriete teksteditor** (bijv. Kladblok) en kopieer de inhoud (CTRL + C)
* ![](<../../../.gitbook/assets/image (4) (1).png>)

**Stap 3: Voeg het certificaat toe aan de Dastra-client**

* Keer terug naar het SAML connectie creatie scherm in Dastra.
* Plak de tekst van het certificaat** in het veld "Identity Provider Certificate (RAW)" (CTRL + V).

**Stap 4: Configureer de IdP URL's in Dastra** * Kopieer de drie Entity links naar de Dastra server

* Kopieer de 3 links Entity Id, SSO Url en Logout Url van stap 4 van Active Directory
* ![](<../../../.gitbook/assets/image (7) (1) (1).png>)
Kopieer de urls volgens het volgende schema:* **Login URL => Single on one.
  **Login URL => Single sign on url.
  **Azure AD Identifier => Identity Id van de Identity provider**.
  **Logout Url => Identity provider Signout url** * Uw SSO-configuratieformulier
* Uw SSO-configuratieformulier in Dastra moet er als volgt uitzien:
* ![](<../../../.gitbook/assets/image (2) (1) (1) (1).png>)
* Je kunt het vakje "Gebruiker aangemaakt als de gebruiker nog nooit is uitgenodigd bij Dastra" aanvinken. Als u deze optie activeert, zullen de accounts van uw AD-organisatie die niet aanwezig zijn in Dastra tijdens het inloggen worden aangemaakt als ze niet lokaal in Dastra bestaan.

![](<../../../.gitbook/assets/image (6).png>)

* Sla uw wijzigingen** op in Dastra

{% hint style="info" %}
Voordat je de verbindingstest start, moet je ervoor zorgen dat er een gebruiker is toegewezen aan de nieuwe applicatie.
{% endhint %}

### Test uw SSO-verbinding

Klik vervolgens op de knop "Test" onderaan het formulier in de actieve map. Als alles correct werkt, wordt u doorgestuurd naar de Dastra-toepassing.

{% hint style="info" %}
Als u **automatic provisioning** van accounts niet hebt geactiveerd, wordt de toegang geweigerd aan de Dastra-kant als het lokale account niet is aangemaakt via een uitnodiging.
{% endhint %}

### Om verder te gaan

{% content-ref url="problemes-connus.md" %}
[problemes-connus.md](problemes-connus.md)
{% endcontent-ref %}

{% content-ref url="saml-2.md" %}
[saml-2.md](saml-2.md)
{% endcontent-ref %}