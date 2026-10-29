---
description: >-
  Vind de geschiedenis van de uitvoeringen van uw agents terug, hun status en
  het detail van wat ze hebben gedaan
---

# Uitvoeringen volgen

De **Inbox** verzamelt de uitvoeringsgeschiedenis van uw agents: wat is gestart, waardoor, wanneer en met welk resultaat.

U vindt hem via **Instellingen voor werkruimte** > **AI agents** > **Inbox**.

<figure><img src="../../../../.gitbook/assets/ai-agents-inbox.png" alt="Inbox met de uitvoeringen van agents"><figcaption><p>De Inbox, met de status en de bron van elke uitvoering</p></figcaption></figure>

Elke rij toont de **Session**, de **Status**, de **Source** (Manual, Schedule of Workflow), het tijdstip van de start (**Started**) en dat van de voltooiing (**Completed**). Met de keuzelijst boven de lijst beperkt u de weergave tot één agent.

Lopende uitvoeringen worden live bijgewerkt: u hoeft de pagina niet te vernieuwen.

***

## Het detail van een uitvoering

Klik op een rij om het detail te openen. Het heeft twee tabbladen:

* **Conversation**: het volledige spoor, met de redenering van de agent, de hulpmiddelen die hij heeft aangeroepen en zijn eindantwoord.
* **Inputs**: de waarden van de invoervelden waarmee de uitvoering is gestart.

<figure><img src="../../../../.gitbook/assets/ai-agents-inbox-detail.png" alt="Detail van een uitvoering van een agent"><figcaption><p>Het detail van een uitvoering</p></figcaption></figure>

Met de knop **Continue in chat** neemt u het resultaat van de uitvoering mee naar een nieuw gesprek. Zo verdiept u zich het gemakkelijkst in een resultaat, vraagt u om een herschrijving of laat u iets corrigeren.

***

## Statussen

Sommige statussen zijn technisch, andere worden door de agent zelf aan het einde van zijn werk gemeld: dat zijn conclusies, geen mislukkingen.

| Status | Betekenis |
| --- | --- |
| **Running** | De uitvoering is bezig |
| **Completed** | De agent heeft zijn opdracht volledig doorlopen |
| **Failed** | Een technische fout heeft de uitvoering onderbroken; de foutmelding staat in het detail |
| **Human review required** | De agent heeft zijn werk gedaan, maar vindt dat een validatie nodig is voordat het verdergaat |
| **Insufficient permission** | De agent had niet de rechten om bepaalde gegevens te bereiken of een actie uit te voeren |
| **Feature required** | Een functie die hij nodig had, zit niet in het abonnement van de organisatie |
| **Missing information** | De beschikbare gegevens lieten niet toe de opdracht te voltooien |
| **Incomplete execution** | De agent bereikte de limiet van hulpmiddeliteraties voordat hij kon afronden |
| **Context limit reached** | Het gesprek werd te lang voor het model |

{% hint style="info" %}
Een status **Missing information** of **Human review required** verwijst meestal terug naar de instructie van de agent of zijn lijst met hulpmiddelen: hij deed wat hij kon met wat hij kreeg. Het detail van de uitvoering legt doorgaans uit wat hij miste.
{% endhint %}

***

## Notificaties

Bent u een van de te notificeren gebruikers (**Notified users**) van een agent, dan ontvangt u aan het einde van elke uitvoering, geslaagd of mislukt, een Dastra-notificatie. Zo houdt u een geplande agent in de gaten zonder de Inbox te openen.

## Technisch logboek

Voor monitoring op organisatieniveau (gebruikt model, duur, gebruiker achter de aanroep) raadpleegt u de aanroeplogboeken van de AI-assistent bij **Organisatie-instellingen** > **Assistent IA**. Ze worden 90 dagen bewaard.
