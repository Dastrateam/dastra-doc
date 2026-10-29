---
description: Integreer de Dastra-cookiebanner in een hybride applicatie.
---

# Hybride toepassingen

Een hybride applicatie toont webpagina's in een WebView. De SDK werkt dan op dezelfde manier als op een website.

1. Voeg de bannercode, gekopieerd uit de sectie **Installatie**, in op de pagina's die de WebView laadt. Zie [Snel aan de slag](../quickstart/README.md).
2. Voeg het adres van deze pagina's toe bij **Geautoriseerde URL's (CORS)**, in de sectie **Configuratie** van de banner. Zonder dit adres verschijnt de banner niet.
3. Geef de gepseudonimiseerde identifier van een gebruiker door om een bewijs van toestemming aan een gebruiker van de applicatie te koppelen. Zie [Gebruikersidentificatie](../identification.md).
4. Gebruik de JavaScript-API van de SDK om de toestemming vanuit uw code te lezen of te wijzigen. Zie [Toestemming programmatisch beheren](../programmatic-consent.md).
5. Voeg in de applicatie een manier toe om de banner opnieuw te openen, met `dastra.openCookieConsent()`.

U moet de trackers van de applicatie nog steeds handmatig configureren. Zie [Cookies blokkeren](../blocking/README.md).
