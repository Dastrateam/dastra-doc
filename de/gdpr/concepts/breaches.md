---
description: Erfahren Sie, wie Sie Meldungen von Datenschutzverletzungen verwalten.
---

# Meldung von Datenschutzverletzungen

## Definition

Nach [Artikel 4 Nummer 12 der DSGVO](https://dsgvo-gesetz.de/art-4-dsgvo/) ist eine **Verletzung des Schutzes personenbezogener Daten**:

> _Eine Verletzung der Sicherheit, die, ob unbeabsichtigt oder unrechtmäßig, zur Vernichtung, zum Verlust, zur Veränderung, oder zur unbefugten Offenlegung von beziehungsweise zum unbefugten Zugang zu personenbezogenen Daten führt, die übermittelt, gespeichert oder auf sonstige Weise verarbeitet wurden._

Anders gesagt: Jeder **Sicherheitsvorfall**, ob **absichtlich oder unbeabsichtigt**, der Folgendes beeinträchtigt, ist eine Datenschutzverletzung:

* die **Vertraulichkeit** (unbefugter Zugriff, Offenlegung),
* die **Integrität** (Veränderung, Fälschung),
* die **Verfügbarkeit** (Verlust, Löschung, Nichtverfügbarkeit).

***

## Typische Beispiele

* Versehentliches Löschen von medizinischen Daten, die nirgendwo sonst gespeichert sind.
* Verlust eines unverschlüsselten USB-Sticks mit einer Kundendatenbank.
* Hackerangriff auf einen Server, bei dem E-Mail-Adressen und Passwörter offengelegt werden.
* E-Mail mit personenbezogenen Daten, die an den falschen Empfänger geschickt wird.
* Personalinformationen, die in einem ungesicherten gemeinsamen Bereich offengelegt werden.

***

## Drei Haupttypen von Datenschutzverletzungen

| Typ | Beschreibung | Beispiel |
| --- | --- | --- |
| **Vertraulichkeit** | Unbefugter Zugriff oder unbefugte Offenlegung | Offenlegung durch Phishing |
| **Integrität** | Unbefugte Änderung oder Fälschung | Veränderung einer Patientenakte |
| **Verfügbarkeit** | Versehentlicher Verlust oder versehentliche Vernichtung | Daten ohne Backup gelöscht |

***

## Gesetzliche Pflichten des Verantwortlichen

### Meldung an die Aufsichtsbehörde

* **Frist**: wenn möglich binnen 72 Stunden, nachdem die Verletzung bekannt wurde. Eine Meldung ist nicht erforderlich, wenn die Verletzung voraussichtlich nicht zu einem Risiko für die Rechte und Freiheiten von Personen führt.
* **Inhalt**:
  * Art der Verletzung,
  * Kategorien und Umfang der betroffenen Daten,
  * wahrscheinliche Folgen,
  * ergriffene oder geplante Maßnahmen.

> Kann die Meldung nicht binnen 72 Stunden erfolgen, muss die **Verzögerung begründet werden**.

Referenz: [Artikel 33 der DSGVO](https://dsgvo-gesetz.de/art-33-dsgvo/)

***

### Benachrichtigung der betroffenen Personen

Wenn die Verletzung **voraussichtlich ein hohes Risiko für die Rechte und Freiheiten von Personen zur Folge hat**, müssen diese **unverzüglich** informiert werden:

* Art der Verletzung,
* betroffene Daten,
* ergriffene Maßnahmen,
* Empfehlungen, um die Folgen zu begrenzen (zum Beispiel das Passwort ändern).

Referenz: [Artikel 34 der DSGVO](https://dsgvo-gesetz.de/art-34-dsgvo/)

***

### Verpflichtende interne Dokumentation

Auch wenn keine Meldung erforderlich ist, **muss jede Verletzung** in einem internen Verzeichnis **erfasst werden**, das Folgendes enthält:

* die Fakten zur Verletzung,
* ihre Auswirkungen,
* die ergriffenen Abhilfemaßnahmen.

> Dieses Verzeichnis **weist die Einhaltung der Vorschriften nach** (Grundsatz der Rechenschaftspflicht).

***

## Der Managementzyklus einer Datenschutzverletzung

1. **Erkennung** → Feststellung eines Vorfalls oder eines ungewöhnlichen Verhaltens.
2. **Einstufung** → Prüfen, ob personenbezogene Daten betroffen sind.
3. **Risikobewertung** → Auswirkung auf die Privatsphäre der Personen.
4. **Meldung (falls erforderlich)** → Aufsichtsbehörde binnen 72 Stunden, betroffene Personen bei hohem Risiko.
5. **Abhilfe** → Korrektur- und Vorbeugungsmaßnahmen.
6. **Dokumentation** → Eintrag in das Verzeichnis der Datenschutzverletzungen.
7. **Erkenntnisse** → organisatorische oder technische Anpassungen.

***

## Bewährte Sicherheitspraktiken

* Erstellen Sie einen **Plan für das Vorfallmanagement** und testen Sie ihn regelmäßig.
* Schulen Sie Ihre Teams in der **schnellen Erkennung und Eskalation** von Vorfällen.
* Setzen Sie **Vorbeugungsmaßnahmen** um (MFA, Netzwerksegmentierung, Backups).
* Verwenden Sie ein **zentrales Verzeichnis**, um jede Verletzung und ihre Lösung zu verfolgen.
* Bewerten Sie den Schweregrad mit einem **standardisierten Risikoraster** (zum Beispiel einem von Ihrer Aufsichtsbehörde veröffentlichten oder ISO/IEC 27005).

***

## Datenschutzverletzungen in Dastra verwalten

Das Modul **Vorfälle** von Dastra dokumentiert und verfolgt Verletzungen des Schutzes personenbezogener Daten:

| Schritt | Dastra-Funktion |
| --- | --- |
| Meldung | Datensatz der Verletzung im Verzeichnis der Vorfälle |
| Bewertung | Risikostufe, berechnet aus der Wahrscheinlichkeit der Identifizierung und der Schwere der Folgen |
| Benachrichtigung | Nachverfolgung der Meldung an die Behörde (Countdown von 72 Stunden) und der Benachrichtigung der betroffenen Personen |
| Überwachung | Zugehörige Aufgaben, nach dem Vorfall beschlossene Maßnahmen, Post-Mortem und Verlauf |
| Reporting | Seite **Statistiken** mit Kennzahlen zu Vorfällen |

***

## Nützliche Ressourcen

* [ICO: reporting a data breach](https://ico.org.uk/for-organizations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/personal-data-breaches/) (auf Englisch)
* [ENISA: die EU-Agentur für Cybersicherheit](https://www.enisa.europa.eu/)
* [ISO/IEC 27035: information security incident management](https://www.iso.org/standard/60803.html) (auf Englisch)

***

{% hint style="success" %}
**Bewährte Praxis:** Ein schnell gemeldeter Vorfall begrenzt die Auswirkungen, stärkt die Transparenz und belegt, dass Sie die Vorschriften beherrschen. Dastra hilft Ihnen, jeden Schritt des Prozesses zu strukturieren und zu dokumentieren.
{% endhint %}

***

## Weiterführende Informationen

{% content-ref url="../../features/incidents/README.md" %}
[Datenschutzvorfälle](../../features/incidents/README.md)
{% endcontent-ref %}

{% content-ref url="../../features/incidents/document-breach.md" %}
[Einen neuen Datenschutzvorfall dokumentieren](../../features/incidents/document-breach.md)
{% endcontent-ref %}
