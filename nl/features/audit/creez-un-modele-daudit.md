---
description: Leer hoe je een auditmodel of een PIA maakt en aanpast met Dastra.
---

# Een auditmodel of PIA maken of wijzigen

## Introductie

Het aanmaken of wijzigen van een audit template of PIA in Dastra is eenvoudig. Ga hiervoor naar de "Audit" functionaliteit.



## Een auditsjabloon of PIA maken of wijzigen

Om een audit of PIA sjabloon te maken, klik je op de "Maak een sjabloon" knop in de "Audit" tab. Vervolgens kun je een van de 3 soorten auditsjablonen selecteren die in Dastra bestaan: geautomatiseerde, gecombineerde of aangepaste audit.

<figure><img src="../../.gitbook/assets/image (16) (3).png" alt=""><figcaption></figcaption></figure>

Dit brengt je naar de sjabloontype selectie interface:&#x20;

[Template type selectie](<../../.gitbook/assets/image (138).png>)

* Door te klikken op de "**Geautomatiseerde audit**" tab, kun je een bestaand voorgedefinieerd audit sjabloon kiezen uit de Dastra audit bibliotheek.
* Door op "**Gecombineerde audit**" te klikken, kun je verschillende audits combineren tot één audit.
* Door op "**Aangepaste audit**" te klikken, kun je je eigen auditmodel bouwen.

{% hint style="info" %}
In tegenstelling tot geautomatiseerde audits zijn aangepaste audits volledig aanpasbaar. Op basis van de antwoorden die respondenten hebben geselecteerd, kun je automatisch een actieplan genereren of de risico's van het model in kaart brengen;
{% endhint %}

## Een DPIA sjabloon maken

PIA sjablonen zijn opgenomen in de geautomatiseerde audit sjablonen en zijn vrij toegankelijk vanuit de Dastra bibliotheek.  Om een PIA sjabloon aan te maken of te wijzigen, klik op "Geautomatiseerde audit", selecteer dan "PIA (CNIL) - privacy effectbeoordeling" voordat je op "Opslaan" klikt.

{% hint style="info" %}
In Dastra zijn PIA's één van de **modellen voor geautomatiseerde audits**.
{% endhint %}

[Bibliotheek selectie knop](<../../.gitbook/assets/Capture web_6-5-2022_103438_app.dastra.eu.jpeg>)

[PIA model] (<../../.gitbook/assets/Capture web\_6-5-2022\_10342_app.dastra.eu.jpeg>)

Als je de sjabloon hebt geselecteerd, kom je in het planningsscherm waar je één van de 2 onderstaande acties kunt uitvoeren:

* ofwel **het sjabloon wijzigen** door te klikken op de knop "Sjabloon wijzigen
* een audit plannen door op de knop "Een audit plannen"&#x20. te klikken;

{% hint style="info" %}
Voor PIA's is een extra optie beschikbaar, indien gewenst:  **importeer uw PIA vanuit de CNIL-tool**. Klik hiervoor op de knop "Importeer uw CNIL PIA" &#x20;

Het is mogelijk om een door de CNIL-tool geproduceerde PIA te importeren. U moet de CNIL PIA in .json formaat uitpakken om deze in Dastra te importeren &#x20;

De meeste elementen zullen worden opgenomen in de Dastra PIA.
{% endhint %}

[Knoppen ](<../../.gitbook/assets/image (216).png>)

## Geautomatiseerde audit sjablonen

Dastra biedt een aantal geautomatiseerde auditsjablonen voor het documenteren van nalevings- en controleprocessen&#x20;

Zo zijn er bijvoorbeeld sjablonen voor de beoordeling van legitieme belangen (LIA) en doorgift uit de EU (TIA) beschikbaar in de applicatie &#x20;

## Aangepaste auditsjablonen

In Dastra kunt u uw eigen gepersonaliseerde auditsjabloon maken. Klik hiervoor op de optie "Aangepaste audit". Dit brengt je naar de interface voor het bewerken van auditsjablonen &#x20;

Stel de gewenste auditsjabloon samen en klik op "Opslaan en doorgaan".

Voorbeeld van een aanpasbaar audit sjabloon (<../../.gitbook/assets/Capture web_6-5-2022_103818_app.dastra.eu.jpeg>)

### Gecontroleerde elementen

Je kunt audits koppelen aan elementen in Dastra. Door het type element te kiezen dat geaudit wordt, forceer je dat alle audit antwoorden gebaseerd op dit model gekoppeld worden aan een object van het gekozen type. Je kunt er bijvoorbeeld voor kiezen dat dit audittemplate altijd wordt gekoppeld aan een Verwerking.&#x20;

<figure><img src="../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

Je kunt ervoor kiezen om een audit niet aan een bepaald object te binden. In dat geval wordt het antwoord altijd gekoppeld aan een organisatorische eenheid. Dit kan bijvoorbeeld het geval zijn voor wereldwijde nalevingsaudits.&#x20;

### Sjabloontypes&#x20;

Als je een aangepaste sjabloon maakt, moet je een sjabloontype kiezen.

<figure><img src="../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

Deze typen staan enige aanpassing van audit modellen toe.

* Standaard audit**: dit is een standaard vragenlijst.
* Nalevingsaudit**: momenteel een standaardvragenlijst.
* Effectbeoordeling**: dit auditmodel geeft een risicomatrix weer (met de vereiste configuratie) en wordt opgeroepen tijdens de PIA-fase van een Verwerking.
* Subcontractor audit**: dit auditmodel wordt opgeroepen tijdens de Recipient Subcontractor fase van een verwerkingsoperatie.
* Transfer Impact Assessment (TIA)**: een audit om de risico's met betrekking tot de doorgifte van gegevens buiten de EU te analyseren.
* Register Audit Rechtsgrondslag (LIA)**: controle van de rechtsgrondslag van legitieme belangen om ervoor te zorgen dat de belangen niet zwaarder wegen dan de rechten en vrijheden van betrokkenen.
* Trainingsvragenlijst**: vragenlijst die wordt gebruikt om trainingsquizzen te maken. Dit type vragenlijst maakt het mogelijk om een juist antwoord te selecteren uit de antwoorden en de juiste antwoorden weer te geven aan het einde van de vragenlijst.

## Gecombineerde auditsjablonen

In Dastra kun je verschillende bestaande auditsjablonen combineren tot één audit. Om dit te doen, selecteer je de optie "Gecombineerde audit" en volg je de stappen.

## Een bestaand auditsjabloon laden

Tot slot kun je een van je audit sjablonen in json formaat importeren. Om dit te doen, selecteer je bij het aanmaken van de audit de optie "Een sjabloon laden" &#x20;

## Om verder te gaan

{% content-ref url="planifier-un-audit.md" %}
[plan-an-audit.md](planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="rapport-daudit.md" %}
[audit-report.md](audit-report.md)
{% endcontent-ref %}

{% content-ref url="supprimer-un-audit-ou-un-modele-daudit.md" %}
[audit-report.md](supprimer-un-audit-ou-un-modele-daudit.md)
{% endcontent-ref %}