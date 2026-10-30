---
description: >-
  Vier werkstroomregels voor Brightmoor Retail Group: nieuwe verzoeken toewijzen,
  taken in een team delen, Microsoft Teams waarschuwen bij een datalek met een
  hoog risico en een HTTP-verzoek versturen.
---

# Werkstroomrecepten

Elk recept is een [werkstroomregel](../features/settings/workflow-rules.md) van Brightmoor Retail Group: een trigger, voorwaarden en acties op één objecttype. Om er een aan te maken, opent u **Automations** > **Regels voor de workflow**, klikt u op **Een werkstroomregel maken**, kiest u **Vanaf nul** en voert u daarna de **Naam van de regel** en het **Soort element** in. Schakel de regel in met de schakelaar **Status** zodra ze is opgeslagen.

Laat **Voer de workflow slechts één keer per item uit (aanbevolen)** ingeschakeld voor de recepten die op een aanmaak of een wijziging reageren, zodat een item nooit twee keer wordt verwerkt.

## Recept 1: nieuwe verzoeken toewijzen

Doel: elk nieuw verzoek van een betrokkene heeft vanaf de eerste minuut een operator, afhankelijk van de dochteronderneming die het heeft ontvangen.

### Trigger

Objecttype: **Verzoek**. Trigger: **Actie**, gebeurtenis **Creatie**.

### Voorwaarden

Een regel heeft maximaal vijf voorwaarden en elke voorwaarde heeft haar eigen acties. Kies voor elk **Specificeer voorwaarden**:

| Voorwaarde | Veld | Waarde |
| --- | --- | --- |
| 1 | **Organisatie-eenheid** | Brightmoor Germany |
| 2 | **Organisatie-eenheid** | Brightmoor UK |
| 3 | **Organisatie-eenheid** | Brightmoor Retail Group |

Een verzoek heeft geen landveld. De organisatorische eenheid van het verzoek vervangt gewoonlijk het land van een dochteronderneming. Om op taal te routeren, gebruikt u in plaats daarvan het veld **Language**, en om op uitgeoefend recht te routeren, het veld **Rights of the data subject** (bijvoorbeeld Erasure).

### Acties

Klik in elke voorwaarde op **+** en kies **Eigenaar definiëren** en selecteer daarna een gebruiker: Sophie Becker voor voorwaarde 1, Liam O'Connor voor voorwaarde 2 en Emma Walsh voor voorwaarde 3. Op een verzoek vult deze actie de **Operator** in.

### Resultaat

Een verzoek dat de Duitse dochteronderneming ontvangt, wordt aan Sophie Becker toegewezen zodra het wordt aangemaakt. In de regel toont **Historiek** elk verwerkt verzoek met zijn status en past **Ren** de regel met de hand toe op een verzoek dat vóór de regel is aangemaakt.

## Recept 2: taken in een team delen

Doel: de nieuwe taken gelijkmatig verdelen over de leden van de privacydesk.

### Trigger

Objecttype: **Taak**. Trigger: **Actie**, gebeurtenis **Creatie**.

### Voorwaarden

**Geldt voor alle elementen**: elke nieuwe taak is betrokken. Om de regel te beperken, kiest u **Specificeer voorwaarden** en filtert u op een veld zoals een label.

### Acties

Voeg **Eigenaar definiëren** toe, kies **Selecteer een gebruiker in het team** en selecteer het team bij **Selecteer een team**. Een gebruiker wordt uit het team gekozen volgens het round-robinmodel: telkens wanneer de regel wordt uitgevoerd, wordt het volgende lid gekozen, en het eerste lid volgt op het laatste.

<figure><img src="../.gitbook/assets/examples-workflow-1.png" alt="Ontwerper van de werkstroomregel met de actie Eigenaar definiëren ingesteld om een gebruiker uit een team te kiezen"><figcaption><p>De round-robintoewijzing</p></figcaption></figure>

### Resultaat

De eerste taak gaat naar het eerste lid van het team, de tweede taak naar het volgende, enzovoort. Het gekozen lid staat in **Toegewezen aan**. Zie [Teams aanmaken en toewijzen](../getting-started/setup/teams.md) om het team aan te maken. Heeft het team geen leden, dan mislukt de uitvoering en verschijnt ze als fout in de historiek.

