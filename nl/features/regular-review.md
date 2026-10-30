---
description: >-
  Activeer regelmatige beoordeling zodat Dastra u eraan herinnert uw items te
  beoordelen: verwerkingsactiviteiten, stakeholders, activa, AI-systemen,
  contracten en controlepunten.
---

# Terugkerende beoordeling (frisheid)

De frisheid geeft aan wanneer een item voor het laatst is beoordeeld. Wanneer u de regelmatige beoordeling voor een type item activeert, bepaalt u een interval tussen twee beoordelingen. Elke beoordeling stelt een volgende beoordelingsdatum in en de frisheid neemt af naarmate die datum nadert. Zo zorgt u ervoor dat de informatie in Dastra regelmatig wordt nagekeken.

Regelmatige beoordeling is beschikbaar voor verwerkingsactiviteiten, stakeholders, activa, AI-systemen, contracten en de controlepunten van het risicobeheer, afhankelijk van de modules van uw abonnement. De specifieke kenmerken van verwerkingsactiviteiten worden beschreven in [Frisheid van verwerkingsactiviteiten](ropa/freshness.md).

<figure><img src="../.gitbook/assets/freshness-en.png" alt="Schema van de werking van de frisheidsindicator"><figcaption><p>Werking van de frisheidsindicator</p></figcaption></figure>

## Regelmatige beoordeling activeren

Alleen gebruikers met de machtiging **Geavanceerde configuratie** kunnen deze instelling wijzigen.

1. Klik in het linkermenu op **Instellingen voor werkruimte** en klik daarna onder **Proces** op **Terugkerende beoordelingen**. U kunt ook klikken op **Activeer regelmatige beordeling van verwerkingen (frisheid)** in het optiemenu van een modulelijst: het item toont of de regelmatige beoordeling al is ingeschakeld voor dat type item.
2. Kies in de keuzelijst boven aan de pagina het type item.
3. Schakel **Schakel regelmatige beoordelingen in** in.
4. Voer bij **Selecteer het gewenste interval tussen elke beoordeling** het interval in jaren, maanden of dagen in.
5. Klik op **Opslaan**.

<figure><img src="../.gitbook/assets/regular-review-1.png" alt="De instellingen voor Terugkerende beoordelingen met de keuzelijst voor het type item, de activeringsschakelaar en het interval"><figcaption><p>De instellingen voor Terugkerende beoordelingen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/regular-review-2.png" alt="De lijst van itemtypen waarvoor regelmatige beoordeling beschikbaar is"><figcaption><p>De beschikbare itemtypen</p></figcaption></figure>

Het interval is hetzelfde voor alle items van een bepaald type. Zodra u het opslaat, vraagt Dastra **De nieuwe interval toepassen?**:

* **Toepassen op alle bestaande beoordelingen** vervangt alle volgende beoordelingsdata die al zijn ingesteld door nieuwe data, berekend vanaf het nieuwe interval.
* **Alleen toepassen op de volgende beoordelingen** behoudt de bestaande data, en het nieuwe interval geldt vanaf de volgende beoordeling.

## Regelmatige beoordeling deactiveren

Kies in dezelfde instellingen het type item, schakel **Schakel regelmatige beoordelingen in** uit en klik op **Opslaan**.

## De frisheid weergeven

De frisheid wordt alleen weergegeven voor **gepubliceerde** items die minstens één keer zijn beoordeeld.

Alle betrokken items hebben een kolom **Frisheid** (in het Engels **Last review date**), die u aan de kolommen van de lijst kunt toevoegen. Ze toont de frisheidsstatus van elk item.

<figure><img src="../.gitbook/assets/regular-review-3.png" alt="Een lijst met de kolom Frisheid"><figcaption><p>De kolom Frisheid</p></figcaption></figure>

Op de pagina van een verwerkingsactiviteit of een AI-systeem toont het rechterpaneel ook de balk **Frisheid**, die korter wordt naarmate de volgende beoordelingsdatum nadert. Naast de status en de kleur ervan ziet u de link **Beoordeling** en het aantal resterende of overschreden dagen.

<figure><img src="../.gitbook/assets/regular-review-4.png" alt="Het frisheidspaneel van de pagina van een verwerkingsactiviteit met de balk, de status en de link Beoordeling"><figcaption><p>De frisheidsindicator van de pagina van een verwerkingsactiviteit</p></figcaption></figure>

### Frisheidsstatussen

| Status | Weergaveregel |
| --- | --- |
| **Fris** (groen) | Het item is onlangs beoordeeld en vraagt geen onmiddellijke aandacht. Deze status wordt weergegeven totdat de huidige datum in de laatste 10 procent van het interval valt. |
| **binnenkort** (oranje) | Het item moet worden gecontroleerd. Deze status wordt weergegeven tijdens de laatste 10 procent van het interval na de laatste beoordeling. |
| **Verouderd** (rood) | De volgende beoordelingsdatum is verstreken: het item voldoet niet meer aan het beoordelingsbeleid. |

{% hint style="info" %}
**Voorbeeld:** u hebt een interval van 1 jaar ingesteld. Een item dat op 1 januari 2026 is beoordeeld, wordt tot eind november 2026 als **Fris** weergegeven, en daarna als **binnenkort** tot 1 januari 2027. Na die datum wordt het als **Verouderd** weergegeven totdat het is beoordeeld.
{% endhint %}

## Een item beoordelen

U kunt op elk moment een item beoordelen, zonder te wachten op de volgende beoordelingsdatum. Klik in een lijst op de cel van de kolom **Frisheid** van het item. Klik op de pagina van een verwerkingsactiviteit of een AI-systeem op **Beoordeling**.

<figure><img src="../.gitbook/assets/regular-review-5.png" alt="Het beoordelingsvenster met de velden ervan"><figcaption><p>Het beoordelingsvenster</p></figcaption></figure>

Vul op het tabblad **Nieuwe recensie** in:

* **Recensent**: de gebruiker die de beoordeling heeft uitgevoerd.
* **Beoordelingsdatum**.
* **Beschrijving van de versie:** wat is gecontroleerd of gewijzigd (optioneel).
* **Datum voor volgende beoordeling**: berekend op basis van het interval dat in de instellingen is gedefinieerd. Om een datum specifiek voor dit item in te stellen, schakelt u **De volgende beoordelingsdatum wijzigen** in en kiest u een datum (ten vroegste de volgende dag).

Klik op **Beoordeling** om op te slaan: er begint een nieuwe frisheidscyclus vanaf de beoordelingsdatum.

Het tabblad **Oude recensies** toont de eerdere beoordelingen van het item. Het biedt ook de knop **Delete all reviews**, waarmee u de geschiedenis wist. Na bevestiging wordt het item beschouwd als nooit beoordeeld, worden de beoordelingsdata gewist en verdwijnt de frisheidsindicator. Deze actie kan niet ongedaan worden gemaakt.

## Beoordelingen volgen op het dashboard

De tegel **Gegevensverwerking** van het [dashboard](dashboard.md) toont de indicator **Een noodzakelijke beoordeling**: het aantal verwerkingsactiviteiten dat volgens het gedefinieerde interval moet worden beoordeeld, en het aantal verwerkingsactiviteiten dat vers is.

## Meldingen

Wanneer een item verouderd raakt, ontvangen de maker ervan en de gebruikers die eraan zijn gekoppeld (bijvoorbeeld de eigenaars van een verwerkingsactiviteit) een e-mail: het item is al lange tijd niet beoordeeld en het is tijd om het te vernieuwen.
