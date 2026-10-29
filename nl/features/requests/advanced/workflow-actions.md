# Extra acties in geautomatiseerde workflows

Workflowregels automatiseren bewerkingen in Dastra. Voor verzoeken van betrokkenen bieden ze specifieke acties die u instelt volgens uw eigen behandelregels. Open **Regels voor de workflow** in de instellingen voor de werkruimte en voeg daarna een actie toe aan een regel die op verzoeken van toepassing is.

<figure><img src="../../../.gitbook/assets/requests-workflow-actions-1.png" alt="De lijst met acties voor een workflowregel die op verzoeken van toepassing is"><figcaption><p>Acties die specifiek zijn voor verzoeken van betrokkenen</p></figcaption></figure>

## Acties die specifiek zijn voor verzoeken

* **Een verzoekbericht verzenden**: stuurt vanuit het verzoek een bericht naar de aanvrager, met vrije tekst of een sjabloon.
* **Het verzoek sluiten**: sluit het verzoek met een reden van sluiting en kan de sluitingsmelding naar de aanvrager versturen.
* **Het verzoek anonimiseren**: wist de identificerende gegevens van het verzoek. De actie is onomkeerbaar.
* **Verplaats naar prullenbak**: verplaatst het verzoek naar de prullenbak, waar daarna de [opschoonregels](purge.md) van toepassing zijn.

## Andere nuttige acties voor verzoeken

* **Een veld bewerken**: werkt een veld van het verzoek bij.
* **Voeg een taak toe**: maakt een taak aan, bijvoorbeeld om de functionaris voor gegevensbescherming (FG) het antwoord te laten valideren.
* **Een melding verzenden**: stuurt een melding over het verzoek naar personen.
* **Eigenaar definiëren**: stelt de eigenaar van het verzoek in.
* **Tag (s) toevoegen**: voegt tags toe aan het verzoek.
* **Een antwoord op een vragenlijst plannen**: plant een antwoord op een vragenlijst.
* **Send an HTTP request**: roept een externe dienst aan.
* **Execute an AI agent**: voert een AI-agent uit, afhankelijk van uw abonnement en uw rechten.

{% hint style="info" %}
Meer over workflows leest u bij [Workflow-regels](../../settings/workflow-rules.md).
{% endhint %}
