---
description: >-
  Maak de API-sleutels van uw organisatie aan en beheer ze: werkruimte, vervaldatum, machtigingen, toegang tot de MCP-server.
---

# API-sleutelbeheer

Deze pagina legt uit waarvoor de API-sleutels van Dastra dienen en hoe u ze aanmaakt en beheert. Alleen de eigenaren van de organisatie hebben er toegang toe.

## Gebruik van API-sleutels

* Een Dastra API-client aanmaken om gegevens buiten de toepassing op te halen of te wijzigen. Deze client kan server-to-server (Client credential) of JavaScript (Authorization code) zijn. Lees voor meer informatie de [documentatie over de authenticatie van de Dastra API](../../api/authentication.md).
* Een widget voor verzoeken van betrokkenen configureren (alleen de openbare sleutel). Lees de [documentatie over de formulieren voor verzoeken](../requests/widget.md).
* Een cookiewidget configureren (alleen de openbare sleutel). Lees de [documentatie over cookies](../cookies/banner/configure.md).
* Een AI-hulpmiddel verbinden met de Dastra MCP-server. Lees de [documentatie over de MCP-server](../general/ai-assistant/mcp.md).

## Waar u API-sleutels beheert

Klik op het tandwielpictogram in de bovenbalk (**Organisatie-instellingen**) en daarna op **API-sleutels** in het linkermenu. Het directe adres is [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api).

De pagina heeft drie tabbladen:

* **API keys**: de lijst met sleutels. Per sleutel ziet u de naam, het laatste gebruik (**Never** als de sleutel nooit is gebruikt) en de werkruimte. De badge **Expired** markeert een sleutel waarvan de vervaldatum is verstreken, en de badge `MCP` een sleutel met toegang tot de MCP-server.
* **MCP Server**: verbind een AI-hulpmiddel met de Dastra MCP-server. Zie [De MCP-server](../general/ai-assistant/mcp.md).
* **tenantId & workspaceId**: de identificatie van de organisatie (**TENANT ID**) en van elke werkruimte (**WORKSPACE ID**), met een knop om ze te kopiëren. API-aanroepen die om deze identificaties vragen, gebruiken ze.

## Een API-sleutel aanmaken

1. Klik in het tabblad **API keys** op **Maak een nieuwe API-sleutel**.
2. Vul de **Naam** van de sleutel in.
3. Kies de werkruimte in **Een specifieke werkruimte selecteren** als u de sleutel tot één werkruimte wilt beperken. Kiest u er geen, dan geldt de sleutel voor **Alle werkplekken**.
4. Kies de **Expiration**: **Unlimited**, 30 dagen, 180 dagen, 365 dagen of **Custom date**.
5. Antwoord bij **Deze API-sleutel volledige rechten geven?** met **Ja** voor een sleutel zonder beperkingen, of met **Neen** om alleen de machtigingen aan te vinken die de sleutel mag gebruiken.
6. Klik op **Creëren**.

<figure><img src="../../.gitbook/assets/settings-api-keys-1.png" alt="Het venster voor het aanmaken van een API-sleutel met naam, werkruimte, vervaldatum en machtigingen"><figcaption><p>Een API-sleutel aanmaken</p></figcaption></figure>

Het paneel **API key details** opent. Het toont:

* de openbare sleutel (`client_id`) en de privésleutel (`client_secret` of API-sleutel), die verborgen is en vanuit het paneel kan worden gekopieerd;
* de knop **Privésleutel opnieuw genereren**, waarmee u een nieuwe privésleutel genereert zonder de API-sleutel te verwijderen;
* de werkruimte, de toegang tot de MCP-server, het laatste gebruik en de vervaldatum van de sleutel;
* de **Permissions** van de sleutel, die u met de bewerkknop aanpast;
* de toegestane CORS-origins en de toegestane redirect-URI's, die u invult als u de API in JavaScript met OAuth2 (Authorization code) gebruikt.

<figure><img src="../../.gitbook/assets/settings-api-keys-2.png" alt="Het paneel met de details van een API-sleutel, met de privésleutel verborgen"><figcaption><p>De details van een API-sleutel</p></figcaption></figure>

{% hint style="info" %}
De vervaldatum en de toegang tot de MCP-server kiest u bij het aanmaken van de sleutel en kunt u daarna niet meer wijzigen. Maak een nieuwe sleutel aan om een van beide te wijzigen.
{% endhint %}

## Een sleutel gebruiken met de MCP-server

Als uw abonnement de MCP-server bevat (Dastra AI Pro), biedt het aanmaakvenster de optie **Allow this key to access the MCP server (requires a specific workspace)**. Schakel ze in en kies een werkruimte: de MCP-server weigert een sleutel zonder deze optie of zonder werkruimte. Toegestane sleutels dragen de badge `MCP` in de lijst. Zie [De MCP-server](../general/ai-assistant/mcp.md).

## Een sleutel vervangen of verwijderen

{% hint style="warning" %}
Bewaar uw API-sleutels veilig. De privésleutel mag nooit openbaar worden gemaakt.

Is de beveiliging van uw API-sleutel in het gedrang gekomen, klik dan in het detailpaneel op **Privésleutel opnieuw genereren**, of verwijder de sleutel uit de lijst (menu met drie puntjes > **Verwijderen**) en maak een nieuwe aan.
{% endhint %}
