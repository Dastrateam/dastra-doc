---
description: >-
  Leer hoe u authenticatie verplicht stelt, de toegang tot documenten beheert en
  de IP-adressen van uw Trust Center filtert.
---

# Beveiliging

De sectie **Veiligheid** van de bewerkingspagina bundelt drie instellingen: verplichte authenticatie, goedkeuring van het downloaden van documenten en filtering op IP-adres. De eigenaren van het Trust Center wijst u aan in de sectie **Configuratie**.

<figure><img src="../../../.gitbook/assets/trust-center-security-1.png" alt="Sectie Veiligheid van een Trust Center met de twee opties en de IP-filterregels"><figcaption><p>De sectie Veiligheid van een Trust Center</p></figcaption></figure>

## Verplichte authenticatie

Schakel **Authenticatie vereist om toegang te krijgen tot het Trust Center** in om inloggen verplicht te stellen. Bezoekers moeten zich dan aanmelden bij Dastra met een account van uw organisatie voordat ze het portaal openen. Als er een SSO is toegewezen aan alle gebruikers, worden ze naar die SSO doorverwezen.

Wij raden aan [SSO](../../settings/sso/README.md) in te stellen met automatische aanmaak van gebruikers: al uw medewerkers hebben dan toegang tot het Trust Center zonder specifieke rol of machtiging.

## Eigenaren

Het veld **Eigenaren** staat in de sectie **Configuratie**. Zie [Startpagina en algemene configuratie](home.md).

## Toegangscontrole tot documenten

De optie **Een goedkeuring vereisen voor het downloaden van bestanden** verschijnt alleen wanneer de functie **Bijlagen** is aangevinkt. Ze is ingeschakeld voor een nieuw Trust Center.

Wanneer ze is ingeschakeld:

1. Bezoekers zien de lijst met documenten, maar kunnen ze niet rechtstreeks downloaden. Ze dienen een **toegangsverzoek** in met hun e-mailadres en een bericht.
2. De eigenaren van het Trust Center ontvangen een e-mail met een link naar het verzoek. Als er geen eigenaar is, ontvangen de eigenaren van de organisatie die e-mail.
3. De eigenaar opent het verzoek, vult indien nodig een **Justificatie van de beslissing** in en klikt vervolgens op **Toegang verzoek goedkeuren** of **Verzoek om toegang afwijzen**. De bezoeker ontvangt de justificatie per e-mail.
4. Als het verzoek wordt goedgekeurd, ontvangt de bezoeker een e-mail met een **downloadlink die 30 dagen geldig is**.

De verzoeken worden behandeld in het scherm **Verzoeken om toegang tot bestanden**, dat alle verzoeken met hun status toont. De link in de meldingsmail opent het scherm rechtstreeks op het betreffende verzoek.

{% hint style="info" %}
Wanneer er eigenaren zijn aangewezen, kunnen alleen zij verzoeken goedkeuren of afwijzen. Zonder eigenaar worden de verzoeken gemeld aan de eigenaren van de organisatie.
{% endhint %}

## Filteren op IP-adres

In deze sectie kunt u ook regels definiëren om de toegang tot uw Trust Center te beperken tot bepaalde IP-bereiken. Standaard, zonder dat u IP-filtering toevoegt, is uw Trust Center toegankelijk voor iedereen met de toegangslink, op voorwaarde dat het Trust Center is geactiveerd.

Klik op **IP-filterregel toevoegen** en geef vervolgens de naam van de regel en het begin en het einde van het IP-bereik op. Een IP-adres dat tot geen enkel bereik behoort, wordt geweigerd.

{% hint style="info" %}
Deze filtering staat **los van** de [IP-filtering van de organisatie](../../settings/ip-filtering.md), die niet van toepassing is op het Trust Center.
{% endhint %}
