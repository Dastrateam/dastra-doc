---
description: >-
  Dastra integreert met Adfs, deze pagina legt de details uit van de
  configuratie van SSO met AD FS
---

# ADFS

## Wat is ADFS?

Active Directory Federation Services (meestal ADFS genoemd) is een single sign-on (SSO) oplossing ontworpen door Microsoft. Met deze services, die een onderdeel zijn van Windows Server-besturingssystemen, kunnen gebruikers zich authenticeren via Active Directory (AD) wanneer ze toegang willen tot een applicatie die geen Integrated Windows Authentication (IWA) kan gebruiken.

**ADFS configureren in Dastra**

**Stap 1: Maak een SAML login aan in Dastra***.

* Ga naar de [Dastra SSO-configuratiepagina](https://app.dastra.eu/general-settings/sso)
* Klik op "Een SSO-login toevoegen".
* Selecteer **SAML** als het type "**SSO Protocol**".
* Voer in het veld "Identity Provider's Entity id (issuer)" de volgende url in: [**http**://<adfs server url>/adfs/services/trust](http://fs.saur.fr/adfs/services/trust)
* Voer in het veld "**Identity Provider single sign on url**" de volgende url in: [**https**://<adfs server url>](http://fs.saur.fr/adfs/services/trust)/adfs/ls

**Stap 2: Het ADFS-certificaat ophalen**".

* Ga naar de map "**Certificates**" op de ADFS-server.
* Haal het .CER-certificaat op van uw ADFS-server met het "**Token-Signing**"-certificaat.

![](<../../../.gitbook/assets/image (259).png>)

* Klik op "**Bekijk Certificaten**".

![](<../../../.gitbook/assets/image (250).png>)

Kopieer de X509 Certificaat code door het CER bestand te openen met een tekstverwerker.

Voeg de certificaat code in in het certificaat veld dat begint met "----BEGIN CERTIFICATE-----" en eindigt met "--------END CERTIFICATE-----".

Uw aanmeldingsconfiguratie zou er als volgt uit moeten zien:

![](<../../..gitbook/assets/image (257).png>)

**Stap 3**: Bewaar de volgende waarden:

* SP redirect URI (formaat: https://account.dastra.eu/xxxxx-xxxx-xxxx-xxxx/Acs) :*De SP redirect URI is Application Callback URL (SAML Token wordt hier gepost). De ondersteunde coderingen zijn SHA 256 en hoger.
* Identity id van de **Identity Provider (uitgever)**.

Deze twee waarden worden gebruikt om de ADFS server te configureren om Dastra SSO verzoeken te accepteren.

## De Dastra-client configureren in ADFS

Zo configureer je Dastra SSO met ADFS SSO SAML2P

**Stap 1**: Open "AD FS Management" op uw ADFS-server.

**Stap 2: Klik met de rechtermuisknop op "Relying Party Trusts" en selecteer "Add Relying Party Trust". Hiermee wordt de wizard **Add Relying Party Trust** gestart.

![](<../../../.gitbook/assets/image (248).png>)

**Stap 3:** Kies in het scherm _**Select Data Source**_ de optie _**Envoer gegevens over de betrouwbare partij handmatig in**_.

![](<../../../.gitbook/assets/image (254).png>)

**Stap 4:**Voer een _**Display naam** in, bijvoorbeeld **"Dastra"**_ _en klik op **"Volgende"**_.

**Stap 5: Kies het _**AD FS profiel**_ met SAML 2.0 en klik op "**Next**".

**Stap 6: Klik op _**Next**_ in het scherm _**Configure Certificate** zonder een certificaat te kiezen_.

**Stap 7:** Selecteer "_**Support for the SAML 2.0 SSO Web SSO protocol**_ inschakelen".

![](<../../../.gitbook/assets/image (252).png>)

In het veld "Relying party SAML 2.0 SSO service URL: zet de url van "**SP redirect URI"** aanwezig in de Dastra. Deze url heeft de vorm: https://account.dastra.eu/xxxx-xxxx-xxxx-xxxx/Acs

**stap 8**: Voeg in de sectie "**Add a Relying party trust identifier**" twee waarden toe** : _account.dastra.eu_ en _https://account.dastra.eu_

**Stap 9: Klik op Volgende om het proces te voltooien.

**Stap 10: Schakel het selectievakje _**Het dialoogvenster Claimregels bewerken openen**_ in voordat u op "Voltooien" klikt. Er verschijnt dan een venster "_**Declaratieregels bewerken"**_.

![](<../../../.gitbook/assets/image (251).png>)

\
**Stap 11: Klik op _**Add Rule**_ en kies de "Claim Rule": "_**Send LDAP Attributes as Claims"**_.

![](<../../../.gitbook/assets/image (256).png>)

**Stap 12**: Breng de claims als volgt in kaart, de claim namen kunnen variëren afhankelijk van je server configuratie. Dastra heeft drie attributen nodig om te functioneren: Email (Verplicht), Naam en Voornaam van de gebruiker :

![](<../../..gitbook/assets/image (258).png>)

**Stap 13: Klik op "Voltooien" en klik weer op "Regel toevoegen". Kies deze keer het type "_**Transform an Incoming Claim"** en klik op Next.

**Stap 14:** Configureer de volgende regel **: E-mailadres => Naam-ID => E-mail**.

![](<../../..gitbook/assets/image (249).png>)

Pas dan de veranderingen toe door op "Toepassen" te klikken.

**Stap 15: Terug in het "AD FS Management"**" venster, klik met de rechtermuisknop op "**Verbruikende partij voor Dastra**" en kies "**Eigenschappen**". In het tabblad _**Advanced**_ kiest u **SHA-256** als beveiligd algoritme.


**Stap 16: Het is je gelukt!

## Afsluiten en testen!

Zodra alles aan beide kanten is geconfigureerd, kunt u terugkeren naar Dastra en direct in de manager een SSO aanmeldtest uitvoeren.
