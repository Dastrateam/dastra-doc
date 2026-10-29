---
description: Leer hoe u dubbele of vergelijkbare verwerkingsactiviteiten samenvoegt tot één verwerkingsactiviteit.
---

# Verwerkingsactiviteiten samenvoegen

## Inleiding

Met samenvoegen combineert u meerdere verwerkingsactiviteiten tot één, waarbij u de informatie die u kiest en de eraan gekoppelde items behoudt. Het is vooral nuttig om uw verwerkingsregister te stroomlijnen, duplicaten te verwijderen en uw documentatie consistent te houden.

Eén van de verwerkingsactiviteiten blijft behouden als referentieversie: u kiest veld per veld de waarden die u uit de andere overneemt, waarna de andere worden verwijderd.

Voor samenvoegen is schrijftoegang tot het verwerkingsregister vereist. Zijn taakbeheer, risicobeheer of vragenlijsten ingeschakeld in uw werkruimte, dan hebt u ook schrijftoegang tot die modules nodig, zodat de gekoppelde items naar de referentieversie kunnen worden verplaatst.

## Een samenvoeging starten

U kunt een samenvoeging op drie plaatsen starten:

* Vanuit de lijst, voor meerdere verwerkingsactiviteiten: selecteer de samen te voegen verwerkingsactiviteiten (minder dan 30), klik op **Kies een bulkactie** en daarna op **Samenvoegen**. De vergelijking opent meteen.
* Vanuit de lijst, voor één verwerkingsactiviteit: open het actiemenu aan het einde van de rij en klik op **Samenvoegen**.
* Vanuit het dossier van een verwerkingsactiviteit: klik op de pijl naast de knop **Opslaan** en daarna op **Samenvoegen**.

<figure><img src="../../.gitbook/assets/ropa-merge-1.png" alt="Optie Samenvoegen in het actiemenu van een verwerkingsactiviteit"><figcaption><p>De optie Samenvoegen in het actiemenu van een verwerkingsactiviteit</p></figcaption></figure>

Start u vanuit één verwerkingsactiviteit, dan vraagt het venster **Samenvoeggereedschap** eerst met welke verwerkingsactiviteiten u ze wilt samenvoegen: selecteer ze bij **Selecteer de objecten waarmee je gegevens wilt samenvoegen** en klik op **Volgende**.

<figure><img src="../../.gitbook/assets/ropa-merge-2.png" alt="Selectie van de verwerkingsactiviteiten om mee samen te voegen"><figcaption><p>De verwerkingsactiviteiten selecteren waarmee u samenvoegt</p></figcaption></figure>

## De te behouden waarden kiezen

Het venster **Samenvoeggereedschap** vergelijkt de verwerkingsactiviteiten naast elkaar, met één kolom per verwerkingsactiviteit.

1. Vink in de kop van haar kolom de te behouden verwerkingsactiviteit aan: ze wordt de **Reference version**. Ze behoudt haar identificatie en haar geschiedenis. De andere kolommen tonen het label **Keep selected fields**: deze verwerkingsactiviteiten worden verwijderd zodra de samenvoeging is bevestigd, en alleen de velden die u erin selecteert, worden overgenomen in de referentieversie.
2. Selecteer voor elk veld met één waarde de kolom waarvan u de waarde wilt behouden.
3. Vink voor elk veld met een lijst (doeleinden, datasets, ontvangers, beveiligingsmaatregelen enzovoort) de te behouden items aan, ongeacht uit welke verwerkingsactiviteit ze komen: ze worden gecombineerd in de referentieversie.
4. Klik op **Samenvoegen**.

<figure><img src="../../.gitbook/assets/ropa-merge-3.png" alt="Venster Samenvoeggereedschap dat twee verwerkingsactiviteiten vergelijkt"><figcaption><p>Het venster Samenvoeggereedschap</p></figcaption></figure>

Om de vergelijking te vergemakkelijken:

* elk veld waarvan de waarde van de ene verwerkingsactiviteit tot de andere verschilt, is gemarkeerd met **Different**, en een teller toont het aantal betrokken rijen;
* de tabel toont alleen de rijen die verschillen; schakel **View all fields** in om alle vergelijkbare velden weer te geven. Verborgen identieke velden behouden de waarde van de referentieversie;
* met de knop **Select all** onder de kop van een kolom behoudt u de waarden van die kolom op alle rijen die verschillen; **Undo selection** maakt dat ongedaan. Een lege waarde vervangt nooit een ingevulde waarde.

Het deel **Linked objects kept** toont hoeveel risicobeoordelingen, taken en vragenlijstantwoorden aan de samengevoegde verwerkingsactiviteiten zijn gekoppeld. Ze worden automatisch aan de referentieversie gekoppeld, zodat niets wat aan de verwijderde verwerkingsactiviteiten was gekoppeld, verloren gaat.

Zodra de samenvoeging is uitgevoerd, bevestigt een melding dit met een link **Object weergeven** om de referentieversie te openen.

{% hint style="warning" %}
De andere verwerkingsactiviteiten dan de referentieversie worden verwijderd zodra de samenvoeging is bevestigd, en dat kan niet ongedaan worden gemaakt. Controleer uw keuzes voordat u op **Samenvoegen** klikt en exporteer de verwerkingsactiviteiten vooraf als u een kopie van hun inhoud wilt bewaren.
{% endhint %}

## Duplicaten automatisch vinden

Om verwerkingsactiviteiten te identificeren die waarschijnlijk duplicaten zijn, klikt u op de pijl naast de knop **Maak een gegevensverwerking** en daarna op **Gegevenskwaliteitsinstrument**. De gedetecteerde duplicaten staan in een lijst met een betrouwbaarheidsscore en u kunt ze vanaf daar samenvoegen.

{% content-ref url="../general/merge.md" %}
[Elementen samenvoegen](../general/merge.md)
{% endcontent-ref %}

## Typische gebruiksgevallen

| Geval                           | Voorbeeld                                                                                       | Voordeel                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Stroomlijnen                    | Twee verwerkingsactiviteiten "HR-beheer" en "Personeelsbeheer"                                  | Duplicaten voorkomen en het onderhoud vereenvoudigen      |
| Reorganisatie                   | Vergelijkbare verwerkingsactiviteiten aangemaakt in meerdere organisatorische eenheden          | Eén enkele, actuele verwerkingsactiviteit behouden        |
| Harmonisatie tussen entiteiten  | Gelijkwaardige verwerkingsactiviteiten die door meerdere dochterondernemingen apart zijn gedocumenteerd | Governance en globale rapportage vergemakkelijken |
| Register opschonen              | Duplicaten die bij een eerste import zijn ontstaan                                              | De duidelijkheid en betrouwbaarheid van het register verbeteren |

## Goede praktijken

1. Controleer de compatibiliteit: voeg alleen verwerkingsactiviteiten samen met identieke of zeer verwante doeleinden.
2. Houd de juridische analyse consistent: voeg geen verwerkingsactiviteiten samen die op verschillende wettelijke bases steunen.
3. Documenteer uw beslissing: leg de redenen voor de samenvoeging uit in een interne discussie bij de referentieversie.

{% hint style="success" %}
Door verwerkingsactiviteiten samen te voegen houdt u een overzichtelijk, actueel register en beperkt u de administratieve last, terwijl u de controle behoudt over elke overgenomen waarde.
{% endhint %}
