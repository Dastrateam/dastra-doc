---
description: >-
  Deze pagina legt uit hoe u de SCIM-configuratie van Dastra met een
  ondernemingsdirectory zoals Azure Active Directory (Cloud)
---

# SCIM

### Hoe het werkt

[SCIM](http://www.simplecloud.info/), wat staat voor System for Cross-domain Identity Management, is een open standaard die de automatisering van de gebruikersvoorziening ondersteunt. Het SCIM-protocol is een tussenpersoon die identiteitsgegevens van gebruikers verzamelt van identiteitsproviders (Azure AD, Google Workspace, Okta, enz.) en deze doorgeeft aan serviceproviders die deze identificatiegegevens nodig hebben (zoals Dastra).

{% hint style="warning" %}
De SCIM-functionaliteit is voorbehouden aan klanten met een **Enterprise plan**.

[Zie onze prijspagina](https://www.dastra.eu/pricing)
{% endhint %}

{% hint style="info" %}
We raden sterk aan dat u eerst [SSO instelt](single-sign-on-sso/)**met de optie "Forceer voor alle gebruikers" geactiveerd**.
{% endhint %}

### Hoe configureer ik SCIM met Azure Active Directory?

Dastra-gebruikers kunnen worden toegevoegd, verwijderd en gewijzigd met SCIM 2.0.

U definieert groepen in uw Azure Directory en Dastra kan deze gebruikers synchroniseren. Het is een geweldige manier om tijd en moeite te besparen bij het beheren van gebruikersaccounts. Het is ook een ideale beveiligingsimplementatie.

#### 1. Log in op Azure en klik op Azure Active Directory

<figure><img src="https://www.reftab.com/img/faq/01-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 2. Ga naar "Bedrijfstoepassingen

<figure><img src="https://www.reftab.com/img/faq/02-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 3. Klik op "Nieuwe toepassing".

<figure><img src="https://www.reftab.com/img/faq/03-azure.png" alt="03-Azure-SCIM"><figcaption></figcaption></figure>

#### 4. Klik op "Maak uw eigen toepassing".

<figure><img src="https://www.reftab.com/img/faq/04-azure.png" alt="04-Azure-SCIM"><figcaption></figcaption></figure>

#### 5. Geef je toepassing een naam

<figure><img src="../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

#### 6. Klik in de nieuw aangemaakte applicatie op de knop "Provision User Accounts".

<figure><img src="https://www.reftab.com/img/faq/06-azure.png" alt="06-Azure-SCIM"><figcaption></figcaption></figure>

#### 7. Klik op "Aan de slag".

<figure><img src="https://www.reftab.com/img/faq/07-azure.png" alt="07-Azure-SCIM"><figcaption></figcaption></figure>

#### 8. Stel de provisioningmodus in op automatisch. Vul de URL van de huurder en het geheime token in van uw Dastra-accountgegevens.

**Log in op Dastra** als beheerder. **Ga naar de organisatieconfiguratie** > **klik op Beveiliging / SCIM**.

![](<../../.gitbook/assets/image (14) (1).png>)

Klik op de **configureer** knop

<figure><img src="../../.gitbook/assets/image (18) (2).png" alt=""><figcaption></figcaption></figure>

Configureer je SCIM. Selecteer de werkruimte die u wilt synchroniseren (teams en gebruikers worden automatisch in deze werkruimte ingesteld).

Kies vervolgens de standaardrol die u aan nieuwe gebruikers wilt geven. De rollen worden lokaal beheerd door de Dastra-accountbeheerder.

Klik op **Registreren**.

**Kopieer het authenticatietoken en de SCIM Url**.

{% hint style="info" %}
Vandaag kunt u met Dastra in SCIM (teams + gebruikers) **alleen één werkruimte per organisatie** synchroniseren.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Klik op "**Test verbinding**" en "**Opslaan**". Als er een fout optreedt tijdens de verbindingstest, kan dit te wijten zijn aan een gebrek aan geactiveerde functionaliteit in uw abonnement. [Neem contact op met support](../../start/support/request-support.md)

#### 9. Applicatieprovisioning inschakelen

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

#### 10. Voeg gebruikers en/of groepen toe aan de gemaakte applicatie

<figure><img src="../../.gitbook/assets/image (9) (3).png" alt=""><figcaption></figcaption></figure>

### Laat je gebruikers verbinden

Uw AD gebruikersaccounts worden automatisch gesynchroniseerd in Dastra. Als ze inloggen in Dastra via [de inlogpagina](https://app.dastra.eu/login), zouden ze moeten kunnen inloggen met hun e-mail. Als SSO niet is geconfigureerd en geforceerd voor alle gebruikers, moeten gebruikers een wachtwoord resetten om in te loggen. Als SSO actief en geforceerd is voor alle gebruikers, worden ze automatisch doorgestuurd naar het inlogformulier van je identity provider (Azure AD, Google Workspace, Okta, etc.).



### Gedrag en beperkingen van SCIM-synchronisatie

#### Beheer van de gebruikerslevenscyclus

**Gebruiker uitgeschakeld in Entra ID**

Wanneer een gebruiker wordt uitgeschakeld in Entra ID:

* Wordt het profiel **geanonimiseerd in Dastra**
* Als de gebruiker later opnieuw wordt geactiveerd:
  * Wordt een **nieuw gebruikersaccount aangemaakt**
  * Het eerder geanonimiseerde account wordt niet hersteld

***

**Volledige verwijdering in Entra ID**

Wanneer een gebruiker definitief wordt verwijderd uit Entra ID:

* Wordt het profiel **volledig geanonimiseerd in Dastra**
* Alle eerdere acties blijven **behouden**
* De gebruiker verschijnt als **"deleted user"**

**Impact op gekoppelde gegevens:**

* Gekoppelde objecten (bijv. verwerkingen, risico’s, verzoeken, enz.) worden **niet verwijderd**
* Relaties (bijv. eigenaar, toegewezen persoon) blijven **behouden**
* Alleen de identiteit van de gebruiker wordt geanonimiseerd

***

#### Beheer van groepen (teams)

**Verwijdering van een groep in Entra ID**

Wanneer een groep wordt verwijderd in Entra ID:

* Wordt het overeenkomstige **team verwijderd in Dastra**
* **Gebruikersaccounts blijven actief**
* Geen impact op individuele gebruikers

***

#### Mapping en synchronisatiebereik

**Groepen en workspaces**

* SCIM ondersteunt de synchronisatie van **meerdere groepen**
* Huidige beperking:
  * Slechts **één workspace per organisatie** kan worden gesynchroniseerd
  * Synchronisatie over meerdere workspaces wordt **niet ondersteund**

***

**Ondersteunde attributen**

Momenteel synchroniseert Dastra:

* De **naam van de groep (`displayName`)**

Niet ondersteund op dit moment:

* Mapping naar **organisatorische eenheden**
* Synchronisatie van attributen zoals:
  * organisatie
  * land

> Dit kan in de toekomst mogelijk worden ondersteund via een specifiek attribuut met een referentie-ID die compatibel is met Dastra.

***

#### Lokale beheeropties in Dastra

Na SCIM-synchronisatie:

* Kunnen beheerders nog steeds:
  * **rollen aanpassen**
  * **rechten beheren**
* Fijnmazig toegangsbeheer blijft **lokaal mogelijk in Dastra**

***

#### Impact op licenties

* SCIM-synchronisatie is beperkt door:
  * het **aantal gebruikers in uw abonnement**
* Als het quotum wordt overschreden:
  * Geeft de SCIM-server een **foutmelding**
  * Extra gebruikers worden **niet aangemaakt**
