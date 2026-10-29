---
description: >-
  Verstuur de e-mails van Dastra vanuit uw eigen Office 365- of Gmail-mailbox in
  plaats van vanaf het standaardadres van Dastra.
---

# Integratie van externe providers (Office 365 / Gmail)

Deze pagina legt uit hoe u de e-mails van Dastra verstuurt vanuit uw eigen Office 365- of Gmail-account. Ze is bedoeld voor eigenaren van de organisatie. Wilt u een andere verzendserver gebruiken, zie dan [SMTP-configuratie](README.md).

## Doel

Standaard komen alle notificaties van Dastra van het adres `no-reply@dastra.eu`. Met de integratie van een externe e-mailprovider (Office 365 of Gmail) verstuurt u deze e-mails vanaf uw eigen adressen. Dat biedt de volgende voordelen:

* uw ontvangers hebben meer vertrouwen in de e-mails, omdat ze vanaf uw domein worden verstuurd;
* u centraliseert uw verzend- en afleverlogs in uw eigen e-mailinfrastructuur;
* u past uw eigen beveiligings-, compliance- en archiveringsregels toe.

## Betrokken e-mails

De configuratie geldt voor alle e-mails die Dastra binnen uw organisatie verstuurt, bijvoorbeeld:

* meldingen van nieuwe taken of verzoeken;
* uitnodigingen en herinneringen;
* compliancewaarschuwingen;
* opvolging van verzoeken van betrokkenen, incidenten, workflows enzovoort.

Zodra de integratie is ingeschakeld, gebruiken al deze e-mails het geconfigureerde adres in plaats van `no-reply@dastra.eu`.

{% hint style="warning" %}
Alle e-mails die vanuit de organisatie worden verstuurd, worden beïnvloed, dus alle werkruimten.
{% endhint %}

## De integratie instellen

De instelling is voorbehouden aan eigenaren van de organisatie en aan het Enterprise-abonnement (geavanceerde beveiligingsfunctie).

### Stap 1: de verbinding met de provider autoriseren

