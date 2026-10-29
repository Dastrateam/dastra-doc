# Integratie van externe providers (Office 365 / Gmail)

## Doel <a href="#objectif" id="objectif"></a>

Standaard komen alle meldingen van Dastra van het adres no-reply@dastra.eu. Met de integratie van uw externe e-mailproviders (Office 365 of Gmail) laat u e-mails versturen vanaf uw eigen e-mailadressen. Dat biedt de volgende voordelen:

* Uw ontvangers hebben meer vertrouwen in de e-mails, want ze komen van uw eigen domein.
* U centraliseert uw verzend- en afleverlogs rechtstreeks in uw e-mailinfrastructuur.
* U beheert zelf uw beveiligings-, compliance- en archiveringsregels.

***

## Betrokken e-mails <a href="#perimetre-des-mails-concernes" id="perimetre-des-mails-concernes"></a>

Deze configuratie geldt voor alle meldingsmails die Dastra binnen uw organisatie verstuurt, bijvoorbeeld:

* Meldingen van nieuwe taken of verzoeken.
* Uitnodigingen en herinneringen.
* Compliancewaarschuwingen.
* Opvolging van verzoeken om rechten uit te oefenen, incidenten, workflows enzovoort.

Alle uitgaande e-mails gebruiken dus het geconfigureerde adres in plaats van no-reply@dastra.eu.

{% hint style="warning" %}
Deze instelling geldt voor alle e-mails die vanuit de organisatie worden verstuurd. Alle werkruimten worden erdoor beïnvloed.
{% endhint %}

***

## De integratie configureren <a href="#configuration-de-lintegration" id="configuration-de-lintegration"></a>

### Stap 1: de integratie met de provider openen en de verbinding autoriseren

* Ga naar **Instellingen voor werkruimte** > **Integraties**.
* Klik op het toevoegen van een configuratie voor Office 365 of Gmail.

