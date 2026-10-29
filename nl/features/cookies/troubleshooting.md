---
description: >-
  De meest voorkomende oorzaken van een cookiebanner die niet verschijnt, en
  hoe u ze oplost.
---

# Problemen oplossen

Verschijnt de cookiebanner niet, controleer dan de volgende punten in deze volgorde.

1. Controleer de toegestane URL's. Klik in het menu op **Toestemming voor cookies** > **Banners**, open de banner en daarna de sectie **Configuratie**. Het adres van uw website moet in de lijst **Geautoriseerde URL's (CORS)** staan, in het formaat `https://myurl.com`, zonder pad. Dit is de meest voorkomende oorzaak: een origin die niet in de lijst staat, wordt geweigerd.

   <figure><img src="../../.gitbook/assets/cookies-configure-6.png" alt="De sectie Configuratie met het veld Geautoriseerde URL's (CORS)"><figcaption><p>Het veld "Geautoriseerde URL's (CORS)"</p></figcaption></figure>
2. Controleer de status van de banner. In de editor moet de schakelaar **Status** op **Actief** staan.
3. Controleer de geldigheid van uw openbare API-sleutel (gebruik niet de privésleutel). Klik op het tandwielpictogram in de bovenbalk (**Organisatie-instellingen**) en daarna op **API-sleutels**. Controleer of de sleutel bestaat en niet is verlopen. Zie [API-sleutelbeheer](../settings/api-keys.md).

   <figure><img src="../../.gitbook/assets/cookies-quickstart-1.png" alt="De pagina API-sleutels met de lijst met sleutels"><figcaption><p>De pagina "API-sleutels"</p></figcaption></figure>
4. Controleer of u niet per ongeluk een weergavetrigger hebt ingesteld. Een te hoge waarde bij **Scroll hoogte als % van het paginaformaat (0% = bovenkant van de pagina)** in de sectie **Triggers** voorkomt dat de banner verschijnt wanneer de bezoeker op de pagina aankomt.
5. Controleer de opties die de banner verbergen. De optie **Schakel de bannerweergave uit (alle cookies met standaardtoestemming worden geactiveerd)** verbergt de banner, en **Activeer de Global Privacy Control (GPC)** doet dat ook voor bezoekers van wie de browser dit signaal verzendt. Een bezoeker die al een keuze heeft gemaakt, ziet de banner niet meer: verwijder de cookie `consent-eu` uit uw browser om te testen.
6. Controleer uw abonnement. Uw abonnement moet de functie bevatten om de cookietoestemmingsbanner te gebruiken. Verschijnt het menu **Toestemming voor cookies** niet in de navigatie, dan is de functie waarschijnlijk niet inbegrepen: neem contact op met de eigenaar van uw organisatie. Is het abonnement verlopen, dan weigert de API de bannerconfiguratie. Voor meer informatie kunt u contact opnemen met de [support](mailto:support@dastra.eu).
7. [Neem contact op met de support](../../getting-started/support/request.md) voor elk ander probleem.