1. Open [https://app.dastra.eu/general-settings/smtp](https://app.dastra.eu/general-settings/smtp), dat wil zeggen **Organisatie-instellingen** > **Aangepaste SMTP**.
2. Klik in de sectie **Leveranciers** op **Outlook (MS Office 365)** of **Gmail (Google workspace)**.
3. Er opent een venster waarin u zich via OAuth aanmeldt bij Microsoft of Google. Gebruik een account dat e-mails mag versturen met het adres dat u wilt gebruiken.
4. Na de authenticatie toont Dastra het scherm voor de configuratie van de afzender.

<figure><img src="../../../.gitbook/assets/screenshot-2025-09-19-110910.png" alt="Pagina Aangepaste SMTP met de knoppen voor de providers Outlook en Gmail"><figcaption><p>De providers die de pagina Aangepaste SMTP aanbiedt</p></figcaption></figure>

{% hint style="info" %}
In de instellingen voor de werkruimte leidt de integratiekaart voor Office 365 of Gmail naar dezelfde pagina.
{% endhint %}

Deze stap is verplicht: zonder autorisatie van de provider kan Dastra geen e-mails met uw account versturen.

### Stap 2: de afzender invullen

Twee velden zijn verplicht:

1. **e-mail van de afzender**: het adres dat als afzender van de notificaties wordt gebruikt (bijvoorbeeld `notifications@uwdomein.com`).
2. **Naam van afzender**: de naam die als afzender wordt weergegeven (bijvoorbeeld `Compliance-team - Uw bedrijf`).

Klik daarna op **Registreren en testen**.

### Stap 3: het verzenden controleren

Dastra stuurt een testbericht naar het e-mailadres van uw account, met de geconfigureerde afzender. Controleer uw inbox en uw Office 365- of Gmail-logs om na te gaan of het bericht is aangekomen.

<figure><img src="../../../.gitbook/assets/settings-smtp-test-email-received.png" alt="Ontvangen testbericht met de bijlage test-attachment.txt"><figcaption><p>Het ontvangen testbericht</p></figcaption></figure>

Zodra de verbinding tot stand is gebracht, toont de pagina **Aangepaste SMTP** het e-mailadres en de naam van de afzender. Klik op **Verwijder de integratie** om terug te keren naar het standaardverzenden van Dastra of om een andere server te gebruiken.

## Belangrijke aandachtspunten

### Verzendlogs

Met uw eigen provider beheert u zelf uw verzendlogs. De teams van Dastra zien geen informatie meer over aflevering, weigering of blokkering van deze e-mails.

### Reputatie van IP-adres en domein

Uw infrastructuur staat in voor een goede aflevering. Zorg ervoor dat:

* uw SPF-, DKIM- en DMARC-records correct zijn ingesteld;
* uw afzenderreputatie goed is;
* uw domein en IP-adres niet als spam op een lijst staan.

### Gevolgen voor uw ontvangers

Notificaties verschijnen alsof uw organisatie ze rechtstreeks heeft verstuurd. Ontvangers herkennen ze, en het risico op verwarring met een generiek adres is kleiner.

## Aanbevelingen voor de beveiliging

* Beperk de adressen die voor het verzenden worden gebruikt (bijvoorbeeld `no-reply@uwdomein.com` of `notifications@uwdomein.com`).
* Schakel meervoudige authenticatie in op de accounts die voor de integratie worden gebruikt.
* Controleer regelmatig uw verzendlogs in Office 365 of Gmail om afwijkingen op te sporen.

## Technische vragen voor IT-beheerders

Dit gedeelte beantwoordt veelgestelde vragen van IT- en beveiligingsteams bij het instellen van de Office 365-integratie.

### Welk authenticatiemodel wordt gebruikt?

De Office 365-integratie gebruikt de OAuth 2.0-autorisatiecodestroom met gedelegeerde machtigingen: Dastra verstuurt e-mails namens het account dat de verbinding heeft geautoriseerd, met de rechten van dat account. Het gaat niet om een toepassingsverbinding met toestemming van een globale beheerder. Afhankelijk van het beleid van uw Microsoft 365-organisatie moet een beheerder de gevraagde machtigingen mogelijk goedkeuren.

### Welke Microsoft Graph-machtigingen worden gevraagd?

Dastra vraagt bij de autorisatie de volgende gedelegeerde machtigingen:

| Machtiging | Gebruik |
| --- | --- |
| `Mail.Send` | E-mails verzenden vanuit de mailbox van het verbonden account |
| `Mail.Send.Shared` | Verzenden vanuit een gedeelde mailbox |
| `offline_access` | De toegang vernieuwen zonder opnieuw aan te melden |

Voor Gmail vraagt Dastra de toegang `https://mail.google.com/`.

### Worden gedeelde mailboxen ondersteund?

Ja. Voor een gedeelde mailbox (bijvoorbeeld `privacy@uwbedrijf.com`) gaat u als volgt te werk:

1. Meld u aan met uw persoonlijke account, dat het recht heeft om vanuit de gedeelde mailbox te verzenden.
2. Vul in het veld **e-mail van de afzender** het adres van de gedeelde mailbox in.

Voor deze instelling is geen wijziging van het Exchange-beleid (ApplicationAccessPolicy) nodig.

{% hint style="info" %}
Controleer of uw persoonlijke account in Active Directory of Exchange de machtiging "Send As" of "Send on Behalf" heeft op de gedeelde mailbox.
{% endhint %}

### Moet ik de uitgaande IP-adressen van Dastra toestaan?

Dastra verstuurt e-mails via de Microsoft Graph API, niet via een traditionele SMTP-server. De aanroepen lopen via de Azure-infrastructuur van Microsoft, die over veel IP-bereiken beschikt (ongeveer 100) die in de loop van de tijd veranderen.

Filteren op IP-adres wordt voor deze integratie niet aanbevolen: het is moeilijk te onderhouden en kan de dienst onderbreken wanneer de Azure-bereiken worden bijgewerkt. De beveiliging berust op OAuth 2.0 en op de autorisatie van het verbonden account.

{% hint style="info" %}
Vereist uw beveiligingsbeleid een IP-beperking, raadpleeg dan de bereiken die Microsoft voor Azure-diensten publiceert: [https://www.microsoft.com/en-us/download/details.aspx?id=56519](https://www.microsoft.com/en-us/download/details.aspx?id=56519). Deze lijst wordt regelmatig bijgewerkt.
{% endhint %}