## Recept 3: een Microsoft Teams-kanaal waarschuwen bij een datalek met een hoog risico

Doel: het privacykanaal meteen waarschuwen wanneer een datalek het niveau Hoog risico bereikt, omdat de toezichthoudende autoriteit en de betrokkenen dan moeten worden geïnformeerd.

Vereiste: de [Microsoft Teams-integratie](../features/integrations/microsoft-teams.md) is geïnstalleerd en ingeschakeld in de werkruimte. Zonder die integratie wordt de actie niet aangeboden.

### Trigger

Objecttype: **Datalek**. Trigger: **Actie**, gebeurtenis **Aanmaken of bewerken**: het risiconiveau bestaat pas zodra de risicoanalyse is ingevuld, na het aanmaken.

### Voorwaarden

Kies **Specificeer voorwaarden** en stel het veld **Punten** in op een waarde groter dan of gelijk aan 6. **Punten** is de score van het datalek, de som van de twee scores van de risicoanalyse, en 6 is de drempel van het niveau Hoog risico (zie [Risicoscores](risk-scoring.md)). Het veld **Risico** zelf wordt niet aangeboden in voorwaarden.

{% hint style="info" %}
Een datalek waarvan het niveau met de hand is ingesteld bij **Conclusie van de risicoanalyse: geschat risiconiveau**, behoudt zijn score, dus de regel volgt de score en niet het niveau dat u hebt gekozen.
{% endhint %}

### Acties

Voeg **Stuur een Teams-notificatie** toe en vul in:

* **Titel van de kaart**: `High risk data breach: {{label}}`;
* **Bericht**: `Score {{score}}. Check the notification deadline to the supervisory authority.`;
* **Een link naar het object in de kaart opnemen**: ingeschakeld, wat de standaardwaarde is.

Typ `{{` in een veld om de variabelen van het datalek te tonen.

### Resultaat

Er verschijnt een kaart in het Teams-kanaal dat aan de webhook is gekoppeld, met een link naar het datalek. Er is geen ontvanger te kiezen: het kanaal is dat van de integratie. Deze actie kan niet worden geprobeerd zonder Teams-kanaal, daarom heeft dit recept geen schermafbeelding.

## Recept 4: een HTTP-verzoek versturen

Doel: telkens wanneer een verzoek binnenkomt, een ticket aanmaken in de servicedesk van Brightmoor.

Vereiste: de integratie [HTTP / Custom API](../features/integrations/custom-http.md) is ingeschakeld in **Instellingen voor werkruimte** > **Integraties**, met een verbinding met de servicedesk (API-sleutel, basisinloggegevens of OAuth 2.0). Voor het toevoegen van deze actie is de machtiging **Integraties** nodig.

### Trigger

Objecttype: **Verzoek**. Trigger: **Actie**, gebeurtenis **Creatie**.

### Voorwaarden

**Geldt voor alle elementen**.

### Acties

Voeg **Send an HTTP request** toe en vul in:

* **Method**: POST. **URL**: `https://servicedesk.brightmoor.example/api/tickets`.
* Tabblad **Authentication**: de verbinding van de servicedesk. De inloggegevens blijven op de verbinding staan, nooit in de regel.
* Tabblad **Body**: het formaat **JSON**, met dit sjabloon:

```
{
  "summary": "{{title}}",
  "reference": "{{refId}}",
  "origin": "Dastra"
}
```

Klik op **Test the request**. **Preview** toont de URL, de headers en de body voor een echt verzoek van de werkruimte zonder iets te versturen. **Send the request** voert de echte aanroep uit en toont het antwoord van de servicedesk. **Genereren met de IA** stelt het verzoek op op basis van een instructie en de payload die de servicedesk verwacht.

<figure><img src="../.gitbook/assets/examples-workflow-2.png" alt="Actie Send an HTTP request met de methode POST, de URL en de JSON-body"><figcaption><p>De actie HTTP-verzoek</p></figcaption></figure>

### Resultaat

De servicedesk ontvangt een ticket voor elk nieuw verzoek. De gerenderde body moet geldige JSON zijn: anders wordt niets verstuurd en wordt de uitvoering als fout gelogd. Elke aanroep wordt getraceerd in de integratielogboeken. Het uitschakelen van de integratie of het verwijderen van de verbinding schakelt de regel uit.
