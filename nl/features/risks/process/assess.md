---
description: >-
  Leer hoe u risico's beoordeelt in Dastra.
---

# 2. Beoordelen

Beoordeel het risico op basis van de elementen die in het risicotype zijn geïdentificeerd en van de context van het object. De beoordeling steunt op waarschijnlijkheid en impact. De app noemt ze **Waarschijnlijkheid** en **Ernst**.

Open op de risicopagina het onderdeel **Risicobeoordeling**. Kies de waarschijnlijkheid en de ernst van het initiële risico en daarna die van het restrisico. Bevat het risicotype een voorbeoordeling, dan zijn deze waarden al ingevuld. Het veld **Reden voor evaluatie** bewaart een spoor van uw redenering.

<figure><img src="../../../.gitbook/assets/risks-assess-1.png" alt="Onderdeel Risicobeoordeling: initiële en resterende niveaus, motivering en risicomatrix"><figcaption><p>Het onderdeel Risicobeoordeling en de matrix ervan</p></figcaption></figure>

Klik op **De beoordeling valideren** om het risico naar de stap **Verwerkingen** te brengen. Alleen de eigenaar van het risico kan dit doen. De knop **Ga terug naar deze stap** brengt het risico één stap terug.

## De risicoschaal bepalen

Om een risico te beoordelen, plaatst u deze twee waarden op een schaal: de risicoschaal. Ze is doorgaans gebaseerd op 5 niveaus. In Frankrijk gebruikt de Ebios-methode (onder meer gepromoot door de CNIL en de ANSSI) een schaal met 4 niveaus.

Bepaal voor elk niveau een toepassingsvoorwaarde. De schaal kan overeenkomen met een geldbedrag, bijvoorbeeld voor de impact.

<figure><img src="../../../.gitbook/assets/risk-default-heatmap-matrix.png" alt="Standaard risicoschaal: matrix van 5 ernstniveaus en 5 waarschijnlijkheidsniveaus"><figcaption><p>De standaard risicoschaal</p></figcaption></figure>

### De risicoschaal configureren

De schaal is aanpasbaar. Ze wordt per werkruimte gedefinieerd, in **Instellingen voor werkruimte** > **Risicobeheer**, onder **Proces**. Dit menu-item is zichtbaar met schrijftoegang tot risico's; het aanmaken, opslaan of activeren van een schaal vereist ook schrijftoegang tot de geavanceerde instellingen.

<figure><img src="../../../.gitbook/assets/risks-assess-2.png" alt="Instellingenpagina van risicobeheer: standaardschaal en knop Maak een aangepaste schaal"><figcaption><p>De risicoschalen van de werkruimte</p></figcaption></figure>

De standaardschaal, **Standaard risico-schaal** (5 niveaus), is alleen-lezen. Om een andere te gebruiken:

1. Klik op **Maak een aangepaste schaal**.
2. Geef de schaal een naam en kies een **Risico-schaalmodel**: **5 niveaus - standaard**, **4 niveaus - CNIL PIA** of **3 niveaus - licht**.
3. Open de nieuwe schaal. Klik op een graduatie van waarschijnlijkheid of ernst om het label, de beschrijving en de waarde ervan te bewerken: standaard een bedrag in euro voor de ernst en een percentage voor de waarschijnlijkheid. Met de plus- en de prullenbakknop voegt u een niveau toe of verwijdert u het, van 1 tot 9 niveaus.
4. Wijzig indien nodig de eenheden (**Maateenheid impact**, **Waarschijnlijkheidseenheid**) en de kleur van elke cel van de matrix.
5. Klik op **Opslaan** en daarna op **Activeer dit raster** om de schaal te gebruiken.

{% hint style="warning" %}
Het activeren van een andere schaal wanneer er al risico's bestaan, heeft ernstige gevolgen voor de risicostatistieken: de app vraagt om een bevestiging voordat het profiel wordt geactiveerd.
{% endhint %}

De score van een risico is het product van de ernst en de waarschijnlijkheid ervan. De maximumscore van een schaal is het product van de twee hoogste niveaus: 25 met de schaal van 5 niveaus, 16 met de schaal van 4 niveaus en 9 met de schaal van 3 niveaus. De percentages in Dastra drukken een score uit ten opzichte van dit maximum.

Voor een berekening stap voor stap, op de standaardschaal en op de CNIL-schaal, zie [Risicoscores](../../../examples/risk-scoring.md).

## Waarschijnlijkheid (kans)

De waarschijnlijkheid is een evaluatie van de frequentie waarmee een risico zich voordoet. Het is een empirisch geëvalueerde score (traditioneel op 5). Elk niveau kan overeenkomen met een frequentie van optreden van het risico en dus van de bedreiging.

## Impact (ernst)