U opent de configuratie ook via deze URL: [https://app.dastra.eu/general-settings/smtp](https://app.dastra.eu/general-settings/smtp)

![Configuratie van de provider voor het verzenden van e-mails](<../../../.gitbook/assets/screenshot-2025-09-19-110910.png>)

* Selecteer de provider die u wilt gebruiken:
  * **Outlook (MS Office 365)**
  * **Gmail (Google workspace)**
* Bij de eerste keer vraagt Dastra u de verbinding te autoriseren:
  * Er opent een venster waarin u zich via OAuth aanmeldt bij Microsoft of Google.
  * Gebruik een account met voldoende rechten (bijvoorbeeld een beheerdersaccount of een account met de toestemming om namens het domein te verzenden).
* Na een geslaagde authenticatie bevestigt Dastra de verbinding en toont het scherm voor de configuratie van de afzender.

{% hint style="warning" %}
Deze stap is noodzakelijk om Dastra te machtigen e-mails via uw provider te versturen. Zonder deze stap werkt de configuratie van de afzender niet.
{% endhint %}

### Stap 2: de gevraagde gegevens invullen

![Scherm voor de configuratie van de afzender](<../../../.gitbook/assets/screenshot-2025-09-19-111634.png>)

U vult twee verplichte velden in:

1. **e-mail van de afzender**
   * Het e-mailadres dat als afzender van de meldingen wordt gebruikt (bijvoorbeeld `notifications@uwdomein.com`).
2. **Naam van afzender**
   * De naam die als afzender wordt getoond (bijvoorbeeld `Compliance team - Uw bedrijf`).

Klik daarna op **Registreren en testen** om de configuratie te valideren.

### Stap 3: controleren en testen

* Dastra verstuurt een testbericht om te bevestigen dat het geconfigureerde adres geldig is.
* Controleer uw inbox en uw Office 365/Gmail-logs om na te gaan of het testbericht is afgeleverd.

Het testbericht bevestigt dat de verbinding correct is ingesteld.

***

## Belangrijke aandachtspunten <a href="#points-importants-a-retenir" id="points-importants-a-retenir"></a>

1. Verantwoordelijkheid voor de logs
   * Gebruikt u uw eigen provider (Office 365 of Gmail), dan beheert u zelf uw verzendlogs.
   * Informatie over aflevering, weigering of blokkering van e-mails is niet meer zichtbaar voor de teams van Dastra.
2. Beheer van de reputatie van IP-adres en domein
   * Uw infrastructuur (Office 365 of Gmail) staat in voor een goede aflevering.
   * Zorg ervoor dat:
     * uw SPF-, DKIM- en DMARC-records correct zijn ingesteld;
     * uw afzenderreputatie goed is;
     * uw domein en IP-adres niet als spam op een lijst staan.
3. Gevolgen voor uw ontvangers
   * Meldingen verschijnen alsof uw organisatie ze rechtstreeks heeft verstuurd.
   * Dat maakt ze herkenbaarder en beperkt het risico op verwarring met generieke adressen.

***

## Aanbevelingen voor de beveiliging <a href="#bonnes-pratiques-de-securite" id="bonnes-pratiques-de-securite"></a>

* Beperk de adressen die voor het verzenden worden gebruikt (bijvoorbeeld `no-reply@uwdomein.com` of `notifications@uwdomein.com`).
* Schakel meervoudige authenticatie in op de accounts die voor de integratie worden gebruikt.
* Controleer regelmatig uw verzendlogs in Office 365/Gmail om afwijkingen op te sporen.

***

Zodra de integratie is ingeschakeld, gebruikt Dastra no-reply@dastra.eu niet meer: al uw meldingsmails worden verstuurd via de door u geconfigureerde provider.

***

## Technische veelgestelde vragen voor IT-beheerders

Dit gedeelte beantwoordt veelgestelde vragen van IT- en beveiligingsteams bij het instellen van de Office 365-integratie.

### Welk authenticatiemodel wordt gebruikt?

De Office 365-integratie gebruikt toestemming op toepassingsniveau (toestemming van een globale beheerder), geen gedelegeerde toestemming namens een gebruiker. Voor de werking van de integratie is geen actieve Exchange-licentie per gebruiker nodig.

### Welke Microsoft Graph-scopes worden gevraagd?

Dastra vraagt bij de OAuth-toestemming de volgende machtigingen:

| Machtiging         | Gebruik                                                    |
| ------------------ | ---------------------------------------------------------- |
| `Mail.Send`        | E-mails verzenden vanuit de geconfigureerde mailbox        |
| `Mail.Send.Shared` | Verzenden vanuit een gedeelde mailbox                      |

### Worden gedeelde mailboxen ondersteund?

Ja. Voor een gedeelde mailbox (bijvoorbeeld `privacy@uwbedrijf.com`) gaat u als volgt te werk:

1. Meld u aan met uw persoonlijke account dat verzendrechten heeft op de gedeelde mailbox.
2. Vul in het veld **e-mail van de afzender** het adres van de gedeelde mailbox in.

Hiervoor is geen wijziging van het Exchange-beleid (ApplicationAccessPolicy) nodig.

{% hint style="info" %}
Controleer of uw persoonlijke account in Active Directory / Exchange de machtiging **Send As** of **Send on Behalf** heeft op de gedeelde mailbox.
{% endhint %}

### Moet ik de uitgaande IP-adressen van Dastra op een whitelist zetten?

Dastra verstuurt e-mails via de Microsoft Graph API, niet via een traditionele SMTP-server. De aanroepen lopen via de Azure-infrastructuur van Microsoft, die over veel IP-bereiken beschikt (ongeveer 100) en in de loop van de tijd verandert.

Filteren op IP-adres wordt voor deze integratie niet aanbevolen: het is moeilijk te onderhouden en kan tot onderbrekingen leiden wanneer de IP-bereiken van Azure worden bijgewerkt. De beveiliging berust op OAuth 2.0 en toestemming van een beheerder.

{% hint style="info" %}
Vereist uw beveiligingsbeleid IP-beperkingen, raadpleeg dan de IP-bereiken die Microsoft voor Azure-diensten publiceert: [https://www.microsoft.com/en-us/download/details.aspx?id=56519](https://www.microsoft.com/en-us/download/details.aspx?id=56519). Deze lijst wordt regelmatig bijgewerkt.
{% endhint %}
