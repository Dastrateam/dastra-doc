---
description: >-
  De implementatiefase is de overgang van het theoretische kader naar de
  operationele uitvoering van conformiteit.
---

# Projectimplementatie

In deze fase configureert u de controles concreet, bepaalt u de verificatiemethoden en bereidt u het verzamelen van bewijs voor.

In dit stadium heeft het project al:

* zijn kaders,
* zijn controles,
* zijn tests en risico's, geïnitialiseerd tijdens de ontwerpfase.

***

## Doel van de fase

De implementatiefase heeft als doel om:

* te bepalen hoe de controles worden geverifieerd,
* de tests (handmatig of geautomatiseerd) te configureren,
* de risico's aan de controles te koppelen,
* het verzamelen van conformiteitsbewijs voor te bereiden.

***

## 1. De status van tests tijdens de implementatiefase begrijpen

Standaard hebben alle tests van het project de status **Ontbrekend bewijs**.

Dat betekent dat:

* de controle bestaat,
* de test is gedefinieerd,
* maar er nog geen bewijs is aangeleverd of verzameld.

Zolang het project zich niet in de monitoringfase bevindt, is het niet aanbevolen bewijs te wijzigen of te valideren.

<figure><img src="../../../.gitbook/assets/image-458.png" alt="Lijst van tests met de status Ontbrekend bewijs"><figcaption></figcaption></figure>

***

## 2. Conformiteitstests configureren

Elke controle kunt u verifiëren met een of meer tests.

{% columns %}
{% column %}
Met een test bepaalt u:

* een verificatieprocedure,
* een uitvoeringsfrequentie (bijvoorbeeld maandelijks, driemaandelijks, jaarlijks),
* een eigenaar van de test.

Tests kunnen zijn:

* handmatig, met een menselijke handeling en bewijs,
* of geautomatiseerd, via een Dastra-connector of een aangepaste connector.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-459.png" alt="Configuratie van een conformiteitstest"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## 3. Risico's koppelen en beoordelen

U kunt controles aan een of meer risico's koppelen om hun invloed op de risicovermindering te meten.

Voor elk risico kunt u:

* een initiële beoordeling vastleggen (waarschijnlijkheid × impact),
* een resterende beoordeling vastleggen, na toepassing van de controles,
* de risicobehandeling kiezen (vermindering, aanvaarding enzovoort).

Met deze aanpak ziet u concreet wat de controles voor de risicohouding betekenen.

<figure><img src="../../../.gitbook/assets/image-461.png" alt="Beoordeling van een risico met initiële en resterende waarden"><figcaption></figcaption></figure>

***

## 4. Bedreigingen, risico's en controles koppelen

Bedreigingen zijn de concrete scenario's die een risico kunnen doen ontstaan\
(bijvoorbeeld injectie van kwaadaardige gegevens, gebrek aan toezicht, exfiltratie van informatie).

Een bedreiging kan zijn:

* gekoppeld aan een of meer risico's,
* indirect gedekt door de ingevoerde controles.

Deze keten zorgt voor volledige traceerbaarheid:\
Bedreiging → Risico → Controle → Test → Bewijs

***

## 5. Een connector installeren om bewijs te automatiseren

Voor bepaalde tests kunt u een Dastra-connector installeren om het verzamelen van bewijs te automatiseren.

Met connectoren kunt u bijvoorbeeld:

* de aanwezigheid van een beleidsdocument of een contract controleren,
* een register bevragen (AI-systemen, incidenten, verwerkingsactiviteiten),
* terugkerende controles automatiseren zonder handmatige actie.

Elke connector wordt geconfigureerd met:

* een uitvoeringsfrequentie,
* verzamelparameters die op de test zijn afgestemd.

<figure><img src="../../../.gitbook/assets/image-462.png" alt="Configuratie van een connector voor een test"><figcaption></figcaption></figure>

***

## 6. Resultaat van de implementatiefase

Na de implementatiefase:

* zijn de controles geconfigureerd,
* zijn de tests klaar om te worden uitgevoerd,
* zijn de risico's beoordeeld en gekoppeld,
* zijn eventuele connectoren geïnstalleerd.

Het project is dan klaar voor de volgende fase: de monitoring. In die fase:

* worden de tests periodiek uitgevoerd,
* wordt het bewijs verzameld,
* wordt de conformiteit in de loop van de tijd gemeten.
