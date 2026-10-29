---
description: >-
  Leer hoe u een sjabloon voor een DPIA-vragenlijst aanmaakt of wijzigt:
  sjabloontype, gekoppeld object en de variabelenamen van het risicoplan.
---

# Een DPIA-sjabloon maken of wijzigen

Dastra heeft verschillende sjablonen voor gegevensbeschermingseffectbeoordelingen (DPIA's). U kunt ook uw eigen sjabloon maken.

{% hint style="info" %}
Begin niet vanaf nul: gebruik een bestaand sjabloon en pas het aan. Zo hebt u een uitgangspunt.
{% endhint %}

## Stap 1: het sjabloon aanmaken

Klik in de module **Audits** op **Maak een sjabloon** en daarna op **Gepersonaliseerde audit**.

<figure><img src="../../../.gitbook/assets/questionnaires-templates-2.png" alt="Venster voor het kiezen van een type sjabloon met de optie Gepersonaliseerde audit"><figcaption><p>De optie Gepersonaliseerde audit in het creatievenster</p></figcaption></figure>

## Stap 2: het sjabloon configureren

Kies in het paneel **Maak een audittemplate** de volgende opties om alle DPIA-functies te benutten.

<figure><img src="../../../.gitbook/assets/questionnaires-pia-1.png" alt="Configuratiepaneel met het DPIA-type en het gekoppelde object Verwerkingsactiviteit"><figcaption><p>De configuratie van een DPIA-sjabloon</p></figcaption></figure>

* **Type audit**: kies **Gegegevensefffectbeoordeling (Data Protection Impact Assessement)**, het DPIA-type zoals de Nederlandse toepassing het toont (in het Engels Privacy impact assessment (DPIA)).

{% hint style="info" %}
Het DPIA-type toont de elementen die specifiek zijn voor DPIA's, in het bijzonder de heatmap in het dashboard van de vragenlijst, en brengt de gegevens van de verwerkingsactiviteit in wanneer de DPIA wordt gegenereerd. Het maakt het ook mogelijk DPIA's in JSON-indeling te importeren uit de PIA-tool van de CNIL.
{% endhint %}

* **Geauditeerd element**: kies de verwerkingsactiviteit. Uw DPIA-vragenlijst wordt dan aan een verwerkingsactiviteit gekoppeld en u vindt de DPIA terug vanuit die verwerkingsactiviteit. Bovendien wordt de **Datum laatste DPIA** van de verwerkingsactiviteit automatisch bijgewerkt wanneer de DPIA wordt gepubliceerd: wanneer de vragenlijst wordt afgerond als de beoordelingsstap is uitgeschakeld, anders wanneer ze wordt gevalideerd.

## Stap 3: de variabelenamen bepalen

Sjablonen van het type DPIA voeden twee soorten elementen:

* risicoanalyses (initiële impact en waarschijnlijkheid, residuele impact en waarschijnlijkheid);
* herstelacties.

Om het resultaatrapport van de DPIA te kunnen tonen, geeft u de variabelen van de secties (veld **Link (slug)**) en van de vragen (veld **Vraag-ID (slug)**) een naam volgens onderstaand plan. Het plan volgt het sjabloon PIA (CNIL) uit de bibliotheek, dat drie beveiligingsrisico's heeft. Elk risico heeft twee secties: de sectie van het initiële risico en de sectie van het residuele risico, waarvan de naam begint met `pia_todo_`.

<figure><img src="../../../.gitbook/assets/questionnaires-pia-2.png" alt="Venster Sectie configureren met het label Verdwijnen van gegevens en de slug pia_34"><figcaption><p>De slug van de sectie Verdwijnen van gegevens</p></figcaption></figure>

| Sectie of vraag | Variabele | Type |
| --- | --- | --- |
| Onrechtmatige toegang tot gegevens (risico 3.2) | `pia_32` | Sectie |
| Bestaande maatregelen | `pia_324` | Dynamische meerkeuzeselector |
| Initiële ernst (impact) | `pia_325` | Keuze met score |
| Initiële waarschijnlijkheid | `pia_326` | Keuze met score |
| Onrechtmatige toegang: residueel risico | `pia_todo_32` | Sectie |
| Geplande maatregelen (herstel) | `pia_todo_324` | Dynamische meerkeuzeselector |
| Details van het actieplan | `pia_todo_321` | Rich text (teksteditor) |
| Residuele ernst (impact) | `pia_todo_325` | Keuze met score |
| Residuele waarschijnlijkheid | `pia_todo_326` | Keuze met score |
| Ongewenste wijziging van gegevens (risico 3.3) | `pia_33` | Sectie |
| Verdwijnen van gegevens (risico 3.4) | `pia_34` | Sectie |

Gebruik voor de risico's 3.3 en 3.4 dezelfde structuur en vervang `32` in alle namen door `33` of `34`, ook in `pia_todo_`. Gebruik voor een extra risico het volgende nummer (`pia_35`, `pia_todo_35` enzovoort). In het CNIL-sjabloon hebben de vragen over ernst en waarschijnlijkheid een score van 0 tot 4.