De impact is de evaluatie van het gevolg van een gevreesde gebeurtenis voor de organisatie. Het is de ernst van dit gevolg die wordt ingeschat.

Naargelang het beoordeelde risico varieert de impact. U kunt hem empirisch inschatten, bijvoorbeeld door de kosten van een datalek of van de onbeschikbaarheid van gegevens na een cyberaanval te schatten.

### Het logboek van gebeurtenissen gebruiken

Het **Logboek** bewaart het geheugen van eerdere gebeurtenissen. Om een gebeurtenis toe te voegen, opent u **Risicobeheer** > **Tijdschrift** en klikt u op **Creëer een evenement**. Vul de naam in, de **Datum van het evenement**, de **Financiële gevolgen van het incident** en, indien mogelijk, het betrokken risicotype.

<figure><img src="../../../.gitbook/assets/risks-assess-3.png" alt="Logboek met drie gebeurtenissen, hun datum en hun financiële gevolgen"><figcaption><p>Het logboek van gebeurtenissen</p></figcaption></figure>

Voor een risico waarvan het type aan gebeurtenissen is gekoppeld, toont het onderdeel **Risicobeoordeling** hun frequentie per jaar en per maand en hun minimale, gemiddelde en maximale financiële impact. Deze cijfers helpen u een realistische waarschijnlijkheid en ernst te kiezen.

{% hint style="info" %}
Bij risico's voor personen (bijvoorbeeld onder de AVG) is de impact de schade die de betrokkenen lijden en de inbreuk op hun rechten en vrijheden: discriminatie, weigering van een contract, ongemak.
{% endhint %}

## Een model voor de effectbeoordeling inzake privacy

