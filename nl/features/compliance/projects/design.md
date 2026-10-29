---
description: >-
  De ontwerpfase is het vertrekpunt van uw conformiteitsproject.
---

# Projectontwerp

In de fase **Design** bepaalt u de **organisatorische perimeter** van het project, selecteert u de **toepasselijke kaders** en initialiseert u automatisch de bijbehorende controles, tests en risico's.

Deze stap legt de basis van het project en bepaalt de kwaliteit van de opvolging in de volgende fasen. Voor een overzicht van de fasen, zie [Projecten](README.md).

***

<figure><img src="../../../.gitbook/assets/image-432.png" alt="De fasen van het conformiteitsproject, met de fase Perimeter in uitvoering"><figcaption></figcaption></figure>

## 1. Het project aanmaken en de perimeter bepalen

Bij het aanmaken van het project moet u een **organisatorische perimeter** selecteren.\
De perimeter groepeert een of meer organisatorische eenheden en bepaalt **het toepassingsgebied van het conformiteitsproject**.

{% columns %}
{% column %}
Zodra het project is aangemaakt, wordt de perimeter weergegeven in de projectkop en gebruikt tijdens de hele conformiteitscyclus.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-490.png" alt="Venster voor het aanmaken van een project met de titel en de perimeter"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## 2. Gebruikers aan het project toewijzen

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image-491.png" alt="Venster voor het aanmaken van een project met de toewijzing van gebruikers"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
In de ontwerpfase wijst u ook **de gebruikers aan die het project mogen beheren**.

* U kunt aan elke gebruiker een rol toewijzen: **Goedkeurder** of **Op de hoogte**.
* Deze gebruikers mogen de controles, tests en audits van het project aansturen.
{% endcolumn %}
{% endcolumns %}

***

<figure><img src="../../../.gitbook/assets/image-433.png" alt="De fasen van het conformiteitsproject, met de fase Design"><figcaption></figcaption></figure>

## 3. Conformiteitskaders toevoegen

Een conformiteitsproject steunt op een of meer **kaders** (normen, interne of aangepaste referentiekaders).

Door een kader toe te voegen importeert u:

* de **vereisten**,
* de **controles**,
* de **tests**,
* en de bijbehorende **risico's**.

<figure><img src="../../../.gitbook/assets/image-434.png" alt="Selectie van een kader om aan het project toe te voegen"><figcaption></figcaption></figure>

Alleen de gepubliceerde versies van een kader worden aangeboden. Als er meerdere gepubliceerde versies bestaan, kiest u de versie in de lijst **Te installeren versie** naast de naam van het kader. De huidige versie is vooraf geselecteerd.

Het project blijft gekoppeld aan de geïnstalleerde versie. Wanneer dat niet meer de huidige versie is, toont de kaderkaart in het projectoverzicht de badge **Beschikbare update**. U schakelt handmatig over naar een andere versie met de actie **Werk de versie van het framework bij**. Dat is niet mogelijk zolang er een audit loopt in het project (zie [Versies van een kader](../library/frameworks/versions.md)).

U kunt achtereenvolgens meerdere kaders aan hetzelfde project toevoegen.

***

## 4. Controles delen tussen kaders

Wanneer u meerdere kaders aan het project toevoegt, detecteert Dastra automatisch de **gemeenschappelijke controles**.

* Een controle die door meerdere kaders wordt gedeeld, **wordt maar één keer geïmporteerd**.
* De invoering ervan dekt tegelijk alle bijbehorende vereisten.
* Zo vergroot u de conformiteitsdekking zonder acties te vermenigvuldigen.

<figure><img src="../../../.gitbook/assets/image-435.png" alt="Import van de controles die tussen meerdere kaders worden gedeeld"><figcaption></figcaption></figure>

***

## 5. De te importeren controles selecteren

Wanneer u een kader toevoegt, hebt u meerdere opties:

* **alle controles** van het kader importeren,
* **alleen bepaalde controles** importeren,
* of **geen controles importeren**, om ze handmatig in te voeren.

<figure><img src="../../../.gitbook/assets/image-437.png" alt="Keuze van de controles die met het kader worden geïmporteerd"><figcaption></figcaption></figure>

Dankzij deze flexibiliteit stemt u het project af op de maturiteit van de organisatie.

***

## 6. Controles en tests initialiseren

{% columns %}
{% column %}
Zodra de kaders zijn geïmporteerd:

* worden de **geselecteerde controles** automatisch aan het project toegevoegd,
* gelden ze **standaard als ingevoerd**,
* worden de **bijbehorende tests** ook aan de controles gekoppeld.

In dit stadium:

* hebben de tests de status **Ontbrekend bewijs**,
* is er nog geen bewijs verzameld.
{% endcolumn %}

{% column %}
<div align="center"><img src="../../../.gitbook/assets/image-438.png" alt="Projectoverzicht met de geïmporteerde kaders"></div>
{% endcolumn %}
{% endcolumns %}

***

## 7. De risicoanalyse voorbereiden

U kunt tijdens het importeren de **risico's van de kaders** selecteren.

Ze vormen:

* de basis voor de **initiële risicobeoordeling**,
* het referentiepunt voor de berekening van het **restrisico** na toepassing van de controles.

<figure><img src="../../../.gitbook/assets/image-439.png" alt="Risicomatrix van het project"><figcaption></figcaption></figure>

***

## Een kader uit het project verwijderen

Op het tabblad **Statistieken** van het project biedt het menu **⋯** van een kaderkaart de actie **Verwijder het framework**. Dastra verwijdert dan uit het project de controles, tests, risico's en bedreigingen die alleen aan dat kader zijn gekoppeld. Een controle die het project nog via een ander kader toepast, blijft behouden.

Verwijderen is niet mogelijk zolang een audit van dat kader niet is gearchiveerd (zie [Audits](audits.md)).

***

## Resultaat van de ontwerpfase

Na de ontwerpfase heeft het project:

* een duidelijk bepaalde perimeter,
* aangewezen eigenaars,
* de toepasselijke geïmporteerde kaders,
* gedeelde controles die klaar zijn voor opvolging,
* geïnitialiseerde tests,
* en een gestructureerde risicobasis.

Het project is dan klaar voor de volgende fase: **Implementatie**.
