---
description: >-
  Met Dastra AI-agents bouwt u uw eigen gespecialiseerde chatassistenten en
  autonome agents die volgens een schema draaien
---

# Dastra AI-agents

Een Dastra AI-agent is een assistent die u zelf configureert: u geeft hem een rol, instructies en de lijst met hulpmiddelen die hij in uw werkruimte mag gebruiken. De standaard [AI-assistent](../README.md) beantwoordt alles, terwijl een agent gespecialiseerd is in één opdracht en zich altijd op dezelfde manier gedraagt.

U configureert agents via **Instellingen voor werkruimte** > **AI agents** ([directe toegang](https://app.dastra.eu/workspace/0/settings/ai-agents)).

<figure><img src="../../../../.gitbook/assets/ai-agents-liste.png" alt="Lijst met de Dastra AI-agents van een werkruimte"><figcaption><p>Instellingen voor werkruimte &#x3E; AI agents: de lijst met geconfigureerde agents</p></figcaption></figure>

{% hint style="warning" %}
Verwar dit niet met het register van AI-systemen. In het onderdeel [AI-systemen](../../../ai-systems/README.md) documenteert u uw eigen AI-systemen voor de AI-verordening. De agents die hier worden beschreven, zijn een Dastra-functie waarmee u met uw gegevens werkt.
{% endhint %}

***

## Twee soorten agents

| | Conversational Agent | Auto Agent |
| --- | --- | --- |
| Waarvoor | Een gespecialiseerde chatassistent met een eigen persoonlijkheid en eigen regels | Een terugkerende taak die zonder toezicht draait |
| Wat start hem | Een gebruiker, door een gesprek te openen | Een handmatige uitvoering, een schema of een workflowregel |
| Interactie | De agent kan vragen stellen en om bevestiging vragen | De agent kan geen vraag stellen en niet om bevestiging vragen: hij voert alles uit en geeft zijn resultaat terug |
| Waar u hem vindt | In het Dastra AI-paneel, via de keuzelijst **Choose an agent** | In **AI agents**, met de uitvoeringen in de **Inbox** |
| Wat u configureert | Welkomstbericht, assistentinstructie, gespreksstarters | Systeeminstructie, invoervelden, planning |

***

## Een agent aanmaken

Klik op **Create agent**. U kunt uit vijf beginpunten kiezen:

<figure><img src="../../../../.gitbook/assets/ai-agents-creation-modal.png" alt="Dialoogvenster voor het aanmaken van een agent met de vijf beginpunten"><figcaption><p>De vijf manieren om een agent aan te maken</p></figcaption></figure>

* **Generate with Dastra AI**: beschrijf de opdracht in een paar woorden en de assistent bouwt de agent samen met u op en slaat hem op zodra u akkoord gaat. Dit is de ingebouwde skill `/scaffold_agent`.
* **Conversational Agent**: begin met een leeg scherm voor een chatassistent. Zie [Een conversational agent aanmaken](conversational.md).
* **Auto Agent**: begin met een leeg scherm voor een uitvoering die op hulpmiddelen draait. Zie [Een autonome agent aanmaken](autonomous.md).
* **Dastra library**: begin met een kant-en-klaar sjabloon van het Dastra-team. Het sjabloon wordt als concept geïmporteerd: controleer de instructies en de hulpmiddelen voordat u het publiceert.
* **Import an agent**: laad een definitiebestand dat u eerder uit Dastra hebt geëxporteerd.

In alle gevallen verloopt het aanmaken in twee stappen: u kiest het type, geeft een naam (maximaal 120 tekens) en eventueel een beschrijving (maximaal 1000 tekens) op, en daarna opent de volledige editor.

{% hint style="info" %}
De editor slaat automatisch op: de tijd van de laatste opslag staat rechtsboven. Er is geen knop Opslaan.
{% endhint %}

***

## Publiceren, deactiveren, archiveren en verwijderen

* **Actief** of **Uitgeschakeld**: een uitgeschakelde agent verschijnt niet meer voor gebruikers en zijn schema's worden niet meer uitgevoerd. Gebruik deze status terwijl u de instructies nog verfijnt.
* Archiveren: de agent gaat naar de prullenbak. In het menu van de agent heet deze actie **Permanent verwijderen**, maar het is geen definitieve verwijdering. Vink in de lijst **Bekijk prullenbak** aan om de agent terug te vinden en te herstellen. De eerdere uitvoeringen blijven bewaard.
* **Verwijderen**: verwijderen is definitief en wist ook alle sessies en berichten van de agent. Gebruik dit wanneer u die gegevens moet wissen.

## Een agent exporteren en importeren

Met de knop **Exporteren** maakt u een JSON-bestand met de definitie van de agent (instructies, hulpmiddelen, invoervelden, planning). U importeert het in een andere werkruimte via **Create agent** > **Import an agent**.

Bij het importeren zet Dastra een aantal zaken terug: de agent wordt gedeactiveerd aangemaakt, zonder logo en zonder te notificeren gebruikers. Controleer hem en schakel hem daarna in.

***

## Wie wat mag doen

De toegang tot agents hangt af van uw abonnement en van uw machtigingen.

| Machtiging | Wat ze toestaat |
| --- | --- |
| AI Assistant usage | De gespreksassistent gebruiken: vragen stellen en de agent zijn hulpmiddelen met leesrechten laten gebruiken |
| AI Assistant edit mode | De assistent records laten aanmaken en bijwerken vanuit het gesprek |
| Custom AI agents execution | De agents van de werkruimte zien en uitvoeren |
| Custom AI agents management | De agents van de werkruimte aanmaken, bijwerken en verwijderen |

U stelt machtigingen in bij **Organisatie-instellingen** > **Rollen en machtigingen**. De [MCP-server](../mcp.md) valt onder een apart abonnement.

{% hint style="info" %}
Een agent heeft nooit meer rechten dan de persoon die hem start. Zijn hulpmiddelen werken met uw eigen machtigingen: heeft u geen toegang tot een record, dan heeft de agent die ook niet.
{% endhint %}

***

## Credits en verbruik

Elk bericht dat u naar een agent stuurt, kost 1 Dastra AI-credit, ongeacht hoeveel hulpmiddelen de agent daarna gebruikt om u te antwoorden. Een gesprek hervatten na een bevestigingsvraag kost niets extra.

Het maandelijkse quotum van uw organisatie en het verbruik ervan volgt u op bij **Organisatie-instellingen** > **Assistent IA**. Zodra het quotum is bereikt, worden gesprekken en uitvoeringen geweigerd en is de knop **Run** van een autonome agent uitgeschakeld.

Modelfamilies, hosting en de gegevens die naar de modellen worden gestuurd, staan beschreven in [Hoe het werkt](../how-it-works.md).

***

{% content-ref url="conversational.md" %}
[Een conversational agent aanmaken](conversational.md)
{% endcontent-ref %}

{% content-ref url="autonomous.md" %}
[Een autonome agent aanmaken](autonomous.md)
{% endcontent-ref %}

{% content-ref url="skills.md" %}
[Skills](skills.md)
{% endcontent-ref %}

{% content-ref url="inbox.md" %}
[Uitvoeringen volgen](inbox.md)
{% endcontent-ref %}
