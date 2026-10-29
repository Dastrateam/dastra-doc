# Veelgestelde vragen

## Ontvangen aanvragers een e-mailnotificatie wanneer een verzoek wordt gesloten?

Standaard wordt er geen e-mail verstuurd. De sluitingsmelding gaat alleen naar de aanvrager als u in het sluitingsvenster het vakje **Stuur een melding van de afsluiting van het verzoek naar** aanvinkt (gevolgd door het e-mailadres van de aanvrager). Het vakje verschijnt alleen wanneer het verzoek een e-mailadres heeft en is grijs wanneer de aanvrager al op de hoogte is gebracht.

<figure><img src="../../.gitbook/assets/requests-faq-1.png" alt="Het sluitingsvenster van een verzoek met het notificatievakje aangevinkt"><figcaption><p>Het notificatievakje in het sluitingsvenster</p></figcaption></figure>

{% hint style="info" %}
Kies deze optie wanneer u de betrokkene wilt informeren dat zijn verzoek is afgehandeld. Dat is een goede praktijk en helpt u aan te tonen dat u de antwoordtermijn van de AVG hebt nageleefd.
{% endhint %}

***

## Hoe lang houdt de aanvrager na sluiting toegang tot de beveiligde ruimte?

Nadat het verzoek is gesloten, houdt de aanvrager gedurende 60 dagen toegang tot zijn beveiligde ruimte (uitwisselingsgeschiedenis, verstuurde documenten). In die periode kan de aanvrager nog steeds via de gespreksinterface een bericht sturen naar de persoon die het verzoek behandelt.

Na 60 dagen wordt de toegang automatisch ingetrokken.

## Hoe werkt de verificatie van het e-mailadres van de aanvrager?

Wanneer een verzoek via het openbare formulier wordt ingediend, ontvangt de aanvrager een bevestigings-e-mail met een validatielink en een code van 6 cijfers. Het verzoek wordt pas in behandeling genomen zodra het adres is gevalideerd.

* De link en de code zijn 24 uur geldig. Deze duur is niet configureerbaar.
* Na meerdere onjuiste invoeren van de code (4) worden verdere pogingen 30 minuten geblokkeerd.
* Wordt de termijn overschreden, dan moet de aanvrager een nieuw verzoek indienen.

## Waarom kan een aanvrager geen nieuw verzoek indienen?

Dezelfde aanvrager (hetzelfde e-mailadres) kan in dezelfde werkruimte geen tweede verzoek van hetzelfde type indienen zolang het vorige, dat minder dan 24 uur geleden is ingediend, niet is gesloten.

## Wat is de maximale lengte van een bericht in een verzoek?

Berichten die met de aanvrager worden uitgewisseld, het bericht van het openbare formulier en sluitingsredenen zijn beperkt tot 3.000 tekens. Een bericht kan maximaal 20 bijlagen bevatten.

***

## Plaatst de pagina voor het verzamelen van verzoeken cookies? Is een toestemmingsbanner nodig?

Nee. De widgetpagina van Dastra (URL van de vorm `https://api.dastra.eu/v1/client/data-subject-request/page?id=…`) plaatst slechts één cookie: `acaAffinity`.

Dit is een cookie voor taakverdeling (Azure Application Gateway). Het enige doel is de serversessie stabiel te houden door verzoeken naar hetzelfde backendknooppunt te routeren. Het duurt zolang de sessie, is beveiligd (`Secure`, `HttpOnly`) en valt onder de vrijstelling van toestemming van artikel 5, lid 3, van de e-privacyrichtlijn, bevestigd door de richtsnoeren van de CNIL (cookies die strikt noodzakelijk zijn voor de werking van de dienst).

Op deze pagina is geen toestemmingsbanner vereist.

{% hint style="success" %}
Audit uitgevoerd op 27 april 2026: 0 analytische cookies, 0 reclamecookies, 0 trackers van derden aangetroffen. De ingeladen bronnen van derden (Bootstrap van cdnjs.cloudflare.com, het lettertype Poppins van fonts.bunny.net, de SDK van cdn.dastra.eu) plaatsen geen cookies.
{% endhint %}

***

## Moet de cookie `acaAffinity` in ons cookieregister staan?

Ja, voor een volledige documentatie, ook al is de cookie vrijgesteld van toestemming. Dit is de aanbevolen vermelding:

| Veld | Waarde |
| --- | --- |
| Naam | `acaAffinity` |
| Domein | `api.dastra.eu` |
| Categorie | Technisch / Strikt noodzakelijk |
| Doeleinde | Taakverdeling: stabiliteit van de serversessie |
| Duur | Sessie (verwijderd wanneer de browser wordt gesloten) |
| Uitgever | Dastra (verwerker) |
| Wettelijke basis | Vrijstelling e-privacy: strikt noodzakelijk |
| Toestemming vereist | Nee |
