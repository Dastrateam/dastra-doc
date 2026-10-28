---
description: Erfahren Sie, wie Sie Meldungen von Datenschutzvorfällen nachverfolgen.
---

# Datenschutzvorfälle

### 📖 Definition

Gemäß [Artikel 4.12 der DSGVO](https://dsgvo-gesetz.de/art-4-dsgvo/) ist\
ein **Datenschutzvorfall** (Verletzung des Schutzes personenbezogener Daten):

> _Eine Verletzung der Sicherheit, die, ob unbeabsichtigt oder unrechtmäßig, zur Vernichtung, zum Verlust, zur Veränderung oder zur unbefugten Offenlegung von beziehungsweise zum unbefugten Zugang zu personenbezogenen Daten führt, die übermittelt, gespeichert oder auf sonstige Weise verarbeitet wurden._

Mit anderen Worten handelt es sich um jeden **Sicherheitsvorfall**, ob **absichtlich oder versehentlich**, der Folgendes beeinträchtigt:

* die **Vertraulichkeit** (unbefugter Zugriff, Offenlegung),
* die **Integrität** (Veränderung, Fälschung),
* die **Verfügbarkeit** (Verlust, Löschung, Nichtverfügbarkeit).

***

### ⚠️ Beispiele typischer Datenschutzvorfälle

* Versehentliche Löschung medizinischer Daten ohne Sicherungskopie.
* Verlust eines unverschlüsselten USB-Sticks mit der Kundendatenbank.
* Hackerangriff auf einen Server, der E-Mail-Adressen und Passwörter offenlegt.
* Versand einer E-Mail mit personenbezogenen Daten an den falschen Empfänger.
* Leak von HR-Informationen auf einem ungesicherten gemeinsamen Speicherplatz.

***

### 🧩 Die drei Haupttypen von Datenschutzvorfällen

| Typ                 | Beschreibung                             | Beispiel                            |
| ------------------- | ---------------------------------------- | ----------------------------------- |
| **Vertraulichkeit** | Unbefugter Zugriff oder Offenlegung      | Datenleck durch Phishing            |
| **Integrität**      | Unbefugte Änderung oder Fälschung        | Veränderung einer Patientenakte     |
| **Verfügbarkeit**   | Versehentlicher Verlust oder Vernichtung | Daten ohne Sicherungskopie gelöscht |

***

### 🕓 Die gesetzlichen Pflichten des Verantwortlichen

Wenn ein Datenschutzvorfall eintritt, muss der **Verantwortliche** **unverzüglich** reagieren.

#### 1️⃣ Meldung an die Aufsichtsbehörde

* **Frist**: 72 Stunden nach Kenntnisnahme.
* **Inhalt**:
  * Art des Vorfalls,
  * Kategorien und Umfang der betroffenen Daten,
  * Voraussichtliche Folgen,
  * Ergriffene oder geplante Abhilfemaßnahmen.

> Wenn die Meldung nicht innerhalb von 72 Stunden erfolgt, muss die **Verzögerung begründet** werden.

📚 Referenz: [Artikel 33 der DSGVO](https://dsgvo-gesetz.de/art-33-dsgvo/)

***

#### 2️⃣ Information der betroffenen Personen

Wenn der Vorfall **ein hohes Risiko für die Rechte und Freiheiten darstellt**,\
müssen die betroffenen Personen **schnellstmöglich** informiert werden:

* Art des Vorfalls,
* Betroffene Daten,
* Ergriffene Maßnahmen,
* Empfehlungen zur Begrenzung der Auswirkungen (z. B.: Passwortänderung).

📚 Referenz: [Artikel 34 der DSGVO](https://dsgvo-gesetz.de/art-34-dsgvo/)

***

#### 3️⃣ Obligatorische interne Dokumentation

Auch wenn keine Meldung erforderlich ist,\
muss **jeder Vorfall** in einem internen Register erfasst werden, das enthält:

* die Fakten zum Vorfall,
* seine Auswirkungen,
* die ergriffenen Korrekturmaßnahmen.

> Dieses Register dient dem **Nachweis der Compliance** (Accountability-Prinzip).

***

### 🔁 Der Managementzyklus eines Datenschutzvorfalls

1. **Erkennung** → Identifizierung eines Vorfalls oder anomalen Verhaltens.
2. **Qualifizierung** → Prüfen, ob personenbezogene Daten betroffen sind.
3. **Risikobewertung** → Auswirkung auf die Privatsphäre der betroffenen Personen.
4. **Meldung (falls erforderlich)** → Aufsichtsbehörde innerhalb von 72h, betroffene Personen bei hohem Risiko.
5. **Abhilfe** → Korrektur- und Präventivmaßnahmen.
6. **Dokumentation** → Eintragung in das Register der Datenschutzvorfälle.
7. **Nachbereitung** → Organisatorische oder technische Anpassungen.

***

### 🧠 Bewährte Sicherheitspraktiken

* Einen **Vorfallmanagementplan** vorbereiten und regelmäßig testen.
* Die Teams in der **Erkennung und schnellen Meldung** von Vorfällen schulen.
* **Präventivmaßnahmen** einrichten (MFA, Netzwerksegmentierung, Backups).
* Ein **zentrales Register** nutzen, um jeden Vorfall und seine Behebung nachzuverfolgen.
* Die Schwere mittels einer **standardisierten Risikomatrix** bewerten (z. B. ISO 27005).

***

### 🧾 Verwaltung von Datenschutzvorfällen in Dastra

Dastra ermöglicht die **zentrale Dokumentation und Steuerung von Datenschutzvorfällen**:

| Schritt          | Dastra-Funktion                                                                     |
| ---------------- | ----------------------------------------------------------------------------------- |
| Meldung          | Anpassbares Meldeformular                                                           |
| Bewertung        | Automatische Risikoberechnung bezüglich der Betroffenenrechte                       |
| Benachrichtigung | Berichterstellung für die Aufsichtsbehörde und Kommunikation an betroffene Personen |
| Nachverfolgung   | Aktionsprotokoll und Abhilfeplan                                                    |
| Reporting        | Dashboards und Compliance-Kennzahlen                                                |

***

### 📚 Nützliche Ressourcen

* [ENISA – Data Breach Notification Guidelines](https://www.enisa.europa.eu/)
* [ISO/IEC 27035 – Management von Informationssicherheitsvorfällen](https://www.dinmedia.de/de/norm/csa-iso-iec-27035-4/400025388?queryId=2f755d5cffcb79a64986797517c3268c\&indexName=prod_dinmedia_products\&position=1)

***

{% hint style="success" %}
💡 **Gute Praxis:** Ein schnell gemeldeter Vorfall begrenzt die Auswirkungen, stärkt die Transparenz und beweist die Beherrschung der Compliance.\
Dastra hilft Ihnen, jeden Schritt des Prozesses zu strukturieren und zu dokumentieren.
{% endhint %}