Een beoordeling is altijd contextueel. De methodologie die de CNIL heeft gepubliceerd voor het uitvoeren van gegevensbeschermingseffectbeoordelingen (DPIA's) biedt echter een raster om de risicoschaal te lezen. Hieronder staat de tabel die de CNIL voorstelt in haar gids over effectbeoordelingen.

### Ernst

<table data-view="cards" data-full-width="true"><thead><tr><th>Niveaus</th><th>Generieke beschrijvingen van de impact (direct en indirect)</th><th>Voorbeelden van fysieke impact</th><th>Voorbeelden van materiële impact</th><th>Voorbeelden van morele impact</th></tr></thead><tbody><tr><td>1. Verwaarloosbaar</td><td>De betrokkenen ondervinden geen gevolgen of hebben enig ongemak, dat ze zonder moeite te boven komen.</td><td>Gebrek aan passende zorg voor een niet-zelfstandige persoon (minderjarige, persoon onder voogdij); voorbijgaande hoofdpijn.</td><td>Verloren tijd om procedures te herhalen of te wachten tot ze zijn afgerond; ontvangst van ongevraagde post (spam); hergebruik van gegevens die op websites zijn gepubliceerd voor gerichte reclame (informatie van sociale netwerken die wordt hergebruikt voor een postmailing); gerichte reclame voor alledaagse consumptieproducten.</td><td>Eenvoudige irritatie over ontvangen of gevraagde informatie; angst de controle over zijn gegevens te verliezen; gevoel van inbreuk op de privacy zonder reële of objectieve schade (commerciële indringing); tijdverlies bij het instellen van zijn gegevens; niet-naleving van de vrijheid om online te komen en te gaan door weigering van toegang tot een commerciële site (alcohol, wegens een onjuiste leeftijd).</td></tr><tr><td>2. Beperkt</td><td>De betrokkenen kunnen aanzienlijk ongemak ondervinden, dat ze ondanks enkele moeilijkheden te boven kunnen komen.</td><td>Lichte lichamelijke kwaal (goedaardige ziekte door niet-naleving van contra-indicaties); gebrek aan zorg die minimale maar reële schade veroorzaakt (handicap); laster die aanleiding geeft tot fysieke of psychologische represailles.</td><td>Niet-geplande betalingen (per vergissing opgelegde boetes), extra kosten (bankkosten, juridische kosten), wanbetaling; weigering van toegang tot administratieve of commerciële diensten; gemiste kansen op comfort (annulering van vrijetijdsactiviteiten, aankopen, vakanties, sluiting van een online account); gemiste professionele promotie; geblokkeerd account voor onlinediensten (spelletjes, administratie); ontvangst van ongevraagde gerichte post die de reputatie van de betrokkenen kan schaden; hogere kosten (hogere verzekeringsprijs); verwerking van onjuiste gegevens die storingen in rekeningen veroorzaakt (bank, klant, sociale zekerheid); gerichte onlinereclame over een privéaspect dat de persoon vertrouwelijk wilde houden (zwangerschap, farmaceutische behandeling); onjuiste of onrechtmatige profilering.</td><td>Weigering om informatiesystemen te blijven gebruiken (klokkenluiden, sociale netwerken); lichte maar objectieve psychologische schade (laster, reputatie); relatieproblemen met persoonlijke of professionele contacten (imago, bezoedelde reputatie, verlies van erkenning); gevoel van inbreuk op de privacy zonder onherstelbare schade; intimidatie op sociale netwerken.</td></tr><tr><td>3. Belangrijk</td><td>De betrokkenen kunnen aanzienlijke gevolgen ondervinden, die ze zouden moeten kunnen overwinnen, maar met reële en grote moeilijkheden.</td><td>Ernstige lichamelijke toestand die langdurige schade veroorzaakt (verslechtering van de gezondheid door slechte behandeling of niet-naleving van contra-indicaties); aantasting van de lichamelijke integriteit, bijvoorbeeld na een aanval, een ongeval in huis of een arbeidsongeval.</td><td>Niet-vergoede verduistering; niet-tijdelijke financiële moeilijkheden (verplichting een lening af te sluiten); gerichte, eenmalige, niet-terugkerende gemiste kansen (hypothecaire lening, weigering van studies, stages of banen, examenverbod); bankverbod; schade aan goederen; verlies van de woning; verlies van de baan; scheiding of echtscheiding; financieel verlies na oplichting (phishing); geblokkeerd in het buitenland; verlies van klantgegevens.</td><td>Ernstige psychologische toestand (depressie, ontwikkeling van een fobie); gevoel van inbreuk op de privacy en onherstelbare schade; gevoel van kwetsbaarheid na een dagvaarding; gevoel van schending van de grondrechten (discriminatie, vrijheid van meningsuiting); slachtoffer van afpersing; cyberpesten en mobbing.</td></tr><tr><td>4. Maximaal</td><td>De betrokkenen kunnen aanzienlijke, zelfs onherstelbare gevolgen ondervinden die ze mogelijk niet te boven kunnen komen.</td><td>Langdurige of blijvende lichamelijke kwaal (na niet-naleving van een contra-indicatie); overlijden (moord, zelfmoord, dodelijk ongeval); blijvende aantasting van de lichamelijke integriteit.</td><td>Financieel gevaar; aanzienlijke schulden; arbeidsongeschiktheid; onmogelijkheid te verhuizen; verlies van bewijsmateriaal in een geschil; verlies van toegang tot vitale infrastructuur (water, elektriciteit).</td><td>Langdurige of blijvende psychologische toestand; strafrechtelijke sanctie; ontvoering; verlies van familiebanden; onmogelijkheid juridische stappen te ondernemen; wijziging van de administratieve status en/of verlies van juridische autonomie (voogdij).</td></tr></tbody></table>

Houd bij deze schaal rekening met de volgende contextuele elementen:

* het identificerende karakter van de gegevens;
* de aard van de risicobronnen;
* het aantal koppelingen, met name met andere landen;
* het aantal ontvangers, waardoor het gemakkelijker wordt gegevens te correleren die aanvankelijk gescheiden waren.

### Waarschijnlijkheid

Om de waarschijnlijkheid te beoordelen, stelt de CNIL de volgende schaal voor:

| Niveaus | Beschrijving |
| --- | --- |
| Verwaarloosbaar | Het lijkt niet mogelijk dat de gekozen risicobronnen de bedreiging uitvoeren door te steunen op de kenmerken van de dragers (bijvoorbeeld diefstal van papieren dragers die zijn opgeslagen in de lokalen van een organisatie waarvan de toegang wordt gecontroleerd met een badge en een toegangscode). |
| Beperkt | Het lijkt moeilijk dat de gekozen risicobronnen de bedreiging uitvoeren door te steunen op de kenmerken van de dragers (bijvoorbeeld diefstal van papieren dragers die zijn opgeslagen in de lokalen van een organisatie waarvan de toegang wordt gecontroleerd met een badge). |
| Belangrijk | Het lijkt mogelijk dat de gekozen risicobronnen de bedreiging uitvoeren door te steunen op de kenmerken van de dragers (bijvoorbeeld diefstal van papieren dragers die zijn opgeslagen in de kantoren van een organisatie waarvan de toegang wordt gecontroleerd door een receptionist). |
| Maximaal | Het lijkt uiterst gemakkelijk dat de gekozen risicobronnen de bedreiging uitvoeren door te steunen op de kenmerken van de dragers (bijvoorbeeld diefstal van papieren dragers die zijn opgeslagen in de openbare hal van de organisatie). |

Houd bij deze schaal rekening met de volgende contextuele elementen:

* of het systeem openstaat voor het internet of gesloten is;
* of er al dan niet gegevens worden uitgewisseld met andere landen;
* koppelingen met andere systemen, of geen;
* heterogeniteit of homogeniteit van het systeem;
* variabiliteit of stabiliteit van het systeem;
* het imago van de organisatie.
