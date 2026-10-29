---
description: >-
  Diagnose en oplossing van de SSO-authenticatieproblemen (SAML 2 en OpenID
  Connect) die het vaakst aan ons supportteam worden gemeld.
---

# Bekende problemen

Deze pagina bundelt de SSO-incidenten waar onze klanten in de praktijk tegenaan lopen, met de oplossing. Ze is geordend op symptoom: zoek wat u op het scherm ziet.

{% hint style="danger" %}
Stel altijd een uitzonderingsaccount in voordat u SSO voor iedereen verplicht.

Schakelt u **Forceer voor alle gebruikers** in en valt SSO uit (verlopen certificaat, upgrade van de identiteitsprovider, configuratiefout), dan kan niemand meer inloggen, ook de eigenaren niet. Geef ten minste één gebruiker op in het veld **Specifieke gebruikers die zijn vrijgesteld van SSO (bijv. beveiligingsbeheerders)**, bij voorkeur een lokaal serviceaccount, zodat u weer bij de configuratie kunt en het probleem kunt oplossen.

Zie [Gebruikers die zijn vrijgesteld van SSO-login](README.md#gebruikers-vrijgesteld-van-sso-login).
{% endhint %}

## De 5 controles die u eerst uitvoert

Loop deze lijst door voordat u dieper gaat zoeken:

1. Test de configuratie. De knop **Testen** op de kaart van de SSO-verbinding controleert de dialoog met uw identiteitsprovider. Mislukt de test, dan zit het probleem in de configuratie en niet in het gebruikersaccount.
2. Bestaat de gebruiker in de organisatie? SSO hoort bij de organisatie: de gebruiker moet in de [gebruikerslijst](https://app.dastra.eu/general-settings/users) staan.
3. Komt het e-mailadres exact overeen? Dastra herkent het account aan het e-mailadres dat de identiteitsprovider terugstuurt. Bij het kleinste verschil van één teken wordt de gebruiker niet herkend.
4. Heeft de gebruiker aan de kant van de identiteitsprovider toegang tot de Dastra-toepassing? Dit is de belangrijkste oorzaak van storingen bij één persoon.
5. Test in een privévenster en controleer of de klok van de machine gesynchroniseerd is: een afwijkende klok maakt tokens ongeldig.

***

## De gebruiker wordt niet herkend door SSO

### Het e-mailadres van de IdP komt niet overeen met het Dastra-account

Verreweg de vaakste oorzaak. Dastra gebruikt de e-mailclaim om de SSO-identiteit aan een bestaand account te koppelen. Verschillen de twee waarden, dan beschouwt Dastra dit als een nieuwe gebruiker. Is het automatisch aanmaken van accounts uitgeschakeld, dan wordt de aanmelding geweigerd.

Typische gevallen:

* het Dastra-account is `first.last@company.com`, maar de IdP van de testomgeving stuurt `first.last@company-stg.com` terug;
* de UPN is in de bedrijfsmap gewijzigd (naamswijziging, domeinmigratie) zonder dat Dastra is bijgewerkt;
* de gebruiker is in Dastra aangemaakt met een verkorte vorm van het adres (`flast@…`), terwijl de IdP de lange vorm terugstuurt.

Oplossing: breng de twee waarden op één lijn, in de richting die u past:

* laat de IdP exact het adres terugsturen dat in Dastra is geregistreerd, of
* maak het Dastra-account aan of corrigeer het, zodat het het adres draagt dat de IdP terugstuurt.

{% hint style="info" %}
Om te weten welke waarde werkelijk wordt verstuurd, bekijkt u de SAML-assertion of het ID-token dat uw IdP terugstuurt (zie [Diagnosegegevens verzamelen](#diagnosegegevens-verzamelen)).
{% endhint %}

### De naam van de claim met het e-mailadres komt niet overeen

Ook als het adres correct wordt doorgegeven, kan Dastra het niet vinden: de claim wordt op zijn exacte naam opgezocht.

Standaard verwacht Dastra de claim:

```
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
```

Sommige IdP's publiceren het attribuut echter onder een korte naam, bijvoorbeeld:

```xml
Name="emailaddress"
NameFormat="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
```

Dastra gebruikt de eigenschap `Name` en niet `NameFormat`: de waarde staat wel in het SAML-antwoord, maar de verwachte claim wordt niet gevonden.

Oplossing:

1. Open uw SSO-configuratie, sectie **Configuratie**.
2. Vervang in het veld **De naam van de claim met het e-mailadres** de waarde door de naam die uw IdP daadwerkelijk publiceert (hier: `emailaddress`).
3. Sla op en voer een nieuwe test uit in een privévenster, zodat een nieuwe sessie wordt aangemaakt.

### De gebruiker heeft geen toegang tot de toepassing bij de identiteitsprovider

Wordt slechts één gebruiker geblokkeerd terwijl iedereen normaal inlogt, dan ligt het probleem bijna altijd bij de IdP.

Oplossing: controleer of de persoon in uw map is aangemaakt en aan de Dastra-toepassing is toegewezen met de vereiste toegangsrechten. Een goede onderscheidende test is de gebruiker te laten inloggen zonder SSO (vrijgesteld account of wachtwoord): werkt dat, dan is het Dastra-account in orde en komt de blokkade van de toegangsrechten bij de IdP.

### De gebruiker is een externe gebruiker

SSO geldt alleen voor accounts die intern zijn voor uw organisatie. Had de gebruiker al een Dastra-account (andere organisatie, proefaccount, persoonlijk account), dan is zijn hoofdorganisatie een andere: de beveiligingsinstellingen van die organisatie gelden, niet de uwe, en de gebruiker verschijnt in uw organisatie als externe gebruiker.

Controleer de status in de [gebruikerslijst van de organisatie](https://app.dastra.eu/general-settings/users). De koppeling met de hoofdorganisatie kan niet via de interface worden gewijzigd: neem contact op met de support en vermeld het betrokken e-mailadres.

***

## Het automatisch aanmaken van accounts werkt niet

### "SSO users autoprovisioning is not allowed for your organization"

Dit bericht betekent dat de optie **Gebruiker aangemaakt als de gebruiker nog nooit is uitgenodigd voor Dastra** niet is ingeschakeld in uw SSO-configuratie. Zolang ze is uitgeschakeld, kan alleen een gebruiker die al voor Dastra is uitgenodigd via SSO inloggen.

Oplossing: een eigenaar van de organisatie schakelt de optie in bij de SSO-configuratie, sectie **Automatisch gebruikers aanmaken**, en kiest de rol die standaard wordt toegekend.

<figure><img src="../../../.gitbook/assets/settings-sso-overview-4.png" alt="De sectie Automatisch gebruikers aanmaken van het SSO-formulier"><figcaption><p>De sectie <strong>Automatisch gebruikers aanmaken</strong></p></figcaption></figure>

{% hint style="warning" %}
Alleen een eigenaar kan de SSO-configuratie wijzigen. Een beheerder ziet deze pagina niet.
{% endhint %}

### De optie is ingeschakeld, maar er worden nog steeds geen accounts aangemaakt

Automatisch aanmaken wordt alleen geactiveerd wanneer de gebruiker via de SSO-link binnenkomt. Een gebruiker die via de gewone aanmeldpagina inlogt, krijgt geen account.

Verspreid de verbindingslink van uw SSO onder uw gebruikers, in de vorm:

```
https://account.dastra.eu/Account/ExternalLogin?returnUrl=https://app.dastra.eu&provider={your provider id}
```

U vindt de link met de knop **Link kopiëren** op de kaart van de SSO-verbinding:

<figure><img src="../../../.gitbook/assets/settings-sso-overview-2.png" alt="De kaart van een SSO-verbinding met de knoppen Testen en Link kopiëren"><figcaption><p>De knop <strong>Link kopiëren</strong> op de kaart</p></figcaption></figure>

### Externe respondenten van een vragenlijst worden niet aangemaakt

Iemand die de SSO-link nooit heeft geopend, is geen Dastra-gebruiker: automatisch aanmaken geldt daarom niet voor respondenten die voor een externe vragenlijst zijn uitgenodigd.

Er zijn twee omwegen:

* maak de accounts vooraf aan: zie [een gebruikerslijst importeren](../../../getting-started/setup/users.md);
* verspreid de vragenlijst via een Trust Center, dat bezoekers een SSO-login biedt.

***

## Authenticatielus of fout bij terugkeren naar Dastra (OpenID Connect)

Symptomen: een omleidingslus tussen Dastra en de IdP, de foutmelding "An error was encountered while handling the remote login" of een HTTP 400-fout bij het ophalen van het token.

In dat geval werken de omleiding naar de IdP en de authenticatie allebei: het is de verwerking van de OIDC-callback die mislukt. Controleer de volgende punten, in deze volgorde.

### Het veld "Autoriteit/domein" verwijst naar het verkeerde eindpunt

Een zeer vaak voorkomende configuratiefout. Dit veld moet de basis-URL van de OIDC-uitgever bevatten, die `/.well-known/openid-configuration` aanbiedt, en niet het eindpunt `/authorize`.

| | |
| --- | --- |
| Onjuist | `https://login.example.com/user/IdPOAuth2/authorize/FB6CB139F80BCAEB` |
| Juist | `https://login.example.com/user/IdPOAuth2/FB6CB139F80BCAEB` |

De eindpunten `/authorize` en `/token` worden dan automatisch gevonden via het well-known-document.

### Het type reactie is onjuist

Het veld **Type reactie (Standaard: id_token)** moet exact een van de waarden bevatten die uw IdP publiceert, meestal `id_token` of `code`.

Let op varianten met een koppelteken: de waarde `id-token` in plaats van `id_token` veroorzaakt een authenticatielus met een 400-fout bij het ophalen van het token. Controleer teken voor teken.

Mislukt de flow met `id_token`, probeer dan `code`: sommige IdP's staan de impliciete flow niet toe.

### De clientauthenticatiemethode is niet de juiste

Ziet de configuratie er correct uit maar kan het token niet worden opgehaald, dan accepteert uw IdP mogelijk geen clientauthenticatie met een geheime sleutel. Selecteer in de sectie **Configuratie** van de verbinding **Privésleutel JWT (private jwt assertion)** in plaats van **Geheime sleutel**, en vul daarna de privésleutel in PEM-formaat en de inhoud van het certificaat in. De velden worden beschreven bij [OpenId](openid.md).

{% hint style="info" %}
Met de privésleutel JWT hoeft u geen geheime sleutel meer op te geven en schakelt het type reactie over op `code`. Vergeet niet één keer op te slaan, zodat de URI van de openbare JSON-sleutel (`jwks_uri`) beschikbaar wordt, en declareer die daarna bij uw identiteitsprovider.
{% endhint %}

Vereist uw IdP een andere clientauthenticatiemethode, zoals HTTP Basic-authenticatie, neem dan contact op met de support.

### Het ID-token is ondertekend met HS256

Afhankelijk van de integratie kan Dastra een asymmetrische RS256-handtekening vereisen, met de openbare sleutel beschikbaar via de `jwks_uri`. Een ID-token dat met HS256 is ondertekend, kan bij de validatie worden geweigerd.

Controleer aan de kant van de IdP of de Dastra-client met een RS256-handtekening kan worden geconfigureerd.

### Andere oorzaken om uit te sluiten

* De omleidings-URL is niet gedeclareerd bij de IdP. Ze moet ongewijzigd worden geregistreerd, in de vorm `https://account.dastra.eu/signin-{schemeId}`, in de toepassing die bij uw provider is gedeclareerd (bijvoorbeeld onder *App Registration* > *Authentication* in Azure).
* De gebruikte `redirect_uri` is niet strikt identiek aan de geconfigureerde.
* De uitgever van het token komt niet exact overeen met de URL die in Dastra is geconfigureerd.
* De scopes zijn niet toegekend. Houd `openid profile email` aan en controleer of alle drie bij de IdP zijn toegestaan.
* De claim `email` ontbreekt in het ID-token.

### "The value of the response_type parameter is unknown"

Verschijnt dit bericht op de pagina van uw identiteitsprovider (en niet in Dastra), dan werkt de omleiding: het probleem zit in de declaratie van de OIDC-client bij de IdP.

Controleer:

* de toegestane waarden van `response_type` voor de toepassing die in uw SSO is gedeclareerd;
* de configuratie van de OIDC-client die aan Dastra is gekoppeld;
* de gebruikte delegatiemodus (bijvoorbeeld CAS/OIDC).

***

## Certificaatfouten (SAML 2)

U krijgt een foutmelding van dit type, die een niet-vertrouwde of ongeldige sleutel meldt:

1. Controleer of het certificaat geldig is: een verlopen certificaat geeft precies dit symptoom, vaak van de ene dag op de andere zonder wijziging aan uw kant.
2. Controleer of bij het kopiëren en plakken van het certificaat geen regeleinde of overbodige spatie is ontstaan.
3. Controleer of het certificaat dat in Dastra is geconfigureerd, dat is van de IdP van de betrokken omgeving: een veelgemaakte fout is het certificaat van de testomgeving op de productieconfiguratie te laten staan.

### Een SSO-certificaat vernieuwen

Het certificaat wordt rechtstreeks bijgewerkt in de [SSO-configuratie van uw organisatie](https://app.dastra.eu/general-settings/sso). Vervang als eigenaar het huidige certificaat door het nieuwe certificaat van uw teams en gebruik daarna de knop **Testen**.

{% hint style="warning" %}
Plan de vervanging vooraf: vernieuw vóór de vervaldatum en controleer of uw SSO-uitzonderingsaccount nog werkt voordat u iets wijzigt.
{% endhint %}

### De configuratie werkt in de testomgeving maar niet in productie

Is de productieconfiguratie gemodelleerd naar een werkende configuratie van de testomgeving, dan verschillen bijna altijd drie parameters:

* de ACS-/antwoord-URL die bij de IdP is gedeclareerd, moet exact overeenkomen met de callback-URL van productie die Dastra levert: controleer dat de URL van de testomgeving niet is overgenomen;
* het SAML-certificaat moet dat van de IdP van productie zijn;
* de tenant-ID moet die van productie zijn. Deze parameter wordt niet in Dastra geconfigureerd: u kunt hem alleen aan de kant van de IdP controleren.

***

## De gebruiker logt in maar heeft nergens toegang toe

### "You are not allowed to access this feature or resource (area/entity)"

Authenticeert de gebruiker correct en komt hij bij het kiezen van zijn werkruimte op deze pagina terecht (in de Nederlandse toepassing met de titel "Onbereikbare bron (403)"), dan ligt het probleem niet bij SSO maar bij zijn rechten.

Eén oorzaak die in productie is vastgesteld: de gebruiker heeft een aangepaste rol zonder enige machtiging. Dastra kan dan geen toegang verlenen en stuurt hem naar deze pagina.

Oplossing: open de betrokken rol en geef die minstens één machtiging die past bij het verwachte toegangsniveau. U hoeft de cache niet te wissen en hoeft SSO niet verder te onderzoeken.

{% content-ref url="../roles.md" %}
[Rollen en machtigingen](../roles.md)
{% endcontent-ref %}

### De fout "Access denied (401)" na het inloggen via SSO

Controleer voordat u SSO verdenkt of de klok van de machine met internet is gesynchroniseerd: de geldigheidsduur van tokens wordt vergeleken met de tijd van de machine. Dit is een klassieke oorzaak van een 401 direct na een geslaagde authenticatie.

Zie ook het onderdeel over 401 bij de [algemene bekende problemen](../../../other/known-problems.md).

***

## Wijziging van het e-mailadres en domeinmigratie (UPN)

In Dastra is het e-mailadres de structurele identificatie van het account: het ligt ten grondslag aan identificatie, uitnodigingen, authenticatie en de koppeling met items op het platform. Het kan daarom niet in bulk via de beheerinterface worden gewijzigd.

Het directe gevolg voor SSO: verandert de UPN in de map zonder dat het adres in Dastra wordt bijgewerkt, dan wordt de gebruiker niet meer herkend.

| Situatie | Wat u doet |
| --- | --- |
| Eén gebruiker | De gebruiker wijzigt zijn eigen adres in zijn profielinstellingen. Alleen de betrokken persoon kan deze actie uitvoeren. |
| Bulkmigratie van een domein | Een uitzonderlijke handeling die Dastra in één keer uitvoert, op basis van een volledig en gecontroleerd bestand dat u aanlevert (oud adres en nieuw adres). Open vooraf een supportticket. |

{% hint style="danger" %}
Houd bij een bulkmigratie drie regels in gedachten:

* in één keer: opeenvolgende gedeeltelijke migraties veroorzaken inconsistenties in SSO, gebruikersidentificatie, machtigingen en koppelingen;
* geen tussenliggend adres: lever meteen het definitieve doeladres aan; hetzelfde account kan niet twee keer worden gemigreerd;
* houd rekening met neveneffecten: lopende verzoeken van betrokkenen en vragenlijsten kunnen de oude adressen bevatten: geef expliciet aan of ze ook moeten worden bijgewerkt.
{% endhint %}

{% hint style="info" %}
Verwijder en maak accounts niet opnieuw aan om tijd te winnen: u verliest dan de geschiedenis en de koppeling tussen de persoon en de items waarvoor die verantwoordelijk is. Let er ook op dat de voor- en achternaam behouden blijven wanneer een verwijderde gebruiker opnieuw wordt uitgenodigd. Dat is het verwachte gedrag.
{% endhint %}

***

## Twee SSO-accounts in dezelfde browser

U kunt niet tegelijk met meerdere verschillende SSO-accounts inloggen vanuit dezelfde browser of dezelfde machine, ook niet met aparte browserprofielen.

Omweg: log in op het tweede account met standaardauthenticatie (e-mail en wachtwoord) in plaats van SSO. Valt dat account onder SSO, geef het dan op bij de vrijgestelde gebruikers.

Dit gedrag verklaart ook enkele fouten die in een privévenster worden gezien wanneer elders al een SSO-sessie openstaat.

***

## Het aanmeldscherm van de identiteitsprovider verschijnt bij elke aanmelding

Bij OpenID Connect verloopt het traject iets anders dan bij SAML:

* bij de eerste aanmelding voert de gebruiker zijn e-mailadres in op de aanmeldpagina van Dastra; zo wordt zijn organisatie geïdentificeerd en wordt hij naar uw identiteitsprovider omgeleid. Een cookie onthoudt deze provider daarna als voorkeursmethode voor aanmelden;
* bij latere aanmeldingen wordt de gebruiker automatisch naar de IdP omgeleid, zonder zijn adres opnieuw in te voeren.

Verschijnt het aanmeldscherm elke keer terwijl aan de kant van de IdP al een sessie actief is, dan dwingt mogelijk een OIDC-instelling het tonen van de aanmeldvraag af. Controleer dit bij de identiteitsprovider en meld het aan de support als het gedrag aanhoudt.

***

## SSO werkt niet meer na een upgrade van de IdP

Een upgrade van uw identiteitsinfrastructuur (versiewijziging van OpenAM of ADFS, migratie naar Entra ID…) kan certificaten, validatiemechanismen en de afhandeling van de OIDC-flow wijzigen. Typisch symptoom: een authenticatielus terwijl er aan de kant van Dastra niets is veranderd.

Wat u doet:

1. Werk in een test- of sandboxomgeving, nooit rechtstreeks in productie.
2. Maak de SSO-configuratie helemaal opnieuw aan in plaats van de bestaande aan te passen: zo sluit u een parameter uit die uit de vorige versie is overgenomen.
3. Let in het bijzonder op het bijwerken en valideren van de certificaten.
4. Voer de controles uit het bovenstaande onderdeel [Authenticatielus of fout bij terugkeren naar Dastra (OpenID Connect)](#authenticatielus-of-fout-bij-terugkeren-naar-dastra-openid-connect) opnieuw uit.

***

## Niemand kan nog inloggen

{% hint style="danger" %}
Om redenen van beveiliging en toegangsbeheer maakt of wijzigt het supportteam van Dastra geen gebruikersaccounts in organisaties van klanten en genereert het geen inloggegevens. Alleen een eigenaar van uw organisatie kan dit.
{% endhint %}

Is SSO voor iedereen verplicht en buiten gebruik:

1. Log in met een SSO-uitzonderingsaccount (vooraf opgegeven in het veld **Specifieke gebruikers die zijn vrijgesteld van SSO (bijv. beveiligingsbeheerders)**).
2. Schakel vanuit dat account de SSO-verbinding uit (de optie **Inschakelen**) terwijl u de configuratie herstelt, zodat gebruikers weer met een wachtwoord kunnen inloggen.
3. Herstel de configuratie, test met de knop **Testen** en schakel de verbinding daarna weer in.

Bestaat er geen uitzonderingsaccount, neem dan onmiddellijk contact op met de support en vermeld de naam van uw organisatie. Maak er een aan zodra de toegang is hersteld.

***

## Diagnosegegevens verzamelen

Is het probleem met de bovenstaande punten niet opgelost, dan kunnen onze teams met een netwerkexport de authenticatieflow nauwkeurig analyseren. Zo gaat u te werk.

### Stap 1: de ontwikkelaarstools openen

* Open een privévenster (Chrome of Edge).
* Druk op `F12` (of `Ctrl + Shift + I`).
* Selecteer het tabblad **Network**.

### Stap 2: het bewaren van het logboek inschakelen

Vink de optie **Preserve log** aan. Dit is essentieel: zonder deze optie gaat de geschiedenis verloren tijdens de omleidingen tussen Dastra en uw identiteitsprovider.

### Stap 3: het probleem reproduceren

Start de SSO-aanmelding en ga door tot de fout of de omleidingslus. Sluit het venster niet na de fout.

### Stap 4: exporteren

* Optie A (aanbevolen): klik met de rechtermuisknop in de lijst met verzoeken, kies **Save all as HAR with content** en stuur ons het `.har`-bestand.
* Optie B: schermafbeeldingen van het tabblad Network, met de verzoeken `/authorize`, `/token` en `/signin` en elk verzoek met een fout (400, 401, 403…).

### Stap 5: de context beschrijven

Vertel ons ook:

* precies wanneer de blokkade optreedt: bij het klikken op de SSO-link, wanneer de authenticatiepagina verschijnt, na het invoeren van de inloggegevens of na het verzenden van het aanmeldformulier;
* de exacte foutmelding (schermafbeelding);
* voor OIDC: de uitgever (issuer), de `client_id` en de `redirect_uri` die bij de IdP zijn geconfigureerd, het handtekeningalgoritme van het token en de teruggestuurde claims (`sub`, `email`, `preferred_username`…), met gevoelige gegevens afgeschermd;
* voor SAML: de ontvangen assertion (gevoelige gegevens afgeschermd).

{% hint style="info" %}
Een video-opname van de hele reeks (bijvoorbeeld met Loom), met de ontwikkelaarstools geopend, versnelt de diagnose aanzienlijk.

Een testaccount dat via uw SSO kan authenticeren, met hetzelfde type toegang als de getroffen gebruikers, is het nuttigste element: zo kunnen wij het hele traject reproduceren. Het account mag tijdelijk zijn en na afloop van het onderzoek worden verwijderd.
{% endhint %}

{% content-ref url="../../../getting-started/support/request.md" %}
[Ondersteuning aanvragen](../../../getting-started/support/request.md)
{% endcontent-ref %}
