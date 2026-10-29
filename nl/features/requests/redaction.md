---
description: >-
  Verberg gegevens in documenten die bij een verzoek van een betrokkene horen
  rechtstreeks in Dastra, met of zonder hulp van AI.
---

# Documenten verbergen

Bij de behandeling van een verzoek van een betrokkene moet u vaak documenten naar de aanvrager sturen: een kopie van een identiteitsbewijs, een contract, een rekeninghistorie, een klantdossier. Deze documenten bevatten bijna altijd vertrouwelijke informatie die niet mag worden bekendgemaakt: gegevens over derden, interne contractvoorwaarden, benoemde verwijzingen.

Dastra bevat een hulpmiddel om gegevens te verbergen in het verzoek zelf. De interface noemt het **Bestand verbergen**.

***

## Het hulpmiddel openen

Het hulpmiddel opent vanuit de bijlagen van het verzoek. Het accepteert PDF-, PNG- en JPEG-bestanden en hangt af van uw abonnement: de knop verschijnt niet als verbergen niet is inbegrepen.

1. Open in het menu **Verzoeken** het **Register van verzoeken** en open daarna het te behandelen verzoek.
2. Open in de sectie **Uitvoering van het verzoek** het tabblad **Bijlagen**. Upload het document indien nodig.
3. Klik op de bestandsrij op het pictogram **Gegevensverduistering**. U kunt ook het voorbeeld van het bestand openen en op **Gegevensverduistering** klikken.

De editor **Bestand verbergen** opent op het document.

<figure><img src="../../.gitbook/assets/dsr-request-processing-attachments.png" alt="Het tabblad Bijlagen van een verzoek, met de pictogrammen voor voorbeeld, verbergen, downloaden en verwijderen op de bestandsrij"><figcaption><p>De bijlagen van het verzoek, met het pictogram om te verbergen bij elk compatibel bestand</p></figcaption></figure>

***

## Handmatig verbergen

Teken met de muis op elke pagina de te verbergen gebieden. De editor toont het aantal verhullingen en biedt deze acties:

* **Verwijder de afscherming** verwijdert één gebied.
* **Laatste verberging ongedaan maken** gaat één gebied terug.
* **Verhullingen van de pagina wissen** en **Alle verduisteringen wissen** beginnen opnieuw met een schone pagina.
* De knoppen voor zoomen en pagina's maken lange documenten leesbaarder.

<figure><img src="../../.gitbook/assets/caviardage-manuel.gif" alt="De te verbergen gebieden van een document handmatig selecteren"><figcaption><p>Teken de te verbergen gebieden rechtstreeks op het document</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/requests-redaction-1.png" alt="De editor Bestand verbergen met het document, de verborgen gebieden in zwart en de werkbalk"><figcaption><p>De editor Bestand verbergen</p></figcaption></figure>

***

## Verbergen met AI

Klik in de editor op **Auto-redact with AI** om het venster **Automatische verdoezeling door IA** te openen. De AI analyseert het document, vindt persoonsgegevens van derden (namen, adressen, contactgegevens, identificatienummers) en plaatst gebieden om te verbergen. Er worden geen gegevens bewaard na de sessie.

Het venster biedt drie opties:

* **Uitsluiten van de informatie van de betrokken persoon van de verdoezeling**: standaard geselecteerd, zodat de eigen gegevens van de aanvrager leesbaar blijven.
* **Aangepaste instructie**: een aanvullende instructie, bijvoorbeeld ook alle bedrijfsnamen verbergen.
* **Extra uitdrukkingen om te verdoezelen**: maximaal 20 uitdrukkingen die overal waar ze voorkomen worden verborgen. Typ een uitdrukking en druk op Enter.

Klik daarna op **Auto-redact with AI**. De voorgestelde gebieden worden aan de editor toegevoegd: verwijder de gebieden die ten onrechte zijn gevonden en voeg de gebieden toe die de AI heeft gemist. De knop **Auto-redact with AI** verschijnt alleen als verbergen met AI in uw abonnement is inbegrepen.

<figure><img src="../../.gitbook/assets/requests-redaction-2.png" alt="Het venster Automatische verdoezeling door IA met de drie opties"><figcaption><p>De opties van automatisch verbergen met AI</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/caviardage-analyse-ia.gif" alt="AI-analyse van een document en automatische detectie van de gebieden met identificatiegegevens van derden"><figcaption><p>De AI analyseert het document en plaatst de gebieden die u daarna controleert</p></figcaption></figure>

{% hint style="warning" %}
Het AI-resultaat is een eerste voorstel, geen definitieve beslissing. Een bevoegde persoon moet elk gebied controleren en valideren voordat het document wordt verstuurd.
{% endhint %}

***

## Het afgeschermde bestand opslaan

Klik na de controle op **Sla het afgeschermde bestand op**. De knop blijft inactief tot er ten minste één gebied is getekend. De schakelaar **Verwijder het originele bestand**, standaard ingeschakeld, bepaalt wat er met het origineel gebeurt:

* Aan: het afgeschermde bestand vervangt het origineel definitief en het origineel wordt verwijderd.
* Uit: het afgeschermde bestand wordt als nieuwe bijlage toegevoegd, met het achtervoegsel `-redacted`, en het origineel blijft behouden.

Dastra vraagt u om bevestiging voordat het bestand wordt opgeslagen. Pagina's worden platgemaakt tot afbeeldingen: de verborgen tekst bestaat niet meer in het resulterende bestand en kan niet worden geëxtraheerd. Een afgeschermd bestand toont de indicator **Geëxtraheerde gegevens**, met het aantal verborgen gebieden.

{% hint style="info" %}
Een gewone ondoorzichtige rechthoek over een niet-platgemaakte PDF kan worden omzeild en is geen conforme redactie. Platmaken tot een afbeelding is de methode die gegevensbeschermingsautoriteiten aanbevelen.
{% endhint %}

***

## Aanbevelingen

* Controleer het afgeschermde document voordat u het verstuurt, om na te gaan dat er geen vertrouwelijke informatie zichtbaar is.
* Schakel **Verwijder het originele bestand** uit om het origineel in het verzoek te bewaren, bijvoorbeeld voor uw compliancedossier, tenzij uw intern beleid verwijdering vereist.
* Combineer bij lange of complexe documenten (contracten met meerdere pagina's, rekeningafschriften) detectie met AI met een handmatige controle per pagina.
